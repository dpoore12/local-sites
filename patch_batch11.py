#!/usr/bin/env python3
"""Batch 11: add /pricing/ blocks + copy sections to 5 legal (contingency) sites."""
import json, pathlib, collections

ROOT = pathlib.Path("/home/user/workspace/local-sites/sites")

CALBAR = "https://www.calbar.ca.gov/legal-professionals/rules/rules-professional-conduct/current-rules-professional-conduct/chapter-1-lawyer-client-relationship"
BP6147 = "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=6147.&lawCode=BPC"
BP6146 = "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=6146.&lawCode=BPC"
CRC7955 = "https://www.courts.ca.gov/cms/rules/index.cfm?title=seven&linkid=rule7_955"
CRC7952 = "https://www.courts.ca.gov/cms/rules/index.cfm?title=seven&linkid=rule7_952"
CCP37760 = "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=377.60.&lawCode=CCP"
SDFEE = "https://www.sdcourt.ca.gov/pls/portal/docs/page/sdcourt/generalinformation/forms/adminforms/adm001.pdf"
SDLIC = "https://sdhumane.org/services/dog-licensing/"
FRESNOFEE = "https://www.fresno.courts.ca.gov/system/files/general/statewide-civil-fee-schedule-eff-01012024.pdf"

TX104 = "https://www.legalethicstexas.com/resources/rules/texas-disciplinary-rules-of-professional-conduct/fees/"
TX71004 = "https://law.justia.com/codes/texas/civil-practice-and-remedies-code/title-4/chapter-71/subchapter-a/section-71-004/"
TX71010 = "https://law.justia.com/codes/texas/civil-practice-and-remedies-code/title-4/chapter-71/subchapter-a/section-71-010/"
TX71009 = "https://law.justia.com/codes/texas/civil-practice-and-remedies-code/title-4/chapter-71/subchapter-a/section-71-009/"
TX71021 = "https://law.justia.com/codes/texas/civil-practice-and-remedies-code/title-4/chapter-71/subchapter-b/section-71-021/"
TXPR142 = "https://statutes.capitol.texas.gov/Docs/PR/htm/PR.142.htm"
TRAVISFEE = "https://www.traviscountytx.gov/images/district_clerk/Docs/Travis-County-District-Clerk-Filing-Fees-2026.pdf"
TRAVISPROB = "https://countyclerk.traviscountytx.gov/departments/probate/probate-fee-information/"
DALFILE = "https://www.dallascounty.org/Assets/uploads/docs/district-clerk/fee-schedules/2024-CIVIL-FILING-FEES-WPD.pdf"
DALSERV = "https://www.dallascounty.org/Assets/uploads/docs/district-clerk/fee-schedules/2024-CIVIL-SERVICE-FEES-WPD.pdf"
DALSHER = "https://www.dallascounty.org/Assets/uploads/docs/district-clerk/fee-schedules/SHERIFF-CONSTABLE-FEES-FY-2025-with-revisions.pdf"
DALPROB = "https://www.dallascounty.org/Assets/uploads/docs/county-clerk/fee-schedules/Probate-Fee-Schedule-01012026.pdf"

FL415 = "https://www-media.floridabar.org/uploads/2026/06/2026_12-JUNE-Chapter-4-RRTFB-1.pdf"
FL76820 = "https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&Search_String=&URL=0700-0799/0768/Sections/0768.20.html"
FL76818 = "https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&Search_String=&URL=0700-0799/0768/Sections/0768.18.html"
FL76825 = "https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&Search_String=&URL=0700-0799/0768/Sections/0768.25.html"
FL76826 = "https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&Search_String=&URL=0700-0799/0768/Sections/0768.26.html"
FL744387 = "https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&Search_String=&URL=0700-0799/0744/Sections/0744.387.html"
DUVALFEE = "https://www.duvalclerk.com/about/fee-schedules"

SITES = {}

