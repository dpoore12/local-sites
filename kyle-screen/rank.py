import json, glob, statistics as st, csv, collections
depth=json.load(open('depth.json'))
rows=[]
for f in glob.glob('serp/*.json'):
    d=json.load(open(f))
    org=d['organic'][:10]
    if not org: continue
    loc=[r for r in org if not r['agg'] and r['domain']]
    pc=[depth[r['domain']]['pages'] for r in loc if r['domain'] in depth and depth[r['domain']]['pages'] is not None]
    wc=[depth[r['domain']]['words'] for r in loc if r['domain'] in depth and depth[r['domain']]['words']]
    if not pc: continue
    weakest=min(pc)
    # weakest LOCAL site actually sitting in the top 5
    top5=[r for r in loc if r['pos']<=5]
    p5=[depth[r['domain']]['pages'] for r in top5 if r['domain'] in depth and depth[r['domain']]['pages'] is not None]
    rows.append({'niche':d['niche'],'city':d['city'],'state':d['state'],'pop':d['pop'],
      'vol':d['vol'],'cpc':round(d['cpc'],2),'value':round(d['vol']*d['cpc']),
      'q':d['q'],'local_in_top10':len(loc),'aggs_in_top10':10-len(loc),
      'winner_pages_med':int(st.median(pc)),'winner_pages_min':weakest,
      'top5_pages_med':int(st.median(p5)) if p5 else '', 'top5_pages_min':min(p5) if p5 else '',
      'winner_words_med':int(st.median(wc)) if wc else '', 'measured':len(pc)})
print('markets scored:',len(rows))
pcs=[r['winner_pages_med'] for r in rows]
print('winner median page count across markets: p10 %d p25 %d med %d p75 %d'%(
  sorted(pcs)[len(pcs)//10],sorted(pcs)[len(pcs)//4],st.median(pcs),sorted(pcs)[3*len(pcs)//4]))
# WINNABLE = weakest top-5 local site is small enough that a 35-page build competes
def score(r):
    s=0
    m=r['top5_pages_med'] if r['top5_pages_med']!='' else r['winner_pages_med']
    if m<=25: s+=45
    elif m<=50: s+=38
    elif m<=100: s+=28
    elif m<=200: s+=18
    elif m<=400: s+=8
    mn=r['top5_pages_min'] if r['top5_pages_min']!='' else r['winner_pages_min']
    if mn<=10: s+=20
    elif mn<=25: s+=15
    elif mn<=50: s+=10
    elif mn<=100: s+=5
    s+=min(20, r['value']/150)                      # lead value
    s+=min(10, r['aggs_in_top10']*2)                # directories = softer real competition
    if r['pop']<60000: s+=5
    return round(s,1)
for r in rows: r['score']=score(r)
rows.sort(key=lambda r:-r['score'])
cols=list(rows[0].keys())
with open('kyle-screen.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=cols); w.writeheader(); w.writerows(rows)
json.dump(rows,open('kyle-screen.json','w'))
print('\nTOP 40')
print(f"{'niche':26s} {'city':16s}{'ST':3s}{'pop':>7s}{'vol':>6s}{'cpc':>8s}{'top5med':>8s}{'min':>5s}{'loc':>4s}{'score':>7s}")
for r in rows[:40]:
    print(f"{r['niche']:26s} {r['city'][:15]:16s}{r['state']:3s}{r['pop']:7d}{r['vol']:6d}{r['cpc']:8.2f}{str(r['top5_pages_med']):>8s}{str(r['top5_pages_min']):>5s}{r['local_in_top10']:4d}{r['score']:7.1f}")
print('\nniche mix in top 120:')
for n,k in collections.Counter(r['niche'] for r in rows[:120]).most_common(): print(' ',n,k)
