#!/usr/bin/env python3
"""Build the call log page from log/calls.csv.

The page is published at a long random path so it is not findable, and the path
is kept in log_slug.txt so it never changes between runs.

  python3 build_log_page.py     # writes <slug>/index.html
"""
import csv
import datetime
import json
import os
import secrets

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "log", "calls.csv")
SLUG_FILE = os.path.join(HERE, "log_slug.txt")


def slug():
    if os.path.exists(SLUG_FILE):
        s = open(SLUG_FILE).read().strip()
        if s:
            return s
    s = "calls-" + secrets.token_hex(8)
    open(SLUG_FILE, "w").write(s + "\n")
    return s


def rows():
    if not os.path.exists(LOG):
        return []
    with open(LOG) as f:
        out = list(csv.DictReader(f))
    out.sort(key=lambda r: r["when_pt"], reverse=True)
    return out


def pretty(n):
    n = (n or "").strip()
    return f"({n[2:5]}) {n[5:8]}-{n[8:]}" if len(n) == 12 and n.startswith("+1") else n


HTML = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Call Log</title>
<style>
:root{--ink:#12212f;--brand:#143d59;--brand-deep:#0b2233;--brand-mid:#1b4f70;
--brand-tint:#eaf0f5;--cta:#f5a524;--cta-deep:#b8730a;--surface:#f7f6f2;--card:#fff;--line:#e2dfd6}
*{box-sizing:border-box}
body{margin:0;background:var(--surface);color:var(--ink);
font:16px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
header{background:var(--brand-deep);color:#fff;padding:1.6rem 1.5rem}
header .wrap{max-width:1180px;margin:0 auto;display:flex;justify-content:space-between;
align-items:baseline;gap:1rem;flex-wrap:wrap}
header h1{margin:0;font-size:1.3rem;letter-spacing:.02em}
header h1 span{color:var(--cta)}
header .stamp{color:#a9bece;font-size:.85rem}
main{max-width:1180px;margin:0 auto;padding:1.5rem 1.5rem 4rem}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:.9rem;margin-bottom:1.8rem}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:1rem 1.1rem}
.card b{display:block;font-size:1.9rem;line-height:1.1;color:var(--brand)}
.card span{font-size:.8rem;text-transform:uppercase;letter-spacing:.06em;color:var(--brand-mid)}
h2{font-size:1rem;text-transform:uppercase;letter-spacing:.07em;color:var(--brand-mid);
margin:2rem 0 .7rem;border-bottom:2px solid var(--cta);padding-bottom:.4rem;display:inline-block}
.tablewrap{background:var(--card);border:1px solid var(--line);border-radius:10px;overflow:auto}
table{border-collapse:collapse;width:100%;font-size:.9rem}
th{background:var(--brand-tint);color:var(--brand-deep);text-align:left;font-weight:600;
padding:.6rem .8rem;position:sticky;top:0;white-space:nowrap;font-size:.78rem;
text-transform:uppercase;letter-spacing:.05em}
td{padding:.55rem .8rem;border-top:1px solid var(--line);white-space:nowrap}
td.wrap{white-space:normal}
tbody tr:hover{background:#fbf8f1}
.num{font-variant-numeric:tabular-nums}
.yes{color:#1c6b3a;font-weight:600}.no{color:#8a8578}
.empty{padding:2.5rem 1.2rem;text-align:center;color:var(--brand-mid)}
input[type=search]{width:100%;max-width:340px;padding:.55rem .8rem;border:1px solid var(--line);
border-radius:8px;font-size:.95rem;margin-bottom:.8rem;background:#fff}
footer{max-width:1180px;margin:0 auto;padding:0 1.5rem 3rem;color:var(--brand-mid);font-size:.85rem}
</style></head><body>
<header><div class="wrap">
<h1>Call <span>Log</span></h1>
<div class="stamp">updated __STAMP__ &middot; __NMARKETS__ of 83 markets have had a call</div>
</div></header>
<main>
<div class="cards">
<div class="card"><b class="num">__TOTAL__</b><span>calls, all time</span></div>
<div class="card"><b class="num">__D7__</b><span>last 7 days</span></div>
<div class="card"><b class="num">__D30__</b><span>last 30 days</span></div>
<div class="card"><b class="num">__MSGS__</b><span>messages left</span></div>
</div>

<h2>By market</h2>
<div class="tablewrap"><table>
<thead><tr><th>Market</th><th>City</th><th>Service</th><th>Calls</th><th>Messages</th>
<th>Last call</th><th>Live to</th></tr></thead>
<tbody>__BYMARKET__</tbody></table></div>

<h2>Every call</h2>
<input type="search" id="q" placeholder="Filter by city, market or number">
<div class="tablewrap"><table>
<thead><tr><th>When (Pacific)</th><th>Market</th><th>City</th><th>Caller</th>
<th>Site number</th><th>Seconds</th><th>Message</th></tr></thead>
<tbody id="calls">__CALLS__</tbody></table></div>
</main>
<footer>No calls are recorded. Only voicemail messages are kept, and only until you delete them.
A caller who hangs up before the beep is still counted here but leaves nothing to listen to.</footer>
<script>
const q=document.getElementById('q'),rows=[...document.querySelectorAll('#calls tr')];
q&&q.addEventListener('input',()=>{const t=q.value.toLowerCase();
rows.forEach(r=>{r.style.display=r.textContent.toLowerCase().includes(t)?'':'none'})});
</script>
</body></html>
"""


def main():
    data = rows()
    routes = json.load(open(os.path.join(HERE, "routes.json")))
    index = {m["domain"]: m
             for m in json.load(open(os.path.join(HERE, "index.json")))["markets"]}
    today = datetime.date.today()

    def within(r, days):
        try:
            d = datetime.datetime.strptime(r["when_pt"][:10], "%Y-%m-%d").date()
        except Exception:
            return False
        return (today - d).days <= days

    per = {}
    for r in data:
        p = per.setdefault(r["domain"], {"calls": 0, "msgs": 0, "last": ""})
        p["calls"] += 1
        p["msgs"] += 1 if r["left_message"] == "yes" else 0
        p["last"] = max(p["last"], r["when_pt"])

    bym = []
    for d, p in sorted(per.items(), key=lambda kv: (-kv[1]["calls"], kv[0])):
        m = index.get(d, {})
        fwd = routes.get(d)
        bym.append(
            f'<tr><td class="wrap">{d}</td><td>{m.get("city","")}</td>'
            f'<td>{m.get("service","")}</td><td class="num">{p["calls"]}</td>'
            f'<td class="num">{p["msgs"]}</td><td class="num">{p["last"]}</td>'
            f'<td class="num">{pretty(fwd) if fwd else "&mdash;"}</td></tr>'
        )
    if not bym:
        bym = ['<tr><td colspan="7" class="empty">No calls yet. '
               'All 83 numbers are live and taking messages.</td></tr>']

    calls = []
    for r in data:
        msg = (f'<span class="yes">yes &middot; {r["message_seconds"]}s</span>'
               if r["left_message"] == "yes" else '<span class="no">no</span>')
        calls.append(
            f'<tr><td class="num">{r["when_pt"]}</td><td class="wrap">{r["domain"]}</td>'
            f'<td>{r["city"]}</td><td class="num">{pretty(r["caller"])}</td>'
            f'<td class="num">{pretty(r["tracking_number"])}</td>'
            f'<td class="num">{r["seconds_on_call"]}</td><td>{msg}</td></tr>'
        )
    if not calls:
        calls = ['<tr><td colspan="7" class="empty">Nothing yet.</td></tr>']

    html = (HTML
            .replace("__STAMP__", datetime.datetime.now().strftime("%b %-d, %Y %-I:%M %p"))
            .replace("__NMARKETS__", str(len(per)))
            .replace("__TOTAL__", str(len(data)))
            .replace("__D7__", str(sum(1 for r in data if within(r, 7))))
            .replace("__D30__", str(sum(1 for r in data if within(r, 30))))
            .replace("__MSGS__", str(sum(1 for r in data if r["left_message"] == "yes")))
            .replace("__BYMARKET__", "\n".join(bym))
            .replace("__CALLS__", "\n".join(calls)))

    out = os.path.join(HERE, slug())
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w").write(html)
    print(f"wrote {out}/index.html — {len(data)} calls, {len(per)} markets")
    print(f"url: https://call-desk-xi.vercel.app/{slug()}/")


if __name__ == "__main__":
    main()
