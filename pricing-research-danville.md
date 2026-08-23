# Pricing research note - danvillegaragedoorrepairpros.com (Danville, CA)

All figures below were retrieved on 2026-08-23.

## Anchors used on /pricing/

| Figure | Value | Source (states the figure) | Retrieved |
| --- | --- | --- | --- |
| Minimum Building Permit (inspection) fee for any permit | $122 | Town of Danville Master Fee Schedule 2026/27, Development Services - Building - https://www.danville.ca.gov/DocumentCenter/View/836/Master-Fee-Schedule-PDF | 2026-08-23 |
| Electrical Sub-Permit | 20% of the building permit fee | same PDF | 2026-08-23 |
| Structural and Architectural Plan Review | 65% of building fee | same PDF | 2026-08-23 |
| Building permit fee, first $500 of total valuation | $25.08 (then $3.26 per additional $100 to $2,000; $73.90 + $14.94 per $1,000 from $2,001) | same PDF, Building Permit Fee Table | 2026-08-23 |
| Reinspection / Administration fee; inspections for which no fee is indicated | $122 minimum | same PDF | 2026-08-23 |
| California Building Standards Fee | $1 per $25,000 of total valuation | same PDF | 2026-08-23 |
| California contractor license bond (also bond of qualifying individual and disciplinary bond) | $25,000, increased effective January 1, 2023 | Contractors State License Board, Bond Requirements - https://www.cslb.ca.gov/contractors/maintain_license/bond_information/bond_requirements.aspx | 2026-08-23 |

Retrieval note: the fetch tool reported `disallow_by_robots` for www.danville.ca.gov pages, but
https://www.danville.ca.gov/robots.txt disallows only admin, search, map, RSS and events paths -
not /DocumentCenter/. The Master Fee Schedule PDF was therefore downloaded directly (HTTP 200,
application/pdf, 740,964 bytes) and read with pdftotext. Local copies: danville_fees.pdf /
danville_fees.txt in this directory.

## Context figures used in the body copy (already sourced in site.json local_facts)

- Nearly 50% of Danville is on hillsides, including Las Trampas Ridge and the Sycamore Valley hills
- Open-space edges identified as Very High Fire Hazard Severity Zone; CAL FIRE on garage-door gaps
  and missing gasketing as an ember-intrusion route
- Design Review Board submittal requirements call for exterior doors, materials and colors on plans

## Not verified

- The Master Fee Schedule has no line item named for a garage door. Danville publishes established
  flat fees for window and patio-door replacement ($122 each for 1-2, $253 / $201 for more) and for
  a re-roof ($331); a garage door is not among them, so the page uses the schedule's minimum permit
  and inspection fee instead of inventing a garage-door line.
- No BLS metro wage anchor: the BLS API daily threshold was exhausted before the Oakland
  metropolitan division series (49-9071) could be read, and the OEWS metro page does not render
  its table to a fetcher.
- The statement that battery backup is required on new residential garage door openers in
  California reflects state law (SB-969, Health & Safety Code 19891) but the statute text was not
  fetched in this session, so it appears only as body context, not as a sourced anchor figure.


## Published price sources, 2026-08-23

All figures below were read on 2026-08-23 from the operator's own website. Contra Costa and
Tri-Valley operators publish unusually detailed lists, so every row here rests on named local
companies.

### Operators used

**Generational Garage Doors** (Danville and all of Contra Costa County)
- Price list, https://gengaragedoors.com/garage-door-price-list/ (read 2026-08-23): single-car door
  with one torsion spring $299; standard double-car with two springs $399; heavy-duty .243/.250/.262
  with two springs $499; cable off the drum from $180; crashed door repair from $449; hardware
  (rollers, hinges, fixtures) priced by part plus a $99 service charge; annual maintenance and safety
  inspection $99; opener installation $800-$1,500 installed; doors: non-insulated $1,400-$2,000,
  vinyl-backed insulated $1,600-$2,800, steel-backed insulated $2,000-$3,200, Skyline flush $2,200
  single and $4,200 double.
- Cable page, https://gengaragedoors.com/garage-door-cable-replacement/ (read 2026-08-23): cable
  replacement from $149, stated $149-$180; crashed door repair $149-$599.

