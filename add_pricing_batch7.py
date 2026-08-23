#!/usr/bin/env python3
"""Batch 7: /pricing/ pages for five legal sites, all fees/contingency.

Oceanside PI, Santa Ana PI, Virginia Beach PI, Birmingham truck, San Diego
wrongful termination. Every figure was read on the source named in the row on
2026-08-23; see pricing-research-*.md for the retrieval log.
"""
import json
import pathlib

SITES = pathlib.Path(__file__).parent / "sites"

CALRULE = ("https://www.calbar.ca.gov/legal-professionals/rules/rules-professional-"
           "conduct/current-rules-professional-conduct/chapter-1-lawyer-client-"
           "relationship")
BPC6146 = "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=6146.&lawCode=BPC"
BPC6147 = "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=6147.&lawCode=BPC"
BPC6148 = "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=6148.&lawCode=BPC"
GOV12965 = "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=12965.&lawCode=GOV"
LAB1194 = "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1194.&lawCode=LAB"
LAB2185 = "https://codes.findlaw.com/ca/labor-code/lab-sect-218-5/"
WIC1412478 = "https://codes.findlaw.com/ca/welfare-and-institutions-code/wic-sect-14124-78/"
SDFEE = ("https://www.sdcourt.ca.gov/pls/portal/docs/page/sdcourt/generalinformation/"
         "forms/adminforms/adm001.pdf")
OCFEE = "https://www.occourts.org/system/files/general/ocfeeschedule.pdf"

VSB15 = "https://vsb.org/Site/Site/about/rules-regulations/rpc-part6-sec2.aspx"
VA1677 = "https://law.lis.virginia.gov/vacode/title16.1/chapter6/section16.1-77/"
VA6948 = "https://law.lis.virginia.gov/vacode/title16.1/chapter4.1/section16.1-69.48:2/"
VA17272 = "https://law.lis.virginia.gov/vacode/title17.1/chapter2/section17.1-272/"
VA3932 = "https://law.lis.virginia.gov/vacode/title54.1/chapter39/section54.1-3932/"
VA58115 = "https://law.lis.virginia.gov/vacode/title8.01/chapter21.1/section8.01-581.15/"
VBGDC = "https://courts.virginiabeach.gov/general-district-court/civil-division"

ALRULE = "https://judicial.alabama.gov/docs/library/rules/cond1_5.pdf"
AL2590 = "https://law.justia.com/codes/alabama/title-25/chapter-5/article-3/section-25-5-90/"
AL3461 = "https://law.justia.com/codes/alabama/title-34/chapter-3/article-3/section-34-3-61/"
JEFFCLERK = "https://jefferson.alacourt.gov/filing-fees/filing-fees-circuit-civil-cases/"
JEFFAOC = "https://www.alacourt.gov/docs/Jefferson-Birmingham.pdf"
CFR3879 = "https://www.law.cornell.edu/cfr/text/49/387.9"

PRICING = {}

# ---------------------------------------------------------------- Oceanside, CA
PRICING["oceansidepersonalinjurylawyerpros.com"] = {
    "mode": "fees",
    "fee_kind": "contingency",
    "table_head": "The published figures behind an Oceanside injury claim",
    "col_a": "The item",
    "col_b": "What the rule or the court publishes",
    "anchors": [
        {
            "label": "Percentage ceiling California writes for a collision or fall claim",
            "value": "None",
            "detail": "The state forbids an unconscionable or illegal fee and stops there. No California statute names a rate for an ordinary injury matter.",
            "source_name": "Cal. Rules of Prof. Conduct, rule 1.5(a)",
            "source_url": CALRULE,
        },
        {
            "label": "Complaint in an unlimited civil case, San Diego County",
            "value": "$435",
            "detail": "Charged on any first paper pleading more than $35,000, whether it is filed at the North County Division in Vista or downtown.",
            "source_name": "San Diego Superior Court civil fee schedule, item 1",
            "source_url": SDFEE,
        },
        {
            "label": "Court reporter per diem, San Diego Superior Court",
            "value": "$585 or $1,170",
            "detail": "Half day and full day for a civil proceeding that runs past an hour. San Diego sets its own per diem under Government Code section 68086(a)(2).",
            "source_name": "San Diego Superior Court civil fee schedule, item 68",
            "source_url": SDFEE,
        },
        {
            "label": "What Medi-Cal may take back out of a settlement",
            "value": "Never more than the patient keeps",
            "detail": "The Director cannot recover more than the beneficiary recovers after attorney fees and litigation costs are deducted from the settlement, judgment or award.",
            "source_name": "Cal. Welf. & Inst. Code 14124.78",
            "source_url": WIC1412478,
        },
    ],
    "fee_rows": [
        {
            "stage": "The one substantive limit on an injury fee",
            "share": "Not unconscionable",
            "note": "Unconscionability is judged on the facts existing when the agreement was signed, unless both sides expected later events to move the fee.",
            "source_name": "Cal. Rules of Prof. Conduct, rule 1.5(b)",
            "source_url": CALRULE,
        },
        {
            "stage": "Terms the contingency contract has to carry",
            "share": "Rate, costs, related matters",
            "note": "The agreed rate, how disbursements and costs hit both the fee and the recovery, and what else the client could owe outside the contract.",
            "source_name": "Cal. Bus. & Prof. Code 6147(a)(1)-(3)",
            "source_url": BPC6147,
        },
        {
            "stage": "The sentence the statute forces into the contract",
            "share": "Not set by law, negotiable",
            "note": "Outside a claim governed by section 6146, the writing must say the fee is not set by law but is negotiable between attorney and client.",
            "source_name": "Cal. Bus. & Prof. Code 6147(a)(4)",
            "source_url": BPC6147,
        },
        {
            "stage": "Motions after the first paper, San Diego County",
            "share": "$60, or $500",
            "note": "Sixty dollars for a discovery motion, a trial continuance or a noticed ex parte application; five hundred for summary judgment or adjudication.",
            "source_name": "San Diego Superior Court civil fee schedule, items 46 and 52",
            "source_url": SDFEE,
        },
        {
            "stage": "A case designated complex",
            "share": "$1,000 each side, $18,000 ceiling",
            "note": "One thousand dollars for all plaintiffs together and another thousand per defendant, capped at eighteen thousand for the whole case.",
            "source_name": "San Diego Superior Court civil fee schedule, items 20 and 21",
            "source_url": SDFEE,
        },
        {
            "stage": "Medical negligence, the single capped category",
            "share": "25% then 33%",
            "note": "The statutory ceiling applies to professional negligence claims against health care providers. It reaches no vehicle, premises or dog bite claim.",
            "source_name": "Cal. Bus. & Prof. Code 6146(a)",
            "source_url": BPC6146,
        },
    ],
}

