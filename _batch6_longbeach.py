import json, pathlib

BAR = "https://www.calbar.ca.gov/legal-professionals/rules/rules-professional-conduct/current-rules-professional-conduct/chapter-1-lawyer-client-relationship"
S6147 = "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=6147.&lawCode=BPC"
S6146 = "https://law.justia.com/codes/california/code-bpc/division-3/chapter-4/article-8-5/section-6146/"
LASC = "https://lascpubstorage.blob.core.windows.net/cpw/LIBSVCExecutiveSupport-265-2024FeeSchedule010124.pdf"
LAB = "https://law.justia.com/codes/california/code-lab/division-4/part-3/chapter-1/section-4906/"

pricing = {
  "mode": "fees",
  "fee_kind": "contingency",
  "table_head": "What the contract has to say in a Long Beach injury claim, and what the Los Angeles courthouse collects",
  "col_a": "Document or filing",
  "col_b": "What the statute or schedule requires",
  "anchors": [
    {
      "label": "Sentence the contract itself must contain",
      "value": "The fee is negotiable",
      "detail": "Outside medical negligence claims, California requires a contingency contract to state that the fee is not set by law but is negotiable between attorney and client.",
      "source_name": "Cal. Bus. & Prof. Code 6147(a)(4)",
      "source_url": S6147,
    },
    {
      "label": "Percentage ceiling on an ordinary injury fee",
      "value": "Not stated anywhere",
      "detail": "The State Bar rule prohibits an unconscionable or illegal fee and supplies thirteen factors for testing one. It assigns no percentage to a negligence recovery.",
      "source_name": "Cal. Rules of Prof. Conduct, rule 1.5(a)-(b)",
      "source_url": BAR,
    },
    {
      "label": "First paper where the claim stays at or under $12,500",
      "value": "$225",
      "detail": "The Los Angeles Superior Court draws its limited-civil line at $12,500 rather than the $10,000 figure printed on schedules elsewhere in California.",
      "source_name": "LASC Civil Fee Schedule, item 13",
      "source_url": LASC,
    },
    {
      "label": "Electronic filing service fee, charged per transaction",
      "value": "$2.25",
      "detail": "Added to each eFiling transaction in Los Angeles civil cases under the Rules of Court provisions governing electronic filing and service.",
      "source_name": "LASC Civil Fee Schedule, item 280",
      "source_url": LASC,
    },
  ],
  "fee_rows": [
    {
      "stage": "The contingency share in a Long Beach injury claim",
      "share": "No statutory percentage",
      "note": "Unconscionability is judged on the facts existing when the agreement was made, weighing proportion to the value of services, relative sophistication, results obtained, and informed consent.",
      "source_name": "Cal. Rules of Prof. Conduct, rule 1.5(b)",
      "source_url": BAR,
    },
    {
      "stage": "Form of the contingency contract",
      "share": "Duplicate signed copy at signing",
      "note": "It states the rate, how disbursements and costs affect both the fee and the recovery, compensation for related matters, and the negotiability statement.",
      "source_name": "Cal. Bus. & Prof. Code 6147(a)",
      "source_url": S6147,
    },
    {
      "stage": "A contract that leaves out a required term",
      "share": "Voidable by the plaintiff",
      "note": "The client may void it, after which the attorney is entitled only to a reasonable fee rather than the percentage the contract named.",
      "source_name": "Cal. Bus. & Prof. Code 6147(b)",
      "source_url": S6147,
    },
    {
      "stage": "Claims against a health care provider, a different statute",
      "share": "25% before filing, 33% after",
      "note": "That schedule governs professional negligence actions against health care providers only, and higher rates require a motion showing good cause.",
      "source_name": "Cal. Bus. & Prof. Code 6146(a)",
      "source_url": S6146,
    },
    {
      "stage": "Workers' compensation fees, a separate track",
      "share": "Approved by the appeals board first",
      "note": "No fee may be demanded or accepted from an injured employee until the appeals board approves or sets the amount, and the contingency contract statute excludes comp.",
      "source_name": "Cal. Lab. Code 4906(b)",
      "source_url": LAB,
    },
    {
      "stage": "Dividing the fee with another firm",
      "share": "Written client consent required",
      "note": "The lawyers need a written agreement, the client consents in writing after full written disclosure, and the total fee cannot rise because of the division.",
      "source_name": "Cal. Rules of Prof. Conduct, rule 1.5.1(a)",
      "source_url": BAR,
    },
  ],
}

LEDE = """California handles injury fees by regulating the contract rather than the number. One statute dictates what the written agreement has to say, including a sentence telling the client the fee is negotiable. A State Bar rule supplies the test the fee has to survive. And the Los Angeles Superior Court publishes every court amount a Long Beach case will encounter."""

