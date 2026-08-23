"""Batch 4: add /pricing/ (mode fees, contingency) to five car-accident sites."""
import json, pathlib, collections

SITES = pathlib.Path(__file__).parent / "sites"

PRICING = {
"concordcaraccidentlawyerpros.com": {
  "mode": "fees",
  "fee_kind": "contingency",
  "table_head": "What North Carolina law and the State Bar rule fix in a Cabarrus County injury claim",
  "col_a": "What it covers",
  "col_b": "What the rule or statute sets",
  "anchors": [
    {"label": "Percentage ceiling on an injury fee",
     "value": "None set",
     "detail": "The State Bar rule bars a clearly excessive fee and lists eight factors for measuring one, but it names no percentage for a motor vehicle claim.",
     "source_name": "N.C. Rule of Professional Conduct 1.5(a)",
     "source_url": "https://www.ncbar.gov/for-lawyers/ethics-and-governing-rules/rules-of-professional-conduct/10-119-client-lawyer-relationship/15-fees/"},
    {"label": "Superior court civil filing total",
     "value": "$200",
     "detail": "The General Court of Justice fee of $180, a $16 facilities fee and a $4 telecommunications and data connectivity fee, paid when the complaint reaches the clerk.",
     "source_name": "N.C. Judicial Branch civil court costs chart",
     "source_url": "https://www.nccourts.gov/assets/documents/publications/Civil-Costs-effective-January-1-2025.pdf"},
    {"label": "Ceiling on a medical provider lien",
     "value": "50%",
     "detail": "A provider claiming against the recovery is limited by statute to half of the damages recovered, measured apart from attorneys' fees.",
     "source_name": "N.C. Gen. Stat. 44-50",
     "source_url": "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_44/GS_44-50.html"}
  ],
  "fee_rows": [
    {"stage": "Share of a car wreck recovery",
     "share": "No numeric cap",
     "note": "North Carolina names no percentage. Reasonableness governs, measured by the difficulty, the result, local custom, and whether the fee is fixed or contingent.",
     "source_name": "N.C. Rule of Prof. Conduct 1.5(a)",
     "source_url": "https://www.ncbar.gov/for-lawyers/ethics-and-governing-rules/rules-of-professional-conduct/10-119-client-lawyer-relationship/15-fees/"},
    {"stage": "Form the agreement has to take",
     "share": "Signed writing",
     "note": "It must give the method, the percentages for settlement, trial and appeal, the expenses deducted, and whether they come off before or after.",
     "source_name": "N.C. Rule of Prof. Conduct 1.5(c)",
     "source_url": "https://www.ncbar.gov/for-lawyers/ethics-and-governing-rules/rules-of-professional-conduct/10-119-client-lawyer-relationship/15-fees/"},
    {"stage": "Fee tied to the result of a criminal charge",
     "share": "Prohibited",
     "note": "Barred outright for a criminal defendant, with a narrow carve-out for representation in a criminal or civil asset forfeiture proceeding.",
     "source_name": "N.C. Rule of Prof. Conduct 1.5(d)(1)",
     "source_url": "https://www.ncbar.gov/for-lawyers/ethics-and-governing-rules/rules-of-professional-conduct/10-119-client-lawyer-relationship/15-fees/"},
    {"stage": "Workers' compensation fee on the same injury",
     "share": "Commission approval",
     "note": "The Industrial Commission weighs time invested, amount involved, results achieved, customary charge and skill, then allows what it finds reasonable.",
     "source_name": "N.C. Gen. Stat. 97-90(a), (c)",
     "source_url": "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_97/GS_97-90.html"},
    {"stage": "Opening a civil file with the clerk",
     "share": "$200 superior · $150 district · $96 magistrate",
     "note": "Three totals, decided by the division the complaint goes to. Each already includes the facilities and connectivity add-ons.",
     "source_name": "N.C. Judicial Branch civil costs chart",
     "source_url": "https://www.nccourts.gov/assets/documents/publications/Civil-Costs-effective-January-1-2025.pdf"},
    {"stage": "Sheriff service of civil process",
     "share": "$30 per item",
     "note": "Charged for every item the sheriff serves, so a wreck with two defendants and a corporate registered agent multiplies it.",
     "source_name": "N.C. Gen. Stat. 7A-311(a)(1), costs chart",
     "source_url": "https://www.nccourts.gov/assets/documents/publications/Civil-Costs-effective-January-1-2025.pdf"}
  ]
},

"harrisburgcaraccidentlawyerpros.com": {
  "mode": "fees",
  "fee_kind": "contingency",
  "table_head": "What Pennsylvania law fixes for a Dauphin County crash claim, and what it leaves open",
  "col_a": "What it covers",
  "col_b": "What Pennsylvania sets",
  "anchors": [
    {"label": "Ceiling on an auto injury fee percentage",
     "value": "Not fixed",
     "detail": "Pennsylvania's conduct rule prohibits an illegal or clearly excessive fee and gives eight measuring factors. No percentage appears anywhere in it.",
     "source_name": "Pa. R.P.C. 1.5(a)",
     "source_url": "https://www.padisciplinaryboard.org/for-attorneys/rules/rule/3/the-rules-of-professional-conduct"},
    {"label": "Workers' compensation counsel fee limit",
     "value": "20%",
     "detail": "The one hard number in Pennsylvania fee law: a judge may approve counsel fees only up to a fifth of the award or of a compromise and release settlement.",
     "source_name": "Pa. Workers' Compensation Act, Sec. 442",
     "source_url": "https://www.pa.gov/content/dam/copapwp-pagov/en/dli/documents/individuals/workers-compensation/publications/documents/wc-act/wcact.pdf"},
    {"label": "District court cost, claim of $4,001 to $12,000",
     "value": "$171",
     "detail": "The 2026 statutory cost for a civil case before a magisterial district judge, the court that hears smaller Dauphin County claims. Postage is extra.",
     "source_name": "204 Pa. Code 29.402 (42 Pa.C.S. 1725.1), 2026 schedule",
     "source_url": "https://www.pacourts.us/assets/opinions/Supreme/out/644%20JADattachment.pdf"},
    {"label": "Medical benefit every auto policy must carry",
     "value": "$5,000",
     "detail": "The statutory floor for first-party medical coverage in Pennsylvania, which is what pays early treatment before any liability claim resolves.",
     "source_name": "75 Pa.C.S. 1711(a)",
     "source_url": "https://www.legis.state.pa.us/WU01/LI/LI/CT/HTM/75/00.017.011.000..HTM"}
  ],
  "fee_rows": [
    {"stage": "Percentage taken from a crash recovery",
     "share": "No statutory ceiling",
     "note": "Judged against eight factors: fixed or contingent, difficulty, preclusion of other work, local custom, amount and result, deadlines, relationship, ability.",
     "source_name": "Pa. R.P.C. 1.5(a)",
     "source_url": "https://www.padisciplinaryboard.org/for-attorneys/rules/rule/3/the-rules-of-professional-conduct"},
    {"stage": "Paperwork the rule demands",
     "share": "Writing, plus a closing statement",
     "note": "The agreement states percentages and expense treatment; at the end the lawyer owes a written statement showing the outcome and the remittance.",
     "source_name": "Pa. R.P.C. 1.5(b), (c)",
     "source_url": "https://www.padisciplinaryboard.org/for-attorneys/rules/rule/3/the-rules-of-professional-conduct"},
    {"stage": "Work injury claim instead of a liability claim",
     "share": "20% maximum",
     "note": "Counsel fees need judge approval and cannot exceed a fifth of the award, or a fifth of a compromise and release settlement amount.",
     "source_name": "Pa. Workers' Comp Act, Sec. 442",
     "source_url": "https://www.pa.gov/content/dam/copapwp-pagov/en/dli/documents/individuals/workers-compensation/publications/documents/wc-act/wcact.pdf"},
    {"stage": "Cost of starting a small civil case",
     "share": "$68.50 · $91 · $114 · $171",
     "note": "Four 2026 tiers before a magisterial district judge, set by claim size from $500 or less up to the $12,000 limit.",
     "source_name": "204 Pa. Code 29.402, 2026 costs",
     "source_url": "https://www.pacourts.us/assets/opinions/Supreme/out/644%20JADattachment.pdf"},
    {"stage": "Enforcing a judgment once entered",
     "share": "$51.50",
     "note": "The 2026 statutory cost of an order of execution in that court, with $23 more for an objection to levy.",
     "source_name": "204 Pa. Code 29.402, 2026 costs",
     "source_url": "https://www.pacourts.us/assets/opinions/Supreme/out/644%20JADattachment.pdf"}
  ]
},

"louisvillecaraccidentlawyerpros.com": {
  "mode": "fees",
  "fee_kind": "contingency",
  "table_head": "What Kentucky law and Supreme Court rule fix for a Jefferson County collision claim",
  "col_a": "What it covers",
  "col_b": "What Kentucky sets",
  "anchors": [
    {"label": "Cap on a collision fee percentage",
     "value": "None",
     "detail": "Kentucky's rule forbids an unreasonable fee and an unreasonable amount for expenses, then lists eight factors. It states no percentage for injury work.",
     "source_name": "Ky. SCR 3.130(1.5)(a)",
     "source_url": "https://www.kycourts.gov/Courts/Supreme-Court/Supreme%20Court%20Orders/200905.pdf"},
    {"label": "Circuit Court civil filing fee",
     "value": "$188",
     "detail": "Paid to the circuit clerk when the case is filed, with a $20 court technology fee and other required charges on top.",
     "source_name": "Supreme Court of Kentucky order 2026-15, CR 3.02(1)",
     "source_url": "https://www.kycourts.gov/Courts/Supreme-Court/Supreme%20Court%20Orders/202615.pdf"},
    {"label": "Ceiling on a workers' compensation fee",
     "value": "$18,000",
     "detail": "Kentucky's one tiered fee schedule: a fifth of the first $25,000, 15 percent of the next $25,000, a tenth of the rest, and never more than this.",
     "source_name": "KRS 342.320(2)(a)",
     "source_url": "https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=47622"},
    {"label": "Limit on basic reparation benefits",
     "value": "$10,000",
     "detail": "The statutory maximum for all economic loss to one injured person from one crash, no matter how many carriers owe the benefit.",
     "source_name": "KRS 304.39-020(2)",
     "source_url": "https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=57854"}
  ],
  "fee_rows": [
    {"stage": "Share of a collision recovery",
     "share": "No fixed ceiling",
     "note": "The test is reasonableness across eight listed factors, including local custom, the result obtained and whether the fee is fixed or contingent.",
     "source_name": "Ky. SCR 3.130(1.5)(a)",
     "source_url": "https://www.kycourts.gov/Courts/Supreme-Court/Supreme%20Court%20Orders/200905.pdf"},
    {"stage": "Written agreement and expense warning",
     "share": "Signed by the client",
     "note": "It must state percentages, list expenses deducted, say whether they come off first, and warn plainly about expenses owed even after a loss.",
     "source_name": "Ky. SCR 3.130(1.5)(c)",
     "source_url": "https://www.kycourts.gov/Courts/Supreme-Court/Supreme%20Court%20Orders/200905.pdf"},
    {"stage": "Matters where a result-based fee is barred",
     "share": "Criminal and divorce",
     "note": "Kentucky forbids it for a criminal defendant and in domestic cases turning on divorce, alimony or support, apart from liquidated arrearages.",
     "source_name": "Ky. SCR 3.130(1.5)(d)",
     "source_url": "https://www.kycourts.gov/Courts/Supreme-Court/Supreme%20Court%20Orders/200905.pdf"},
    {"stage": "Work injury fee schedule",
     "share": "20% / 15% / 10%, capped at $18,000",
     "note": "Approved by an administrative law judge, paid from the award, with the approval motion due inside 30 days of finality.",
     "source_name": "KRS 342.320(2)(a), (3)",
     "source_url": "https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=47622"},
    {"stage": "Filing the lawsuit in Jefferson Circuit Court",
     "share": "$188 plus $20",
     "note": "The rule adds a court technology fee and other required charges such as the court facility and library fees to the base filing fee.",
     "source_name": "Ky. CR 3.02(1), 2026 order",
     "source_url": "https://www.kycourts.gov/Courts/Supreme-Court/Supreme%20Court%20Orders/202615.pdf"},
    {"stage": "Threshold before pain and suffering is claimable",
     "share": "$1,000",
     "note": "Medical expense benefits must pass that figure unless a fracture, permanent injury, disfigurement, loss of a body member or death is involved.",
     "source_name": "KRS 304.39-060(2)(b)",
     "source_url": "https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=30030"}
  ]
},

"modestocaraccidentlawyerpros.com": {
  "mode": "fees",
  "fee_kind": "contingency",
  "table_head": "What California fixes for a Stanislaus County injury claim, and where the caps really apply",
  "col_a": "What it covers",
  "col_b": "What California sets",
  "anchors": [
    {"label": "Statutory percentage for a traffic collision claim",
     "value": "None",
     "detail": "The State Bar rule bars an unconscionable or illegal fee, and the fee statute for injury contracts requires the contract to say the rate is negotiable.",
     "source_name": "Cal. Rule of Professional Conduct 1.5(a)",
     "source_url": "https://www.calbar.ca.gov/legal-professionals/rules/rules-professional-conduct/current-rules-professional-conduct/chapter-1-lawyer-client-relationship"},
    {"label": "Medical negligence ceiling, before a filing",
     "value": "25%",
     "detail": "California's only numeric fee ceiling reaches claims against health care providers, and it drops to this level when the release is signed before anything is filed.",
     "source_name": "Cal. Bus. & Prof. Code 6146(a)(1)",
     "source_url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=6146."},
    {"label": "First paper, unlimited civil case",
     "value": "$435",
     "detail": "Due from the plaintiff when a case worth more than $35,000 is filed, and again from every other party that files a first paper.",
     "source_name": "Statewide Civil Fee Schedule, eff. Jan. 1, 2026 (Gov. Code 70611)",
     "source_url": "https://courts.ca.gov/system/files/file/statewide-civil-fee-schedule-eff-01012026.pdf"},
    {"label": "Advance jury fee",
     "value": "$150",
     "detail": "A nonrefundable deposit required to keep the right to a jury, with daily jury deposits set separately by the court once trial begins.",
     "source_name": "Cal. Code Civ. Proc. 631(b), 2026 fee schedule",
     "source_url": "https://courts.ca.gov/system/files/file/statewide-civil-fee-schedule-eff-01012026.pdf"}
  ],
  "fee_rows": [
    {"stage": "Share of a vehicle injury recovery",
     "share": "No cap in statute",
     "note": "Only the unconscionable-or-illegal standard applies. The legislature wrote percentage limits for medical negligence claims and left driving cases out.",
     "source_name": "Cal. Rule of Prof. Conduct 1.5(a)",
     "source_url": "https://www.calbar.ca.gov/legal-professionals/rules/rules-professional-conduct/current-rules-professional-conduct/chapter-1-lawyer-client-relationship"},
    {"stage": "What the contract must tell the client",
     "share": "Rate is negotiable",
     "note": "The statute requires that sentence whenever the medical negligence limits do not apply, plus a duplicate signed copy handed over at signing.",
     "source_name": "Cal. Bus. & Prof. Code 6147(a)",
     "source_url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=6147."},
    {"stage": "Claim against a health care provider",
     "share": "25% before filing · 33% after",
     "note": "Measured on the net sum after costs, and a higher share needs a motion showing good cause to the court or arbitrator.",
     "source_name": "Cal. Bus. & Prof. Code 6146",
     "source_url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=6146."},
    {"stage": "Filing in Stanislaus County Superior Court",
     "share": "$435",
     "note": "Charged on the complaint in an unlimited civil case and on each other party's first paper, which is why defense answers add up.",
     "source_name": "2026 Statewide Civil Fee Schedule",
     "source_url": "https://courts.ca.gov/system/files/file/statewide-civil-fee-schedule-eff-01012026.pdf"},
    {"stage": "Keeping a jury trial available",
     "share": "$150 nonrefundable",
     "note": "Deposited in advance under the code, then daily jury deposits are set by the court for each day the panel sits.",
     "source_name": "Cal. Code Civ. Proc. 631(b), (e)",
     "source_url": "https://courts.ca.gov/system/files/file/statewide-civil-fee-schedule-eff-01012026.pdf"},
    {"stage": "Case designated complex",
     "share": "$1,000 per side",
     "note": "One charge covers all plaintiffs, then each defendant owes the same, with a total of $18,000 for the whole case.",
     "source_name": "Cal. Gov. Code 70616, 2026 fee schedule",
     "source_url": "https://courts.ca.gov/system/files/file/statewide-civil-fee-schedule-eff-01012026.pdf"}
  ]
},

"oxnardcaraccidentlawyerpros.com": {
  "mode": "fees",
  "fee_kind": "contingency",
  "table_head": "What the law sets for a Ventura County crash claim, priced from the court's own schedule",
  "col_a": "What it covers",
  "col_b": "What the rule, statute or court sets",
  "anchors": [
    {"label": "Legal limit on a crash fee percentage",
     "value": "No number",
     "detail": "California measures an injury fee against the unconscionable-or-illegal standard. The percentage limits in the fee statute reach medical negligence claims only.",
     "source_name": "Cal. Rule of Professional Conduct 1.5(a)",
     "source_url": "https://www.calbar.ca.gov/legal-professionals/rules/rules-professional-conduct/current-rules-professional-conduct/chapter-1-lawyer-client-relationship"},
    {"label": "Complaint over $35,000, Ventura County",
     "value": "$435",
     "detail": "The court's published figure for an initial complaint, petition or application above the unlimited civil line, and the same amount per answering defendant.",
     "source_name": "Ventura County Superior Court fee answers",
     "source_url": "https://ventura.courts.ca.gov/general-information/frequently-asked-questions"},
    {"label": "Motion after the first appearance",
     "value": "$60",
     "detail": "Charged by the Ventura civil division on each motion once the first appearance fee has already been paid, which is what makes discovery fights expensive.",
     "source_name": "Ventura County Superior Court, Civil Division",
     "source_url": "https://ventura.courts.ca.gov/divisions/civil"},
    {"label": "Small claims filing, up to $12,500",
     "value": "$75",
     "detail": "The court's top small claims tier for a natural person, with $30 and $50 tiers below it and $15 per defendant for certified mail service.",
     "source_name": "Ventura County Superior Court form VN139",
     "source_url": "https://ventura.courts.ca.gov/system/files/vn139.pdf"}
  ],
  "fee_rows": [
    {"stage": "Fee taken from a collision settlement",
     "share": "Unregulated by percentage",
     "note": "California polices it through the unconscionable-or-illegal test rather than a ceiling, so the written contract carries the whole burden.",
     "source_name": "Cal. Rule of Prof. Conduct 1.5(a)",
     "source_url": "https://www.calbar.ca.gov/legal-professionals/rules/rules-professional-conduct/current-rules-professional-conduct/chapter-1-lawyer-client-relationship"},
    {"stage": "Six things the injury contract must contain",
     "share": "Voidable if missed",
     "note": "Miss any required provision and the plaintiff may void the agreement, leaving the lawyer entitled only to a reasonable fee.",
     "source_name": "Cal. Bus. & Prof. Code 6147(a), (b)",
     "source_url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=6147."},
    {"stage": "Where percentages truly are capped",
     "share": "Health care provider claims",
     "note": "A quarter of a pre-complaint settlement and a third after filing, computed on the net sum left once disbursements come out.",
     "source_name": "Cal. Bus. & Prof. Code 6146(a), (c)(1)",
     "source_url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=6146."},
    {"stage": "Opening and answering a Ventura civil case",
     "share": "$435 · $370 · $225",
     "note": "Tiers turn on the amount demanded: above $35,000, above $10,000, or $10,000 and under. Each defendant pays to respond.",
     "source_name": "Ventura County Superior Court fee answers",
     "source_url": "https://ventura.courts.ca.gov/general-information/frequently-asked-questions"},
    {"stage": "Appealing an unlimited civil decision",
     "share": "$775 plus $100",
     "note": "The larger amount goes to the Court of Appeal; the deposit goes to the Ventura clerk for preparing the transcript.",
     "source_name": "Ventura County Superior Court, Civil Division",
     "source_url": "https://ventura.courts.ca.gov/divisions/civil"},
    {"stage": "Small claims route for a minor collision",
     "share": "$30 · $50 · $75",
     "note": "Set by claim size, rising to $100 for anyone who has filed more than twelve claims in the previous twelve months.",
     "source_name": "Ventura County Superior Court form VN139",
     "source_url": "https://ventura.courts.ca.gov/system/files/vn139.pdf"}
  ]
}
}