# --------------------------------------------------------------- Santa Ana, CA
PRICING["santaanapersonalinjurylawyerpros.com"] = {
    "mode": "fees",
    "fee_kind": "contingency",
    "table_head": "Orange County court amounts, and the California rules that judge a fee",
    "col_a": "What is being priced",
    "col_b": "The figure on the schedule or in the rule",
    "anchors": [
        {
            "label": "Complaint in an unlimited civil case, Orange County",
            "value": "$435",
            "detail": "The uniform statewide first paper fee, charged at the Central Justice Center on Civic Center Drive and at every other Orange County location.",
            "source_name": "Orange County Superior Court civil fee schedule, item 1",
            "source_url": OCFEE,
        },
        {
            "label": "Electronic filing convenience fee, Orange County",
            "value": "$2.25",
            "detail": "Charged per transaction. Civil filings here move through the court's electronic system, so this line repeats every time a document is submitted.",
            "source_name": "Orange County Superior Court civil fee schedule, item 211",
            "source_url": OCFEE,
        },
        {
            "label": "Court reporter per diem, Orange County",
            "value": "$430 or $860",
            "detail": "Half day and full day for a civil proceeding lasting more than an hour. Each county sets its own amount, and Orange County's is not Los Angeles County's.",
            "source_name": "Orange County Superior Court civil fee schedule, item 68",
            "source_url": OCFEE,
        },
        {
            "label": "Rate the Legislature fixed for a Santa Ana crash claim",
            "value": "Zero",
            "detail": "California regulates the fee through a prohibition rather than a number: no agreement for, charge of, or collection of an unconscionable or illegal fee.",
            "source_name": "Cal. Rules of Prof. Conduct, rule 1.5(a)",
            "source_url": CALRULE,
        },
    ],
    "fee_rows": [
        {
            "stage": "How a fee gets tested later",
            "share": "All the facts at signing",
            "note": "The rule lists factors without limitation, among them overreaching, undisclosed material facts, the amount involved, the result, and informed consent.",
            "source_name": "Cal. Rules of Prof. Conduct, rule 1.5(b)",
            "source_url": CALRULE,
        },
        {
            "stage": "How costs are described in the contract",
            "share": "Effect on fee and recovery",
            "note": "The writing must state how disbursements and costs incurred prosecuting or settling the claim will affect both the fee and what the client receives.",
            "source_name": "Cal. Bus. & Prof. Code 6147(a)(2)",
            "source_url": BPC6147,
        },
        {
            "stage": "Any work billed outside a contingency",
            "share": "Writing above $1,000",
            "note": "Where total expense to the client including fees is reasonably foreseeable to pass one thousand dollars, the engagement has to be in writing.",
            "source_name": "Cal. Bus. & Prof. Code 6148(a)",
            "source_url": BPC6148,
        },
        {
            "stage": "Keeping a jury in an Orange County case",
            "share": "$150, then daily deposits",
            "note": "One hundred fifty dollars nonrefundable in advance, with later daily jury deposits set by the court rather than printed on the schedule.",
            "source_name": "Orange County Superior Court civil fee schedule, items 65 and 66",
            "source_url": OCFEE,
        },
        {
            "stage": "A second reporter, or moving the case out of the county",
            "share": "$430 per half day, $50",
            "note": "An extra reporter is billed at the same per diem as the first. Processing a venue change costs fifty dollars, and the motion itself is separate.",
            "source_name": "Orange County Superior Court civil fee schedule, items 69 and 56",
            "source_url": OCFEE,
        },
        {
            "stage": "The percentages that belong to malpractice only",
            "share": "25% before filing, 33% after",
            "note": "Section 6146 governs professional negligence claims against health care providers, measured on the net recovery. It says nothing about traffic collisions.",
            "source_name": "Cal. Bus. & Prof. Code 6146(a)",
            "source_url": BPC6146,
        },
    ],
}

