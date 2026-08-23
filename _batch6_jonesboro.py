import json, pathlib

RPC = "https://law.justia.com/cases/arkansas/supreme-court/2016/2016-ark-286.html"
CONST = "https://law.justia.com/constitution/arkansas/article-5/section-32/"
WC = "https://law.justia.com/codes/arkansas/title-11/chapter-9/subchapter-7/section-11-9-715/"
FILING = "https://law.justia.com/codes/arkansas/title-21/chapter-6/subchapter-4/section-21-6-403/"
SHERIFF = "https://law.justia.com/codes/arkansas/title-21/chapter-6/subchapter-3/section-21-6-307/"
CLERK = "https://www.craigheadcircuitclerk.com/filling-fees"
COUNTY = "https://craigheadcountyar.gov/transparency/craighead-county-fees"

pricing = {
  "mode": "fees",
  "fee_kind": "contingency",
  "table_head": "Published Arkansas figures behind a Craighead County injury claim, and the blank where a fee cap would be",
  "col_a": "What somebody is asking about",
  "col_b": "What Arkansas has written down",
  "anchors": [
    {
      "label": "Ceiling on an injury contingency percentage",
      "value": "Arkansas sets none",
      "detail": "The rule requires only that a fee be reasonable, and gives eight factors for measuring that. No Arkansas statute assigns a percentage to a negligence recovery.",
      "source_name": "Ark. R. Prof. Conduct 1.5(a)",
      "source_url": RPC,
    },
    {
      "label": "Opening a civil case, Craighead County Circuit Clerk",
      "value": "$167.50",
      "detail": "The clerk's published amount for initiating a cause of action including the initial summons, built on the $150.00 statutory base. The county's own fee page lists $165.00 for the same line.",
      "source_name": "Craighead County Circuit Clerk filing fees",
      "source_url": CLERK,
    },
    {
      "label": "Legislated limit on an injury or death recovery",
      "value": "Constitutionally forbidden",
      "detail": "Article 5 says that apart from workers' compensation, no law shall be enacted limiting the amount to be recovered for injuries resulting in death or for injuries to persons or property.",
      "source_name": "Ark. Const. art. 5, sec. 32",
      "source_url": CONST,
    },
    {
      "label": "The only Arkansas fee percentage, and it is workers' compensation",
      "value": "25% of indemnity benefits",
      "detail": "Valid only with Workers' Compensation Commission approval, and on a controverted claim the carrier pays half of it on top of the benefits while the claimant pays the other half.",
      "source_name": "Ark. Code Ann. 11-9-715(a)(1)(B)",
      "source_url": WC,
    },
  ],
  "fee_rows": [
    {
      "stage": "Share of a Jonesboro injury recovery",
      "share": "Negotiated, reviewed for reasonableness",
      "note": "The eight factors weigh time and labor, difficulty, the fee customarily charged locally, the amount involved and results obtained, the length of the relationship, and whether payment is contingent.",
      "source_name": "Ark. R. Prof. Conduct 1.5(a)",
      "source_url": RPC,
    },
    {
      "stage": "Any engagement likely to produce a fee above this",
      "share": "$1,000.00",
      "note": "Above that figure the agreement must be confirmed in writing and must state the method by which sums due to the lawyer will be calculated.",
      "source_name": "Ark. R. Prof. Conduct 1.5(b)(2)",
      "source_url": RPC,
    },
    {
      "stage": "Content of the contingent agreement",
      "share": "Writing, with percentages named",
      "note": "It states the percentages accruing on settlement, trial and appeal, the expenses deducted, whether that happens before or after the fee, and a closing written statement follows.",
      "source_name": "Ark. R. Prof. Conduct 1.5(c)",
      "source_url": RPC,
    },
    {
      "stage": "Compensation appeal fees, a separate system",
      "share": "$500 and $1,000 maximums",
      "note": "Five hundred dollars on appeal to the full Commission and one thousand on appeal to the Court of Appeals or Supreme Court, with a $200 change-of-physician fee alongside.",
      "source_name": "Ark. Code Ann. 11-9-715(b)(2)",
      "source_url": WC,
    },
    {
      "stage": "Sheriff serving a summons or subpoena",
      "share": "$30.00 each",
      "note": "Charged for every person named unless several are served at one location, with $20.00 to return the paper and $100.00 for a writ of execution.",
      "source_name": "Ark. Code Ann. 21-6-307(a)(1)",
      "source_url": SHERIFF,
    },
    {
      "stage": "Reopening a closed circuit court case",
      "share": "$50.00",
      "note": "Set statewide by statute, matching the transfer fee, and the county government page lists the same amount for a reopening.",
      "source_name": "Ark. Code Ann. 21-6-403(b)(3)",
      "source_url": FILING,
    },
  ],
}

LEDE = """Arkansas measures a legal fee instead of capping one. The state constitution goes further and blocks the legislature from limiting what an injured person can recover at all. That leaves a Jonesboro claim governed by a reasonableness rule, a written agreement, a clerk's fee list, and one 25 percent figure that belongs to workers' compensation and to nothing else."""

