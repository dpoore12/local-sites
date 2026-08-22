#!/usr/bin/env python3
"""Domain ownership ledger.

The registrar dashboard is the truth for what we own, but it is not in the repo
and nobody can diff it. This script rewrites DOMAINS.csv + the table in
DOMAINS.md so the repo always carries a checked-in, reviewable record of what is
registered, who holds it, and what is wired up.

Two inputs, in order of authority:

1. ``data/registrar-snapshot.json`` -- a snapshot of the Cloudflare
   Registrar account produced by ``cf_sync.py``. This is the only source that
   proves a name is *ours* rather than merely taken, and it carries the real
   expiry and auto-renew flags off the registrar.
2. Verisign RDAP -- a public second opinion, used for any name missing from the
   snapshot. HTTP 404 means unregistered, HTTP 200 means someone holds it. A 200
   alone is not proof that we hold it, so a name that is registered but absent
   from the Cloudflare snapshot is flagged as possibly lost, never accepted
   quietly.

    python3 cf_sync.py            # refresh the registrar snapshot (needs the token)
    python3 domains.py            # refresh the ledger
    python3 domains.py --check    # exit 1 if the ledger is stale (for CI)
"""
import csv
import json
import pathlib
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).parent
SCREEN = ROOT / "data" / "markets.json"
CF_SNAPSHOT = ROOT / "data" / "registrar-snapshot.json"
CSV_PATH = ROOT / "DOMAINS.csv"
MD_PATH = ROOT / "DOMAINS.md"
RDAP = "https://rdap.verisign.com/com/v1/domain/{}"

# Cloudflare at-cost .com, taken off a real renewal screen on 2026-08-22.
# Verisign raises the wholesale rate on 2026-11-01; names registered before then
# bill at the old rate for the whole term.
PRICE = 10.46


def cf_snapshot():
    """-> {domain: registrar record}. Empty dict if the snapshot is missing."""
    if not CF_SNAPSHOT.exists():
        return {}
    try:
        return json.load(open(CF_SNAPSHOT))
    except Exception:                                         # noqa: BLE001
        return {}


def probe(domain):
    """-> (state, registered_on). state is 'registered' | 'available' | 'unknown'."""
    try:
        raw = urllib.request.urlopen(RDAP.format(domain), timeout=25).read().decode()
        m = re.search(r'"registration"[^}]*?"eventDate":"(\d{4}-\d{2}-\d{2})', raw)
        return "registered", (m.group(1) if m else "")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return "available", ""
        return "unknown", f"http {e.code}"
    except Exception as e:                                    # noqa: BLE001
        return "unknown", type(e).__name__


def site_written(domain):
    """Same bar `scaffold.py --status` calls buildable, read from source.

    Deliberately not `dist/` -- that directory is gitignored, so a CI checkout
    would see zero finished sites and `--check` would fail every run.
    """
    d = ROOT / "sites" / domain
    if not (d / "site.json").exists() or not (d / "copy.md").exists():
        return False, ""
    meta = json.loads((d / "site.json").read_text())
    blocks = re.findall(r"^## (\S+)[ \t]*\n(.*?)(?=\n## |\Z)",
                        (d / "copy.md").read_text(), re.S | re.M)
    filled = blocks and all(v.strip() and v.strip() != "TODO" for _, v in blocks)
    done = bool(filled
                and len(meta.get("local_facts", [])) >= 3
                and len(meta.get("neighborhoods", [])) >= 6
                and len(list((d / "assets").glob("*.jpg"))) >= 4)
    phone = meta.get("phone", "")
    if meta.get("phone_status") == "PLACEHOLDER":
        phone = ""
    return done, phone


