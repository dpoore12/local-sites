import json, subprocess, concurrent.futures as cf, time, os
grid=json.load(open('grid.json'))
qs=sorted({g['q'] for g in grid})
B=[qs[i:i+1000] for i in range(0,len(qs),1000)]
print('unique keywords',len(qs),'batches',len(B),flush=True)
os.makedirs('vol',exist_ok=True)
def run(i):
    f=f'vol/{i}.json'
    if os.path.exists(f): return i,'cached'
    body=[{"keywords":B[i],"location_code":2840,"language_code":"en","search_partners":False}]
    for a in range(3):
        try:
            p=subprocess.run(['curl','-s','--max-time','170','-X','POST','https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live',
              '-H','Content-Type: application/json','-d',json.dumps(body)],capture_output=True,text=True,timeout=185)
            d=json.loads(p.stdout); t=d['tasks'][0]
            if t.get('status_code')!=20000: time.sleep(5); continue
            res=[{'q':r.get('keyword'),'vol':r.get('search_volume'),'cpc':r.get('cpc'),'comp':r.get('competition')} for r in (t.get('result') or [])]
            json.dump(res, open(f,'w')); return i,f'ok {len(res)}'
        except Exception as e:
            time.sleep(5); last=str(e)[:60]
    return i,'FAIL'
with cf.ThreadPoolExecutor(max_workers=1) as ex:
    for i,s in ex.map(run, range(len(B))): print(f'batch {i}: {s}',flush=True)
