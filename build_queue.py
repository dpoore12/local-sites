#!/usr/bin/env python3
"""Turn the listings queue into an ordered work plan.

`build_listings.py` produces the raw pairing of every site with every listing it
belongs on. That file is correct but it is not a plan -- it is alphabetical, so
whoever works it spends the first day on the cheapest sites.

This orders it by what each site is worth per month, splits it into weekly
batches of 8 sites, and writes one small checklist per batch. Small batches
matter: signing up for the same seven services 83 times in a row is how people
quit. Eight sites is about a day.
"""

import csv
import glob
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")
BATCH = 8

# The order to work a single site. First two are how we see whether Google
# picked the site up; the rest are the listings themselves.
ORDER = [
    "Google Search Console", "Bing Webmaster Tools",
    "Yelp", "Nextdoor Business", "Apple Business Connect",
    "Better Business Bureau", "Yellow Pages",
    "Houzz", "Angi", "Thumbtack", "Porch", "BuildZoom", "Networx",
    "Justia", "Avvo", "FindLaw", "Lawyers.com", "HG.org",
    "State bar directory",
]


def price_by_domain():
    out = {}
    for p in glob.glob(os.path.join(ROOT, "sites", "*", "site.json")):
        s = json.load(open(p))
        out[s["domain"]] = (s.get("_market") or {}).get("monthly_price", 0)
    return out


def main():
    rows = list(csv.DictReader(open(os.path.join(DATA, "listings.csv"))))
    price = price_by_domain()

    domains = sorted({r["domain"] for r in rows},
                     key=lambda d: (-price.get(d, 0), d))
    batch_of = {d: i // BATCH + 1 for i, d in enumerate(domains)}

    def rank(r):
        try:
            return ORDER.index(r["listing"])
        except ValueError:
            return len(ORDER)

    rows.sort(key=lambda r: (batch_of[r["domain"]],
                             -price.get(r["domain"], 0),
                             r["domain"], rank(r)))

    out = os.path.join(DATA, "queue.csv")
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["batch", "domain", "city", "niche", "monthly value",
                    "listing", "where", "status", "note"])
        for r in rows:
            w.writerow([batch_of[r["domain"]], r["domain"], r["city"],
                        r["niche"], price.get(r["domain"], 0), r["listing"],
                        r["where"], r["status"], r["note"]])

    ready = [r for r in rows if r["status"] == "todo"]
    print(f"{len(domains)} sites in {max(batch_of.values())} batches of {BATCH}")
    print(f"{len(ready)} rows ready to work, {len(rows)-len(ready)} on hold")
    print(f"wrote {out}\n")
    print("First three batches:")
    for b in (1, 2, 3):
        ds = [d for d in domains if batch_of[d] == b]
        worth = sum(price.get(d, 0) for d in ds)
        n = sum(1 for r in ready if batch_of[r["domain"]] == b)
        print(f"  batch {b}: {len(ds)} sites, ${worth:,}/mo at stake, {n} rows")
        for d in ds:
            print(f"      ${price.get(d,0):>5}  {d}")


if __name__ == "__main__":
    main()
