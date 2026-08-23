#!/usr/bin/env python3
"""Make sure every one of the 83 properties has its sitemap submitted, and report.

    python3 gsc_sitemaps.py        # submit anything missing, then print a summary
"""

import json
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
G = "https://www.googleapis.com"


def curl(method, url, tries=3):
    for n in range(tries):
        out = subprocess.run(["curl", "-s", "-w", "\n%{http_code}", "-X", method, url],
                             capture_output=True, text=True, timeout=90).stdout
        text, _, code = out.rpartition("\n")
        if code.strip().isdigit():
            return int(code.strip()), text
        time.sleep(1.5 * (n + 1))
    return 0, ""


def all_domains():
    return sorted(d for d in os.listdir(DIST)
                  if os.path.isdir(os.path.join(DIST, d)) and "." in d)


def main():
    done_path = os.path.join(ROOT, "data", "gsc_sitemaps_done.json")
    done = set(json.load(open(done_path))) if os.path.exists(done_path) else set()

    todo = [d for d in all_domains() if d not in done]
    print(f"{len(done)} already submitted, checking {len(todo)}")

    for d in todo:
        prop = f"sc-domain%3A{d}"
        sm = f"https%3A%2F%2F{d}%2Fsitemap.xml"
        code, body = curl("GET", f"{G}/webmasters/v3/sites/{prop}/sitemaps/{sm}")
        if code == 200 and "lastSubmitted" in body:
            done.add(d)
            print(f"ok       {d}")
        elif code == 404:
            pc, _ = curl("PUT", f"{G}/webmasters/v3/sites/{prop}/sitemaps/{sm}")
            time.sleep(0.8)
            code2, body2 = curl("GET", f"{G}/webmasters/v3/sites/{prop}/sitemaps/{sm}")
            if code2 == 200 and "lastSubmitted" in body2:
                done.add(d)
                print(f"sent     {d}")
            else:
                print(f"retry    {d}")
        else:
            print(f"unclear  {d}  (will retry)")
        time.sleep(1.6)

    json.dump(sorted(done), open(done_path, "w"), indent=2)
    print(f"\n{len(done)} of {len(all_domains())} sitemaps submitted")
    return 0 if len(done) == len(all_domains()) else 1


if __name__ == "__main__":
    sys.exit(main())
