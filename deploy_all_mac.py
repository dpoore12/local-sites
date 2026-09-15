"""Dist-authoritative Cloudflare Pages deploy for local-sites.

Safer replacement for deploy_add_mac.py. That script could only ADD brand-new
sites and aborted on any change to an existing site, because it reconstructed
the "live" manifest by re-fetching pages (never exact). This one is
dist-authoritative: the manifest is the blake3 hash of the actual built bytes
on disk, so there is nothing to reconstruct and no need to freeze existing
sites. A Cloudflare Pages deployment's manifest is the COMPLETE file listing;
unchanged files' hashes already live in Cloudflare's content-addressed store,
so only genuinely-new bytes upload, while the manifest still describes the
whole site.

TWO MODES:

  DRY RUN (default -- no token, writes NOTHING to Cloudflare):
      uv run --with blake3 --with requests python3 deploy_all_mac.py
    Reads dist/ (build it fresh with --live first), computes the exact
    manifest, hard-checks every robots.txt is index-allowed, diffs against
    data/manifest.json (the last committed live manifest), prints
    added/removed/changed, and writes deploy-manifest.json for the push step.

  PUSH (only after a dry run has been reviewed):
      uv run --with blake3 --with requests python3 deploy_all_mac.py --push <token>
    Uploads only the missing hashes, then POSTs the full reviewed manifest
    plus router/_worker.js as a new deployment.

The build MUST have been produced with --live. If any dist robots.txt says
Disallow, this script aborts before doing anything -- a noindex deploy would
pull the whole network out of Google.
"""
import json, base64, os, sys, mimetypes
import blake3

S = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(S, 'dist')
BASELINE = os.path.join(S, 'data', 'manifest.json')
PREVIEW = os.path.join(S, 'deploy-manifest.json')
A = 'a3bf1a13d93899d8408b9d1ea94df078'
P = 'local-sites'
API = 'https://api.cloudflare.com/client/v4'


def h(content, ext):
    """Cloudflare Pages asset hash: blake3(base64(content)+ext)[:32]."""
    return blake3.blake3((base64.b64encode(content).decode() + ext).encode()).hexdigest()[:32]


def compute_manifest():
    """Walk dist/, return {'/<domain>/<relpath>': hash} for every file."""
    manifest = {}
    for root, _, files in os.walk(DIST):
        for f in files:
            fp = os.path.join(root, f)
            rel = '/' + os.path.relpath(fp, DIST).replace(os.sep, '/')
            body = open(fp, 'rb').read()
            manifest[rel] = h(body, f.rsplit('.', 1)[-1] if '.' in f else '')
    return manifest


def safety_check_robots():
    """Every built site must be index-allowed. Abort loudly on any noindex."""
    bad = []
    for d in sorted(os.listdir(DIST)):
        rp = os.path.join(DIST, d, 'robots.txt')
        if not os.path.isdir(os.path.join(DIST, d)):
            continue
        if not os.path.exists(rp):
            bad.append(f'{d}: no robots.txt built')
            continue
        txt = open(rp).read()
        if 'Disallow: /' in txt or 'Allow: /' not in txt:
            bad.append(f'{d}: robots.txt is NOT index-allowed (noindex build)')
    return bad


def dry_run():
    if not os.path.isdir(DIST) or not os.listdir(DIST):
        print('ABORT: dist/ is empty. Build first:')
        print('  uv run --with jinja2 --with markdown python3 template/build.py --live')
        sys.exit(2)

    bad = safety_check_robots()
    if bad:
        print('ABORT: refusing to preview a noindex build. A deploy of this '
              'would deindex the network.')
        for b in bad:
            print('   ', b)
        sys.exit(2)

    built = compute_manifest()
    base = json.load(open(BASELINE)) if os.path.exists(BASELINE) else {}

    bk, xk = set(built), set(base)
    added = sorted(bk - xk)
    removed = sorted(xk - bk)
    changed = sorted(k for k in (bk & xk) if built[k] != base[k])

    domains_built = sorted({k.split('/')[1] for k in built if k.startswith('/')})

    print('=' * 68)
    print('DRY RUN -- nothing has been sent to Cloudflare')
    print('=' * 68)
    print(f'sites built in dist/ : {len(domains_built)}')
    print(f'files in fresh build : {len(built)}')
    print(f'files in live baseline (data/manifest.json, last committed): {len(base)}')
    print()
    print(f'ADDED   (new files not in the live baseline) : {len(added)}')
    print(f'REMOVED (in baseline, not in fresh build)    : {len(removed)}')
    print(f'CHANGED (same path, different bytes)         : {len(changed)}')
    print()

    # New PAGES specifically (index.html), grouped by domain -- the human-
    # meaningful additions (question pages, expansions).
    from collections import Counter
    add_pages = Counter(k.split('/')[1] for k in added if k.endswith('index.html'))
    if add_pages:
        print('New PAGES added, by site:')
        for dom, c in sorted(add_pages.items(), key=lambda x: -x[1]):
            print(f'   +{c:3d}  {dom}')
        print()

    if removed:
        print('REMOVED files (verify these SHOULD disappear):')
        for k in removed[:40]:
            print('   -', k)
        if len(removed) > 40:
            print(f'   ... and {len(removed) - 40} more')
        print()

    # Changed is expected to be large: og:image + twitter:card were added to
    # the shared <head>, so every page's HTML genuinely changed by one meta
    # tag. That is correct, not a bug.
    changed_pages = sum(1 for k in changed if k.endswith('index.html'))
    changed_assets = len(changed) - changed_pages
    print(f'CHANGED breakdown: {changed_pages} page(s), {changed_assets} asset(s).')
    print('   (A large page count here is expected: the og:image/twitter:card')
    print('    tags were added to the shared head, so every page changed by one')
    print('    line. Email-containing pages may also show as changed due to')
    print("    Cloudflare's serve-time email obfuscation -- harmless.")
    print()

    json.dump(built, open(PREVIEW, 'w'))
    print(f'Wrote {PREVIEW} ({len(built)} entries).')
    print('Review the above. To actually deploy the REVIEWED manifest:')
    print('  uv run --with blake3 --with requests python3 deploy_all_mac.py --push <token>')


