# Carrollton phase 2 — completion report

## Build result

```
[PASS] carrolltongaragedoorrepairexperts.com -- home 1738 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           376 words  /about/
           611 words  /contact/
          1367 words  /garage-door-opener-repair/
          1543 words  /garage-door-replacement/
          1336 words  /garage-door-spring-repair/
          1836 words  /
          1385 words  /off-track-garage-door-repair/
          1738 words  /pricing/
           582 words  /services/
```
exit code 0. Zero shared 15-word runs with all eight named siblings (verified with an independent normalized 15-gram diff, not just the build check).

Files touched: only `sites/carrolltongaragedoorrepairexperts.com/copy.md` and the `"phase"` field in that site's `site.json` (1 → 2).

## Differentiator as built

The site's spine is hail and the insurance claim.

- `/garage-door-replacement/` carries the claim argument end to end: cosmetic vs non-functional findings, the scope of the state's prescribed cosmetic exclusion (HO-145 = roof coverings only), percentage-deductible arithmetic, Chapter 542 carrier deadlines and the 18% penalty, Chapter 1813 appraisal (effective Sept 1 2025), why a single section usually cannot be matched (component-substitution guidance), and the same-size-no-permit rule plus the 2024 code adoption.
- `/off-track-garage-door-repair/` carries the physical-damage half: Blackland Prairie/Houston Black shrink-swell racking jambs, the May 28 2024 bow echo, and the inspection-sheet distinction between a dent and a door that cannot operate.
- `/garage-door-spring-repair/` deliberately closes the claim door: a spring at cycle limit is wear and tear, never a storm claim.
- `/garage-door-opener-repair/` covers 16 CFR 1211 entrapment protection (1211.6(a), 1211.6(b), 1211.7(a)(1), 1211.7(f)(1), 1211.7(g)(1)), plus the single-trade electrical permit and city contractor registration.

## 3 strongest verified local facts (with URLs)

1. **May 28, 2024 bow echo over Carrollton** — NOAA Storm Events event 1186827 logs a 65 kt gust at 2.66 W Hebron (Denton County) at 05:00 on 2024-05-28 with the narrative "Intense thunderstorm winds caused tree damage across Carrollton"; the episode narrative records NWS storm surveys finding straight-line winds of 80–95 mph. [NOAA Storm Events event 1186827](https://www.ncei.noaa.gov/stormevents/eventdetails.jsp?id=1186827)
2. **Carrollton's adopted code edition** — the city adopted the 2024 I-Codes and the 2023 NEC by Ordinances 4265 and 4290, effective 09/01/2025 (previous cycle: 2021 I-Codes, Ord. 4044). [City of Carrollton codes and ordinances](https://www.cityofcarrollton.com/departments/departments-a-f/building-inspection/codes-ordinances)
3. **The Texas cosmetic-damage exclusion is roof-coverings-only** — TDI Commissioner's Bulletin B-0030-98 approved Endorsement HO-145, "Exclusion of Cosmetic Damage to Roof Coverings Caused by Hail" (and TDP-022 for dwelling forms), effective May 2, 1998, attachable only where the policy gets an impact-resistant roof credit and void unless signed by the insured. There is no TDI-prescribed cosmetic exclusion for a garage door. [TDI Bulletin B-0030-98](https://www.tdi.texas.gov/bulletins/1998/b-0030-8.html)

Supporting sources also used: [TDI deductibles page](https://www.tdi.texas.gov/tips/deductibles.html) (5% of $150,000 = $7,500; $6,500 loss pays $0 vs $6,000 at a $500 deductible), [Insurance Code ch. 542](https://statutes.capitol.texas.gov/Docs/IN/pdf/IN.542.pdf), [Insurance Code ch. 1813](https://statutes.capitol.texas.gov/Docs/IN/htm/IN.1813.htm), [Texas DPS gate operators/garage door openers](https://www.dps.texas.gov/section/private-security/gate-operatorsgarage-door-openers), [Carrollton contractor registration](https://www.cityofcarrollton.com/departments/departments-a-f/building-inspection/my-development/permit-processing-issuance/contractor-registration), [NRCS Houston Black series](https://soilseries.sc.egov.usda.gov/OSD_Docs/H/HOUSTON_BLACK.html), [ANSI/DASMA 102-2004](https://law.resource.org/pub/us/cfr/regulations.gov.docket.15/dasma.102.2004.html), DASMA TDS 174/175/183/190, and 16 CFR part 1211 on govinfo. Full source log: `carrollton-phase2-research.md`.

## Things in the task brief that were wrong or needed correction

1. **Counties.** The brief said Carrollton spans Dallas, Denton and Collin counties. `site.json` lists only `["Dallas","Denton"]`, and per the brief's precedence rule site.json wins, so the copy references Dallas and Denton only. (The city's own footprint does touch Collin County, but I did not override the authority file.)
2. **Pricing page ceiling.** The brief predicted the pricing page would blow its 1750-word ceiling. It did not: pricing came in at 1738 words after phase-2 nav growth. I still trimmed pricing prose lightly for flow and kept every dollar figure intact ($125 remodel permit, $125 nonrefundable application processing fee, $4 per $1,000 single-trade, $75 minimum, $50 reinspection, $50 miscellaneous construction). The page that actually broke a ceiling was `/garage-door-replacement/` (1694 → 1543 against a 1550 cap).
3. **NWS Fort Worth hail event pages.** The brief pointed at NWS Fort Worth as a primary source for the big documented hail events. The relevant event pages (e.g. `weather.gov/fwd/june132012hail`, `/apr112016hail`) 404, so documented event data came from NOAA Storm Events records instead (e.g. the June 13, 2012 Dallas County event with 2.50 in hail at South Irving and "over a billion dollars in hail damage": https://www.ncei.noaa.gov/stormevents/eventdetails.jsp?id=386503).
4. **"TDI position on cosmetic damage exclusions."** What TDI actually publishes is narrower than the brief implies: the prescribed exclusion is for *roof coverings* only. Any garage-door cosmetic exclusion is a carrier's own endorsement. The copy says exactly that rather than implying a statewide garage-door exclusion.
5. **"Texas has no state contractor license for this trade" — verified, with a caveat.** DPS states no license is required from it to install residential garage door openers *unless* the operator is connected to an alarm system or records entry/exit. Separately, electrical work does require a state license, and Carrollton requires free annual contractor registration before permits or inspections. Both nuances are in the copy.
