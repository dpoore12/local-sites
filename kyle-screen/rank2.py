import json, glob, statistics as st, csv, collections
depth=json.load(open('depth.json'))
cities=json.load(open('cities.json'))
allc=json.load(open('grid.json'))
# ambiguity: does another US city (in the top-1000 by pop) share this name?
import csv as _c
raw=list(_c.DictReader(open('/tmp/cities1k.csv')))
byname=collections.defaultdict(list)
for x in raw: byname[x['City'].lower()].append((x['State'],int(x['Population'])))
def ambiguous(city,state_full,pop):
    others=[o for o in byname[city.lower()] if o[0]!=state_full]
    if not others: return 0
    big=max(o[1] for o in others)
    return 2 if big>pop else 1     # 2 = a BIGGER same-name city exists, data is polluted
rows=[]
for f in glob.glob('serp/*.json'):
    d=json.load(open(f))
    org=d['organic'][:10]
    if not org: continue
    loc=[r for r in org if not r['agg'] and r['domain']]
    def pg(r): return depth.get(r['domain'],{}).get('pages')
    def wd(r): return depth.get(r['domain'],{}).get('words')
    pc=[pg(r) for r in loc if pg(r) is not None]
    if not pc: continue
    top5=[r for r in loc if r['pos']<=5]
    p5=[pg(r) for r in top5 if pg(r) is not None]
    wc=[wd(r) for r in loc if wd(r)]
    amb=ambiguous(d['city'], d['state_full'], d['pop'])
    rows.append({'niche':d['niche'],'city':d['city'],'state':d['state'],'pop':d['pop'],
      'vol':d['vol'],'cpc':round(d['cpc'],2),'lead_value':round(d['vol']*d['cpc']),
      'query':d['q'],'name_conflict':['clean','same name elsewhere','BIGGER same name'][amb],
      'local_in_top10':len(loc),'directories_in_top10':10-len(loc),
      'top5_pages_med':st.median(p5) if p5 else '','top5_pages_min':min(p5) if p5 else '',
      'top10_pages_med':int(st.median(pc)),'top10_pages_min':min(pc),
      'winner_words_med':int(st.median(wc)) if wc else '','winners_measured':len(pc),'amb':amb})
def score(r):
    s=0
    m=r['top5_pages_med'] if r['top5_pages_med']!='' else r['top10_pages_med']
    s+= 45 if m<=25 else 38 if m<=50 else 28 if m<=100 else 18 if m<=200 else 8 if m<=400 else 0
    mn=r['top5_pages_min'] if r['top5_pages_min']!='' else r['top10_pages_min']
    s+= 20 if mn<=10 else 15 if mn<=25 else 10 if mn<=50 else 5 if mn<=100 else 0
    s+=min(20, r['lead_value']/150)
    s+=min(10, r['directories_in_top10']*2)
    if r['pop']<60000: s+=5
    if r['winners_measured']<3: s-=10          # thin measurement, less confident
    if r['amb']==2: s-=35                       # volume and competition both polluted
    elif r['amb']==1: s-=8
    return round(max(s,0),1)
for r in rows: r['score']=score(r)
rows.sort(key=lambda r:-r['score'])
for r in rows: r.pop('amb')
with open('kyle-screen.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
json.dump(rows,open('kyle-screen.json','w'))
clean=[r for r in rows if r['name_conflict']=='clean']
print('markets scored',len(rows),'| unambiguous city name',len(clean))
pcs=[r['top10_pages_med'] for r in clean]
print('winner page count (clean markets): p10 %d p25 %d med %d p75 %d'%(sorted(pcs)[len(pcs)//10],sorted(pcs)[len(pcs)//4],st.median(pcs),sorted(pcs)[3*len(pcs)//4]))
print('\nTOP 45, CLEAN CITY NAMES ONLY')
print(f"{'service':27s}{'city':17s}{'ST':3s}{'pop':>7s}{'vol':>6s}{'cpc':>7s}{'t5med':>6s}{'t5min':>6s}{'wrds':>6s}{'loc':>4s}{'sc':>6s}")
for r in clean[:45]:
    print(f"{r['niche']:27s}{r['city'][:16]:17s}{r['state']:3s}{r['pop']:7d}{r['vol']:6d}{r['cpc']:7.2f}{str(r['top5_pages_med']):>6s}{str(r['top5_pages_min']):>6s}{str(r['winner_words_med']):>6s}{r['local_in_top10']:4d}{r['score']:6.1f}")
print('\nservice mix, clean top 150:')
for n,k in collections.Counter(r['niche'] for r in clean[:150]).most_common(): print(f'  {n:28s}{k}')
