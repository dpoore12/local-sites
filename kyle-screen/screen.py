import json, glob, collections, statistics as st
vol={}
for f in glob.glob('vol/*.json'):
    for r in json.load(open(f)):
        vol[r['q']]={'vol':r['vol'] or 0,'cpc':r['cpc'] or 0,'comp':r['comp']}
grid=json.load(open('grid.json'))
for g in grid:
    v=vol.get(g['q'],{}); g['vol']=v.get('vol',0); g['cpc']=v.get('cpc',0); g['comp']=v.get('comp')
print('grid rows',len(grid),'with volume data',sum(1 for g in grid if g['vol']>0))
# Kyle economics: rent ~= a fraction of what the leads are worth. Use vol * cpc as a lead-value proxy.
for g in grid: g['value']=g['vol']*g['cpc']
hits=[g for g in grid if g['vol']>=50 and g['cpc']>=5]
print('vol>=50 and cpc>=$5:',len(hits))
for lo in (50,70,100,150,200,300):
    print(f'  vol>={lo}: {sum(1 for g in grid if g["vol"]>=lo and g["cpc"]>=5)}')
print('\nby niche (vol>=70, cpc>=$5):')
c=collections.Counter(); vv=collections.defaultdict(list)
for g in grid:
    if g['vol']>=70 and g['cpc']>=5: c[g['niche']]+=1; vv[g['niche']].append(g)
for n,k in c.most_common():
    cp=[x['cpc'] for x in vv[n]]; vl=[x['vol'] for x in vv[n]]
    print(f'  {n:30s} {k:4d} cities   med cpc ${st.median(cp):6.2f}   med vol {st.median(vl):5.0f}')
json.dump(grid, open('grid-scored.json','w'))
