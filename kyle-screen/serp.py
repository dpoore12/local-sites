import json, subprocess, os, time, concurrent.futures as cf
C=json.load(open('candidates.json')); os.makedirs('serp',exist_ok=True)
AGG={'yelp.com','reddit.com','thumbtack.com','angi.com','homeadvisor.com','bbb.org','nextdoor.com','facebook.com','mapquest.com','yellowpages.com','porch.com','houzz.com','tripadvisor.com','indeed.com','craigslist.org','manta.com','birdeye.com','expertise.com','threebestrated.com','superpages.com','chamberofcommerce.com','justdial.com','buildzoom.com','angieslist.com','trustpilot.com','instagram.com','tiktok.com','youtube.com','pinterest.com','linkedin.com','x.com','twitter.com','apple.com','google.com','dexknows.com','citysearch.com','local.com','yellowbook.com','opendi.us','cylex.us.com','hotfrog.com','brownbook.net','wikipedia.org','carwise.com','repairpal.com','openbay.com','fixr.com','homeguide.com','thumbtack.ca','networx.com','modernize.com','hometownlocal.com','budgetdumpster.com','dumpsters.com','hometown-dumpster.com','waste-management.com','wm.com','republicservices.com','1800gotjunk.com','junk-king.com','collegehunkshaulingjunk.com','safelite.com','glass.com','ziebart.com','llumar.com','chimneysafety.org','csia.org','nadca.com','angi.ca','homes.com','realtor.com','zillow.com','trulia.com','redfin.com'}
def dom(u):
    try: return u.split('/')[2].lower().replace('www.','')
    except: return ''
def run(i):
    f=f'serp/{i}.json'
    if os.path.exists(f): return i,'cached'
    c=C[i]
    body=[{"keyword":c['q'],"location_name":f"{c['city']},{c['state_full']},United States","language_code":"en","device":"desktop","depth":20}]
    for a in range(4):
        try:
            p=subprocess.run(['curl','-s','--max-time','120','-X','POST','https://api.dataforseo.com/v3/serp/google/organic/live/regular',
              '-H','Content-Type: application/json','-d',json.dumps(body)],capture_output=True,text=True,timeout=140)
            d=json.loads(p.stdout); t=d['tasks'][0]
            if t.get('status_code')!=20000: time.sleep(4+a*4); continue
            items=(t['result'][0].get('items') or [])
            org=[x for x in items if x.get('type')=='organic']
            rows=[]
            for pos,x in enumerate(org,1):
                dd=dom(x.get('url','') or '')
                rows.append({'pos':pos,'domain':dd,'url':x.get('url'),'agg':dd in AGG or any(dd.endswith('.'+a) for a in AGG)})
            json.dump({**c,'organic':rows}, open(f,'w')); return i,f'ok {len(rows)}'
        except Exception: time.sleep(4+a*4)
    return i,'FAIL'
with cf.ThreadPoolExecutor(max_workers=1) as ex:
    ok=fa=0
    for i,s in ex.map(run, range(len(C))):
        if s=='FAIL': fa+=1
        else: ok+=1
        if (ok+fa)%50==0: print(f'{ok+fa}/{len(C)} ok={ok} fail={fa}',flush=True)
print('done ok',ok,'fail',fa)
