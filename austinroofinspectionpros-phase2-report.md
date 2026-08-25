# austinroofinspectionpros.com — phase 2 complete

## Build
```
[PASS] austinroofinspectionpros.com -- home 1744 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           326 words  /about/
           555 words  /contact/
          1809 words  /
          1744 words  /pricing/
          1329 words  /roof-certification-inspection/
          1372 words  /roof-inspection/
          1268 words  /roof-leak-inspection/
           544 words  /services/
          1527 words  /storm-damage-roof-inspection/
```
exit 0. Files changed: `sites/austinroofinspectionpros.com/copy.md`, and `"phase": 1` → `2` in that site's `site.json` (nothing else in the JSON).

## Slugs written
roof-inspection, roof-leak-inspection, storm-damage-roof-inspection, roof-certification-inspection (exactly as in site.json; symptom teasers 1–4 map to them in that order).

## Differentiator delivered
Hail forensics + the inspection standard + the roofing-contractor regulation gap. No use of the insurance claim clock (chapter 542, 542A), IICRC S500, TDLR mold, Atlas 14, expansive-clay geology beyond the pre-existing pricing paragraph, Shoal/Onion Creek, or Travis County government framing. Carrollton's HO-145 cosmetic endorsement, percentage-deductible arithmetic and May 28 2024 bow echo were deliberately avoided; hail history uses Travis County queries and different NOAA URLs.

## Strongest verified local facts
1. Sept 24, 2023: NOAA/NCEI records three-inch hail on Burnet Lane in the Brentwood area of Austin, $300 million property damage on the Travis County entry, part of a complex tied to $1.3 billion in hail losses across Texas, Oklahoma and Missouri — https://www.ncei.noaa.gov/stormevents/eventdetails.jsp?id=1140580 ; county counts (19 days at 1.50 in.+ and 39 days at 1 in.+, 2010–2025) from https://www.ncei.noaa.gov/stormevents/listevents.jsp?eventType=%28C%29+Hail&beginDate_mm=01&beginDate_dd=01&beginDate_yyyy=2010&endDate_mm=12&endDate_dd=31&endDate_yyyy=2025&county=TRAVIS%3A453&hailfilter=1.50&tornfilter=0&windfilter=000&sort=DT&submitbutton=Search&statefips=48%2CTEXAS
2. Austin's adopted residential code fills in a 105 mph ultimate design wind speed with no ice-barrier requirement, while the shingle wind-classification table starts at 110 mph — https://up.codes/viewer/austin/irc-2021/chapter/3/building-planning and https://up.codes/viewer/austin/irc-2021/chapter/9/roof-assemblies (2021 IRC adoption effective Sept 1, 2021: https://publicinput.com/2021TechnicalCodeChanges)
3. Austin exempts shingle-for-shingle covering replacement, and roof decking up to 128 square feet, from a building permit — unless the property is in the Wildland-Urban Interface area and 50% or more of the roofing is replaced; exempt work must still comply with code — https://www.austintexas.gov/development-services/work-exempt-building-permits

Runner-up used on the pages: TREC 22 TAC 535.228(c)-(d) (https://www.trec.texas.gov/online-sops), FHA Handbook 4000.1 two-year remaining-roof-life rule (https://www.hud.gov/sites/dfiles/OCHCO/documents/4000.1hsgh.pdf), NWS Austin-area heat rankings — 1991–2020 average 29 days at or above 100°F vs 15 long-period, 2023 warmest year at 72.2°F (https://www.weather.gov/media/ewx/climate/ATTtemprankings.pdf), Hyde Park historic roof standards (https://services.austintexas.gov/edims/document.cfm?id=407691) and Mueller 6:12–9:12 roof-slope guidelines (https://www.austintexas.gov/sites/default/files/files/Redevelopment/Redevelopment_Projects/Mueller/Chapter_2_opt.pdf).

## Does Texas register roofing contractors
**No — not at the state level.** The Roofing Contractors Association of Texas states on its own licensing page that TDLR "does NOT currently administer licensure for roofing contractors," that anyone can call themselves a roofer, and that a roofer "is not required to be knowledgeable, insured, licensed, or registered with the state." The only credential is that association's voluntary license: principal of a Texas-domiciled roofing company for 2+ continuous years, fixed physical address, exams at 70%+, and $500,000 combined single limit GL for commercial or $300,000 residential — https://www.rcat.net/licensing.html. (The site describes it as "the state roofing trade association" rather than naming it, per the no-business-names rule.)

## Corrections to the brief
- The brief was right on both statutes. Verified: Ins. Code §4101.251(b) bars a roofing contractor from acting as an adjuster or advertising to adjust claims on property it may roof (https://codes.findlaw.com/tx/insurance-code/ins-sect-4101-251/); Ins. Code §707.002 requires the insured to pay the deductible and B&C §27.02 makes paying/waiving/absorbing/rebating it a Class B misdemeanor with a 12-point notice required at $1,000+ (https://texas.public.law/statutes/tex._ins._code_section_707.002, https://texas.public.law/statutes/tex._bus._and_com._code_section_27.02).
- Confirmed the brief's NWS Fort Worth 404 warning; used NCEI Storm Events via curl because the fetch tool is robots-blocked on ncdc/ncei list pages.
- One widely repeated claim I did **not** use because it is false for Texas: the "five days to cancel a roofing contract after a claim denial" rule is Kentucky/Georgia law, not Texas. Texas gives three business days on door-to-door sales over $25 (B&C ch. 601, https://www.texasattorneygeneral.gov/consumer-protection/home-real-estate-and-travel/door-door-sales-3-day-right-rescission).
- HB 3344 (89R) would create a state roofing license effective Sept 1, 2026, but the capitol bill-history page is robots-blocked, so passage could not be verified and the bill is **not** mentioned on the site.
- site.json vs brief: no conflicts. site.json local_fact 1 (TDI 15-business-day claim deadlines) was deliberately left unused on the new pages because the water-damage sibling owns the claim clock.
- Could not verify and wrote around: whether specific neighborhoods fall inside the Wildland-Urban Interface area, Bouldin Creek/East Cesar Chavez build eras, and any Austin-specific ice-and-water or underlayment amendment beyond the state guidance (Austin's Table R301.2 says no ice barrier required).

## Full research notes
`/home/user/workspace/local-sites/austinroofinspectionpros-phase2-research.md`