# ---------------------------------------------------------------- San Diego --
SITES["sandiegodogbitelawyerpros.com"] = {
 "pricing": {
  "mode": "fees",
  "fee_kind": "contingency",
  "table_head": "What California pins down in a San Diego dog bite claim, and what it deliberately leaves to negotiation",
  "col_a": "What it covers",
  "col_b": "What California sets",
  "anchors": [
   {"label": "First paper in an unlimited civil case, San Diego Superior Court",
    "value": "$435",
    "detail": "Charged under Government Code 70611 when a complaint over $35,000 is filed, and again on the answer filed by each other party.",
    "source_name": "San Diego Superior Court Fee Schedule 1, effective July 1, 2026",
    "source_url": SDFEE},
   {"label": "Listed factors behind the word unconscionable",
    "value": "13",
    "detail": "Rule 1.5(b) enumerates thirteen considerations, opening with fraud or overreaching in setting the fee and failure to disclose material facts.",
    "source_name": "Cal. Rules of Professional Conduct 1.5(b)",
    "source_url": CALBAR},
   {"label": "Appeal from a dangerous or vicious dog determination",
    "value": "$45",
    "detail": "The Superior Court charges this to hear an owner's appeal under Food and Agricultural Code 31622, separate from any injury case.",
    "source_name": "San Diego Superior Court Fee Schedule 1, item 179",
    "source_url": SDFEE},
   {"label": "City of San Diego dog license, altered dog, one year",
    "value": "$20",
    "detail": "Sold by San Diego Humane Society for the city, with a $25 penalty when a renewal runs past the expiration date.",
    "source_name": "San Diego Humane Society dog licensing fees",
    "source_url": SDLIC}],
  "fee_rows": [
   {"stage": "The share taken from a bite recovery",
    "share": "Not capped",
    "note": "No California statute limits the percentage in a dog bite matter. Rule 1.5(a) bars an unconscionable or illegal fee and stops there.",
    "source_name": "Cal. Rules of Professional Conduct 1.5(a)",
    "source_url": CALBAR},
   {"stage": "The only percentages California does fix",
    "share": "Medical negligence only",
    "note": "Section 6146(a) limits fees to 25 percent, or 33 percent once a complaint is filed, in professional negligence claims against health care providers.",
    "source_name": "Cal. Bus. & Prof. Code 6146(a)",
    "source_url": BP6146},
   {"stage": "The contract handed over at signing",
    "share": "Signed duplicate",
    "note": "Section 6147(a) requires a written contract signed by attorney and client, with a duplicate copy given to the client that same day.",
    "source_name": "Cal. Bus. & Prof. Code 6147(a)",
    "source_url": BP6147},
   {"stage": "The sentence about negotiating the rate",
    "share": "Mandatory clause",
    "note": "Under 6147(a)(4) a claim outside section 6146 needs a contract stating the fee is not set by law and can be negotiated.",
    "source_name": "Cal. Bus. & Prof. Code 6147(a)(4)",
    "source_url": BP6147},
   {"stage": "A bitten child's settlement",
    "share": "Judge sets the fee",
    "note": "Rule 7.955(a)(1) makes the court apply a reasonable fee standard to money paid for a minor unless it blessed the agreement beforehand.",
    "source_name": "Cal. Rules of Court 7.955(a)(1)",
    "source_url": CRC7955},
   {"stage": "Running the case through the courthouse",
    "share": "$435 to open",
    "note": "The same schedule adds $150 for the advance jury fee, $573 for a reporter past one hour, and $500 for summary judgment.",
    "source_name": "San Diego Superior Court Fee Schedule 1",
    "source_url": SDFEE}]},
 "lede": ("A dog bite claim here is normally taken on for a share of whatever the claim eventually pays, and California "
          "fixes no number for that share, so this page sets out what the State Bar rule and section 6147 force into the "
          "written agreement, what the Superior Court charges to move a case through, and the small city amounts that attach "
          "to the animal."),
 "body": """### California regulates the fee without capping it

Rule 1.5(a) of the California Rules of Professional Conduct runs to one sentence: no lawyer may enter into an agreement for, charge, or collect a fee that is unconscionable or illegal. That is the whole of the limit for a bite claim in this state. There is no graduated schedule and no ceiling by stage of the case. So the figure written into a contingency fee agreement in San Diego is a proposal being made to a client, not a rate the state handed down, and a person reading one is entitled to push back on it.

### Thirteen things that decide whether a fee is unconscionable

Rule 1.5(b) judges the fee on the facts as they stood when the agreement was signed, except where both sides expected later events to change it. The listed considerations run from whether the lawyer engaged in fraud or overreaching while setting the fee, and whether material facts went undisclosed, through the proportion between the fee and the value of the work performed, the relative sophistication of lawyer and client, the novelty and difficulty of the questions, the chance that taking the matter shuts out other employment, the sum at stake and what was achieved, and the ability of the people actually doing the work.

### What section 6147 forces onto the page

Business and Professions Code section 6147(a) requires the contingency contract to be in writing, signed by both the attorney and the client or the client's guardian, with a duplicate copy handed to the client when it is signed. Four things have to appear in it. The agreed contingency rate, at 6147(a)(1). How disbursements and costs will hit both the fee and the client's own recovery, at (a)(2). Whether the client could owe compensation for related matters the contract does not cover, at (a)(3). And, at (a)(4), a plain statement that the fee is not set by law and is negotiable between attorney and client. Subdivision (b) supplies the teeth: a contract that misses any of this is voidable at the client's option, and the attorney is then limited to a reasonable fee.

### The percentages that belong to a different case

California does cap contingency percentages in exactly one area, and a dog bite is not it. Section 6146(a) covers claims against a health care provider based on professional negligence, and there the limits are 25 percent of the amount recovered when the case settles before a complaint or arbitration demand is filed, and 33 percent afterward, with 6146(a)(3) letting the plaintiff's attorney move for more on evidence of good cause. Those figures get quoted loosely around injury work generally. They have no application to a claim against a dog owner, a landlord, or a homeowners insurer, and a contract citing them for this kind of claim is citing the wrong statute.

### When the person bitten is a child

Children take a large share of serious bites, and a child's money runs on a separate track. Rule 7.955(a)(1) requires the court to apply a reasonable fee standard when allowing attorney fees payable out of money paid for the benefit of a minor, unless it approved the fee agreement in advance. Subdivision (b) gives fourteen nonexclusive factors, including three specific to contingent arrangements at (b)(13): the risk of loss the attorney carried, the costs advanced, and the delay in being paid. Subdivision (c) requires a declaration from the attorney addressing whichever factors apply, and (d) voids local rules that try to set their own standard. Under rule 7.952(a), the person petitioning and the child both have to appear at the hearing unless the court excuses them for good cause. Where the court orders a guardianship investigation, Probate Code 1513.1 puts that at $800 on the San Diego schedule.

### What the courthouse actually charges

Litigation costs are published, not negotiated. San Diego's Fee Schedule 1, effective July 1, 2026, puts a first paper in an unlimited civil case at $435 under Government Code 70611, with the same $435 due from each other party filing an answer. A motion requiring a hearing is $60, summary judgment is $500 under 70617(d), and the nonrefundable advance jury fee is $150 under Code of Civil Procedure 631(b). Court reporting is $30 for a proceeding under an hour and $573 beyond that. A complex designation adds $1,000 for the plaintiffs and $1,000 per defendant, capped at $18,000. These are case costs, and the agreement should state who advances them and what becomes of them if nothing is recovered.

### The paperwork attached to the dog

San Diego Humane Society sells licenses for the City of San Diego at $20 for one year, $35 for two and $50 for three when the dog is altered, and $60, $100 and $150 when it is not, a spread Food and Agricultural Code 30804.5 requires. A late renewal adds $25, and a change of ownership or a transfer from another jurisdiction $15 each. None of that decides a claim, but a lapsed license, a prior impoundment, or a dangerous dog determination the owner paid $45 to appeal all become records that speak to what the owner knew.""",
}

