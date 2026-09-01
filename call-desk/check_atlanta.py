#!/usr/bin/env python3
"""Settle whether a post-launch call was a real lead or a wrong number.

A caller with a real emergency leaves a message. A wrong number hears an
unfamiliar business name and hangs up on the greeting. So: recording or no
recording is the whole test, and it is decisive.

The greeting runs 8-10 seconds. A 16-second call that left no recording, or a
1.5-second recording that is just the beep, is a hang-up.

  export TELNYX_API_KEY=...
  python3 check_atlanta.py                 # last 30 days, all 83 markets
  python3 check_atlanta.py --domain atlantaemergencyplumberpros.com
  python3 check_atlanta.py --since 2026-08-23 --download

--download saves any voicemail audio into log/recordings/ so you can listen.
Recording links are signed and expire ~10 minutes after they are issued, so the
download happens in the same run that fetches them.
"""
import argparse, datetime as dt, json, os, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
API = "https://api.telnyx.com/v2"
KEY = os.environ.get("TELNYX_API_KEY", "").strip()
if not KEY:
    sys.exit("Set TELNYX_API_KEY first:  export TELNYX_API_KEY=KEY...")

TOLL_FREE = ("+1800", "+1833", "+1844", "+1855", "+1866", "+1877", "+1888")


def get(path, tries=8):
    """Telnyx returns an EMPTY BODY over its rate limit, not a 429. An empty
    reply is a retry, never a zero -- this is the bug that produced a false
    '23 area codes out of stock' reading and a false '83 done' on Search
    Console. Every call here reads its result back before counting it."""
    for attempt in range(tries):
        out = subprocess.run(
            ["curl", "-sS", "-H", f"Authorization: Bearer {KEY}", API + path],
            capture_output=True, text=True).stdout
        if out.strip():
            try:
                return json.loads(out)
            except Exception:
                pass
        time.sleep(2.0 * (attempt + 1))
    raise RuntimeError(f"GET {path} returned nothing usable after {tries} tries")


def page_all(path, cap=50):
    items, page = [], 1
    while page <= cap:
        sep = "&" if "?" in path else "?"
        d = get(f"{path}{sep}page[number]={page}&page[size]=250")
        batch = d.get("data") or []
        items += batch
        meta = d.get("meta") or {}
        if page >= (meta.get("total_pages") or 1) or not batch:
            break
        page += 1
    return items


def last10(v):
    return "".join(c for c in str(v or "") if c.isdigit())[-10:]


ap = argparse.ArgumentParser()
ap.add_argument("--since", default=(dt.date.today() - dt.timedelta(days=30)).isoformat())
ap.add_argument("--domain", default=None, help="limit to one market")
ap.add_argument("--download", action="store_true", help="save voicemail audio")
a = ap.parse_args()

# index.json is {"base": ..., "markets": [...]} -- the markets list is what we want
idx_path = os.path.join(HERE, "index.json")
markets = []
if os.path.exists(idx_path):
    raw = json.load(open(idx_path))
    markets = raw.get("markets", raw) if isinstance(raw, dict) else raw
by_number = {last10(m.get("tracking_number")): m for m in markets if m.get("tracking_number")}
ours = set(by_number)

print(f"Recordings since {a.since}\n")
recs = page_all(f"/recordings?filter[created_at][gte]={a.since}T00:00:00Z")
print(f"total recordings in account: {len(recs)}\n")

rows = []
for r in recs:
    at = r.get("attributes", r)
    rid = at.get("id") or r.get("id")
    # the list endpoint omits to/from; the single-recording endpoint carries them
    if not at.get("to"):
        at = (get(f"/recordings/{rid}") or {}).get("data", at)
    frm, to = str(at.get("from") or ""), str(at.get("to") or "")
    ms = at.get("duration_millis") or 0
    m = by_number.get(last10(to))
    label = ""
    if last10(frm) in ours:
        label = "TEST (our own number)"
    elif frm.startswith(TOLL_FREE):
        label = "LIKELY ROBOCALL (toll-free)"
    elif ms < 3000:
        label = "HANG-UP (beep only)"
    rows.append(dict(
        when=at.get("created_at") or "",
        domain=(m["domain"] if m else "(not one of ours)"),
        market=(f"{m['city']} {m['service']}" if m else "-"),
        caller=frm, seconds=round(ms / 1000, 1), label=label,
        link=(at.get("download_urls") or {}).get("mp3")))

if a.domain:
    rows = [r for r in rows if r["domain"] == a.domain]

if not rows:
    print("No recordings in this window. Every call hung up on the greeting")
    print("without leaving a message -- consistent with wrong numbers, not leads.")
    sys.exit(0)

print(f"{'when':21}{'market':38}{'caller':16}{'secs':>6}  label")
for r in sorted(rows, key=lambda x: x["when"]):
    print(f"{str(r['when'])[:19]:21}{r['market'][:38]:38}{r['caller'][:16]:16}"
          f"{r['seconds']:>6}  {r['label']}")

real = [r for r in rows if not r["label"]]
print(f"\n{len(real)} of {len(rows)} look like a genuine caller "
      f"(not a test, not toll-free, message over 3 seconds).")

if a.download:
    outdir = os.path.join(HERE, "log", "recordings")
    os.makedirs(outdir, exist_ok=True)
    n = 0
    for r in rows:
        if not r["link"]:
            continue
        safe = r["domain"].replace("/", "_")
        fn = os.path.join(outdir, f"{str(r['when'])[:10]}_{safe}_{r['caller']}.mp3")
        subprocess.run(["curl", "-sS", "-o", fn, r["link"]])
        if os.path.exists(fn) and os.path.getsize(fn) > 1000:
            n += 1
    print(f"saved {n} recordings to log/recordings/ -- listen to these")
