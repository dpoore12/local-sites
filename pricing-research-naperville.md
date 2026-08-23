# Pricing research: garagedoorrepairnapervillepros.com (Naperville, IL)

All figures retrieved 2026-08-23. Mode: `cost`.

## Anchors

| Anchor | Figure | Source (fetched) | Exact wording found |
| --- | --- | --- | --- |
| Miscellaneous residential permit filing | $18 clerical + $25 per plan page | https://www.naperville.il.us/contentassets/2beca6c2168344f3a65cc84c9479731b/permit-fee-schedule-res-101122.pdf | "Miscellaneous residential permits, not otherwise listed -- $18 clerical fee + $25/plan page" |
| Reinspection, single family / duplex | $68 (first inspection $50) | same schedule | "$50 per inspection; $68 per reinspection (clerical fee + inspection fee)" |
| Median hourly wage, carpenters (47-2031), Chicago-Naperville-Elgin MSA 16980 | $38.68, TOT_EMP 14,220 | https://www.bls.gov/oes/current/oes_16980.htm (figure from May 2025 OEWS data file) | MSA_M2025_dl.xlsx row: 16980, Chicago-Naperville-Elgin IL-IN, 47-2031 Carpenters, TOT_EMP 14220, H_MEDIAN 38.68 |

Schedule provenance: "Effective February 1, 2019 per Ord 18-145", updated 2022-10-11.
Comparison used in the anchor detail: DFW carpenters H_MEDIAN 23.44 in the same May 2025
file, so Chicago is roughly 65% higher (38.68 / 23.44 = 1.65).

Permit applicability (permit required when a door replacement alters the size or style of
the opening or relocates the door; like-for-like swap not on the permit-required list),
the six-decade garage stock (median home 1989; Cress Creek 1960s, 1,200+ residences;
Ashbury early-to-mid 1990s) and the August 11, 2026 NWS Chicago derecho are pre-existing
sourced facts in this site's site.json.

## Market cost rows

Seven rows. The extension-spring-to-torsion conversion row and the salt/slush hardware
rows are specific to this housing stock and climate. Ranges reflect the much higher
Chicago-area labor figure above; they are market observations, not a document figure and
not a quote.

**Correction made during drafting:** an early draft asserted that Illinois requires
battery backup on new residential garage door openers. That requirement is California
(SB 969), not Illinois. The claim was removed before the page was built; the opener row
and the quote-reading paragraph now mention battery backup only as an option to look for.


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

- Naperville publishes no line item named for a garage door or exterior door permit; the
  anchor uses the "miscellaneous residential permits, not otherwise listed" line, which
  is the category such a permit falls into. No after-hours inspection fee is published.

## Published price sources, 2026-08-23

Figures read 2026-08-23. DuPage County operators publish more granular price
lists than the Texas markets, so every Naperville row is backed by two to four
posted figures.