COPY = {}

COPY["concordcaraccidentlawyerpros.com"] = ("""North Carolina never wrote down a percentage for what may be taken out of an injury settlement, so this page lays out the standard the State Bar rule uses instead, the costs the Cabarrus County clerk collects to open a civil file, and the statute that limits what a treating provider can pull from the same recovery.""",
"""### The rule sets a standard, not a number

Rule 1.5(a) of the North Carolina Rules of Professional Conduct prohibits an illegal or
clearly excessive fee, and prohibits charging a clearly excessive amount for expenses on
top of it. The rule then names the eight things a fee gets measured against: the time and
labor required along with the difficulty of the questions and the skill needed; whether
taking the matter blocks other work; the fee customarily charged in this locality for
similar legal services; the amount at stake and the result reached; deadlines imposed by
the client or by circumstances; how long the professional relationship has run; the
experience, reputation and ability of the lawyer; and whether the fee is fixed or
contingent.

Read that list again and notice what is missing. There is no percentage in it. Anyone
searching for "the North Carolina percentage" is hunting for a figure the rule does not
contain, and a page that hands one over is inventing it. The standard is elastic on
purpose, because a rear-end claim resolved on a first demand and a disputed left-turn case
tried to a Cabarrus jury are not the same piece of work.

### Where the state does write down a limit

Two places worth knowing about. A work injury runs on a different track: G.S. 97-90 makes
attorney fees subject to Industrial Commission approval, and the Commission weighs time
invested, amount involved, results achieved, whether the fee is fixed or contingent, the
customary charge for similar services, skill level, and the nature of the services. The
agreement has to be filed with the hearing officer before the hearing closes.

The second limit protects the injured person from a different direction. Under G.S. 44-50,
a lien asserted against the recovery by a provider who treated the injuries cannot exceed
half of the damages recovered, and that fifty percent is figured apart from attorneys'
fees. On a modest settlement with a long course of treatment, that statute is often the
only reason money reaches the person who was hurt.

### The sentence that quietly changes the arithmetic

Rule 1.5(c) requires the agreement to be in a writing signed by the client, and requires
it to state the method of calculation, the percentages that apply on settlement, at trial
and on appeal, the litigation and other expenses deducted from the recovery, and whether
those expenses come off before or after the fee is calculated. That last clause is the one
people skim.

Take a $60,000 settlement carrying $9,000 of case expenses and a one-third share. Compute
the share on the gross and the fee is $20,000, expenses come out next, and $31,000 is
left. Subtract expenses first and the share is figured on $51,000, the fee is $17,000, and
$34,000 is left. Same percentage, same expenses, $3,000 of difference decided by one
sentence in the paperwork.

### What the courthouse itself charges

Court costs are separate from any fee and go to the state, not to a firm. A civil
complaint in superior court carries a $200 total: a General Court of Justice fee of $180,
of which ninety-five cents goes to the State Bar legal aid account, plus a $16 facilities
fee and a $4 telecommunications and data connectivity fee. The district court total is
$150 and a magistrate small claims filing is $96. Every item of civil process the sheriff
serves adds $30, so a collision involving two drivers and a trucking company's registered
agent is billed three times.

Then come the real expenses of proving a claim: the crash report, certified records from
each treating provider, deposition transcripts, a mediator's charge, and in a contested
liability case a reconstruction review of a wreck on Concord Parkway or the US-29 corridor.

### Reading the paper before signing it

Ask where the percentage moves and what event moves it. Ask whether expenses are advanced
and what happens to them if the claim ends with nothing collected. Ask for the itemized
list of anticipated expenses and whether approval is needed before an expert is hired.
Ask how a provider lien under the fifty percent statute will be handled, and who
negotiates reimbursement claims that arise under other law.

### The traps

A tier that rises "on filing" without defining filing. An expense line with no itemization
and no approval threshold. A verbal assurance about lien reduction that never reaches the
signed writing. And one absolute: Rule 1.5(d)(1) bars a fee tied to the result of a
criminal case, with a narrow exception for an asset forfeiture proceeding, so any pitch
that bundles a traffic charge and an injury claim into one outcome-based number is
describing something the rule forbids.""")

