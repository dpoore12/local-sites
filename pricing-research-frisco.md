# Pricing research: friscogaragedoorrepairexperts.com (Frisco, TX)

All figures retrieved 2026-08-23. Mode: `cost`.

## Anchors

| Anchor | Figure | Source (fetched) | Exact wording found |
| --- | --- | --- | --- |
| Windows / doors replacement permit | $75 (plus $25 per additional element, $150 maximum) | https://www.friscotexas.gov/DocumentCenter/View/864/Permit-Fee-Schedule-PDF?bidId= | "Windows / Doors Replacement -- $75 plus $25 for each additional element to a maximum of $150" |
| Inspection outside normal business hours | $150 | same schedule | "Inspection outside of normal business hours ... $150.00" |
| Median hourly wage, maintenance and repair workers general (49-9071), DFW MSA 19100 | $23.49, TOT_EMP 39,740 | https://www.bls.gov/oes/current/oes_19100.htm (figure from May 2025 OEWS data file) | MSA_M2025_dl.xlsx row: 19100, 49-9071 Maintenance and Repair Workers General, TOT_EMP 39740, H_MEDIAN 23.49 |

Schedule stamp: "Updated 10-7-2025". Also verified on the same document but not used:
residential reinspection $50.00; plan revision review $50.00 per hour.

Housing-stock and HOA context (58,574 single-family units; 39.6% built 2000-2009, 31.2%
2010-2019, 11.4% 2020 or later; more than 200 HOAs) and the April 3, 2014 NWS two-inch
hail report in Frisco are pre-existing sourced facts in this site's site.json.

## Market cost rows

Seven rows, market ranges for the north Dallas suburbs. Not attributed to a document:
they are informed by the wage anchor, the very young housing stock (standard openings,
easy access, builder-package hardware reaching end of life on the same schedule street
by street), and HOA-driven special-order door costs. Notes name the local driver;
integers with low < high throughout.


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

- Frisco publishes no fee for HOA architectural review (those are private association
  costs), so no dollar figure for association review appears anywhere on the page.

## Published price sources, 2026-08-23

Figures read 2026-08-23 from company-owned pages. Frisco is inside DFW, so the
citations were deliberately built on Collin County operators (Prosper Garage
Door Repair, Metro Garage Door Repair in Plano) rather than the Fort Worth and
Garland lists used on the sister sites.

| Company (serves) | Posted figure, verbatim | Job | URL |
| --- | --- | --- | --- |
| Prosper Garage Door Repair, Frisco / Collin County | "$150-$350" garage door spring repair in Frisco | Springs | https://prosperdoorrepair.com/garage-door-spring-repair/frisco |
| Prosper Garage Door Repair, Plano | Repair $100-$250 (gear kits, logic boards, sensors); gear kit repair $100-$150; new opener installed $350-$600 | Opener | https://prosperdoorrepair.com/garage-door-opener-repair/plano |
| Prosper Garage Door Repair, Frisco | "$800-$2,500+" installed, new residential garage door in Frisco | New door | https://prosperdoorrepair.com/new-garage-door-installation/frisco |
| Metro Garage Door Repair, Plano | Tune-up / minor adjustment $75-$150; cable $150-$250 per side; bottom bracket $75-$150; torsion swap on a two-car door $200-$350; off-track re-track $125-$200; circuit board $150-$250; panel $250-$600+; opener replacement $300-$600 installed; full door replacement $800-$2,500 installed; emergency premium $50-$100 | Full posted breakdown | https://www.metrogaragedoor.net/garage-door-repair-cost-plano-tx-what-youll-actually-pay-and-why/ |
| Fast Mobile Garage Doors (service list includes Frisco) | Service call / tune-up $75-$125; both torsion springs $200-$350; cable $100-$200; opener repair $75-$175; opener replacement $250-$500; panel $150-$400 | Full posted list | https://fastmobilegaragedoors.com/garage-door-repair-cost-dallas-tx.html |
| Garage Door Rescue LLC, DFW | Tune-up $75-$150; cable $120-$250; panel $250-$700+; new door $800-$3,000+ | Full posted list | https://garagedoorrescuellc.com/garage-door-repair-cost-dfw/ |

Row changes: the first row was retitled from a bare service-call charge to a
tune-up and diagnostic visit at 75-150, because the three Collin County price
pages publish the visit as a tune-up with the fee credited against work, not as
a standalone dispatch charge. Springs 150-350, cables and drums 100-250, opener
board or gear kit 75-250, belt-drive opener installed 250-600, single section
150-700, full double door 800-3000. Seven rows, all re-sourced, none deleted.

No posted figures found on: Plano Overhead Garage Door
(https://www.planooverhead.com/garage-door-broken-springs), Discount Garage Door
Repair (Frisco), Fast Fix Garage Door, The Garage Door Man of McKinney. Anytime
Garage Door's Frisco page posts a $799-$40,000 span for a new door, too wide to
be usable as a market bound, so it was recorded but not cited.

## Itemized totals corrected, 2026-08-23

Audited all 7 rows. Two rows moved, both because Metro Garage Door Repair (Plano) posts per-side and per-part prices rather than per-job totals.

| Row | Was | Now | Arithmetic / reason |
|---|---|---|---|
| Torsion springs replaced in pairs on a builder-grade door | $150-350 | **$200-350** | The old low came from Prosper's $150-350 (https://prosperdoorrepair.com/garage-door-spring-repair/frisco), which is generic spring repair, not a pair. The pair-specific posted lows are Metro's two-car torsion swap at $200-$350 (https://www.metrogaragedoor.net/garage-door-repair-cost-plano-tx-what-youll-actually-pay-and-why/) and Fast Mobile's both-springs $200-$350 (https://fastmobilegaragedoors.com/garage-door-repair-cost-dallas-tx.html). Low raised to $200. |
| Lift cables, drums and bottom brackets replaced | $100-250 | **$100-650** | Metro posts cable replacement at **$150-$250 per side** plus a bottom bracket at **$75-$150**. This row replaces both cables and the brackets: 2 x $250 = $500, + $150 bracket = **$650**; the low end of the same build-up is 2 x $150 = $300 + $75 = **$375**. High raised from $250 to $650. Low held at $100 from Fast Mobile's all-in cable $100-$200. |

Rows verified as already all-in and job-matched: tune-up/diagnostic ($75-150), opener repair row cites only repair prices (Prosper $100-250, Metro board $150-250, Fast Mobile $75-175), opener replacement row cites only replacement prices (Prosper $350-600, Metro $300-600, Fast Mobile $250-500), panel row, full-door row.

Conditional charge not totaled: Metro posts an emergency premium of $50-$100 for after-hours calls only.
