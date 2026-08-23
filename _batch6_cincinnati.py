import json, pathlib

RULES = "https://www.supremecourt.ohio.gov/docs/LegalResources/Rules/ProfConduct/profConductRules.pdf"
RC4705 = "https://codes.ohio.gov/ohio-revised-code/section-4705.15"
RC2315 = "https://codes.ohio.gov/ohio-revised-code/section-2315.18"
RC1901 = "https://codes.ohio.gov/ohio-revised-code/section-1901.17"
RC4123 = "https://codes.ohio.gov/ohio-revised-code/section-4123.512"
HAM = "https://hamiltoncountycourts.org/wp-content/uploads/2016/02/Municipal_Civil_Rule_18.pdf"

pricing = {
  "mode": "fees",
  "fee_kind": "contingency",
  "table_head": "What Ohio law settles in a Hamilton County injury claim, and what stays inside the signed agreement",
  "col_a": "The piece being decided",
  "col_b": "What Ohio actually sets",
  "anchors": [
    {
      "label": "Percentage limit on an injury contingency",
      "value": "None in the rule",
      "detail": "Ohio's fee rule forbids an illegal or clearly excessive fee and lists eight factors for judging one. It prints no percentage for a negligence claim in Cincinnati or anywhere else in the state.",
      "source_name": "Ohio Prof. Cond. R. 1.5(a)",
      "source_url": RULES,
    },
    {
      "label": "Ceiling on noneconomic damages in a tort claim",
      "value": "$250,000 or three times economic loss",
      "detail": "Whichever of the two is greater, and never above $350,000 for one plaintiff or $500,000 for one occurrence. Economic loss is not limited at all, and catastrophic injuries are exempt.",
      "source_name": "Ohio Rev. Code 2315.18(B)(2)",
      "source_url": RC2315,
    },
    {
      "label": "Filing a civil suit, Hamilton County Municipal Court",
      "value": "$90",
      "detail": "Collected when the complaint is docketed, with service billed separately at $30 for personal or residential service and $10 for certified mail.",
      "source_name": "Hamilton County Municipal Court Civil Rule XVIII",
      "source_url": HAM,
    },
    {
      "label": "Jury deposit in that same court",
      "value": "$300",
      "detail": "Posted before a civil jury is seated, on top of a $10 charge for filing the jury demand itself. A motion costs $5 and a subpoena $6.",
      "source_name": "Hamilton County Municipal Court Civil Rule XVIII",
      "source_url": HAM,
    },
  ],
  "fee_rows": [
    {
      "stage": "Share of an injury recovery",
      "share": "No percentage set by law",
      "note": "Judged against eight factors: time and labor, difficulty, the charge customary in this locality, the amount involved and result, deadlines, the relationship, standing, and whether the arrangement is contingent.",
      "source_name": "Ohio Prof. Cond. R. 1.5(a)",
      "source_url": RULES,
    },
    {
      "stage": "Form the contingent agreement must take",
      "share": "Signed writing, percentages spelled out",
      "note": "It must give the method, the separate percentages for settlement, trial and appeal, the litigation expenses being deducted, and whether they come off before or after the fee is computed.",
      "source_name": "Ohio Prof. Cond. R. 1.5(c)(1)",
      "source_url": RULES,
    },
    {
      "stage": "Accounting owed when money arrives",
      "share": "Signed closing statement",
      "note": "Ohio statute requires one in every tort matter, showing how the compensation was figured, which costs and expenses were taken out, and any proposed division with referring counsel.",
      "source_name": "Ohio Rev. Code 4705.15(C)",
      "source_url": RC4705,
    },
    {
      "stage": "Contingent fee for a criminal defendant",
      "share": "Not allowed",
      "note": "Ohio bars it outright, alongside contingent fees in domestic relations matters. The prohibition has nothing to do with injury work and is often confused with one.",
      "source_name": "Ohio Prof. Cond. R. 1.5(d)(2)",
      "source_url": RULES,
    },
    {
      "stage": "Workers' compensation appeal fee taxed to an employer",
      "share": "$5,000 maximum",
      "note": "This dollar limit lives in the compensation appeal statute and applies when a claimant wins in common pleas. It is not a limit on a negligence contingency.",
      "source_name": "Ohio Rev. Code 4123.512(F)",
      "source_url": RC4123,
    },
    {
      "stage": "Dollar line between the two Cincinnati courthouses",
      "share": "$15,000",
      "note": "Municipal court original jurisdiction stops there, so a larger claim is filed in common pleas and draws that court's own deposit schedule instead.",
      "source_name": "Ohio Rev. Code 1901.17",
      "source_url": RC1901,
    },
  ],
}

LEDE = """Ohio never wrote down what a share of an injury recovery is allowed to be. What the state did write down is the test a fee has to survive afterward, the two documents that have to exist around it, a ceiling on one category of damages, and the amounts the Hamilton County courthouse collects from every plaintiff alike."""