COPY["harrisburgcaraccidentlawyerpros.com"] = ("""Pennsylvania puts one hard percentage in its fee law, and it is not the one drivers expect: twenty percent belongs to workers' compensation, while an auto claim in Dauphin County is governed by a reasonableness rule with no ceiling at all, alongside statutory court costs and a required medical benefit that are fixed to the dollar.""",
"""### The auto claim has no ceiling, and that is the finding

Pennsylvania Rule of Professional Conduct 1.5(a) says a lawyer shall not enter into an
agreement for, charge, or collect an illegal or clearly excessive fee. Eight factors decide
propriety: whether the fee is fixed or contingent; time, labor, novelty and skill; whether
the engagement precludes other employment; the fee customarily charged in the locality;
the amount involved and the results obtained; time limits imposed by the client or the
circumstances; the nature and length of the relationship; and the experience, reputation
and ability of the lawyer. A comment to the rule acknowledges that other law may impose a
ceiling on the percentage. For a Harrisburg collision claim, no such law does.

### The twenty percent everyone half-remembers

Section 442 of the Workers' Compensation Act is where the number lives. Counsel fees
agreed between a claimant and counsel must be approved by the workers' compensation judge
or the board, and may not exceed twenty per centum of the amount awarded. The same section
caps fees at a fifth of a compromise and release settlement, and it lets a judge award a
reasonable fee without regard to any percentage where counsel's work produces a favorable
result with no immediate award, as in a termination or suspension fight.

That figure gets repeated on the street as though it governed every injury in
Pennsylvania. It does not. If a Camp Hill delivery driver is hit on Cameron Street while
working, the compensation side of that same crash is capped at a fifth and the third-party
claim against the other driver is not capped at all. Same crash, two rulebooks.

### The MCARE question, answered plainly

Pennsylvania's medical malpractice statute, the MCARE Act of 2002, is often assumed to cap
attorney fees the way California's malpractice statute does. It was read for this page. It
does not. Section 509 discusses periodic payment of future medical damages after the
proportionate share of counsel fees and costs is paid, and sets a $100,000 line below which
a claimant may object to periodic payments. Nowhere does the act state a percentage limit.

### What the paperwork must contain

Rule 1.5(b) requires that the basis or rate of the fee be communicated in writing to a
client the lawyer has not regularly represented. Rule 1.5(c) requires a contingent fee
agreement to be in writing stating how the fee is determined, the percentages for
settlement, trial and appeal, the litigation and other expenses deducted from the recovery,
and whether those expenses come off before or after the calculation. It also requires
something people forget to ask for: at the conclusion of the matter, a written statement of
the outcome that shows the remittance and how it was determined. Request that statement
rather than a lump-sum check with a handwritten note.

### Court costs in Dauphin County are statutory, and small

A claim inside the $12,000 civil limit belongs before a magisterial district judge, where
the 2026 cost table set under 42 Pa.C.S. 1725.1 runs $68.50 for actions of $500 or less,
$91 above $500 through $2,000, $114 above $2,000 through $4,000, and $171 from $4,001 to
$12,000. An order of execution costs $51.50 and an objection to levy $23. Postage and
registered mail sit outside those figures and fall on the plaintiff. A larger claim moves
to the Court of Common Pleas at the courthouse on Market Street, where the prothonotary's
own fee schedule governs and should be checked at the counter before filing.

### The coverage number that decides who pays first

Every Pennsylvania auto liability policy must carry medical benefit coverage of at least
$5,000 under 75 Pa.C.S. 1711. That is the money treating an Allison Hill fender-bender in
the first weeks, long before any liability question is settled, and it is why a bill can
land in collections while a claim is open. Ask how the first-party benefit is being
coordinated, and get the answer in writing.

### What actually deserves scrutiny

Whether the percentage steps up, and at which docket event. Whether expenses are itemized
and whether an estimate precedes an expert retention. Whether the closing written statement
is promised. Whether a compensation claim is running beside the liability claim, because
the twenty percent limit applies to one of them and not the other, and a single blended
figure across both is a warning rather than a convenience.""")

