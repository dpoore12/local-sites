import json, pathlib

RPC = "https://www.ncbar.gov/for-lawyers/ethics/rules-of-professional-conduct/rule-15-fees/"
G621 = "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_6/GS_6-21.1.html"
G4450 = "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_44/GS_44-50.html"
G7A305 = "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_7A/GS_7A-305.html"
G108A = "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_108A/GS_108A-57.html"
G9021 = "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_90/GS_90-21.19.html"
G9790 = "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_97/GS_97-90.html"

pricing = {
  "mode": "fees",
  "fee_kind": "contingency",
  "table_head": "The figures North Carolina publishes for a Cabarrus County injury claim, and the one it leaves blank",
  "col_a": "Item under discussion",
  "col_b": "Where the number comes from",
  "anchors": [
    {
      "label": "Statutory percentage for an injury contingency",
      "value": "There is none",
      "detail": "The State Bar rule bars a clearly excessive fee and gives eight factors for testing one. No North Carolina statute or rule assigns a percentage to a negligence recovery.",
      "source_name": "N.C. Rev. R. Prof. Conduct 1.5(a)",
      "source_url": RPC,
    },
    {
      "label": "General Court of Justice fee, superior court civil action",
      "value": "$180",
      "detail": "Paid to the Clerk of Superior Court in Concord when the complaint is filed, alongside a $16 facilities fee and a $4.00 telecommunications and data connectivity charge.",
      "source_name": "N.C. Gen. Stat. 7A-305(a)(2)",
      "source_url": G7A305,
    },
    {
      "label": "Fee a judge can tax against an insurer that refused to negotiate",
      "value": "$10,000 maximum",
      "detail": "Available where damages recovered are $25,000 or less and the recovery beat the highest offer made ninety days before trial. It adds money for the injured side.",
      "source_name": "N.C. Gen. Stat. 6-21.1(a)",
      "source_url": G621,
    },
    {
      "label": "Ceiling on a medical provider's lien, not on a lawyer's fee",
      "value": "50% of damages recovered",
      "detail": "Measured exclusive of attorneys' fees, and the statute says nothing in it interferes with amounts due for attorney's services. It limits what doctors and hospitals claim.",
      "source_name": "N.C. Gen. Stat. 44-50",
      "source_url": G4450,
    },
  ],
  "fee_rows": [
    {
      "stage": "The contingency percentage in a Concord injury claim",
      "share": "Set by agreement, tested for excess",
      "note": "The eight factors include the customary charge in this locality, the amount involved and the result, the skill required, and whether the arrangement was fixed or contingent.",
      "source_name": "N.C. Rev. R. Prof. Conduct 1.5(a)",
      "source_url": RPC,
    },
    {
      "stage": "Documents the arrangement requires",
      "share": "Client-signed writing, plus a closing statement",
      "note": "The agreement states the percentages on settlement, trial and appeal, which expenses are deducted, and when. At the end the lawyer furnishes a written statement of outcome and remittance.",
      "source_name": "N.C. Rev. R. Prof. Conduct 1.5(c)",
      "source_url": RPC,
    },
    {
      "stage": "Filing a notice of hearing on a motion",
      "share": "$20 per motion",
      "note": "Charged for motions not already priced in the clerk's separate schedule, and assessed once for each motion rather than once for the case.",
      "source_name": "N.C. Gen. Stat. 7A-305(f)",
      "source_url": G7A305,
    },
    {
      "stage": "Recovering the cost of a private process server",
      "share": "Actual cost or $50, whichever is less",
      "note": "The lower figure controls unless the court makes a finding that serving that defendant was difficult. Expert witness charges are assessable only for time actually spent testifying.",
      "source_name": "N.C. Gen. Stat. 7A-305(d)(6)",
      "source_url": G7A305,
    },
    {
      "stage": "A Medicaid claim reaching into the settlement",
      "share": "One-third of gross recovery presumed",
      "note": "That presumption applies where the agency's claim exceeds a third, and the injured person may dispute it by application within thirty days under a clear and convincing standard.",
      "source_name": "N.C. Gen. Stat. 108A-57(a1)",
      "source_url": G108A,
    },
    {
      "stage": "Malpractice noneconomic damages, a different case type",
      "share": "$500,000, adjusted for inflation",
      "note": "Applies to claims against health care providers, resets every third year by consumer price index, and disappears entirely where disfigurement or death meets reckless conduct.",
      "source_name": "N.C. Gen. Stat. 90-21.19(a)",
      "source_url": G9021,
    },
  ],
}

LEDE = """Anyone injured on Church Street or on Concord Parkway hears percentages quoted with great confidence. North Carolina supplies none of them. The state supplies a standard, a required writing, a clerk's cost schedule that applies to everybody, and several published limits that belong to medical bills and other case types rather than to the fee."""

