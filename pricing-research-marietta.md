# Pricing research: mariettagaragedoorrepairpros.com (Marietta, GA)

All figures retrieved 2026-08-23. Mode: `cost`.

## Anchors

| Anchor | Figure | Source (fetched) | Exact wording found |
| --- | --- | --- | --- |
| Residential building permit, valuation based | $5 per $1,000 of construction cost (labor + materials), $50 minimum, no plan review fee | https://www.mariettaga.gov/443/Building-Permits | "Residential permit fee -- $5 per $1,000 of total construction costs (labor + materials)"; "$50 minimum"; "No plan review fee" |
| Reinspection escalation, third failure | $100 (1st inspection no charge; 1st failure $50; 2nd $75; 3rd and each additional $100) | same page | "1st inspection -- No charge; 1st disapproved reinspection -- $50.00; 2nd -- $75.00; 3rd -- $100.00; each additional failed reinspection -- $100.00" |
| Median hourly wage, maintenance and repair workers general (49-9071), Atlanta-Sandy Springs-Roswell MSA 12060 | $23.86, TOT_EMP 25,190 | https://www.bls.gov/oes/current/oes_12060.htm (figure from May 2025 OEWS data file) | MSA_M2025_dl.xlsx row: 12060, Atlanta-Sandy Springs-Roswell GA, 49-9071, TOT_EMP 25190, H_MEDIAN 23.86 |

Cross-checked https://www.mariettaga.gov/1495/City-Fee-Chart (city fee chart page), which
shows the same residential building permit fee of $5 per $1,000 and reinspection fees of
$50 / $75 / $100, with electric, plumbing and mechanical permits at $50 each, updated
per Res. 1753 on 2025-10-08. The PDF at mariettaga.gov/DocumentCenter/View/1495 is
disallowed by robots and was not retrieved; the HTML fee chart and the Building Permits
page carry the same amounts.

Permit applicability (permit required to construct, enlarge, alter, repair, move or
demolish a structure, with no garage-door-only exemption, processed through SagesGov) and
the Downtown Historic District Certificate of Approval requirement are pre-existing
sourced facts in this site's site.json. NWS north Georgia climate figures (50-55 inches of
rain, ~120 days with measurable rainfall) are also a pre-existing sourced fact and drive
the corrosion reasoning.

## Market cost rows

Seven rows, weighted toward this market's wood and wood-clad door stock: a balance and
drag correction row, a rot / refinish row, and a carriage-style replacement row whose
ceiling reflects historic review downtown. Ranges are market observations.


### BLS OEWS retrieval method (all five sites)

The human-readable OEWS metro pages at `bls.gov/oes/current/oes_<MSA>.htm` return HTTP 403
to scripts, and the BLS public data API (`api.bls.gov/publicAPI/v2`) returned
`REQUEST_NOT_PROCESSED -- daily threshold ... reached` for the unregistered key on the
retrieval date. The figures below were therefore taken from the official May 2025 OEWS
metropolitan data file, downloaded successfully on 2026-08-23:

- File: `https://www.bls.gov/oes/special-requests/oesm25ma.zip` -> `oesm25ma/MSA_M2025_dl.xlsx`
  (HTTP 200, 39,932,338 bytes, retrieved 2026-08-23)
- Columns read: `AREA`, `AREA_TITLE`, `OCC_CODE`, `OCC_TITLE`, `TOT_EMP`, `H_MEDIAN`
- Note: the May 2025 release publishes metropolitan statistical areas only; the older
  metropolitan divisions (Fort Worth-Arlington-Grapevine 23104, Dallas-Plano-Irving 19124)
  are no longer broken out, so all three Texas cities fall inside MSA 19100. Each Texas
  site therefore cites a different occupation from that metro rather than the same figure.
