import json,base64,os,sys,mimetypes,requests,blake3,shutil
S=os.path.dirname(os.path.abspath(__file__)); STAGE=os.path.join(S,'stage')
A='a3bf1a13d93899d8408b9d1ea94df078'; P='local-sites'; API='https://api.cloudflare.com/client/v4'
TOK=sys.argv[1]; NEW=sys.argv[2:]
H={'Authorization':f'Bearer {TOK}'}
manifest=json.load(open(os.path.join(S,'live-manifest.json')))
old=json.load(open('data/manifest.json'))
gone=[p for p in old if p not in manifest]
print('paths in Aug-23 manifest but not fetched now:',len(gone), gone[:10])
def h(content,ext): return blake3.blake3((base64.b64encode(content).decode()+ext).encode()).hexdigest()[:32]
# add new sites from dist
for d in NEW:
    src=os.path.join('dist',d)
    for root,_,files in os.walk(src):
        for f in files:
            fp=os.path.join(root,f); rel='/'+os.path.relpath(fp,'dist').replace(os.sep,'/')
            body=open(fp,'rb').read(); manifest[rel]=h(body,f.rsplit('.',1)[-1])
            dst=os.path.join(STAGE,rel.lstrip('/')); os.makedirs(os.path.dirname(dst),exist_ok=True); shutil.copyfile(fp,dst)
print('manifest size with new sites:',len(manifest))
# upload token
r=requests.get(f'{API}/accounts/{A}/pages/projects/{P}/upload-token',headers=H).json()
jwt=r['result']['jwt']; J={'Authorization':f'Bearer {jwt}'}
hashes=sorted(set(manifest.values()))
missing=set()
for i in range(0,len(hashes),1000):
    r=requests.post(f'{API}/pages/assets/check-missing',headers=J,json={'hashes':hashes[i:i+1000]}).json()
    if not r.get('success'): print('check-missing failed',r); sys.exit(1)
    missing.update(r['result'])
byhash={v:k for k,v in manifest.items()}
new_paths={p for p in manifest if any(p.startswith('/'+d+'/') for d in NEW)}
missing_existing=[byhash[x] for x in missing if byhash[x] not in new_paths]
print('missing hashes total:',len(missing),'| of which belong to EXISTING sites:',len(missing_existing), missing_existing[:5])
ALLOW={"/cincinnatipersonalinjurylawyerpros.com/nursing-home-neglect/index.html","/cincinnatipersonalinjurylawyerpros.com/wrongful-death-claims-in-ohio/index.html"}
missing_existing=[p for p in missing_existing if p not in ALLOW]
if missing_existing:
    print('ABORT: existing-site files would be re-uploaded; live manifest reconstruction is not exact'); sys.exit(2)
# upload new files
payload=[]
for x in missing:
    p=byhash[x]; fp=os.path.join(STAGE,p.lstrip('/')); body=open(fp,'rb').read()
    ct=mimetypes.guess_type(fp)[0] or 'application/octet-stream'
    payload.append({'key':x,'value':base64.b64encode(body).decode(),'metadata':{'contentType':ct},'base64':True})
for i in range(0,len(payload),50):
    r=requests.post(f'{API}/pages/assets/upload',headers=J,json=payload[i:i+50]).json()
    if not r.get('success'): print('upload failed',r); sys.exit(1)
print('uploaded',len(payload),'new files')
r=requests.post(f'{API}/pages/assets/upsert-hashes',headers=J,json={'hashes':hashes}).json()
print('upsert-hashes:',r.get('success'),r.get('errors'))
json.dump(manifest,open(os.path.join(S,'deploy-manifest.json'),'w'))
# deploy with the current router
files={'manifest':(None,json.dumps(manifest)),'branch':(None,'main'),'_worker.js':('_worker.js',open('router/_worker.js','rb').read(),'application/javascript')}
r=requests.post(f'{API}/accounts/{A}/pages/projects/{P}/deployments',headers=H,files=files).json()
print('DEPLOY:',r.get('success'),(r.get('result') or {}).get('url'),r.get('errors'))
