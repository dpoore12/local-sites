#!/usr/bin/env python3
"""Generate the per-market call-handling XML for all 83 markets.

Two files per market:
  v/<domain>.xml  -- what happens when the tracking number rings
  w/<domain>.xml  -- the whisper the contractor hears before he is bridged in

If routes.json has no forward number for a market, v/<domain>.xml takes a
message. If it has one, the call rings that number first (with the whisper) and
falls back to the message if nobody picks up.

Nothing here is dynamic and nothing needs a secret. Change routes.json, rerun
this, redeploy. That is the whole flip.
"""
import json
import os
import re
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

BASE = "https://call-desk.vercel.app"  # overwritten by DESK_BASE env if set
BASE = os.environ.get("DESK_BASE", BASE).rstrip("/")

VOICE = "Polly.Joanna"


def load_markets():
    markets = {m["domain"]: m for m in json.load(open(os.path.join(REPO, "data", "markets.json")))}
    out = []
    for domain in sorted(markets):
        sj = os.path.join(REPO, "sites", domain, "site.json")
        s = json.load(open(sj))
        phone = (s.get("phone_tel") or "").strip()
        if not re.match(r"^\+1\d{10}$", phone):
            raise SystemExit(f"{domain}: bad phone {phone!r}")
        out.append(
            {
                "domain": domain,
                "brand": s["brand"],
                "city": s["city"],
                "state": s["state"],
                "service": s["service"],
                "phone": phone,
                "display": s.get("phone_display", ""),
            }
        )
    return out


def spoken_domain(domain):
    """sacramentoacrepair.com -> 'sacramento a c repair dot com' is worse than
    just reading the brand. Whisper says the brand instead."""
    return domain.replace(".com", " dot com")


def voicemail_body(m):
    return (
        f'  <Say voice="{VOICE}">Thanks for calling {escape(m["brand"])}. '
        "Leave your name, your number and the address, and we will call you right back.</Say>\n"
        '  <Record maxLength="120" timeout="5" finishOnKey="#" playBeep="true" '
        'trim="trim-silence" format="mp3"/>\n'
        f'  <Say voice="{VOICE}">Got it. We will call you right back.</Say>\n'
        "  <Hangup/>\n"
    )


def voice_xml(m, forward):
    parts = ['<?xml version="1.0" encoding="UTF-8"?>', "<Response>"]
    if forward:
        parts.append(
            f'  <Dial timeout="25">'
            f'<Number url="{BASE}/w/{m["domain"]}.xml">{forward}</Number>'
            f"</Dial>"
        )
    parts.append(voicemail_body(m).rstrip("\n"))
    parts.append("</Response>")
    return "\n".join(parts) + "\n"


def whisper_xml(m):
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        "<Response>\n"
        f'  <Say voice="{VOICE}">Call from your {escape(m["city"])} '
        f'{escape(m["service"].lower())} website.</Say>\n'
        "</Response>\n"
    )


def main():
    markets = load_markets()
    routes_path = os.path.join(HERE, "routes.json")
    if os.path.exists(routes_path):
        routes = json.load(open(routes_path))
    else:
        routes = {m["domain"]: None for m in markets}

    # keep routes.json in sync with the market list, never dropping a set number
    routes = {m["domain"]: routes.get(m["domain"]) for m in markets}
    json.dump(routes, open(routes_path, "w"), indent=1, sort_keys=True)

    for sub in ("v", "w"):
        os.makedirs(os.path.join(HERE, sub), exist_ok=True)

    live = 0
    for m in markets:
        fwd = routes.get(m["domain"])
        if fwd:
            if not re.match(r"^\+1\d{10}$", fwd):
                raise SystemExit(f"{m['domain']}: forward number must be +1XXXXXXXXXX, got {fwd!r}")
            live += 1
        open(os.path.join(HERE, "v", m["domain"] + ".xml"), "w").write(voice_xml(m, fwd))
        open(os.path.join(HERE, "w", m["domain"] + ".xml"), "w").write(whisper_xml(m))

    index = {
        "base": BASE,
        "markets": [
            {
                "domain": m["domain"],
                "brand": m["brand"],
                "city": m["city"],
                "state": m["state"],
                "service": m["service"],
                "tracking_number": m["phone"],
                "tracking_display": m["display"],
                "forwards_to": routes.get(m["domain"]),
            }
            for m in markets
        ],
    }
    json.dump(index, open(os.path.join(HERE, "index.json"), "w"), indent=1)
    print(f"wrote {len(markets)} markets — {live} forwarding, {len(markets) - live} taking messages")


if __name__ == "__main__":
    main()
