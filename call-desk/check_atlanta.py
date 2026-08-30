#!/usr/bin/env python3
"""Settle whether the post-launch Atlanta calls were real leads or a recycled number.

The three Atlanta calls ran 16-17 seconds. The greeting alone is ~8-10 seconds.
If a caller left a message there is a recording; if they hung up on the greeting
there is not. That is the whole test, and it is decisive.

  export TELNYX_API_KEY=...
  python3 check_atlanta.py                 # last 30 days, all 83 markets
  python3 check_atlanta.py --domain atlantaemergencyplumberpros.com
  python3 check_atlanta.py --since 2026-08-23 --download

--download saves any voicemail audio into log/recordings/ so you can listen.
Recording links are signed and expire ~10 minutes after they are issued, so the
download happens in the same run that fetches them.
"""
import argparse, datetime as dt, json, os, subprocess, sys, time, zoneinfo

HERE = os.path.dirname(os.path.abspath(__file__))
API = "https://api.telnyx.com/v2"
PT = zoneinfo.ZoneInfo("America/Los_Angeles")
KEY = os.environ.get("TELNYX_API_KEY", "").strip()
if not KEY:
    sys.exit("Set TELNYX_API_KEY first:  export TELNYX_API_KEY=KEY...")

def get(path, tries=8):
    """Telnyx returns an EMPTY BODY over its rate limit, not a 429. An empty
    reply is a retry, never a zero -- this is the bug that produced a false
    '23 area codes out of stock' reading and a false '83 done' on Search Console."""
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

ap = argparse.ArgumentParser()
ap.add_argument("--since", default=(dt.date.today()-dt.timedelta(days=30)).isoformat())
ap.add_argument("--domain", default=None, help="limit to one market")
ap.add_argument("--download", action="store_true", help="save voicemail audio")
a = ap.parse_args()

index = {r["domain"]: r for r in json.load(open(os.path.join(HERE, "index.json")))} \
        if os.path.exists(os.path.join(HERE, "index.json")) else {}
ours = {str(r.get("tracking_number","")).replace("-","").replace(" ","")[-10:]
        for r in index.values()}

print(f"Recordings since {a.since}\n")
recs = page_all(f"/recordings?filter[created_at][gte]={a.since}T00:00:00Z")
print(f"total recordings in account: {len(recs)}\n")

rows = []
for r in recs:
    at = r.get("attributes", r)
    cid = str(at.get("from") or at.get("call_leg_id") or "")
    to  = str(at.get("to") or "")
    dur = at.get("duration_millis")
    dur = round(dur/1000) if dur else at.get("duration_secs")
    made = at.get("created_at") or at.get("recording_started_at") or ""
    urls = at.get("download_urls") or {}
    link = urls.get("mp3") or urls.get("wav")
    dom = None
    for d, meta in index.items():
        tn = str(meta.get("tracking_number","")).replace("-","").replace(" ","")[-10:]
        if tn and tn in to.replace("-","").replace(" ",""):
            dom = d; break
    rows.append(dict(when=made, domain=dom or "(unmatched)", caller=cid, to=to,
                     seconds=dur, id=at.get("id") or r.get("id"), link=link))

if a.domain:
    rows = [r for r in rows if r["domain"] == a.domain]

if not rows:
    print("No recordings matched. Every post-launch call hung up on the greeting")
    print("without leaving a message -- consistent with wrong numbers, not leads.")
else:
    print(f"{'when':22}{'market':40}{'caller':15}{'secs':>5}")
    for r in sorted(rows, key=lambda x: x["when"]):
        print(f"{str(r['when'])[:19]:22}{str(r['domain'])[:40]:40}{r['caller'][:15]:15}{str(r['seconds']):>5}")

    if a.download:
        outdir = os.path.join(HERE, "log", "recordings")
        os.makedirs(outdir, exist_ok=True)
        n = 0
        for r in rows:
            if not r["link"]:
                continue
            fn = os.path.join(outdir, f"{str(r['when'])[:10]}_{r['domain']}_{r['caller']}.mp3")
            subprocess.run(["curl", "-sS", "-o", fn, r["link"]])
            if os.path.exists(fn) and os.path.getsize(fn) > 1000:
                n += 1
        print(f"\nsaved {n} recordings to log/recordings/ -- listen to these")

print("\nThe test: a caller with a real emergency leaves a message. A wrong number")
print("hears an unfamiliar business name and hangs up. If the Atlanta calls have")
print("no recording, they were not leads.")
