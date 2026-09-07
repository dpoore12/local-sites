# Index coverage baseline — 7 September 2026, 03:00 UTC

Taken **three hours after** the router redirect fix (deployment 01c4f3a8) went
live. Every measurement before this date is contaminated: from 24 August the
router answered slash-less URLs with a redirect to a doubled path, which is how
Googlebot reaches a site it discovers externally. This file exists so the same
measurement can be repeated in two to three weeks and compared honestly.

## Method

`site:<domain>` via DataForSEO `/v3/serp/google/organic`, location 2840, depth
100, counting organic rows. Validated against Search Console on
denverdivorcelawyerpros.com: the GSC coverage export said 7 indexed and this
method returned exactly 7.

Caveat: `se_results_count` on a `site:` query is Google's own estimate and can
undercount. Ann Arbor returned `se_results_count: 10, pages_count: 1`, so the
figures below are not a page-one display cap — but GSC remains the authority.

## Result

| Domain | Pages live | Indexed | Coverage |
|---|---|---|---|
| denverdivorcelawyerpros.com | 9 | 7 | 78% |
| allenacrepairpros.com | 9 | 6 | 67% |
| annarborgaragedoorrepairpros.com | 25 | 10 | 40% |
| bocaratongaragedoorrepairpros.com | 25 | 10 | 40% |
| coloradospringsmoldremediationexperts.com | 25 | 10 | 40% |
| mckinneygaragedoorrepairpros.com | 9 | 2 | 22% |
| appliancerepairtampaco.com | 25 | 3 | 12% |
| lasvegasdogbitelawyerpros.com | 9 | 1 | 11% |
| coloradospringsfurnacerepair.com | 9 | 1 | 11% |
| sanjoseemergencyplumberpros.com | 9 | 1 | 11% |
| dallaswrongfuldeathlawyerpros.com | 25 | 2 | 8% |
| tampatileroofrepair.com | 25 | 1 | 4% |

**Aggregate: 54 of 204 pages indexed — 26%.**
25-page sites: 36 of 150 (24%). 9-page sites: 18 of 54 (33%).

## What this says

Roughly **three quarters of the network is not in Google's index.** That is the
finding, and it is bigger than the page-count gap RANKING-PLAN-AUG29 identified.
Page count cannot be the binding constraint while three of every four pages that
already exist are invisible.

It is not primarily a function of site size. Ann Arbor and Boca Raton carry 25
pages at 40% coverage; Las Vegas and San Jose carry 9 pages at 11%. The spread
within each size band is wider than the gap between the bands.

Cause is not yet separable. Candidates, in order of my confidence:

1. The redirect bug, live 24 Aug to 6 Sep across every domain.
2. Crawl budget on brand-new domains with zero inbound links.
3. Duplicate filtering across 83 near-identical sites — the failure mode
   RANKING-PLAN-AUG29 Part 2 names, where enforcement is deindexing rather than
   low ranking.

(1) is now fixed, which makes the re-measure a real experiment rather than a
guess. If coverage climbs, volume is the right lever and the expansion should
proceed at full speed. If it stays flat, the constraint is uniqueness or
authority, and writing 2,859 more pages would make the pattern worse.

## Re-measure

Same 12 domains, same method, on or after **28 September 2026**. Do not change
the domain set — the comparison is the point.
