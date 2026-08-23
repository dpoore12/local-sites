"""Add /pricing/ fees pages to the five batch-5 injury sites."""
import json, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parent
SITES = ROOT / "sites"

RULE15 = "https://www.calbar.ca.gov/legal-professionals/rules/rules-professional-conduct/current-rules-professional-conduct/chapter-1-lawyer-client-relationship"
BPC6147 = "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=6147.&lawCode=BPC"
BPC6146 = "https://law.justia.com/codes/california/code-bpc/division-3/chapter-4/article-8-5/section-6146/"
CCP1033 = "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1033.5.&lawCode=CCP"
CCP631 = "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=631.&lawCode=CCP"
CIV3040 = "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=3040.&lawCode=CIV"
MONTEREY = "https://www.monterey.courts.ca.gov/system/files/general/2024-civil-fee-schedule.pdf"
SANTABARB = "https://www.santabarbara.courts.ca.gov/system/files/general/statewide-civil-fee-schedule-eff-01012024.pdf"
SANBERN = "https://sanbernardino.courts.ca.gov/system/files/civil/feesched.pdf"
LASC = "https://lascpubstorage.blob.core.windows.net/cpw/LIBSVCExecutiveSupport-265-2024FeeSchedule010124.pdf"
VSB = "https://vsb.org/Site/Site/about/rules-regulations/rpc-part6-sec2.aspx"
VA275 = "https://law.lis.virginia.gov/vacode/title17.1/chapter2/section17.1-275/"
VA1727 = "https://law.lis.virginia.gov/vacode/title58.1/chapter17/section58.1-1727/"
VA662 = "https://law.lis.virginia.gov/vacode/title8.01/chapter3/section8.01-66.2/"
VA413 = "https://law.lis.virginia.gov/vacode/title8.01/chapter14/section8.01-413/"
VA58115 = "https://law.lis.virginia.gov/vacode/title8.01/chapter21.1/section8.01-581.15/"
VBSCHED = "https://www.vacourts.gov/caseinfo/circuit_fees/virginia_beach_circ_civil_fees.pdf"

DATA = {}