# ----------------------------------------------------------- Virginia Beach, VA
PRICING["virginiabeachpersonalinjurylawyerpros.com"] = {
    "mode": "fees",
    "fee_kind": "contingency",
    "table_head": "What Virginia publishes for an injury claim brought in Virginia Beach",
    "col_a": "Item",
    "col_b": "The published amount or requirement",
    "anchors": [
        {
            "label": "Filing civil papers, Virginia Beach General District Court",
            "value": "$52",
            "detail": "The clerk's published cost to file civil papers, including a warrant in debt. The total varies with the amount in controversy.",
            "source_name": "Virginia Beach General District Court, Civil Division fees",
            "source_url": VBGDC,
        },
        {
            "label": "Injury or wrongful death claim a district court may hear",
            "value": "Up to $50,000",
            "detail": "Below $4,500 the district court has exclusive original jurisdiction; between that and fifty thousand dollars it shares jurisdiction with the circuit court.",
            "source_name": "Va. Code 16.1-77(1)",
            "source_url": VA1677,
        },
        {
            "label": "Maximum percentage the Commonwealth sets for injury work",
            "value": "Nothing",
            "detail": "Virginia opens its fee rule with the requirement that a fee be reasonable and then lists eight factors. No percentage appears in the rule.",
            "source_name": "Va. Rules of Prof. Conduct, Rule 1.5(a)",
            "source_url": VSB15,
        },
        {
            "label": "Window for written notice of an attorney's lien",
            "value": "45 days",
            "detail": "A lien attaches to a tort cause of action on contracting, but written notice must reach the client, the other side and the clerk within that window or before settlement.",
            "source_name": "Va. Code 54.1-3932(A)",
            "source_url": VA3932,
        },
    ],
    "fee_rows": [
        {
            "stage": "Statutory share of a district court civil filing",
            "share": "$36",
            "note": "The fee set by statute for court and magistrate services on a civil warrant or garnishment, of which ten dollars funds court technology.",
            "source_name": "Va. Code 16.1-69.48:2",
            "source_url": VA6948,
        },
        {
            "stage": "Getting the papers served",
            "share": "$12, or $75 out of state",
            "note": "Twelve dollars to serve civil process on one person, firm or corporation. Papers returnable outside Virginia cost seventy-five.",
            "source_name": "Va. Code 17.1-272(A)(1) and (C)",
            "source_url": VA17272,
        },
        {
            "stage": "What a contingent agreement must state in writing",
            "share": "Method, percentages, expenses",
            "note": "How the fee is computed, the percentages on settlement, trial and appeal, the expenses deducted, and whether they come out before or after the fee.",
            "source_name": "Va. Rules of Prof. Conduct, Rule 1.5(c)",
            "source_url": VSB15,
        },
        {
            "stage": "Matters where a contingent fee is off limits",
            "share": "Two categories",
            "note": "Domestic relations work, except in rare instances, and the defense of a criminal case. An injury claim sits outside both.",
            "source_name": "Va. Rules of Prof. Conduct, Rule 1.5(d)",
            "source_url": VSB15,
        },
        {
            "stage": "Medical malpractice, a limit on the verdict",
            "share": "Caps recovery, not the fee",
            "note": "Virginia's sliding statutory ceiling on the total recoverable from a health care provider climbs to three million dollars for acts after June 2031.",
            "source_name": "Va. Code 8.01-581.15",
            "source_url": VA58115,
        },
    ],
}

# ------------------------------------------------------------- Birmingham, AL
PRICING["birminghamtruckaccidentlawyerpros.com"] = {
    "mode": "fees",
    "fee_kind": "contingency",
    "table_head": "What Alabama and the federal carrier rules fix in a Jefferson County truck claim",
    "col_a": "What is being measured",
    "col_b": "The published figure",
    "anchors": [
        {
            "label": "Complaint over $50,000, Jefferson County Circuit Court",
            "value": "$351",
            "detail": "The clerk's civil filing fee for one plaintiff against one defendant above fifty thousand dollars, with ten dollars for each additional defendant.",
            "source_name": "Jefferson County Circuit Court, Civil Division filing fees",
            "source_url": JEFFCLERK,
        },
        {
            "label": "Federal liability insurance floor for an interstate truck",
            "value": "$750,000 to $5 million",
            "detail": "Seven hundred fifty thousand for nonhazardous freight, one million for oil and most hazardous materials, five million for bulk hazardous substances.",
            "source_name": "49 C.F.R. 387.9, Table 1",
            "source_url": CFR3879,
        },
        {
            "label": "Percentage cap Alabama places on an injury fee",
            "value": "None",
            "detail": "Alabama's rule bars a clearly excessive fee and lists nine factors for judging one, among them whether a written agreement was signed by the client.",
            "source_name": "Ala. R. Prof. Conduct 1.5(a)",
            "source_url": ALRULE,
        },
        {
            "label": "Demanding a jury in a Jefferson County civil case",
            "value": "$100",
            "detail": "A separate statutory line item, charged on top of the docket fee when a party asks for a jury rather than a bench trial.",
            "source_name": "Ala. Code 12-19-71(a)(13), Jefferson County fee distribution chart",
            "source_url": JEFFAOC,
        },
    ],
    "fee_rows": [
        {
            "stage": "Workers' compensation, the one capped percentage",
            "share": "15%",
            "note": "A judge fixes the plaintiff's attorney fee in a compensation case and it cannot exceed fifteen percent of the compensation awarded or paid.",
            "source_name": "Ala. Code 25-5-90(a)",
            "source_url": AL2590,
        },
        {
            "stage": "What a contingent agreement must contain",
            "share": "Writing, then a closing statement",
            "note": "The method of computing the fee, the percentages on settlement, trial and appeal, and the expenses deducted, plus a written accounting at the end.",
            "source_name": "Ala. R. Prof. Conduct 1.5(c)",
            "source_url": ALRULE,
        },
        {
            "stage": "Where Alabama forbids a contingent fee",
            "share": "Divorce and criminal defense",
            "note": "A fee turning on securing a divorce, on alimony, support or a property settlement in lieu of it, and any fee for defending a criminal case.",
            "source_name": "Ala. R. Prof. Conduct 1.5(d)",
            "source_url": ALRULE,
        },
        {
            "stage": "Smaller claim, and getting the truck driver served",
            "share": "$251, plus $10",
            "note": "The civil docket fee up to fifty thousand dollars, and ten dollars for every document the Jefferson County Sheriff's Department serves.",
            "source_name": "Jefferson County Circuit Court, Civil Division filing fees",
            "source_url": JEFFCLERK,
        },
        {
            "stage": "The motion a carrier's insurer files",
            "share": "$50",
            "note": "Judgment on the pleadings, default judgment or summary judgment each carry the same statutory motion fee in circuit court.",
            "source_name": "Ala. Code 12-19-71(a)(10), Jefferson County fee distribution chart",
            "source_url": JEFFAOC,
        },
        {
            "stage": "The lawyer's claim against a judgment",
            "share": "Ahead of everything but taxes",
            "note": "On actions and judgments for money the fee lien ranks above all liens except tax liens, and it attaches only once the defendant is served.",
            "source_name": "Ala. Code 34-3-61(b) and (d)",
            "source_url": AL3461,
        },
    ],
}