def push(token):
    import requests
    if not os.path.exists(PREVIEW):
        print('ABORT: no reviewed manifest. Run the dry run first (no --push).')
        sys.exit(2)
    manifest = json.load(open(PREVIEW))
    # Re-verify the reviewed manifest still matches what is on disk, so a stale
    # preview can never be deployed against a changed dist.
    live_now = compute_manifest()
    if live_now != manifest:
        print('ABORT: dist/ changed since the dry run. Re-run the dry run, '
              'review again, then push.')
        sys.exit(2)
    bad = safety_check_robots()
    if bad:
        print('ABORT: noindex build detected at push time.')
        for b in bad:
            print('   ', b)
        sys.exit(2)

    H = {'Authorization': f'Bearer {token}'}
    r = requests.get(f'{API}/accounts/{A}/pages/projects/{P}/upload-token', headers=H).json()
    if not r.get('success'):
        print('ABORT: could not get upload token (check the token scope):', r.get('errors'))
        sys.exit(1)
    jwt = r['result']['jwt']
    J = {'Authorization': f'Bearer {jwt}'}

    hashes = sorted(set(manifest.values()))
    missing = set()
    for i in range(0, len(hashes), 1000):
        r = requests.post(f'{API}/pages/assets/check-missing', headers=J,
                          json={'hashes': hashes[i:i + 1000]}).json()
        if not r.get('success'):
            print('check-missing failed', r)
            sys.exit(1)
        missing.update(r['result'])
    print(f'{len(missing)} of {len(hashes)} unique hashes need upload '
          f'(the rest already live in Cloudflare\'s store).')

    byhash = {v: k for k, v in manifest.items()}
    payload = []
    for x in missing:
        p = byhash[x]
        fp = os.path.join(DIST, p.lstrip('/'))
        body = open(fp, 'rb').read()
        ct = mimetypes.guess_type(fp)[0] or 'application/octet-stream'
        payload.append({'key': x, 'value': base64.b64encode(body).decode(),
                        'metadata': {'contentType': ct}, 'base64': True})
    for i in range(0, len(payload), 50):
        r = requests.post(f'{API}/pages/assets/upload', headers=J, json=payload[i:i + 50]).json()
        if not r.get('success'):
            print('upload failed', r)
            sys.exit(1)
    print('uploaded', len(payload), 'new files')

    r = requests.post(f'{API}/pages/assets/upsert-hashes', headers=J,
                      json={'hashes': hashes}).json()
    print('upsert-hashes:', r.get('success'), r.get('errors'))

    files = {'manifest': (None, json.dumps(manifest)),
             'branch': (None, 'main'),
             '_worker.js': ('_worker.js', open(os.path.join(S, 'router', '_worker.js'), 'rb').read(),
                            'application/javascript')}
    r = requests.post(f'{API}/accounts/{A}/pages/projects/{P}/deployments',
                      headers=H, files=files).json()
    print('DEPLOY:', r.get('success'), (r.get('result') or {}).get('url'), r.get('errors'))


if __name__ == '__main__':
    if '--push' in sys.argv:
        i = sys.argv.index('--push')
        tok = sys.argv[i + 1] if i + 1 < len(sys.argv) else None
        if not tok:
            print('Usage: deploy_all_mac.py --push <token>')
            sys.exit(2)
        push(tok)
    else:
        dry_run()