# ------------------------------------------------------------------- Austin --
SITES["austinwrongfuldeathlawyerpros.com"] = {
 "pricing": {
  "mode": "fees",
  "fee_kind": "contingency",
  "table_head": "What Texas Rule 1.04 and chapter 71 govern in a Travis County death case, and what no Texas rule limits",
  "col_a": "What it covers",
  "col_b": "What Texas sets",
  "anchors": [
   {"label": "Total base fee to file a civil suit, Travis County District Clerk",
    "value": "$350",
    "detail": "Built from a $213 local consolidated fee and a $137 state consolidated fee, due when the petition is filed.",
    "source_name": "Travis County District Clerk filing fees, effective January 1, 2026",
    "source_url": TRAVISFEE},
   {"label": "Reasonableness factors listed in the Texas fee rule",
    "value": "8",
    "detail": "Rule 1.04(b) lists eight, among them the fee customarily charged in the locality for similar legal services.",
    "source_name": "Tex. Disciplinary R. Prof. Conduct 1.04(b)",
    "source_url": TX104},
   {"label": "Application for administration or determination of heirship, Travis County Clerk",
    "value": "$360",
    "detail": "The probate filing fee for opening an estate, with a $525 ad litem deposit required in the circumstances the Clerk lists.",
    "source_name": "Travis County Clerk probate fee information",
    "source_url": TRAVISPROB},
   {"label": "District Clerk registry fee on funds held for a beneficiary",
    "value": "5 percent, up to $50",
    "detail": "Charged under Local Government Code 117.055 on money deposited into the court registry that is not earning interest.",
    "source_name": "Travis County District Clerk filing fees, court registry section",
    "source_url": TRAVISFEE}],
  "fee_rows": [
   {"stage": "The percentage taken from a death recovery",
    "share": "No ceiling in Texas",
    "note": "Rule 1.04(a) forbids an illegal or unconscionable fee, measured by whether a competent lawyer could believe it reasonable. No percentage is named.",
    "source_name": "Tex. Disciplinary R. Prof. Conduct 1.04(a)",
    "source_url": TX104},
   {"stage": "What the contingent fee agreement must break out",
    "share": "Three percentages",
    "note": "Rule 1.04(d) requires a signed writing giving the percentage on settlement, on trial and on appeal, plus the expenses deducted.",
    "source_name": "Tex. Disciplinary R. Prof. Conduct 1.04(d)",
    "source_url": TX104},
   {"stage": "Whether costs come off before or after the fee",
    "share": "Stated in writing",
    "note": "Rule 1.04(d) makes the contract say whether expenses are subtracted before or after the contingent percentage is calculated.",
    "source_name": "Tex. Disciplinary R. Prof. Conduct 1.04(d)",
    "source_url": TX104},
   {"stage": "Who is entitled to file the claim",
    "share": "Spouse, children, parents",
    "note": "Section 71.004(a) gives the action to those three classes exclusively, and (c) hands it to the executor after three calendar months.",
    "source_name": "Tex. Civ. Prac. & Rem. Code 71.004",
    "source_url": TX71004},
   {"stage": "How one recovery splits among the family",
    "share": "Shares found by the jury",
    "note": "Section 71.010(b) has the damages divided among the surviving persons in the shares the jury finds, which fixes each fee base.",
    "source_name": "Tex. Civ. Prac. & Rem. Code 71.010(b)",
    "source_url": TX71010},
   {"stage": "Fee for setting up a minor's chapter 142 trust",
    "share": "Capped at $1,000",
    "note": "Property Code 142.005(l) allows the petitioning party reimbursement of reasonable attorney fees not exceeding one thousand dollars.",
    "source_name": "Tex. Prop. Code 142.005(l)",
    "source_url": TXPR142}]},
 "lede": ("Texas puts no percentage limit on a fee taken out of a death recovery, and it is Rule 1.04 rather than a rule "
          "numbered 1.5 that governs the arrangement, so this page walks through what that rule demands of the writing, who "
          "chapter 71 lets bring the claim, how a jury's split of the damages sets each share, and what the Travis County "
          "clerks charge along the way."),
 "body": """### The rule number is 1.04, and it names no percentage

Fee conduct in Texas sits in Rule 1.04 of the Texas Disciplinary Rules of Professional Conduct, not in a rule numbered 1.5 as it is in most states. Subdivision (a) prohibits an illegal fee and an unconscionable one, and it defines unconscionable in a single sentence: a fee is unconscionable if a competent lawyer could not form a reasonable belief that it is reasonable. Nothing in the rule, and nothing in the Civil Practice and Remedies Code, states a maximum percentage for a death claim. Families comparing two agreements in Austin are comparing two offers, and the standard against which either one is judged is a professional judgment test rather than an arithmetic limit.

### The eight measures of a reasonable fee

Rule 1.04(b) sets out what goes into that judgment. The labor and hours a case demands, how novel and difficult its questions are, and the skill needed to handle them properly. Whether accepting the matter keeps the lawyer from other employment. The fee customarily charged in the locality for similar legal services, which is why an Austin comparison is not a Houston comparison. The amount involved and the results obtained. Time limitations imposed by the client or by events. The nature and length of the professional relationship. And whether the fee is fixed or contingent.

### What has to be on paper

Under Rule 1.04(c) the basis or rate of the fee has to be communicated to the client, preferably in writing, before or within a reasonable time after the representation begins. For a contingent arrangement, 1.04(d) goes further. The agreement must be in writing, signed by the client, and it must state the method by which the fee is to be determined, including the percentage that accrues to the lawyer in the event of settlement, trial or appeal. Those three numbers are frequently different from one another. It must state the litigation and other expenses to be deducted from the recovery and, critically, whether those expenses come off before or after the contingent percentage is figured. At the end of the matter the lawyer owes the client a written statement of the outcome and, where money was recovered, the remittance and how it was reached.

### Who owns the claim, and what happens if nobody files

Section 71.004(a) of the Civil Practice and Remedies Code makes the wrongful death action the exclusive property of the surviving spouse, children and parents of the deceased. Under (b) any one of them, or all of them together, may bring it for the benefit of everyone entitled. Subsection (c) is the deadline most families never hear about: if none of those individuals has begun an action within three calendar months of the death, the executor or administrator of the estate is required to bring it, unless all of the beneficiaries ask that it not be filed. Section 71.021 keeps the deceased person's own injury claim alive separately, passing it to the heirs, legal representatives and estate.

### The jury splits the money before the fee is applied

Section 71.010 lets the jury award damages in a proportion it finds and then divides the recovery among those entitled in the shares the jury sets. A single settlement or verdict resolves into separate shares belonging to separate people, each with a different age, dependency and loss, and a contingent percentage lands on each of those shares rather than on one undivided pot. Where one of those people is a minor, that share cannot simply be handed over.

### A minor's share and the chapter 142 route

Property Code chapter 142 governs money recovered for a child with no legal guardian, who appears through a next friend or a guardian ad litem. Section 142.001 lets the court, on application and after a hearing, decree how the funds are invested. Section 142.004 limits the vehicles to a qualified tuition or ABLE account and federally insured interest-bearing time deposits, widening only slightly where the clerk of court invests on written order. Section 142.005 allows a court-created trust instead, and (b) fixes its terms, including that a minor's trust ends at death, at a stated age, or at the twenty-fifth birthday, whichever comes first. Subdivision (l) caps what the petitioning party may be reimbursed in attorney fees for setting the trust up at $1,000, and (m) and (n) restrict who may serve as trustee depending on whether the principal exceeds $50,000.

### What the Travis County clerks charge

The District Clerk's schedule effective January 1, 2026 puts the total base fee for a civil suit at $350, being a $213 local consolidated fee and a $137 state consolidated fee. Issuing a citation, subpoena or writ is $8. Service by certified mail through the District Clerk is $85, while a Travis County constable serving citations and notices charges $90 plus a separate $10 witness payment fee. A jury demand under Rule 216 costs $10. Later filings in the same case, including an intervention, a counterclaim, a third party petition or a motion for new trial, are $80 each. Money held in the court registry carries an administrative charge of 5 percent capped at $50 where it earns no interest, or 10 percent of the interest where it does. On the probate side the County Clerk charges $360 to apply for letters of administration, for a determination of heirship, or for a management trust, with a $525 ad litem deposit in the situations the Clerk identifies, $2 to issue letters, and $25 to file an annual account.""",
}

