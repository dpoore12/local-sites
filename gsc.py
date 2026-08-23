#!/usr/bin/env python3
"""Put all 83 sites into Google Search Console and submit every sitemap.

Four phases. The DNS phase needs the Cloudflare key, everything else needs the
Google key, and they cannot be attached at the same time -- the sandbox routes
one host at a time.

    python3 gsc.py tokens    # Google key   -- ask Google for a TXT value per site
    python3 gsc.py dns       # Cloudflare key -- write those TXT records
    python3 gsc.py verify    # Google key   -- claim each site, then submit sitemap
    python3 gsc.py status    # no key needed -- where everything stands

Each site becomes a whole-domain property, which covers the plain address, the
www address and every page under both. State lives in data/gsc.json so any phase
can be re-run and picks up only what is unfinished.
"""

import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
STATE = os.path.join(ROOT, "data", "gsc.json")
G = "https://www.googleapis.com"
CF = "https://api.cloudflare.com/client/v4"
ACCOUNT = "a3bf1a13d93899d8408b9d1ea94df078"


def call(method, url, body=None, tries=4):
    cmd = ["curl", "-s", "-X", method, url]
    if body is not None:
        cmd += ["-H", "Content-Type: application/json", "-d", json.dumps(body)]
    for n in range(tries):
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=180).stdout
        if not out.strip():
            return {}                      # Google returns an empty body on success
        try:
            return json.loads(out)
        except json.JSONDecodeError:
            time.sleep(1.5 * (n + 1))
    return {"error": {"message": "unreadable response"}}


def why(r):
    e = r.get("error") or {}
    if isinstance(e, dict):
        return e.get("message") or json.dumps(e)[:120]
    return str(e)[:120]


def domains():
    return sorted(d for d in os.listdir(DIST)
                  if os.path.isdir(os.path.join(DIST, d)) and "." in d)


def load():
    if os.path.exists(STATE):
        return json.load(open(STATE))
    return {}


def save(s):
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    json.dump(s, open(STATE, "w"), indent=2, sort_keys=True)


def rec(s, d):
    return s.setdefault(d, {})


# ------------------------------------------------------------------ phases

def tokens():
    """Ask Google for the TXT value that proves we own each domain."""
    s = load()
    todo = [d for d in domains() if not rec(s, d).get("txt")]
    print(f"asking Google for {len(todo)} verification value(s)")

    def one(d):
        r = call("POST", f"{G}/siteVerification/v1/token",
                 {"verificationMethod": "DNS_TXT",
                  "site": {"type": "INET_DOMAIN", "identifier": d}})
        return d, r.get("token"), why(r)

    for d, tok, msg in (one(x) for x in todo):
        if True:
            if tok:
                rec(s, d)["txt"] = tok
                print(f"ok   {d}")
            else:
                print(f"FAIL {d:<44}{msg}")
    save(s)
    got = sum(1 for d in domains() if rec(s, d).get("txt"))
    print(f"\n{got} of {len(domains())} have a verification value")
    return 0 if got == len(domains()) else 1


def dns():
    """Write each TXT value into that domain's DNS at Cloudflare."""
    s = load()
    todo = [d for d in domains()
            if rec(s, d).get("txt") and not rec(s, d).get("dns")]
    print(f"writing {len(todo)} DNS record(s)")

    zones = {}
    page = 1
    while True:
        z = call("GET", f"{CF}/zones?per_page=50&page={page}")
        rows = z.get("result") or []
        for r in rows:
            zones[r["name"]] = r["id"]
        if len(rows) < 50:
            break
        page += 1
        time.sleep(0.5)
    print(f"found {len(zones)} domain(s) at Cloudflare")

    def one(d):
        want = s[d]["txt"]
        zid = zones.get(d)
        if not zid:
            return d, "domain not found at Cloudflare"
        time.sleep(3.0)
        have = call("GET", f"{CF}/zones/{zid}/dns_records?type=TXT&name={d}")
        for r in (have.get("result") or []):
            if want in (r.get("content") or ""):
                return d, None                      # already there
            if "google-site-verification" in (r.get("content") or ""):
                call("DELETE", f"{CF}/zones/{zid}/dns_records/{r['id']}")
        w = call("POST", f"{CF}/zones/{zid}/dns_records",
                 {"type": "TXT", "name": d, "content": want, "ttl": 60})
        if w.get("success"):
            return d, None
        msgs = "; ".join(e.get("message", "?") for e in (w.get("errors") or []))
        return d, msgs or "could not write the record"

    for d, bad in (one(x) for x in todo):
        if True:
            if bad:
                print(f"FAIL {d:<44}{bad}")
            else:
                rec(s, d)["dns"] = True
                print(f"ok   {d}")
    save(s)
    done = sum(1 for d in domains() if rec(s, d).get("dns"))
    print(f"\n{done} of {len(domains())} DNS records written")
    return 0 if done == len(domains()) else 1


def verify():
    """Claim each domain with Google, then hand it the sitemap."""
    s = load()
    todo = [d for d in domains()
            if rec(s, d).get("dns") and not rec(s, d).get("sitemap")]
    print(f"claiming and submitting {len(todo)} site(s)")

    def one(d):
        time.sleep(1.0)
        r = rec(s, d)
        if not r.get("claimed"):
            v = call("POST",
                     f"{G}/siteVerification/v1/webResource?verificationMethod=DNS_TXT",
                     {"site": {"type": "INET_DOMAIN", "identifier": d}})
            if not v.get("id") and "error" in v:
                return d, f"claim: {why(v)}"
            r["claimed"] = True

        prop = f"sc-domain:{d}"
        a = call("PUT", f"{G}/webmasters/v3/sites/{prop.replace(':', '%3A')}")
        if "error" in a:
            return d, f"add: {why(a)}"

        sm = f"https://{d}/sitemap.xml".replace(":", "%3A").replace("/", "%2F")
        m = call("PUT", f"{G}/webmasters/v3/sites/"
                        f"{prop.replace(':', '%3A')}/sitemaps/{sm}")
        if "error" in m:
            return d, f"sitemap: {why(m)}"
        r["sitemap"] = True
        return d, None

    for d, bad in (one(x) for x in todo):
        print(f"{'ok  ' if not bad else 'FAIL'} {d:<44}{bad or ''}")
    save(s)
    done = sum(1 for d in domains() if rec(s, d).get("sitemap"))
    print(f"\n{done} of {len(domains())} claimed with the sitemap submitted")
    return 0 if done == len(domains()) else 1


def status():
    s = load()
    all_d = domains()
    step = [("verification value", "txt"), ("DNS record", "dns"),
            ("claimed with Google", "claimed"), ("sitemap submitted", "sitemap")]
    for label, key in step:
        n = sum(1 for d in all_d if rec(s, d).get(key))
        print(f"{n:>3} of {len(all_d)}  {label}")
    stuck = [d for d in all_d if not rec(s, d).get("sitemap")]
    if stuck:
        print(f"\n{len(stuck)} not finished:")
        for d in stuck[:20]:
            r = rec(s, d)
            at = ("nothing yet" if not r.get("txt") else
                  "needs DNS" if not r.get("dns") else
                  "needs claiming" if not r.get("claimed") else "needs sitemap")
            print(f"  {d:<44}{at}")
    return 0


PHASES = {"tokens": tokens, "dns": dns, "verify": verify, "status": status}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in PHASES:
        print(__doc__)
        sys.exit(1)
    sys.exit(PHASES[sys.argv[1]]())
