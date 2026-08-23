# Pricing research — cincinnatipersonalinjurylawyerpros.com (Personal Injury, Cincinnati / Hamilton County, OH)

Mode `fees`, fee_kind `contingency`. All figures retrieved **2026-08-23**.

## Bottom line on Ohio

**Ohio does not cap a contingency percentage in ordinary injury work.** No statute
and no Supreme Court rule prints a percentage for a negligence claim. The control
is Prof. Cond. R. 1.5(a): an "illegal or clearly excessive" fee is prohibited,
measured after the fact against eight enumerated factors. The page says that
plainly and never implies a ceiling exists.

## Figures used, with sources

| Figure | Authority | URL | Verified |
| --- | --- | --- | --- |
| No percentage ceiling; "illegal or clearly excessive fee" plus 8 factors | Ohio Prof. Cond. R. 1.5(a) | https://www.supremecourt.ohio.gov/docs/LegalResources/Rules/ProfConduct/profConductRules.pdf | 2026-08-23 |
| Contingent fee agreement must be a writing signed by client and lawyer, stating method, percentages for settlement / trial / appeal, expenses deducted, and whether deducted before or after the fee | Ohio Prof. Cond. R. 1.5(c)(1) | same PDF | 2026-08-23 |
| Signed closing statement required at or before receipt of compensation | Ohio Prof. Cond. R. 1.5(c)(2); R.C. 4705.15(C) | same PDF; https://codes.ohio.gov/ohio-revised-code/section-4705.15 | 2026-08-23 |
| Contingent fee for a criminal defendant prohibited; "earned upon receipt" language conditioned | Ohio Prof. Cond. R. 1.5(d)(2), (d)(3) | same PDF | 2026-08-23 |
| Tort contingent fee agreement must be reduced to writing, signed by both, copy to client | R.C. 4705.15(B) (definition of "tort action" in (A)(2)) | https://codes.ohio.gov/ohio-revised-code/section-4705.15 | 2026-08-23 |
| Noneconomic damages: greater of $250,000 or 3x economic loss, max $350,000 per plaintiff / $500,000 per occurrence; no limit on economic loss; no limit for the listed catastrophic injuries; jury not instructed on the limit | R.C. 2315.18(B)(1), (B)(2), (B)(3)(a)-(b), (F)(2) | https://codes.ohio.gov/ohio-revised-code/section-2315.18 | 2026-08-23 |
| Municipal court original jurisdiction limit $15,000 | R.C. 1901.17 | https://codes.ohio.gov/ohio-revised-code/section-1901.17 | 2026-08-23 |
| Civil suit filing $90 (service not included); new service residential/personal $30; certified mail $10; motion $5; jury demand filing fee $10; **jury deposit $300**; subpoena $6; witness fee $6 half day / $12 full day | Hamilton County Municipal Court Civil Rule XVIII (Filing Fees, Civil Division) | https://hamiltoncountycourts.org/wp-content/uploads/2016/02/Municipal_Civil_Rule_18.pdf | 2026-08-23 |
| Attorney fee taxed against the employer/commission in a successful common pleas workers' comp appeal **shall not exceed $5,000** | R.C. 4123.512(F) | https://codes.ohio.gov/ohio-revised-code/section-4123.512 | 2026-08-23 |
| Comp fee practice: written fee agreement required; no fee on ongoing temporary total or ongoing permanent total payments | Ohio Industrial Commission Joint Resolution R07-1-01, VII.B, VII.C, VII.D | https://www.ic.ohio.gov/about-ic/policies/resolutions-pdfs/r07_1_01.pdf | 2026-08-23 |

## Caps found that do NOT apply to a personal injury fee

- **R.C. 4123.512(F) $5,000** — a ceiling on the fee *taxed against the employer*
  when a claimant wins a workers' compensation appeal in common pleas. It is not
  a limit on a negligence contingency and is labeled that way on the page.
- **R.C. 2315.18(B)(2)** — a cap on *noneconomic damages*, not on the fee. It does
  reach ordinary injury claims, so the page presents it as a damages limit with
  the (B)(3) catastrophic-injury exceptions stated.
- Industrial Commission fee guidelines (R07-1-01) publish **no percentage**; the
  resolution governs authorizations and written agreements, not a rate.

## Could not verify

- **Hamilton County Clerk of Courts common pleas civil deposit amounts.**
  `courtclerk.org` returns HTTP 503 to scripts (Wordfence "advanced blocking"),
  and the 2025 Wayback capture renders the fee *labels* without the amounts.
  Because no amount could be read from a primary source, no common pleas dollar
  figure appears on the page. The municipal court amounts (Civil Rule XVIII) are
  used instead, together with the R.C. 1901.17 $15,000 jurisdiction line that
  explains which court a Cincinnati claim lands in.
- No Ohio statute setting a contingency percentage exists to cite, in any case
  type; the only comp-side dollar figure is the R.C. 4123.512(F) $5,000 above.
## Build verification (2026-08-23)

- `python template/build.py <domain> --check-only` -> [PASS], zero [ERROR]. Pricing page 1710 visible words (limit 900-1750).
- Full-portfolio `--check-only` run: this site appears in no [ERROR] line. Remaining portfolio failures belong to other in-flight batches (home-service sites plus other legal domains), not to this batch.
- Cross-site 15-word duplicate guard: statutory quotations that collided with other portfolio sites were paraphrased into distinct wording while preserving the rule's meaning and cited subdivision. No figure, percentage, or citation was changed to satisfy the guard.
