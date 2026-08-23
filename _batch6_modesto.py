import json, pathlib

BAR = "https://www.calbar.ca.gov/legal-professionals/rules/rules-professional-conduct/current-rules-professional-conduct/chapter-1-lawyer-client-relationship"
S6147 = "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=6147.&lawCode=BPC"
S6146 = "https://law.justia.com/codes/california/code-bpc/division-3/chapter-4/article-8-5/section-6146/"
LAB = "https://law.justia.com/codes/california/code-lab/division-4/part-3/chapter-1/section-4906/"
LIEN = "https://law.justia.com/codes/california/code-civ/division-3/part-4/title-14/chapter-4/section-3045-4/"
SCHED = "https://www.stanislaus.courts.ca.gov/system/files/general/statewide-civil-fee-schedule-eff-01012024-final.pdf"

pricing = {
  "mode": "fees",
  "fee_kind": "contingency",
  "table_head": "Three separate questions in a Stanislaus County injury claim: the fee standard, the caps on other case types, and the clerk's amounts",
  "col_a": "Question being asked",
  "col_b": "The published answer",
  "anchors": [
    {
      "label": "Number California puts on a negligence fee",
      "value": "There is no number",
      "detail": "The governing rule bars an unconscionable or illegal fee and then lists thirteen circumstances for evaluating one. A percentage for injury work appears nowhere in it.",
      "source_name": "Cal. Rules of Prof. Conduct, rule 1.5(a)",
      "source_url": BAR,
    },
    {
      "label": "First paper where the claim runs above $10,000 to $35,000",
      "value": "$370",
      "detail": "Taken from the civil fee schedule the Stanislaus County Superior Court posts for filings in Modesto, and charged again on the answering party's first paper.",
      "source_name": "Stanislaus County Superior Court civil fee schedule, item 7",
      "source_url": SCHED,
    },
    {
      "label": "Court reporting for a civil hearing of an hour or less",
      "value": "$30",
      "detail": "Beyond an hour the schedule switches to a per diem of $700 for a full day or $350 for a half day, charged for each reporter the proceeding requires.",
      "source_name": "Stanislaus County Superior Court civil fee schedule, item 66",
      "source_url": SCHED,
    },
    {
      "label": "Ceiling on a hospital lien against a settlement",
      "value": "50 percent of the money due",
      "detail": "That limit governs how much a hospital lien can pull out of a judgment or settlement after prior liens are paid. It is a limit on the hospital, not on a fee.",
      "source_name": "Cal. Civ. Code 3045.4",
      "source_url": LIEN,
    },
  ],
  "fee_rows": [
    {
      "stage": "Fee in a Modesto negligence claim",
      "share": "Not set by statute",
      "note": "Reviewed against thirteen listed circumstances, including whether material facts went undisclosed, the proportion between fee and the value of services, and whether informed consent was given.",
      "source_name": "Cal. Rules of Prof. Conduct, rule 1.5(b)",
      "source_url": BAR,
    },
    {
      "stage": "Professional negligence against a health care provider",
      "share": "25% before filing, 33% after",
      "note": "A medical negligence schedule and nothing broader, computed on the sum recovered after disbursements, with higher rates allowed only on a good-cause motion.",
      "source_name": "Cal. Bus. & Prof. Code 6146(a)",
      "source_url": S6146,
    },
    {
      "stage": "Workers' compensation representation",
      "share": "Amount fixed by the appeals board",
      "note": "The board approves or sets the figure before any fee may be demanded or accepted from the injured worker, weighing responsibility assumed, care exercised, time involved and results.",
      "source_name": "Cal. Lab. Code 4906(b), (d)",
      "source_url": LAB,
    },
    {
      "stage": "Contingency contract missing a required statement",
      "share": "Voidable at the client's option",
      "note": "Once voided, the attorney may collect a reasonable fee instead of the contract share, which is why the required disclosures deserve reading at signature.",
      "source_name": "Cal. Bus. & Prof. Code 6147(b)",
      "source_url": S6147,
    },
    {
      "stage": "Reclassifying a limited case as unlimited",
      "share": "$140",
      "note": "Filed when discovery shows the claim exceeds the limited jurisdiction ceiling, while an amendment that raises the amount at issue within the same tier is $145.",
      "source_name": "Stanislaus County Superior Court civil fee schedule, item 15",
      "source_url": SCHED,
    },
    {
      "stage": "Motions during the case",
      "share": "$60, or $500 for summary judgment",
      "note": "Any paper requiring a hearing draws the first amount, while a summary judgment or summary adjudication motion draws the second.",
      "source_name": "Stanislaus County Superior Court civil fee schedule, items 45 and 51",
      "source_url": SCHED,
    },
  ],
}

LEDE = """Three different questions get collapsed into one when somebody asks what an injury lawyer costs in Modesto. What does California allow a fee to be. Which published percentages belong to other kinds of cases. And what does the Stanislaus County Superior Court collect along the way. Each has a documented answer, and only the first one has no number attached."""

