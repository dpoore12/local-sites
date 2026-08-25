# santabarbaracaraccidentlawyer.com — phase 2 complete

Build: `python3 template/build.py --check-only santabarbaracaraccidentlawyer.com` → **[PASS]**, exit 0
Label: `home 1743 words, 4 symptoms, 3 local Q&As, 3 sourced facts`

## Page word counts (visible, rendered)
| Page | Words |
|---|---|
| / | 1817 |
| /pricing/ | 1743 |
| /services/ | 597 |
| /about/ | 380 |
| /contact/ | 588 |
| /rear-end-collision-lawyer/ | 1490 |
| /uninsured-driver-claim-lawyer/ | 1539 |
| /commercial-truck-collision-lawyer/ | 1438 |
| /injury-claim-negotiation/ | 1450 |

## Service slugs
1. rear-end-collision-lawyer — Rear-End Collision Claims
2. uninsured-driver-claim-lawyer — Uninsured Driver Claims
3. commercial-truck-collision-lawyer — Commercial Truck Collisions
4. injury-claim-negotiation — Injury Claim Negotiation

## Strongest verified local facts (fetched this session)
1. Santa Barbara 2026 Safety Analysis (SBPD data 2020–2024): 2,196 reported injury collisions — 14 fatal, 178 severe, 1,035 other visible injury, 970 complaint of pain; 62% at intersections; Tier 1 segments = 5% of street length but 45% of severe/fatal injury collisions. https://santabarbaraca.gov/sites/default/files/2026-07/04_Safety_Analysis_07-2026.pdf
2. OTS 2023 rankings: city of Santa Barbara 1st of 103 similar cities for bicyclist victims killed and injured (131) and 12th for hit-and-run (47 collisions); Santa Barbara County 2nd of 58 for bicyclists (252) and 9th for hit-and-run (197). https://www.ots.ca.gov/rankings/santa-barbara-2023/ and https://www.ots.ca.gov/rankings/santa-barbara-county-2023/
3. SBCAG 2022 US 101 Comprehensive Multimodal Corridor Plan: ~94,000 AADT rising to a forecast 140,000 by 2040; 3,500–4,500 trucks/day (5.4% of traffic) moving ~15M tons/yr; PM 9.2–12.3 is the only Central Coast freeway segment designated a Critical Urban Freight Corridor and US 101 the only Central Coast STAA National Network highway. https://www.sbcag.org/wp-content/uploads/2023/09/2022-U.S.-101-Comprehensive-Multimodal-Corridor-Plan-.pdf

Also cited in copy: CCP 335.1 (2-year), Gov Code 911.2 (6-month claim) / 945.6, Li v. Yellow Cab (pure comparative fault), CDI 30/60/15 effective as policies renew from Jan 1 2025 plus CLCA 10/20/3, Insurance Code 11580.2 (24-hour unknown-driver report, 30-day sworn statement, consent-to-settle, underinsured definition, 2-year trigger), Civil Code 3333.4 with its (c) exception, Civil Code 3040 and 3045.4 lien caps, VC 20008, VC 34501.12 (BIT terminal records), CHP crash report request, Caltrans SR-154/Foxen Canyon $10,820,300 project, Caltrans District 5 (302 centerline miles in the county), UCSB ~14,000 daily bike commuters, Rule of Professional Conduct 1.5.

## Collision avoidance
Zero 15-word runs with any of the other 82 sites (checker clean). Rewrote all statutory paraphrases that had collided with modestocaraccidentlawyerpros.com (underinsured definition, unknown-driver reporting, 2-year trigger, lease/decal sentence, damages-in-order sentence) and swapped two citation URLs that collided with oceansidepersonalinjurylawyerpros.com (State Bar rules PDF path, Gov Code 911.2 now via findlaw).

Files changed: `sites/santabarbaracaraccidentlawyer.com/copy.md`, and `"phase": 1` → `"phase": 2` in that site's `site.json`. Staging draft left at `_sb_phase2_blocks.md`.
