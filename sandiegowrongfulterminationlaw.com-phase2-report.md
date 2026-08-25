# Phase 2 complete — sandiegowrongfulterminationlaw.com

## PASS line
```
[PASS] sandiegowrongfulterminationlaw.com -- home 1747 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           407 words  /about/
           578 words  /contact/
          1906 words  /
          1747 words  /pricing/
          1408 words  /retaliation-claim-lawyer/
           599 words  /services/
          1408 words  /severance-agreement-review/
          1348 words  /workplace-discrimination-lawyer/
          1486 words  /wrongful-termination-lawyer/
EXIT:0
```
`"phase": 2` set in site.json (that field only). Only `copy.md` + that field were edited.

## Authored block word counts
symptom_1 62, symptom_2 59, symptom_3 58, symptom_4 58 (all 40-80).
services_summary 103 (95-115). crosslink_head shortened to 5 words ("Facing a different workplace problem?").
Ledes: wrongful termination 41, retaliation 41, discrimination 35, severance 38 (all 30-45).
Bodies: wrongful termination ~894, retaliation ~827, discrimination ~774, severance ~832 (700-900), 7 `###` sections each.
pricing_body trimmed by ~72 words of prose to clear the 1750 ceiling. No dollar figure, fee, statute cite, or URL was removed — $435, $60, $500, $150, $30, $1,000, 25/33 percent all intact.

## Three strongest verified local facts
1. City of San Diego minimum wage is $17.75 per hour effective January 1, 2026 (from $17.25), and the Earned Sick Leave and Minimum Wage Ordinance, SDMC ch. 3, art. 9, div. 1, took effect July 11, 2016, accruing one hour per 30 hours worked with an 80-hour accrual cap and a 40-hour front-load alternative — https://www.sandiego.gov/labor-and-wage/minimum-wage/earned-sick-leave (coverage at two hours of work in a week inside city boundaries: https://www.sandiego.gov/sites/default/files/2025-01/mwo-notice-english.pdf)
2. Local rule 1.2.2(E) folds the East and South divisions into the Central Division for civil limited and unlimited filings at 330 West Broadway, Room 225 — https://www.sdcourt.ca.gov/sdcourt/civil2/civilwheretofile
3. CRD requires an employment intake form within three years of the date last harmed, and a right-to-sue notice then allows one year to file suit (Gov. Code 12965(c)(1)(C)) — https://calcivilrights.ca.gov/complaintprocess/ and https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=12965.&lawCode=GOV

## Brief items worth flagging
- Agency name verified as requested: DFEH became the Civil Rights Department effective July 1, 2022 under SB 189 (https://calcivilrights.ca.gov/deptnamechange/). AB 9 (2019) is correctly credited with the one-year to three-year extension (https://www.gov.ca.gov/2019/10/10/governor-newsom-signs-worker-protection-bills-addressing-sexual-harassment-wages-and-health-protections/).
- Tension inside the brief: section on pricing says the pricing page is "the only page with numbers and you are not writing it," while the task instruction says to expect the pricing page over its ceiling and to trim `pricing_body`. `pricing_body` already existed from phase 1; I trimmed prose only. Service pages do carry market-cost numbers (statutory penalties, court fees), which the brief's own reference site does too.
- site.json vs brief: no conflicts found. site.json slugs, neighborhoods, and the three local facts were used exactly as given; symptom titles 1 and 3 were re-pointed so each teaser matches its mapped service slug (site.json `symptom_service` order governs).
- Written around, not asserted: the 65-day LWDA PAGA review window (only found in secondary sources). Two `leginfo` single-section fetches (Gov. Code 12964.5, Civil Code 1542) were blocked by robots, so those two are cited to Justia's statute text pages instead.
- Two long sentences remain in the pre-existing `pricing_body` (48 and 49 words) because both are close statutory paraphrases and splitting them would push the page back over 1750. All authored phase-2 sentences are under 45 words.

Research notes with every fetched URL: `sandiegowrongfulterminationlaw.com-phase2-research.md`.
Edit script used: `_sd_employment_phase2.py`. Pre-edit backup of copy.md: `/tmp/copy.bak.md`.