# --------------------------------------------------------------------------- #
# Salinas / Monterey County
# --------------------------------------------------------------------------- #
DATA["salinascaraccidentlawyer.com"] = {
    "pricing": {
        "mode": "fees",
        "fee_kind": "contingency",
        "table_head": "What California fixes in a Monterey County injury claim, and what it leaves to the written contract",
        "col_a": "The part of the money",
        "col_b": "What the rule or statute fixes",
        "anchors": [
            {
                "label": "Percentage ceiling on an injury fee",
                "value": "None stated",
                "detail": "Rule 1.5 of the California Rules of Professional Conduct bars an unconscionable or illegal fee and then lists thirteen factors for testing one. It prints no percentage for ordinary negligence work.",
                "source_name": "Cal. Rules of Prof. Conduct, rule 1.5(a)-(b)",
                "source_url": RULE15,
            },
            {
                "label": "First paper in an unlimited civil case, Monterey County",
                "value": "$435",
                "detail": "Charged by the Monterey County Superior Court on the complaint in any case pleading more than $35,000, and again on the first paper filed by each other party.",
                "source_name": "Monterey County Superior Court civil fee schedule",
                "source_url": MONTEREY,
            },
            {
                "label": "Advance jury fee, nonrefundable",
                "value": "$150",
                "detail": "One side of the case posts it or the right to a jury is waived. Daily juror deposits after the first day are set by the court on top of it.",
                "source_name": "Cal. Code Civ. Proc. 631(b)",
                "source_url": CCP631,
            },
            {
                "label": "Health plan lien ceiling once a lawyer is involved",
                "value": "One-third",
                "detail": "A managed-care or medical-group reimbursement lien cannot take more than a third of the money due to the injured person under a judgment, compromise or settlement.",
                "source_name": "Cal. Civ. Code 3040(c)",
                "source_url": CIV3040,
            },
        ],
        "fee_rows": [
            {
                "stage": "The fee itself, in a crash claim",
                "share": "No statutory percentage",
                "note": "Tested after the fact against thirteen listed factors, among them proportionality to the work, the results obtained, and whether the client gave informed consent.",
                "source_name": "Cal. Rules of Prof. Conduct, rule 1.5(b)",
                "source_url": RULE15,
            },
            {
                "stage": "Medical malpractice claims only",
                "share": "25% before filing, 33% after",
                "note": "Malpractice-specific statute. Twenty-five percent where the claim settles before a complaint or arbitration demand is filed, thirty-three percent after, and more only by motion on good cause.",
                "source_name": "Cal. Bus. & Prof. Code 6146(a)",
                "source_url": BPC6146,
            },
            {
                "stage": "The written contingency contract",
                "share": "Duplicate signed copy, four required statements",
                "note": "It must state the rate, how costs affect both the fee and the recovery, any charges for related matters, and that the fee is not set by law but is negotiable.",
                "source_name": "Cal. Bus. & Prof. Code 6147(a)",
                "source_url": BPC6147,
            },
            {
                "stage": "Filing the complaint in Salinas",
                "share": "$435 unlimited, $370 or $225 limited",
                "note": "The $35,000 pleading line decides which tier applies, and the limited tier splits again at $10,000.",
                "source_name": "Monterey County Superior Court civil fee schedule",
                "source_url": MONTEREY,
            },
            {
                "stage": "Motions and a summary judgment motion",
                "share": "$60 and $500",
                "note": "Each paper requiring a hearing draws sixty dollars; a summary judgment or summary adjudication motion draws five hundred.",
                "source_name": "Monterey County Superior Court civil fee schedule",
                "source_url": MONTEREY,
            },
            {
                "stage": "Costs recoverable if the case is won",
                "share": "Statutory list",
                "note": "Filing, motion and jury fees, depositions, service of process and court-ordered expert fees are on it. Investigation expenses and experts the court did not order are not.",
                "source_name": "Cal. Code Civ. Proc. 1033.5",
                "source_url": CCP1033,
            },
        ],
    },
    "pricing_lede": (
        "California puts no number on what pursuing a crash claim is worth to the lawyer who "
        "handles it. It does fix the standard a fee has to survive, the contract that has to "
        "exist before anyone signs, and the court and lien amounts that read the same for "
        "every plaintiff filing in Monterey County."
    ),
    "pricing_body": """### The governing rule never names a percentage

Rule 1.5(a) of the California Rules of Professional Conduct runs one sentence: a lawyer shall not make an agreement for, charge, or collect an unconscionable or illegal fee. Behind it sits no schedule of permitted percentages. Rule 1.5(b) supplies thirteen factors for measuring a fee instead, and they read like an audit rather than a price list: whether there was overreaching in setting the fee, whether material facts were withheld, the amount of the fee in proportion to the value of the services actually performed, the relative sophistication of the two sides, the difficulty of the questions, the amount involved and the result reached, the time and labor spent, whether the fee is fixed or contingent, and whether the client gave informed consent to it.

Two things follow. Any percentage stated as "the California rate" is somebody's practice, not law. And the review happens looking backward, on the facts as they stood when the agreement was signed, unless the parties expected later events to move the number.

### The one corner where California does cap a percentage

Business and Professions Code section 6146 caps a contingency fee in an action against a health care provider for professional negligence: twenty-five percent of the amount recovered where the claim resolves by settlement and release before a civil complaint or an arbitration demand is filed, thirty-three percent where it resolves after that point, and anything higher only if the court or arbitrator grants a motion supported by evidence of good cause. The statute also defines what "recovered" means: the net sum after disbursements and costs, with the injured person's own medical bills and the lawyer's office overhead excluded from that deduction.

That ceiling belongs to malpractice claims. A rear-end impact at Boronda Road, a left-turn collision off North Main Street, a farm truck that pulls onto Highway 101 without clearance -- all ordinary negligence, none of them governed by section 6146. Anyone reciting the twenty-five and thirty-three percent figures for a car crash has picked up the wrong statute.

### Section 6147 decides what has to be on paper

For any contingency arrangement, section 6147(a) requires a written contract, signed by both sides, with a duplicate copy handed to the plaintiff at the moment it is entered into. Four things have to appear in it: the rate agreed on, how disbursements and costs will affect both the fee and the client's share, the extent to which the client could owe compensation for related matters outside the contract, and, in every case that section 6146 does not reach, a statement that the fee is not set by law but is negotiable between attorney and client. Section 6147(b) supplies the consequence: a contract missing any of that is voidable at the plaintiff's option, and the lawyer is then left with a reasonable fee rather than the bargain.

### Costs are the other half of the arithmetic

Costs are money that leaves the file and goes to third parties. Code of Civil Procedure section 1033.5 sets out which of them a winning party can recover: filing, motion and jury fees, deposition transcripts and video, service of process, court-ordered expert fees, statutory court reporter fees, exhibit enlargements that helped the trier of fact. It also names what a prevailing party cannot recover -- experts the court never ordered, investigation expenses in preparing for trial, postage, telephone and photocopying outside exhibits. Those lines still get spent in real cases; they just do not come back.

The court amounts in Monterey County are public. A complaint pleading more than $35,000 is an unlimited civil case at $435; below that line it is limited civil at $370, or $225 where the claim stays under $10,000. Every paper requiring a hearing costs $60, a summary judgment motion $500, court reporting for a hearing of an hour or less $30, and the advance jury fee $150. A case designated complex adds $1,000 for the plaintiffs and $1,000 for each defendant, capped at $18,000.

### The order of subtraction changes the answer

Two agreements with the same percentage can hand a client different amounts. Compute the fee on the gross and then subtract costs, and the fee is calculated on money that was never available to anyone. Subtract costs first and compute the fee on the remainder, and the client keeps the percentage of that cost total. Section 6147 requires the contract to state which way it works, which is the point of the requirement. Ask for the sentence, and ask who advances a $3,000 expert retainer if the file needs one.

### What comes off the top besides the fee

Civil Code section 3040 limits a health plan or medical group reimbursement lien to what the plan actually paid providers, and then, where the injured person engaged a lawyer, to no more than one-third of the money due under the judgment or settlement. It further requires pro rata reduction for the attorney fees and costs that produced the fund, and reduction by the same comparative-fault percentage the recovery was cut by. Hospital liens, Medi-Cal recovery and workers' compensation claims run under separate provisions, so the one-third figure is not universal.

### Questions worth asking in Monterey County before signing anything

Is the percentage the same before and after a complaint is filed. Are costs deducted before or after the fee is figured. Who fronts the cost of an out-of-county deposition when a commercial driver lives elsewhere. What happens to the fee if the file is associated out to another firm -- rule 1.5.1 requires a written agreement, written client consent after full disclosure, and no increase in the total fee for the division. If the answers are not in the contract, they are not answers.""",
}

