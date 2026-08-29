import json, subprocess, re, concurrent.futures as cf, time, os
rows=[r for r in json.load(open('kyle-screen.json')) if r['name_conflict']=='clean'][:70]
SLUG={'dumpster rental':'dumpsterrental','dryer vent cleaning':'dryerventcleaning','air duct cleaning':'airductcleaning',
'window tinting':'windowtinting','pressure washing':'pressurewashing','junk removal':'junkremoval','chimney sweep':'chimneysweep',
'roof cleaning':'roofcleaning','septic tank pumping':'septicpumping','towing service':'towing','auto glass repair':'autoglass',
'land clearing':'landclearing','paintless dent repair':'dentrepair','gutter installation':'gutterinstallation',
'stucco repair':'stuccorepair','siding repair':'sidingrepair','pool resurfacing':'poolresurfacing'}
def cands(r):
    c=re.sub(r'[^a-z]','',r['city'].lower()); s=SLUG.get(r['niche'],re.sub(r'[^a-z]','',r['niche']))
    return [f'{c}{s}.com', f'{s}{c}.com', f'{c}{s}pros.com', f'{c}{s}co.com', f'{s}of{c}.com']
def avail(d):
    tld=d.rsplit('.',1)[1]
    url=f'https://rdap.verisign.com/{tld}/v1/domain/{d}'
    for a in range(3):
        try:
            p=subprocess.run(['curl','-s','-o','/dev/null','-w','%{http_code}','--max-time','15',url],capture_output=True,text=True,timeout=20)
            code=p.stdout.strip()
            if code=='404': return True
            if code=='200': return False
            time.sleep(1.5)
        except Exception: time.sleep(1.5)
    return None
allc={}
for r in rows:
    for d in cands(r): allc[d]=None
print('checking',len(allc),'domains',flush=True)
with cf.ThreadPoolExecutor(max_workers=12) as ex:
    keys=list(allc)
    for d,v in zip(keys, ex.map(avail, keys)): allc[d]=v
out=[]
for r in rows:
    free=[d for d in cands(r) if allc.get(d) is True]
    out.append({**r,'domain':free[0] if free else '','alt':' | '.join(free[1:3])})
json.dump(out, open('kyle-batch.json','w'))
got=[r for r in out if r['domain']]
print('markets with a domain available:',len(got),'of',len(out))
for r in got[:50]:
    print(f"{r['domain']:44s} {r['niche']:24s}{r['city'][:15]:16s}{r['state']:3s} vol={r['vol']:5d} cpc=${r['cpc']:6.2f} winners={str(r['top5_pages_med']):>5s}p  score={r['score']}")
