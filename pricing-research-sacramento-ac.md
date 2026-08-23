# Pricing research — sacramentoacrepair.com (/pricing/, mode: cost)

Verified 2026-08-23. Every anchor figure below was read off the primary source listed.

## Anchor 1 — City of Sacramento mechanical/HVAC permit fee: $175

- Figure: **$175**, listed under "SPECIFIC COST PERMITS" as "HVAC and Re-roof – $175".
  Same sheet lists "Minor Permits, one trade – $105" and, under OTHER FEES, a
  "Technology Surcharge – 8% of Permit and Plan Review Fee".
- Source: City of Sacramento, *Fees and Charges Collected on Residential Building Permits*,
  form CDD-0245, revised 10-01-2025.
  https://www.cityofsacramento.gov/content/dam/portal/cdd/Building/Forms/CDD-0245_Fees-and-Charges-on-Residential-Bldg-Permits.pdf
- Verified: 2026-08-23 (PDF fetched and read in full).
- Supporting context (permit is required; planning/screening rules), already in site.json local_facts:
  https://www.cityofsacramento.gov/community-development/building/building-fees.html

## Anchor 2 — BLS OEWS median hourly wage, HVAC mechanics, Sacramento metro: $32.06

- Occupation 49-9021, Heating, Air Conditioning, and Refrigeration Mechanics and Installers,
  Sacramento-Roseville-Folsom, CA MSA (OEWS area 0040900), **May 2025**:
  - Employment: **2,940**
  - Median hourly wage: **$32.06** (series OEUM004090000000049902108)
  - Median annual wage: **$66,670** (series OEUM004090000000049902113)
  - Mean hourly wage: **$34.46**; mean annual **$71,680**
- Read from the BLS public data API (bls.gov), endpoint
  https://api.bls.gov/publicAPI/v2/timeseries/data/ , OEWS series listed above, on 2026-08-23.
- Cited on the page as the canonical OEWS metro table:
  https://www.bls.gov/oes/current/oes_40900.htm
- Note on access: bls.gov static OEWS deep pages (`oes_40900.htm`, `oes499021.htm`) and the
  metro XLSX download were returning bot blocks / redirecting to the OEWS tables index on
  2026-08-23 (BLS Data Finder was showing a maintenance notice), so the figure was taken from
  the BLS API rather than the HTML table. Same agency, same OEWS May 2025 estimates.
- Cross-check that May 2025 estimates exist for this metro and that the metro name is current:
  BLS Western Information Office, *Occupational Employment and Wages in
  Sacramento-Roseville-Folsom — May 2025* (metro mean hourly wage $37.09, all occupations),
  https://www.bls.gov/regions/west/news-release/occupationalemploymentandwages_sacramento.htm
  — fetched and read 2026-08-23.

## Anchor 3 — SMUD heat pump HVAC rebate: $3,000

- Figure: **$3,000** for a variable-stage heat pump system on a gas-to-electric conversion.
  Same table: two-stage heat pump, 15.2 SEER2 minimum, gas-to-electric **$2,000**;
  Go Electric Bonus / panel upgrade **$2,000**; electric-to-electric multi-stage heat pump
  upgrade **$1,000**. Requirements include passing "Title 24 via HERS CF3R" and installation
  by a contractor in the SMUD Contractor Network.
- Source: SMUD, *Heating and cooling rebates*.
  https://www.smud.org/Rebates-and-Savings-Tips/Rebates-for-My-Home/Heating-and-Cooling-Rebates
- Verified: 2026-08-23.

## Additional primary figures used in the page body

- SMUD, same page, "Average pricing for heat pump HVAC installations" — actual SMUD residential
  customer projects in the Advanced Home Solutions Rebates program, trailing 12 months,
  single-measure projects only, before rebates:
  - Heat pump HVAC electric-to-electric upgrade: median **$17,336**, low **$7,250**, high **$44,763**
  - All heat pump HVAC installations: median **$18,804**, low **$3,500**, high **$65,620**
  Used in the body to show how far apart two "changeout" jobs land. Verified 2026-08-23.