BODY = """### Reasonable, not capped

Rule 1.5(a) of the Arkansas Rules of Professional Conduct is short. A lawyer's fee shall be reasonable, and no lawyer may agree to, charge or collect either an unreasonable fee or an unreasonable amount for expenses. Eight factors define reasonable: time and labor with the skill the work demands, whether the engagement precludes other employment, the customary local charge for comparable service, the sum at stake alongside the outcome achieved, deadlines the client or the situation imposes, how long the professional relationship has run, the experience and ability of the lawyers involved, and whether payment is fixed or contingent.

There is no ninth factor stating a number. Anyone who says Arkansas allows a certain percentage on injury claims is quoting a habit of the local market, not the rule.

### The constitution closes the door the other way too

Article 5, section 32 of the Arkansas Constitution, as amended, lets the General Assembly fix compensation amounts for injured workers, then adds a clause that shapes the rest of injury law here: otherwise no law shall be enacted limiting the amount to be recovered for injuries resulting in death or for injuries to persons or property. Arkansas accordingly has no noneconomic damages cap and no legislated fee schedule for negligence claims. What a case is worth is a question of proof.

### The one percentage in Arkansas fee law, and where it lives

Section 11-9-715 covers attorney fees in workers' compensation claims and is the source of every 25 percent figure quoted in this state. Fees in a compensation claim are not valid unless approved by the Workers' Compensation Commission, and they run twenty-five percent of compensation for indemnity benefits, with no fee on medical benefits except in one narrow situation.

Who pays that 25 percent depends on whether the claim was fought. On a controverted claim the employer or carrier pays half in addition to the compensation awarded, and the claimant pays the other half out of compensation. On an uncontroverted claim the Commission may allow a fee not exceeding twenty-five percent, paid by the claimant. Appeals add ceilings: $500 more before the full Commission and $1,000 before the appellate courts. A change-of-physician request carries a $200 fee.

Every line of that governs a claim before the Commission. A collision on Highland Drive, a fall in a Jonesboro store or a truck crash on Interstate 555 is a negligence case in circuit court, and none of those ceilings reaches it.

### What has to be in writing

Rule 1.5(b)(1) requires scope and the basis or rate of the fee and expenses to be communicated, preferably in writing, before or soon after the work begins, with later changes communicated too. Rule 1.5(b)(2) adds an Arkansas-specific trigger: any agreement likely to produce a total fee above $1,000.00, or any retainer above it, must be confirmed in writing stating how sums due will be calculated. Nearly every injury engagement clears that threshold.

Rule 1.5(c) then governs contingency. The agreement is in writing, states the method of determining the fee including the percentages accruing on settlement, at trial and on appeal, identifies the expenses deducted from the recovery, and says whether they come off before or after the fee is calculated. It must notify the client clearly of expenses owed whether or not the client prevails, and a written statement of outcome and remittance follows at the conclusion. Rule 1.5(f) presumes, absent a contrary writing, that funds paid to a lawyer are advances held in trust until earned. Rule 1.5(d) bars contingency in divorce-linked matters and for a criminal defendant.

### The Craighead County numbers

Arkansas fixes circuit court filing fees by statute rather than by county. Section 21-6-403(b)(1) prices initiating a cause of action in circuit court, including appeals, at $150.00, with reopening and transfer at $50.00 each, no partial refunds, an exemption for a party proceeding in forma pauperis under Rule 72, and a bar on county-added filing fees.

Two local totals sit above that base. The Craighead County Circuit Clerk lists $167.50 to initiate a civil, domestic, foreign-judgment or appeal case including the initial summons. The county government's fee page lists $165.00 for the same item, citing the same statute. That $2.50 gap is worth confirming with the clerk on the day of filing. Both pages agree on smaller items: $140.00 to have a civil process server appointed, $50.00 to renew it, $2.50 for a summons or subpoena.

Service through the sheriff is priced in section 21-6-307: $30.00 to serve a summons, subpoena or writ of garnishment, $20.00 to return one, $30.00 to serve an order or notice of the court, and $100.00 for a writ of execution. Those charges apply per person named unless several are served at the same location, which matters when a trucking defendant, its driver and a registered agent all need papers.

### What to settle before signing in Jonesboro

Get the settlement, trial and appeal percentages written separately. Establish whether costs come off before or after the fee is computed, since the sequence changes the net. Establish who fronts a deposition, an expert or the filing fee, and whether that money is owed back if nothing is recovered. Ask when the closing statement arrives and what it shows. Ask whether another firm shares the fee, which Rule 1.5(e) permits only in proportion to services performed or with joint responsibility by written agreement."""

root = pathlib.Path("/home/user/workspace/local-sites/sites/jonesboropersonalinjurylawyerpros.com")
p = root / "site.json"
d = json.loads(p.read_text())
d["pricing"] = pricing
p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
c = root / "copy.md"
t = c.read_text().split("## pricing_lede")[0].rstrip("\n")
t += "\n\n## pricing_lede\n\n" + LEDE + "\n\n## pricing_body\n\n" + BODY + "\n"
c.write_text(t)
print("ok")