COPY["louisvillecaraccidentlawyerpros.com"] = ("""Kentucky writes an exact fee schedule for work injuries and nothing at all for car wrecks, and this page separates the two: what SCR 3.130(1.5) demands of a written agreement, what the Jefferson Circuit Court clerk collects, and the two dollar figures in the no-fault statute that shape a Louisville claim before any fee question arises.""",
"""### One state, two very different rules

Start with the rule the Supreme Court of Kentucky adopted. SCR 3.130(1.5)(a) says a lawyer
shall not make an agreement for, charge, or collect an unreasonable fee or an unreasonable
amount for expenses, and gives eight reasonableness factors: time and labor with the
novelty and difficulty of the questions; whether the work precludes other employment; the
fee customarily charged in the locality; the amount involved and the results obtained; the
time limits at play; the nature and length of the relationship; experience, reputation and
ability; and whether the fee is fixed or contingent. No percentage appears. For a crash on
the Watterson Expressway or a rear-end collision in the Highlands, reasonableness is the
entire ceiling.

Now the contrast. KRS 342.320 governs a workers' compensation claim with arithmetic rather
than judgment: twenty percent of the first $25,000 of the award, fifteen percent of the next
$25,000, ten percent of the remainder, and a maximum fee of $18,000 for contracts signed on
or after July 14, 2018. No fee is paid until an administrative law judge approves it, the
approval motion is due within thirty days after the claim becomes final, and the fee comes
out of the employee's award or settlement proceeds. Kentucky knew how to write a cap. It
chose not to write one for motor vehicle claims.

### What the written agreement has to carry

Under SCR 3.130(1.5)(c) a contingent fee agreement must be in a writing signed by the
client, and must state the method of determination, the percentages that accrue on
settlement, at trial and on appeal, the litigation and other expenses deducted from the
recovery, and whether those expenses are deducted before or after the fee is figured. Two
requirements in the Kentucky version deserve special attention. The agreement must clearly
notify the client of any expenses the client will owe whether or not the client prevails.
And at the conclusion of the matter, the lawyer must provide a written statement of the
outcome showing the remittance and the method by which it was determined.

Paragraph (d) closes two doors: no fee tied to the result for a criminal defendant, and no
fee in a domestic relations matter contingent on securing a divorce or on the amount of
alimony, maintenance, support or property settlement, apart from liquidated sums already in
arrears.

### The two figures in the no-fault statute

Kentucky is a choice no-fault state, and two numbers drive the early stage of a Louisville
claim. Basic reparation benefits are capped at $10,000 for all economic loss to one injured
person from one accident under KRS 304.39-020, regardless of how many carriers might owe
them. And KRS 304.39-060 allows recovery for pain, suffering, mental anguish and
inconvenience only where medical expense benefits exceed $1,000, or where the injury
involves permanent disfigurement, a bone fracture, loss of a body member, permanent injury
within reasonable medical probability, permanent loss of bodily function, or death.

Those figures explain a pattern people misread as delay. Treatment gets paid from the
reparation benefit, the $10,000 runs out faster than anyone expects on an emergency room
visit plus imaging plus therapy, and the liability claim then has to carry both the
remaining bills and the human loss.

### Court costs, and what else leaves the recovery

Filing suit in Jefferson Circuit Court costs $188 under CR 3.02(1) as amended for 2026,
plus a $20 court technology fee and other required charges, including the court facility
fee and library fee, collected by the circuit clerk. Those are costs of the case, not a
fee. Depositions, medical records, records custodians, a mediator, an accident
reconstruction opinion in a disputed intersection case, and trial exhibits are all case
expenses too, and the written agreement decides who advances them and when.

### Questions worth asking out loud

What percentage applies if the claim resolves before suit, and what changes it after suit
is filed. Whether expenses come off the top or after the fee is figured. Whether the
expense obligation survives a defense verdict, since the rule requires that warning
anyway. Whether a compensation claim is running in parallel, because the $18,000 statutory
ceiling governs that half and nothing governs the other half. And whether the closing
written statement will arrive with the settlement check, because the rule already entitles
the client to it.""")

