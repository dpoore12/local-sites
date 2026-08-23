#!/usr/bin/env python3
"""Check what is really in Search Console, then add and submit whatever is missing.

Every step is confirmed by reading the property back, so an empty reply from
Google is never mistaken for success.

    python3 gsc_audit.py check   # list what is present and what is missing
    python3 gsc_audit.py fix     # add the missing ones, confirming each
"""

import json
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
G = "https://www.googleapis.com"


def raw(method, url, tries=5):
    for n in range(tries):
        out = subprocess.run(["curl", "-s", "-w", "\n%{http_code}", "-X", method, url],
                             capture_output=True, text=True, timeout=120).stdout
        body, _, code = out.rpartition("\n")
        if code.strip().isdigit():
            return int(code.strip()), body
        time.sleep(2 * (n + 1))
    return 0, ""


def domains():
    return sorted(d for d in os.listdir(DIST)
                  if os.path.isdir(os.path.join(DIST, d)) and "." in d)


def present():
    """Domains Google confirms we own, read one at a time so nothing is guessed."""
    owned = set()
    for d in domains():
        prop = f"sc-domain%3A{d}"
        code, body = raw("GET", f"{G}/webmasters/v3/sites/{prop}")
        if code == 200 and "siteOwner" in body:
            owned.add(d)
        time.sleep(0.6)
    return owned


def check():
    owned = present()
    all_d = domains()
    print(f"{len(owned)} of {len(all_d)} in Search Console")
    missing = [d for d in all_d if d not in owned]
    for d in missing:
        print("  missing:", d)
    json.dump(sorted(missing), open(os.path.join(ROOT, "data", "gsc_missing.json"), "w"),
              indent=2)
    return 0 if not missing else 1


def fix():
    path = os.path.join(ROOT, "data", "gsc_missing.json")
    todo = json.load(open(path)) if os.path.exists(path) else domains()
    print(f"adding {len(todo)} site(s)")
    stuck = []
    for d in todo:
        prop = f"sc-domain%3A{d}"

        # claim ownership (harmless if already claimed)
        raw("POST", f"{G}/siteVerification/v1/webResource"
                    f"?verificationMethod=DNS_TXT&site.type=INET_DOMAIN&site.identifier={d}")
        time.sleep(0.5)

        ok = False
        for attempt in range(4):
            raw("PUT", f"{G}/webmasters/v3/sites/{prop}")
            time.sleep(1.0)
            code, body = raw("GET", f"{G}/webmasters/v3/sites/{prop}")
            if code == 200 and "siteOwner" in body:
                ok = True
                break
            time.sleep(2 * (attempt + 1))

        if not ok:
            stuck.append(d)
            print(f"FAIL {d}")
            continue

        sm = f"https%3A%2F%2F{d}%2Fsitemap.xml"
        raw("PUT", f"{G}/webmasters/v3/sites/{prop}/sitemaps/{sm}")
        time.sleep(0.8)
        code, body = raw("GET", f"{G}/webmasters/v3/sites/{prop}/sitemaps/{sm}")
        tag = "ok  " if code == 200 else "site added, sitemap pending"
        print(f"{tag} {d}")

    json.dump(sorted(stuck), open(path, "w"), indent=2)
    print(f"\n{len(todo) - len(stuck)} added, {len(stuck)} still to go")
    return 0 if not stuck else 1


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "check"
    sys.exit({"check": check, "fix": fix}.get(mode, check)())
