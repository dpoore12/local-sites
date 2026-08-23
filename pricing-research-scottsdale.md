# Pricing research — scottsdalegaragedoorrepairpros.com (Scottsdale, AZ)

Trade: Garage Door Repair. Pricing mode: `cost`. All retrievals 2026-08-23.

## Sourced anchors (each figure read on the page cited)

| Figure | Value | Source (named on page) | URL | Retrieved |
| --- | --- | --- | --- | --- |
| Minimum Permit (one discipline) | $121 | City of Scottsdale Miscellaneous Permit Fee Schedule, Exhibit A, Resolution No. 13391, effective July 1, 2025 | https://www.scottsdaleaz.gov/docs/default-source/scottsdaleaz/planning---develpment/fees-fy25-26/permit-fee-schedule---miscellaneous.pdf?sfvrsn=8c6543cc_4 | 2026-08-23 |
| Reinspection | $121 | Same fee schedule | https://www.scottsdaleaz.gov/docs/default-source/scottsdaleaz/planning---develpment/fees-fy25-26/permit-fee-schedule---miscellaneous.pdf?sfvrsn=8c6543cc_4 | 2026-08-23 |
| Minimum Combination (all disciplines) | $379 | Same fee schedule (verified, not used on the page) | same URL | 2026-08-23 |
| Contractor licensing exemption threshold, aggregate contract price incl. labor and materials | under $1,000, and only where no local building permit is required; splitting contracts to evade it is prohibited | Arizona Revised Statutes 32-1121 | https://www.azleg.gov/ars/32/01121.htm | 2026-08-23 |
| Median hourly wage, Carpenters (SOC 47-2031), Phoenix-Mesa-Chandler metro | $29.00/hr, employment 12,710 | BLS Occupational Employment and Wage Statistics, May 2025 | https://www.bls.gov/oes/current/oes_38060.htm | 2026-08-23 |

Verbatim from A.R.S. 32-1121(A)(14): exempt is "Any person other than a licensed contractor
engaging in any work or operation on one undertaking or project by one or more contracts, for which
the aggregate contract price, including labor, materials and all other items ... is less than
$1,000," and the exemption does not apply "In any case in which the performance of the work
requires a local building permit," nor where work is divided "in contracts of amounts less than
$1,000 ... for the purpose of evasion of this chapter."

BLS retrieval method: bls.gov HTML and the BLS public data API were both unavailable to scripts
(API: `REQUEST_NOT_PROCESSED — daily threshold ... reached`). Figures came from
https://download.bls.gov/pub/time.series/oe/oe.data.0.Current, release `2025A01` = May 2025.
Series IDs:
- `OEUM003806000000047203108` = area 0038060 (Phoenix-Mesa-Chandler), occ 47-2031, datatype 08 (hourly median) → 29.00
- `OEUM003806000000047203101` = same, datatype 01 (employment) → 12,710

## Other verified local facts used in the body (not anchors)

| Fact | Source | URL | Retrieved |
| --- | --- | --- | --- |
| Work needing no permit includes "Non-structural items such as glass in doors or windows, interior doors, hardware, kitchen cabinets, carpeting, flooring or trim work (not affecting a pool enclosure or garage)" | City of Scottsdale, Home Improvement | https://www.scottsdaleaz.gov/planning-development/home-improvement | 2026-08-23 |
| 30 consecutive days at or above 110°F in Phoenix, July 2023; 42 Maricopa County excessive heat warning days in 2023 | Existing site.json `local_facts.extreme_heat` (NWS Phoenix 2023 Monsoon Season Review) | https://www.weather.gov/psr/2023MonsoonSeasonReview | existing fact |
| Aug 22, 2024 Scottsdale thunderstorm: uprooted trees, downed power lines, >0.5 in. rain in 30 minutes | Existing site.json `local_facts.monsoon_wind_event` | https://www.weather.gov/psr/Aug222024 | existing fact |
| Historic Preservation Commission reviews exterior alterations for properties on the Scottsdale Historic Register | Existing site.json `local_facts.historic_exterior_review` | https://www.scottsdaleaz.gov/historic-preservation-program | existing fact |

## Notes and limits

- No Scottsdale fee line names garage doors specifically. The page therefore uses the published
  minimum single-discipline permit fee, which is the floor any permitted door job would hit, and
  says so in the anchor detail rather than implying a garage-door-specific fee exists.
- The seven cost rows are market ranges for this metro, reasoned from the Phoenix wage floor, the
  parts class in each row, and the heat and monsoon conditions already sourced in the site's
  `local_facts`. The upper bound of the custom-door row reflects clad/full-view doors common in the
  ranch communities; it is a market observation, not a published figure. No aggregator source is
  used or cited anywhere.

## Build status

`python template/build.py scottsdalegaragedoorrepairpros.com --check-only` → [PASS], /pricing/ 1536 visible words.

## Published price sources, 2026-08-23

Phoenix-metro operators that serve Scottsdale and post their own figures. All pages read 2026-08-23.