BODY = """### Nowhere in the Ohio rule is there a percentage

Professional Conduct Rule 1.5(a) opens with a prohibition rather than a schedule: a lawyer shall not make an agreement for, charge, or collect an illegal or clearly excessive fee. The rule then defines the second phrase by describing a reader, not a number. A fee is clearly excessive when a lawyer of ordinary prudence, reviewing the facts, would be left with a definite and firm conviction that the fee exceeded a reasonable one.

Eight factors decide that: time and labor and the difficulty of the questions, whether the case shut out other work, the fee customarily charged in the locality for similar service, the amount involved and the result obtained, time limits imposed by the client or by circumstances, the length of the professional relationship, the experience and ability of the lawyer, and whether the fee was fixed or contingent.

Not one of those is a percentage. Any figure recited as "the Ohio rate" for a Hamilton County collision or a fall at a Norwood store describes local habit rather than state law.

### The limit Ohio did legislate sits on damages

Revised Code 2315.18 caps one slice of a tort recovery. Noneconomic damages, meaning pain, suffering and loss of enjoyment, are limited to the greater of $250,000 or three times economic loss, and that computation can never produce more than $350,000 for a single plaintiff or $500,000 for a single occurrence. Economic loss itself, under (B)(1), carries no limit whatsoever: medical bills, lost earnings and future care are proved for what they are worth.

Subdivision (B)(3) then removes the cap entirely for the worst injuries, listing permanent and substantial physical deformity, loss of use of a limb, loss of a bodily organ system, and permanent physical functional injury that leaves someone unable to care independently for themselves. Jurors are never told any of this; subdivision (F)(2) keeps the limit out of the courtroom and leaves the reduction to the judge afterward. All of it constrains the recovery, not the fee percentage, and the two get mixed up constantly.

### Ohio requires paper at the front and paper at the end

Rule 1.5(c)(1) sets what the agreement itself has to contain: a signed writing giving the method of determining the fee, the percentages applying on settlement, at trial and on appeal, each litigation expense charged against the recovery, whether such expenses come off before or after the fee is figured, and a clear notice of any expense the client owes whether the claim wins or loses.

Revised Code 4705.15 says the same thing with statutory force for tort claims specifically. Subsection (B) requires the contingent fee agreement to be reduced to writing and signed by both the attorney and the client, with a copy going to the client. Subsection (C) adds the ending: a signed closing statement specifying how the compensation was determined, the costs and expenses deducted, and any proposed division with a lawyer who referred the matter. Rule 1.5(c)(2) puts that statement's timing at or before the moment compensation is received.

### Costs are third-party money, tracked separately

Filing fees, service charges, deposition transcripts, records from Cincinnati hospitals, crash reconstruction and jury deposits are payments that leave the file and go to somebody else. They sit outside the percentage, and the sequence in which they are subtracted changes what an injured person keeps. Rule 1.5(c)(1) requires the agreement to answer that sequencing question in writing.

### Which Cincinnati courtroom sets the arithmetic

Revised Code 1901.17 caps municipal court original jurisdiction at $15,000, so the size of the claim decides the schedule. In Hamilton County Municipal Court, Civil Rule XVIII prices a civil suit at $90 without service, small claims at $39, new residential or personal service at $30, certified mail service at $10, an amended complaint at $15, a third-party complaint at $25, a motion at $5, a subpoena at $6, and the jury demand at $10 with a $300 deposit behind it. Witnesses draw $6 for a half day and $12 for a full day.

Claims above that line move to the Court of Common Pleas, whose clerk collects its own advance deposits; confirm those amounts with that clerk rather than assuming the municipal figures.

### Limits that belong to other kinds of cases

Two Ohio numbers get quoted at injury clients by mistake. Revised Code 4123.512(F) says an attorney fee taxed against an employer or the commission, after a claimant wins a workers' compensation appeal in common pleas, shall not exceed $5,000. That is a compensation appeal, not a liability claim. The Industrial Commission's own fee resolution, separately, requires a written fee agreement and bars a fee against ongoing temporary total payments, and it states no percentage at all.

### Worth asking before signing in Hamilton County

Does the percentage change if the claim reaches trial or an appeal, and is each number written out. Are expenses deducted before or after the fee is computed. Who advances a records deposit or an expert retainer, and is that money owed back if the claim fails. Will the closing statement arrive before funds are disbursed. Is any part of the fee going to a lawyer who referred the file. Every one of those answers belongs in the signed writing, not in conversation."""

root = pathlib.Path("/home/user/workspace/local-sites/sites/cincinnatipersonalinjurylawyerpros.com")
p = root / "site.json"
d = json.loads(p.read_text())
d["pricing"] = pricing
p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
c = root / "copy.md"
t = c.read_text().split("## pricing_lede")[0].rstrip("\n")
t += "\n\n## pricing_lede\n\n" + LEDE + "\n\n## pricing_body\n\n" + BODY + "\n"
c.write_text(t)
print("ok")
