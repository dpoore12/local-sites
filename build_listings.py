#!/usr/bin/env python3
"""Build the listings work pack.

Two outputs:

  data/nap.csv          one row per site -- the exact name, phone, city and
                        description to type into every listing, so all 83 are
                        consistent everywhere they appear.

  data/listings.csv     the work queue: every site crossed with every listing
                        it should be on, with a status column to tick off.

Listings differ by trade, so the queue is built from the niche, not the city.
Legal sites deliberately get no professional-directory rows until a firm signs
-- those profiles describe a named attorney and cannot be filled in honestly
before then.
"""

import csv
import glob
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")

# Everyone gets these. Free, and they are the consistency signal.
UNIVERSAL = [
    ("Google Search Console", "search.google.com/search-console", "not a link -- how we see indexing"),
    ("Bing Webmaster Tools", "bing.com/webmasters", "import from Search Console in one click"),
    ("Yelp", "biz.yelp.com", "real call volume; claim only, never solicit reviews"),
    ("Yellow Pages", "yellowpages.com", "free tier"),
    ("Better Business Bureau", "bbb.org", "free listing; skip paid accreditation"),
    ("Nextdoor Business", "business.nextdoor.com", "genuinely local"),
    ("Apple Business Connect", "businessconnect.apple.com", "feeds Apple Maps and Siri"),
]

# Home-services trades only.
HOME = [
    ("Houzz", "houzz.com/pro", "followed link, free pro profile"),
    ("Angi", "angi.com/companylist", "expect sales calls"),
    ("Thumbtack", "thumbtack.com/pro", "free to list"),
    ("Porch", "porch.com/pro", "contractor directory"),
    ("BuildZoom", "buildzoom.com", "free claim"),
    ("Networx", "networx.com/contractor", "contractor directory"),
]

# Legal directories -- HELD until a firm signs.
LEGAL_HELD = [
    ("Justia", "lawyers.justia.com", "strong followed link"),
    ("Avvo", "avvo.com/claim-your-profile", "free claim"),
    ("FindLaw", "lawyers.findlaw.com", "free basic tier"),
    ("Lawyers.com", "lawyers.com", "free basic tier"),
    ("HG.org", "hg.org", "free basic tier"),
    ("State bar directory", "varies by state", "best local legal link there is"),
]

LEGAL_WORDS = ("lawyer", "attorney", "law", "accident", "injury", "dui",
               "divorce", "defense", "bite", "termination", "wrongful",
               "violence", "criminal", "family")


def niche_of(s):
    svc = (s.get("service") or "").lower()
    dom = s["domain"].lower()
    if any(w in svc or w in dom for w in LEGAL_WORDS):
        return "legal"
    return "home services"


def blurb(s):
    """The description to paste into every listing. Same words everywhere."""
    return (f"{s['brand']} connects {s['city']}, {s['state']} homeowners with "
            f"local {s['service_inline']} professionals. Call "
            f"{s['phone_display']} to describe the problem and get a price "
            f"before any work begins.")


def main():
    os.makedirs(DATA, exist_ok=True)
    sites = []
    for p in sorted(glob.glob(os.path.join(ROOT, "sites", "*", "site.json"))):
        s = json.load(open(p))
        if not os.path.isdir(os.path.join(ROOT, "dist", s["domain"])):
            continue  # not built, not live, not listed
        sites.append(s)

    nap_path = os.path.join(DATA, "nap.csv")
    with open(nap_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["domain", "niche", "business name", "phone", "phone (digits)",
                    "city", "state", "website", "service", "service area",
                    "description to paste"])
        for s in sites:
            area = ", ".join(s.get("counties") or []) or f"{s['city']} metro"
            w.writerow([s["domain"], niche_of(s), s["brand"], s["phone_display"],
                        s["phone_tel"], s["city"], s["state"],
                        f"https://{s['domain']}/", s["service"], area, blurb(s)])

    q_path = os.path.join(DATA, "listings.csv")
    rows = 0
    with open(q_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["domain", "city", "niche", "listing", "where", "status", "note"])
        for s in sites:
            n = niche_of(s)
            items = list(UNIVERSAL)
            if n == "home services":
                items += HOME
                extra = []
            else:
                extra = LEGAL_HELD
            for name, where, note in items:
                w.writerow([s["domain"], s["city"], n, name, where, "todo", note])
                rows += 1
            for name, where, note in extra:
                w.writerow([s["domain"], s["city"], n, name, where,
                            "hold until a firm signs", note])
                rows += 1

    home = sum(1 for s in sites if niche_of(s) == "home services")
    print(f"{len(sites)} sites -- {home} home services, {len(sites)-home} legal")
    print(f"wrote {nap_path}")
    print(f"wrote {q_path} ({rows} rows)")


if __name__ == "__main__":
    main()