COPY["modestocaraccidentlawyerpros.com"] = ("""California wrote percentage ceilings into its fee law once, for claims against health care providers, and never extended them to traffic collisions, so a Modesto injury fee is bounded by an unconscionability standard, a contract statute with teeth, and a Stanislaus County filing bill that is fixed to the dollar.""",
"""### The cap exists, but not for a crash claim

Business and Professions Code 6146 is the statute people are thinking of when they say
California limits injury fees. It sets twenty-five percent of the amount recovered when a
settlement and release is executed by all parties before a civil complaint or arbitration
demand is filed, and thirty-three percent when recovery comes by settlement, arbitration or
judgment after filing. A higher share requires a motion, served on all parties, granted on
evidence of good cause. "Recovered" means the net sum after disbursements and costs, and
the statute specifically refuses to let the plaintiff's own medical care costs or office
overhead be deducted first.

Every word of that reaches professional negligence claims against health care providers.
None of it reaches a collision on Briggsmore Avenue. For that claim the governing limit is
Rule 1.5(a) of the California Rules of Professional Conduct: a lawyer shall not make an
agreement for, charge, or collect an unconscionable or illegal fee. Paragraph (c) of the
same rule bars a result-based fee for a criminal defendant and in specified family law
matters, which is why a package number covering a citation and an injury claim together is
not a lawful structure.

### The contract statute is where California actually bites

Business and Professions Code 6147 governs every injury contingency contract. The contract
must be in writing, signed by both lawyer and client, with a duplicate copy handed to the
client at the moment it is entered into. It must state the agreed rate. It must state how
disbursements and costs will affect both the fee and the client's recovery. It must state
the extent to which the client could owe compensation for related matters outside the
contract. And unless the claim falls under section 6146, it must state that the fee is not
set by law but is negotiable between attorney and client.

That last sentence is a right, not boilerplate. If any required provision is missing, the
statute makes the agreement voidable at the plaintiff's option, and the lawyer is then
limited to a reasonable fee. Workers' compensation contracts sit outside section 6147
entirely.

### What the Stanislaus County courthouse costs

Court costs are public charges and belong on their own line. Under the statewide civil fee
schedule effective January 1, 2026, the first paper in an unlimited civil case, meaning one
worth more than $35,000, costs $435, and every other party filing a first paper owes the
same amount. Keeping a jury requires a nonrefundable advance jury fee of $150 under Code of
Civil Procedure 631(b), with daily jury deposits set by the court once trial starts. If a
case is designated complex, Government Code 70616 adds $1,000 for all plaintiffs together
and $1,000 for each defendant, up to $18,000 for the case.

The Stanislaus court publishes its own additions alongside the state schedule, including a
$1,000 supplemental fee when a high-frequency litigant files a construction-related
accessibility complaint and $30 to register an out-of-state conservatorship. Neither
touches a collision case, but both show that the local schedule is worth reading rather
than assuming.

### Why a Central Valley claim gets expensive to prove

Cost, not percentage, is where an injury budget actually moves. A Highway 99 or Highway 132
collision often involves a commercial vehicle, which brings electronic control module data,
driver qualification files and a records custodian deposition. Farm-truck traffic and
agricultural equipment on county roads produce liability disputes that get resolved by
reconstruction opinions rather than police narrative. Medical records arrive from several
systems and each certification costs money. Interpreter needs for a household where English
is not the first language add scheduling and expense. Each of those items is a cost, is
advanced by somebody, and is repaid from the recovery under whatever the written agreement
says.

### Reading the agreement in the order that matters

Find the rate, then find the sentence saying the rate is negotiable, then find the sentence
explaining how costs hit the recovery. Confirm the duplicate signed copy is in hand that
day. Ask what happens to advanced costs if the case is lost. Ask whether the share changes
at filing, at arbitration, or on appeal, and confirm the trigger is written rather than
assumed. Ask who deals with hospital reimbursement claims and health plan liens, because
that negotiation decides the final number more often than a percentage does.

### The trap

The trap in California is not an inflated percentage. It is a fee computed on the gross
while costs are also charged to the client, with no line explaining the sequence. Section
6147 requires that explanation. Ask for the arithmetic on a hypothetical number before
signing, and get it in writing.""")

