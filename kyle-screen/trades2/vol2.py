"""Add ~30 bigger home-service trades to the Aug 29 grid: Google Ads volume + CPC for each trade in
each of the 707 towns (DataForSEO search_volume live, US). Research only. Writes trades2/grid2.json."""
import json, subprocess, concurrent.futures as cf, time, os
HERE = os.path.dirname(os.path.abspath(__file__))
T = ["plumber", "water heater installation", "drain cleaning", "sewer line repair", "ac repair", "furnace repair",
     "hvac installation", "roofing contractor", "roof repair", "garage door repair", "pest control", "termite treatment",
     "bed bug exterminator", "tree removal", "tree service", "foundation repair", "water damage restoration", "mold removal",
     "locksmith", "electrician", "appliance repair", "carpet cleaning", "window replacement", "gutter cleaning",
     "concrete contractor", "sprinkler repair", "local movers", "house painters", "pool service", "lawn care",
     "septic system installation", "garage door installation", "emergency plumber"]
cities = json.load(open(os.path.join(HERE, '..', 'cities.json')))
grid = [{'niche': t, 'q': f"{t} {c['city'].lower()}", **c} for t in T for c in cities]
qs = sorted({g['q'] for g in grid})
B = [qs[i:i + 1000] for i in range(0, len(qs), 1000)]
env = dict(l.strip().split('=', 1) for l in open(os.path.expanduser('~/.dataforseo.env')) if '=' in l)
auth = f"{env['DATAFORSEO_LOGIN']}:{env['DATAFORSEO_PASSWORD']}"
os.makedirs(os.path.join(HERE, 'vol'), exist_ok=True)
def run(i):
    f = os.path.join(HERE, 'vol', f'{i}.json')
    if os.path.exists(f): return i, 'cached', 0
    body = [{"keywords": B[i], "location_code": 2840, "language_code": "en", "search_partners": False}]
    for a in range(3):
        p = subprocess.run(['curl', '-s', '--max-time', '170', '-u', auth, '-X', 'POST',
                            'https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live',
                            '-H', 'Content-Type: application/json', '-d', json.dumps(body)], capture_output=True, text=True, timeout=185)
        try:
            t = json.loads(p.stdout)['tasks'][0]
        except Exception:
            time.sleep(5); continue
        if t.get('status_code') != 20000: time.sleep(5); continue
        res = [{'q': r.get('keyword'), 'vol': r.get('search_volume'), 'cpc': r.get('cpc'), 'comp': r.get('competition')} for r in (t.get('result') or [])]
        json.dump(res, open(f, 'w')); return i, f'ok {len(res)}', t.get('cost') or 0
    return i, 'FAIL', 0
print('keywords', len(qs), 'batches', len(B), flush=True)
cost = 0
with cf.ThreadPoolExecutor(max_workers=2) as ex:
    for i, s, c in ex.map(run, range(len(B))): cost += c; print(f'batch {i}: {s}', flush=True)
m = {}
for i in range(len(B)):
    for r in json.load(open(os.path.join(HERE, 'vol', f'{i}.json'))): m[r['q']] = r
for g in grid:
    r = m.get(g['q']) or {}
    g.update(vol=r.get('vol'), cpc=r.get('cpc'), comp=r.get('comp'))
json.dump(grid, open(os.path.join(HERE, 'grid2.json'), 'w'))
print('cost $%.2f' % cost)
