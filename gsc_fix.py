#!/usr/bin/env python3
"""Claim, add and submit the sitemap for every site not yet confirmed in Search Console.

Truth comes from one read of the whole property list, not from per-site reads,
which throttle and give false answers.
"""

import json
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
G = "https://www.googleapis.com"


def curl(method, url, body=None, tries=3):
    cmd = ["curl", "-s", "-w", "\n%{http_code}", "-X", method, url]
    if body is not None:
        cmd += ["-H", "Content-Type: application/json", "-d", json.dumps(body)]
    for n in range(tries):
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=90).stdout
        text, _, code = out.rpartition("\n")
        if code.strip().isdigit():
            return int(code.strip()), text
        time.sleep(1.5 * (n + 1))
    return 0, ""


def all_domains():
    return sorted(d for d in os.listdir(DIST)
                  if os.path.isdir(os.path.join(DIST, d)) and "." in d)


def owned_now():
    code, body = curl("GET", f"{G}/webmasters/v3/sites")
    if code != 200:
        return None
    entries = json.loads(body).get("siteEntry", [])
    return {e["siteUrl"].replace("sc-domain:", "").rstrip("/")
            for e in entries if e["permissionLevel"] == "siteOwner"}


def run():
    owned = owned_now()
    if owned is None:
        print("could not read the property list")
        return 1
    todo = [d for d in all_domains() if d not in owned]
    print(f"{len(owned & set(all_domains()))} already confirmed, {len(todo)} to do")

    for d in todo:
        prop = f"sc-domain%3A{d}"
        vc, vb = curl("POST",
                      f"{G}/siteVerification/v1/webResource?verificationMethod=DNS_TXT",
                      {"site": {"type": "INET_DOMAIN", "identifier": d}})
        if vc not in (200, 201):
            print(f"FAIL {d:<44}ownership check: {vb[:90]}")
            continue
        curl("PUT", f"{G}/webmasters/v3/sites/{prop}")
        curl("PUT", f"{G}/webmasters/v3/sites/{prop}/sitemaps/"
                    f"https%3A%2F%2F{d}%2Fsitemap.xml")
        print(f"ok   {d}")
        time.sleep(2.5)

    final = owned_now()
    if final is not None:
        n = len(final & set(all_domains()))
        print(f"\n{n} of {len(all_domains())} confirmed in Search Console")
        left = [d for d in all_domains() if d not in final]
        json.dump(left, open(os.path.join(ROOT, "data", "gsc_missing.json"), "w"), indent=2)
        return 0 if not left else 1
    return 1


if __name__ == "__main__":
    sys.exit(run())
