# Phoenix leak detection — phase 2 research (primary sources, fetched 2026-08-25)

## Post-tension slab (the site's differentiator)
- 2024 Phoenix Building Construction Code, adopted by City Council June 18, 2025, Ordinance G-7397, effective August 1, 2025. Includes 2024 IBC, IRC, IPC, UPC, ISPSC.
  https://www.phoenix.gov/administration/departments/pdd/tools-resources/codes-ordinance/building-code.html
- 2024 IBC Phoenix amendment **Section 1907.5 Post-tensioned slabs on ground**: "All post-tensioned slabs on ground shall be permanently stamped, marked, or otherwise identified in a conspicuous location... Conspicuous locations include, but are not limited to, entrance porches, slabs at garage doors, or patio slabs."
  Stated reasons: "Many structures have been, and continue to be, constructed with post-tensioned slabs on ground"; "If a tendon is cut throughout the life of the structure, it can cause serious injury to people in the area"; the stamp lets "the contractor... know to identify tendon locations before cutting or drilling into the slab."
  https://www.phoenix.gov/content/dam/phoenix/pddsite/documents/codes-ordinances/amendmentcodes/2024-ibc.pdf
- 2024 IBC Phoenix amendment **1803.5.13**: geotechnical investigation required for design of all *structural* post-tensioned slabs on ground; report must include soil parameters per PTI DC-10.5; drawings must show slab type, bearing value and depth, coefficient of subgrade friction, soil subgrade modulus, **em and ym for expansive soils**, and special inspection requirements. (Same PDF.)
- Earlier version: 2018 PBCC, Ordinance G-6463, effective July 6, 2018 — 1907.2 stamping + 1803.5.13.
  https://www.phoenix.gov/content/dam/phoenix/pddsite/documents/codes-ordinances/2018%20international%20building%20code%20(ibc)%20phoenix%20amendments.pdf

## Money / city policy
- **Phoenix City Code 37-27**: "Each customer served by City water is responsible for all leaks, or damages due to leaks, downstream of the customer's point of service delivery. Each customer is responsible for full payment of charges to the City for any water lost due to leaks..." 37-27(B): customer must maintain pipes, faucets, valves, sprinklers and fixtures in good repair; Director may terminate service in an emergency or after 10 days' written notice.
  https://phoenix.municipal.codes/CC/37-27
  → **There is no Phoenix water-leak credit/adjustment program.** The brief's premise of a "leak adjustment or high-bill credit policy" is wrong for Phoenix.
- Only published adjustment: **Sewer Fee Review** (sewer charge recalculated each July from average Jan–Mar use; request more than 60 days after the July bill date is ineligible; prior years not adjusted).
  https://www.phoenix.gov/administration/departments/waterservices/city-services-bill/submit-a-sewer-fee-review.html
- **Point of service delivery**, Phoenix City Code Section 37-1, quoted in city handout: "the terminal end of a service connection from the public water system. If a meter is installed at the end of the service connection, then the point of service delivery shall mean the downstream end (i.e., customer's side) of the meter."
  https://www.phoenix.gov/content/dam/phoenix/pddsite/documents/trt/external/dsd_trt_pdf_00634.pdf
- Water rates effective March 2025: $6.13 per 100 cubic feet June–Sept inside city, $4.93 low season, $4.64 monthly service charge on 5/8-inch meter (from site.json pricing anchors).
  https://www.phoenix.gov/content/dam/phoenix/waterservicessite/documents/rates_effective_march_2025.pdf
- Minimum residential permit fee $195, includes first re-inspection, $195 each re-inspection after.
  https://www.phoenix.gov/content/dam/phoenix/pddsite/documents/impact-fees/fee-schedule.pdf

## Meter / leak checking
- City "Outdoor Leaks": "the City of Phoenix operates one of the country's most aggressive leak detection programs"; "Unaccounted for month-to-month or year-to-year increases in cost or water consumption units may indicate a leak"; inspect irrigation weekly/biweekly to "prevent water damage to plants, patios, and building slabs"; insulate exposed outdoor pipe against winter freeze.
  https://www.phoenix.gov/administration/departments/waterservices/supply-conservation/save-water/how-to-save-water/outdoor-leaks.html
- "Do You Have a High Water Bill?": start with the bill, surges may mean an undetected outdoor leak.
  https://www.phoenix.gov/administration/departments/waterservices/supply-conservation/save-water/how-to-save-water/do-you-have-a-high-water-bill.html
- Billable water units = current read minus previous read (example 241 - 234 = 7 units); meters read by electronic device.
  https://www.phoenix.gov/administration/departments/waterservices/city-services-bill/how-to-read-your-city-services-bill.html
  https://www.phoenix.gov/administration/departments/waterservices/city-services-bill/general-service-issues.html
- Water emergency hotline 602-261-8000; customer service 602-262-6251.
  https://www.phoenix.gov/administration/departments/waterservices/contact-us.html
- Phoenix Water Smart residential GPCD: 139 (1990), 137 (2000), 108 (2010), 102 (2020), 92 (2023).
  https://waterworks.phoenix.gov/water-conservation/