# --------------------------------------------------------------------------- #
# Santa Barbara
# --------------------------------------------------------------------------- #
DATA["santabarbaracaraccidentlawyer.com"] = {
    "pricing": {
        "mode": "fees",
        "fee_kind": "contingency",
        "table_head": "The published amounts behind a Santa Barbara County injury claim",
        "col_a": "What is being measured",
        "col_b": "The figure the law or the court publishes",
        "anchors": [
            {
                "label": "An unconscionable or illegal fee",
                "value": "Prohibited",
                "detail": "That is the whole of California's substantive limit on an injury fee. Unconscionability is judged on the facts existing when the agreement was made, using thirteen enumerated factors.",
                "source_name": "Cal. Rules of Prof. Conduct, rule 1.5(a)",
                "source_url": RULE15,
            },
            {
                "label": "Any paper requiring a hearing, Santa Barbara Superior Court",
                "value": "$60",
                "detail": "Payable on discovery motions, motions to continue a trial date, motions for new trial and ex parte applications requiring notice, unless it is the party's first paper.",
                "source_name": "Santa Barbara Superior Court civil fee schedule, item 45",
                "source_url": SANTABARB,
            },
            {
                "label": "Summary judgment or summary adjudication motion",
                "value": "$500",
                "detail": "The single most expensive routine filing in a civil case, and the one an insurer is most likely to bring in a disputed-liability crash claim.",
                "source_name": "Santa Barbara Superior Court civil fee schedule, item 51",
                "source_url": SANTABARB,
            },
            {
                "label": "Malpractice fee ceiling, and only malpractice",
                "value": "25% / 33%",
                "detail": "The statutory limit on a contingency fee in a professional negligence action against a health care provider. It has no application to a motor vehicle claim.",
                "source_name": "Cal. Bus. & Prof. Code 6146(a)",
                "source_url": BPC6146,
            },
        ],
        "fee_rows": [
            {
                "stage": "Testing a fee after the fact",
                "share": "Thirteen factors",
                "note": "Overreaching, undisclosed material facts, proportion to the value of services, sophistication of the parties, difficulty, result, time spent, informed consent, and more.",
                "source_name": "Cal. Rules of Prof. Conduct, rule 1.5(b)",
                "source_url": RULE15,
            },
            {
                "stage": "Language the contract has to contain",
                "share": "Fee is negotiable, in writing",
                "note": "Outside malpractice claims, the contract must say in terms that the fee is not set by law but negotiable, and the plaintiff leaves with a signed duplicate.",
                "source_name": "Cal. Bus. & Prof. Code 6147(a)(4)",
                "source_url": BPC6147,
            },
            {
                "stage": "First paper, unlimited civil case",
                "share": "$435",
                "note": "Santa Barbara charges the uniform statewide amount; no local courthouse construction surcharge applies in this county.",
                "source_name": "Santa Barbara Superior Court civil fee schedule, item 1",
                "source_url": SANTABARB,
            },
            {
                "stage": "Jury demand and court reporting",
                "share": "$150 and $30",
                "note": "One hundred fifty dollars nonrefundable to preserve a jury, and thirty dollars for reporting a civil proceeding lasting an hour or less.",
                "source_name": "Santa Barbara Superior Court civil fee schedule, items 64 and 66",
                "source_url": SANTABARB,
            },
            {
                "stage": "Moving the case to another county",
                "share": "$50",
                "note": "Processing a change of venue, paid to the court the transfer is requested from. It arrives when a defendant is based elsewhere.",
                "source_name": "Santa Barbara Superior Court civil fee schedule, item 55",
                "source_url": SANTABARB,
            },
            {
                "stage": "Splitting a fee with an outside firm",
                "share": "Written consent, no markup",
                "note": "The division needs a written agreement between the firms, the client's written consent after full disclosure of the terms, and no increase in the total fee.",
                "source_name": "Cal. Rules of Prof. Conduct, rule 1.5.1(a)",
                "source_url": RULE15,
            },
        ],
    },
    "pricing_lede": (
        "Two different systems set numbers in a Santa Barbara injury claim: the State Bar rules, "
        "which control how a fee is judged without ever naming a percentage, and the Superior "
        "Court's published fee schedule, which prices every filing to the dollar. This page "
        "separates them."
    ),
    "pricing_body": """### Start with the court's schedule, because those figures are exact

The Superior Court of California, County of Santa Barbara publishes the civil fee schedule it charges by, and the amounts in it do not move with the facts of a case. Opening an unlimited civil case -- any complaint pleading more than $35,000 -- costs $435, and each other party pays $435 on its first paper. Every subsequent paper that requires a hearing costs $60: discovery motions, a motion to continue trial, a motion for new trial, an ex parte application that requires notice. A summary judgment or summary adjudication motion costs $500. Reporting a proceeding of an hour or less costs $30. Preserving the right to a jury costs $150 in advance, nonrefundable, and if it is not paid the jury is waived. Processing a change of venue costs $50. A complex designation adds $1,000 for the plaintiff side and $1,000 for each defendant, to a ceiling of $18,000.

Nothing local inflates those numbers here. The statewide schedule carries a courthouse construction surcharge in only three counties, and Santa Barbara is not one of them, so a case opened in the Anacapa Street courthouse and a case opened in Santa Maria are priced identically.

### Now the fee, where California prints no figure at all

The temptation is to assume the state also fixes a percentage. It does not. Rule 1.5(a) of the California Rules of Professional Conduct forbids making an agreement for, charging, or collecting an unconscionable or illegal fee, and stops there. Rule 1.5(b) then tells anyone reviewing that fee what to weigh: whether there was fraud or overreaching in negotiating it, whether material facts were left undisclosed, the fee in proportion to the value of the services performed, how sophisticated each side was, the novelty and difficulty of the questions, whether the engagement closed off other work, the amount at stake and the result obtained, the time pressure, the length of the relationship, the experience and ability of the lawyers, whether the fee is fixed or contingent, the time and labor required, and whether the client gave informed consent.

That is a standard, not a cap, and it is applied on the facts as they stood when the agreement was signed unless both sides expected later events to affect the fee.

### The exception, kept in its box

California does cap a contingency percentage in one category of case. Business and Professions Code section 6146 limits the fee in an action against a health care provider based on professional negligence to twenty-five percent of the amount recovered if the matter settles before a civil complaint or arbitration demand is filed, and thirty-three percent afterwards, with more available only if a court or arbitrator finds good cause on a motion. The statute measures the percentage against the net sum recovered after costs, and expressly refuses to let the plaintiff's own medical expenses or a lawyer's overhead be treated as deductible costs.

Section 6146 applies to malpractice. It does not reach a collision on the 101 through Montecito, a driver rear-ended at a Milpas Street light, or a cyclist struck on the Mesa. Seeing those percentages quoted for a crash claim is a signal that whoever wrote the page did not check the statute.

### Section 6147, and why the contract is the document that matters

Because the state sets no rate, the contract is where the rate lives, and section 6147 controls its contents. It must be in writing, signed by both attorney and client, and the plaintiff must receive a duplicate signed copy at the time it is entered into. It must state the agreed rate. It must state how disbursements and costs affect the fee and the client's recovery. It must state what the client might owe for related matters outside the contract. And in any case not governed by section 6146 it must say that the fee is not set by law but is negotiable. Failure on any of those points makes the agreement voidable at the plaintiff's election, leaving the lawyer with a reasonable fee determined elsewhere.

If an outside firm is brought in, rule 1.5.1 adds three conditions: a written agreement between the lawyers, the client's written consent after full disclosure of who is splitting the fee and on what terms, and no increase in the total fee because of the split.

### What a recovery gets reduced by before anyone sees it

Court fees are the small end. The larger deductions in a Santa Barbara injury file tend to be deposition transcripts, medical records, treating-physician testimony, and any retained expert on biomechanics or future care. Code of Civil Procedure section 1033.5 lists what a prevailing party can recover from the other side -- filing, motion and jury fees, depositions and travel to them, service of process, court-ordered experts, statutory reporter fees -- and lists what it cannot, including experts the court did not order, investigation expenses, and photocopying outside exhibits. Reimbursement claims from a health plan then run under Civil Code section 3040, which caps a plan lien at one-third of the money due where the injured person engaged counsel and requires pro rata reduction for the fees and costs that created the fund.

### The practical read

A fee is negotiable in this state, and the statute requires the contract to say so. Costs are separate from the fee, and the contract has to say how they interact. The court's own numbers are published, so any figure attributed to the courthouse can be checked in an afternoon. Everything else is a matter for the written agreement between an injured person and the lawyer that person chooses.""",
}

