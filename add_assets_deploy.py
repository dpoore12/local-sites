"""Add new files (photos) to sites that are already live, without changing anything else.

add_sites_deploy.py refuses any domain that is already live. This one takes live domains,
adds only the files in dist/<domain>/ that the live manifest doesn't have yet, and refuses if
any file that IS live would change. Before sending, it fetches each domain's home page and
checks the bytes still match the manifest, so a stale data/manifest.json can't roll anything back.

Projects: `local-sites` (data/manifest.json, written back on success) and `local-sites-2`
(Pensacola only; its manifest is that domain's slice of data/manifest.json, and the new one is
saved to data/manifest-local-sites-2.json).

usage (from the repo root; token value is the part after '=' in ~/.local-sites-token):
  uv run --with blake3 --with requests python3 add_assets_deploy.py DOMAIN ... [--project P]               # dry run
  uv run --with blake3 --with requests python3 add_assets_deploy.py DOMAIN ... [--project P] --push TOKEN
"""
import base64, json, mimetypes, os, subprocess, sys
import blake3

REPO = os.path.dirname(os.path.abspath(__file__))
A = 'a3bf1a13d93899d8408b9d1ea94df078'
API = 'https://api.cloudflare.com/client/v4'


def h(content, ext):
    return blake3.blake3((base64.b64encode(content).decode() + ext).encode()).hexdigest()[:32]


args = sys.argv[1:]
token, P = None, 'local-sites'
if '--push' in args:
    i = args.index('--push'); token = args[i + 1]; del args[i:i + 2]
if '--project' in args:
    i = args.index('--project'); P = args[i + 1]; del args[i:i + 2]
domains = args
if not domains or P not in ('local-sites', 'local-sites-2'):
    sys.exit(__doc__)

main = json.load(open(os.path.join(REPO, 'data', 'manifest.json')))
if P == 'local-sites':
    live = main
else:
    live = {k: v for k, v in main.items() if any(k.startswith('/' + d + '/') for d in domains)}
new, files = dict(live), {}
for d in domains:
    root = os.path.join(REPO, 'dist', d)
    if not any(k.startswith('/' + d + '/') for k in live):
        sys.exit(f'ABORT: {d} is not live in {P}; use add_sites_deploy.py for new sites')
    if 'Disallow: /' in open(os.path.join(root, 'robots.txt')).read():
        sys.exit(f'ABORT: {d} robots.txt is noindex; rebuild with --live')
    home = subprocess.run(['curl', '-sf', f'https://{d}/'], capture_output=True).stdout
    if h(home, 'html') != live.get(f'/{d}/index.html'):
        sys.exit(f'ABORT: https://{d}/ does not match the manifest; it is stale, not deploying')
    for r, _, fs in os.walk(root):
        for f in fs:
            fp = os.path.join(r, f)
            key = '/' + os.path.relpath(fp, os.path.join(REPO, 'dist')).replace(os.sep, '/')
            body = open(fp, 'rb').read()
            hv = h(body, f.rsplit('.', 1)[-1] if '.' in f else '')
            files[hv] = (fp, body)  # also lets a project's store be topped up with bytes it never got
            if key in live:
                if live[key] != hv:
                    sys.exit(f'ABORT: {key} differs from live; this script only adds files')
                continue
            new[key] = hv
added = sorted(k for k in new if k not in live)
print(f'{P}: {len(added)} files added; {len(live)} live files unchanged.')
for k in added:
    print('  +', k)
if not token:
    print('DRY RUN: nothing sent.')
    sys.exit(0)

import requests
H = {'Authorization': f'Bearer {token}'}
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
unknown = missing - set(files)
if unknown:
    sys.exit(f'ABORT: {len(unknown)} live hashes are missing from Cloudflare\'s store; not deploying.')
payload = [{'key': k, 'value': base64.b64encode(files[k][1]).decode(),
            'metadata': {'contentType': mimetypes.guess_type(files[k][0])[0] or 'application/octet-stream'},
            'base64': True} for k in missing]
for i in range(0, len(payload), 20):
    r = requests.post(f'{API}/pages/assets/upload', headers=J, json=payload[i:i + 20]).json()
    if not r.get('success'):
        sys.exit(f'ABORT: upload {r}')
print('uploaded', len(payload), 'new files')
r = requests.post(f'{API}/pages/assets/upsert-hashes', headers=J, json={'hashes': hashes}).json()
print('upsert-hashes:', r.get('success'), r.get('errors'))
fl = {'manifest': (None, json.dumps(new)), 'branch': (None, 'main'),
      '_worker.js': ('_worker.js', open(os.path.join(REPO, 'router', '_worker.js'), 'rb').read(),
                     'application/javascript')}
r = requests.post(f'{API}/accounts/{A}/pages/projects/{P}/deployments', headers=H, files=fl).json()
print('DEPLOY:', r.get('success'), (r.get('result') or {}).get('url'), r.get('errors'))
if r.get('success'):
    out = 'manifest.json' if P == 'local-sites' else 'manifest-local-sites-2.json'
    json.dump(new, open(os.path.join(REPO, 'data', out), 'w'))
    print(f'data/{out} updated to the new live manifest')
