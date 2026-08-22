#!/usr/bin/env python3
"""Turn a screened market row into a site directory the builder can render.

Reads the 83 verified markets, picks an available domain for each, merges the
niche structure pack, and writes sites/<domain>/site.json plus a copy.md stub
listing every block a writer has to fill in.

It never invents a local fact and never writes prose. Copy is written per city
by a human or a writing pass -- this only builds the frame and records what is
still missing, so `python3 scaffold.py --status` always tells the truth about
how much of the portfolio is actually finished.
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent
MARKETS = pathlib.Path("/home/user/workspace/screen/m83.json")

# Markets already built by hand keep the domain they were built on, so the
# scaffolder never forks a second site for the same city and trade.
EXISTING = {"garage door repair naperville": "garagedoorrepairnapervillepros.com"}
NICHES = ROOT / "niches"
SITES = ROOT / "sites"

# Every copy.md block the builder requires. Kept here so --status can report a
# real completion percentage instead of a guess.
BLOCKS = [
    "meta_title", "meta_description", "hero_promise",
    "what_happens_when_you_call", "what_they_will_ask",
    *[f"symptom_{i}{s}" for i in (1, 2, 3, 4) for s in ("_title", "")],
    *[f"qa_{i}{s}" for i in (1, 2, 3) for s in ("_question", "_answer")],
    "closing_cta", "services_summary", "about_summary",
    *[f"value_{i}{s}" for i in (1, 2, 3, 4) for s in ("_title", "")],
    *[f"step_{i}{s}" for i in (1, 2, 3) for s in ("_title", "")],
    "expect_intro_1", "expect_intro_2",
    *[f"expect_{i}{s}" for i in (1, 2, 3, 4) for s in ("_label", "")],
    *[f"factor_{i}{s}" for i in (1, 2, 3, 4) for s in ("_title", "")],
    # Band headings and the footer safety note. Authored per site so no niche
    # language is baked into the shared template and no two sites share chrome.
    "urgency_bullet", "values_eyebrow", "values_head", "values_lede",
    "factors_lede", "problem_lede", "problem_nudge", "expect_eyebrow", "expect_head",
    "emergency_note",
]

# Blocks only a phase-2 site needs, because they head bands that phase 1 does
# not render at all.
PHASE2_BLOCKS = ["services_summary", "services_pick_head", "crosslink_head"]

STATE_ABBR = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
    "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE",
    "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID",
    "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
    "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
    "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN",
    "Mississippi": "MS", "Missouri": "MO", "Montana": "MT", "Nebraska": "NE",
    "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ",
    "New Mexico": "NM", "New York": "NY", "North Carolina": "NC",
    "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK", "Oregon": "OR",
    "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
    "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT",
    "Vermont": "VT", "Virginia": "VA", "Washington": "WA",
    "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY",
}

TZ = {
    "CA": "America/Los_Angeles", "WA": "America/Los_Angeles",
    "OR": "America/Los_Angeles", "NV": "America/Los_Angeles",
    "AZ": "America/Phoenix", "UT": "America/Denver", "CO": "America/Denver",
    "NM": "America/Denver", "MT": "America/Denver", "ID": "America/Denver",
    "WY": "America/Denver",
    "TX": "America/Chicago", "IL": "America/Chicago", "MN": "America/Chicago",
    "WI": "America/Chicago", "IA": "America/Chicago", "MO": "America/Chicago",
    "AR": "America/Chicago", "LA": "America/Chicago", "OK": "America/Chicago",
    "KS": "America/Chicago", "NE": "America/Chicago", "SD": "America/Chicago",
    "ND": "America/Chicago", "MS": "America/Chicago", "AL": "America/Chicago",
    "TN": "America/Chicago",
}


def title_city(c):
    """virginia beach -> Virginia Beach, and keep the odd ones readable."""
    small = {"of", "and", "the"}
    return " ".join(w if w in small else w.capitalize() for w in c.split())


def brand_for(city, service):
    """A believable local brand with no company name we do not own."""
    s = service.replace(" Lawyer", " Law").replace(" Attorney", " Law")
    return f"{city} {s} Pros"


def pick_domain(row):
    """Prefer the shortest available domain that leads with the city."""
    free = row.get("free") or []
    if not free:
        return None
    city = row["city"].replace(" ", "")
    lead = [d for d in free if d.lower().startswith(city)]
    return sorted(lead or free, key=len)[0]


def niche_slug(seed):
    return seed.lower().replace(" ", "-")


def load_pack(seed):
    p = NICHES / f"{niche_slug(seed)}.json"
    return json.loads(p.read_text()) if p.exists() else None


def build_site(row, pack):
    city = title_city(row["city"])
    state = STATE_ABBR[row["state_full"]]
    ac = row["area_codes"][0]
    return {
        "domain": pick_domain(row),
        # Phase 1 = home + about + contact, which is what goes live and gets
        # ranked. The four service pages are phase 2, added per market once it
        # is earning. site.json still carries the service definitions now so
        # phase 2 is purely a writing job later, not a config job.
        "phase": 1,
        "brand": brand_for(city, pack["service"]),
        "service": pack["service"],
        "service_inline": pack["service_inline"],
        "city": city,
        "state": state,
        "state_full": row["state_full"],
        "counties": row["counties"],
        "area_codes": row["area_codes"],
        # A reserved-for-fiction 555-01XX number, so nothing dials a real
        # stranger while the site is still a draft. The build WARNs on this
        # until a live Telnyx number in the right area code replaces it.
        "phone_display": f"({ac}) 555-0100",
        "phone_tel": f"+1{ac}5550100",
        "phone_status": "PLACEHOLDER",
        "phone_note": (
            f"Reserved 555-01XX fictional range. Replace with a real Telnyx "
            f"{ac} number before this domain resolves publicly."
        ),
        "emergency": pack["emergency"],
        "timezone": TZ.get(state, "America/New_York"),
        "tenant": {
            "status": "none", "business_name": None, "license_number": None,
            "years_in_business": None, "reviews": None, "service_hours": None,
            "family_owned": None, "veteran_owned": None,
        },
        # Deliberately empty. Three sourced, city-specific facts are required
        # before the build passes. Nothing here may be guessed.
        "local_facts": [],
        "neighborhoods": [],
        "symptoms": pack["symptoms"],
        "schema": {
            "local_business": False,
            "local_business_reason": (
                "No tenant signed. Emitting LocalBusiness markup with no "
                "verifiable business behind it is a fabrication."
            ),
        },
        "hero_accent": pack["hero_accent"],
        "trust_third": pack["trust_third"],
        "services": pack["services"],
        "symptom_service": pack["symptom_service"],
        "_market": {
            "keyword": row["kw"], "monthly_price": row["price"],
            "score": row["sc"], "volume": row["vol"], "cpc_usd": row["cpc"],
            "weakest_competitor": row["lead"], "competitor_dr": row["dr"],
        },
    }


def copy_stub(site):
    """A writer's worksheet: every block, in order, with the rules at the top."""
    phase = site.get("phase", 1)
    svc_blocks = []
    if phase == 2:
        for o in site["services"]:
            k = o["slug"].replace("-", "_")
            svc_blocks += [f"svc_{k}_lede", f"svc_{k}_body"]
    blocks = [b for b in BLOCKS if b not in PHASE2_BLOCKS]
    if phase == 2:
        blocks += PHASE2_BLOCKS
    scope = (["- Home page lands 1,300-2,300 visible words. Each service page 900-1,500.",
              "- symptom_N blocks are 40-80 word teasers only. The depth goes on the",
              "  service page they link to."] if phase == 2 else
             ["- PHASE 1: this site is home + about + contact only. No service pages.",
              "- Home page lands 1,700-3,200 visible words.",
              "- symptom_N blocks are 200-360 words each. In phase 1 the card IS the",
              "  coverage of that problem, so give it the full explanation."])
    lines = [
        f"# Copy — {site['domain']}",
        "",
        f"**{site['service']} in {site['city']}, {site['state']}** · "
        f"target keyword `{site['_market']['keyword']}`",
        "",
        "## RULES",
        "",
        "- Write for this city. Every block must be unreusable on another site.",
        "  The build fails if any 15 consecutive words match another site.",
        "- Never promise a phone consultation. Sell the work: what gets fixed,",
        "  what it costs, when someone arrives.",
        "- Never name a business, a licence, a review count, a price or a year",
        "  in business. No tenant is signed, so none of it is true yet.",
        *scope,
        "- site.json needs 3 local_facts with a real source URL each, and 6",
        "  neighbourhoods, before this will build.",
        "",
        "---",
        "",
    ]
    for b in blocks + svc_blocks:
        lines += [f"## {b}", "", "TODO", ""]
    return "\n".join(lines)


