"""Add one short paragraph with a link to a Kyle batch 1 site on the live home page of a few
older sites, and change nothing else.

Like swap_phone_deploy.py: the live deployment is data/manifest.json. Each source home page is
fetched, proven to match the manifest byte-for-byte, patched with one paragraph just before the
bottom call-to-action, and the same manifest is redeployed with only those hashes changed.
Undeployed work in dist/ (14-15 Sep) is not touched.

usage (from the repo root):
  uv run --with blake3 --with requests python3 -I link_from_old_deploy.py [--push TOKEN]
"""
import base64, json, os, subprocess, sys
import blake3

REPO = os.getcwd()
A = 'a3bf1a13d93899d8408b9d1ea94df078'
P = 'local-sites'
API = 'https://api.cloudflare.com/client/v4'
MARK = '\n<div class="bottom-cta">'

LINKS = {  # source home page -> paragraph HTML (Dan's OK, 31 Oct 2026)
    'mariettagaragedoorrepairpros.com':
        'Opening up the garage for a winter project tends to stir up the dust that settles in Marietta ductwork. '
        'For that job, see <a href="https://mariettaairductcleaningpros.com/">air duct cleaning in Marietta</a>.',
    'atlantaemergencyplumberpros.com':
        'Plumbing calls in older Cobb County houses often turn up ductwork that has not been touched in years. '
        'North of the city, see <a href="https://mariettaairductcleaningpros.com/">Marietta air duct cleaning</a>.',
    'garagedoorrepairnapervillepros.com':
        'Elsewhere in the western suburbs: <a href="https://wheatonairductcleaningpros.com/">air duct cleaning in Wheaton</a> '
        'and <a href="https://schaumburgairductcleaningpros.com/">Schaumburg air duct cleaning</a>.',
    'bocaratongaragedoorrepairpros.com':
        'Clearing out a garage before new doors go in? For a roll-off box in western Palm Beach County, see '
        '<a href="https://wellingtondumpsterrentalpros.com/">dumpster rental in Wellington, FL</a>.',
    'appliancerepairtampaco.com':
        'When a dryer needs two cycles to dry a load, the vent is usually the cause rather than the machine. '
        'North of Tampa, see <a href="https://dryerventcleaningocala.com/">dryer vent cleaning in Ocala</a>.',
    'tampatileroofrepair.com':
        'If the heat is coming in through the glass rather than the roof, see '
        '<a href="https://windowtintingbradenton.com/">window tinting in Bradenton</a>.',
    'jacksonvilleemergencyplumberpros.com':
        'Homes on a septic tank rather than city sewer need a pump-out, not a plumber. In Miami-Dade, see '
        '<a href="https://northmiamiseptictankpumpingpros.com/">septic tank pumping in North Miami</a>.',
}


def h(content, ext):
    return blake3.blake3((base64.b64encode(content).decode() + ext).encode()).hexdigest()[:32]


def fetch(url):
    r = subprocess.run(['curl', '-sS', '--max-time', '30', '-w', '\n%{http_code}', url], capture_output=True)
    body, _, code = r.stdout.rpartition(b'\n')
    return code.decode().strip(), body


push_token = sys.argv[sys.argv.index('--push') + 1] if '--push' in sys.argv else None
live = json.load(open(os.path.join(REPO, 'data', 'manifest.json')))
new = dict(live)
uploads = {}
for d, para in LINKS.items():
    path = f'/{d}/index.html'
    code, body = fetch(f'https://{d}/')
    if code != '200' or h(body, 'html') != live.get(path):
        sys.exit(f'ABORT: https://{d}/ is not what data/manifest.json says is live ({code}). Nothing sent.')
    text = body.decode('utf-8')
    if 'class="nearby-link"' in text:
        sys.exit(f'ABORT: {d} already has a nearby link')
    if text.count(MARK) != 1:
        sys.exit(f'ABORT: {d} has {text.count(MARK)} bottom-cta markers')
    block = ('\n<div class="band"><div class="band-inner"><p class="nearby-link">' + para + '</p></div></div>')
    patched = text.replace(MARK, block + MARK).encode('utf-8')
    new[path] = h(patched, 'html')
    uploads[new[path]] = patched
    print(f'  {d}: +1 paragraph')

changed = [k for k in new if new[k] != live[k]]
assert set(new) == set(live) and len(changed) == len(LINKS)
assert all(k.endswith('/index.html') and k.count('/') == 2 for k in changed)
print(f'{len(changed)} home pages change; {len(new) - len(changed)} live files untouched.')
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
