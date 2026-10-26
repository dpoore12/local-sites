"""Score the 191 clean markets the way Kyle sizes up a market, from oct_top3.py's data.

A page-one spot is WEAK when it is held by a small local site: not a directory, not a national
brand, Ahrefs Domain Rating 15 or under and under 2,000 visits a month ("Joe, Bill and Steve").
It is STRONG when a directory, national brand, government site or a DR 30+ site holds it.
Anything else is MIDDLE.

Verdict, in Kyle's terms (he builds where he can "do 10% better" than the top three):
  BUILD   2 or 3 of the top 3 spots are weak
  BUILD-B 1 of the top 3 is weak and at least 2 of the top 5 are weak (spot 3-5 still gets calls)
  MAYBE   exactly 1 weak spot in the top 5
  SKIP    no weak spot in the top 5

usage (from kyle-screen/): python3 -I oct_score.py
"""
import csv, json, os, re, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'oct-top3')

dr = {}
for line in open(os.path.join(OUT, 'dr.txt')):
    d, r, t = line.split()
    dr[d] = (float(r), int(t))
pages = json.load(open(os.path.join(OUT, 'pages.json')))
first70 = {(r['niche'], r['city'], r['state']): r['domain'] for r in json.load(open(os.path.join(HERE, 'kyle-batch.json')))}


def spot(o):
    if o['kind'] == 'directory':
        return 'STRONG', 'directory'
    if o['kind'] in ('national', 'gov/edu'):
        return 'STRONG', o['kind']
    r, t = dr.get(o['domain'], (None, None))
    if r is None:
        return 'MIDDLE', 'no data'
    if r >= 30:
        return 'STRONG', f'DR {r:g}'
    if r <= 15 and t < 2000:
        return 'WEAK', f'DR {r:g}'
    return 'MIDDLE', f'DR {r:g}'


def looks_rank_and_rent(domain, niche, city):
    d = domain.replace('-', '')
    c = city.lower().replace(' ', '').replace('.', '')
    words = [w for w in niche.lower().split() if len(w) > 3]
    return c in d and any(w[:5] in d for w in words)


rows = []
for f in sorted(os.listdir(os.path.join(OUT, 'serp')), key=lambda x: int(x.split('.')[0])):
    m = json.load(open(os.path.join(OUT, 'serp', f)))
    org = sorted(m['organic'], key=lambda o: o['pos'] or 99)
    top5 = org[:5]
    grades = [spot(o) for o in top5]
    w3 = sum(1 for g in grades[:3] if g[0] == 'WEAK')
    w5 = sum(1 for g in grades if g[0] == 'WEAK')
    if w3 >= 2:
        verdict = 'BUILD'
    elif w3 == 1 and w5 >= 2:
        verdict = 'BUILD-B'
    elif w5 >= 1:
        verdict = 'MAYBE'
    else:
        verdict = 'SKIP'
    weak_pages = [pages.get(o['url'], {}) for o, g in zip(top5[:3], grades[:3]) if g[0] == 'WEAK']
    words = [p['words'] for p in weak_pages if p.get('words')]
    imgs = [p['images'] for p in weak_pages if p.get('images') is not None]
    pack = m.get('map_pack') or []
    reviews = [p['reviews'] or 0 for p in pack]
    rr = sum(1 for o, g in zip(top5, grades) if g[0] == 'WEAK' and looks_rank_and_rent(o['domain'], m['niche'], m['city']))
    top3_txt = '; '.join(f"{o['pos']}. {o['domain']} ({g[1]})" for o, g in zip(org[:3], grades[:3]))
    rows.append({
        'verdict': verdict, 'niche': m['niche'], 'city': m['city'], 'state': m['state'], 'pop': m['pop'],
        'searches': m['vol'], 'cpc': m['cpc'], 'lead_value': m['lead_value'],
        'weak_top3': w3, 'weak_top5': w5, 'top3': top3_txt,
        'weak_page_words_max': max(words) if words else '', 'weak_page_images_med': statistics.median(imgs) if imgs else '',
        'winner_pages_med_aug': m.get('top5_pages_med'),
        'map_pack': len(pack), 'map_pack_max_reviews': max(reviews) if reviews else '',
        'rank_and_renters_in_top5': rr,
        'domain_aug29': first70.get((m['niche'], m['city'], m['state']), ''),
        'query': m['query'],
    })

order = {'BUILD': 0, 'BUILD-B': 1, 'MAYBE': 2, 'SKIP': 3}
rows.sort(key=lambda r: (order[r['verdict']], -r['lead_value']))
with open(os.path.join(OUT, 'kyle-verdicts.csv'), 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
import collections
print(collections.Counter(r['verdict'] for r in rows))
print(collections.Counter(r['niche'] for r in rows if r['verdict'] in ('BUILD', 'BUILD-B')).most_common())
