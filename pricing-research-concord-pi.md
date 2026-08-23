# Pricing research — concordpersonalinjurylawyer.com (Personal Injury, Concord / Cabarrus County, NC)

Mode `fees`, fee_kind `contingency`. All figures retrieved **2026-08-23**.

## Bottom line on North Carolina

**North Carolina sets no percentage ceiling on an injury contingency.** Rule 1.5(a)
of the Rules of Professional Conduct forbids a "clearly excessive" fee and lists
eight factors. The frequently misquoted 50% figure in G.S. 44-50 is a ceiling on
a **medical provider's lien**, expressly "exclusive of attorneys' fees" — it is not
a fee cap, and the page labels it as a lien limit. Workers' compensation fees are
the one place a decision-maker sets the number: G.S. 97-90 requires **Industrial
Commission approval**.

## Figures used, with sources

| Figure | Authority | URL | Verified |
| --- | --- | --- | --- |
| No percentage ceiling; "clearly excessive fee" plus 8 factors; basis communicated preferably in writing | N.C. Rev. R. Prof. Conduct 1.5(a), (b) | https://www.ncbar.gov/for-lawyers/ethics/rules-of-professional-conduct/rule-15-fees/ | 2026-08-23 |
| Contingent fee agreement in writing signed by the client, stating method, percentages for settlement / trial / appeal, expenses deducted and whether before or after the fee, and expenses owed win or lose; written statement of outcome and remittance at the conclusion | N.C. Rev. R. Prof. Conduct 1.5(c) | same URL | 2026-08-23 |
| No contingent fee for a criminal defendant (asset-forfeiture carve-out); none where law prohibits | N.C. Rev. R. Prof. Conduct 1.5(d)(1), (d)(2) | same URL | 2026-08-23 |
| Court may tax reasonable attorneys' fees as costs in a personal injury / property damage suit on unwarranted refusal to negotiate, where damages recovered are **$25,000 or less** and recovery exceeded the highest offer made at least 90 days before trial; **award shall not exceed $10,000** | G.S. 6-21.1(a), (b) | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_6/GS_6-21.1.html | 2026-08-23 |
| Provider lien attaches to settlement funds; nothing interferes with any amount due for attorney's services; lien, **exclusive of attorneys' fees, shall in no case exceed 50%** of damages recovered | G.S. 44-50 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_44/GS_44-50.html | 2026-08-23 |
| General Court of Justice fee **$180 superior**, $130 district, $80 magistrate; facilities fee $16 district/superior; $4.00 telecommunications and data connectivity fee; advance costs collected at filing | G.S. 7A-305(a)(2), (a)(1), (a)(1a), (c) | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_7A/GS_7A-305.html | 2026-08-23 |
| **$20** fee for filing a notice of hearing on a motion not listed in G.S. 7A-308; one fee per motion | G.S. 7A-305(f) | same URL | 2026-08-23 |
| Private process server assessable at actual cost **or $50, whichever is less**, unless the court finds service was difficult; expert witness fees only for actual time spent providing testimony; (d) is an exclusive list of assessable expenses | G.S. 7A-305(d)(6), (d)(11), (d) | same URL | 2026-08-23 |
| If the Medicaid claim exceeds one-third of the gross recovery, **one-third of the gross recovery is presumed** to represent the claim; beneficiary may dispute by application within 30 days under a clear-and-convincing standard | G.S. 108A-57(a1), (a2) | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_108A/GS_108A-57.html | 2026-08-23 |
| Medical malpractice noneconomic damages limited to **$500,000**, adjusted by CPI every third year from Jan. 1, 2014; no limit where disfigurement, loss of use, permanent injury or death is joined with reckless, grossly negligent, fraudulent, intentional or malicious conduct; jury not instructed on the limit | G.S. 90-21.19(a), (b)(1)-(2), (d) | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_90/GS_90-21.19.html | 2026-08-23 |
| Workers' comp attorney fees subject to Industrial Commission approval; agreement filed before the hearing concludes, approved unless unreasonable, appeal path to the full Commission then to the senior resident superior court judge; Commission has **no jurisdiction over fees in a third-party action** | G.S. 97-90(a), (c) | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_97/GS_97-90.html | 2026-08-23 |

## Caps found that do NOT apply to a personal injury fee

- **G.S. 44-50, 50%** — a ceiling on what medical providers can take from the
  settlement, computed *exclusive of* attorneys' fees. Not a fee cap. Labeled as a
  provider-lien limit in both the anchor and the body.
- **G.S. 90-21.19(a), $500,000** — medical malpractice noneconomic damages only.
- **G.S. 6-21.1(a), $10,000** — a ceiling on a fee the *court taxes against the
  defendant* as costs; it adds money on the claimant's side rather than limiting
  the contract.
- **G.S. 97-90** — Commission approval applies to workers' compensation, and the
  statute itself disclaims jurisdiction over third-party (liability) fees.

## Could not verify / notes

- Nothing failed to verify. Every figure above was read from ncleg.gov or the
  N.C. State Bar's own rule page on 2026-08-23.
- Cabarrus County has no separate local civil filing schedule; costs are the
  statewide General Court of Justice amounts in G.S. 7A-305, collected by the
  Cabarrus County Clerk of Superior Court. The page therefore cites the statute
  rather than a county chart (the companion car-accident site uses the statewide
  costs chart PDF, so the statute cite also keeps the two pages distinct).
## Build verification (2026-08-23)

- `python template/build.py <domain> --check-only` -> [PASS], zero [ERROR]. Pricing page 1743 visible words (limit 900-1750).
- Full-portfolio `--check-only` run: this site appears in no [ERROR] line. Remaining portfolio failures belong to other in-flight batches (home-service sites plus other legal domains), not to this batch.
- Cross-site 15-word duplicate guard: statutory quotations that collided with other portfolio sites were paraphrased into distinct wording while preserving the rule's meaning and cited subdivision. No figure, percentage, or citation was changed to satisfy the guard.