# ------------------------------------------------------------------- Dallas --
SITES["dallaswrongfuldeathlawyerpros.com"] = {
 "pricing": {
  "mode": "fees",
  "fee_kind": "contingency",
  "table_head": "What the Texas fee rule requires of a Dallas County death case, and what the two clerks charge to run one",
  "col_a": "What it covers",
  "col_b": "What Texas sets",
  "anchors": [
   {"label": "Filing suit with no service, Dallas County District Clerk",
    "value": "$350",
    "detail": "The schedule adopted under Senate Bill 1612 charges this once for the case and adds no fee for additional plaintiffs.",
    "source_name": "Dallas County District Clerk civil filing fees",
    "source_url": DALFILE},
   {"label": "Attorney ad litem deposit on a heirship application",
    "value": "$600",
    "detail": "Required alongside the $360 probate filing fee when heirship is determined, plus the newspaper publication bill.",
    "source_name": "Dallas County Clerk probate fee schedule, effective January 1, 2026",
    "source_url": DALPROB},
   {"label": "Sheriff or constable service of a citation",
    "value": "$80",
    "detail": "Set by commissioners court order for service of a citation, summons, notice, subpoena or order not otherwise listed.",
    "source_name": "Dallas County Sheriff and Constable fees, FY 2025",
    "source_url": DALSHER},
   {"label": "Consent needed before a second firm shares the fee",
    "value": "Written",
    "detail": "Rule 1.04(f) requires the client to consent in writing to the identity of every lawyer, the basis of the split and each share.",
    "source_name": "Tex. Disciplinary R. Prof. Conduct 1.04(f)",
    "source_url": TX104}],
  "fee_rows": [
   {"stage": "A share of what the case recovers",
    "share": "Unlimited by rule",
    "note": "Texas names no maximum. The only test in Rule 1.04(a) is whether a competent lawyer could reasonably believe the fee is reasonable.",
    "source_name": "Tex. Disciplinary R. Prof. Conduct 1.04(a)",
    "source_url": TX104},
   {"stage": "Telling the client the basis of the fee",
    "share": "Before, or soon after",
    "note": "Rule 1.04(c) requires the rate or basis to be communicated, preferably in writing, before or within a reasonable time of starting work.",
    "source_name": "Tex. Disciplinary R. Prof. Conduct 1.04(c)",
    "source_url": TX104},
   {"stage": "The signed contingent fee contract",
    "share": "Writing required",
    "note": "Rule 1.04(d) requires the client's signature and separate percentages for settlement, trial and appeal, with the deducted expenses named.",
    "source_name": "Tex. Disciplinary R. Prof. Conduct 1.04(d)",
    "source_url": TX104},
   {"stage": "Splitting the fee with a referring firm",
    "share": "Client consent in writing",
    "note": "Rule 1.04(f) permits a division only in proportion to services or on joint responsibility, disclosed in writing and not increasing the total.",
    "source_name": "Tex. Disciplinary R. Prof. Conduct 1.04(f)",
    "source_url": TX104},
   {"stage": "The estate's own surviving claim",
    "share": "Separate cause",
    "note": "Section 71.021 keeps the deceased person's injury claim alive and passes it to the heirs, legal representatives and the estate.",
    "source_name": "Tex. Civ. Prac. & Rem. Code 71.021",
    "source_url": TX71021},
   {"stage": "Opening the estate at the County Clerk",
    "share": "$360 plus deposits",
    "note": "Probate applications run $360, with a $600 ad litem deposit on heirship and $88 for constable service inside Dallas County.",
    "source_name": "Dallas County Clerk probate fee schedule",
    "source_url": DALPROB}]},
 "lede": ("Nothing in Texas law caps the percentage a lawyer may take out of a death recovery, so what protects a family in "
          "Dallas is the disclosure Rule 1.04 forces into the contract and the published cost of running the case, and this "
          "page sets out both, along with the separate survival claim and the probate filings a death case usually drags "
          "behind it."),
 "body": """### Two clerks, two schedules, one case

A Dallas wrongful death matter almost always touches two courthouses. The district court where the negligence claim is filed, and the probate court where the estate is opened so that someone has authority to act for it. The District Clerk charges $350 to file suit with no service under the schedule adopted after Senate Bill 1612, and adds nothing for extra plaintiffs, which matters when a spouse, three children and a parent all appear on the same petition. Issuing a citation or any other writ is $8, as is issuing a subpoena or abstracting a judgment. Non-original filings in a case already on the docket, among them a cross action, an intervention, a third party petition or a motion for new trial, are $80 apiece.

### The fee itself is governed by Rule 1.04, not Rule 1.5

Texas numbers its fee rule 1.04, which trips up anyone reading a form contract drafted for another state. Subdivision (a) is short and absolute: a lawyer shall not enter into an arrangement for, charge or collect an illegal fee or an unconscionable one. Unconscionable carries a defined meaning here, namely a fee that no competent lawyer could form a reasonable belief was reasonable. No number appears there or anywhere else in the rule. A family being shown a percentage in Oak Cliff or Richardson is looking at a proposed term, and the eight considerations in 1.04(b) are the vocabulary for questioning it. Among them: the amount involved and the results obtained, the fee customarily charged in the locality for similar legal services, and the time limitations the circumstances impose.

### Disclosure obligations that run before the signature and after the check

Rule 1.04(c) requires the basis or rate of the fee to be communicated to the client, preferably in writing, either before the representation starts or within a reasonable time afterward. Rule 1.04(d) then sets out what a contingent contract must contain: the client's signature, the method of determining the fee, the percentage accruing on settlement, on trial and on appeal stated separately, the expenses to be deducted from the recovery, and whether those expenses are subtracted before or after the percentage is applied. Two contracts with the same headline percentage produce different checks depending on that one clause. When the case ends, the same subdivision requires a written statement of the outcome, and where money was recovered, the remittance to the client and how it was calculated.

### When a second firm is in the case

Death cases are referred between firms constantly, and Rule 1.04(f) controls what happens to the fee when they are. A division between lawyers not in the same firm is permitted only if it is made in proportion to the professional services each performs, or if each lawyer assumes joint responsibility for the representation. Either way the client has to consent in writing to the identity of every lawyer or firm involved, to whether fees will be divided by proportional service or joint responsibility, and to the share each lawyer or firm will receive. A family that learns after the fact that a referring firm took a cut was entitled to that disclosure in advance.

### The claim the family brings and the claim the estate brings

Section 71.004(a) of the Civil Practice and Remedies Code gives the wrongful death action to the surviving spouse, children and parents, for their exclusive benefit, and section 71.010 divides any recovery among them in the shares the jury finds. Section 71.021 is the second track: the deceased person's own personal injury claim survives the death and passes to the heirs, legal representatives and estate, which is why a single event often produces two claims with two sets of damages. Section 71.009 permits exemplary damages where the death resulted from a willful act or omission or from gross negligence. Because the survival claim belongs to the estate, someone has to be appointed to pursue it.

### The probate filings a death case pulls along

The Dallas County Clerk's probate schedule, effective January 1, 2026, charges $360 for an application to probate a will, for letters testamentary, for muniment of title, and for any of the administration applications. A combined administration and determination of heirship is also $360 but adds a $600 attorney ad litem deposit and a publication bill from the Daily Commercial Record. An application to determine heirship alone carries the same $600 deposit. Letters of guardianship cost $360, plus $25 for a court investigator where guardianship of the person is sought, a $100 bond deposit, and $88 for constable service on the proposed ward inside Dallas County. A civil suit ancillary to an estate is $360.

### Service, collection and the costs nobody quotes

Service is a separate line item and it is not trivial. The commissioners court order in force for fiscal year 2025 sets $80 to serve a citation, summons, notice, subpoena or order not otherwise listed, $65 for service by publication or certified mail, $20 to post a notice, and $20 for a district court bailiff fee. A writ of execution is $400, and deputies serving one bill $50 per hour per deputy after the first two hours. All of these are case costs rather than attorney fees, which is precisely why the contract has to say who advances them and who carries them if the case recovers nothing.""",
}