BODY = """### Question one: what does California allow

Rule 1.5(a) of the California Rules of Professional Conduct states the whole standard in a single line: an attorney is barred from agreeing to, charging or collecting any unconscionable or illegal fee. No schedule follows, and no percentage for ordinary negligence work appears anywhere in the rule.

Rule 1.5(b) explains how unconscionability gets tested. It is judged on all the facts existing at the time the agreement was entered into, except where the parties contemplated later events affecting the fee, and thirteen listed circumstances feed the analysis: fraud or overreaching in setting the fee, failure to disclose material facts, the fee measured against the value of services actually performed, the relative sophistication of lawyer and client, the amount involved and results obtained, time and labor required, whether the fee is fixed or contingent, and informed consent.

Two consequences matter for anyone comparing arrangements along McHenry Avenue. The percentage is negotiable, and the review looks backward at the moment of signature. Rule 1.5(c) adds two flat prohibitions that show what a genuine ban looks like when California means one: no contingent fee in a family law dissolution or support matter, and, in subdivision (c)(2), none for representing a defendant in a criminal case. Injury claims appear on neither list.

### Question two: whose percentages are those

Three California provisions print numbers, and none of them governs a Modesto crash or fall.

Business and Professions Code section 6146 sets a ceiling for actions against a health care provider based on professional negligence: twenty-five percent of the amount recovered where the claim resolves before a complaint or arbitration demand is filed, thirty-three percent afterward, and more only on a good-cause motion. The base is the net sum after disbursements. Medical negligence is its entire scope.

Labor Code section 4906 covers workers' compensation. A comp fee is unenforceable beyond what the appeals board finds reasonable, and no attorney may demand or accept payment from an injured worker until that board has approved or fixed the sum. Within ten days of execution the agreement is submitted for review, and the board looks at what responsibility the attorney took on, the care shown, the hours consumed and what the worker recovered, while a disclosure form sets out the range of fees customarily approved. Section 6147(c) excludes compensation contracts from the contingency contract statute altogether.

Civil Code section 3045.4 is the third and most frequently misread. A hospital holding a lien can reach the payor for the lien amount, or so much as can be satisfied out of 50 percent of the money due under a final judgment, compromise or settlement after prior liens are paid. That figure limits what the hospital takes from the injured person's recovery, not what a lawyer charges.

### Question three: what the Modesto courthouse collects

The Stanislaus County Superior Court posts the statewide civil fee schedule for its Modesto filings, so the amounts are public and identical for every litigant. Where the demand exceeds $10,000 but stays at or under $35,000, the first paper is $370, and the responding party pays $370 as well. At or below $10,000 both are $225. Anything pleading more than $35,000 is unlimited civil.

The schedule also prices the middle of a case. Amending a complaint to raise the amount at issue is $145. Reclassifying a limited case as unlimited, which happens when discovery shows the injuries are worse than the first pleading assumed, is $140. Any motion or other paper requiring a hearing is $60, summary judgment or summary adjudication is $500, and the advance jury fee is $150 with later daily juror deposits set by the court. Court reporting is $30 for a hearing of an hour or less and shifts to a $700 full-day or $350 half-day per diem beyond that. Two items on the schedule do not apply here at all: the courthouse construction surcharges printed on it are collected only in Riverside, San Bernardino and San Francisco filings.

### Where the contract has to be explicit

Section 6147(a) requires the contingency agreement to be written and signed by both sides, with a duplicate given to the plaintiff at signing, stating the rate, the effect of disbursements and costs on the fee and the recovery, any compensation owed for related matters, and, outside section 6146 claims, that the fee is not set by law but is negotiable. Subsection (b) makes noncompliance voidable at the plaintiff's option, leaving a reasonable fee.

The cost-and-fee interaction is the practical heart of that list. Suppose a file carries $6,000 in records, deposition and filing expenses. Taking those off the recovery first and applying the percentage to what remains leaves the client a different number than applying the percentage first and reimbursing afterward. Both are lawful, and the contract has to say which one applies.

### Worth pinning down before signature in Stanislaus County

Confirm the rate at each stage in writing, including any change once a complaint is filed. Confirm the deduction order for expenses. Confirm who advances the jury fee, a reporter per diem or an expert retainer, and what happens to those advances if the case ends without a recovery. Confirm how a hospital or health plan lien gets handled before disbursement. And confirm the negotiability statement is present, since its absence is itself a defect the client can act on."""

root = pathlib.Path("/home/user/workspace/local-sites/sites/modestopersonalinjurylawyerpros.com")
p = root / "site.json"
d = json.loads(p.read_text())
d["pricing"] = pricing
p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
c = root / "copy.md"
t = c.read_text().split("## pricing_lede")[0].rstrip("\n")
t += "\n\n## pricing_lede\n\n" + LEDE + "\n\n## pricing_body\n\n" + BODY + "\n"
c.write_text(t)
print("ok")
