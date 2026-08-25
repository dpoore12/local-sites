# Phase 2 conversion report — harrisburgcaraccidentlawyerpros.com

## Build result

```
[PASS] harrisburgcaraccidentlawyerpros.com -- home 1554 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           361 words  /about/
          1390 words  /commercial-truck-collision-lawyer/
           564 words  /contact/
          1808 words  /
          1350 words  /injury-claim-negotiation/
          1554 words  /pricing/
          1405 words  /rear-end-collision-lawyer/
           565 words  /services/
          1357 words  /uninsured-driver-claim-lawyer/
```
`python3 template/build.py --check-only harrisburgcaraccidentlawyerpros.com` → exit 0.

Files changed: `sites/harrisburgcaraccidentlawyerpros.com/copy.md` and the single `"phase": 1` → `"phase": 2` field in that site's `site.json`. Nothing else touched.

## Block word counts (authored)

| Block | Words | Target |
|---|---|---|
| services_summary | 106 | 95–115 |
| services_pick_head | 10 | 6–10 |
| crosslink_head | 5 | 4–7 |
| symptom_1 / 2 / 3 / 4 bodies | 58 / 57 / 49 / 54 | 40–80 |
| svc_rear_end_collision_lawyer_lede / _body | 40 / ~760 | 30–45 / 700–900 |
| svc_uninsured_driver_claim_lawyer_lede / _body | 38 / ~750 | 30–45 / 700–900 |
| svc_commercial_truck_collision_lawyer_lede / _body | 42 / ~780 | 30–45 / 700–900 |
| svc_injury_claim_negotiation_lede / _body | 44 / ~740 | 30–45 / 700–900 |

Every service body carries 7 `###` subheads. Pricing came in at **1554 words, under the 1750 ceiling** — no trimming was needed, so no dollar figure or fee was removed.

## Differentiator

Built on Pennsylvania's limited tort vs. full tort election as the spine: the standardized 1705 notice, the election carrying forward through every renewal until a signed form changes it, the 1702 "serious injury" definition, the 1705(d) exceptions that restore full tort (DUI conviction or ARD, out-of-state registered vehicle, intentional injury, defendant without financial responsibility, occupant of a non-private-passenger vehicle), the 1711 $5,000 medical benefit and the 1722 subtraction, 1731/1738 UM/UIM rejection and stacking waiver forms, the 7102(a) 51% bar, the 5524 two-year limit, Dauphin County's $50,000 compulsory arbitration board, and 31 Pa. Code Ch. 146 claim-handling deadlines.

## Three strongest verified local facts

1. **Dauphin County crash volume.** PennDOT's county crash workbook records **2,914 total crashes in Dauphin County in 2024**, including 1,112 intersection crashes (427 at signalized intersections), 239 heavy truck crashes, 259 commercial vehicle crashes, and 132 winter-condition crashes — [PennDOT county crash statistics workbook](https://www.pa.gov/content/dam/copapwp-pagov/en/penndot/documents/travelinpa/safety/documents/crash_statistics.xlsx). Matches site.json's stated fact.
2. **The I-83 Capital Beltway is a corridor, not a single interchange.** PennDOT's master plan covers roughly **11 miles from the New Cumberland Interchange (Exit 40B) to the I-81 junction (Exit 51)**, through the Paxton Street, Eisenhower and Derry Street interchanges, in four project sections (three in Dauphin County), with minimum operating requirements of interstate standards, 60 mph mainline design speed and three through lanes each direction — [PennDOT I-83 Capital Beltway Master Plan](https://www.pa.gov/agencies/penndot/projects-near-you/district-8-projects/i-83-capital-beltway-master-plan).
3. **Compulsory arbitration threshold in this county.** Dauphin County's local rules send **every action at issue where the amount in controversy is $50,000 or less** (except title to real estate) to a Board of Arbitration, with no stipulating around it; the Bar Association supplies 30 names, arbitrators serve two years, and one three-attorney panel sits one week a month — [Dauphin County local rules FAQ](https://www.dauphincounty.gov/docs/default-source/local-rules-of-court/frequently-asked-questions-(local-rules)-9-22-(002).pdf?sfvrsn=b195d317_1).

Runner-up: NWS State College puts Harrisburg's seasonal snowfall normal at **32.8 inches** across winters 1949–50 through 2014–15, with 1960–61 peaking at 81.3 inches — [NWS State College snowfall analysis](https://www.weather.gov/media/ctp/Spotter%20Newsletters/ONI%20vs_%20Seasonal%20Snowfall%20at%20Harrisburg,%20PA.pdf).

## Primary sources fetched and used

