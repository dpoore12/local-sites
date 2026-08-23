# Pricing research — overlandparkgaragedoorrepairpros.com (Overland Park, KS)

Trade: Garage Door Repair. Pricing mode: `cost`. All retrievals 2026-08-23.

## Sourced anchors (each figure read on the page cited)

| Figure | Value | Source (named on page) | URL | Retrieved |
| --- | --- | --- | --- | --- |
| Flat building permit fee, remodel/repair project valued under $5,000 | $30 (and $50 for projects valued $5,000–$19,000) | City of Overland Park, Common Permit Fees | https://www.opkansas.gov/common-permit-fees | 2026-08-23 |
| Flat plan review fee, due at application | $30 (so $60 total for work valued $1–$5,000) | Overland Park Master Fee Schedule effective 08-01-2025 | https://content.civicplus.com/api/assets/ks-overlandpark/5c2ef6d8-b38f-41aa-999c-0537f894e89c?cache=1800 | 2026-08-23 |
| Median hourly wage, Carpenters (SOC 47-2031), Kansas City MO-KS MSA | $29.72/hr, employment 4,540 | BLS Occupational Employment and Wage Statistics, May 2025 | https://www.bls.gov/oes/current/oes_28140.htm | 2026-08-23 |

Note on the permit fee: the Common Permit Fees page renders its fee text with JavaScript, so it
was confirmed by screenshot as well as by the master fee schedule PDF. The screenshot shows
verbatim: "Projects valued less than $5,000 / Permits for these projects are $30." and
"Projects valued between $5,000 and $19,000 / Permits for these projects are $50."
The master fee schedule states: "The Flat Building Permit Fee shall be paid in addition to the
Flat Plan Review Fee" and "Total Plan Review and Permit Fee — work valued at $1 - $5,000: $60".

BLS retrieval method: bls.gov HTML and the BLS public data API were both unavailable to scripts
(API: `REQUEST_NOT_PROCESSED — daily threshold ... reached`). Figures came from the flat-file
release https://download.bls.gov/pub/time.series/oe/oe.data.0.Current, release `2025A01` = May 2025.
Series IDs:
- `OEUM002814000000047203108` = area 0028140 (Kansas City, MO-KS), occ 47-2031, datatype 08 (hourly median) → 29.72
- `OEUM002814000000047203101` = same, datatype 01 (employment) → 4,540

## Other verified local facts used in the body (not anchors)

| Fact | Source | URL | Retrieved |
| --- | --- | --- | --- |
| Overland Park requires contractors to hold an active Johnson County contractor's license to receive a building permit for work in the city | City of Overland Park, Building + Construction | https://www.opkansas.org/city-services/building-construction/ | 2026-08-23 |
| Median year built 1989 | Existing site.json `local_facts.housing_vintage` | https://data.census.gov/table/ACSDT5Y2024.B25035?tid=ACSDT5Y2024.B25035 | verified earlier (existing fact) |
| Jan 24, 2026 Johnson County winter storm warning, wind chills to 17 below, 4–6 in. additional snow | Existing site.json `local_facts.january_2026_cold_snap` (NWS Kansas City/Pleasant Hill) | https://forecast.weather.gov/showsigwx.php?warnzone=KSZ105&warncounty=KSC091&firewxzone=KSZ105&local_place1=Overland+Park+KS&product1=Winter+Storm+Warning | existing fact |

## Attempted and not found

- Johnson County Contractor Licensing fee amounts. The county's Contractor Licensing pages were
  reachable but no fee schedule page with dollar amounts could be retrieved
  (https://www.jocogov.org/department/contractor-licensing returned no fee figures;
  a /license-fees path returned a client error). The license requirement is cited in the body
  from the city's own page instead, with no dollar figure attached. Not used as an anchor.

## Cost rows

Seven rows. Market ranges for the metro, reasoned from the metro carpenter wage as the labor
floor, the parts class in each row, and local conditions already sourced in the site's
`local_facts` (1989 median build year producing a mix of extension-spring and torsion
installations; January cold snap exposing end-of-life springs). No aggregator source is used or
cited. The ranges themselves are not published by any government document — that is the one thing
on this page that cannot be verified against a primary source, which is why the page frames them
as researched market ranges rather than prices.

## Build status

`python template/build.py overlandparkgaragedoorrepairpros.com --check-only` → [PASS], /pricing/ 1545 visible words.

## Published price sources, 2026-08-23

Kansas City metro operators that publish their own figures. All pages read 2026-08-23. This is the
thinnest of the five markets: most Johnson County shops advertise free estimates and publish no
numbers, which is why the table now carries five rows rather than seven.

