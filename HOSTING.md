# Hosting — all 83 sites

Every site is live on Cloudflare. One hosting project holds all 83, and a small
router in front reads the web address the visitor typed and serves that site's
folder. Visitors never see it — each domain looks and behaves like its own site.

Why one project instead of 83: Cloudflare caps how many separate hosting
projects an account can have. We hit that cap at about 22. One project has no
such limit, costs nothing extra, and deploys in a single step instead of 83.

Nothing about this changes how the sites look to Google. Each one is a separate
domain, with its own pages written for that city and its own phone number.

## Where things live

- Project: `local-sites` (Cloudflare account a3bf1a13d93899d8408b9d1ea94df078)
- Direct address: https://local-sites-5d8.pages.dev
- Router source: `router/functions/[[path]].js`
- Built sites: `dist/<domain>/`
- State and manifest: `data/hosting.json`, `data/manifest.json`

## Re-deploying after a site changes

    python3 template/build.py          # rebuild dist/
    python3 host_all.py stage          # gather all 83 into one folder
    python3 host_all.py pass           # with the Cloudflare credential
    python3 host_all.py upload         # WITHOUT any credential
    ./redeploy.sh                      # with the Cloudflare credential
    python3 host_all.py check          # without any credential

`upload` and `check` must run with no credential attached — the sandbox proxy
rewrites the auth header on Cloudflare calls, which breaks the upload pass and
blocks every other host.

## Synthetic monitor

GitHub Action `.github/workflows/site-health.yml` runs every 6 hours (and on
push to the router/check paths):

1. `python3 test_unprefix.py` — unit pin for the Location-leak fix
2. `python3 host_all.py check` — every domain: home + 3 sitemap interiors +
   slashless `/services` Location must not contain `/<host>/`

This is what should have caught the Aug 24–Sep 7 outage on day one. It never
rebuilds or redeploys.

## Router-only redeploy (no rebuild)

When `.stage/` already holds the live expanded sites, push a worker fix without
`build.py`:

    python3 host_all.py stage_router
    python3 host_all.py pass          # Cloudflare credential
    python3 host_all.py upload        # NO credential
    python3 host_all.py publish       # Cloudflare credential
    python3 host_all.py check

## Token needed

An account token with: Cloudflare Pages · Edit, DNS · Edit, Zone · Read (all zones).
A read-only token will silently do nothing useful.

## 2026-09-08 — deploying from Dan's Mac without wrangler

The sandbox-era `host_all.py` flow needs wrangler. On the Mac the working path is:

    live_manifest_mac.py     # fetch every live file from the 83 sitemaps, hash it the way
                               # Pages does (blake3 of base64(content)+ext, first 32 hex),
                               # write scratchpad/stage + live-manifest.json
    deploy_add_mac.py <token> <new-domain> ...
                               # add dist/<new-domain> to that manifest, upload only the
                               # missing hashes with an upload-token JWT, POST the deployment
                               # with router/_worker.js. Refuses to run if any EXISTING site's
                               # file would change (guard), so the 83 live pages stay byte-identical.

Known wrinkle: Cloudflare's email obfuscation rewrites any page that contains an email
address on every request, so those pages cannot be fetched byte-exact. Two Cincinnati PI
pages (nursing-home-neglect, wrongful-death-claims-in-ohio) were re-uploaded with the
obfuscation reversed on 2026-09-08. `data/manifest.json` is now the exact live manifest
(2015 files: 83 sites + kalamazootowingpros.com, evansvilletowingpros.com,
savannahmobilemechanicpros.com, wilmingtonmobilemechanicexperts.com).

The token also needs Zone > DNS > Edit to create the CNAMEs for new zones; without it the
Pages custom domains sit at "pending".

## 2026-09-14 — deploy_all_mac.py: the safe full-network deploy

`deploy_add_mac.py` could only ADD new sites; it aborted on any change to an
existing site because it reconstructed the live manifest by re-fetching pages
(never exact). `deploy_all_mac.py` replaces it and is dist-authoritative: it
hashes the actual built bytes, so there is nothing to reconstruct and existing
sites can change safely.

Two steps, and step 1 touches nothing on Cloudflare:

    uv run --with jinja2 --with markdown python3 template/build.py --live
    uv run --with blake3 --with requests python3 deploy_all_mac.py
                               # DRY RUN: computes the manifest, verifies every
                               # robots.txt is index-allowed (aborts on noindex),
                               # diffs vs data/manifest.json, prints added/
                               # removed/changed, writes deploy-manifest.json.
                               # Sends NOTHING to Cloudflare.
    uv run --with blake3 --with requests python3 deploy_all_mac.py --push "$(cat ~/.local-sites-token)"
                               # PUSH: re-verifies the reviewed manifest still
                               # matches disk, re-checks robots, uploads only the
                               # missing hashes, POSTs the deployment.

A changed shared head (og:image, title tweaks) shows as "every page changed" in
the diff -- that is correct, one line per page, not a rewrite. Only genuinely-new
bytes upload; unchanged files already live in Cloudflare's content-addressed store.
