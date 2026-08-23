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

## Token needed

An account token with: Cloudflare Pages · Edit, DNS · Edit, Zone · Read (all zones).
A read-only token will silently do nothing useful.
