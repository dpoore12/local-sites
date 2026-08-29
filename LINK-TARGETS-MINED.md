# Link Targets, Mined From All 83 Markets

Run Aug 29, 2026. Real page-one results pulled live for all 83 markets, then every competitor's link profile pulled from Ahrefs.

## What was measured

- 83 markets, live page-one results, city-level geolocation (DataForSEO, `serp/google/organic/live/regular`)
- Top 3 real businesses per market after removing directories and platforms → **214 unique competitors**
- Link profile pulled for all 214 → **64,200 link rows, 8,038 unique linking domains**

## Finding 1 — the "big" link profiles are a spam blast, not spending

The most-shared linking domains hit almost every one of the 214 competitors:

| Linking domain | Competitors it links to | DR |
|---|---|---|
| za.com | 209 of 214 | 90 |
| rankyour.website | 207 | 74 |
| backlinker.shop | 205 | 72 |
| buybacklinks.agency | 205 | 69 |
| rank-top.click | 200 | 60 |
| pbnseolinks.shop | 192 | 53 |

553 linking domains match obvious spam patterns. A network that links to 209 of 214 unrelated businesses in different states and different trades was not bought by any of them. It is background noise that lands on everything that ranks. **None of these sites are penalized.** So this whole tier is neither a threat nor something to copy.

## Finding 2 — the citation list, ranked by what page-one winners actually have

This replaces guesswork. Percentage = share of the 214 winners carrying that link.

| Directory | Winners on it | DR |
|---|---|---|
| expertise.com | 75% | 88 |
| yellowpages.com | 70% | 90 |
| dexknows.com | 57% | 78 |
| superpages.com | 54% | 85 |
| yp.com | 52% | 73 |
| birdeye.com | 49% | 86 |
| bbb.org | 43% | 93 |
| chamberofcommerce.com | 43% | 84 |
| citysquares.com | 38% | 73 |
| ezlocal.com | 35% | 80 |
| golocal247.com | 33% | 71 |
| neustarlocaleze.biz | 32% | 72 |
| threebestrated.com | 29% | 80 |
| fyple.com | 26% | 62 |
| freelistingusa.com | 25% | 74 |
| local.com | 23% | 76 |
| porch.com | 22% | 76 |
| 2findlocal.com | 22% | 76 |
| hotfrog.com | 21% | 81 |
| homeadvisor.com | 20% | 91 |
| avvo.com (legal) | 20% | 89 |
| superlawyers.com (legal) | 20% | 88 |
| iglobal.co | 20% | 73 |
| yellowbook.com | 19% | 73 |
| justia.com (legal) | 17% | 91 |
| crunchbase.com | 18% | 91 |
| mapquest.com | 17% | 91 |
| elocal.com | 16% | 74 |
| lawinfo.com (legal) | 15% | 73 |
| findlaw.com (legal) | 14% | 90 |
| americantowns.com | 10% | 71 |
| alignable.com | 9% | 84 |

Notes:
- Thryv owns yellowpages / superpages / dexknows / yp — likely one submission feeds all four.
- **Yelp did not appear as a linking domain on a single one of the 214.** Yelp is worth having for the trust signal and the traffic, but it is not passing link value.
- Ten of these were never on our list: citysquares, ezlocal, golocal247, freelistingusa, fyple, 2findlocal, iglobal, elocal, americantowns, neustar localeze.
- expertise.com and threebestrated.com are editorial picks, not open signups — they choose you.

## Finding 3 — 981 per-market local targets

`data/link-targets-mined.csv` — up to 12 targets per site, taken from what that market's own top three are linked from, filtered to domains linking 12 or fewer of the 214 (so: genuinely local, not network noise). 717 of the 981 look local by name pattern (chamber, news, times, county, city, .org, .edu, .gov, or the city name in the domain).

Columns: `our_site, city, state, vertical, link_target, domain_rating, competitors_using_it, found_on_competitor, looks_local`

## What this changes

1. The directory queue should be reordered to the table above, and ten sites added.
2. Buying links is pointless here — the volume tier is free spam that arrives on its own. What the winners have that we don't is the citation set plus a small number of real local links.
3. The local targets are per-market and need email outreach, not forms.

## Sources

- Live page-one results: DataForSEO SERP API, `https://api.dataforseo.com/v3/serp/google/organic/live/regular`, city-level location codes, Aug 29 2026
- Link profiles: Ahrefs API, `https://api.ahrefs.com/v3/site-explorer/refdomains`, date 2026-08-29, top 300 by domain rating per competitor
