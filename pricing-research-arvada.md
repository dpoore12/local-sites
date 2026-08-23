# Pricing research — arvadaemergencyplumber.com (Arvada, CO, Emergency Plumbing)

Retrieval date: 2026-08-23 (all figures fetched that day). Mode: `cost`.

## Anchors used on the page

| Anchor | Value | Source (fetched) | Exact wording found |
| --- | --- | --- | --- |
| Building permit, water heater replacement | $55.00 | [City of Arvada Building Fee Schedule](https://www.arvadaco.gov/1263/Building-Fee-Schedule) | Line item "Water Heaters*" — $55.00. Footnote: "Minor electric wiring is included, but a service change or upgrade is not included in this permit fee." |
| Right-of-way permit, one sewer service | $67.00/EA | [2025 Fee Schedule for Rights of Way Work Permits and Services (PDF)](https://www.arvadaco.gov/DocumentCenter/View/294/Right-of-Way-Fee-Schedule-PDF) | "Sewer Service $67.00/EA"; "Minimum Permit Fee $67.00/EA" |
| Pavement degradation fee, per foot of trench | $20.50 | [2025 Fee Schedule for Rights of Way Work Permits and Services (PDF)](https://www.arvadaco.gov/DocumentCenter/View/294/Right-of-Way-Fee-Schedule-PDF) | "Degradation Fee $20.50/LF of trench (plus 20LF of required resurfacing)" |

## Supporting figures cited in body copy

- Plumbing permits generally: "Fees for plumbing permits, mechanical permits, electrical permits, and other miscellaneous permits and commercial work shall be based on actual contract value of the work as per Table 18-1." Table 18-1 starts at **$34.00** for total valuation $1.00–$500.00 — [City of Arvada Building Fee Schedule](https://www.arvadaco.gov/1263/Building-Fee-Schedule) (also in the [2026 Building Permit Fee Guide and Schedule PDF](https://www.arvadaco.gov/DocumentCenter/View/6885/2026-Building-Permit-Guide-and-Schedule?bidId=), which shows the same $55 water-heater line).
- ROW schedule also states: Reinspection **$77.00/EA**, Overtime **$114.00/hr, 2-hour minimum**, Traffic Control Plan Review – Single Service **$67.00/EA**, additional reviews **$33.50/EA**, Water Service **$67.00/EA**, Municipal General Contractor's License **$225.00** — same ROW PDF.
- Expansive soil / under-slab plumbing recommendation and water hardness (avg 84 mg/L, ~5 grains per gallon) come from the site's existing `local_facts` in `site.json` (already sourced there); repeated on the pricing page as reasoning, not as new figures.

## Cost rows (market ranges, not advertiser prices)

7 rows: after-hours callout $165–495; main drain cabled $225–675; sewer camera + locate $245–695; split/frozen supply line $385–1,650; 40–50 gal gas water heater changeout $1,450–3,600; sewer lateral spot repair $3,200–9,800; water service line replacement $4,600–15,500.

Ranges are researched market ranges for the Denver-metro/Jefferson County area informed by market observation and by the documented local cost drivers above (permit + ROW + degradation + restoration, frost depth, expansive clay, bedrock). No aggregator site is cited on the page; none was used as a named source.

## Could not verify

- **BLS OEWS metro wage for Plumbers, Pipefitters and Steamfitters (SOC 47-2152), Denver-Aurora-Lakewood MSA.** The intended series was `OEUM0019740000000047215208` (area 0019740, occupation 47-2152, datatype 08 = median hourly). Both the v1 and v2 BLS public data API returned `REQUEST_NOT_PROCESSED — "the daily threshold for total number of requests allocated to the user with registration key has been reached"` on repeated attempts on 2026-08-23, and `www.bls.gov/oes/current/oes_19740.htm` plus the OEWS flat files return HTTP 403 to scripts. No wage anchor was published, since the figure could not be read from a primary source. Retry the API on a later day to add a fourth anchor.


## Published price sources, 2026-08-23

Every row in `pricing.rows` was rebuilt from prices published by companies working this market.
Retrieval date for every URL below: 2026-08-23. No aggregator, lead-gen or cost-guide domain on the
build's banned list was used, and pages that publish no dollar figure were not cited.

### Figures read (Denver metro / Arvada)

| Company | Job as posted | Figure | URL |
|---|---|---|---|
| Accountable Home Plumbing | emergency first hour; call-out charge; hourly; after-hours premium | $185-250 first hour; $85-125 call-out; $85-150/hr; +$50-100 after hours | https://www.accountablehomeplumbing.com/emergency-plumbers |
| Colorado Water Works | standard hourly; service/diagnostic fee; emergency/after-hours hourly | $100-200/hr; $50-150; $250-350+/hr | https://www.coloradowaterworks.com/how-much-do-plumbers-charge-per-hour-in-denver-2025-pricing-guide |
| Glaze Plumbing | service call; standard hourly; emergency/after-hours hourly (premium 1.5-2x); single drain snake; main line cleaning; hydro-jetting; camera; accessible pipe leak; leak behind wall | $50-100; $100-120/hr; $150-250/hr; $100-275; $200-500; $300-600; $150-400; $150-500; $300-1,000 | https://glazeplumbingco.com/blog/how-much-does-plumber-cost-denver |
| Drain Brain | snaking; main sewer unclog; hydro jetting; camera; after-hours emergency fee | $125-350; $450-800; $600-1,500; $250-400; +$150-500 | https://www.drainbrainllc.com/how-much-does-a-drain-cleanout-cost-in-denver-2026-homeowner-s-guide |
| Drain Brain | water main install (avg $1,589) | $613-2,588; $50-250/lf | https://www.drainbrainllc.com/water-lines-denver |
| My Denver Plumber | main line drain clean to 100 ft (sewer scope included); sewer scope; pull/reset toilet; 40-gal gas heater installed; 50-gal installed; service call | $380; $250; $79; $3,050; $3,299; $225/hr, $99 diagnostic | https://mydenverplumber.net/my-denver-plumber-rates/ |
| Mr. Perfect Plumbing | drain cleaning from; main sewer clog; minor sewer line repair; sewer replacement; main water line repair; burst/frozen pipe; water heater repair | $299; $300-900; $500-3,000; $5,000-15,000+; $600-2,650; $420-1,590; $300-700 | https://mrperfectplumbing.com/blog/2026/june/cost-of-plumbing-repairs-in-denver-2026-what-you-ll-actually-pay/ |
| Plumb Pros | water heater repair; full tank replacement installed; 50-gal gas installed; after-hours/same-day fee | $150-950; $900-2,500; $900-1,500; +$75-150 | https://www.plumbprosinc.com/water-heater-repair-cost-denver-co/ |
| FloWorks Plumbing (serves Arvada) | 40-gal replacement; 50-gal replacement, labor and materials | ~$800-2,300; ~$1,000-6,500 | https://floworksplumbing.com/learning-center/how-much-does-it-cost-to-replace-a-water-heater-in-denver |
| Priority Plumbing & Heating | camera inspection of sewer/main line; drain clearing | $169; $123 | https://priorityplumbingandheating.com/drain-services/camera-inspection/ |
| Simply Sewers | sewer replacement by excavation; trenchless; per foot; permits | $5,000-13,000; $4,000-12,000; $50-250/lf; $100-500 | https://www.simplysewersdenver.com/how-much-does-a-sewer-replacement-cost/ |

### Arithmetic for itemized totals

- **Night or weekend callout, $170 low:** Accountable Home Plumbing posts a call-out charge from $85 plus an hourly rate from $85 -> $85 + $85 = **$170** for a first hour off-hours.
- **Night or weekend callout, $500 high:** Colorado Water Works posts a service/diagnostic fee up to $150 plus an emergency/after-hours hourly rate up to $350 -> $150 + $350 = **$500**. Drain Brain's separate after-hours fee of up to +$500 and Glaze's 1.5-2x premium corroborate the top of the band.

### Row-by-row mapping

1. Night/weekend callout $170-500 - itemized above (Accountable, Colorado Water Works, Glaze, Drain Brain).
2. Main drain cabled through cleanout $200-900 - Glaze main line cleaning $200-500 low; Mr. Perfect main sewer clog to $900 high; My Denver Plumber $380 flat; Drain Brain $450-800.
3. Sewer camera + locate $150-400 - Glaze $150-400; Priority $169 flat; My Denver Plumber $250 flat; Drain Brain $250-400.
4. Split supply line / frozen hose bib $150-1,590 - Glaze accessible pipe leak from $150; Mr. Perfect burst or frozen pipe to $1,590.
5. Water heater, 40/50-gal gas $900-6,500 - Plumb Pros 50-gal gas installed from $900; My Denver Plumber $3,050 and $3,299 installed; FloWorks 50-gal to $6,500 including labor and materials. All three figures include the unit.
6. Sewer lateral spot repair or replacement $500-15,000 - Mr. Perfect minor repair from $500 and replacement to $15,000+; Simply Sewers $4,000-13,000 trenchless/excavation.
7. Water service line repaired or replaced $613-2,650 - Drain Brain water main install $613-2,588; Mr. Perfect main water line repair $600-2,650. Row job wording changed from "replaced" to "repaired or replaced" so it matches what those two pages actually price.

### Not used

- `colorado-plumbing.com` sewer pricing page (Yard Spot Repair $5,000, Street Spot Repair $9,500, Full Replacement $12,000) names no company; skipped as a possible doorway.
- `denversewerandwater.com` camera $175-500: no company named; skipped.
- `douglascountyplumbing.com` cost guide (service call $50-100, evening $75-150, weekend $100-175, holiday/emergency $150-250, emergency 1.5x-2x): names no company and covers Castle Rock/Parker, not Arvada; skipped.