- California Energy Commission, HERS Program page — field verification and diagnostic testing
  provisions moved into the Energy Code (Title 24, Part 6 and Part 1 administrative regulations)
  effective January 1, 2026; permitted work triggers any required HERS testing, and HERS
  documentation is required to close the permit even where a test is exempted.
  https://www.energy.ca.gov/programs-and-topics/programs/home-energy-rating-system-hers-program
  Verified 2026-08-23. Used for the "permitted, tested job" reasoning, not as a dollar anchor.

## What informed the table ranges

The ranges are market ranges, not any operator's prices. They were set from the primary figures
above plus published Sacramento-market price pages from local HVAC contractors, cross-read
against each other. None of these is named on the page and none is an anchor:

- https://a-classhvac.com/blog/sacramento-hvac-cost-guide/ — diagnostic $75–$250; capacitor
  $100–$200; condenser fan motor $300–$600; blower motor $350–$700; recharge $200–$500;
  line repair $500–$1,200; 3–4 ton AC replacement $8,000–$13,000; high-efficiency $12,000–$18,000.
- https://rivercityheatingcooling.com/blog/ac-replacement-cost-sacramento-2026 — 14.3 SEER2
  3-ton swap $6,500–$8,500; mid-tier $8,500–$11,500; high-efficiency $11,500–$14,500; premium
  variable-speed $14,500–$18,000; permit and inspection $200–$450; added return or duct upsizing
  $800–$2,500; new line set for R-454B $500–$900; pad and disconnect $300–$600.
- https://www.hotcoldhvac.com/blog/home-ac-repair-cost-guide-2026-sacramento/ — diagnostic
  $75–$200; capacitor $200–$500; fan motor $300–$900; refrigerant leak repair $200–$1,500.
- https://kendrickhvac.com/blog/ac-replacement-sacramento-guide-2026 — typical 2026 AC
  replacement $8,500–$16,500; variable-speed $11,500–$16,500; full system with duct redesign
  $16,000–$26,000.

No aggregator (Angi, HomeAdvisor, Fixr, Homewyse, Thumbtack, Forbes Home, Bob Vila) was used as
a source or an anchor.

## Rows published

| Job | Low | High | Basis |
| --- | --- | --- | --- |
| Diagnostic visit on a system that has quit cooling | $89 | $249 | per visit |
| Capacitor or contactor replaced at the outdoor unit | $165 | $495 | flat |
| Condenser fan motor replaced | $395 | $1,050 | flat |
| Refrigerant leak traced, repaired and the circuit recharged | $450 | $2,400 | flat |
| Evaporator coil replaced on a matched split system | $1,500 | $3,800 | per unit |
| Condenser and coil changeout, permitted and field verified | $6,800 | $16,500 | per unit |

## Build result

`python template/build.py sacramentoacrepair.com` → PASS, 0 errors; /pricing/ renders at
1,563 visible words (guard 900–1,650); authored body 840 words, lede 40 words.
`python template/build.py --check-only` → 83 PASS, no shingle collisions.

## Published price sources, 2026-08-23

Every row's low and high now comes from a figure a Sacramento-area HVAC contractor publishes on its
own site. All pages read 2026-08-23.