# ------------------------------------------- San Diego, CA wrongful termination
PRICING["sandiegowrongfulterminationlaw.com"] = {
    "mode": "fees",
    "fee_kind": "contingency",
    "table_head": "What California fixes in a San Diego wrongful termination fee, and who can be made to pay whose fees",
    "col_a": "The question",
    "col_b": "What the statute or rule answers",
    "anchors": [
        {
            "label": "Ceiling on a contingency percentage in an employment case",
            "value": "None set by California law",
            "detail": "A contingent fee is permitted and ordinary in employment work, and no statute or rule names a rate for it. The limit is a prohibition on an unconscionable or illegal fee.",
            "source_name": "Cal. Rules of Prof. Conduct, rule 1.5(a)",
            "source_url": CALRULE,
        },
        {
            "label": "Attorney fees in a FEHA discrimination or retaliation case",
            "value": "Court's discretion, one way in practice",
            "detail": "The court may award the prevailing party fees, costs and expert witness fees, but a winning employer gets nothing unless the action was frivolous, unreasonable or groundless.",
            "source_name": "Cal. Gov. Code 12965(c)(6)",
            "source_url": GOV12965,
        },
        {
            "label": "When an employment engagement must be in writing",
            "value": "Above $1,000",
            "detail": "Outside a contingency, any matter where total expense to the client including fees is reasonably foreseeable to exceed one thousand dollars needs a written contract.",
            "source_name": "Cal. Bus. & Prof. Code 6148(a)",
            "source_url": BPC6148,
        },
        {
            "label": "The employer's first paper in San Diego Superior Court",
            "value": "$435",
            "detail": "Each party other than the plaintiff pays the same first appearance fee in an unlimited civil case, which is what an answer to a termination complaint costs.",
            "source_name": "San Diego Superior Court civil fee schedule, item 5",
            "source_url": SDFEE,
        },
    ],
    "fee_rows": [
        {
            "stage": "The sentence a contingency contract must contain",
            "share": "Fee is negotiable",
            "note": "Because no statute governs the rate in an employment claim, the writing must say the fee is not set by law but is negotiable between attorney and client.",
            "source_name": "Cal. Bus. & Prof. Code 6147(a)(4)",
            "source_url": BPC6147,
        },
        {
            "stage": "The rest of what section 6147 requires",
            "share": "Signed duplicate at signing",
            "note": "The rate, the effect of costs on both fee and recovery, what the client may owe for related matters, and a duplicate signed copy handed over immediately.",
            "source_name": "Cal. Bus. & Prof. Code 6147(a)",
            "source_url": BPC6147,
        },
        {
            "stage": "An action for unpaid wages or benefits",
            "share": "Prevailing party, with a catch",
            "note": "Fees go to whoever prevails if requested at the outset, except that a winning employer recovers only if the court finds the employee sued in bad faith.",
            "source_name": "Cal. Labor Code 218.5(a)",
            "source_url": LAB2185,
        },
        {
            "stage": "A minimum wage or overtime claim",
            "share": "Employee only",
            "note": "The statute lets an underpaid employee recover the unpaid balance with interest, reasonable attorney fees and costs. It gives the employer no matching right.",
            "source_name": "Cal. Labor Code 1194(a)",
            "source_url": LAB1194,
        },
        {
            "stage": "Jury and reporter charges, San Diego Superior Court",
            "share": "$150 and $30",
            "note": "One hundred fifty dollars nonrefundable to preserve a jury, thirty dollars to have a civil proceeding of under an hour reported.",
            "source_name": "San Diego Superior Court civil fee schedule, items 65 and 67",
            "source_url": SDFEE,
        },
        {
            "stage": "The percentage cap that belongs to a different case type",
            "share": "25% and 33%, medical only",
            "note": "Section 6146 limits fees in professional negligence claims against health care providers. It has no bearing on a termination or retaliation claim.",
            "source_name": "Cal. Bus. & Prof. Code 6146(a)",
            "source_url": BPC6146,
        },
    ],
}

COPY = {}