- Equivalent API series IDs, recorded for reproducibility once the quota resets:
  `OEUM001910000000047203108` (DFW, 47-2031, median hourly),
  `OEUM001910000000049907108` (DFW, 49-9071, median hourly),
  `OEUM001910000000049909908` (DFW, 49-9099, median hourly),
  `OEUM001698000000047203108` (Chicago-Naperville-Elgin, 47-2031, median hourly),
  `OEUM001206000000049907108` (Atlanta-Sandy Springs-Roswell, 49-9071, median hourly).
- `source_url` on each anchor is the human-readable metro page, which a reader can open:
  oes_19100.htm (DFW), oes_16980.htm (Chicago), oes_12060.htm (Atlanta).


## Could not verify

- No dollar amount is published for the Historic Board of Review Certificate of Approval
  application, so the page describes the review as a requirement and a timeline factor
  rather than attaching a fee to it.
- Marietta publishes no door- or garage-door-specific permit line; the valuation formula
  is the applicable calculation.

## Published price sources, 2026-08-23

Figures read 2026-08-23. Cobb County operators mostly quote on the phone, so
the citable figures came from Marietta-serving companies that publish ranges
plus two Atlanta-metro price tables.

| Company (serves) | Posted figure, verbatim | Job | URL |
| --- | --- | --- | --- |
| Acworth Overhead Doors, Marietta page | Smaller repairs $150-$350; panel and track repairs $300-$800, larger jobs $1,200 or higher; full door replacement $1,000-$3,000, custom above $4,000 | Marietta repair costs | https://acworthoverheaddoors.com/garage-door-repair-marietta-ga |
| Acworth Overhead Doors, Cobb County | Garage door repair $150-$600; spring replacement $300-$700; opener installation $500-$1,500; track repair or replacement $400-$1,200; door replacement $1,200-$2,800; single 8x7 door $700-$1,200; double 16x7 $1,200-$2,000 | Service cost table | https://acworthoverheaddoors.com/acworth-ga-overhead-doors-service-costs |
| Habpro Garage Doors, metro Atlanta | Extension spring replacement $275-$400; torsion spring replacement on standard residential doors $375-$550; wood custom carriage doors $1,000 or more; Wayne Dalton Torquemaster systems $450-$650 | Spring replacement | https://www.habprogaragedoors.com/atlanta-ga/spring-replacement/ |
| Liberty Garage Door Solutions, metro Atlanta | Spring repair $180-$340; cable repair $130-$250; opener repair $120-$320; opener installation $250-$550; panel replacement $250-$500; track realignment $120-$240; roller replacement $110-$220; new door installation $700-$2,200; general repair $150-$600 | Full posted table | https://libertygaragedoorsolutionsatlanta.com/garage-door-repair-cost/ |
| Georgia Garage LLC, Georgia | Residential standard service call $99 including dispatch, 20-point inspection, lube and tune and labor on most repairs; springs $89-$500 per spring; roller replacement quoted as $99 plus the cost of rollers | Services and prices | https://georgiagaragellc.com/services/ |
| Good Golly Garage Doors, Marietta and Cobb | "$49" garage door tune-up, per door, residential | Tune-up | https://goodgollygarage.com/garage-door-maintenance/garage-door-tune-up-in-atlanta-ga |
| Garage Door Atlanta, Atlanta and surrounding | Cable replacement "$100 and $300" | Cables | https://atlantagaragedoorfix.com/garage-door-cable-replacement-atlanta-ga/ |
| Garage Doors Atlanta GA, Atlanta area | Repairs generally $150-$350; spring repair or replacement $100-$300; cable repair or replacement $100-$200; track adjustment or repair $125-$300 | Posted cost list | https://garagedoorsatlantaga.com/blog/how-much-does-it-cost-to-repair-a-garage-door-in-atlanta.html |