# ------------------------------------------------------------------- Fresno --
SITES["fresnowrongfuldeathlawyerpros.com"] = {
 "pricing": {
  "mode": "fees",
  "fee_kind": "contingency",
  "table_head": "What California law settles about fees in a Fresno County death case, and what it leaves to the contract",
  "col_a": "What it covers",
  "col_b": "What California sets",
  "anchors": [
   {"label": "Petition to compromise a minor's claim with no action pending",
    "value": "$435",
    "detail": "Charged under Government Code 70655(c)(1) for a Probate Code 3600 petition, on the schedule the Fresno court publishes.",
    "source_name": "Statewide Civil Fee Schedule published by Fresno Superior Court, item 138",
    "source_url": FRESNOFEE},
   {"label": "Court reporter for a civil proceeding lasting over an hour",
    "value": "$440 half day, $880 day",
    "detail": "Set under Government Code 68086(a)(1)(B), on top of $30 for any proceeding that runs an hour or less.",
    "source_name": "Statewide Civil Fee Schedule published by Fresno Superior Court, items 66-67",
    "source_url": FRESNOFEE},
   {"label": "Classes of people who may assert the death claim",
    "value": "3",
    "detail": "Section 377.60 groups them into heirs at (a), dependents at (b), and a dependent minor of the household at (c).",
    "source_name": "Cal. Code Civ. Proc. 377.60",
    "source_url": CCP37760},
   {"label": "Factors a judge may weigh on a fee paid from a minor's recovery",
    "value": "14",
    "detail": "Rule 7.955(b) lists fourteen, three of them specific to the risk, advanced costs and payment delay of a contingency.",
    "source_name": "Cal. Rules of Court 7.955(b)",
    "source_url": CRC7955}],
  "fee_rows": [
   {"stage": "The percentage in a death case",
    "share": "Left to the parties",
    "note": "No California statute limits it. Rule 1.5(a) prohibits an unconscionable or illegal fee and leaves the figure to be negotiated.",
    "source_name": "Cal. Rules of Professional Conduct 1.5(a)",
    "source_url": CALBAR},
   {"stage": "The clause saying the rate is negotiable",
    "share": "Required by statute",
    "note": "Section 6147(a)(4) makes the written contract state that the fee is not fixed by law wherever section 6146 does not apply.",
    "source_name": "Cal. Bus. & Prof. Code 6147(a)(4)",
    "source_url": BP6147},
   {"stage": "The statutory percentages people confuse with this",
    "share": "Medical negligence only",
    "note": "The 25 and 33 percent limits in section 6146(a) apply solely to professional negligence claims against health care providers.",
    "source_name": "Cal. Bus. & Prof. Code 6146(a)",
    "source_url": BP6146},
   {"stage": "Standing to bring the claim",
    "share": "Heirs and dependents",
    "note": "Section 377.60 lists a spouse, domestic partner, children and issue, intestate takers, dependent relatives, and a qualifying minor of the household.",
    "source_name": "Cal. Code Civ. Proc. 377.60",
    "source_url": CCP37760},
   {"stage": "A fee paid out of a child's share",
    "share": "Court allowed",
    "note": "Rule 7.955(a)(1) applies a reasonable fee standard to money paid for a minor unless the court approved the agreement in advance.",
    "source_name": "Cal. Rules of Court 7.955(a)(1)",
    "source_url": CRC7955},
   {"stage": "Attendance at the compromise hearing",
    "share": "Both must appear",
    "note": "Rule 7.952(a) requires the petitioner and the minor to attend unless the court dispenses with the appearance for good cause.",
    "source_name": "Cal. Rules of Court 7.952(a)",
    "source_url": CRC7952}]},
 "lede": ("California sets no percentage on what a lawyer may take out of a wrongful death recovery, and it protects families "
          "instead through what the contract has to disclose and what a judge has to approve, so this page lays out both, who "
          "the Code of Civil Procedure lets sue, and what the Fresno County courthouse charges to carry a case to trial."),
 "body": """### Nothing in California law fixes the number

The starting point is short. Rule 1.5(a) of the California Rules of Professional Conduct forbids an agreement for, a charge of, or collection of an unconscionable or illegal fee, and no statute anywhere in California supplies a percentage ceiling for a wrongful death claim. In practice the percentage on a Fresno family's contract came from the lawyer who drafted it, and the law's answer is not to cap it but to force it into the open and, where a child or a dependent adult is involved, hand it to a judge.

### How unconscionability actually gets tested

Rule 1.5(b) measures the fee against all the facts and circumstances existing when the agreement was entered into, unless the parties contemplated that later events would affect it. The enumerated considerations include whether there was fraud or overreaching in negotiating or setting the fee, whether material facts went undisclosed, the amount of the fee in proportion to the value of the services performed, the relative sophistication of the lawyer and the client, whether the engagement precludes other work, and the amount involved and the results obtained. A grieving family is rarely a sophisticated buyer of legal services, and that asymmetry is itself on the list.

### What the contract has to say out loud

Business and Professions Code section 6147 governs the paperwork. Subdivision (a) requires a written contract signed by both the attorney and the client, or the client's guardian or representative, with a duplicate copy provided at the time it is entered into. It must state the agreed rate, explain how disbursements and costs incurred in prosecuting or settling the claim will affect both the fee and the client's recovery, and disclose any compensation the client might owe for related matters outside the contract. Then, at (a)(4), unless the claim falls under section 6146, the contract must state that no law sets this fee and that its amount is open to negotiation between the two of them. If any of that is missing, subdivision (b) makes the agreement voidable at the client's option and limits the attorney to a reasonable fee.

### The 25 and 33 percent figures belong somewhere else

Those two numbers circulate as though they were general injury law in California. They are not. Section 6146(a) applies only where a person seeks damages against a health care provider based on that provider's alleged professional negligence, and it caps the fee at 25 percent of the amount recovered where the case resolves by settlement and release signed before a civil complaint or arbitration demand is filed, and 33 percent where recovery follows the filing. A death caused by a truck driver, a defective machine, or an unsafe premises in Fresno County is outside that section entirely, and a contract applying those percentages to it has borrowed the wrong statute.

### Who California lets bring the claim

Section 377.60 of the Code of Civil Procedure decides standing, and it is broader than most families expect. Subdivision (a) covers the surviving spouse, domestic partner, children and the issue of deceased children, or, where no issue survives, the people who would take the decedent's property by intestate succession, and it lets legal guardians step in where the parents who could have sued are themselves deceased. Subdivision (b) adds, whether or not they qualify under (a), a dependent putative spouse and that spouse's children, stepchildren, parents, or legal guardians. Subdivision (c) reaches a minor who lived in the household for the 180 days before the death and depended on the decedent for at least half of their support. Any of them may sue, or the personal representative may sue on their behalf, and a contingent percentage attaches to each resulting share rather than to one lump.

### A child's money goes past the judge

Where part of a recovery belongs to a minor or a person with a disability, the fee stops being purely contractual. Rule 7.955(a)(1) requires the court to use a reasonable fee standard in approving attorney fees payable from that money, unless it approved the agreement in advance, and (a)(2) has the court evaluate the agreement on the facts as they stood when it was made. Subdivision (b) gives fourteen nonexclusive factors, including at (b)(9) the informed consent of the minor's representative to the fee and at (b)(13) the risk of loss borne by the attorney, the costs advanced, and the delay in payment. Subdivision (c) requires a declaration addressing the applicable factors. Under rule 7.952(a) the petitioner and the minor both attend the hearing unless excused for good cause, and the court may require the examining physician to testify.

### What the courthouse on O Street costs to use

The fee schedule the Fresno court publishes puts a first paper in an unlimited civil case at $435, and the same amount is due from each other party filing an answer. Summary judgment is $500 under Government Code 70617(d), and a complex designation adds $1,000 for all plaintiffs plus $1,000 per defendant up to $18,000 for the case. The advance jury fee is $150 and nonrefundable. Court reporting runs $30 for a proceeding of an hour or less, then $440 per half day or $880 per day. On the probate side, a petition to compromise a minor's claim where no civil action is pending costs $435 under 70655(c)(1), a petition for appointment of a guardian of the estate is $435, and guardianship of the person alone is $225. Every one of those is a case cost rather than a fee, and the contract should state who fronts them and what happens if the case ends with no recovery.""",
}

