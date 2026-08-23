#!/usr/bin/env python3
"""The call log. One row per call, per market, kept forever in log/calls.csv.

Telnyx keeps call events for a short window, so this pulls them and appends to a
CSV we own. Run it daily (or any time) -- it dedupes, so running it twice is safe.

  python3 call_log.py                 # last 2 days, append to log/calls.csv
  python3 call_log.py --since 2026-08-01
  python3 call_log.py --report        # print the summary from the CSV, no API calls

Columns: when (Pacific), domain, city, service, caller, tracking_number,
seconds_on_call, left_message, message_seconds, message_url_expires
"""
import csv
import datetime as dt
import json
import os
import subprocess
import sys
import time
import zoneinfo

HERE = os.path.dirname(os.path.abspath(__file__))
API = "https://api.telnyx.com/v2"
LOG = os.path.join(HERE, "log", "calls.csv")
PT = zoneinfo.ZoneInfo("America/Los_Angeles")
FIELDS = ["leg_id", "when_pt", "domain", "city", "service", "caller", "tracking_number",
          "seconds_on_call", "left_message", "message_seconds"]
WANT = {"call_initiated", "call_answered", "call_hangup"}


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


def page_all(path, cap=200):
    items, page = [], 1
    while page <= cap:
        sep = "&" if "?" in path else "?"
        r = call(f"{path}{sep}page%5Bsize%5D=250&page%5Bnumber%5D={page}")
        if "data" not in r:
            raise RuntimeError(f"{path} page {page}: {r}")
        items += r["data"]
        meta = r.get("meta") or {}
        if not r["data"] or page >= (meta.get("total_pages") or 1):
            return items
        page += 1
        time.sleep(0.4)
    return items


def parse_ts(s):
    s = s.replace("Z", "").strip()
    for fmt in ("%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%d %H:%M:%S",
                "%Y-%m-%dT%H:%M:%S"):
        try:
            return dt.datetime.strptime(s, fmt).replace(tzinfo=dt.timezone.utc)
        except ValueError:
            continue
    raise ValueError(s)


def markets_by_app():
    wiring = json.load(open(os.path.join(HERE, "wiring.json")))
    index = {m["domain"]: m for m in json.load(open(os.path.join(HERE, "index.json")))["markets"]}
    return {v["app_id"]: index[d] for d, v in wiring.items() if d in index}


def read_log():
    if not os.path.exists(LOG):
        return {}
    with open(LOG) as f:
        return {r["leg_id"]: r for r in csv.DictReader(f)}


def write_log(rows):
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    ordered = sorted(rows.values(), key=lambda r: r["when_pt"])
    with open(LOG, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(ordered)


def report(rows):
    if not rows:
        print("no calls logged yet")
        return
    per = {}
    for r in rows.values():
        p = per.setdefault(r["domain"], {"city": r["city"], "calls": 0, "messages": 0, "secs": 0})
        p["calls"] += 1
        p["messages"] += 1 if r["left_message"] == "yes" else 0
        p["secs"] += int(r["seconds_on_call"] or 0)
    print(f"{'market':46} {'city':18} {'calls':>6} {'messages':>9} {'avg secs':>9}")
    for d, p in sorted(per.items(), key=lambda kv: -kv[1]["calls"]):
        print(f"{d:46} {p['city']:18} {p['calls']:>6} {p['messages']:>9} "
              f"{round(p['secs'] / p['calls']):>9}")
    print(f"\n{sum(p['calls'] for p in per.values())} calls across {len(per)} markets")


def main():
    rows = read_log()
    if "--report" in sys.argv:
        report(rows)
        return

    if "--since" in sys.argv:
        since = sys.argv[sys.argv.index("--since") + 1]
        if len(since) == 10:
            since += "T00:00:00Z"
    else:
        since = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=2)).strftime(
            "%Y-%m-%dT%H:%M:%SZ")
    print(f"pulling call events since {since}")

    by_app = markets_by_app()
    events = page_all(f"/call_events?filter%5Boccurred_at%5D%5Bgte%5D={since}")
    print(f"{len(events)} events on the account in that window")

    legs = {}
    for e in events:
        if e.get("name") not in WANT or e.get("type") != "call_scripting_webhook":
            continue
        m = by_app.get(str(e.get("connection_id")))
        if not m:
            continue  # not one of our 83 markets
        leg = legs.setdefault(e["leg_id"], {"m": m, "from": e.get("from"),
                                            "to": e.get("to"), "t": {}})
        leg["t"].setdefault(e["name"], parse_ts(e["occurred_at"]))

    recs = page_all("/recordings")
    msg_by_leg = {}
    for r in recs:
        if r.get("initiated_by") != "RecordVerb":
            continue
        msg_by_leg[r.get("call_leg_id")] = round((r.get("duration_millis") or 0) / 1000)

    added = 0
    for leg_id, leg in legs.items():
        t = leg["t"]
        start = t.get("call_initiated") or t.get("call_answered")
        if not start:
            continue
        end = t.get("call_hangup")
        secs = round((end - start).total_seconds()) if end else ""
        msg = msg_by_leg.get(leg_id)
        row = {
            "leg_id": leg_id,
            "when_pt": start.astimezone(PT).strftime("%Y-%m-%d %H:%M:%S"),
            "domain": leg["m"]["domain"],
            "city": leg["m"]["city"],
            "service": leg["m"]["service"],
            "caller": leg["from"] or "",
            "tracking_number": leg["to"] or leg["m"]["tracking_number"],
            "seconds_on_call": secs,
            "left_message": "yes" if msg else "no",
            "message_seconds": msg or "",
        }
        if leg_id not in rows:
            added += 1
        rows[leg_id] = row

    write_log(rows)
    print(f"{added} new call(s) added — {len(rows)} total in {LOG}\n")
    report(rows)


if __name__ == "__main__":
    main()
