import json, glob, os, re, subprocess, concurrent.futures as cf, gzip, io
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'
def get(u,t=20):
    try:
        p=subprocess.run(['curl','-sL','--max-time',str(t),'-A',UA,'--compressed',u],capture_output=True,timeout=t+8)
        return p.stdout
    except Exception: return b''
def urls_from(x):
    try: s=x.decode('utf-8','ignore')
    except Exception: return []
    return re.findall(r'<loc>\s*([^<\s]+)\s*</loc>', s, re.I)
def pagecount(d):
    seen=set(); idx=[]
    for c in ['https://%s/sitemap.xml'%d,'https://%s/sitemap_index.xml'%d,'https://%s/wp-sitemap.xml'%d,'https://%s/sitemap-index.xml'%d,'https://%s/sitemap1.xml'%d]:
        b=get(c)
        if b'<loc' not in b[:400000] and b'<loc' not in b: continue
        u=urls_from(b)
        subs=[x for x in u if re.search(r'\.xml(\.gz)?$',x,re.I)]
        if subs:
            idx=subs[:40]; break
        seen.update(u)
        if seen: break
    if idx:
        for s in idx:
            b=get(s)
            if s.endswith('.gz'):
                try: b=gzip.decompress(b)
                except Exception: pass
            seen.update(x for x in urls_from(b) if not re.search(r'\.xml(\.gz)?$',x,re.I))
    if not seen:
        b=get('https://%s/robots.txt'%d,12)
        for m in re.findall(r'(?i)sitemap:\s*(\S+)', b.decode('utf-8','ignore')):
            bb=get(m)
            u=urls_from(bb)
            subs=[x for x in u if re.search(r'\.xml(\.gz)?$',x,re.I)]
            if subs:
                for s in subs[:40]:
                    b2=get(s)
                    if s.endswith('.gz'):
                        try: b2=gzip.decompress(b2)
                        except Exception: pass
                    seen.update(x for x in urls_from(b2) if not re.search(r'\.xml(\.gz)?$',x,re.I))
            else: seen.update(u)
            if seen: break
    return len(seen) if seen else None
def words(u):
    b=get(u,25)
    if not b: return None
    h=b.decode('utf-8','ignore')
    h=re.sub(r'<(script|style|nav|footer|svg|noscript|head)[^>]*>.*?</\1>',' ',h,flags=re.S|re.I)
    return len(re.sub(r'<[^>]+>',' ',h).split())
tgt={}
for f in glob.glob('serp/*.json'):
    d=json.load(open(f))
    for r in d['organic'][:6]:
        if r['agg'] or not r['domain']: continue
        tgt.setdefault(r['domain'], r['url'])
tgt=list(tgt.items())
print('unique local winner domains to measure:',len(tgt),flush=True)
out={}
if os.path.exists('depth.json'): out=json.load(open('depth.json'))
todo=[(d,u) for d,u in tgt if d not in out]
print('todo',len(todo),flush=True)
def one(x):
    d,u=x
    return d,{'pages':pagecount(d),'words':words(u),'url':u}
n=0
with cf.ThreadPoolExecutor(max_workers=14) as ex:
    for d,v in ex.map(one, todo):
        out[d]=v; n+=1
        if n%100==0:
            json.dump(out,open('depth.json','w')); print(n,'measured',flush=True)
json.dump(out,open('depth.json','w')); print('DONE',len(out),flush=True)