| Company (serves) | Posted figure, verbatim | Job | URL |
| --- | --- | --- | --- |
| Garage Door Center, Naperville | Service call fixed $30 (deducted from total); tune-up $90-$150; spring labor $120-$150 plus parts $90-$150; remote or keypad programming $90-$120; cable $120-$180; basic repair $90-$130; sensors $120-$200; off-track $120-$200; opener installation $500-$700; new door installation $400-$650 | Full posted list | https://garagedoorcenterusa.com/service-area/garage-door-repair-services-naperville-il |
| Garage Door Guys, St Charles (serves Naperville, most of DuPage) | "ONLY $300 - $350" for service call, two replacement springs, labor, check-up and warranty | Spring pair | https://www.garagedoorguys.biz/garage-door-spring-repair |
| Trusted Garage Door, Cook / DuPage / Lake | General repair and track realignment from $95; broken spring replacement from $225; opener replacement from $625; new door installation from $1,195 | Posted starting prices | https://www.trusted-garagedoor.com/services/ |
| John Garage Door Repair, Chicago area | Single torsion $150-$250; pair $250-$375; high-cycle $300-$450; extension pair $150-$250; cable $150-$275 per side; opener repair $150-$300; chain-drive install $300-$450; belt, wall-mount or smart install $400-$650; off-track $150-$300; panel $250-$800; roller set $100-$200; remote programming $50-$100; keypad $75-$150; service call $75-$125; new door $800-$2,500+ | Full posted table | https://johngaragedoorrepair.com/garage-door-repair-cost/ |
| Royal Garage Doors, Aurora | Single torsion $280 flat; double torsion package $320-$460; extension sets $150-$250; cables and brackets $180-$220; safety sensors $120-$180; Torquemaster conversion $530; new opener $450; new door installed from $1,350; diagnostic $120 if work does not proceed | Posted flat rates | https://royalgaragedoorrepairs.com/locations/garage-door-spring-repair-aurora/ |
| Infantino's Garage Door, Chicago and north suburbs | Spring replacement from $179; opener install from $625; new door from $899; high-cycle springs $40-$60 more per spring; after-hours call-out $149 | Posted starting prices | https://infantinosgaragedoor.com/services/cost |
| Premium Garage Door Repair, Naperville / DuPage | Common repairs (springs, opener) $150-$400; complex repairs involving panel replacement or track realignment $400-$800 | Repair ranges | https://premiumgarageil.com/garage-door-repair-naperville/ |

**Row deleted.** "Extension spring system converted to a torsion shaft" was
removed. Only one operator in the market posts a conversion price at all (Royal
Garage Doors, $530 Torquemaster conversion), and a single price list cannot
carry a market range. It was replaced with remotes, keypad and safety eyes at
50-200, which three separate DuPage-area lists publish (Garage Door Center
$90-$200, John Garage Door Repair $50-$150, Royal $120-$180).

Other rows: spring pair 225-460; cables and re-tracking 120-300; rollers and
hinges 95-200; belt-drive opener with backup 400-700; bent track and struts
120-800; insulated double door 800-2500. Seven rows total.

No posted figures: O'Connor Garage Door (Naperville page carries only
dollar-off coupons against a "Regular Price $190" line), Consolidated Garage
Doors, The Door Dr, A-All Style Garage Door, Royal Garage Doors Repair of
Naperville-Aurora.

## Itemized totals corrected, 2026-08-23

Audited all 7 rows. One row moved.

| Row | Was | Now | Arithmetic / reason |
|---|---|---|---|
| Cables replaced and a door lifted back into its tracks | $120-300 | **$120-550** | John Garage Door Repair posts cable replacement at **$150-$275 per side** (https://johngaragedoorrepair.com/garage-door-repair-cost/). Both sides = 2 x $275 = **$550** at the top, 2 x $150 = **$300** at the bottom, before the off-track correction it also prices at $150-$300. High raised from $300 to $550. Low held at Garage Door Center's all-in cable $120-$180 (https://garagedoorcenterusa.com/service-area/garage-door-repair-services-naperville-il). |

Service-call handling on this market's itemized sources:
- Garage Door Center posts a **$30 service call that it states is deducted from the total**, so it is not additive. Its spring line itemizes labor $120-$150 + parts $90-$150 = **$210-$300**, which sits inside the spring row's $225-460.
- Garage Door Guys posts $300-$350 and states it **includes the service call and two springs** (https://www.garagedoorguys.biz/garage-door-spring-repair) - already a total.
- Trusted Garage Door posts "from $225" for both springs including parts, labor, tax and disposal (https://www.trusted-garagedoor.com/services/) - already a total.
- Royal posts a free service call (https://royalgaragedoorrepairs.com/locations/garage-door-spring-repair-aurora/); its $320-460 double-spring figure needs no addition.
- Infantino's posts a **$149 after-hours surcharge** (https://infantinosgaragedoor.com/services/cost). Conditional, so excluded from the ranges.
