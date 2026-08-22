#!/usr/bin/env python3
"""Re-read the Telnyx account and report drift against what the sites claim.

Does not buy anything. Run it whenever you suspect the sites and the carrier
disagree:

    bash(command="cd local-sites && python3 phones.py",
         api_credentials=["custom-cred:api.telnyx.com"])
"""
import json, pathlib, subprocess, time

ROOT = pathlib.Path(__file__).parent


def account_numbers():
    out = []
    for page in range(1, 6):
        u = ("https://api.telnyx.com/v2/phone_numbers"
             f"?page%5Bsize%5D=50&page%5Bnumber%5D={page}")
        p = subprocess.run(["curl", "-s", "--max-time", "60", u,
                            "-H", "Accept: application/json"],
                           capture_output=True, text=True)
        try:
            r = json.loads(p.stdout)
        except Exception:
            break
        d = r.get("data") or []
        out += d
        if page >= (r.get("meta") or {}).get("total_pages", 1):
            break
        time.sleep(1)
    return {n["phone_number"]: n for n in out}


if __name__ == "__main__":
    have = account_numbers()
    print(f"{len(have)} numbers on the Telnyx account")
    missing, placeholder, inactive = [], [], []
    for sj in sorted((ROOT / "sites").glob("*/site.json")):
        s = json.loads(sj.read_text())
        dom = sj.parent.name
        if s.get("phone_status") == "PLACEHOLDER":
            placeholder.append(dom)
            continue
        tel = s.get("phone_tel")
        if tel not in have:
            missing.append((dom, tel))
        elif have[tel].get("status") != "active":
            inactive.append((dom, tel, have[tel].get("status")))
    print(f"placeholder, must not be published: {len(placeholder)}")
    for d in placeholder:
        print("  ", d)
    if missing:
        print(f"ON A SITE BUT NOT ON THE ACCOUNT: {len(missing)}")
        for d, t in missing:
            print("  ", d, t)
    if inactive:
        print(f"NOT ACTIVE: {len(inactive)}")
        for d, t, st in inactive:
            print("  ", d, t, st)
    if not missing and not inactive:
        print("every live site number is present and active")
