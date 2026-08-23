# Pricing pages batch 5 — as-built summary (2026-08-23)

All five sites got a `pricing` block in `sites/<domain>/site.json` (inserted after `schema`, matching the
Tampa reference) plus `## pricing_lede` and `## pricing_body` in `sites/<domain>/copy.md`.
All use `mode: "fees"`, `fee_kind: "contingency"`, 4 anchors and 6 fee_rows.

| Site | Rendered /pricing/ words | Status |
|---|---|---|
| salinascaraccidentlawyer.com | 1749 | PASS |
| santabarbaracaraccidentlawyer.com | 1743 | PASS |
| victorvillecaraccidentlawyerpros.com | 1731 | PASS |
| westcovinacaraccidentlawyerpros.com | 1717 | PASS |
| virginiabeachcaraccidentlawyerpros.com | 1720 | PASS |

Portfolio check (`python template/build.py --check-only`): **82 PASS / 1 FAIL**. The single failure is
`sanjoseduilawyerpros.com`, which shares five 15-word runs with `newportbeachduilawyerpros.com` — both are
DUI sites outside this batch whose pricing copy was added by another concurrent batch. None of the five
sites in this batch collide with each other or with any other site.

## Rules and statutes cited

California (Salinas, Santa Barbara, Victorville, West Covina):
- Cal. Rules of Prof. Conduct rule 1.5(a)-(b) — unconscionable/illegal fee prohibited, thirteen factors, no
  percentage cap for ordinary negligence; rule 1.5.1(a) fee-division conditions.
  https://www.calbar.ca.gov/legal-professionals/rules/rules-professional-conduct/current-rules-professional-conduct/chapter-1-lawyer-client-relationship
- Cal. Bus. & Prof. Code 6147(a)-(b) — written contingency contract, duplicate copy, four required
  statements including "the fee is not set by law but is negotiable"; defect makes it voidable.
  https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=6147.&lawCode=BPC
- Cal. Bus. & Prof. Code 6146(a) — 25% / 33% ceiling, labeled on every page as **medical malpractice only**.
  https://law.justia.com/codes/california/code-bpc/division-3/chapter-4/article-8-5/section-6146/
- Cal. Code Civ. Proc. 1033.5 — recoverable vs non-recoverable costs.
  https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1033.5.&lawCode=CCP
- Cal. Code Civ. Proc. 631(b) — $150 nonrefundable advance jury fee (Salinas, West Covina).
  https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=631.&lawCode=CCP
- Cal. Civ. Code 3040(c) — one-third ceiling on a health plan / medical group reimbursement lien.
  https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=3040.&lawCode=CIV

County fee schedules, one per California site (no convergence):
- Monterey County (Salinas): $435 / $370 / $225, $60 motion, $500 MSJ, $150 jury, $30 reporter, $1,000 complex.
  https://www.monterey.courts.ca.gov/system/files/general/2024-civil-fee-schedule.pdf
- Santa Barbara County: item numbers cited — $435 (1), $60 (45), $500 (51), $50 change of venue (55), $150 (64), $30 (66).
  https://www.santabarbara.courts.ca.gov/system/files/general/statewide-civil-fee-schedule-eff-01012024.pdf
- San Bernardino County (Victorville): $35 local courthouse-construction surcharge, limited civil $240 / $380, unlimited $435.
  https://sanbernardino.courts.ca.gov/system/files/civil/feesched.pdf
- Los Angeles County (West Covina): court reporter $30 / $382 / $764, complex $1,000 + $1,000 per defendant to $18,000,
  daily jury deposit $15 per juror per day plus $0.34/mile one way.
  https://lascpubstorage.blob.core.windows.net/cpw/LIBSVCExecutiveSupport-265-2024FeeSchedule010124.pdf

Virginia (Virginia Beach):
- Va. Rules of Prof. Conduct Rule 1.5(a)-(d) — reasonable fee + eight factors, written contingent-fee terms
  (method, percentages on settlement/trial/appeal, expenses, before-or-after), closing statement,
  nonrefundable advanced legal fees prohibited, contingent fees barred in domestic relations and criminal defense.
  https://vsb.org/Site/Site/about/rules-regulations/rpc-part6-sec2.aspx
- Va. Code 17.1-275(A)(13), (13a) — clerk's fee $100 / $200 / $250 / $300, $50 settlement-approval petition.
  https://law.lis.virginia.gov/vacode/title17.1/chapter2/section17.1-275/
- Va. Code 58.1-1727 — writ tax $5 / $15 / $25.
  https://law.lis.virginia.gov/vacode/title58.1/chapter17/section58.1-1727/
- Va. Code 8.01-66.2 and 8.01-66.5 — lien ceilings $2,500 / $750 / $200 and the written-notice requirement.
  https://law.lis.virginia.gov/vacode/title8.01/chapter3/section8.01-66.2/
  https://law.lis.virginia.gov/vacode/title8.01/chapter3/section8.01-66.5/
- Va. Code 8.01-413(B2)-(B3) — records charges, $160 electronic cap.
  https://law.lis.virginia.gov/vacode/title8.01/chapter14/section8.01-413/
- Va. Code 8.01-581.15 — $2.70M / $2.75M malpractice cap, labeled as a cap on recovery, not on fees.
  https://law.lis.virginia.gov/vacode/title8.01/chapter21.1/section8.01-581.15/
- Virginia Beach Circuit Court civil fee schedule — $9 legal aid, $5 technology trust fund, $4 law library,
  $2 courthouse maintenance, $1 indigent defense, $10 court technology.
  https://www.vacourts.gov/caseinfo/circuit_fees/virginia_beach_circ_civil_fees.pdf

## Could not verify
- Welf. & Inst. Code 14124.78 (Medi-Cal lien arithmetic) is robots-disallowed on leginfo, so no Medi-Cal
  figure was used on any page.
- No 2026-dated Monterey or Los Angeles fee schedule is published; the 2024-dated court-hosted schedules were
  used and each cited figure matches the statewide schedule effective 01/01/2026 where the statewide schedule
  contains it.
- No single named "personal injury filing fee" total exists for Virginia Beach; the page shows the components
  instead, which is how the clerk publishes them.

## Helper scripts left in place
- `apply_pricing_batch5.py` — the generator that wrote the blocks (already run; re-running will refuse because
  the pricing blocks now exist).
- `dupe_check_batch5.py` — cross-site 15-word shingle comparison across the five sites.
