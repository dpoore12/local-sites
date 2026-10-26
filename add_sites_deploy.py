"""Add new sites to the live local-sites deployment without touching the existing ones.

The live deployment is data/manifest.json. This adds the built files of the named domains
(dist/<domain>/, from `template/build.py --live <domain> ...`) to that manifest, refuses if any
existing path would change, uploads only the new bytes, and posts the deployment with the same
router. Then, with --hookup, it attaches each domain to the Pages project and points its DNS at it
(the same steps host_all.py hook_up uses).

usage (from the repo root; token value is the part after '=' in ~/.local-sites-token):
  uv run --with blake3 --with requests python3 add_sites_deploy.py DOMAIN ...                 # dry run
  uv run --with blake3 --with requests python3 add_sites_deploy.py DOMAIN ... --push TOKEN
  uv run --with blake3 --with requests python3 add_sites_deploy.py DOMAIN ... --hookup TOKEN
"""
import base64, json, mimetypes, os, sys
import blake3

REPO = os.path.dirname(os.path.abspath(__file__))
A = 'a3bf1a13d93899d8408b9d1ea94df078'
P = 'local-sites'
API = 'https://api.cloudflare.com/client/v4'


def h(content, ext):
    return blake3.blake3((base64.b64encode(content).decode() + ext).encode()).hexdigest()[:32]


args = sys.argv[1:]
token = None
mode = 'dry'
for flag in ('--push', '--hookup'):
    if flag in args:
        i = args.index(flag)
        token = args[i + 1]
        mode = flag[2:]
        del args[i:i + 2]
domains = args
if not domains:
    sys.exit(__doc__)

live = json.load(open(os.path.join(REPO, 'data', 'manifest.json')))
new, files = dict(live), {}
for d in ([] if mode == 'hookup' else domains):
    root = os.path.join(REPO, 'dist', d)
    if not os.path.isdir(root):
        sys.exit(f'ABORT: {root} missing; build it with template/build.py --live {d}')
    robots = open(os.path.join(root, 'robots.txt')).read()
    if 'Disallow: /' in robots:
        sys.exit(f'ABORT: {d} robots.txt is noindex; rebuild with --live')
    for r, _, fs in os.walk(root):
        for f in fs:
            fp = os.path.join(r, f)
            key = '/' + os.path.relpath(fp, os.path.join(REPO, 'dist')).replace(os.sep, '/')
            if key in live:
                sys.exit(f'ABORT: {key} already live; this script only adds new sites')
            body = open(fp, 'rb').read()
            hv = h(body, f.rsplit('.', 1)[-1] if '.' in f else '')
            new[key] = hv
            files[hv] = (fp, body)
added = [k for k in new if k not in live]
assert all(live[k] == new[k] for k in live)
if mode != 'hookup':
    print(f'{len(added)} files added across {len(domains)} new sites; {len(live)} live files unchanged.')
    for d in domains:
        print(f'  {d}: {sum(1 for k in added if k.startswith("/" + d + "/"))} files')

if mode == 'dry':
    print('DRY RUN: nothing sent.')
    sys.exit(0)

import requests
H = {'Authorization': f'Bearer {token}'}

if mode == 'push':
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
    payload = []
    for k in missing:
        fp, body = files[k]
        payload.append({'key': k, 'value': base64.b64encode(body).decode(),
                        'metadata': {'contentType': mimetypes.guess_type(fp)[0] or 'application/octet-stream'},
                        'base64': True})
    for i in range(0, len(payload), 50):
        r = requests.post(f'{API}/pages/assets/upload', headers=J, json=payload[i:i + 50]).json()
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
        json.dump(new, open(os.path.join(REPO, 'data', 'manifest.json'), 'w'))
        print('data/manifest.json updated to the new live manifest')

if mode == 'hookup':
    target = (requests.get(f'{API}/accounts/{A}/pages/projects/{P}', headers=H).json().get('result') or {}).get('subdomain') or f'{P}.pages.dev'
    for d in domains:
        r = requests.post(f'{API}/accounts/{A}/pages/projects/{P}/domains', headers=H, json={'name': d}).json()
        attach = 'ok' if r.get('success') else r.get('errors')
        z = (requests.get(f'{API}/zones', headers=H, params={'name': d}).json().get('result') or [])
        if not z:
            print(d, 'attach', attach, '| NO ZONE')
            continue
        zid = z[0]['id']
        recs = requests.get(f'{API}/zones/{zid}/dns_records', headers=H, params={'per_page': 100}).json().get('result') or []
        have = [x for x in recs if x['name'] == d and x['type'] in ('A', 'AAAA', 'CNAME')]
        if any(x['type'] == 'CNAME' and x['content'] == target for x in have):
            dns = 'already'
        else:
            for x in have:
                requests.delete(f'{API}/zones/{zid}/dns_records/{x["id"]}', headers=H)
            w = requests.post(f'{API}/zones/{zid}/dns_records', headers=H,
                              json={'type': 'CNAME', 'name': d, 'content': target, 'ttl': 1, 'proxied': True}).json()
            dns = 'ok' if w.get('success') else w.get('errors')
        print(d, '| attach', attach, '| dns', dns)
