#!/usr/bin/env python3
"""Turn a market live (send its calls to a contractor) or back to voicemail.

  python3 flip.py sacramento +19165551234     # calls now ring that shop
  python3 flip.py sacramento off              # back to taking messages
  python3 flip.py --status                    # who is live right now

The market can be given as the domain, the city, or any unique piece of either.
Nothing on Telnyx changes and no phone number changes -- only the one file that
says what to do when that number rings. Takes about ten seconds.
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROUTES = os.path.join(HERE, "routes.json")
INDEX = os.path.join(HERE, "index.json")


def markets():
    return json.load(open(INDEX))["markets"]


def find(term):
    t = term.lower().strip()
    ms = markets()
    exact = [m for m in ms if m["domain"].lower() == t]
    if exact:
        return exact[0]
    hits = [m for m in ms if t in m["domain"].lower() or t in m["city"].lower()]
    if not hits:
        raise SystemExit(f"no market matches {term!r}")
    if len(hits) > 1:
        print(f"{term!r} matches more than one market — be more specific:")
        for m in hits:
            print(f"  {m['domain']}  ({m['city']}, {m['state']} — {m['service']})")
        raise SystemExit(1)
    return hits[0]


def normalise(number):
    digits = re.sub(r"\D", "", number)
    if len(digits) == 10:
        digits = "1" + digits
    if len(digits) != 11 or not digits.startswith("1"):
        raise SystemExit(f"{number!r} is not a US phone number")
    return "+" + digits


def pretty(n):
    return f"({n[2:5]}) {n[5:8]}-{n[8:]}" if n else ""


def status():
    routes = json.load(open(ROUTES))
    live = [(m, routes.get(m["domain"])) for m in markets() if routes.get(m["domain"])]
    if not live:
        print("nobody is live — all 83 markets are taking messages")
        return
    print(f"{len(live)} market(s) live:")
    for m, fwd in live:
        print(f"  {m['city']}, {m['state']:2} {m['service']:26} "
              f"{pretty(m['tracking_number'])} -> {pretty(fwd)}   {m['domain']}")


def deploy():
    r = subprocess.run(
        ["npx", "--yes", "vercel", "deploy", "--prod", "--yes",
         "--token", os.environ.get("VERCEL_TOKEN", "")],
        cwd=HERE, capture_output=True, text=True)
    out = (r.stdout or "") + (r.stderr or "")
    if r.returncode != 0:
        print(out[-800:])
        raise SystemExit("deploy failed — nothing changed on the live site")
    print("live.")


def main():
    if "--status" in sys.argv or len(sys.argv) < 2:
        status()
        return
    if len(sys.argv) < 3:
        raise SystemExit("usage: flip.py <market> <phone number | off>")

    m = find(sys.argv[1])
    target = sys.argv[2]
    routes = json.load(open(ROUTES))

    if target.lower() in ("off", "none", "voicemail", "stop"):
        routes[m["domain"]] = None
        print(f"{m['city']}, {m['state']} {m['service']} — back to taking messages")
    else:
        fwd = normalise(target)
        routes[m["domain"]] = fwd
        print(f"{m['city']}, {m['state']} {m['service']} — calls to "
              f"{pretty(m['tracking_number'])} now ring {pretty(fwd)}")
        print("the shop hears \"Call from your "
              f"{m['city']} {m['service'].lower()} website\" before it connects")

    json.dump(routes, open(ROUTES, "w"), indent=1, sort_keys=True)
    base = json.load(open(INDEX))["base"]
    env = dict(os.environ, DESK_BASE=base)
    subprocess.run([sys.executable, os.path.join(HERE, "build_xml.py")], cwd=HERE, env=env,
                   check=True, capture_output=True)
    deploy()


if __name__ == "__main__":
    main()
