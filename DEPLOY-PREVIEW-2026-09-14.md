# Deploy preview — 14 Sep 2026

This is a **dry run**. Nothing has been sent to Cloudflare. It shows exactly
what the next deploy would do, so it can be reviewed before anything goes live.

Produced by: `deploy_all_mac.py` (dry-run mode) against a fresh `--live` build
of all 87 sites, diffed against `data/manifest.json` (the last committed live
manifest).

## The one-line summary

Deploying would **add 30 pages, change 1,414 files, and remove nothing.**
Every change is accounted for below. No live page disappears.

## The 30 pages added (all real, all intended)

| Site | Pages | What they are |
|---|---|---|
| coloradospringsfurnacerepair.com | +20 | Furnace question pages that were written months ago but never deployed (how-long-does-a-furnace-last, furnace-blowing-cold-air, furnace-wont-ignite, etc.). This is the "why isn't Colorado's stuff live" answer. |
| fortworthgaragedoorrepairpros.com | +3 | Town pages (Benbrook, Haltom City, Keller) — written in a prior session, never deployed. |
| mesquiteacrepairpros.com | +1 | ac-blowing-warm-air (Reddit-sourced, built today) |
| annarborgaragedoorrepairpros.com | +1 | garage-door-opener-not-working (built today) |
| fresnowrongfuldeathlawyerpros.com | +1 | how-long-does-a-wrongful-death-lawsuit-take (built today) |
| kalamazootowingpros.com | +1 | car-wont-start-in-cold-weather (built today) |
| orlandomovingcompanypros.com | +1 | how-far-in-advance-to-book-movers (built today) |
| sanjoseemergencyplumberpros.com | +1 | low-water-pressure-in-house (built today) |
| scottsdalegaragedoorrepairpros.com | +1 | garage-door-insulation service page — prior session, never deployed |

## The 1,414 changed files (all explained)

- **1,327 pages** — that's *every existing page on all 87 sites*. They changed
  because the `og:image` and `twitter:card` tags were added to the shared page
  head (so link previews on text/Slack/social finally show an image), plus the
  About/Contact title fix on those two pages per site. One or two lines per
  page, no content rewrite.
- **87 sitemaps** — one per site, regenerated. Sitemaps are hint files for
  Google; harmless. No image, stylesheet, or other real asset changed.

## The 0 files removed

Nothing on any live site is deleted by this deploy.

## Safety checks that passed before this preview was allowed

- All 87 sites built cleanly with `--live` (index-allowed, NOT noindex).
- Every `robots.txt` verified `Allow: /` — a noindex build would have aborted
  the preview before it ran.
- The manifest is computed from the actual built bytes on disk (blake3 of
  base64+ext, matching Cloudflare Pages), not reconstructed by re-fetching live
  pages. That is why this replaces the old `deploy_add_mac.py`, which had to
  refuse any change to an existing site.

## To actually deploy (the second, deliberate step)

After this preview is accepted:

```bash
cd ~/Documents/GitHub/local-sites && uv run --with blake3 --with requests python3 deploy_all_mac.py --push "$(cat ~/.local-sites-token)"
```

The push step re-verifies the reviewed manifest still matches disk and
re-checks robots before uploading, then uploads only the genuinely-new bytes
and posts the deployment with the current router.
