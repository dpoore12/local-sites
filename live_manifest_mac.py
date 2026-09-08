"""Rebuild the live Pages manifest by fetching every live file from the 83 domains.
Writes stage/<domain>/... and live-manifest.json (path -> cloudflare asset hash)."""
import json,base64,re,os,sys,subprocess,concurrent.futures as cf
import blake3
S=os.path.dirname(os.path.abspath(__file__)); STAGE=os.path.join(S,'stage'); os.makedirs(STAGE,exist_ok=True)
domains=list(json.load(open('data/hosting.json'))['codes'].keys())
ASSETS=['/assets/favicon.svg','/assets/hero.jpg','/assets/theme.css','/assets/work-1.jpg','/assets/work-2.jpg','/assets/work-3.jpg','/robots.txt','/sitemap.xml']
def get(url):
    r=subprocess.run(['curl','-sL','--max-time','25','-w','\n%{http_code}',url],capture_output=True)
    body,_,code=r.stdout.rpartition(b'\n')
    return code.decode().strip(),body
def h(content,ext): return blake3.blake3((base64.b64encode(content).decode()+ext).encode()).hexdigest()[:32]
def site(d):
    out={}; missing=[]
    code,sm=get(f'https://{d}/sitemap.xml')
    if code!='200': return d,out,['sitemap '+code]
    urls=re.findall(r'<loc>\s*(https?://[^<\s]+)\s*</loc>',sm.decode('utf-8','ignore'))
    paths=set()
    for u in urls:
        p=re.sub(r'^https?://[^/]+','',u)
        if not p.endswith('/'): p+='/'
        paths.add(p+'index.html')
    paths.update(ASSETS)
    for p in sorted(paths):
        code,body=get(f'https://{d}{p}')
        if code!='200' or not body: missing.append(f'{p} {code}'); continue
        fp=os.path.join(STAGE,d,p.lstrip('/')); os.makedirs(os.path.dirname(fp),exist_ok=True)
        open(fp,'wb').write(body)
        out['/'+d+p]=h(body,p.rsplit('.',1)[-1])
    return d,out,missing
manifest={}; report={}
with cf.ThreadPoolExecutor(max_workers=12) as pool:
    for d,out,missing in pool.map(site,domains):
        manifest.update(out); report[d]=(len(out),missing)
        print(f'{d}: {len(out)} files' + (f'  MISSING {missing}' if missing else ''), flush=True)
json.dump(manifest,open(os.path.join(S,'live-manifest.json'),'w'),indent=0)
print('TOTAL files:',len(manifest),'sites:',len(report))