def rows():
    markets = json.load(open(SCREEN))
    cf = cf_snapshot()

    # Keep whatever we already knew so a transient RDAP failure cannot quietly
    # downgrade a domain we have already paid for, and so the hand-maintained
    # columns (phone, tenant, hosting) survive a refresh.
    prior = {}
    if CSV_PATH.exists():
        prior = {r["domain"]: r for r in csv.DictReader(open(CSV_PATH))}

    # Only names the registrar does not vouch for need a public lookup.
    unproven = [m["domain"] for m in markets if m["domain"] not in cf]
    probes = {}
    if unproven:
        with ThreadPoolExecutor(8) as ex:
            probes = dict(zip(unproven, ex.map(probe, unproven)))

    out = []
    for m in sorted(markets, key=lambda r: -r["rent"]):
        d = m["domain"]
        was = prior.get(d, {})
        rec = cf.get(d)

        if rec:
            state = "registered"
            when = (rec.get("created_at") or "")[:10]
            expires = (rec.get("expires_at") or "")[:10]
            renew = "yes" if rec.get("auto_renew") else "NO"
            ours = "yes"
        else:
            state, when = probes.get(d, ("unknown", "not probed"))
            expires, renew = "", ""
            if state == "unknown" and was.get("status") == "registered":
                state, when = "registered", was.get("registered_on", "")
                expires = was.get("expires_on", "")
                renew = was.get("auto_renew", "")
            # Registered but not in our registrar account: either someone else
            # took it or the snapshot is stale. Needs a human either way.
            ours = was.get("ours", "") if state == "registered" else ""

        written, phone = site_written(d)
        out.append({
            "domain": d,
            "city": m["city"],
            "state_code": m["state"],
            "service": m["service"],
            "rent_month": m["rent"],
            "status": state,
            "registered_on": when,
            "expires_on": expires,
            "auto_renew": renew,
            "ours": ours,
            "site_written": "yes" if written else "",
            # site.json is the truth for the number; the CSV only carries it
            # forward so the ledger reads the same as the site ships.
            "phone": phone or was.get("phone", ""),
            "tenant": was.get("tenant", ""),
            "hosting": was.get("hosting", ""),
        })
    return out


FIELDS = ["domain", "city", "state_code", "service", "rent_month", "status",
          "registered_on", "expires_on", "auto_renew", "ours", "site_written",
          "phone", "tenant", "hosting"]