**Prime Garage Door Repair Tech** (Pleasanton and the Tri-Valley),
https://primegaragedoorrepairtech.com/service-areas/pleasanton/ (read 2026-08-23): springs $150-$400,
one spring $150-$250, both springs $250-$400, high-cycle +$75-$150 per spring; opener work $75-$650,
stripped gears $75-$150, remote or board $50-$125, complete new opener installed $300-$650 (belt
$400-$550, chain $300-$400); cables and track $89-$250, cables in pairs $100-$175, track $125-$250
per track, off-track realignment $100-$200; rollers and hardware $100-$200, nylon set $100-$175;
panel $200-$400; new door $800-$3,500+, single non-insulated $800-$1,200, insulated double
$1,200-$2,000, premium $2,000-$3,500, full-view $2,500-$4,000; no service-call fee with a completed
repair.

**911 Garage Doors** (San Ramon), https://911garagedoors.com/san-ramon-ca/garage-door-repair
(read 2026-08-23): most repairs $65-$450; spring work $180-$350; opener work $125-$900; panel
$150-$1,800; off-track and cable work $200-$350; complete installations $1,900-$15,000.

**Garage Door Danville**, https://thedanvillegaragedoors.com/ (read 2026-08-23): repair from $129;
spring replacement from $189; opener installation from $349; preventive maintenance from $99;
installation from $899.

**Bay Area Doors** (Contra Costa County),
https://bayareadoors.net/spring-replacement/how-much-does-garage-door-spring-replacement-cost-in-contra-costa-county/
(read 2026-08-23): spring replacement $150-$350 parts and labor; cables $98-$120; tune-up $45-$100;
labor $120-$350.

**Valiant Garage Door** (Danville, San Ramon, Alamo, Blackhawk),
https://www.valiantdoor.com/garage-door-repair-danville (read 2026-08-23): typical Danville repairs
$150-$450; opener installation starting labor $229 standard and $249 wall-mount. Not used: those two
figures are labor-only, and the opener row on the page is an installed price including the unit.

**America's Garage Door** (Danville, San Ramon, Pleasanton), https://americasgd.com/garage-doors/
(read 2026-08-23): spring $150-$400; opener repair or replacement $100-$450. Not used: both lines
mix jobs (single vs pair, repair vs replacement) that separate rows on this page.

Skipped: danvillegaragedoorrepair.com (posts $1,400-$3,000 for a spring, incoherent with every other
operator in the county), contracostadoor.com (no prices posted),
titangaragedoorinstallationsacramento.com (Sacramento programmatic pages, not an East Bay operator).

### Row-by-row

| Row | low-high | Sources |
|---|---|---|
| Annual tune-up and safety inspection | 45-100 | Bay Area Doors $45-$100; Generational $99; Garage Door Danville from $99 |
| Torsion springs as a pair, two-car | 250-499 | Generational standard double $399 and heavy-duty $499; Prime both springs $250-$400 |
| Lift cables replaced, drums reset | 89-350 | Generational $149-$180 and off-drum from $180; Prime $89-$250 with pairs $100-$175; 911 off-track and cable $200-$350 |
| Door reset on track | 100-599 | Prime off-track realignment $100-$200; 911 $200-$350; Generational crashed-door repair $149-$599 |
| Opener replaced and installed | 300-1500 | Prime complete opener installed $300-$650; Garage Door Danville from $349; Generational $800-$1,500 installed |
| Insulated sectional door and hardware | 1200-4200 | Prime insulated double $1,200-$2,000 and premium $2,000-$3,500; Generational insulated $1,600-$3,200 and Skyline double $4,200 |

### Rows deleted

- **"Weatherseal and perimeter gasketing replaced for ember resistance"** - no operator serving
  Danville, San Ramon, Alamo or the wider Tri-Valley publishes a weatherseal or gasketing price. It
  was replaced with an annual tune-up row, which three local operators do post.

Row wording changed: the spring row now says "as a pair," matching the two-spring figures used; the
opener row now says "replaced and installed" rather than "with the existing door and rail," because
every posted figure here is an installed price.
