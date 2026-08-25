#!/usr/bin/env python3
"""Find real leads nobody has been told about yet, and tell someone.

The lead form writes into Cloudflare D1. Agency sales pitches are already
filed with spam=1 by the router, so this only ever looks at spam=0. A lead
is announced exactly once: the notified flag is set after a successful send,
never before, so a failed send retries on the next run instead of vanishing.

Usage
  python3 alert_leads.py --list          print unannounced leads as JSON
  python3 alert_leads.py --mark 4,7,9    flag those ids as announced
  python3 alert_leads.py --sms           text them (needs alert_cell.txt)
  python3 alert_leads.py --status        show the config and the backlog

Cloudflare needs api_credentials=["custom-cred:api.cloudflare.com"].
Texting needs api_credentials=["custom-cred:api.telnyx.com"] as well.
"""

import json
import os
import subprocess
import sys

ACCOUNT = "a3bf1a13d93899d8408b9d1ea94df078"
DATABASE = "ab96c54f-96fd-4afc-88e0-852aaa94f4c4"
D1 = (f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}"
      f"/d1/database/{DATABASE}/query")

HERE = os.path.dirname(os.path.abspath(__file__))
CELL_FILE = os.path.join(HERE, "alert_cell.txt")
SENDER_FILE = os.path.join(HERE, "alert_sender.txt")

# A run that quietly reports "no new leads" because the query failed is worse
# than a run that stops loudly, so a failed query raises instead of returning [].
TIMEOUT = 60


def d1(sql):
    out = subprocess.run(
        ["curl", "-s", "--max-time", str(TIMEOUT), "-X", "POST", D1,
         "-H", "Content-Type: application/json",
         "--data-binary", json.dumps({"sql": sql})],
        capture_output=True, text=True, timeout=TIMEOUT + 30).stdout
    try:
        body = json.loads(out)
    except json.JSONDecodeError:
        raise SystemExit("lead store returned something that is not JSON: "
                         + out[:200])
    if not body.get("success"):
        raise SystemExit("lead store refused the query: "
                         + json.dumps(body.get("errors"))[:300])
    return body["result"][0]["results"]


def pending():
    # CAST, not a bare comparison. The flags are written by more than one
    # place and turn up as 0, '0' or NULL; COALESCE strips column affinity, so
    # '0' = 0 is false in SQLite and a lead would silently never be announced.
    return d1(
        "SELECT id, created_at, site, page, name, phone, problem, zip, email,"
        " best_time FROM leads"
        " WHERE CAST(COALESCE(spam,0) AS INTEGER) = 0"
        "   AND CAST(COALESCE(notified,0) AS INTEGER) = 0"
        " ORDER BY id ASC LIMIT 25"
    )


def mark(ids):
    ids = [int(i) for i in ids]
    if not ids:
        return 0
    d1("UPDATE leads SET notified = 1 WHERE id IN ("
       + ",".join(str(i) for i in ids) + ")")
    return len(ids)


def pretty_phone(p):
    p = str(p or "")
    if len(p) == 12 and p.startswith("+1"):
        return f"({p[2:5]}) {p[5:8]}-{p[8:]}"
    return p


def one_line(lead):
    """One lead, short enough to read on a lock screen."""
    said = " ".join(str(lead.get("problem") or "").split())
    if len(said) > 160:
        said = said[:157].rstrip() + "..."
    bits = [f"{lead.get('name')} {pretty_phone(lead.get('phone'))}",
            str(lead.get("site") or "")]
    if lead.get("zip"):
        bits.append("ZIP " + str(lead["zip"]))
    if lead.get("best_time"):
        bits.append("call " + str(lead["best_time"]).lower())
    return " | ".join(bits) + "\n" + said


def send_sms(leads):
    """Text each lead. Returns the ids that actually went out."""
    if not os.path.exists(CELL_FILE):
        raise SystemExit("no destination yet: write the cell number into "
                         + CELL_FILE)
    to = open(CELL_FILE).read().strip()
    sender = (open(SENDER_FILE).read().strip()
              if os.path.exists(SENDER_FILE) else "")
    if not sender:
        raise SystemExit("no sending number yet: write it into " + SENDER_FILE)

    sent = []
    for lead in leads:
        body = {"from": sender, "to": to, "text": "New lead. " + one_line(lead)}
        out = subprocess.run(
            ["curl", "-s", "--max-time", str(TIMEOUT), "-X", "POST",
             "https://api.telnyx.com/v2/messages",
             "-H", "Content-Type: application/json",
             "--data-binary", json.dumps(body)],
            capture_output=True, text=True, timeout=TIMEOUT + 30).stdout
        try:
            res = json.loads(out)
        except json.JSONDecodeError:
            print(f"  lead {lead['id']}: telnyx returned {out[:120]}",
                  file=sys.stderr)
            continue
        if "data" in res:
            print(f"  lead {lead['id']}: queued {res['data']['id']}")
            sent.append(lead["id"])
        else:
            print(f"  lead {lead['id']}: refused "
                  f"{json.dumps(res.get('errors'))[:200]}", file=sys.stderr)
    return sent


def status():
    rows = d1("SELECT CAST(COALESCE(spam,0) AS INTEGER) AS spam,"
              " CAST(COALESCE(notified,0) AS INTEGER) AS n,"
              " COUNT(*) AS c FROM leads GROUP BY 1,2")
    print("lead store:")
    for r in rows:
        kind = "pitch" if r["spam"] else "real"
        state = "announced" if r["n"] else "waiting"
        print(f"  {kind} / {state}: {r['c']}")
    cell = (open(CELL_FILE).read().strip()
            if os.path.exists(CELL_FILE) else "(not set)")
    sender = (open(SENDER_FILE).read().strip()
              if os.path.exists(SENDER_FILE) else "(not set)")
    print(f"texts to:   {cell}")
    print(f"texts from: {sender}")


def main():
    args = sys.argv[1:]
    if not args or args[0] == "--status":
        status()
    elif args[0] == "--list":
        print(json.dumps(pending(), indent=2))
    elif args[0] == "--mark":
        if len(args) < 2:
            raise SystemExit("--mark needs a comma-separated list of ids")
        print("marked", mark(args[1].split(",")))
    elif args[0] == "--sms":
        leads = pending()
        if not leads:
            print("nothing waiting")
            return
        print(f"{len(leads)} waiting")
        sent = send_sms(leads)
        print("marked", mark(sent))
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