COPY["oceansidepersonalinjurylawyerpros.com"] = ("""
Two sets of numbers touch an Oceanside injury claim: the amounts the San Diego \
Superior Court prints on its own fee schedule, and the fee, which California \
regulates without ever naming a percentage. This page keeps them apart.
""", """
### California writes no rate for an injury fee, and that is the finding

The first thing to settle is what the state does not do. Under rule 1.5(a) of the \
California Rules of Professional Conduct, a fee that is unconscionable, or one \
that is illegal, may not be agreed to, billed, or taken in the first place. No \
subdivision after it turns that ban into a percentage. So a page announcing "the \
California limit" on a rear-end collision claim on Coast Highway is describing a \
custom, not a statute.

Rule 1.5(b) explains how the prohibition is enforced. Unconscionability is \
measured on all the facts and circumstances existing when the agreement was \
entered into, except where both sides expected later events to affect the fee. \
The rule then lists considerations without closing the list: fraud or \
overreaching in setting the fee, material facts left undisclosed, the size of \
the fee against the value of the work actually performed, how sophisticated each \
side was, the amount at stake and the result, the experience of the lawyers, \
whether the fee was fixed or contingent, and whether the client gave informed \
consent. A percentage that looks unremarkable in a disputed-liability case with \
three carriers can look very different on a claim resolved with one letter.

### Because the rate is open, the contract is the document that decides it

Business and Professions Code section 6147 is where an injured person's leverage \
actually sits. The contract has to be written, signed by attorney and client, \
and the client walks away from the signing with a duplicate signed copy in hand. \
The rate the parties settled on has to appear. So does the treatment of \
disbursements and costs, and their effect on both fee and recovery, which is the \
clause people skip and then argue about. So does any compensation the client \
might owe on related matters the agreement leaves out. And unless the claim is \
one of the health care cases governed by section 6146, the writing has to say the \
rate is negotiable rather than fixed by law. When the writing misses a required \
element the \
agreement is voidable at the client's election, and the lawyer is left with a \
reasonable fee rather than the one in the contract.

Read the costs clause twice. Applying the same percentage before costs and after \
costs produces two different checks, and the difference on a claim with \
depositions and treating-physician testimony is not small.

### The court's own figures, which do not move with the facts

San Diego County publishes its civil fee schedule and the amounts are fixed. \
Opening an unlimited civil case, meaning any complaint pleading more than \
$35,000, is $435, and each other party pays the same on its first appearance. A \
motion or paper requiring a hearing is $60, whether it is a discovery motion, a \
request to move the trial date, a motion for new trial, or an ex parte \
application that requires notice to the other side. Summary judgment or summary \
adjudication is $500. Preserving a jury takes $150 in advance and the deposit is \
not refundable. Reporting a civil proceeding of less than an hour is $30, while \
anything longer is billed as a court reporter per diem of $585 for a half day \
and $1,170 for a full day. A complex designation adds $1,000 charged to the \
plaintiff side, plus $1,000 per defendant, and the complex fees stop at $18,000 \
for the whole case.

An Oceanside claim that reaches litigation usually files at the North County \
Division in Vista rather than downtown, and the schedule is the same either way. \
What changes with the courthouse is travel time, not the price of a filing.

### What comes off a recovery before anybody sees a check

Fees are one deduction and costs are another. The larger line items in a North \
County file tend to be deposition transcripts, records from Tri-City and other \
providers, treating-physician testimony, and any retained expert. Reimbursement \
claims are the third deduction, and they have their own statutory limits. Where \
Medi-Cal paid for treatment, Welfare and Institutions Code section 14124.78 \
provides that the Director shall in no event recover more than the beneficiary \
recovers after attorney fees and litigation costs paid by the beneficiary are \
deducted. That is a floor under the injured person's share, and it is worth \
asking about early, because a claim resolved without that arithmetic done can \
leave a person holding very little.

### The percentages that belong to a case this is not

California caps a contingency in exactly one setting. Section 6146 limits the \
fee in an action for injury against a health care provider based on professional \
negligence to 25 percent of the recovery when every party signs a release and \
settles before any complaint or demand for arbitration has been filed. Once the \
case passes that point the figure becomes 33 percent, measured against the net \
sum recovered. A lawyer who tried the case may move for more, and the court \
decides on evidence of good cause.

Those figures have nothing to do with a truck merging off the 78, a pedestrian \
struck near a Coast Highway crossing, or a fall in a Mission Avenue parking lot. \
When they appear on a general injury page, that page was assembled rather than \
checked.

### The practical version

Nothing in California law sets the rate, so the rate is negotiated and the \
statute requires the contract to say so. Costs sit separate from the fee, and the \
contract has to explain how they interact. Everything else is between an injured \
person and the lawyer that person picks.
""")

COPY["santaanapersonalinjurylawyerpros.com"] = ("""
An injury fee in Santa Ana is set by contract, not by statute, and the Orange \
County Superior Court prices its filings to the dollar on a schedule anyone can \
download. Here is what each of those documents actually says.
""", """
### Start with the document a client signs

Orange County's court fees are public and rigid. The fee agreement is neither, \
and it is the only place a percentage exists. Business and Professions Code \
section 6147 tells you what has to be inside it. The agreement is written and \
signed by both sides, and the client walks away with a duplicate signed copy the \
same day. It states the contingency rate the two of them agreed on. It states \
how disbursements and costs incurred in prosecuting or settling the claim will \
affect the fee and the client's recovery, which is the clause that decides how \
much money changes hands at the end. It states what the client might owe for \
related matters outside the agreement. And because a traffic or premises claim \
is not one of the health care cases covered by section 6146, the agreement must \
say the fee is not set by law but is negotiable between attorney and client. \
That is a legislative instruction to bargain, printed inside the form.

If the same firm bills anything hourly, a second statute applies. Section 6148 \
requires a written contract in any matter outside section 6147 where it is \
reasonably foreseeable that total expense to the client, fees included, will \
exceed $1,000.

### What "no cap" actually means in California

There is no percentage ceiling for an Orange County crash or fall claim. The \
California Rules of Professional Conduct address the subject at rule 1.5(a), \
which bars a fee that is unconscionable or otherwise illegal and stops there. \
Rule 1.5(b) then supplies the test, applied on the facts as they stood at signing \
unless the parties anticipated that later events would change the fee, and its \
factor list is expressly open-ended. Among them: overreaching during the \
negotiation; material facts withheld; what the work was actually worth set beside \
what the fee came to; how sophisticated each side was; how hard the questions \
were; the sum at stake and the outcome reached; deadlines the client imposed; the \
lawyers' experience; fixed versus contingent structure; informed consent. A \
reviewing court weighs those. It does not consult a table.

### The Orange County schedule, line by line

The court's civil fee schedule is where exact numbers live. A complaint in an \
unlimited civil case, over $35,000, is $435, and every other party pays $435 on \
its first paper. A motion or other paper requiring a hearing is $60 unless it is \
that party's first paper. Summary judgment or summary adjudication is $500. \
Keeping a jury costs $150 in advance, nonrefundable, followed by daily jury \
deposits in an amount the court sets. Court reporter per diem for a proceeding \
running past an hour is $430 a half day and $860 a full day, and an extra \
reporter is billed at the same rate. Processing a change of venue is $50, with \
the motion fee charged separately. A complex designation adds $1,000 for the \
plaintiff side and $1,000 per defendant, to an $18,000 ceiling.

Then there is the line nobody budgets for. Orange County charges an electronic \
filing convenience fee of $2.25 per transaction. One filing is trivial. A \
litigated claim with motions, declarations, notices and exhibits submits \
documents dozens of times, and the total lands somewhere real. It is a small \
example of the general rule that court costs arrive in a stream rather than a \
lump.

### Why the same claim costs more to work here than the schedule suggests

Filing fees are identical statewide, so the difference between a $3,000 cost file \
and a $30,000 one is never the clerk. It is depositions, records and experts. \
Santa Ana sits at the junction of the 5, the 22 and the 55, which means \
multi-vehicle collisions, commercial vehicles making deliveries into the county's \
industrial corridors, and drivers insured through carriers that litigate rather \
than settle. Add a language-access requirement for a deposition, which is \
routine in a city where a large share of households speak Spanish or Vietnamese \
at home, and the interpreter is another cost line the fee agreement should \
address before it appears.

### The trap: percentages borrowed from a different statute

Search for California contingency limits and someone will hand you 25 percent \
and 33 percent. Those come from Business and Professions Code section 6146, and \
they govern one thing: an action for injury or damage against a health care \
provider based on alleged professional negligence, with the percentage measured \
against the net sum recovered after costs and the two tiers turning on whether \
all parties signed a release before a complaint or arbitration demand was filed. \
The statute expressly refuses to treat the plaintiff's own medical expenses or a \
firm's overhead as deductible costs, and a lawyer who tried the case can move \
for more on a showing of good cause.

Nothing in section 6146 reaches a lane-change collision on Bristol Street or a \
slip in a Main Place walkway. A page that quotes those numbers for ordinary \
injury work has told you something about the page, not about the law.

### What to check before signing anything

Confirm the rate and whether it changes if the case is filed or tried. Confirm \
whether the percentage is calculated before or after costs come off. Confirm who \
advances costs and what happens to them if the claim recovers nothing. Confirm \
that the negotiability sentence is in the document, because the Legislature \
required it. Ask for the duplicate signed copy at the table rather than by mail. \
None of that is adversarial. It is the arithmetic the statute assumed a client \
would do.
""")