**Row deleted.** "Wood door refinished or a rotted bottom rail rebuilt" came
out. Nobody serving Cobb County publishes a figure for refinishing or rebuilding
a wood door; the closest posted number is Habpro's $1,000-plus for springs on a
wood custom carriage door, which is a different job. It was replaced with panels
and track repaired after a strike at 120-1200, published by three separate
businesses (Acworth Overhead Doors $300-$800 rising past $1,200, Liberty
$250-$500 panel and $120-$240 track, Garage Doors Atlanta GA $125-$300 track).

Other rows: springs in pairs 100-700; sticking or dragging door 49-600; cables
and bottom brackets 100-300; rollers, hinges and end bearings 99-220; opener
replaced 250-1500; carriage door on a visible elevation 700-3000. Seven rows.

No posted figures, phone quote only: Metro Garage Doors (Marietta and Atlanta
tune-up pages, "flat fee per door, quoted when you book"), All 4 Seasons Garage
Doors (Marietta storefront), Aaron Overhead Doors Marietta, Sweet Home Garage
Doors, Neighborhood Garage Door Service Kennesaw price-list page (which carries
no prices). Town and Country Garage of Kennesaw posts only a $39 trip fee waived
with repair and Affordable Garage Door Service of Marietta only "starting at
just $99", so both were recorded but neither was used as a range bound.

## Itemized totals corrected, 2026-08-23

Audited all 7 rows. One row was re-sourced and re-ranged, and one row was replaced because its only itemized source never posts the parts amount.

**Georgia Garage, posted services and prices** (https://georgiagaragellc.com/services/, read 2026-08-23) is itemized: a **$99 residential service call** that covers a 20-point inspection, lubrication, tuning and labor, plus **springs at $89-$500 each**.

Total for a **pair**, as the spring row describes: 99 + (2 x 89) = **$277** at the bottom; 99 + (2 x 500) = **$1,099** at the top.

| Row | Was | Now | Arithmetic / reason |
|---|---|---|---|
| Torsion springs renewed in pairs | $100-700 | **$277-1099** | Dropped Garage Doors Atlanta GA's $100-$300, a generic single-spring figure that does not price a pair. Range now runs from Georgia Garage's $277 pair total to its $1,099 pair total, corroborated by Habpro's torsion $375-$550 with wood and custom sets above $1,000 (https://www.habprogaragedoors.com/atlanta-ga/spring-replacement/) and Acworth Overhead Doors' spring line at $300-$700 (https://acworthoverheaddoors.com/acworth-ga-overhead-doors-service-costs). |
| Rollers, hinges and end bearings refreshed | $99-220 (deleted) | replaced by **Opener gear or carriage replaced instead of the whole head, $120-320** | Georgia Garage prices roller work as "$99 plus the cost of the rollers" and never posts the parts amount, so no total can be computed - it had to be dropped, leaving the row with one source. No other Cobb or Atlanta operator posts a roller labor figure: searched repeatedly and found only parts-only listings (Above & Beyond's $130 ten-pack of nylon rollers, Moving Up's $1.70-$3.27 each) and a "$50 off" promotion at Sweet Home, none of which price the job. Row replaced with an opener-component repair, which the market does publish: Don't Panic posts flat **totals** of $189 for a chain or belt drive gear assembly, $150 for a screw-drive inner slide and $125 for a Genie carriage (https://dontpanicdoor.com/), and Liberty posts opener repair at $120-$320 (https://libertygaragedoorsolutionsatlanta.com/garage-door-repair-cost/). Range $120-$320. |

Don't Panic also posts a **$75 trip charge plus $1 per minute of labor** for door-off-track work. That is not a fixed total, so it is not used to set any range.

Rows verified as already all-in and job-matched: tune-up and balance ($49-600), cables and bottom brackets ($100-300), opener replacement row cites only installation prices (Liberty $250-$550, Acworth $500-$1,500), panel and track ($120-1200), full carriage-style replacement ($700-3000).

Note text on several rows was shortened to keep the pricing page inside the 1,750-word ceiling after the new source names were added.
