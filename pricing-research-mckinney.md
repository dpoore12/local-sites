# Pricing research — mckinneygaragedoorrepairpros.com (McKinney, TX)

Trade: Garage Door Repair. Pricing mode: `cost`. All retrievals 2026-08-23.

## Sourced anchors (each figure read on the page cited)

| Figure | Value | Source (named on page) | URL | Retrieved |
| --- | --- | --- | --- | --- |
| Residential alteration permit rate, single-family | $0.68 per gross sq ft of addition or affected area of alteration | City of McKinney building permit fee schedule for new construction, remodels and repairs | https://www.mckinneytexas.org/DocumentCenter/View/358/Fee-Schedule | 2026-08-23 |
| 1st reinspection fee | $50.00 | Same fee schedule ("Reinspection fees per hour — 1st Reinspection $50.00") | https://www.mckinneytexas.org/DocumentCenter/View/358/Fee-Schedule | 2026-08-23 |
| Median hourly wage, Carpenters (SOC 47-2031), Dallas-Fort Worth-Arlington MSA | $23.44/hr, employment 9,480 | BLS Occupational Employment and Wage Statistics, May 2025 | https://www.bls.gov/oes/current/oes_19100.htm | 2026-08-23 |

BLS retrieval method: bls.gov and the BLS public data API were both unavailable to scripts
(API returned `REQUEST_NOT_PROCESSED — daily threshold ... reached`). Figures were pulled from
the BLS flat-file release instead: https://download.bls.gov/pub/time.series/oe/oe.data.0.Current
(release `2025A01` = May 2025, per https://download.bls.gov/pub/time.series/oe/oe.release).
Exact series IDs used:
- `OEUM001910000000047203108` = area 0019100 (Dallas-Fort Worth-Arlington), occ 47-2031, datatype 08 (hourly median wage) → 23.44
- `OEUM001910000000047203101` = same, datatype 01 (employment) → 9,480
Datatype codes verified at https://download.bls.gov/pub/time.series/oe/oe.datatype.
The human-readable OEWS metro page is cited as `source_url` because a reader can open it even
though a script cannot.

## Other verified local facts used in the body (not anchors)

| Fact | Source | URL | Retrieved |
| --- | --- | --- | --- |
| Doors and Windows are listed among repairs that require a permit; finish work (painting, flooring, cabinets) does not | City of McKinney, Home Repairs & Permit Information | https://www.mckinneytexas.org/3350/Home-Repairs-Permit-Information | 2026-08-23 |
| General contractor registration: "There is no fee or form to fill out"; electrical, plumbing and mechanical registrations carry "No registration fee" | City of McKinney, Contractor Registration | https://www.mckinneytexas.org/257/Contractor-Registration | 2026-08-23 |
| 85% of housing built after 1990, 40% between 2000 and 2009 | Already in site.json `local_facts.housing_vintage` (City of McKinney housing profile) | https://www.mckinneytexas.org/DocumentCenter/View/33676/Updated-Section-II-Housing-Profile-and-Affordability?bidId= | verified 2026-08-21 (existing fact) |

## Cost rows

Seven rows. These are market ranges for the metro, not quotes and not sourced to any single
document: they are reasoned from (a) the metro carpenter wage above as the labor floor,
(b) parts classes named in each row, and (c) the local conditions in the site's existing
`local_facts` (builder-spec ~10,000-cycle springs on post-1990 stock, Collin County hail
damage to rails and struts). No aggregator site is cited anywhere on the page or here.

Unverified by primary source: the dollar ranges themselves. No government or utility document
publishes garage door service prices, so the table is presented on the page as researched market
ranges with the caveat the build inserts automatically.

## Build status

`python template/build.py mckinneygaragedoorrepairpros.com --check-only` → [PASS], /pricing/ 1639 visible words.

## Published price sources, 2026-08-23

Collin County and DFW-wide operators that publish their own figures. All pages read 2026-08-23.

| Company | URL | Figures read |
|---|---|---|
| Prosper Door Repair, McKinney | https://prosperdoorrepair.com/garage-door-spring-repair/mckinney | complete spring repair $150–350, springs replaced in pairs |
| Prosper Door Repair, McKinney | https://prosperdoorrepair.com/garage-door-opener-repair/mckinney | opener repairs $100–250; new opener installed $350–600 |
| Prosper Door Repair, McKinney | https://prosperdoorrepair.com/garage-door-panel-replacement/mckinney | panel replacement $250–800 |
| Prosper Door Repair, McKinney | https://prosperdoorrepair.com/new-garage-door-installation/mckinney | new door installed $800–2,500+ |
| Fast Mobile Garage Doors, Dallas (DFW) | https://fastmobilegaragedoors.com/garage-door-repair-cost-dallas-tx.html | service call and tune-up $75–125; single torsion $150–250; both springs $200–350; extension $100–200; cable $100–200; off-track $125–275; opener repair $75–175; opener replacement $250–500; rollers $75–150; panel $150–400; new door $800–2,500 |
| Garage Door Rescue, Dallas (DFW) | https://garagedoorrescuellc.com/garage-door-repair-cost-dfw/ | spring $150–350; torsion $200–350; dual spring $300–500; opener repair $120–300; opener replacement $350–800; cable $120–250; track $100–280; roller set $120–220; sensor $80–180; panel $250–700+; tune-up $75–150; after-hours premium $50–150; new door $800–3,000+ |
| Metro Garage Door, Plano | https://www.metrogaragedoor.net/garage-door-repair-cost-plano-tx-what-youll-actually-pay-and-why/ | tune-up $75–150; cable $150–250 per cable per side; spring $200–350, broken spring $220–320; panel $250–600+; full door $800–2,500 installed; off-track $125–200 plus $50–150 parts; after-hours premium $50–100; bottom bracket $75–150 |
| M and M Garage, Dallas | https://mandmgaragedfw.com/blog/garage-door-repair-cost-dallas/ | cable $129–349; safety sensor $175–300; track $275–775; standard repairs $150–350 |

### Row by row

1. **Trip out to diagnose, $75–$300.** Low: Fast Mobile $75 service call. High: itemized Garage Door
   Rescue, tune-up and diagnostic visit at the top of its $75–150 band + posted after-hours premium at
   the top of its $50–150 band = **$300 total**. Metro's $75–150 visit plus $50–100 premium
   ($225 top) sits inside.
2. **One snapped torsion spring, $150–$350.** Low: Fast Mobile single torsion $150. High: Garage Door
   Rescue torsion $350, matched by Metro $200–350. Pair figures excluded from this row.
3. **Both springs replaced together, $150–$500.** Low: Prosper complete spring repair $150, which its
   page states covers springs replaced in pairs. High: Garage Door Rescue dual spring $500. Fast Mobile
   both springs $200–350 sits inside.
4. **Cables replaced and door reset on tracks, $100–$500.** Low: Fast Mobile cable $100. High:
   itemized Metro, cables posted at $150–250 per cable per side, so a two-sided replacement is
   2 × $250 = **$500 total**. Garage Door Rescue cable $120–250 with off-track $100–280 and M and M
   $129–349 agree with the band.
5. **Full set of nylon rollers, $75–$220.** Low: Fast Mobile rollers $75. High: Garage Door Rescue
   roller set $220. The row was narrowed from "rollers and worn hinges" because no DFW operator found
   posts a hinge price, so hinges are no longer described in the job.
6. **Opener logic board or gear kit, $75–$300.** Low: Fast Mobile opener repair $75. High: Garage Door
   Rescue opener repair $300. Prosper $100–250 sits inside. Whole-head replacement prices excluded.
7. **Two dented sections, $300–$1,600.** Panels are posted one at a time, so both ends are doubled:
   Fast Mobile $150 per panel × 2 = **$300**; Prosper $800 per panel × 2 = **$1,600**. Garage Door
   Rescue $250–700+ and Metro $250–600+ per panel agree.

### Notes on scope

Row 3 previously described a higher cycle-rated spring set. No operator serving McKinney publishes a
high-cycle upgrade price, so the job was rewritten to the pair replacement that four operators do
price. Quality Garage Door (https://www.qualitygd.com/garage-door-repair-cost-dallas) serves McKinney
but posts no figures, and Plano Overhead and garagedoor-mckinney.com post none either; neither is cited.
Two Collin County pages (Prosper Door Repair, Metro Garage Door in Plano) are used alongside the
DFW-wide lists so the table is not a Dallas clone.

### Build status, 2026-08-23

`python template/build.py mckinneygaragedoorrepairpros.com --check-only` → [PASS], /pricing/ 1731
visible words, zero errors. Anchors (McKinney permit fee schedule, reinspection fee, BLS wage) unchanged.