# ------------------------------------------------------------- Jacksonville --
SITES["jacksonvillewrongfuldeathlawyerpros.com"] = {
 "pricing": {
  "mode": "fees",
  "fee_kind": "contingency",
  "table_head": "The sliding fee schedule Florida actually publishes for a Duval County death claim, tier by tier",
  "col_a": "What it covers",
  "col_b": "What Florida sets",
  "anchors": [
   {"label": "Presumed limit on the first $1 million, settled before an answer",
    "value": "33 1/3 percent",
    "detail": "Rule 4-1.5(f)(4)(B)(i)a.1 makes a fee above this presumptively excessive when the case resolves before an answer is filed.",
    "source_name": "Fla. Bar Rule 4-1.5(f)(4)(B)(i)a",
    "source_url": FL415},
   {"label": "Circuit civil filing fee, Duval County Clerk",
    "value": "$401",
    "detail": "The standard fee to open a circuit civil case, with $10 for each summons issued and $2.50 per defendant past five.",
    "source_name": "Duval County Clerk of Courts fee schedules",
    "source_url": DUVALFEE},
   {"label": "Formal administration of an estate, Duval County Clerk",
    "value": "$401",
    "detail": "Needed because the personal representative, not the family, files the death claim; guardianship of the property is $400.",
    "source_name": "Duval County Clerk of Courts probate and guardianship fees",
    "source_url": DUVALFEE},
   {"label": "Net settlement to a child that forces a property guardianship",
    "value": "Over $15,000",
    "detail": "Section 744.387 lets a natural guardian settle up to that figure without bond and requires a guardian of the property above it.",
    "source_name": "Fla. Stat. 744.387(2) and (3)(b)",
    "source_url": FL744387}],
  "fee_rows": [
   {"stage": "Resolved before an answer or arbitration demand",
    "share": "33 1/3, 30, 20 percent",
    "note": "One third of the first million dollars, 30 percent of the next million, and 20 percent of anything above two million.",
    "source_name": "Fla. Bar Rule 4-1.5(f)(4)(B)(i)a",
    "source_url": FL415},
   {"stage": "After the answer, through entry of judgment",
    "share": "40, 30, 20 percent",
    "note": "The first tier rises to 40 percent of the first million once an answer or arbitration demand is filed; later tiers hold.",
    "source_name": "Fla. Bar Rule 4-1.5(f)(4)(B)(i)b",
    "source_url": FL415},
   {"stage": "All defendants admit liability, damages tried alone",
    "share": "33 1/3, 20, 15 percent",
    "note": "Where liability is conceded in the answers and only damages go to trial, the upper tiers drop to 20 and 15 percent.",
    "source_name": "Fla. Bar Rule 4-1.5(f)(4)(B)(i)c",
    "source_url": FL415},
   {"stage": "Appeal, postjudgment relief or collection",
    "share": "Additional 5 percent",
    "note": "Five percentage points may be added to any recovery obtained after an appellate proceeding or postjudgment action becomes necessary.",
    "source_name": "Fla. Bar Rule 4-1.5(f)(4)(B)(i)d",
    "source_url": FL415},
   {"stage": "Going above the schedule",
    "share": "Court approval",
    "note": "A client who cannot retain chosen counsel within these limits may petition the court to approve the contract under subdivision (f)(4)(B)(ii).",
    "source_name": "Fla. Bar Rule 4-1.5(f)(4)(B)(ii)",
    "source_url": FL415},
   {"stage": "How the fee comes out of a death recovery",
    "share": "Pro rata by award",
    "note": "Section 768.26 has the personal representative pay fees and expenses, deducted from each survivor's and the estate's award in proportion.",
    "source_name": "Fla. Stat. 768.26",
    "source_url": FL76826}]},
 "lede": ("Florida is one of the few states that publishes an actual sliding scale for a contingent fee in a death case, and "
          "the tiers move depending on how far the case has gone, so this page sets out each one exactly as Rule 4-1.5 states "
          "it, the route a client uses to go above it, and the probate steps and Duval County Clerk charges that a death claim "
          "brings with it."),
 "body": """### Florida publishes a schedule, and it is real

Most states cap nothing and simply ban an unreasonable fee. Florida is different. Rule 4-1.5(f)(4)(B) of the Rules Regulating The Florida Bar sets numeric limits for personal injury, property damage, and death resulting from personal injuries based on tortious conduct, products liability included. A contract exceeding those limits is presumed, unless rebutted, to be a clearly excessive fee. So a Jacksonville family reading a percentage can check it against a published figure rather than against a professional judgment standard.

### The tiers before an answer is filed

Where the matter resolves before the defendant files an answer, or before a demand for appointment of arbitrators, or before the time for either expires, subdivision (f)(4)(B)(i)a fixes the schedule in three layers. Thirty three and one third percent of any recovery up to $1 million. Plus 30 percent of any portion between $1 million and $2 million. Plus 20 percent of any portion above $2 million. The tiers stack rather than replace each other, so a $2.5 million settlement at this stage produces a fee built from all three layers.

### What changes once the defense answers

Subdivision (f)(4)(B)(i)b governs the period after the answer or the arbitration demand is filed, through entry of judgment. The first layer rises to 40 percent of any recovery up to $1 million, while the next two hold at 30 percent between $1 million and $2 million and 20 percent above $2 million. That single step from one third to 40 percent is the most consequential number here, because in a contested death case an answer is filed as a matter of course.

### The variant nobody mentions

Subdivision (f)(4)(B)(i)c covers the case where every defendant admits liability when filing their answers and asks for a trial only on damages. There the schedule reads 33 and one third percent up to $1 million, plus 20 percent between $1 million and $2 million, plus 15 percent above $2 million. Those upper tiers are the lowest in the rule, and a contract keeping the contested percentages in place after liability is conceded is worth a question.

### Appeals add five points, not a new contract

Subdivision (f)(4)(B)(i)d permits an additional 5 percent of any recovery after institution of any appellate proceeding, or of postjudgment relief or action required to collect on the judgment. It is an addition to whichever tier already applies, not a replacement schedule. Under (f)(4)(D) the lawyer with primary responsibility takes no less than 75 percent of the total fee and a secondary lawyer no more than 25 percent absent court authorization.

### The lawful way to exceed the schedule

The limits are not absolute. Under (f)(4)(B)(ii), a client who cannot obtain the lawyer of the client's choice because of those limits may petition the court where the matter would be filed, or the circuit court where the cause of action arose, to approve the fee contract. The court authorizes it on determining that the client fully understands the rights being given up and the terms. The petition may be filed as a separate proceeding before suit or together with the complaint, and that aspect of the file may be sealed. Authorization does not foreclose a later inquiry into whether the fee actually charged was clearly excessive.

### Three days to walk away, and a written closing statement

Before any of the tiers matter, (f)(4)(A) requires the client to have received, read and signed the Statement of Client's Rights, and it lets the client cancel by written notice within 3 business days of signing, owing no fee for work done in that window, although the lawyer may recover funds reasonably advanced. At the other end, (f)(5) requires a closing statement itemizing every cost and expense and stating each lawyer's fee, signed by all participating lawyers and by the client and retained for 6 years. Where a recovery is paid over time, (f)(6) calculates the percentage only on the cost of the structured settlement or its present money value, whichever is less.

### Who files, and who has to approve the deal

Section 768.20 of the Florida Statutes puts the action in the hands of the decedent's personal representative, who recovers for the benefit of the survivors and the estate. Survivors are defined in 768.18 to include the spouse, children, parents and certain dependent relatives, and that section defines minor children as children under 25 years of age. Section 768.25 then requires court approval of a settlement, as to amount or apportionment, whenever a survivor objects or a survivor who is a minor or an incompetent is affected. Section 768.26 controls how the money leaves the pot: fees and litigation expenses are paid by the personal representative and deducted from the awards to the survivors and the estate in proportion to the amounts awarded, except expenses incurred for one survivor, which come from that person's share. Under 744.387, a natural guardian may settle a claim up to $15,000 without bond, while a larger net settlement requires appointment of a guardian of the property.

### What the Duval County Clerk charges

Opening a circuit civil case in Jacksonville costs $401, with $10 for each summons issued and $2.50 for every defendant past the first five. A counterclaim, cross claim or third party claim is $395, and certification of a court record $2 per document. A deposit into the court registry runs 3 percent of the first $500 and 1.5 percent of each subsequent $100. On the probate side, formal administration is $401, guardianship of the property $400, and guardianship of the person alone $235. An inventory audit costs $85 once a ward's property exceeds $25,000. None of that is attorney fee, and the contract should say who advances it.""",
}


def main():
    for dom, spec in SITES.items():
        d = ROOT / dom
        sj = d / "site.json"
        data = json.loads(sj.read_text(), object_pairs_hook=collections.OrderedDict)
        data["pricing"] = spec["pricing"]
        sj.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
        cp = d / "copy.md"
        txt = cp.read_text().rstrip("\n")
        # remove any prior pricing sections
        if "## pricing_lede" in txt:
            txt = txt.split("## pricing_lede")[0].rstrip("\n")
        txt += ("\n\n## pricing_lede\n\n" + spec["lede"].strip()
                + "\n\n## pricing_body\n\n" + spec["body"].strip() + "\n")
        cp.write_text(txt)
        bw = len(spec["body"].split()) + len(spec["lede"].split())
        print(f"{dom}: authored {bw} words")


if __name__ == "__main__":
    main()
