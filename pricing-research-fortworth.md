# Pricing research: fortworthgaragedoorrepairpros.com (Fort Worth, TX)

All figures retrieved 2026-08-23. Mode: `cost`. Aggregator sites were not used at any point.

## Anchors

| Anchor | Figure | Source (fetched) | Exact wording found |
| --- | --- | --- | --- |
| Residential remodel permit, single trade | $112.50 | https://www.fortworthtexas.gov/files/assets/public/v/9/development-services/documents/resources-applications-forms-videos/f/development-fees-schedule.pdf | "TABLE IA-1 -- RESIDENTIAL REMODEL FEES -- Based upon the number of trades required for the project -- Number of Trades: 1 -- Minimum Permit Fee ... $112.50" |
| Reinspection fee | $63.00 | same PDF (Ordinance No. 27191-09-2024) | "Reinspection fee ... $63.00" |
| Median hourly wage, carpenters (47-2031), Dallas-Fort Worth-Arlington MSA 19100 | $23.44, TOT_EMP 9,480 | https://www.bls.gov/oes/current/oes_19100.htm (figure read from the May 2025 OEWS data file, see method below) | MSA_M2025_dl.xlsx row: 19100, Dallas-Fort Worth-Arlington TX, 47-2031 Carpenters, TOT_EMP 9480, H_MEDIAN 23.44 |

Fee schedule effective date: "This Ordinance shall take effect on October 1, 2024."
Other verified amounts from the same PDF, not used as anchors: plan review deposit
$276.75 (requiring circulation) / $106.87 (without circulation); inspections outside
normal business hours $112.50 minimum.

Permit applicability came from the site's existing sourced local fact: Fort Worth
Development Services states replacement or addition of exterior doors requires a
building permit. Hail context (April 24-29, 2026 NWS Fort Worth/Dallas severe weather
episode) is also an existing sourced fact in site.json.

## Market cost rows

Ranges are market observations for the DFW area, not a quote from any operator, and are
not sourced to any single document. They were set from the labor arithmetic above (a
billed hour that is a multiple of a $23.44 median wage), local access conditions
documented in the site's own housing-stock fact (about a third of ~397,600 units predate
1980; 1920s alley garages with limited headroom), and parts-cost structure for torsion
springs, cables, rollers, opener heads, track/strut correction and insulated steel doors.
Each row's `note` states the specific local driver, and each low/high pair is a whole
dollar integer with low < high.


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

- No Fort Worth line item exists specifically named "door replacement" or "garage door";
  the anchor uses the residential-remodel minimum that a single-trade door replacement
  files under. The permit requirement itself is sourced separately (site.json fact 2).

## Published price sources, 2026-08-23

All figures below were read on 2026-08-23 from each company's own website. No
aggregator or national cost-guide domain was used. Each row in `site.json` now
takes its `low` from the lowest posted figure and its `high` from the highest.

| Company (serves) | Posted figure, verbatim | Job | URL |
| --- | --- | --- | --- |
| Cowtown Garage Doors, Fort Worth | "$295 Installed" single torsion spring; "$365 Installed" double torsion spring; "$195 Installed" old style extension springs | Spring replacement, metal doors | https://www.cowtowndoors.com/page-14.html |
| Cowtown Garage Doors, Fort Worth | "$125" typical tune-up with 10 new rollers | Rollers / tune-up | https://www.cowtowndoors.com/page-17.html |
| Panther Garage Pros, Fort Worth (Wedgwood, Arlington) | Torsion spring total $150-$300; extension spring total $80-$150; safety cables $25-$40 | Springs, cables | https://panthergaragepros.com/services/garage-door-springs-replacement/ |
| Panther Garage Pros, Fort Worth | Tune-up $79-$149; spring repair $99-$200; cable repair $150-$200; track adjustment $125-$150; opener repair $100-$190 | Posted service cost list | https://panthergaragepros.com/garage-door-repair-service-costs-wedgwood-square/ |
| Fast Mobile Garage Doors, DFW (lists Fort Worth) | Single torsion spring $150-$250; both springs $200-$350; extension pair $100-$200; cable $100-$200; off-track $125-$275; opener repair $75-$175; opener replacement $250-$500; roller replacement $75-$150; panel $150-$400; new door installed $800-$2,500; service call / tune-up $75-$125 | Full posted list | https://fastmobilegaragedoors.com/garage-door-repair-cost-dallas-tx.html |
| Garage Door Rescue LLC, DFW | Spring replacement $150-$350; dual spring $300-$500; opener repair $120-$300; opener replacement $350-$800; cable $120-$250; track repair or realignment $100-$280; roller $120-$220; panel $250-$700+; tune-up $75-$150; emergency add-on $50-$150; new door $800-$3,000+ | Full posted list | https://garagedoorrescuellc.com/garage-door-repair-cost-dfw/ |
| Veteran Garage Door, DFW metro | "$259" installed spring replacement (60-165 lb doors, .207-.243 wire); conversion $545 (8x7) and $645 (16x7) | Springs, conversions | https://veterangaragedoor.com/springs/ |

Rows and the ranges they now carry: springs 200-500 (Cowtown, Fast Mobile,
Garage Door Rescue, Veteran); off-track and cables 120-275 (Fast Mobile,
Panther, Rescue); rollers, hinges and bearings 75-220 (Cowtown, Fast Mobile,
Rescue); opener head 250-800 (Fast Mobile, Rescue); track and strut 100-280
(Panther track adjustment, Rescue track realignment); two-car insulated door
800-3000 (Fast Mobile, Rescue). Six rows, all re-sourced, none deleted.

Read but carrying no posted figures, so not cited: Precision Garage Door of
Fort Worth (https://precisiondoorfortworth.com/garage-door-spring-repair --
estimate on request only), Welborn Garage Keller page, Doorvana Fort Worth
tune-up and cable pages. thegaragedoorpros.us posts ranges but lists service
offices in roughly eighty cities nationwide, so it was treated as a lead-gen
network and skipped.

## Itemized totals corrected, 2026-08-23

Audited all 6 rows for itemized (component) posted prices. Only one row moved.

| Row | Was | Now | Arithmetic / reason |
|---|---|---|---|
| Door jumped the track, cables reset and drums retimed | $120-275 | **$120-280** | Garage Door Rescue posts track repair and realignment at $100-$280 (https://garagedoorrescuellc.com/garage-door-repair-cost-dfw/, read 2026-08-23), the same job as this row; the prior high came only from Fast Mobile's off-track $125-$275 (https://fastmobilegaragedoors.com/garage-door-repair-cost-dallas-tx.html). Low held at Rescue's cable $120. |

No source on this site posts a component build-up. Cowtown Doors posts $365 for a double torsion spring set *installed* (https://www.cowtowndoors.com/page-14.html); Veteran posts $259 installed (https://veterangaragedoor.com/springs/); Fast Mobile's $200-350 is for *both* springs; Rescue's $300-500 is its dual-spring line. Nothing to add.

Conditional charge not totaled: Rescue posts an emergency or after-hours add-on of $50-$150. It applies only outside normal hours, so it is excluded from every range rather than added to the high.

Job-match check: opener REPAIR figures (Panther $100-190, Fast Mobile $75-175) are confined to no row here; the opener row is a full head replacement and cites only replacement prices (Fast Mobile $250-500, Rescue $350-800).