# --------------------------------------------------------------------------- #
# Victorville / San Bernardino County
# --------------------------------------------------------------------------- #
DATA["victorvillecaraccidentlawyerpros.com"] = {
    "pricing": {
        "mode": "fees",
        "fee_kind": "contingency",
        "table_head": "San Bernardino County filing amounts, and the California rules that govern a fee",
        "col_a": "Line item",
        "col_b": "Published amount or requirement",
        "anchors": [
            {
                "label": "Local courthouse construction surcharge",
                "value": "$35",
                "detail": "San Bernardino is one of three California counties whose first-paper filings carry a local surcharge, which is why limited civil filings cost more here than the statewide figure.",
                "source_name": "San Bernardino Superior Court civil fee schedule appendix",
                "source_url": SANBERN,
            },
            {
                "label": "Limited civil first paper, over $10,000 up to $35,000",
                "value": "$380",
                "detail": "Ten dollars above the $370 statewide amount once the surcharge is applied. A claim pleaded under $10,000 costs $240 here rather than $225.",
                "source_name": "San Bernardino Superior Court civil fee schedule appendix",
                "source_url": SANBERN,
            },
            {
                "label": "Percentage ceiling written into California law for a crash claim",
                "value": "None",
                "detail": "Rule 1.5 forbids an unconscionable or illegal fee and lists thirteen factors for judging one. It sets no rate for ordinary negligence work of any kind.",
                "source_name": "Cal. Rules of Prof. Conduct, rule 1.5",
                "source_url": RULE15,
            },
            {
                "label": "Contract defect remedy",
                "value": "Voidable",
                "detail": "A contingency agreement that omits anything section 6147 requires is voidable at the plaintiff's option, and the lawyer is then held to a reasonable fee instead.",
                "source_name": "Cal. Bus. & Prof. Code 6147(b)",
                "source_url": BPC6147,
            },
        ],
        "fee_rows": [
            {
                "stage": "Unlimited civil first paper, San Bernardino",
                "share": "$435",
                "note": "The surcharge is offset in this tier, so the High Desert courthouses charge the same $435 as the rest of the state for a case pleading over $35,000.",
                "source_name": "San Bernardino Superior Court civil fee schedule",
                "source_url": SANBERN,
            },
            {
                "stage": "Limited civil first paper, San Bernardino",
                "share": "$240 or $380",
                "note": "Both figures include the county's $35 courthouse construction surcharge. The split falls at a $10,000 pleaded amount.",
                "source_name": "San Bernardino Superior Court civil fee schedule appendix",
                "source_url": SANBERN,
            },
            {
                "stage": "Jury fee and motion fees",
                "share": "$150, $60, $500",
                "note": "Nonrefundable advance jury fee, then sixty dollars per paper requiring a hearing and five hundred for a summary judgment motion.",
                "source_name": "San Bernardino Superior Court civil fee schedule",
                "source_url": SANBERN,
            },
            {
                "stage": "How a contingency rate is set",
                "share": "By negotiation, in writing",
                "note": "Section 6147 requires the rate in a signed contract, with a duplicate copy handed over, plus a statement that the fee is not fixed by law.",
                "source_name": "Cal. Bus. & Prof. Code 6147(a)",
                "source_url": BPC6147,
            },
            {
                "stage": "Malpractice claims, a separate rule",
                "share": "25% or 33%",
                "note": "Statutory ceilings that apply only to professional negligence claims against health care providers, measured on the net recovery after costs.",
                "source_name": "Cal. Bus. & Prof. Code 6146(a)",
                "source_url": BPC6146,
            },
            {
                "stage": "A health plan's reimbursement claim",
                "share": "One-third maximum",
                "note": "Where the injured person retained counsel, the plan lien cannot exceed a third of the money due, and it drops pro rata for the fees and costs that produced it.",
                "source_name": "Cal. Civ. Code 3040(c)",
                "source_url": CIV3040,
            },
        ],
    },
    "pricing_lede": (
        "Filing a civil case in San Bernardino County costs more than filing the same case "
        "almost anywhere else in California, and the reason is printed in the court's own fee "
        "schedule. What a fee taken out of a recovery may be is a separate question, and the "
        "State Bar rules answer it with a standard rather than a rate."
    ),
    "pricing_body": """### The county surcharge is real, and it is in the appendix

Most California civil filing fees are uniform statewide. Three counties are carved out, and San Bernardino is one of them: a local courthouse construction surcharge of $35 is added to first-paper filings. The court's published schedule shows the arithmetic. A limited civil complaint pleading up to $10,000 costs $240 here instead of the statewide $225. A limited civil complaint pleading over $10,000 and up to $35,000 costs $380 instead of $370. In the unlimited tier the surcharge is offset, so a complaint pleading more than $35,000 costs $435, matching the rest of the state.

Those are not large sums against an injury claim, but they show something useful: the numbers attached to a courthouse are published, checkable, and identical for every person who walks in. The numbers attached to a lawyer are not published anywhere, because no California authority publishes them.

### The rule that governs a fee sets a standard, not a rate

Rule 1.5 of the California Rules of Professional Conduct prohibits making an agreement for, charging, or collecting an unconscionable or illegal fee. Then it lists thirteen factors that decide whether a fee crossed that line, judged on the circumstances existing when the agreement was made: overreaching in the negotiation, failure to disclose material facts, the fee measured against the value of the services performed, the relative sophistication of lawyer and client, the difficulty of the questions, whether taking the matter cost the lawyer other work, the sum at stake and the outcome reached, deadlines imposed, the history between the two, the lawyer's experience and ability, whether the fee is fixed or contingent, the time and labor put in, and whether the client gave informed consent.

Nowhere in that list is a number. Anybody who tells a High Desert reader that California limits an auto injury fee to a specific percentage is describing a different statute, and the next section says which one.

### Section 6146 is the malpractice rule, and only the malpractice rule

Business and Professions Code section 6146 does cap percentages. It limits a contingency fee in an action for injury or death against a health care provider based on professional negligence to twenty-five percent of the amount recovered where the case settles before a civil complaint or arbitration demand is filed, thirty-three percent where it resolves later, and anything above that only on a motion the court or arbitrator grants for good cause. "Recovered" is defined as the net after disbursements and costs, and the statute refuses to count the plaintiff's medical treatment costs or the lawyer's overhead as deductions.

None of that governs a collision at Bear Valley Road, a truck merging off Interstate 15, or a driver hit at the D Street crossing. Those are ordinary negligence claims, outside section 6146 entirely.

### What section 6147 forces into the contract

Since the rate is negotiated, the statute regulates the paper. Section 6147(a) requires a written contract signed by both sides, with a duplicate signed copy given to the plaintiff at signing, stating the agreed rate, how disbursements and costs affect the fee and the recovery, and what compensation might be owed for related matters outside the contract. Unless the claim falls under section 6146, the contract must also state that the fee is not set by law but is negotiable between attorney and client. Under section 6147(b), missing any of that makes the agreement voidable at the plaintiff's option, leaving the lawyer entitled only to a reasonable fee.

### Distance is what makes a High Desert file expensive

Cost, not fee, is where geography shows up. Records come from providers spread between Victorville, Apple Valley, Hesperia and the hospitals down the Cajon Pass. Defense depositions of a commercial driver or a corporate representative are often set in San Bernardino or in Los Angeles County, which turns a deposition into a travel day plus a transcript. Retained experts on collision reconstruction and future care bill by the hour regardless of where the crash happened.

Code of Civil Procedure section 1033.5 decides which of those a winning party can shift to the other side. Recoverable: filing, motion and jury fees, deposition taking, transcription and travel, service of process, court-ordered expert fees, statutory reporter fees. Not recoverable, absent express authority: experts the court never appointed, investigation expenses in preparing for trial, postage, telephone and photocopying outside exhibits. A file can therefore be won and still carry costs nobody reimburses, which is exactly why the contract has to say who advanced them and how they come out.

### The reimbursement claim that arrives after the settlement

Civil Code section 3040 caps a managed-care or medical-group reimbursement lien at what the plan actually paid providers, and where the injured person engaged a lawyer it caps the lien again at one-third of the money due under the judgment or settlement. The lien reduces pro rata for the attorney fees and costs that created the fund, and reduces by the same comparative-fault share the recovery was reduced by. Hospital liens, Medi-Cal recovery and workers' compensation reimbursement are governed by different statutes, so a person who received care through more than one system should expect more than one set of rules.

### Three questions the paperwork should answer without being asked

Whether the percentage changes if a complaint is filed. Whether costs come off before or after the fee is computed. Who carries the cost of an out-of-county deposition and a reconstruction expert if the case gets there. Those answers belong in the signed contract, in writing, before anything is filed at the Victorville courthouse.""",
}