- 75 Pa.C.S. 1705 (tort election) — https://www.legis.state.pa.us/WU01/LI/LI/CT/HTM/75/00.017.005.000..HTM
- 75 Pa.C.S. 1702 (serious injury; $15,000/$30,000/$5,000) — https://www.legis.state.pa.us/WU01/LI/LI/CT/HTM/75/00.017.002.000..HTM
- 75 Pa.C.S. 1711 ($5,000 medical benefit) — https://www.legis.state.pa.us/WU01/LI/LI/CT/HTM/75/00.017.011.000..HTM
- 75 Pa.C.S. 1722 (preclusion of first-party amounts) — https://www.legis.state.pa.us/WU01/LI/LI/CT/HTM/75/00.017.022.000..HTM
- 75 Pa.C.S. 1731 (UM/UIM offer and rejection form) — https://www.legis.state.pa.us/WU01/LI/LI/CT/HTM/75/00.017.031.000..HTM
- 75 Pa.C.S. 1738 (stacking and waiver) — https://www.legis.state.pa.us/WU01/LI/LI/CT/HTM/75/00.017.038.000..HTM
- 42 Pa.C.S. 5524 (two years) — https://www.legis.state.pa.us/WU01/LI/LI/CT/HTM/42/00.055.024.000..HTM
- 42 Pa.C.S. 7102(a) (modified comparative negligence) — https://www.legis.state.pa.us/WU01/LI/LI/CT/HTM/42/00.071.002.000..HTM
- 31 Pa. Code Ch. 146 (unfair claim settlement practices) — https://www.pacodeandbulletin.gov/secure/pacode/data/031/chapter146/031_0146.pdf
- Pa. R.P.C. 1.5 (fees) — https://www.padisciplinaryboard.org/for-attorneys/rules/rule/3/the-rules-of-professional-conduct
- PennDOT 2024 Crash Facts & Statistics — https://www.pa.gov/content/dam/copapwp-pagov/en/penndot/documents/travelinpa/safety/documents/2024_cfb_linked.pdf
- PA State Police crash report request ($22, 15 days) — https://www.pa.gov/services/psp/request-a-copy-of-a-vehicle-crash-report
- PennDOT AA-600 driver crash report (five days, 75 Pa.C.S. 3747(a)) — https://www.pa.gov/content/dam/copapwp-pagov/en/penndot/documents/public/pubsforms/forms/aa-600.pdf
- 49 CFR 395.8(k)(1) / 395.11 (six-month retention, supporting documents) — https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-395/section-395.8
- Dauphin County local rules index — https://www.dauphincounty.gov/government/courts/local-rules-of-court

## Things in the brief that were wrong or imprecise

1. **"The Capital Beltway interchange."** PennDOT does not describe it as an interchange. It is an ~11-mile I-83 corridor containing several interchanges (New Cumberland, Paxton Street, Eisenhower, Derry Street, I-81). Copy reflects PennDOT's framing.
2. **"Expect the pricing page over its 1750 ceiling."** It was not. The pricing page renders at 1554 words, comfortably inside 900–1750, so no prose was trimmed.
3. **"PA's compulsory arbitration threshold"** as a single statewide number: 42 Pa.C.S. 7361 sets a $50,000 statutory maximum but the operative threshold is set by local rule. I could not fetch 7361's text (the legis host repeatedly timed out), so the $50,000 figure is sourced to Dauphin County's own local-rules FAQ instead, and the copy attributes it to local rules rather than to a statewide statute.
4. **"PA minimum liability limits"** — these live in the 1702 definition of "financial responsibility" ($15,000/$30,000/$5,000), not in a separately titled minimum-limits section.
5. **site.json vs. newer data.** site.json's "2,914 total crashes in Dauphin County in 2024" is correct in the current PennDOT workbook. That workbook now also carries a 2025 column (Dauphin: 2,888). Per instruction, site.json governs and 2024 was used throughout.

## Collision avoidance

An independent 15-word normalized-run comparison against every other `sites/*/copy.md` now returns **zero shared runs**. The first check flagged 24 runs across birminghamtruckaccidentlawyerpros, concordcaraccidentlawyerpros, modestocaraccidentlawyerpros, santabarbaracaraccidentlawyer and victorvillecaraccidentlawyerpros — clustered around the 49 CFR 395.11 document list, the Rule 1.5(a) sentence, a chain-reaction "middle link" sentence, an underinsured-limit sentence, and one `###` heading. All five were rewritten rather than deleted, and the build's own duplicate guard passes.

## QC notes

No banned phrase appears anywhere in `copy.md`. No sentence exceeds 44 words (two pre-existing over-length sentences in `pricing_lede` and `pricing_body` were split). No heading reaches 90 characters, no single-sentence heading ends with a period, no repeated heading text on a page, no bare decimals, no doubled words, no three consecutive paragraphs opening on the same word. One accuracy fix during proofing: rear-end was described as the "second most common" collision type statewide; PennDOT's 2024 table puts Angle (32,969) and Hit Fixed Object (31,543) above Rear End (20,825), so the ranking claim was removed and only the raw counts kept.

Staging file left in place at `/home/user/workspace/local-sites/_harrisburg_phase2_blocks.md`.