def write_csv(data):
    with open(CSV_PATH, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(data)


def write_md(data):
    ours = [r for r in data if r["ours"] == "yes"]
    disputed = [r for r in data if r["status"] == "registered" and r["ours"] != "yes"]
    avail = [r for r in data if r["status"] == "available"]
    odd = [r for r in data if r["status"] == "unknown"]
    live_rent = sum(r["rent_month"] for r in ours)
    all_rent = sum(r["rent_month"] for r in data)
    written = [r for r in ours if r["site_written"] == "yes"]
    no_phone = [r for r in ours if not r["phone"]]
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    L = []
    L.append("# Domains — what we own and what is still open\n")
    L.append("Generated by `python3 domains.py` on "
             f"{stamp}. Do not hand-edit the tables; edit the tenant / phone /\n"
             "hosting columns in `DOMAINS.csv` and re-run. Ownership comes from the\n"
             "Cloudflare Registrar snapshot in `data/registrar-snapshot.json`,\n"
             "refreshed by `python3 cf_sync.py`.\n")

    L.append("## Position\n")
    L.append(f"- **Ours: {len(ours)} of {len(data)}** — ${live_rent:,}/mo modelled")
    L.append(f"- Sites written and building clean: {len(written)} of {len(ours)}")
    L.append(f"- Still open to register: {len(avail)} — ${all_rent - live_rent:,}/mo modelled")
    if disputed:
        L.append(f"- **Registered but not in our account: {len(disputed)}** — "
                 "re-run `cf_sync.py`; if still absent, the market needs re-picking")
    if odd:
        L.append(f"- **Could not resolve {len(odd)}** — re-run before trusting this file")
    L.append(f"- Registrar: Cloudflare, at cost, ~${PRICE:.2f}/yr per name")
    if no_phone:
        L.append(f"- **{len(no_phone)} owned names still on a placeholder phone** — "
                 "the build warns on these and they must not be published")
    if avail:
        L.append(f"- Cost to finish the set: {len(avail)} x ${PRICE:.2f} = "
                 f"**${len(avail) * PRICE:,.2f}**")
    L.append("")
    L.append("Verisign raises the .com wholesale rate on **2026-11-01**. Anything\n"
             "registered before that date bills at the old rate for the full term.\n")

    L.append("## Ours\n")
    if ours:
        L.append("| Domain | Market | Rent | Registered | Expires | Auto-renew "
                 "| Site written | Phone | Tenant | Hosting |")
        L.append("|---|---|---:|---|---|---|---|---|---|---|")
        for r in ours:
            L.append(f"| `{r['domain']}` | {r['city']}, {r['state_code']} — {r['service']} "
                     f"| ${r['rent_month']:,} | {r['registered_on'] or '—'} "
                     f"| {r['expires_on'] or '—'} | {r['auto_renew'] or '—'} "
                     f"| {r['site_written'] or 'no'} | {r['phone'] or 'PLACEHOLDER'} "
                     f"| {r['tenant'] or 'none'} | {r['hosting'] or 'not deployed'} |")
    else:
        L.append("_None yet._")

    if avail:
        L.append("\n## Still to register\n")
        L.append("In buy order — highest modelled rent first. Sites already written are\n"
                 "marked, because those can go live the day the domain resolves.\n")
        L.append("| Domain | Market | Rent | Site written |")
        L.append("|---|---|---:|---|")
        for r in avail:
            L.append(f"| `{r['domain']}` | {r['city']}, {r['state_code']} — {r['service']} "
                     f"| ${r['rent_month']:,} | {r['site_written'] or 'no'} |")

    if disputed:
        L.append("\n## Registered, but not proven ours\n")
        L.append("Someone holds these and the Cloudflare snapshot does not list them.\n"
                 "Refresh the snapshot first; if a name is still missing, we lost it.\n")
        for r in disputed:
            L.append(f"- `{r['domain']}` — {r['city']}, {r['state_code']} — "
                     f"{r['service']} — registered {r['registered_on'] or 'unknown'}")

    if odd:
        L.append("\n## Needs a re-check\n")
        for r in odd:
            L.append(f"- `{r['domain']}` — {r['registered_on']}")

    L.append("\n## What the columns mean\n")
    L.append("- **status** — `registered` means someone holds the name, from the\n"
             "  Cloudflare snapshot where possible and Verisign RDAP otherwise.")
    L.append("- **ours** — whether *we* are that someone. Set only by the Cloudflare\n"
             "  snapshot. `registered` with an empty `ours` needs a human.")
    L.append("- **expires_on / auto_renew** — straight off the registrar. An\n"
             "  `auto_renew` of `NO` on a rented site is a revenue risk, not a detail.")
    L.append("- **site_written** — the copy exists and `template/build.py` passes it.\n"
             "  Independent of whether the domain is bought.")
    L.append("- **phone** — the tracking number on the site. `PLACEHOLDER` means the\n"
             "  build still warns and the site must not be published.")
    L.append("- **tenant** — the contractor renting it. Empty means no tenant, which\n"
             "  changes what the site is allowed to claim (see `template/LOCKED.md`).")
    L.append("- **hosting** — where it is actually served from, once deployed.\n")
    MD_PATH.write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    data = rows()
    if "--check" in sys.argv:
        before = CSV_PATH.read_text() if CSV_PATH.exists() else ""
        write_csv(data)
        if CSV_PATH.read_text() != before:
            print("DOMAINS.csv was stale and has been refreshed — commit it.")
            write_md(data)
            sys.exit(1)
        print("ledger current")
        sys.exit(0)
    write_csv(data)
    write_md(data)
    mine = sum(1 for r in data if r["ours"] == "yes")
    print(f"{mine} ours of {len(data)} -> DOMAINS.csv, DOMAINS.md")