BODY = """### The statute writes part of the contract for you

Business and Professions Code section 6147 governs any contingency agreement a plaintiff signs in this state. Subsection (a) requires a written contract signed by both attorney and client, with a duplicate copy handed to the plaintiff when it is entered into. Four items must appear: the contingency rate, how disbursements and costs affect both the fee and the recovery, how far the client might owe compensation on related matters lying outside the contract, and, unless section 6146 governs the claim, a statement telling the client that this fee is negotiable between the parties rather than fixed by law.

That last requirement is the one worth reading twice. The legislature ordered the disclosure precisely because clients assume a standard rate exists. Where section 6146 does apply, subsection (a)(5) requires a different statement: that those statutory rates are maximum limits and a lower rate may be negotiated.

Subsection (b) provides the enforcement. A contract that fails to comply is voidable at the plaintiff's option, and the attorney is then entitled to a reasonable fee rather than the agreed share. Subsection (c) removes workers' compensation representation from the section entirely.

### What stands in for a cap

Under the California Rules of Professional Conduct, rule 1.5(a) forbids a fee that is unconscionable or illegal. Rule 1.5(b) then measures unconscionability against all facts existing when the agreement was entered into, unless later events affecting the fee were contemplated, and supplies thirteen factors. They include overreaching or fraud during the fee negotiation, material facts left undisclosed, proportion between the fee and the value of work performed, how sophisticated each side was, the sum at issue with the result achieved, hours and effort expended, contingency versus a fixed charge, and the client's informed consent.

Nothing in that list is a percentage, so a rate quoted as California's standard is a market convention that still has to survive the thirteen-factor review.

### The percentages that do exist belong elsewhere

Section 6146 caps contingency fees in actions against health care providers based on professional negligence, at twenty-five percent of the amount recovered where the matter resolves before a complaint or arbitration demand is filed and thirty-three percent afterward, with anything higher requiring a motion supported by good cause. Those numbers are quoted constantly at people whose claims have nothing to do with them. A rear-end impact on Pacific Coast Highway, a fall inside a Long Beach market, a bicycle struck near the port entrance, a delivery van running a light on Atlantic Avenue: all ordinary negligence, none of it section 6146 territory.

Workers' compensation is the other separate track. Labor Code section 4906 makes a comp fee unenforceable above a reasonable amount and bars any attorney from demanding or accepting payment from an injured employee before the appeals board approves or fixes the sum. That agreement reaches the board inside ten days, and the board weighs the responsibility taken on, the care shown, the hours spent and what the worker ultimately obtained. The section names no percentage.

### The Los Angeles Superior Court's published amounts

Long Beach civil filings are handled at the Governor George Deukmejian Courthouse, under the fee schedule the Los Angeles Superior Court publishes for the whole county. A first paper in an unlimited civil case, meaning one pleading more than $35,000, is $435, and each other party pays the same amount on its first appearance. Where the claim exceeds $12,500 but not $35,000, the first paper is $370. At or under $12,500 it is $225. That $12,500 dividing line is a Los Angeles particularity worth noting, because schedules in other counties still print $10,000 on the equivalent line.

From there the schedule prices the litigation. A motion or other paper requiring a hearing is $60, and summary judgment or summary adjudication is $500. An order authorizing service by posting or publication is $20. The advance jury fee, nonrefundable and forfeiting the jury if nobody posts it, is $150, with later daily deposits of $15 per juror plus $0.34 per mile one way. A complex designation adds $1,000 for the plaintiffs collectively and $1,000 per defendant, capped at $18,000. Electronic filing adds $2.25 per transaction, a returned check draws $65, and a partial payment draws $25.

### Costs and the fee are two different subtractions

Court fees, deposition transcripts, service of process, medical records and expert retainers are third-party expenses, distinct from the percentage. Section 6147(a)(2) exists because the interaction decides what an injured person receives: a fee computed on the gross with costs taken afterward yields a different net than costs taken first. The contract must describe the mechanism, so it can be discussed before signature rather than at disbursement.

A related point often surfaces late. If a firm associates in another firm, rule 1.5.1 permits the division only with a written agreement between the lawyers, the client's written consent given after full written disclosure, and no increase in the total charged because of the arrangement.

### Questions to raise at the first Long Beach meeting

Which percentage applies before a complaint is filed, which after, and which on appeal. Are costs deducted before or after the fee is calculated. Who advances the jury fee, a summary judgment fee or an expert retainer, and is any of it owed back if the claim fails. Does the contract contain the negotiability sentence section 6147 requires. Will another firm share the fee, disclosed in writing. The answers belong on the copy handed over at signing."""

root = pathlib.Path("/home/user/workspace/local-sites/sites/longbeachpersonalinjurylawyerpros.com")
p = root / "site.json"
d = json.loads(p.read_text())
d["pricing"] = pricing
p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
c = root / "copy.md"
t = c.read_text().split("## pricing_lede")[0].rstrip("\n")
t += "\n\n## pricing_lede\n\n" + LEDE + "\n\n## pricing_body\n\n" + BODY + "\n"
c.write_text(t)
print("ok")
