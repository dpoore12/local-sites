# Phase 2 conversion report — austinwrongfuldeathlawyerpros.com

## Build result

```
[PASS] austinwrongfuldeathlawyerpros.com -- home 1743 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           343 words  /about/
           588 words  /contact/
          1308 words  /fatal-car-accident-claim/
          1230 words  /fatal-work-accident-claim/
          1866 words  /
          1215 words  /medical-negligence-death-claim/
          1743 words  /pricing/
           582 words  /services/
          1326 words  /wrongful-death-damages-claim/
```
Exit code 0. `"phase": 2` set in site.json (only that field changed).

## Differentiator as built
Who may sue (71.004 list, siblings/grandparents/grandchildren excluded), the three-calendar-month executor duty (71.004(c)), the survival claim and the estate/probate step (71.021, 16.062), and the public-entity wall (Austin's 45-day charter notice, 101.023 caps, 101.106 election, 101.056 discretionary function). Structure differs from Dallas: road-ownership framing on the vehicle page, Labor Code 408.182 beneficiary mismatch on the work page, medical examiner records + Central Health hospital-district trap on the medical page, and 71.010 share-splitting + per-defendant cap arithmetic on the damages page. All authority citations use Justia, FindLaw, txcourts.gov, austintexas.gov, traviscountytx.gov, tdi.texas.gov paths not used by the listed sites.

## Does Austin's charter shorten the notice period? YES — 45 days
Austin City Charter art. XII, §3 requires written notice, verified by affidavit, to the city council or city manager within forty-five (45) days, stating when/where/how, the apparent extent of injury, the damages claimed, the claimant's residence and the witnesses relied on; failure "shall exonerate, excuse and exempt the city from any liability whatsoever."
https://services.austintexas.gov/edims/document.cfm?id=292113 — confirmed by the city's claims page: https://www.austintexas.gov/services/file-claim
CPRC 101.101(b) expressly ratifies charter notice provisions, so the statutory six months is displaced.

## Three strongest verified local facts
1. Roughly 65%–75% of Austin traffic fatalities occur on state-owned roads; Austin recorded 99 traffic deaths in 2025 (+2% vs 2024) and 301 serious injuries (−28%). https://www.austintexas.gov/transportation-public-works/mobility-matters/severe-crashes-show-downward-trend-2025 (supported by the Vision Zero project-performance PDF showing city-road fatalities flat while state/other-agency road fatalities rose: https://www.austintexas.gov/sites/default/files/files/TPW/VisionZero/VZ-Analytics-Austin-Safety-Project-Performance-10.02.25.pdf)
2. The Travis County Medical Examiner's CCP art. 49.25 jurisdiction includes deaths occurring less than 24 hours after hospital admission, exams generally take 12–24 hours, and the autopsy report is public under the PIA (https://www.traviscountytx.gov/medical-examiner/faq); fee schedule effective Jan 1, 2025: $25 autopsy report, $5 investigation report, $50 certification, $30 per disc, legal next of kin exempt (https://www.traviscountytx.gov/medical-examiner/fee-schedule).
3. Central Health is Travis County's taxpayer-funded hospital district, created by voters in 2004 — i.e., a governmental unit, which drops a care-related claim into 101.101 notice and 101.023's $100k/$300k local-unit caps. https://www.centralhealth.net/about/
(Runner-up: TxDOT counted 139 fatal crashes and 155 traffic deaths in Travis County in 2024 — https://www.txdot.gov/content/dam/docs/division/trf/crash-records/2024/13.pdf)

## Where the brief was wrong
The brief asked about "the constitutional provision said to exempt a wrongful death exemplary award from the statutory cap." That exemption is **not established Texas law**, and the site says so plainly rather than asserting it:
- Tex. Health Enterprises v. Geisler declined to hold the cap unconstitutional and noted another court had approved applying the cap in wrongful death actions: https://caselaw.findlaw.com/court/tx-court-of-appeals/1092508.html
- In the 2005 Diamond Shamrock gross-negligence death case the Supreme Court of Texas resolved the appeal on the evidence and did not disturb the court of appeals' holding that CPRC 41.008 applied and was not unconstitutional as applied: https://law.justia.com/cases/texas/supreme-court/2005/2000547.html
- A Supreme Court of Texas opinion delivered May 22, 2026 (No. 24-0045) computes the 41.008(b) cap defendant-by-defendant, using each defendant's share of economic damages: https://www.txcourts.gov/media/1462759/240045.pdf

Other brief notes:
- As predicted, `statutes.capitol.texas.gov` was unusable; all statutes are cited to Justia.
- The Justia path for CPRC 16.003 returned 404, so the two-year period is stated without a citation on the damages page (16.001 and 16.062 are cited).
- The verified TxDOT crash-report fees ($6/$8) were dropped because the source URL collides with Dallas.
- site.json and the brief did not conflict; site.json slugs, city/state, counties and neighborhoods were followed exactly.

## Files
- Edited: `sites/austinwrongfuldeathlawyerpros.com/copy.md`, `sites/austinwrongfuldeathlawyerpros.com/site.json` (phase only)
- Research notes: `research-notes-austin-wrongful-death.md`
- Scratch draft of inserted blocks: `new_blocks.md`