## Licensing and permits
- ARS 32-1121(A)(14): licensure exemption only where aggregate contract price is **less than $1,000** including labor and materials, work is "of a casual or minor nature," and the exemption **does not apply** "in any case in which the performance of the work requires a local building permit," nor where the work is part of a larger operation or split into sub-$1,000 contracts.
  https://www.azleg.gov/ars/32/01121.htm
- ROC: "Generally, if labor and materials exceed $1,000 OR a permit is required (regardless of the price of labor and materials), then a license is required."
  https://roc.az.gov/license-classifications
- Phoenix PDD residential guidance: permits required to move or add sinks, toilets and tubs; not required to replace existing fixtures or existing landscape irrigation.
  https://www.phoenix.gov/administration/departments/pdd/residential-building/resident-plan-reviews.html
  Work Exempt from Permit handout: https://www.phoenix.gov/content/dam/phoenix/pddsite/documents/trt/external/dsd_trt_pdf_00618.pdf

## Soils and ground movement
- UA Cooperative Extension az1281 (peer reviewed, March 2002): caliche = soil particles cemented by calcium carbonate, at or below surface, lumps under 1 inch to several inches, or a solid layer "ranging from a few inches to several feet in thickness"; it restricts root development and **restricts water drainage**.
  https://extension.arizona.edu/publication/managing-caliche-home-yard
- USGS Professional Paper 1781, Section 7, West Salt River Valley: pumping caused water-level declines of more than 50 ft, in places more than 300 ft; "water depletion has led to aquifer compaction and land subsidence"; east of the White Tank Mountains and north of I-10 the land surface "had subsided as much as 18 ft by 1995" and reversed flow in part of the Dysart Drain. Middle basin unit up to 800 ft thick with playa/alluvial-fan/fluvial silt, clay, siltstone; lenses over 80 percent silt and clay near Goodyear and Glendale. 1980 Groundwater Management Code created ADWR and the Phoenix Active Management Area.
  https://pubs.usgs.gov/pp/1781/pdf/pp1781_section7.pdf
- Arizona Geological Survey: groundwater withdrawal drives subsidence and earth fissures; Maricopa County hosts fissures; fissures can damage utility lines, roads, canals (site.json local_fact).
  https://azgs.arizona.edu/earth-fissures-ground-subsidence/more-arizonas-earth-fissures

## Climate
- NWS Phoenix: "Our 'monsoon season' officially extends from June 15th through September 30th"; flash floods are the #1 thunderstorm-related killer in Arizona.
  https://www.weather.gov/psr/monsoonawarenessweek

## Water chemistry
- Phoenix 2025 Water Quality Report: total hardness 172–302 ppm (10–17.6 grains per gallon); hard water can scale pipes, water heaters, fixtures (site.json local_fact).
  https://www.phoenix.gov/content/dam/phoenix/waterservicessite/documents/wsdprimarywqr.pdf

## Landlord obligation (Arizona)
- ARS 33-1324(A)(4),(6): landlord shall "maintain in good and safe working order and condition all electrical, plumbing, sanitary, heating, ventilating, air-conditioning and other facilities and appliances" and "supply running water and reasonable amounts of hot water at all times."
  https://www.azleg.gov/ars/33/01324.htm
- ARS 33-1363 self-help for minor defects: if reasonable cost of compliance is less than **$300 or one-half of one month's rent, whichever is greater**, tenant may notify the landlord in writing; if the landlord fails to comply **within ten days** (or promptly in an emergency), the tenant may have the work done **by a licensed contractor** and deduct actual reasonable cost after giving the landlord an itemized statement and a waiver of lien.
  https://www.azleg.gov/ars/33/01363.htm
- ARS 33-1364: remedies where the landlord deliberately or negligently fails to supply running water — procure and deduct, damages for diminished rental value, or substitute housing.
  https://www.azleg.gov/ars/33/01364.htm

## Pools
- Arizona Water Facts: average evaporation rate in Phoenix and Tucson approximately **6 feet per year**; an average pool (16,000 gallons) evaporates its entire contents each year; meter the refill water — a sharp increase may indicate a leak.
  https://www.arizonawaterfacts.com/tips-resources/be-cool-your-pool
- Phoenix Water Smart conservation page lists leak checks at hose bib, pool auto-refill device, pool pump, outdoor water line.
  https://waterworks.phoenix.gov/water-conservation/

## Could not verify / wrote around
- No Phoenix "water leak credit," forgiveness, or high-bill adjustment program exists; the brief is wrong on this point. Only the sewer fee review, plus code 37-27 which assigns all downstream loss to the customer.
- No primary-source figure found for the share of Phoenix or Maricopa County homes on post-tensioned slabs, or for a build year after which they became standard. The city amendment's own words ("many structures have been, and continue to be, constructed with post-tensioned slabs on ground") are used instead of a percentage.
- No government source found quantifying under-slab copper failure rates or attributing them to flux residue or soil chemistry, so the copy describes mechanisms qualitatively and does not assign a cause or a rate.
- No City of Phoenix page found stating a specific spot-repair versus repipe permit threshold in plumbing terms; used the published residential permit rules (move or add fixtures) plus the $195 minimum fee and ARS 32-1121's permit trigger.
