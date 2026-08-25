# Jonesboro PI pages — phase 2 conversion report

## Build check

```
[PASS] jonesboropersonalinjurylawyerpros.com -- home 1750 words, 4 symptoms, 3 local Q&As, 3 sourced facts
exit 0
```

## Per-page word counts

| Page | Words |
|---|---|
| / | 1787 (check counts 1750 body, limit 1300–2300) |
| /services/ | 572 |
| /slip-and-fall-lawyer/ | 1491 |
| /medical-malpractice-lawyer/ | 1522 |
| /product-liability-lawyer/ | 1455 |
| /catastrophic-injury-lawyer/ | 1536 |
| /pricing/ | 1750 (ceiling 1750) |
| /about/ | 401 |
| /contact/ | 581 |

Pricing landed exactly at the ceiling after trimming prose only. No dollar figure or fee line was removed; every statutory fee ($150.00, $50.00, $167.50, $165.00, $140.00, $2.50, $30.00, $20.00, $100.00, $500, $1,000, $200, $1,000.00) is still on the page.

## What changed

- `symptom_1`–`symptom_4` cut from 200–360 words to 40–80-word teasers, each pointing at its mapped service page (slip and fall, medical malpractice, product liability, catastrophic injury).
- Added `services_summary` (110 words), `services_pick_head`, `crosslink_head`.
- Added `svc_slip_and_fall_lawyer_lede/_body`, `svc_medical_malpractice_lawyer_lede/_body`, `svc_product_liability_lawyer_lede/_body`, `svc_catastrophic_injury_lawyer_lede/_body` — 7 `###` sections each, slugs taken from site.json.
- `site.json` `"phase"` flipped 1 → 2. Nothing else in site.json touched.
- Collision guard: independently verified 0 shared 15-word runs against all 8 named siblings. Two passages had unconsciously tracked the Cincinnati file (the 25/50/25 limits sentence and the catastrophic-damages documentation paragraph); both were rewritten from scratch.
- QC sweep after writing: no sentence of 45+ words in any new block, no doubled words, no bare decimals, no heading over 90 chars, no one-sentence heading ending in a period.

## Three strongest verified local facts

1. Craighead County has two county seats and two courthouse districts, and the Second Judicial Circuit's own administrative plan sets out how the work splits: in the Eastern District at Lake City every civil and criminal case goes to the judge in Division 10, while in the Western District at Jonesboro civil filings are divided equally among Divisions 1, 2 and 9. Six counties, nine courthouses. https://arcourts.gov/sites/default/files/files-list/2nd%20Circuit.pdf
2. Both Jonesboro hospitals — St. Bernards Medical Center and NEA Baptist Memorial Hospital — are designated Level III trauma centers, and no Level I or Level II center is designated anywhere in northeast Arkansas; the nearest Level I facilities are Regional One Health in Memphis and UAMS in Little Rock. https://healthy.arkansas.gov/wp-content/uploads/Designated-Trauma-Centers-7-15-26.pdf
3. ARDOT records that a 4.8-mile segment of Highway 63 between Southwest Drive and Highway 91 (Dan Avenue) was approved as part of Interstate 555 in November 2021, completing a corridor upgrade that drew more than $300 million in investment. https://ardot.gov/news/21-385/

Runner-up used on the product page: USDA's 2022 Census of Agriculture counts 393 farms and 283,467 acres of farmland in Craighead County (91,851 acres soybeans, 79,950 cotton, 38,632 rice, 33,955 corn), while Ark. Code § 11-9-102(11)(A)(iii) excludes agricultural farm labor from workers' compensation coverage. https://www.nass.usda.gov/Publications/AgCensus/2022/Online_Resources/County_Profiles/Arkansas/cp05031.pdf and https://law.justia.com/codes/arkansas/title-11/chapter-9/subchapter-1/section-11-9-102/

## Where the brief was wrong or incomplete

1. **The collateral source rule is no longer intact.** The brief asked for "Arkansas's rule on the collateral source doctrine" as settled background. Act 28 of 2025 (HB1204, approved Feb. 11, 2025) amended § 16-64-120 so that recovery for past necessary medical care "includes only those costs actually paid by or on behalf of the plaintiff or that remain unpaid and for which the plaintiff or any third party is legally responsible." That is materially the same paid-not-billed limit the Supreme Court struck in 2009 as an evidence rule (§ 16-55-212(b), Johnson v. Rockwell Automation), now rewritten as a damages rule. No decided constitutional challenge was found. https://arkleg.state.ar.us/Home/FTPDocument?path=/ACTS/2025R/Public/ACT28.pdf
2. **The 2003 act never contained a non-economic damages cap.** The brief refers to "damages caps" in the 2003 tort reform act. Act 649 of 2003 capped punitive damages (§ 16-55-208, struck in Bayer CropScience LP v. Schafer), created nonparty fault (§ 16-55-202, struck in Johnson v. Rockwell), limited medical-cost evidence (§ 16-55-212(b), struck), and added a same-specialty expert requirement (§ 16-114-206(a), struck in Broussard). There was no statutory non-economic cap to strike.
3. **The 2018 amendment was not voted down; it never reached a count.** Issue 1 (SJR 8) was removed from the ballot by the Supreme Court on Oct. 18, 2018 for violating the separate-vote requirement of article 19, § 22 — its sections were not reasonably germane. It would have set a $500,000 non-economic cap, a punitive cap at the greater of $500,000 or three times compensatory damages, and a 33 1/3 percent contingency-fee limit. https://wehco.media.clients.ellingtoncms.com/news/documents/2018/10/18/issue1.pdf
4. **Arkansas State University claims do not go to circuit court at all, and the fork is narrower than "claims against the state."** Article 5, § 20 is absolute, and the Claims Commission's exclusive jurisdiction under § 19-10-204 covers the state and its institutions but expressly not counties, cities or school districts. The commission also cannot pay an award above $15,000 without a referral to the General Assembly (§ 19-10-215).
5. **No verifiable traffic figure exists for the corridor at the level requested.** No ARDOT AADT or truck-percentage number for I-555 or US 63 through Jonesboro could be fetched, so the trucking material is written around investment, designation history and corridor geography instead of invented volumes. Likewise, no primary source was found for build eras or development dates of the six site.json neighborhoods, so they are used only as locations.

No conflict was found between site.json and the brief; site.json's four slugs, county, city and neighborhood list were used exactly as written.

## Files

- Edited: `sites/jonesboropersonalinjurylawyerpros.com/copy.md`, `sites/jonesboropersonalinjurylawyerpros.com/site.json` (phase only)
- Research notes with every URL: `jonesboro-pi-phase2-research.md`
- Draft block staging file (left in place): `_jonesboro_new_blocks.md`