COPY["virginiabeachpersonalinjurylawyerpros.com"] = ("""
Virginia does not set a percentage for an injury fee. It sets a reasonableness \
standard, a written-terms requirement, a court schedule, and a lien notice \
deadline. This page puts each of those next to the rule or code section it comes \
from.
""", """
### The standard, and why no number follows it

The Virginia Rules of Professional Conduct handle fees through Rule 1.5, and \
subdivision (a) states the whole substantive limit in five words: a lawyer's fee \
shall be reasonable. Eight factors follow for testing one: hours and labor \
demanded alongside the skill required to do the work properly; whether the \
engagement shut out other employment; what lawyers in the locality customarily \
charge for comparable services; how much was at stake and what result came of it; \
deadlines set by the client or by the circumstances; how long the professional \
relationship has run; the reputation and experience the lawyers bring; and \
whether the arrangement is a fixed fee or a contingent one.

A percentage is absent from that list on purpose. The Commonwealth measures a fee \
against the work rather than against a table, which means a rate quoted as "the \
Virginia maximum" for a collision at Virginia Beach Boulevard and First Colonial \
is a market convention someone has dressed up as law.

Subdivision (c) is the operative paperwork rule for injury work. A contingent \
agreement has to put the method of computing the fee in writing, with the \
percentage attaching at settlement, at trial and on appeal, an account of \
litigation and other expenses chargeable against the recovery, and a statement of \
whether the fee is figured before those expenses are taken off or after them. At \
the end of the matter \
the client gets a written statement of the outcome and, if there was money, the \
remittance and how it was figured. Subdivision (d) marks the two places a \
contingent fee is barred in Virginia: domestic relations matters, except in rare \
instances, and defending a criminal case. An injury claim is neither.

### Which courthouse the claim goes to, because that decides the cost

Virginia sorts civil cases by amount before anything else. Under Va. Code \
16.1-77(1) the general district court has exclusive original jurisdiction over a \
claim for injury to person up to $4,500, and shares jurisdiction with the circuit \
court from there up to $50,000. The Virginia Beach General District Court \
publishes its own civil costs: $52 to file civil papers, with the exact figure \
depending on the amount in controversy, and $12 for each person served. Its Civil \
Division confirms the same $50,000 concurrent ceiling for personal injury and \
wrongful death claims.

Underneath that $52 sits a statutory component. Va. Code 16.1-69.48:2 fixes a $36 \
fee for all court and magistrate services on a civil warrant, garnishment, \
attachment or similar proceeding, with $10 of it apportioned to the Courts \
Technology Fund, collected when process issues. Service charges are statutory \
too: Va. Code 17.1-272(A)(1) sets $12 for serving civil process on a person, firm \
or corporation, subsection (B) sets $25 for a writ of possession or a levy, and \
subsection (C) sets $75 for papers returnable out of state. On a claim against an \
out-of-state trucking company or a franchise owner in another state, that last \
number is the one that shows up.

A district court case is faster and cheaper, and it is also a ceiling. A claim \
worth more than fifty thousand dollars belongs in circuit court, so choosing the \
cheaper forum to hold down filing costs is a decision about what the claim is \
worth.

### The lien deadline that catches people out

Va. Code 54.1-3932(A) gives a lawyer a lien on a tort cause of action as security \
for fees from the moment the client contracts. The lien only bites once written \
notice of the claim goes to the client or former client, the opposing party or \
that party's lawyer or agent, and the clerk of the court where a case is pending. \
Notice must come within 45 days of the end of the representation, or before \
settlement or adjustment in a tort case, whichever is earlier. A settlement made \
after that notice is void against the lien. For a client changing lawyers \
mid-claim, that is the provision that determines whether the first lawyer's fee \
follows the file.

### What actually moves the cost of working a Virginia Beach claim

Not the clerk. The variables are the same ones anywhere on the resort strip and \
the corridors feeding it: how many treating providers there are, whether records \
come from a military treatment facility or the Veterans Affairs system for one of \
the region's many service members and dependents, whether an out-of-state \
defendant has to be served, and whether an expert is needed on causation or \
future care. Each of those is a cost line, separate from the fee, and the written \
agreement is supposed to say who advances it and when it comes off.

### The cap that is not a fee cap

Virginia does cap money in one category, and it is regularly quoted wrong. Va. \
Code 8.01-581.15 limits the total amount recoverable for injury to or death of a \
patient in a malpractice action against a health care provider, on a scale that \
rises each year and reaches three million dollars for acts of malpractice \
occurring on or after July 1, 2031. That statute constrains the verdict or \
judgment. It says nothing about any lawyer's percentage, it applies only to \
malpractice, and it has no bearing on a rear-end collision on Independence \
Boulevard or a fall at a Lynnhaven store.

### The short version

Reasonable, in writing, with the expense order spelled out. A district court \
claim tops out at fifty thousand dollars and costs $52 plus $12 a defendant to \
start. Service out of state runs $75. The lien notice clock is 45 days. Anything \
presented as Virginia's statutory fee percentage does not exist.
""")

