"""Weekly ranking check for the 10 Kyle batch 1 sites (Dan's standing OK, 26 Oct 2026).

For each site: its main search plus one search per service page, run as a desktop Google
search located in the site's city (DataForSEO live/advanced, top 100). Records where the site
appears (or that it doesn't) and saves to kyle-screen/ranks/<date>.json, then prints a table
with the change since the last saved run.

usage (from the repo root): python3 -I kyle-screen/rank_check.py
"""
import base64, glob, json, os, sys, time, urllib.request, concurrent.futures as cf

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
OUT = os.path.join(HERE, 'ranks')
ENV = dict(l.strip().split('=', 1) for l in open(os.path.expanduser('~/.dataforseo.env')) if '=' in l)
AUTH = 'Basic ' + base64.b64encode(f"{ENV['DATAFORSEO_LOGIN']}:{ENV['DATAFORSEO_PASSWORD']}".encode()).decode()
batch = json.load(open(os.path.join(HERE, 'oct-top3', 'batch1.json')))
DOMAINS = list(batch) if isinstance(batch, dict) else [x['domain'] for x in batch]


def searches(d):
    s = json.load(open(os.path.join(REPO, 'sites', d, 'site.json')))
    loc = f"{s['city']},{s['state_full']},United States"
    qs = [s['_market']['keyword']] + [x['keyword'].lower() for x in s['services'] if x.get('keyword')]
    return [(d, q, loc) for q in dict.fromkeys(qs)]


def run(job):
    d, q, loc = job
    body = json.dumps([{'keyword': q, 'location_name': loc, 'language_code': 'en', 'device': 'desktop', 'depth': 100}]).encode()
    for attempt in range(3):
        try:
            req = urllib.request.Request('https://api.dataforseo.com/v3/serp/google/organic/live/advanced', data=body,
                                         headers={'Authorization': AUTH, 'Content-Type': 'application/json'})
            t = json.loads(urllib.request.urlopen(req, timeout=120).read())['tasks'][0]
            if t.get('status_code') != 20000:
                raise RuntimeError(t.get('status_message'))
            items = t['result'][0].get('items') or []
            pos = next((x.get('rank_group') for x in items if x.get('type') == 'organic'
                        and (x.get('domain') or '').removeprefix('www.') == d), None)
            url = next((x.get('url') for x in items if x.get('type') == 'organic'
                        and (x.get('domain') or '').removeprefix('www.') == d), None)
            return {'site': d, 'query': q, 'position': pos, 'url': url, 'cost': t.get('cost')}
        except Exception as e:
            err = str(e)
            time.sleep(3)
    return {'site': d, 'query': q, 'position': None, 'url': None, 'error': err}


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    jobs = [j for d in DOMAINS for j in searches(d)]
    with cf.ThreadPoolExecutor(max_workers=5) as ex:
        res = list(ex.map(run, jobs))
    prev_files = sorted(glob.glob(os.path.join(OUT, '*.json')))
    prev = {}
    if prev_files:
        prev = {(r['site'], r['query']): r['position'] for r in json.load(open(prev_files[-1]))['results']}
    today = time.strftime('%Y-%m-%d')
    json.dump({'date': today, 'results': res}, open(os.path.join(OUT, f'{today}.json'), 'w'), indent=1)
    found = sum(1 for r in res if r['position'])
    print(f"{today}: {len(res)} searches, site found in the top 100 for {found}; cost ${sum(r.get('cost') or 0 for r in res):.3f}")
    for r in res:
        p = r['position'] or '-'
        was = prev.get((r['site'], r['query']), 'n/a')
        print(f"  {r['site']:38s} {r['query']:45s} {str(p):>4}  (last {was}){'  ERROR ' + r['error'] if r.get('error') else ''}")
