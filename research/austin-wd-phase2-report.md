# waterdamageaustinco.com — phase 2 completion report

## Build result

```
[PASS] waterdamageaustinco.com -- home 1749 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           349 words  /about/
          1381 words  /basement-water-damage-restoration/
           617 words  /contact/
          1323 words  /flood-damage-restoration/
          1902 words  /
          1749 words  /pricing/
           586 words  /services/
          1316 words  /sewage-cleanup/
          1325 words  /water-extraction/
exit=0
```

Authored body lengths: water_extraction 800, basement 852, sewage 783, flood 771 words. Ledes 42-44 words. Symptom teasers 40-80 words. `"phase": 2` set in site.json (only field changed).

## Files changed
- `sites/waterdamageaustinco.com/copy.md`
- `sites/waterdamageaustinco.com/site.json` (phase only)

Symptom titles 2, 3 and 4 were rewritten so each teaser matches the service page it links to per `symptom_service` in site.json (2 → basement, 3 → sewage, 4 → flood). The old symptom 4 (hidden leak / musty room) content moved into the water-extraction body.

Pricing page trimmed from 1813 to 1749 words by cutting prose only. No dollar figure or fee removed ($200.43, $184.70, $1,500-$4,000, $448, $65, $1,031, $175, section 15-9-141 all intact). The expansive-clay sentence was cut from `pricing_body` — it was collision risk with foundationrepairaustinco.com and not needed.

## Differentiator built into the site
Insurance claim clock + technical standard of care:
- Ch. 542 prompt-pay schedule (water-extraction page)
- Ch. 542A pre-suit notice (sewage + flood pages, phrased differently on each)
- Ch. 1813 appraisal, S.B. 458 (basement page)
- TDLR mold licensing, 25 contiguous sq ft, water-damage emergency notification, Certificate of Mold Damage Remediation (basement page)
- S500 categories and classes, EPA 24-48 hours, EPA "no federal limits" position (all four pages, split so no page repeats another)

## Sources verified by fetch
- Tex. Ins. Code ch. 542 — https://statutes.capitol.texas.gov/Docs/IN/pdf/IN.542.pdf
- Tex. Ins. Code ch. 542A — https://statutes.capitol.texas.gov/Docs/IN/pdf/IN.542A.pdf
- Tex. Ins. Code ch. 1813 (S.B. 458, eff. 9/1/2025) — https://statutes.capitol.texas.gov/Docs/IN/pdf/IN.1813.pdf
- TDI water damage & mold — https://www.tdi.texas.gov/tips/when-are-water-damage-and-mold-covered-by-insurance.html
- TDI home damage FAQ (sewer/drain backup "depends on your policy") — https://www.tdi.texas.gov/consumer/storms/home-damaged-faq.html
- TDLR mold FAQ — https://www.tdlr.texas.gov/mld/mldfaq.htm
- TDLR consumer mold information sheet (certificate, 5 years, underwriting) — https://www.tdlr.texas.gov/mld/pdf/cmis.pdf
- TDLR mold notifications ($25 fee, water-damage emergency) — https://www.tdlr.texas.gov/mld/mldnotifications.htm
- IICRC S500 5th ed. 2021 — https://iicrc.org/s500/
- IICRC weather position statement (Cat 3 definition, 10.4.1, 12.2.6) — https://iicrc.org/wp-content/uploads/2026/04/Weather-Related-Position-Statement_2026.pdf
- S500 categories 1-3 quoted verbatim — https://ehs.ucr.edu/media/4811/download
- S500 classes 1-4 quoted verbatim (ANSI/IICRC S500) — https://www.bgsu.edu/risk-management/policies-and-procedures/water-intrusion-protocol.html
- EPA ten things (24-48 hours, moisture control) — https://www.epa.gov/mold/what-are-ten-things-i-need-know-about-mold
- EPA testing/sampling (no federal limits) — https://www.epa.gov/mold/mold-testing-or-sampling
- EPA mold and health — https://www.epa.gov/mold/mold-and-health
- FEMA flood insurance (30-day wait) — https://www.fema.gov/flood-insurance
- Atlas 14 Austin FAQ (10.2 in vs >13 in) — https://www.austintexas.gov/sites/default/files/files/Watershed/flood/Atlas14__FAQ_English.pdf
- Austin flood safety (10% of land, 75% of deaths in vehicles, Class B misdemeanor) — https://www.austintexas.gov/watershed-protection/atx-flood-safety
- Austin creek flooding (9,000 buildings, 300 bridges) — https://www.austintexas.gov/watershed-protection/projects/creek-flooding
- 2013 Halloween Flood (41 ft, 11 ft in 15 min, 659/259/15) — https://data.austintexas.gov/stories/s/2013-Halloween-Flood/fr92-dkxr/
- Shoal Creek 1981 (6 in, 13 deaths, $35.5M, 16,000 cfs; 1991/2001/2015 peaks) — https://www.austintexas.gov/sites/default/files/files/Watershed/flood/Shoal_Presentation_March2017.pdf
- Austin Water mains (4,000 mi, 9.2 breaks/100 mi vs 25 industry) — https://services.austintexas.gov/edims/document.cfm?id=447846
- Boil water notices 2018 / 2021 / 2022 (turbidity 5-6 to 387 NTU; Feb 5-8, 2022) — https://www.austintexas.gov/sites/default/files/files/Auditor/Audit_Reports/Special_Report_External_Review_of_Austin_Water_Quality_Events_January_2023.pdf
- Feb 5 2022 citywide boil water notice — https://www.austintexas.gov/water/news/austin-water-issues-precautionary-citywide-boil-water-notice-mandatory-emergency-water
- Austin Water leak adjustment, City Code 15-9-141 — https://www.austintexas.gov/water/high-water-bill-options

## Things in the brief that were wrong or unverifiable
1. **Typical mold sublimit dollar figures do not appear on TDI.** TDI says most home policies do not include mold cleanup and testing after a damaged item is removed, and that coverage may be addable. No sublimit number was published, so no figure was written.
2. **Building count discrepancy.** site.json and the city's creek-flooding page say "more than 9,000 buildings in the 100-year floodplain"; the city's flood-safety page says "more than 10,000 buildings and 300 bridges." site.json wins, so the copy uses 9,000.
3. **EPA "stop the water rather than sample" is two separate pages,** not one statement: the sampling position is on the mold testing page, the moisture-control statement on the ten-things page. Both cited.
4. **Category/class definitions are not published on iicrc.org.** They were verified from two institutional documents that quote ANSI/IICRC S500 verbatim (UC Riverside EHS, Bowling Green State University). The copy therefore describes tiers without asserting a numbered list attributed directly to a fetched IICRC page.
5. **Onion Creek rainfall/deaths and Camp Mabry climate data were deliberately avoided** — foundationrepairaustinco.com owns that material.