COPY["birminghamtruckaccidentlawyerpros.com"] = ("""
Alabama does not fix a percentage for a truck injury fee. It bars a clearly \
excessive one, requires the contingent agreement in writing, and publishes the \
Jefferson County court costs to the dollar. The federal carrier rules add \
insurance figures of their own.
""", """
### Alabama's rule uses a different adjective, and it matters

Most states test a fee against the word reasonable. Alabama's Rule of \
Professional Conduct 1.5(a) forbids agreeing to, billing, or collecting a fee \
that is clearly excessive, and gives nine factors for deciding whether one is: \
hours and labor spent, together with how novel and difficult the questions were \
and the skill they called for; the odds, if the client could see them, that the \
engagement would foreclose other work; what the locality customarily charges for \
comparable services; the sum at issue and the outcome reached; time limitations \
in play; how long and of what character the professional relationship has been; \
the ability, standing and experience of the lawyers involved; whether the fee is \
fixed or contingent; and whether a written fee agreement carries the client's \
signature.

That last factor is worth pausing on, because Alabama put the existence of a \
signed writing into the excessiveness analysis itself. No percentage appears \
anywhere in the rule. Alabama sets no ceiling on a contingency in a \
tractor-trailer case, and a figure presented as the state maximum is a practice, \
not a statute.

Rule 1.5(c) governs the paperwork. A contingent agreement goes in writing and \
spells out how the fee is computed: the percentages attaching at settlement, at \
trial and on appeal, which litigation and other expenses are charged against the \
recovery, and whether the percentage is applied before those expenses are \
subtracted or afterward. At the conclusion the lawyer owes the client a written \
statement of the outcome and, where there is a recovery, the remittance and the \
method of its determination. Rule 1.5(d) is the prohibition list: a fee may not \
ride on obtaining a divorce, nor on the size of alimony, support, or a property \
settlement standing in for them, and no contingent fee may be taken for defending \
a \
criminal matter.

### The 15 percent figure, and the case it belongs to

Search Alabama attorney fees and a hard number surfaces: fifteen percent. It is \
real and it is not an injury cap. Ala. Code 25-5-90(a) provides that no part of \
workers' compensation payable under the Act goes to the claimant's attorney \
unless the judge orders or approves the employment, and that the judge fixes the \
fee and the manner of its payment, which shall not exceed 15 percent of the \
compensation awarded or paid. That is a workers' compensation provision, applied \
by a judge in a compensation proceeding.

The distinction is live in a Birmingham truck case, because a driver hurt on the \
job in a commercial vehicle can have a compensation claim and a claim against the \
at-fault carrier running at the same time, under two different fee regimes. \
Anyone quoting the comp percentage as the limit on a third-party liability claim \
has merged two files.

### What the federal side publishes

Truck claims come with numbers no state prints. Under 49 C.F.R. 387.9, an \
interstate for-hire carrier operating a vehicle rated above 10,000 pounds must \
carry at least $750,000 in public liability coverage for nonhazardous property. \
The floor rises to $1,000,000 for oil and most hazardous materials and waste, and \
to $5,000,000 for bulk hazardous substances, bulk Division 1.1 through 1.3 \
explosives, and highway route controlled quantities of Class 7 radioactive \
material.

Those are minimums, not the coverage a given carrier actually bought, and they \
say nothing about what a claim is worth. What they do is set the questions to ask \
about the rigs moving through the I-20, I-59 and I-65 interchange: what the \
trailer was carrying, whether the load made the run a hazmat run, and who filed \
the coverage. That usually decides which insurer is at the table.

### Jefferson County's published costs

The Circuit Clerk publishes the civil filing fees. One plaintiff against one \
defendant is $251 where the claim is up to $50,000 and $351 above that or where \
the amount is unspecified, with $100 for each additional plaintiff up to a \
thousand-dollar total and $10 for each additional defendant. A jury demand is \
$100. Service through the Jefferson County Sheriff's Department adds $10 per \
document, a charge that also attaches to subpoenas, garnishments and executions. \
A subpoena itself is $12. A counterclaim, cross claim or third-party complaint is \
$297. Judgment on the pleadings, default judgment and summary judgment each carry \
a $50 motion fee, and the Administrative Office of Courts chart for Jefferson \
County ties those lines to Ala. Code 12-19-71.

Those figures are the small end of a truck file. Electronic control module \
downloads, driver qualification and hours-of-service records, maintenance \
histories, a reconstruction expert and multiple depositions are the real cost \
lines, they are separate from the fee, and Rule 1.5(c) requires the agreement to \
say whether they are deducted before or after the percentage is applied.

### One more Alabama provision worth knowing

Ala. Code 34-3-61 gives a lawyer a lien for fees. On papers and money already in \
hand the lien is possessory. On actions and judgments for money it is superior to \
every lien except a tax lien, and no one may satisfy the judgment until the fee \
claim is satisfied. The lien does not attach until the defendant has been served \
with summons, writ or other process, and a settlement reached before the \
defendant has actual notice of the filing discharges the claim. In a case where a \
client changes firms, that section, not the fee agreement, is what governs who \
gets paid out of the recovery.

### The short version

No cap on a contingency here, a clearly excessive fee prohibited, and the rate \
left to a written agreement that spells out the expense order. Fifteen percent is \
workers' compensation. Jefferson County charges $351 to open a claim over \
$50,000, $100 for a jury and $10 a document for service.
""")

