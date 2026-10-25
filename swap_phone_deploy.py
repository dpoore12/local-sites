"""Swap one site's phone number on the live local-sites deployment and change nothing else.

The live deployment is data/manifest.json (the 8 Sep push). This fetches every live file
of the one domain, proves each matches that manifest byte-for-byte, replaces the number in
the pages that show it, and redeploys the same manifest with only those hashes changed.
Undeployed work in dist/ (14-15 Sep) is not touched.

usage (run from the local-sites repo):
  uv run --with blake3 --with requests python3 -I swap_phone_deploy.py DOMAIN OLD_DISPLAY NEW_DISPLAY OLD_TEL NEW_TEL [--push TOKEN]
"""
import base64, json, os, re, subprocess, sys
import blake3

REPO = os.getcwd()
A = 'a3bf1a13d93899d8408b9d1ea94df078'
P = 'local-sites'
API = 'https://api.cloudflare.com/client/v4'


def h(content, ext):
    return blake3.blake3((base64.b64encode(content).decode() + ext).encode()).hexdigest()[:32]


def fetch(url):
    r = subprocess.run(['curl', '-sS', '--max-time', '30', '-w', '\n%{http_code}', url], capture_output=True)
    body, _, code = r.stdout.rpartition(b'\n')
    return code.decode().strip(), body


domain, old_d, new_d, old_t, new_t = sys.argv[1:6]
push_token = sys.argv[sys.argv.index('--push') + 1] if '--push' in sys.argv else None

live = json.load(open(os.path.join(REPO, 'data', 'manifest.json')))
new = dict(live)
uploads = {}
for path in sorted(k for k in live if k.startswith(f'/{domain}/')):
    rel = path[len(domain) + 1:]
    url = f'https://{domain}' + (rel[:-len('index.html')] if rel.endswith('index.html') else rel)
    code, body = fetch(url)
    ext = path.rsplit('.', 1)[-1]
    if code != '200' or h(body, ext) != live[path]:
        sys.exit(f'ABORT: {url} is not what data/manifest.json says is live ({code}). Nothing sent.')
    if ext != 'html':
        continue
    text = body.decode('utf-8')
    n = text.count(old_d) + text.count(old_t)
    if not n:
        continue
    patched = text.replace(old_d, new_d).replace(old_t, new_t).encode('utf-8')
    new[path] = h(patched, ext)
    uploads[new[path]] = patched
    print(f'  {path}: {n} replacements')

tail = old_t[-7:-4] + '[-. )]*' + old_t[-4:]  # e.g. 402[-. )]*0614, catches any other format
left = [k for k, b in uploads.items() if re.search(tail.encode(), b)]
changed = [k for k in new if new[k] != live[k]]
print(f'{len(changed)} files change, all under /{domain}/; {len(new)} files in the deployment (same as live).')
assert all(k.startswith(f'/{domain}/') for k in changed) and set(new) == set(live) and not left

if not push_token:
    print('DRY RUN: nothing sent. Add --push <token> to deploy.')
    sys.exit(0)

import requests
H = {'Authorization': f'Bearer {push_token}'}
r = requests.get(f'{API}/accounts/{A}/pages/projects/{P}/upload-token', headers=H).json()
if not r.get('success'):
    sys.exit(f'ABORT: upload token: {r.get("errors")}')
J = {'Authorization': f'Bearer {r["result"]["jwt"]}'}
hashes = sorted(set(new.values()))
missing = set()
for i in range(0, len(hashes), 1000):
    r = requests.post(f'{API}/pages/assets/check-missing', headers=J, json={'hashes': hashes[i:i + 1000]}).json()
    if not r.get('success'):
        sys.exit(f'ABORT: check-missing {r}')
    missing.update(r['result'])
unknown = missing - set(uploads)
if unknown:
    sys.exit(f'ABORT: {len(unknown)} live hashes are missing from Cloudflare\'s store; not deploying.')
payload = [{'key': k, 'value': base64.b64encode(uploads[k]).decode(),
            'metadata': {'contentType': 'text/html'}, 'base64': True} for k in missing]
if payload:
    r = requests.post(f'{API}/pages/assets/upload', headers=J, json=payload).json()
    if not r.get('success'):
        sys.exit(f'ABORT: upload {r}')
print('uploaded', len(payload), 'new files')
r = requests.post(f'{API}/pages/assets/upsert-hashes', headers=J, json={'hashes': hashes}).json()
print('upsert-hashes:', r.get('success'), r.get('errors'))
files = {'manifest': (None, json.dumps(new)), 'branch': (None, 'main'),
         '_worker.js': ('_worker.js', open(os.path.join(REPO, 'router', '_worker.js'), 'rb').read(),
                        'application/javascript')}
r = requests.post(f'{API}/accounts/{A}/pages/projects/{P}/deployments', headers=H, files=files).json()
print('DEPLOY:', r.get('success'), (r.get('result') or {}).get('url'), r.get('errors'))
if r.get('success'):
    json.dump(new, open(os.path.join(REPO, 'data', 'manifest.json'), 'w'))
    print('data/manifest.json updated to the new live manifest')