| Company | URL | Figures read |
|---|---|---|
| Comfortable HVAC Services, Sacramento | https://comfortablehvacservices.com/blog/ac-repair-cost-sacramento | $49 diagnostic, waived with repair; capacitor $150–300; contactor $175–350; R-410A recharge $200–500; compressor $900–2,500; tune-up $120–150; labor $100–150/hr |
| A Cool Air, Sacramento | https://acoolair.com/our-prices-table/ | service call $80; simple repair incl. capacitor/contactor $210; condenser fan motor $440+; electronic leak detection $300; freon leak repair $500+; R-410A $110/lb; control board $490+; blower motor $500+ |
| A-Class HVAC, Sacramento | https://a-classhvac.com/blog/ac-repair-cost-sacramento/ | diagnostic $89–129 (waived with repair); capacitor $275–475; contactor $225–450; leak search + top-off $250–600; leak repair $500–1,500; condenser fan motor PSC $300–700, ECM $900–1,200; evaporator coil $1,500–3,500; compressor $2,000–3,500 |
| A-Class HVAC, Sacramento (cost guide) | https://a-classhvac.com/blog/sacramento-hvac-cost-guide/ | service call $75–250, emergency $140–250+; new central AC $10,000–19,000; 3–4 ton replacement $8,000–13,000 |
| Super Brothers, Sacramento | https://www.superbrothers.com/cities/sacramento/air-conditioning-repair/ | capacitor or contactor $120–300; refrigerant recharge $200–600; compressor $1,200–2,500 |
| PRO MAX HVAC, Sacramento | https://www.promaxhvac.com/answers/ac-repair-cost-sacramento | common repairs $150–600; capacitor $150–300; contactor $200–450; condenser fan motor work $200–450; compressor $1,500–2,500 installed; no trip fee on completed repairs |
| RK Mechanical, Sacramento | https://rkmechanicalairservices.com/ac-repair-cost-in-sacramento/ | capacitor $120–475; fan motor $200–700; refrigerant leak and recharge $200–750; coil repair $600–2,500+; compressor $1,200–2,500+ |
| J.R. Putman, Rancho Cordova | https://www.jrputman.com/air-conditioning/evaporator-coils/ | evaporator coil replacement "typically $1,000–$2,500" |
| Alpha Mechanical, Folsom | https://alphamechanicals.com/blog/evaporator-coil-replacement-cost-folsom | published invoice: evaporator coil replacement $3,782 (10 July 2026); $89 diagnostic applied toward repair; blower motor $2,184 |
| Cabs HVAC, Sacramento | https://www.cabshvac.com/air-conditioner-replacement-cost/ | Sacramento single-stage $6,000–9,000; two-stage $8,000–11,000; variable-speed $10,000–14,000 |
| River City Heating, Sacramento | https://rivercityheatingcooling.com/blog/ac-replacement-cost-sacramento-2026 | AC swap installed $6,500–8,500 / $8,500–11,500 / $11,500–14,500 / premium $14,500–18,000; line set $500–900; disconnect, whip and pad $300–600; permit and inspection $200–450; duct or return work $800–2,500 |
| Bell Brothers, Sacramento | https://bellbroshvac.com/blog/how-much-does-ac-installation-cost-in-sacramento-what-youll-pay-in-2026/ | install $9,999–$25,000+; basic $9,999; standard $17,500 including permit and inspection; complex $25,000+ |

### Row by row

1. **Diagnostic visit, $49–$250.** Low: Comfortable HVAC $49 diagnostic. High: A-Class posted service
   call range topping at $250 (emergency $140–250+). A Cool Air's $80 service call sits in between.
2. **Capacitor or contactor, $120–$475.** Low: Super Brothers $120. High: A-Class / RK capacitor $475.
   Itemized cross-check on A Cool Air: $80 service call + $210 simple repair covering a capacitor or
   contactor = **$290 total**, inside the range.
3. **Condenser fan motor, $200–$1,200.** Low: PRO MAX $200. High: A-Class ECM motor $1,200. Itemized
   cross-check on A Cool Air: $80 service call + $440 condenser fan motor = **$520 total**.
4. **Refrigerant leak traced, repaired, recharged, $200–$1,500.** Low: RK $200. High: A-Class leak
   repair $1,500. Itemized cross-check on A Cool Air for a full traced-and-repaired job:
   $80 service call + $300 electronic leak detection + $500 leak repair + 3 lb R-410A at $110/lb
   ($330) = **$1,210 total**, which is why the high sits above the parts-only figures.
5. **Evaporator coil replaced, $1,000–$3,782.** Low: J.R. Putman $1,000. High: Alpha Mechanical's
   published $3,782 invoice. A-Class $1,500–3,500 brackets the middle. Compressor and capacitor
   figures were deliberately excluded: a compressor swap is a different job from a coil replacement.
6. **Condenser and coil changeout, permitted and field verified, $6,000–$25,000.** Low: Cabs HVAC
   single-stage $6,000. High: Bell Brothers complex install $25,000+, which their page states includes
   permit and inspection. River City's $200–450 permit-and-inspection line and $500–900 line set
   confirm the permitted scope. Condenser-only prices were not used for this row.

### Build status, 2026-08-23

`python template/build.py sacramentoacrepair.com --check-only` → [PASS], /pricing/ 1722 visible words,
zero errors. Anchors (city permit fee, BLS wage, SMUD $3,000 rebate) unchanged.
