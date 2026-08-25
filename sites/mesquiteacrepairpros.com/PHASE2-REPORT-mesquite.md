# Phase 2 report — mesquiteacrepairpros.com

## Build result

```
[PASS] mesquiteacrepairpros.com -- home 1742 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           359 words  /about/
          1533 words  /ac-compressor-repair/
          1386 words  /ac-refrigerant-leak-repair/
          1318 words  /ac-tune-up/
          1527 words  /air-conditioner-repair/
           603 words  /contact/
          1997 words  /
          1742 words  /pricing/
           560 words  /services/
```
`python3 template/build.py --check-only mesquiteacrepairpros.com` → exit 0.
`site.json` `"phase"` flipped 1 → 2. Only `copy.md` and that one field were edited.

Slugs used exactly as in site.json: `air-conditioner-repair`, `ac-compressor-repair`, `ac-refrigerant-leak-repair`, `ac-tune-up`.

## Collision status

Independent 15-word shingle check against all six named siblings (allen, modesto, sacramento, denver furnace, tampa tile roof, arlington bathroom): **zero shared runs**. Three Allen collisions found on the first check (compressor symptom list, Schrader-core leak-order line, condenser-cleaning homeowner-limits line) were rewritten with different wording and sentence shape.

## Spine: the refrigerant transition

Built the site on the AIM Act Technology Transitions rule, differentiated from Allen/Modesto by citing the regulation itself rather than the headline: 40 CFR 84.54(c)(1) 700-GWP limit, the May 26, 2026 final rule at 91 FR 31284 (FR Doc 2026-10387, docket EPA-HQ-OAR-2025-0005, effective July 27, 2026), the "For servicing existing equipment only" component label, condenser-then-coil replacement sequencing, the 50-lb leak-repair threshold that does *not* reach house systems, Section 608 certification and the venting prohibition, and Mesquite Ordinance 5246's A2L provisions.

## 3 strongest verified local facts

1. **Mesquite Ordinance 5246** — passed May 18, 2026, effective July 1, 2026, adopts the 2024 International Mechanical Code and amends IMC 306.3 attic-appliance access (30 in high × 22 in wide passageway, ≤20 ft, 24-in continuous flooring, 30 × 30 service space, pull-down stair rated ≥300 lb) plus IMC 1104.3.1.1 for Group A2L refrigerants referencing ASHRAE 15 §7.6, with new §202 definitions of "refrigerant detection system" citing UL 60335-2-40 and ASHRAE 15-2022: https://apps.cityofmesquite.com/city_secweb/ordinances/5246.pdf
2. **NWS Fort Worth 100-degree data for DFW** — 23 triple-digit days in 2024 (peak 107°F on Aug 19), 55 in 2023, 7 in 2025, 71 in 2011; first 100° reading Jul 7 in 2026 and Jun 23 in 2024: https://www.weather.gov/fwd/d100data
3. **TDLR air conditioning contractor licensing** — Class A (any size) vs Class B (≤25 tons / 1.5M BTU/hr), environmental air conditioning endorsement, TACL license number format, $115 application fee, and the requirement to hold a contractor license before offering or performing work: https://www.tdlr.texas.gov/acr/contractor-apply.htm and https://www.tdlr.texas.gov/acr/acrfaq.htm

Full fact list with URLs: `RESEARCH-NOTES-mesquite-phase2.md` in this folder.

## Things in the brief that were wrong or unusable

1. **"The refrigerant transition is not the spine of any other portfolio site" — not accurate.** Allen already cites the 700-GWP limit and R-454B (GWP 470); Modesto cites the 700 ceiling, R-454B, *and* the May 2026 rule. The differentiator had to be rebuilt around a deeper, differently-cited layer of the same rule (CFR/FR citations, component labeling, condenser-vs-system sequencing, the 50-lb threshold) plus Mesquite's own A2L code adoption.
2. **site.json's "36 percent built before 1970" conflicts with its own source.** The city plan's 2023 table works out to roughly 21% pre-1970. Per instructions site.json wins, so the figure was not contradicted — the copy was written around it using decade unit counts (1980s: 17,076 units ≈ 30.9%; 1970s: 8,158) instead of restating the percentage.
3. **`mesquite.onlinegovt.com` is Mesquite, Nevada** — excluded from research entirely.
4. **Mesquite's online fee-schedule page does not publish mechanical permit dollar amounts.** The flat $65 residential mechanical permit fee is sourced from the code of ordinances permit-fee sections (12-102 / 12-104, ordinance 5136) and appears only on the pricing page.
5. **Texas landlord cooling obligation: there is effectively none to cite as a duty.** The State Law Library is explicit that "there is no state law that specifically gives tenants the right to be provided with climate control measures"; the copy handles it through §92.052 / §92.056 / §92.0561(d)(3) repair-duty framing instead of claiming an AC requirement. https://www.sll.texas.gov/faqs/tenants-rights-ac-heating/

## QC self-check performed after PASS

No sentence over 44 words; no headings ≥85 chars or ending in a period; no doubled words; no banned phrases (`licensed and insured`, `since 19/20`, `free consultation`, `map pack`, `SERP`); no British spellings (build guard); no dollar figures outside the pricing page; no first-person pricing; no links in body copy. Pricing page trimmed from 1798 to 1742 visible words by cutting prose only — every dollar figure and fee (service-call fee, after-hours premium, $65 permits, $500 repair example, $2,000–$3,400 Oncor incentive, $300,000/$600,000 insurance minimums, per-pound refrigerant comparison) is intact.