def scaffold(force=False):
    rows = json.loads(MARKETS.read_text())
    made, skipped, nopack = [], [], {}
    for row in rows:
        pack = load_pack(row["seed"])
        if not pack:
            nopack.setdefault(row["seed"], 0)
            nopack[row["seed"]] += 1
            continue
        site = build_site(row, pack)
        if row["kw"] in EXISTING:
            site["domain"] = EXISTING[row["kw"]]
        d = SITES / site["domain"]
        if d.exists() and not force:
            skipped.append(site["domain"])
            continue
        (d / "assets").mkdir(parents=True, exist_ok=True)
        (d / "site.json").write_text(json.dumps(site, indent=2) + "\n")
        if not (d / "copy.md").exists():
            (d / "copy.md").write_text(copy_stub(site))
        made.append(site["domain"])
    print(f"scaffolded {len(made)}  |  already present {len(skipped)}")
    if nopack:
        print("\nno niche pack yet, so these markets were not scaffolded:")
        for k, v in sorted(nopack.items(), key=lambda x: -x[1]):
            print(f"  {v:3d}  {k}   (write niches/{niche_slug(k)}.json)")
    return made


def status():
    """Honest completion report. TODO blocks and empty facts both count."""
    rows = []
    for d in sorted(SITES.iterdir()):
        if not (d / "site.json").exists():
            continue
        s = json.loads((d / "site.json").read_text())
        cm = (d / "copy.md").read_text() if (d / "copy.md").exists() else ""
        blocks = re.findall(r"^## (\S+)[ \t]*\n(.*?)(?=\n## |\Z)", cm,
                            re.S | re.M)
        total = len(blocks)
        done = sum(1 for _, v in blocks if v.strip() and v.strip() != "TODO")
        rows.append({
            "domain": d.name,
            "price": s.get("_market", {}).get("monthly_price", 0),
            "copy": f"{done}/{total}" if total else "0/0",
            "pct": round(100 * done / total) if total else 0,
            "facts": len(s.get("local_facts", [])),
            "hoods": len(s.get("neighborhoods", [])),
            "photos": len(list((d / "assets").glob("*.jpg"))),
            "phone": "live" if s.get("phone_status") != "PLACEHOLDER" else "placeholder",
        })
    ready = [r for r in rows if r["pct"] == 100 and r["facts"] >= 3
             and r["hoods"] >= 6 and r["photos"] >= 4]
    print(f"{'domain':52} {'copy':>8} {'%':>4} {'facts':>6} {'hoods':>6} "
          f"{'photos':>7} {'$/mo':>6}")
    for r in sorted(rows, key=lambda x: (-x["pct"], -x["price"])):
        print(f"{r['domain']:52} {r['copy']:>8} {r['pct']:>4} {r['facts']:>6} "
              f"{r['hoods']:>6} {r['photos']:>7} {r['price']:>6}")
    mo = sum(r["price"] for r in rows)
    print(f"\n{len(rows)} sites scaffolded · {len(ready)} buildable · "
          f"${mo:,}/mo modelled · ${mo * 12:,}/yr")
    print(f"copy blocks written: {sum(int(r['copy'].split('/')[0]) for r in rows)}"
          f" of {sum(int(r['copy'].split('/')[1]) for r in rows)}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="overwrite site.json (never touches copy.md)")
    a = ap.parse_args()
    if a.status:
        status()
    else:
        scaffold(force=a.force)
        print()
        status()
