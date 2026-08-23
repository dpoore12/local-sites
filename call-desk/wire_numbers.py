#!/usr/bin/env python3
"""Point each market's tracking number at that market's own call-handling file.

One TeXML application per market, named after the domain, whose voice URL is
https://<base>/v/<domain>.xml. Then the market's phone number is attached to
that application. After this runs, a call to any of the 83 numbers is handled by
that market's XML and shows up in Telnyx under that market's own connection --
which is what makes per-market call counts and minutes readable later.

Run:  python3 wire_numbers.py            (dry run, shows what it would do)
      python3 wire_numbers.py --apply
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.environ.get("DESK_BASE", "https://call-desk-xi.vercel.app").rstrip("/")
API = "https://api.telnyx.com/v2"
STATE = os.path.join(HERE, "wiring.json")


def call(method, path, body=None, tries=8):
    for attempt in range(tries):
        cmd = ["curl", "-sS", "-X", method, API + path]
        if body is not None:
            cmd += ["-H", "Content-Type: application/json", "-d", json.dumps(body)]
        out = subprocess.run(cmd, capture_output=True, text=True).stdout
        if not out.strip():
            time.sleep(2.0 * (attempt + 1))  # empty body == rate limited, never zero
            continue
        try:
            return json.loads(out)
        except Exception:
            time.sleep(2.0 * (attempt + 1))
    raise RuntimeError(f"{method} {path} gave nothing usable after {tries} tries")


def all_numbers():
    """number -> telnyx id"""
    found, page = {}, 1
    while True:
        r = call("GET", f"/phone_numbers?page%5Bsize%5D=50&page%5Bnumber%5D={page}")
        data = r.get("data")
        if data is None:
            raise RuntimeError(f"phone_numbers page {page}: {r}")
        if not data:
            break
        for n in data:
            found[n["phone_number"]] = n["id"]
        meta = r.get("meta") or {}
        if page >= (meta.get("total_pages") or 1):
            break
        page += 1
        time.sleep(0.3)
    return found


def existing_apps():
    """friendly_name -> app id"""
    found, page = {}, 1
    while True:
        r = call("GET", f"/texml_applications?page%5Bsize%5D=50&page%5Bnumber%5D={page}")
        data = r.get("data")
        if data is None:
            raise RuntimeError(f"texml_applications page {page}: {r}")
        if not data:
            break
        for a in data:
            found[a["friendly_name"]] = a["id"]
        meta = r.get("meta") or {}
        if page >= (meta.get("total_pages") or 1):
            break
        page += 1
        time.sleep(0.3)
    return found


def main():
    apply = "--apply" in sys.argv
    index = json.load(open(os.path.join(HERE, "index.json")))
    markets = index["markets"]
    if "--only" in sys.argv:
        want = sys.argv[sys.argv.index("--only") + 1]
        markets = [m for m in markets if m["domain"] == want]
        if not markets:
            raise SystemExit(f"no market named {want}")

    numbers = all_numbers()
    apps = existing_apps()
    print(f"telnyx: {len(numbers)} numbers on the account, {len(apps)} texml apps already there")

    missing = [m for m in markets if m["tracking_number"] not in numbers]
    if missing:
        for m in missing:
            print(f"  MISSING ON TELNYX  {m['domain']}  {m['tracking_number']}")
        raise SystemExit(f"{len(missing)} markets have a number that is not on the account")

    state = json.load(open(STATE)) if os.path.exists(STATE) else {}
    for i, m in enumerate(markets, 1):
        domain = m["domain"]
        name = domain
        url = f"{BASE}/v/{domain}.xml"
        app_id = apps.get(name) or (state.get(domain) or {}).get("app_id")

        if not apply:
            print(f"[dry] {domain}: {'reuse app ' + app_id if app_id else 'create app'} -> {url}"
                  f" ; attach {m['tracking_number']}")
            continue

        if not app_id:
            r = call("POST", "/texml_applications", {
                "friendly_name": name,
                "voice_url": url,
                "voice_method": "get",
                "active": True,
                "inbound": {"shaken_stir_enabled": False},
            })
            if "data" not in r:
                raise RuntimeError(f"{domain}: app create failed: {r}")
            app_id = r["data"]["id"]
            time.sleep(0.8)
        else:
            r = call("PATCH", f"/texml_applications/{app_id}", {
                "friendly_name": name, "voice_url": url, "voice_method": "get",
            })
            if "data" not in r:
                raise RuntimeError(f"{domain}: app update failed: {r}")
            time.sleep(0.3)

        num_id = numbers[m["tracking_number"]]
        r = call("PATCH", f"/phone_numbers/{num_id}", {"connection_id": app_id})
        if "data" not in r:
            raise RuntimeError(f"{domain}: number attach failed: {r}")

        state[domain] = {"app_id": app_id, "number_id": num_id,
                         "number": m["tracking_number"], "voice_url": url}
        json.dump(state, open(STATE, "w"), indent=1, sort_keys=True)
        print(f"[{i}/{len(markets)}] {domain}  app {app_id}  number {m['tracking_number']}")
        time.sleep(0.8)

    if apply:
        print(f"done — {len(state)} markets wired")


if __name__ == "__main__":
    main()
