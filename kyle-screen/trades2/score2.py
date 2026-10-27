"""Grade each high-value market Kyle's way, with a cheap first pass instead of Ahrefs:
a page-one spot is WEAK when it is a small local site (not a directory, national brand or gov)
with under 1,000 estimated Google visits a month (DataForSEO Labs bulk traffic estimate, US).
STRONG = directory / national / gov, or 5,000+ visits. Else MIDDLE.
BUILD = 2+ of the top 3 weak. Finalists get the Ahrefs DR check afterwards.
Writes trades2/traffic.json and trades2/verdicts2.csv. Research only."""
import base64, csv, json, os, collections, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
ENV = dict(l.strip().split('=', 1) for l in open(os.path.expanduser('~/.dataforseo.env')) if '=' in l)
AUTH = 'Basic ' + base64.b64encode(f"{ENV['DATAFORSEO_LOGIN']}:{ENV['DATAFORSEO_PASSWORD']}".encode()).decode()
ms = json.load(open(os.path.join(HERE, 'markets2.json')))
serps = {}
for i in range(len(ms)):
    f = os.path.join(HERE, 'serp', f'{i}.json')
    if os.path.exists(f):
        serps[i] = json.load(open(f))
tf = os.path.join(HERE, 'traffic.json')
traffic = json.load(open(tf)) if os.path.exists(tf) else {}
doms = sorted({x['domain'] for s in serps.values() for x in sorted(s['organic'], key=lambda x: x['pos'] or 99)[:5]
               if x['kind'] == 'site'} - set(traffic))
cost = 0
for k in range(0, len(doms), 1000):
    body = [{'targets': doms[k:k + 1000], 'location_code': 2840, 'language_code': 'en', 'item_types': ['organic']}]
    req = urllib.request.Request('https://api.dataforseo.com/v3/dataforseo_labs/google/bulk_traffic_estimation/live',
                                 data=json.dumps(body).encode(), headers={'Authorization': AUTH, 'Content-Type': 'application/json'})
    t = json.loads(urllib.request.urlopen(req, timeout=180).read())['tasks'][0]
    cost += t.get('cost') or 0
    for it in ((t.get('result') or [{}])[0].get('items') or []):
        traffic[it['target']] = round(((it.get('metrics') or {}).get('organic') or {}).get('etv') or 0)
    for d in doms[k:k + 1000]:
        traffic.setdefault(d, 0)
json.dump(traffic, open(tf, 'w'))
def spot(x):
    if x['kind'] != 'site':
        return 'STRONG'
    t = traffic.get(x['domain'], 0)
    return 'WEAK' if t < 1000 else 'STRONG' if t >= 5000 else 'MIDDLE'
rows = []
for i, s in serps.items():
    org = sorted(s['organic'], key=lambda x: x['pos'] or 99)
    gr = [spot(x) for x in org[:5]]
    w3, w5 = gr[:3].count('WEAK'), gr.count('WEAK')
    v = 'BUILD' if w3 >= 2 else 'BUILD-B' if w3 == 1 and w5 >= 2 else 'MAYBE' if w5 else 'SKIP'
    pack = s.get('map_pack') or []
    rows.append({'verdict': v, 'trade': s['niche'], 'city': s['city'], 'state': s['state'], 'pop': s['pop'],
                 'searches': s['vol'], 'cpc': s['cpc'], 'weak_top3': w3, 'weak_top5': w5,
                 'top3': '; '.join(f"{x['domain']} ({g}{', ' + str(traffic.get(x['domain'])) + '/mo' if x['kind'] == 'site' else ''})" for x, g in zip(org[:3], gr[:3])),
                 'map_pack_max_reviews': max([p['reviews'] or 0 for p in pack], default='')})
order = {'BUILD': 0, 'BUILD-B': 1, 'MAYBE': 2, 'SKIP': 3}
rows.sort(key=lambda r: (order[r['verdict']], -(r['searches'] or 0) * (r['cpc'] or 0)))
with open(os.path.join(HERE, 'verdicts2.csv'), 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print('traffic cost $%.2f;' % cost, collections.Counter(r['verdict'] for r in rows))
print(collections.Counter(r['trade'] for r in rows if r['verdict'] == 'BUILD').most_common())