COPY["oxnardcaraccidentlawyerpros.com"] = ("""Nothing in California law caps the share taken from a Ventura County collision recovery, and this page shows what does apply: an unconscionability standard, a contract statute that voids agreements missing a required term, and the filing amounts the Ventura County Superior Court publishes for itself.""",
"""### Where the percentage limits stop

California's numeric fee ceilings live in Business and Professions Code 6146, and they
belong to one kind of case: professional negligence against a health care provider. There
the share is a quarter of the amount recovered when all parties execute a settlement and
release before a complaint or arbitration demand is filed, and a third when recovery
follows filing, computed on the net sum after disbursements. An arbitrator or judge may
allow more only on a motion showing good cause.

A rear-end impact on Rice Avenue or a broadside at Oxnard Boulevard is not that kind of
case. The applicable limit is Rule 1.5(a) of the California Rules of Professional Conduct,
which forbids making an agreement for, charging, or collecting an unconscionable or illegal
fee. There is no schedule behind it and no percentage published anywhere in the rule. That
absence is the honest answer to the question "what is the legal limit in California," and
it puts the weight on the contract instead.

### The contract statute, and the word "voidable"

Section 6147 requires an injury contingency contract to be written, signed by both the
attorney and the client, with a duplicate signed copy provided to the client when the
contract is entered into. The contract must set out the agreed rate; how disbursements and
costs affect both the fee and the client's recovery; what compensation, if any, the client
might owe for related matters outside the contract; and, because a collision claim is not a
6146 claim, a statement that the fee is not set by law but is negotiable.

Failure on any provision renders the agreement voidable at the plaintiff's option, and the
attorney is then entitled to collect only a reasonable fee. That is unusually sharp
consumer protection, and it only works for people who read the document. Anyone signing in
a hospital bed should keep the duplicate copy and read it the following week.

### What the Ventura County court charges

The court publishes its own figures, and they are worth knowing before deciding whether a
claim belongs in a full civil filing or in small claims. An initial complaint, petition or
application costs $435 when the amount demanded exceeds $35,000, $370 when it is above
$10,000 through $35,000, and $225 at $10,000 or less. An answer or response costs the same
amounts, charged per defendant, so a crash with several drivers and a vehicle owner
generates several of them.

After a first appearance fee has been paid, each motion costs $60 in the civil division,
which is what makes a discovery dispute a budget item rather than a footnote. Appealing an
unlimited civil decision runs $775 to the Court of Appeal plus a $100 deposit to the Ventura
clerk for the transcript. On the small claims side, the court's own instructions set filing
at $30 for a claim of $1,500 or less, $50 above $1,500 through $5,000, and $75 above $5,000
through $12,500 for a natural person, rising to $100 for anyone who has filed more than
twelve claims in the previous twelve months, with $15 per defendant for certified mail
service. A small claims appeal costs $75.

### Costs behave differently from fees

A fee compensates work. A cost pays a third party, and it comes out of the recovery no
matter how the percentage is written. In a Ventura County collision claim the recurring
ones are certified medical records from several providers, the traffic collision report,
deposition reporter charges, a private mediator's daily rate, treating physician testimony,
and photogrammetry or reconstruction work when a farm-road intersection or a Highway 101
merge is in dispute. Agricultural and port traffic around Oxnard means commercial vehicles
appear often, and a commercial defendant brings corporate records, safety files and more
depositions.

### The questions that reveal a weak agreement

Does the percentage change, and does the document name the event that changes it. Are costs
deducted before or after the fee is calculated, and is a worked example available. Who owes
advanced costs if nothing is recovered. Is there a cost approval threshold above which the
client is consulted before an expert is retained. Who negotiates hospital and health plan
reimbursement claims, and is that work inside the stated rate or billed separately.

### One firm rule to carry away

The percentage is negotiable and the statute says so in writing. The court costs above are
not negotiable and go to the county and the state regardless of who is hired. Keeping those
two categories apart on paper is the single best defense against a settlement statement
nobody can explain.""")


def apply(domain):
    sdir = SITES / domain
    sj = sdir / "site.json"
    data = json.loads(sj.read_text(), object_pairs_hook=collections.OrderedDict)
    out = collections.OrderedDict()
    for k, v in data.items():
        if k == "hero_accent":
            out["pricing"] = PRICING[domain]
        out[k] = v
    if "pricing" not in out:
        out["pricing"] = PRICING[domain]
    sj.write_text(json.dumps(out, indent=1) + "")
    cm = sdir / "copy.md"
    text = cm.read_text().rstrip("\n")
    lede, body = COPY[domain]
    text += "\n\n## pricing_lede\n\n" + lede.strip() + "\n\n## pricing_body\n\n" + body.strip() + "\n"
    cm.write_text(text)
    print("patched", domain)


for d in PRICING:
    apply(d)
