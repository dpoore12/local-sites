# Phase-2 conversion report — virginiabeachpersonalinjurylawyerpros.com

## Build result

```
[PASS] virginiabeachpersonalinjurylawyerpros.com -- home 1732 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           378 words  /about/
          1472 words  /catastrophic-injury-lawyer/
           547 words  /contact/
          1936 words  /
          1460 words  /medical-malpractice-lawyer/
          1732 words  /pricing/
          1459 words  /product-liability-lawyer/
           583 words  /services/
          1533 words  /slip-and-fall-lawyer/
EXIT 0
```

`site.json` `"phase"` flipped 1 -> 2 (only field changed). Only this site's `copy.md` and `site.json` were edited.

Service slugs used exactly as in site.json: `slip-and-fall-lawyer`, `medical-malpractice-lawyer`, `product-liability-lawyer`, `catastrophic-injury-lawyer`.

## Fixes made during the check loop
- Pricing page opened at 1751 (1 over the 1750 ceiling): trimmed prose only, no dollar figure or fee removed. Final 1732.
- 3 fifteen-word runs collided with `birminghamtruckaccidentlawyerpros.com` (Rule 1.5(c) contingent-fee paperwork language). All four fee passages were rewritten in distinct phrasing; run collisions cleared.
- QC section 12 sweep with a custom checker: 11 sentences over 44 words split (contact essentials list, Rule 1.5 eight-factor list, Rule 1.5(c) paperwork sentence, cost-driver list, 8.01-581.15 cap sentence, 8.01-20.1 certification sentence, Logan v. Montgomery Ward holding, resort-equipment list, three fee paragraphs). No long headings, no heading-ending periods, no back-to-back headings, no repeated headings, no bare decimals, no doubled words, no 3-in-a-row identical paragraph openers, no runs of 5+ single-sentence paragraphs. "Virginia" 0.43% and "Beach" 0.30% of the document.

## Three strongest verified local facts
1. Virginia Beach's own notice-of-claim procedure: written notice within 6 months to the City Attorney (Mark D. Stiles, 2401 Courthouse Drive), then forwarded to Risk Management — https://attorney.virginiabeach.gov/file-a-notice-of-claim
2. Virginia Beach Circuit Court civil practice: stated goal of concluding a civil case within 18 months of filing, civil cover sheet with the first pleading, praecipe to obtain a trial date — https://courts.virginiabeach.gov/circuit-court-clerks-office/circuit-court-civil ; General District Court $50,000 personal-injury / wrongful-death limit — https://courts.virginiabeach.gov/general-district-court/civil-division
3. Resort-area exposure quantified: 14.3 million visitors in 2024, $2.6B visitor spending, $3.9B total impact, 34,076 jobs (19% of city jobs), 58.8% day visitors — https://virginiabeach.gov/connect/news/tourism-continues-to-fuel-economic-growth-in-virginia-beach-with-3-9b-total-impact-in-2024 ; Oceanfront Resort District three-mile boardwalk and 40+ beachfront hotels — https://planning.virginiabeach.gov/zoning/form-based-code/oceanfront-resort-district

## Differentiator doctrine, all verified
- Med-mal TOTAL damages cap, Va. Code 8.01-581.15: caps everything recoverable, $50,000 annual steps; $2.70M for acts 7/1/2025–6/30/2026, **$2.75M for acts 7/1/2026–6/30/2027 (current)**, $3,000,000 for acts on/after 7/1/2031 — https://law.lis.virginia.gov/vacode/title8.01/chapter21.1/section8.01-581.15/
- Expert certification tied to service, 8.01-20.1 (sanctions, possible dismissal with prejudice, common-knowledge exception, amended 2025) — https://law.lis.virginia.gov/vacode/title8.01/chapter3/section8.01-20.1/
- Medical Malpractice Review Panel: request within 30 days of responsive pleading (8.01-581.2), panel composition (8.01-581.3), opinion admissible but not conclusive (8.01-581.8), statewide standard of care and expert's active clinical practice within one year (8.01-581.20)
- Limitations: 2 years personal injury whatever the theory, 5 years injury to property (8.01-243); 5 years signed written contract, 3 years unwritten (8.01-246); 4 years UCC sale from tender of delivery (8.2-725)
- Punitive cap $350,000 and jury not advised (8.01-38.1); ad damnum may be argued to the jury (8.01-379.1)
- Tort Claims Act: $100,000 or policy limits cap and 1-year written notice to the Division of Risk Management / Attorney General (8.01-195.3, 8.01-195.6); 6-month notice for city negligence claims (15.2-209)
- Contributory negligence bar: 8.01-58 shows the single statutory carve-out (railroad employees), confirming the bar elsewhere
- Assumption of risk as "venturousness," subjective test — Amusement Slides Corp. v. Lehmann, 217 Va. 815 (1977)
- Open-and-obvious / invitee duties — Fobbs v. Webb Building Ltd. P'ship; constructive notice sufficient — Memco Stores v. Yeatman
- Product burden and no res ipsa — Logan v. Montgomery Ward, 216 Va. 425 (1975)
- FTCA route for a federal employee: 2-year agency presentment, suit within 6 months of mailed denial, sum-certain limit — 28 U.S.C. 2401(b), 2675
- NAS Oceana scale (commissioned Aug 17, 1943; 14,600+ military personnel; 19 fighter/attack squadrons) — https://cnrma.cnic.navy.mil/Installations/NAS-Oceana/About/History/

Full URL list with per-fact detail: `research-vb-pi/NOTES-virginiabeachpersonalinjurylawyerpros.md`.

## Things in the brief that were wrong or needed deviation
1. **"the notice/certification requirement" for med mal** — Virginia has no live pre-suit *notice* statute for medical malpractice. What exists is the 8.01-20.1 certification tied to *requesting service* plus the *optional* review-panel request after a responsive pleading. The copy states it that way.
2. **"Expect the pricing page over its 1750 ceiling"** — the phase-1 pricing page was already 1682, comfortably under. The final phase-2 page needed only a 19-word trim after the first check, not the substantial trimming the brief anticipated.
3. **symptom_2 / symptom_3 titles rewritten** (deliberate deviation): the inherited symptom_2 was about a military/federal connection, which conflicted with site.json's `symptom_service` mapping (`medical-malpractice` in slot 2, `product-liability` in slot 3). symptom_2 is now harm during medical treatment; symptom_3 is a failed product. The military/federal angle was moved to the catastrophic-injury page and retained in qa_1.
4. **Va. Code 8.2-318 (privity)** could not be fetched (three consecutive timeouts on law.lis.virginia.gov), so no privity claim was written. `law.lis.virginia.gov` returns frequent 408s; fetch one URL at a time.
5. No conflict between the brief and site.json on city/state — Virginia Beach, VA in both.
