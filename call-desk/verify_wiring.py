#!/usr/bin/env python3
"""Read the truth back off Telnyx and check every market against it.

Checks, per market:
  * the number is on the account
  * the number is attached to a TeXML application named after that domain
  * that application's voice URL is the market's own file
  * that file is actually live on the internet and is valid XML
"""
import json
import os
import re
import subprocess
import time
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
API = "https://api.telnyx.com/v2"


def call(path, tries=8):
    for attempt in range(tries):
        out = subprocess.run(["curl", "-sS", API + path], capture_output=True, text=True).stdout
        if out.strip():
            try:
                return json.loads(out)
            except Exception:
                pass
        time.sleep(2.0 * (attempt + 1))
    raise RuntimeError(f"GET {path} gave nothing usable")


def page_all(path):
    items, page = [], 1
    while True:
        sep = "&" if "?" in path else "?"
        r = call(f"{path}{sep}page%5Bsize%5D=50&page%5Bnumber%5D={page}")
        data = r.get("data")
        if data is None:
            raise RuntimeError(f"{path} page {page}: {r}")
        items += data
        meta = r.get("meta") or {}
        if not data or page >= (meta.get("total_pages") or 1):
            return items
        page += 1
        time.sleep(0.4)


def check_files(index, markets):
    """Must run WITHOUT the Telnyx credential attached -- that proxy only allows
    api.telnyx.com, so every other host comes back as HTTP 000."""
    problems = []
    for m in markets:
        for kind in ("v", "w"):
            url = f"{index['base']}/{kind}/{m['domain']}.xml"
            r = subprocess.run(
                ["curl", "-sS", "-o", "/tmp/chk.xml", "-w", "%{http_code}", url],
                capture_output=True, text=True).stdout.strip()
            if r != "200":
                problems.append(f"{m['domain']}: {kind} file returned HTTP {r}")
                continue
            try:
                ET.parse("/tmp/chk.xml")
            except Exception as e:
                problems.append(f"{m['domain']}: {kind} file is not valid XML — {e}")
    return problems


def main():
    index = json.load(open(os.path.join(HERE, "index.json")))
    markets = index["markets"]

    if "--files-only" in sys.argv:
        problems = check_files(index, markets)
        if problems:
            print(f"{len(problems)} PROBLEM(S):")
            for p in problems:
                print("  " + p)
            raise SystemExit(1)
        print(f"OK — all {len(markets)} markets: both files live and valid XML")
        return

    numbers = {n["phone_number"]: n for n in page_all("/phone_numbers")}
    apps = {a["id"]: a for a in page_all("/texml_applications")}
    print(f"account has {len(numbers)} numbers and {len(apps)} call-handling apps")

    problems = []
    for m in markets:
        d, num = m["domain"], m["tracking_number"]
        n = numbers.get(num)
        if not n:
            problems.append(f"{d}: {num} is not on the account")
            continue
        app = apps.get(str(n.get("connection_id")))
        if not app:
            problems.append(f"{d}: {num} is not attached to any call-handling app "
                            f"(connection_id={n.get('connection_id')!r})")
            continue
        if app["friendly_name"] != d:
            problems.append(f"{d}: {num} is attached to {app['friendly_name']!r}")
            continue
        want = f"{index['base']}/v/{d}.xml"
        if app.get("voice_url") != want:
            problems.append(f"{d}: app points at {app.get('voice_url')!r}, expected {want!r}")

    if problems:
        print(f"\n{len(problems)} PROBLEM(S):")
        for p in problems:
            print("  " + p)
        raise SystemExit(1)
    print(f"\nOK — all {len(markets)} markets: number attached to its own app and "
          f"the app points at that market's own file")
    print("now run again with --files-only and NO telnyx credential to check the files")


if __name__ == "__main__":
    main()