# --------------------------------------------------------------------------- #
# West Covina / Los Angeles County
# --------------------------------------------------------------------------- #
DATA["westcovinacaraccidentlawyerpros.com"] = {
    "pricing": {
        "mode": "fees",
        "fee_kind": "contingency",
        "table_head": "Los Angeles Superior Court amounts, and the California limits on a fee",
        "col_a": "What gets billed",
        "col_b": "Amount or rule",
        "anchors": [
            {
                "label": "Court reporter per diem, Los Angeles Superior Court",
                "value": "$382 / $764",
                "detail": "Three hundred eighty-two dollars for a civil proceeding running more than one hour but under four, and seven hundred sixty-four for four hours or more. Thirty dollars covers an hour or less.",
                "source_name": "Los Angeles Superior Court civil fee schedule",
                "source_url": LASC,
            },
            {
                "label": "Complex case designation",
                "value": "$1,000",
                "detail": "One thousand dollars for all plaintiffs and another thousand for each defendant, to a ceiling of $18,000 per case, on top of the ordinary first-paper fee.",
                "source_name": "Los Angeles Superior Court civil fee schedule",
                "source_url": LASC,
            },
            {
                "label": "Daily jury deposit after the first day",
                "value": "$15 plus mileage",
                "detail": "Los Angeles sets the running deposit at fifteen dollars per juror per day plus thirty-four cents a mile one way, deposited at the start of each session.",
                "source_name": "Los Angeles Superior Court civil fee schedule",
                "source_url": LASC,
            },
            {
                "label": "Statutory percentage for an auto injury fee",
                "value": "Not set by statute",
                "detail": "California controls the fee through an unconscionability standard and a written-contract statute. The rate itself is negotiated between the injured person and the lawyer.",
                "source_name": "Cal. Rules of Prof. Conduct, rule 1.5",
                "source_url": RULE15,
            },
        ],
        "fee_rows": [
            {
                "stage": "Opening the case",
                "share": "$435",
                "note": "First paper in an unlimited civil case, and again for each other party's first paper. Limited civil filings run $370 or $225 by pleaded amount.",
                "source_name": "Los Angeles Superior Court civil fee schedule",
                "source_url": LASC,
            },
            {
                "stage": "Motions",
                "share": "$60, or $500",
                "note": "Sixty dollars for any paper requiring a hearing, including discovery motions and trial continuances; five hundred for summary judgment or summary adjudication.",
                "source_name": "Los Angeles Superior Court civil fee schedule",
                "source_url": LASC,
            },
            {
                "stage": "Keeping the jury",
                "share": "$150 in advance",
                "note": "Nonrefundable, and waived if unpaid by the deadline. After day one the Los Angeles deposit is fifteen dollars per juror per day plus mileage.",
                "source_name": "Cal. Code Civ. Proc. 631(b)",
                "source_url": CCP631,
            },
            {
                "stage": "The fee agreement",
                "share": "Written, duplicate, negotiable",
                "note": "Section 6147 requires the rate, the treatment of costs, and a statement that the fee is not set by law, in a contract signed by both sides.",
                "source_name": "Cal. Bus. & Prof. Code 6147(a)",
                "source_url": BPC6147,
            },
            {
                "stage": "Health care malpractice claims",
                "share": "25% pre-filing, 33% after",
                "note": "A statutory ceiling limited to professional negligence claims against health care providers, with more allowed only by motion for good cause.",
                "source_name": "Cal. Bus. & Prof. Code 6146(a)",
                "source_url": BPC6146,
            },
            {
                "stage": "Costs a winning party can shift",
                "share": "Enumerated list",
                "note": "Filing, motion and jury fees, depositions, service of process and court-ordered experts are recoverable; investigation expenses and uninvited experts are not.",
                "source_name": "Cal. Code Civ. Proc. 1033.5",
                "source_url": CCP1033,
            },
        ],
    },
    "pricing_lede": (
        "The Los Angeles Superior Court publishes what it charges for every step of a civil case, "
        "down to a court reporter's half day. California's fee rules publish no percentage at all. "
        "This page sets both sides of that out for a West Covina crash claim."
    ),
    "pricing_body": """### Los Angeles prices the process, not the lawyer

A civil case in Los Angeles County has a published price list, and it is worth reading before signing anything, because it explains where money actually goes. The first paper in an unlimited civil case -- a complaint pleading more than $35,000 -- costs $435, and each other party pays $435 to appear. Limited civil filings cost $370 or $225 depending on the pleaded amount. Any paper requiring a hearing costs $60. A summary judgment or summary adjudication motion costs $500. A complex designation adds $1,000 for the plaintiff side and $1,000 for each defendant, capped at $18,000 for the case.

Then come the Los Angeles line items that surprise people. Court reporting for a proceeding of one hour or less is $30, but a proceeding running more than an hour and under four costs $382, and four hours or more costs $764. The advance jury fee is $150, nonrefundable; from the second day onward the court's deposit is $15 per juror per day plus $0.34 a mile one way. A single contested motion day with a reporter, in other words, can cost more than opening the case did.

### What California actually limits about a fee

Nothing in the state's rules assigns a percentage to injury work. Rule 1.5(a) of the California Rules of Professional Conduct prohibits an unconscionable or illegal fee. Rule 1.5(b) then supplies the measuring stick: whether the lawyer engaged in fraud or overreaching in setting the fee, whether material facts were disclosed, the fee compared with the value of the services performed, how sophisticated the client was relative to the lawyer, the novelty and difficulty of the work, whether the case foreclosed other work, the amount involved and the result obtained, time pressure, the length of the relationship, the lawyer's experience and ability, whether the fee is fixed or contingent, the hours and labor involved, and whether the client gave informed consent.

Read that as a review mechanism. The state does not pre-approve a rate; it reserves the right to look at one afterwards, on the facts as they stood when the agreement was signed.

### The malpractice statute, labeled as such

Business and Professions Code section 6146 is the only California provision that caps an injury contingency percentage, and it reaches one kind of claim: an action for injury or death against a health care provider based on professional negligence. There, the fee cannot exceed twenty-five percent of the amount recovered if the matter is resolved by settlement and release before a civil complaint or arbitration demand is filed, or thirty-three percent if resolved after that, unless a court or arbitrator grants a motion for more on evidence of good cause. The statute computes the percentage on the net recovery after costs and forbids treating the plaintiff's medical care costs or the lawyer's overhead as deductible.

A rear-end collision on Azusa Avenue, a lane-change crash on the 10 near Citrus, a pedestrian struck near the Eastland shopping district: none of those are malpractice claims, so section 6146's percentages have nothing to say about them. Any West Covina page quoting those numbers for a car crash has mislabeled the statute.

### Section 6147 is the consumer protection that does apply

The contract does the work the statute declines to do. Section 6147(a) requires a contingency agreement to be in writing, signed by both attorney and client, with a duplicate signed copy provided to the plaintiff when it is entered into. It must state the agreed rate. It must state how disbursements and costs affect both the fee and the client's recovery. It must state what the client might owe for related matters that fall outside the contract. And unless section 6146 governs the claim, it must say plainly that the fee is not set by law but is negotiable between attorney and client. Section 6147(b) makes a defective contract voidable at the plaintiff's option, with the lawyer limited to a reasonable fee.

That negotiability sentence is the most useful line in the statute. It exists because the legislature expected people to assume the rate was fixed.

### Cost-shifting is narrower than most people expect

Code of Civil Procedure section 1033.5 lists what a prevailing party may recover as costs: filing, motion and jury fees, taking and transcribing necessary depositions plus travel to attend them, service of process, ordinary witness fees, court-ordered expert fees, statutory court reporter fees, and exhibit costs that helped the trier of fact. It also lists what is not allowable without express authority: fees of experts the court did not order, investigation expenses in preparing the case, postage, telephone and photocopying outside exhibits, and transcripts the court did not order.

In a real Los Angeles file the biggest advances are usually the ones on the wrong side of that line. A retained reconstruction or life-care expert the court never appointed is not recoverable from the defense as a cost, even in a case that wins. That is why the treatment of costs in the fee agreement matters as much as the percentage in it.

### The two sentences to look for in any agreement

First, whether costs are subtracted before or after the fee is calculated -- section 6147 requires the contract to address it, and the two orders produce different numbers on identical facts. Second, whether the percentage shifts at a milestone such as filing suit or setting trial, because the court fees above show why a filed case costs more to run than a pre-suit claim. Everything else on this page can be verified from the Los Angeles Superior Court's own fee schedule and from the statutes named beside each figure.""",
}

