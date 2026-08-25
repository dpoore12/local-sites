# concordpersonalinjurylawyer.com — Phase 2 conversion report

## Build result

```
[PASS] concordpersonalinjurylawyer.com -- home 1745 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           375 words  /about/
          1536 words  /catastrophic-injury-lawyer/
           573 words  /contact/
          1905 words  /
          1500 words  /medical-malpractice-lawyer/
          1745 words  /pricing/
          1538 words  /product-liability-lawyer/
           584 words  /services/
          1513 words  /slip-and-fall-lawyer/
EXIT=0
```

`site.json` `"phase"` flipped 1 -> 2. Only `copy.md` and that one field were edited.

Duplicate 15-word-run check against every other `sites/*/copy.md`: **zero shared runs** (independent shingle scan, not just the build's sibling list). Pricing sits at 1745 of the 1750 ceiling with every dollar figure and fee intact.

## Differentiator

Four services, all non-auto, using slugs exactly as in site.json:
`slip-and-fall-lawyer`, `medical-malpractice-lawyer`, `product-liability-lawyer`, `catastrophic-injury-lawyer`.

Legal spine (all fetched from ncleg.gov unless noted):
- Premises: Nelson v. Freeland single reasonable-care duty for lawful visitors; NC pattern instruction 805.55 on obvious dangers and equal/superior knowledge; G.S. 1-50(a)(5) six-year repose plus the (d) possession/control carve-out.
- Malpractice: G.S. 90-21.12(a) same-or-similar-communities standard; (b) clear-and-convincing burden for emergency medical conditions; Rule 9(j) certification and the 120-day extension; G.S. 1-15(c) two clocks and the four-year outer wall; G.S. 90-21.19 cap.
- Products: G.S. 99B-1.1 (no strict liability), 99B-6 design, 99B-5 warning, 99B-4 three complete bars, 99B-3 alteration; G.S. 1-46.1(1) twelve-year repose; dog bite via G.S. 67-4.4 / 67-4.1 / 67-12.
- Catastrophic: G.S. 97-10.1 exclusivity; Woodson v. Rowland; G.S. 97-22 thirty-day notice and 97-24(a) two-year bar; G.S. 28A-18-2 and 1-53(4).
- Forum/fees: G.S. 7A-243 $25,000 division line, Cabarrus County Courthouse; NC Rev. R. Prof. Conduct 1.5.

Contributory negligence appears only twice, briefly, phrased as "blame is not split into shares," with no overlap with the car-accident sibling's wording, and none of its facts (I-85 widening, 2023 crash counts, Bruton Smith Boulevard, G.S. 20-279.21, 50/100/50 minimums) reused.

## Three strongest verified local facts

1. **Atrium Health Cabarrus is a Level III trauma center at 920 Church Street North, Concord** — NC Office of EMS trauma contacts list: https://oems.nc.gov/wp-content/uploads/2025/07/Trauma-Contacts-07.25.pdf
2. **Propst Realty Company paid $66,000 in January 1937 for the 213 acres that became Wil-Mar Park; Gibson Mill village housing dates 1900–1940, with 86 houses by 1901 and roughly twelve original McGill Avenue storefronts still standing** — City of Concord Historic Architectural Survey: https://apps.concordnc.gov/legacy/planningweb/Historic/HPP-Architectural%20Survey.pdf
3. **Concord-Padgett Regional Airport supports 4,430 local jobs, has 226 based aircraft, and hosts NASCAR's air force plus several flight schools** — City of Concord: https://concordnc.gov/Services/Community/News/ID/193/Concord-Padgett-Regional-Airport-Generates-$900-Million-Economic-Impact

Also used: the med-mal cap of **$712,847 as of January 1, 2026**, up from $656,730 as of January 1, 2023 — NC Office of State Budget and Management: https://www.osbm.nc.gov/facts-figures/economy/liability-limit-noneconomic-damages-medical-malpractice (verified from the page's raw HTML; an LLM extraction of the same page returned a wrong figure/date, so trust the raw values). Cabarrus County Courthouse address confirmed at https://www.nccourts.gov/locations/cabarrus-county/cabarrus-county-courthouse

## Errors found in the brief

1. **"the 4-year statute of repose for product liability" is wrong.** North Carolina's product liability repose is **twelve years** from the date of initial purchase for use or consumption, G.S. 1-46.1(1): https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_1/GS_1-46.1.html — the four-year figure is the *medical malpractice* outer limit in G.S. 1-15(c). The copy uses twelve years for products and four years for malpractice.
2. **G.S. 67-4.4 is narrower than "strict liability for dog owners."** It applies only to a "dangerous dog" as defined in G.S. 67-4.1, which normally requires an administrative determination by the local animal control authority, with three-day objections, a hearing within ten days, and de novo appeal to superior court. The copy says so explicitly.
3. Minor: the brief suggested Cabarrus Health Alliance as a possible trauma destination. It is not one — it is the county's public health authority, created effective July 1, 1997 (https://www.cabarrushealth.org/218/About-Us). Atrium Health Cabarrus is the Level III trauma center, and the copy uses that.

No conflicts arose between site.json and the brief; site.json's city, state, slugs, neighborhoods and local facts were followed exactly.