| Company | URL | Figures read |
|---|---|---|
| Above All Garage Door, Scottsdale | https://www.above-allgaragedoor.com/pricing | service call $35, credited if work proceeds; torsion spring $180–290 per spring fitted; high-cycle +$80–120 per spring; cable pair $200; drum $125 each; nylon rollers whole door $249; hinge $125 each; off-track from $200; opener gear kit $289; Chamberlain belt drive installed $689; wall mount from $1,350; tune-up visit $100 |
| Above All Garage Door, Scottsdale (Arizona cost list) | https://www.above-allgaragedoor.com/guides/garage-door-repair-cost-arizona | 16x7 double door $1,800, insulated with windows $2,650; 8x7 single $1,250, insulated $1,650 |
| Triple B Garage Doors, Scottsdale and Phoenix metro | https://triplebgaragedoors.com/pricing/ | both springs, standard 20,000-cycle, 16x7 door $355; both springs, 80,000-cycle $425; heavy door pair $525; jumped cable repair $215–295; premium nylon roller set of 10 $325; tune-up $125; LiftMaster belt drive installed $830; 16x7 installed from $1,590 |
| Same Day Garage Door, Phoenix | https://samedaygaragedoorservices.com/resources/garage-door-spring-repair-cost-in-phoenix-2026-guide | single torsion $270; double/pair $540; extension pair $319; spring plus cable $575–900 |
| Great Doors and Gates, Phoenix | https://greatdoorsandgatesaz.com/2026/03/21/garage-door-spring-replacement-cost-in-phoenix-what-youll-pay-in-2026-and-why-prices-vary-so-much/ | spring replacement $150–400; single torsion $150–250; dual $250–400; extension pair $150–225; extended life +$50–100 |
| Pride Garage Doors, Phoenix | https://www.pridegaragedoors.com/services/phoenix-garage-door-roller-replacement/ | single spring $199–299; double spring $299–399; opener repair $120 and up; panel replacement starts at $200+ |
| Level Up Garage Door, Mesa (East Valley incl. Scottsdale) | https://www.levelupgaragedoor.com/garage-door-opener-repair-az | gear, sprocket, capacitor or sensor repair from $275; openers $650–750 installed |
| Level Up Garage Door, Mesa | https://www.levelupgaragedoor.com/garage-door-panel-replacement-az | single-section replacement $250–800 |
| Rite-A-Way, Scottsdale | https://www.callriteaway.com/service-pages/garage-door-opener-installation | opener installation $300–800 including removal of the old unit; opener itself from $150 |
| Rite-A-Way, Phoenix | https://www.callriteaway.com/blog/the-cost-of-garage-door-replacement-in-phoenix-a-2025-guide | replacement $800–3,500; single $800–1,500; double $1,500–3,500; custom $2,000–6,000+ |
| Garage Door 101, Scottsdale | https://www.garagedoor101.net/services/garage-door-panel-replacement | $500–2,500 per panel |
| Elite Garage Doors, Scottsdale | https://elitegaragedoorsandgates.com/garage-door-installation-cost-in-scottsdale/ | single-car $800–2,500 installed; two-car $1,500–5,000; wood $2,000–5,000 with premium cedar reaching $10,000; carriage house $2,000–10,000; full-view glass above $6,000; permits $50–200 |
| High Grade Doors, Scottsdale | https://highgradegaragedoors.com/how-much-does-a-new-garage-door-cost-in-scottsdale-az/ | new door $1,200–6,000 installed; insulated steel double $1,800–3,500; single $750–2,500; opener $218–539 installed |

### Row by row

1. **One torsion spring, $150–$299.** Low: Great Doors single torsion $150. High: Pride $299. Same Day
   $270 and Above All $180–290 per spring sit inside. Pair prices were kept off this row.
2. **Matched pair, $250–$580.** Low: Great Doors dual $250. High: itemized Above All, two springs at
   $290 fitted = **$580 total**; the $35 service call is credited when work proceeds, so it is not
   added. Same Day $540 and Triple B $355 / $425 / $525 confirm the band.
3. **Roller set and hinges, $249–$499.** Low: Above All nylon rollers, whole door, $249. High:
   itemized Above All, $249 rollers + two hinges at $125 = **$499 total**. Triple B's $325 ten-roller
   set with servicing included sits between.
4. **Opener gear kit, board or capacitor, $120–$289.** Low: Pride opener repair from $120. High: Above
   All gear kit $289. Level Up's from-$275 repair floor sits inside. Whole-head prices excluded.
5. **Opener replaced, installed, $218–$950.** Low: High Grade $218 installed. High: itemized
   Rite-A-Way, opener from $150 + installation $300–800 including removal = **$950 total**. Above All's
   $689 belt drive installed, Triple B $830 and Level Up $650–750 sit inside.
6. **Two sections replaced, $400–$5,000.** Sections are posted per panel, so both figures are doubled:
   Pride from $200 per panel × 2 = **$400**; Garage Door 101 $2,500 per panel × 2 = **$5,000**. Level Up
   $250–800 per section × 2 = $500–1,600 sits inside.
7. **Custom wood-look or full-view door, $2,000–$10,000.** Low: Elite wood from $2,000. High: Elite
   carriage-house and premium cedar reaching $10,000; Elite also posts full-view glass above $6,000.
   Rite-A-Way custom $2,000–6,000+ agrees.

### Row deleted

**Bottom weather seal and threshold reset** was removed. Only one operator serving Scottsdale posts a
figure (Lucky Boy Garage Door, weather seal $150–450,
https://www.luckyboygaragedoor.com/weather-seal-replacement), and the build requires two separate
businesses per row. The nearest other posted seal price found, Kooler Garage Doors at $434 single and
$618 double (https://koolergaragedoors.com/garage-door-weather-seal-replacement-cost/), is a Grand
Junction and Montrose, Colorado price and does not apply to this metro. The row was replaced with the
opener-replacement row above, which four operators price.

### Build status, 2026-08-23

`python template/build.py scottsdalegaragedoorrepairpros.com --check-only` → [PASS], /pricing/ 1707
visible words, zero errors. Anchors (Scottsdale minimum permit, ARS 32-1121 threshold, BLS wage) unchanged.