COPY["sandiegowrongfulterminationlaw.com"] = ("""
A contingent fee is permitted and completely ordinary in a California employment \
case, and no California law caps the percentage. What the law does set is the \
contract requirements, the court's filing amounts, and which side can be made to \
pay the other's attorney fees.
""", """
### Yes, these cases are taken on contingency, and no, there is no percentage cap

Wrongful termination, retaliation, discrimination and unpaid wage claims are \
routinely handled on a contingent fee in California. Nothing in the Labor Code, \
the Government Code or the Business and Professions Code sets a rate for one. \
The single substantive limit is rule 1.5(a) of the California Rules of \
Professional Conduct, which prohibits making an agreement for, charging, or \
collecting an unconscionable or illegal fee, tested under rule 1.5(b) on the \
facts as they stood at signing. The rate is a negotiated term, and the statute \
below makes the contract admit that in writing.

The percentages people find online, 25 percent and 33 percent, come from \
Business and Professions Code section 6146, which limits fees in an action \
against a health care provider based on professional negligence. Medical \
negligence only. It has no application to a termination claim, and quoting it as \
an employment ceiling is simply wrong.

### What section 6147 requires the agreement to say

Section 6147 governs every contingency contract. It must be written and signed by \
both attorney and client, and the client receives a duplicate signed copy at the \
time it is entered into, not later. It must state the contingency rate the \
parties agreed on. It must state how disbursements and costs will affect both the \
fee and the client's recovery. It must state to what extent the client could owe \
compensation for related matters the contract does not cover, which in employment \
work is the clause that matters when one dispute produces a wage claim, an agency \
charge and a lawsuit. \
And because a termination claim is not a section 6146 case, the contract has to \
say the rate is negotiable between attorney and client rather than something the \
law sets. A contract missing a required term is voidable at the client's election, \
which leaves the lawyer with a reasonable fee instead of the agreed one.

Section 6148 covers the other half of an employment engagement. Where a matter \
falls outside section 6147 and the foreseeable total expense to the client, fees \
included, will exceed $1,000, the contract for services must be in writing. \
Hourly advice on a severance agreement sits here, and few such engagements come \
in under the threshold.

### Fee shifting: who can be made to pay whose fees

This is the part that changes the economics of an employment case, and it is not \
a cap on anything.

Under Government Code section 12965(c)(6), in a civil action brought under the \
Fair Employment and Housing Act the court may in its discretion award the \
prevailing party, including the department, reasonable attorney fees and costs \
including expert witness fees. The subdivision then adds an asymmetry: \
notwithstanding Code of Civil Procedure section 998, a prevailing defendant shall \
not be awarded fees and costs unless the court finds the action was frivolous, \
unreasonable, or groundless when brought, or that the plaintiff continued to \
litigate after it clearly became so. A winning employee can shift fees to the \
employer; a winning employer generally cannot, absent that finding.

Labor Code section 218.5(a) covers an action for nonpayment of wages, fringe \
benefits, or health, welfare or pension fund contributions. The court shall award \
fees and costs to the prevailing party if any party requested them when the \
action was initiated, except that where the prevailing party is not an employee, \
fees and costs are awarded only if the court finds the employee brought the \
action in bad faith. Labor Code section 1194(a) runs one way only: an employee \
paid less than the legal minimum wage or overtime compensation may recover the \
unpaid balance with interest, reasonable attorney fees and costs of suit, and the \
employer gets no reciprocal right.

Two things follow. A fee-shifting statute is not a percentage limit, and no one \
should describe it as one. And because a court-awarded fee and a contingency can \
both arrive in the same case, the written agreement should say how they interact.

### What the San Diego courthouse charges

The Superior Court of California, County of San Diego publishes its civil fee \
schedule, and an employment case follows it like any other. A complaint in an \
unlimited civil case, over $35,000, is $435, and the employer pays $435 on its \
first appearance. A motion requiring a hearing is $60; summary judgment or \
adjudication, the motion that ends a large share of termination cases before \
trial, is $500. Preserving a jury takes $150 in advance, nonrefundable. A civil \
proceeding under an hour is reported for $30.

### What is separate from the fee

Costs. Deposition transcripts for a supervisor, a human resources manager and a \
coworker witness; personnel and payroll records; an economist on lost earnings \
where the termination ended a long tenure. In a San Diego market weighted toward \
defense contractors, hospital systems, biotech employers and bayfront \
hospitality, those files are document heavy. Ask which costs are advanced, what \
happens to them if the case recovers nothing, and whether the percentage applies \
before or after they come off.

### The short version

Contingency: permitted, ordinary, no California ceiling. The contract: written, \
duplicate copy at signing, rate stated, cost treatment stated, negotiability \
stated. Fee shifting: available to a winning employee under FEHA and the wage \
statutes, available to a winning employer only on a bad-faith or frivolousness \
finding.
""")


def main():
    for domain, block in PRICING.items():
        d = SITES / domain
        sj = d / "site.json"
        data = json.loads(sj.read_text())
        keys = list(data.keys())
        new = {}
        for k in keys:
            new[k] = data[k]
            if k == "schema":
                new["pricing"] = block
        if "pricing" not in new:
            new["pricing"] = block
        sj.write_text(json.dumps(new, indent=1, ensure_ascii=False) + "\n")

        cm = d / "copy.md"
        text = cm.read_text().rstrip("\n")
        if "## pricing_lede" in text:  # idempotent re-run
            text = text.split("## pricing_lede")[0].rstrip("\n")
        lede, body = COPY[domain]
        text += "\n\n## pricing_lede\n\n" + lede.strip() + "\n\n## pricing_body\n\n" + body.strip() + "\n"
        cm.write_text(text)
        print("wrote", domain)


if __name__ == "__main__":
    main()