# --------------------------------------------------------------------------- #
# Virginia Beach
# --------------------------------------------------------------------------- #
DATA["virginiabeachcaraccidentlawyerpros.com"] = {
    "pricing": {
        "mode": "fees",
        "fee_kind": "contingency",
        "table_head": "What Virginia's rule and the Virginia Beach clerk set in an injury claim",
        "col_a": "Item",
        "col_b": "What Virginia sets",
        "anchors": [
            {
                "label": "Circuit court clerk's fee, claim for money damages",
                "value": "$100 to $300",
                "detail": "One hundred dollars where the claim seeks up to $49,999, $200 up to $100,000, $250 up to $500,000, and $300 above that. Ten dollars of each goes to the Courts Technology Fund.",
                "source_name": "Va. Code 17.1-275(A)(13)",
                "source_url": VA275,
            },
            {
                "label": "Writ tax on commencing a civil action",
                "value": "$5 / $15 / $25",
                "detail": "A tax on the suit itself, tiered by the damages demanded: five dollars up to $49,999, fifteen up to $100,000, twenty-five above $100,000.",
                "source_name": "Va. Code 58.1-1727",
                "source_url": VA1727,
            },
            {
                "label": "Hospital lien ceiling against an injury claim",
                "value": "$2,500",
                "detail": "A hospital or nursing home lien for a just and reasonable charge cannot exceed $2,500, with $750 for each physician, nurse, physical therapist or pharmacy and $200 per emergency medical services provider.",
                "source_name": "Va. Code 8.01-66.2",
                "source_url": VA662,
            },
            {
                "label": "Percentage ceiling on an injury fee in Virginia",
                "value": "None stated",
                "detail": "Rule 1.5 of the Virginia Rules of Professional Conduct requires that a fee be reasonable and lists eight factors. It fixes no percentage for injury work.",
                "source_name": "Va. Rules of Prof. Conduct, Rule 1.5(a)",
                "source_url": VSB,
            },
        ],
        "fee_rows": [
            {
                "stage": "The standard a fee must meet",
                "share": "Reasonable, eight factors",
                "note": "Time and labor, difficulty, the fee customarily charged locally for similar work, the amount involved and result, time limits, the relationship, experience and ability, fixed or contingent.",
                "source_name": "Va. Rules of Prof. Conduct, Rule 1.5(a)",
                "source_url": VSB,
            },
            {
                "stage": "What a contingent agreement must state in writing",
                "share": "Four required terms",
                "note": "The method of computing the fee, the percentages on settlement, trial and appeal, the expenses deducted from the recovery, and whether they come out before or after the fee.",
                "source_name": "Va. Rules of Prof. Conduct, Rule 1.5(c)",
                "source_url": VSB,
            },
            {
                "stage": "Nonrefundable advanced legal fees",
                "share": "Prohibited",
                "note": "Virginia's rule bars them outright, and at the close of a contingent matter the lawyer owes a written statement of the outcome and how the remittance was figured.",
                "source_name": "Va. Rules of Prof. Conduct, Rule 1.5",
                "source_url": VSB,
            },
            {
                "stage": "Filing the suit in Virginia Beach Circuit Court",
                "share": "Clerk fee plus writ tax plus local fees",
                "note": "The clerk's schedule assembles a total from the statutory fee and tax plus a $9 legal aid fee, $5 technology trust fund fee, $4 law library fee and $2 courthouse maintenance charge.",
                "source_name": "Virginia Beach Circuit Court civil fee schedule",
                "source_url": VBSCHED,
            },
            {
                "stage": "Getting the medical records",
                "share": "$0.50 per page, $160 cap",
                "note": "Paper copies run up to fifty cents a page for the first fifty pages and a quarter after, with search and handling capped at twenty dollars; electronic production is capped at $160.",
                "source_name": "Va. Code 8.01-413(B2)-(B3)",
                "source_url": VA413,
            },
            {
                "stage": "Medical malpractice, a cap on recovery not on fees",
                "share": "$2.75 million",
                "note": "For acts of malpractice from July 1, 2026 through June 30, 2027 the total recoverable is capped by statute. It limits the verdict, not the lawyer's percentage.",
                "source_name": "Va. Code 8.01-581.15",
                "source_url": VA58115,
            },
        ],
    },
    "pricing_lede": (
        "Virginia handles injury fees with a reasonableness rule, a list of terms that must appear "
        "in a written contingent agreement, and a set of statutory amounts a clerk and a hospital "
        "can claim. This page walks through each of those, with the rule or code section beside it."
    ),
    "pricing_body": """### Virginia's rule requires a reasonable fee and names what that means

Rule 1.5 of the Virginia Rules of Professional Conduct opens with four words that carry the whole standard: a lawyer's fee shall be reasonable. It then lists eight factors for testing one. The time and labor required, the novelty and difficulty of the questions, and the skill needed to do the work properly. Whether taking the matter closed off other employment. The fee customarily charged in the locality for similar legal services. The amount involved and the results obtained. Time limits imposed by the client or the circumstances. The nature and length of the professional relationship. The experience, reputation and ability of the lawyers doing the work. And whether the fee is fixed or contingent.

No percentage appears anywhere in that list. Virginia does not legislate a rate for injury work, so any figure presented as "the Virginia limit" for a car crash claim is somebody's practice rather than the Commonwealth's rule.

### Rule 1.5 also controls the paperwork, and it is specific

Two disclosure duties sit alongside the standard. Rule 1.5(b) requires the fee to be adequately explained to the client, and where the lawyer has not regularly represented that client, the amount, basis or rate must be communicated preferably in writing before or within a reasonable time after the representation begins.

Rule 1.5(c) is stricter for contingent matters, because a contingent fee agreement has to state in writing the method by which the fee is determined, the percentage or percentages that accrue to the lawyer in the event of settlement, trial or appeal, the litigation and other expenses to be deducted from the recovery, and whether those expenses are deducted before or after the contingent fee is calculated. When the matter concludes, the rule requires a written statement showing the outcome and, where there was a recovery, the remittance to the client and how it was computed.

Two consequences deserve emphasis. A single percentage for every scenario is not what the rule contemplates -- it asks separately about settlement, trial and appeal. And the before-or-after question about expenses is not a technicality: the same percentage applied in the two orders produces different money for the client.

Virginia adds one flat prohibition that not every state has. Nonrefundable advanced legal fees are prohibited. Contingent fees are also barred entirely in two settings: domestic relations matters, except in rare instances, and representing a defendant in a criminal case.

### What the Virginia Beach clerk charges to open a case

Court costs in the Commonwealth are assembled from parts rather than quoted as one figure. Under Va. Code 17.1-275(A)(13) the circuit court clerk's fee in a civil action that includes a claim for money damages is $100 where the recovery sought does not exceed $49,999, $200 above that up to $100,000, $250 above that up to $500,000, and $300 where more than $500,000 is sought; $10 of each fee is apportioned to the Courts Technology Fund. A petition asking a court to approve a settlement where no action has yet been filed carries a $50 clerk's fee. Copies of papers or electronic records from the clerk run fifty cents per page or image.

Separately, Va. Code 58.1-1727 imposes a writ tax on commencing a civil action in a court of record: $5 where the debt or damages demanded does not exceed $49,999, $15 where the demand exceeds that but not $100,000, and $25 where it exceeds $100,000.

The Virginia Beach Circuit Court's own civil fee schedule then shows how a total is built, listing the components charged alongside the clerk fee and writ tax: a $9 legal aid fee, a $5 technology trust fund fee, a $4 law library fee, a $2 courthouse maintenance charge, a $1 indigent defense assessment, and a $10 court technology fund line on the higher-tier civil filings. That is why a filing total in this city ends in an odd figure rather than a round one.

### The claims that reach a recovery before the injured person does

Virginia gives medical providers a statutory lien on an injury claim, with dollar ceilings. Under Va. Code 8.01-66.2 a hospital or nursing home lien for a just and reasonable charge cannot exceed $2,500; each physician, nurse, physical therapist or pharmacy is limited to $750; each emergency medical services provider or agency is limited to $200. Those liens do not attach automatically. Under Va. Code 8.01-66.5 written notice of the lien must be served on or given to the party alleged to have caused the injury, the injured person, or that person's lawyer, except where counsel already knew the Commonwealth provided or paid for the care.

Getting the records that prove the claim has its own price ceilings. Va. Code 8.01-413 allows a health care provider to charge no more than fifty cents a page for the first fifty pages of paper copies and twenty-five cents a page after that, with a search and handling fee capped at twenty dollars, plus postage. For records produced electronically the caps are thirty-seven cents and eighteen cents a page, and the total for an electronic production requested on or after July 1, 2021 cannot exceed $160 apart from the reasonable cost of an audit trail if one is specifically requested.

### One cap that is often misdescribed

Virginia does cap money in medical malpractice cases, and it is not a fee cap. Va. Code 8.01-581.15 limits the total amount recoverable for injury to or death of a patient, on a sliding annual scale tied to when the malpractice occurred: $2.70 million for acts from July 1, 2025 through June 30, 2026, and $2.75 million for acts from July 1, 2026 through June 30, 2027, rising by $50,000 a year until it reaches $3 million for acts on or after July 1, 2031. That statute constrains the verdict or judgment, not the percentage a lawyer may charge, and it has no application to an ordinary collision at Independence Boulevard or on Shore Drive.

### The short version for a Virginia Beach reader

The Commonwealth sets no percentage, requires the percentages to be written down for settlement, trial and appeal, forbids nonrefundable advance fees, requires a written accounting at the end, and fixes the clerk's fee, the writ tax, the provider lien ceilings and the records charges by statute. Everything else is negotiated in a written agreement between an injured person and the lawyer that person chooses, and the figures above are the ones a reader can check before that conversation starts.""",
}


def insert_pricing(domain, block):
    p = SITES / domain / "site.json"
    s = json.loads(p.read_text(), object_pairs_hook=collections.OrderedDict)
    out = collections.OrderedDict()
    for k, v in s.items():
        if k == "hero_accent":
            out["pricing"] = block
        out[k] = v
    if "pricing" not in out:
        out["pricing"] = block
    p.write_text(json.dumps(out, indent=1, ensure_ascii=False))


def append_copy(domain, lede, body):
    p = SITES / domain / "copy.md"
    txt = p.read_text().rstrip("\n")
    if "## pricing_lede" in txt:
        raise SystemExit(f"{domain}: pricing blocks already present")
    txt += "\n\n## pricing_lede\n\n" + lede.strip() + "\n\n## pricing_body\n\n" + body.strip() + "\n"
    p.write_text(txt)


for domain, d in DATA.items():
    insert_pricing(domain, d["pricing"])
    append_copy(domain, d["pricing_lede"], d["pricing_body"])
    print("wrote", domain)