| Company | URL | Figures read |
|---|---|---|
| KC Door Company, Kansas City | https://www.kcdoorcompany.com/blog/how-much-does-it-cost-to-replace-garage-door-springs | torsion springs $50–150 per spring; extension springs $15–45 each; professional labor $150–300; complete spring replacement, parts and labor, $150–400 |
| State Line Door and Lift, Kansas City | https://statelinedoorlift.com/garage-door-repair-kansas-city-kansas | most repairs $125–290 including materials and labor; spring repair $95–290; spring replacement $200–300; torsion spring part $40–100; extension spring part $5–30; opener or cable work $100–190 plus parts; free on-site estimates |
| All Access Door KC, Kansas City | https://www.allaccessdoorkc.com/spring-replacement | residential service calls start at $80 |
| 5 Star Garage Door Services, Blue Springs | https://5stargaragedoorservices.com/garage-door-repair/ | garage door repair $150–450, with track adjustment and cable tightening at the low end and spring or cable replacement higher |
| Premier Garage Doors, Overland Park | https://www.premier-garagedoor.com/ | torsion or extension spring replaced from $189; free service call on every repair |
| Radio Controlled Garage Door, Kansas City | https://radiocontrolledgaragedoorandgate.com/the-cost-of-garage-door-opener-installation-in-kansas-city-mo-whats-included/ | chain-drive opener $150–300; belt $200–500; screw $200–400; smart $300–600+; professional installation $150–300; rails and brackets $50–100; remotes and keypads $20–50 |
| Team Taylor Doors, Kansas City | https://www.teamtaylordoors.com/garage-door-opener-installation-in-kansas-city/ | opener installation labor $100–300; installation fee $100–500; opener replacement $200–600 |
| Bernard Exteriors, Overland Park | https://bernardexteriors.com/post/how-much-should-i-budget-for-a-new-garage-door | standard steel door $700–1,500; insulated or premium door $1,500–3,500+; custom wood or carriage $4,000+; professional installation $200–500, with the door prices stated to exclude installation |
| Priority Garage Door Service, Olathe | https://www.prioritygaragedoorservice.com/service-areas/olathe-ks-garage-door-repair | a new door can cost $799.00 to $40,000.00 depending on size, weight and insulation |

### Row by row

1. **First visit plus a common repair, $80–$450.** Low: All Access Door KC service calls start at $80.
   High: 5 Star repair band top of $450. State Line's $125–290 for most repairs including materials and
   labor sits inside. The job wording was widened from a diagnosis-only visit because these operators
   post visit-plus-repair figures rather than a standalone diagnostic fee.
2. **Torsion spring pair renewed, $150–$600.** Low: KC Door Company complete spring replacement $150,
   parts and labor. High: itemized KC Door Company, two torsion springs at $150 each + labor at the top
   of its $150–300 band = **$600 total**. State Line $200–300 and Premier from $189 sit inside.
3. **Extension springs replaced on an older single door, $180–$390.** Both ends are itemized from KC
   Door Company: low = two extension springs at $15 each ($30) + labor $150 = **$180 total**;
   high = two at $45 each ($90) + labor $300 = **$390 total**. State Line's extension spring part at
   $5–30 and its $95–290 spring repair band agree with the shape. The row no longer claims added
   containment cables, which no operator here prices.
4. **Opener swapped for a belt or wall-mount unit, $300–$1,100.** Both ends are itemized. Low: Radio
   Controlled chain-drive opener $150 + professional installation $150 = **$300 total**. High: Team
   Taylor opener replacement $600 + installation fee $500 = **$1,100 total**.
5. **Insulated double door replaced and hauled away, $799–$4,000.** Low: Priority Garage Door Service
   posts new doors from $799.00. High: itemized Bernard Exteriors, insulated or premium door $3,500 +
   professional installation $500, which their page states is separate from the door price =
   **$4,000 total**.

### Rows deleted

- **Bent track section and flattened rollers replaced.** No Kansas City metro operator located
  publishes a track or roller figure. Royalty Garage (https://www.royaltygarage.com/broken-spring-replacement),
  Garage Door Service of Kansas City (https://www.garagedoorservice-kansascity.com/garage-door-cable-replacement/),
  ProLift Doors Johnson County, Right Track Door, AGDS and Bousman Door all publish service pages with
  no prices; A1 Garage's Overland Park page (https://a1garage.com/overland-park-ks/) shows fees only
  inside customer review text, which is not a posted price list.
- **Bottom section replaced after a bumper strike.** No operator serving Overland Park posts a panel or
  section price. Rather than keep an invented figure, the row was removed; five rows still satisfies the
  build's four-to-eight requirement.

Also checked and not cited: Overhead Door Company of Kansas City posts a $129 annual maintenance
program and promotional tune-up coupons rather than repair prices
(https://overheaddoorkansascity.com/services/garage-door-maintenance-in-kansas-city/), so no discount
figure was carried onto the page.

### Build status, 2026-08-23

`python template/build.py overlandparkgaragedoorrepairpros.com --check-only` → [PASS], /pricing/ 1624
visible words, zero errors. Anchors (Overland Park permit fee, plan review fee, BLS wage) unchanged.