BODY = """### Start with the rule that has no number in it

Rule 1.5(a) of the North Carolina Rules of Professional Conduct forbids any lawyer from making an agreement for, charging, or collecting a fee that is illegal or clearly excessive, then hands over eight factors for measuring that second phrase. They cover the labor and skill the matter demanded, the difficulty of what was disputed, whether the engagement cost the lawyer other work, the fee customarily charged around Cabarrus County for comparable service, the sum at stake and the outcome reached, the deadlines involved, the history between lawyer and client, and whether payment was fixed or contingent.

Rule 1.5(b) adds that scope and the basis of the fee are communicated, preferably in writing, before or within a reasonable time after the work begins. A percentage introduced as the state's standard rate has no statutory backing.

### The paperwork requirement is specific about content

Under Rule 1.5(c) a contingent arrangement has to be in writing and signed by the client. The writing states the method by which the fee is determined, including the separate percentages that accrue on settlement, at trial and on appeal, and identifies the expenses deducted from the recovery plus whether those deductions happen before or after the fee is calculated. It also notifies the client clearly about any expense owed regardless of who prevails.

The rule then governs the ending. When the matter concludes, the lawyer provides a written statement setting out the result and, where money came in, showing the remittance and how it was determined. Rule 1.5(d)(1) separately forbids a contingent fee for representing a criminal defendant, and (d)(2) forbids one wherever law prohibits it.

### The famous 50 percent figure caps the hospital, not the lawyer

General Statute 44-50 is the most misquoted provision in North Carolina injury practice. It gives physicians, dentists, nurses, hospitals and ambulance services a lien on funds recovered by an injured person. Two sentences settle what the 50 percent means. One says nothing in the section shall be construed to interfere with any amount due for attorney's services. The other says the lien, exclusive of attorneys' fees, shall in no case exceed fifty percent of the damages recovered.

So the ceiling governs how much of a recovery treating providers can absorb, computed after the fee is set aside. Read as a limit on legal fees, it describes something the statute never said.

Medicaid follows separate arithmetic. Under 108A-57(a1), where the agency's claim exceeds a third of the gross recovery, a third of that gross is presumed to represent the claim, and (a2) lets the beneficiary contest that presumption within thirty days.

### Cabarrus County court costs come from a statute, not a local list

Cabarrus County publishes no civil filing prices of its own. Costs in a Concord case are the General Court of Justice amounts in General Statute 7A-305, collected by the Clerk of Superior Court: $180 in superior court, $130 in district court, $80 before a magistrate, plus a $16 facilities fee and $4.00 for the Court Information Technology Fund. Subsection (c) has the clerk collect advance costs at filing.

Subsection (d) is an exclusive list of assessable expenses. Deposition transcripts are on it. Private process servers are on it, recoverable at actual cost or $50, whichever is less, unless the court finds service proved difficult. Expert witness fees are on it but limited to time actually spent testifying, so file review and travel stay with the party who hired the expert. Subsection (f) prices a notice of hearing on a motion at $20.

### Two places where somebody other than the client decides a fee

General Statute 6-21.1 lets a judge tax reasonable attorneys' fees as costs against a losing defendant or insurer on a finding of unwarranted refusal to negotiate or pay. Three conditions gate it: damages recovered of $25,000 or less, a recovery exceeding the highest offer made at least ninety days before trial, and a written order with findings. The award cannot exceed $10,000, and it moves money toward the injured party rather than restricting the fee contract.

Workers' compensation runs differently. Under 97-90(a) compensation attorney fees are subject to Industrial Commission approval, and (c) requires the agreement filed before the hearing closes, approved unless found unreasonable, with appeals to the full Commission and then a superior court judge. That subsection also says the Commission has no jurisdiction over fees in any third-party action, which puts a liability claim outside the approval process.

### A malpractice cap that never touches a crash file

General Statute 90-21.19(a) limits noneconomic damages against a health care provider to $500,000, adjusted every third year by consumer price index, and (b) lifts the limit where disfigurement, permanent injury or death meets reckless conduct. It caps damages in a professional negligence case and says nothing about a fee.

### Before signing anything in Concord

Ask which percentage attaches at settlement, at trial and on appeal, and confirm all three appear in the writing. Ask whether expenses come off before or after the fee is figured. Ask who advances a records subpoena, a reconstruction or a treating physician's deposition, and whether that money is owed back if nothing is recovered. Ask how provider liens and any Medicaid claim get negotiated before disbursement. A fee arrangement that cannot be described on paper is not worth signing."""

root = pathlib.Path("/home/user/workspace/local-sites/sites/concordpersonalinjurylawyer.com")
p = root / "site.json"
d = json.loads(p.read_text())
d["pricing"] = pricing
p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
c = root / "copy.md"
t = c.read_text().split("## pricing_lede")[0].rstrip("\n")
t += "\n\n## pricing_lede\n\n" + LEDE + "\n\n## pricing_body\n\n" + BODY + "\n"
c.write_text(t)
print("ok")
