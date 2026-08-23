# Pricing research — modestopersonalinjurylawyerpros.com (Personal Injury, Modesto / Stanislaus County, CA)

Mode `fees`, fee_kind `contingency`. All figures retrieved **2026-08-23**.
Court authority: the **Stanislaus County Superior Court's own posted civil fee
schedule**. Structured differently from the Long Beach page (which is built on the
§ 6147 written-contract requirements and the Los Angeles Superior Court schedule) and
written to avoid reusing sentences from modestocaraccidentlawyerpros.com.

## Bottom line on California

**No California statute or rule caps a contingency percentage in ordinary injury
work.** Rule 1.5(a) prohibits an unconscionable or illegal fee; rule 1.5(b) supplies
thirteen factors. Every numeric percentage in California fee law belongs to a
different track: § 6146 (medical negligence) and Labor Code § 4906 (workers'
compensation, where the appeals board must approve the amount before it is accepted).
The 50% figure in Civil Code § 3045.4 is a **hospital lien** ceiling.

## Figures used, with sources

| Figure | Authority | URL | Verified |
| --- | --- | --- | --- |
| No unconscionable or illegal fee; unconscionability measured on the facts existing when the agreement was entered into; thirteen factors, including whether the lawyer failed to disclose material facts, the amount involved and results obtained, the relative sophistication of lawyer and client, and whether the client gave informed consent | Cal. Rules of Prof. Conduct, rule 1.5(a), (b) | https://www.calbar.ca.gov/legal-professionals/rules/rules-professional-conduct/current-rules-professional-conduct/chapter-1-lawyer-client-relationship | 2026-08-23 |
| Contingent fee barred in family law dissolution/support matters; barred for representing a criminal defendant (subdivision **(c)(2)**) | Cal. Rules of Prof. Conduct, rule 1.5(c)(1), (c)(2) | same URL | 2026-08-23 |
| **25%** before filing / **33%** after — claims against a health care provider based on professional negligence only | Bus. & Prof. Code § 6146(a) | https://law.justia.com/codes/california/code-bpc/division-3/chapter-4/article-8-5/section-6146/ | 2026-08-23 |
| Contingency contract must be signed in duplicate and state the rate, the effect of disbursements and costs, compensation for related matters, and — unless § 6146 governs — that the fee is not set by law but is negotiable; **noncompliance makes the contract voidable at the plaintiff's option**, with a reasonable fee then allowed; comp contracts excluded | Bus. & Prof. Code § 6147(a), (b), (c) | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=6147.&lawCode=BPC | 2026-08-23 |
| Comp fee unenforceable above a reasonable amount; attorney **shall not demand or accept any fee from an employee until the amount has been approved or set by the appeals board**; agreement submitted within 10 days; statutory factors; written disclosure form describing the range of fees customarily approved | Lab. Code § 4906(a)-(e) | https://law.justia.com/codes/california/code-lab/division-4/part-3/chapter-1/section-4906/ | 2026-08-23 |
| Hospital lien: payor liable "or so much thereof as can be satisfied out of **50 percent** of the moneys due under any final judgment, compromise, or settlement agreement after paying any prior liens" | Civ. Code § 3045.4 | https://law.justia.com/codes/california/code-civ/division-3/part-4/title-14/chapter-4/section-3045-4/ | 2026-08-23 |
| First paper, claim **over $10,000 up to $35,000: $370** (Gov. Code § 70613(a)); answer $370; unlimited civil first paper $435; first paper up to $10,000 $225 (§ 70613(b)) | Statewide Civil Fee Schedule eff. 01/01/2024, as posted by the Superior Court of California, County of Stanislaus — items 7, 9, 1, 10 | https://www.stanislaus.courts.ca.gov/system/files/general/statewide-civil-fee-schedule-eff-01012024-final.pdf | 2026-08-23 |
| Amendment increasing the amount at issue $145; **reclassification from limited to unlimited $140** (Gov. Code § 70619) | same schedule — items 13/14, 15 | same URL | 2026-08-23 |
| Motion or other paper requiring a hearing **$60**; summary judgment or adjudication **$500** | same schedule — items 45, 51 | same URL | 2026-08-23 |
| **Court reporting, civil hearing of one hour or less: $30** (Gov. Code § 68086(a)(1)(A)); per diem beyond one hour **$700 full day / $350 half day** | same schedule — items 66, 67 | same URL | 2026-08-23 |
| Advance jury fee $150; subsequent daily jury deposits set by the court | same schedule — items 64, 65 | same URL | 2026-08-23 |
| Courthouse-construction surcharges on the schedule apply to Riverside, San Bernardino and San Francisco filings only (not Stanislaus) | same schedule, surcharge note | same URL | 2026-08-23 |

## Caps found that do NOT apply to a personal injury fee

- **§ 6146(a), 25%/33%** — medical negligence only; stated as such on the page.
- **Lab. Code § 4906(b)** — workers' compensation approval requirement, and § 6147(c)
  keeps comp contracts outside the contingency-contract statute entirely.
- **Civ. Code § 3045.4, 50%** — a hospital lien ceiling measured against the injured
  person's settlement money, not against the fee.
- **Rule 1.5(c)(2)** — criminal-defendant contingency ban lives in (c)(2), verified on
  the State Bar page; it is not a fee cap for injury work.

## Could not verify / notes

- leginfo blocks script fetches of Civ. Code § 3045.4 and Lab. Code § 4906; the Justia
  copies were fetched and cited. Bus. & Prof. Code § 6147 was fetched from leginfo.
- The Stanislaus court posts the statewide schedule rather than a county-specific one;
  the citation therefore names the court that publishes it and the schedule's
  effective date. No Stanislaus-specific surcharge exists on that schedule.
- Divergence from modestocaraccidentlawyerpros.com: this page is anchored on the $370
  mid-tier first paper, the $30/$700/$350 court-reporting items and the $140
  reclassification fee, plus § 4906 and § 3045.4 — none of which anchor the car page
  (which uses $435, the $150 jury fee and the $1,000 complex designation).
## Build verification (2026-08-23)

- `python template/build.py <domain> --check-only` -> [PASS], zero [ERROR]. Pricing page 1745 visible words (limit 900-1750).
- Full-portfolio `--check-only` run: this site appears in no [ERROR] line. Remaining portfolio failures belong to other in-flight batches (home-service sites plus other legal domains), not to this batch.
- Cross-site 15-word duplicate guard: statutory quotations that collided with other portfolio sites were paraphrased into distinct wording while preserving the rule's meaning and cited subdivision. No figure, percentage, or citation was changed to satisfy the guard.
