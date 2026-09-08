# What Google actually sees — 8 September 2026 (Search Console API, not `site:`)

This replaces the 7 Sep `site:` baseline. Pulled through the Search Console API
(readonly token in ~/.gsc) across all 84 verified properties.

## Impressions — the sites are being shown, and more every week

| ISO week | impressions | clicks | avg position |
|---|---|---|---|
| 34 (launch, 23 Aug) | 51 | 0 | 66 |
| 35 | 5,323 | 0 | 77 |
| 36 | 9,214 | 6 | 62 |

Last 28 days: **16,135 impressions, 6 clicks, 483 distinct pages shown at least once.**
Daily impressions went from ~600 (24 Aug) to ~1,200–1,850 (1–6 Sep). Average
position moved from ~79 to ~60 over the same span. 4 of 84 properties have zero
impressions.

So the honest statement is: Google has these pages, is showing them, and is showing
them more each week. What it is not doing is ranking them where anyone clicks:
average position 60 is page six, and 16,000 impressions produced 6 clicks.

## What the 26% figure was, and why it misled

The 7 Sep baseline counted `site:` results (54 of 204 on 12 domains). Today's URL
Inspection sample (68 pages on 4 sites) returns "Crawled – currently not indexed" for
every page, while the same sites show impressions in the performance report. The
sitemap report shows "indexed 0" on every property. Those Google reports disagree with
each other and with `site:`; none of them is a clean coverage number for a two-week-old
site. Impressions are the one signal that cannot be faked: a page with impressions was
served. **Do not use the 26% number again.** The constraint is position, not indexing.

## Sample inspection detail (4 sites, 68 pages)

- fortworthgaragedoorrepairpros.com (25): 21 crawled-not-indexed, 3 discovered, 1 unknown. Home page last crawled 7 Sep 03:14 UTC, after the router fix; fetch SUCCESSFUL, canonical correct, robots ALLOWED.
- denverdivorcelawyerpros.com (9): 7 crawled-not-indexed, 1 discovered, 1 "excluded by noindex" (/about/, crawl of 23 Aug — the launch build carried noindex on about pages).
- coloradospringsfurnacerepair.com (9): 5 discovered, 3 crawled-not-indexed, 1 unknown.
- appliancerepairtampaco.com (25): 13 discovered, 9 unknown to Google, 3 crawled-not-indexed.

"Discovered / unknown" on the 25-page sites means Google has not bothered to fetch the
expansion pages yet — crawl priority, i.e. authority.

## What this changes

1. Plumbing is fine now (fetch OK, canonical OK, sitemaps downloaded 5–8 Sep).
2. The lever is authority and click-worthiness at position 60 → page one: links and
   citations, plus titles that win the click. Not more pages.
3. The 28 Sep re-measure should be the performance report (impressions, position,
   clicks by property), not `site:`.
4. The four new test sites (towing ×2, mobile mechanic ×2) go into the same Search
   Console account as soon as the token has write scope (needs re-auth with
   `webmasters` + `siteverification`; DNS TXT verification is now possible).

Data: scratchpad gsc_perf_28d_2026-09-08.json, gsc_byday_2026-09-08.json,
gsc_sitemap_report_2026-09-08.json (session scratchpad; regenerate with the API).
