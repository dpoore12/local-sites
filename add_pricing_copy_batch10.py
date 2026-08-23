#!/usr/bin/env python3
"""Batch 10: append pricing_lede and pricing_body to five dog bite copy.md files."""
import pathlib, re

SITES = pathlib.Path(__file__).parent / "sites"

COPY = {}

COPY["atlantadogbitelawyerpros.com"] = ("""\
A dog bite claim in Georgia is handled on a contingency, meaning the attorney is paid out of the money that comes in rather than by the hour, and this page sets out what the State Bar rule actually requires of that arrangement, what the Fulton County Clerk charges to put a case on file, and which city amounts apply to the animal itself.
""", """\
### Georgia sets a standard, not a ceiling

Anyone comparing arrangements in Atlanta should know the first thing about Georgia law here: there is no statewide percentage limit on a fee taken from an injury recovery. Rule 1.5(a) of the Georgia Rules of Professional Conduct forbids an unreasonable fee and leaves the number itself to negotiation between the client and the lawyer. That is a genuine difference from New York, where the Appellate Division publishes a graduated schedule for the same kind of claim. The consequence for a bite victim in Buckhead or Grant Park is simple. The percentage in front of a person is a proposal, and it is open to discussion.

### The eight things a fee is measured against

Rule 1.5(a) lists what makes a fee reasonable. The hours and labor the matter demands, and the novelty and difficulty of the questions it raises. Whether taking the case shuts the lawyer out of other work. What the locality customarily charges for comparable representation. The amount at stake and the result reached. Time limits imposed by the client or the circumstances. The nature and length of any prior relationship. The experience, reputation and ability of the person doing the work. And whether the fee is fixed or contingent, which matters because a contingency carries the risk of no payment at all. Note the maximum sanction the State Bar attaches to a Rule 1.5 violation is a public reprimand.

### What the writing has to contain

Rule 1.5(c)(1) is the provision worth reading before signing anything. A contingent fee agreement must be in writing. It must state the method by which the fee is determined. It must give the percentage that accrues in the event of settlement, in the event of trial, and in the event of appeal, which are frequently three different figures. It must identify the litigation and other expenses to be deducted from the recovery. And it must say whether those expenses are subtracted before or after the percentage is calculated. That last clause changes the money in a client's hand more than most people expect, so it deserves a slow read rather than a nod.

### The statement owed at the end

Rule 1.5(c)(2) closes the loop. When the matter concludes and there is a recovery, the lawyer owes the client a written statement setting out the outcome, the remittance to the client, the method by which that remittance was determined, the amount of the attorney fee, and, where another lawyer shared in the fee, the amount that went to that lawyer and the basis for it. A person who never receives that document is entitled to ask for it.

### Where a contingency is not permitted at all

Rule 1.5(d) draws two hard lines. No fee may be contingent on securing a divorce, or on the amount of alimony, support or a property settlement in place of it. And no lawyer may take a contingent fee for defending someone against a criminal charge. Neither restriction touches a dog bite claim, but knowing they exist explains why the rule treats injury work as the place where a share of the recovery is allowed.

### What the courthouse on Pryor Street charges

Litigation has its own price list, published by the Fulton County Clerk of Superior Court and set by statute rather than by anyone's business decision. A general civil action costs $215.00 to file under O.C.G.A. 15-21A-6, with $8.00 added for each party past the first under 15-6-77.2. Service of the complaint by the Sheriff runs $50.00, subpoena service $10.00, and a motion filed in an existing case $1.00. Certified copies are $2.50 plus fifty cents a page. These are costs, not fees, and a contingency agreement should say plainly who advances them and what happens to them if the claim does not produce a recovery.

### City amounts attached to the dog

Section 18-61 of the Atlanta Code of Ordinances requires an annual owner's permit for every dog six months or older, at $3.00 per dog and no more than $10.00 for one family. When Animal Services impounds a dog, the owner has seven days from the mailed notice to reclaim it and owes a $7.50 impoundment fee plus $3.00 for each day of boarding, along with any unpaid permit fee and the cost of rabies vaccination where the dog wore no current tag. Those figures rarely decide a claim, but records of an unpaid permit or a prior impoundment often matter to what a bite claim can prove about the owner's knowledge.
""")

COPY["lasvegasdogbitelawyerpros.com"] = ("""\
Nevada leaves the size of a contingent fee in an animal attack claim to negotiation while regulating the paperwork around it closely, and the sections below walk through Rule 1.5 of the Nevada Rules of Professional Conduct, the single statute that does cap a percentage, and the filing amounts the Eighth Judicial District Court publishes for Clark County.
""", """\
### The percentage itself is open

There is no Nevada rule that fixes a maximum percentage on a bite or animal attack recovery. Rule 1.5(a) of the Nevada Rules of Professional Conduct says only that a lawyer shall not make an agreement for, charge, or collect an unreasonable fee or an unreasonable amount for expenses. Reasonableness is then judged against eight considerations: time and labor, novelty and difficulty, and the skill needed; whether accepting the matter blocks other employment; what lawyers in the locality customarily charge for similar work; the amount involved and the result obtained; deadlines imposed by the client or the situation; how long and how closely the two have worked together; the standing and ability of counsel; and whether payment is fixed or hangs on the outcome.

### The formalities Nevada adds

Rule 1.5(b) requires the scope of the work and the basis of the fee and expenses to be communicated, preferably in writing, before or within a reasonable time after the representation starts. Rule 1.5(c) goes considerably further than most states. The contingent fee agreement must be written, must be signed by the client, and its key terms must appear in boldface type at least as large as the largest type used anywhere in the document. Those terms are the method of calculating the fee including the percentages on settlement, trial and appeal; whether expenses are taken out of the recovery and whether that happens before or after the fee is figured; and whether the client owes those expenses whatever the outcome.

### Two warnings the document must carry

Nevada is unusual in requiring the agreement to state the downside in the same emphasized type. Rule 1.5(c)(4) requires it to say that if the case is lost the client may be liable for the opposing party's attorney fees and will be liable for the opposing party's costs to the extent the law requires. Rule 1.5(c)(5) requires it to say that a suit brought solely to harass or to coerce a settlement may result in liability for malicious prosecution or abuse of process. At the end of the matter the lawyer owes a written statement of the outcome and, if money came in, the remittance and how it was calculated.

### The one Nevada cap, and why it is not this claim

NRS 7.095 is the statute people sometimes hear about secondhand. It bars a contingent fee greater than 35 percent of the amount recovered when the client is seeking damages for injury or death against a provider of health care based on professional negligence, and it applies whether the money arrives by settlement, arbitration award or judgment. Subsection 3 defines the recovered amount as the net figure after disbursements and the costs of prosecuting or settling the claim come out. A claim against the owner or keeper of a dog is not a professional negligence action against a health care provider, so that ceiling has nothing to say about it. Rule 1.5(d) separately bars any contingency in a divorce-related matter or for a criminal defendant.

### What the Regional Justice Center charges

Filing amounts come from the Clerk of the Eighth Judicial District Court and are built from a stack of statutes rather than set locally by choice. A general civil complaint is $270.00, assembled from components in NRS 19.013, 19.020, 19.030, 19.0302, 19.0303, 19.031, 19.0312, 19.0313 and 19.0315. Each additional plaintiff adds $30.00 under NRS 19.0335, and each defendant filing an answer pays $223.00 with the same $30.00 addition per extra party. A third party complaint costs $135.00 and a summary judgment motion $200.00. A construction defect or otherwise complex complaint jumps to $520.00. In a contingency arrangement these amounts are usually advanced and then recouped from the recovery, so the written agreement should say so directly.

### Costs beyond the filing window

NRS 18.005 defines what counts as costs a prevailing party can be awarded, and the list is long: clerks' and reporters' fees, jurors' fees, witness fees, interpreters, service of process, photocopies, postage, travel and lodging for depositions, and reasonable and necessary expenses including computerized legal research. The figure worth remembering is in subsection 5, which allows reasonable fees for no more than five expert witnesses at no more than $15,000 for each of them unless the court finds the circumstances warranted paying more. In a serious attack case, a treating specialist or a reconstructive surgeon giving opinion testimony is exactly the kind of expense that provision governs.

### Where the county ordinance puts dollar figures

Clark County Code Title 10 attaches money mainly to permits rather than to bites. Section 10.08.135 charges $800 for a breeder or show permit, including the initial site inspection by Animal Protection Services, and $800 again on annual renewal, falling to $400 where each animal has taken part in a show once during the year. A failed inspection or a violation of Chapter 10 adds a $100 reinspection fee. Separately, NRS 202.500 makes it a misdemeanor to keep a dog known to be vicious more than seven days, and a category D felony where such a dog causes substantial bodily harm, while forbidding any local ordinance that turns on breed alone.
""")

COPY["losangelesdogbitelawyerpros.com"] = ("""\
California asks whether a fee is unconscionable rather than whether it exceeds some set percentage, and the sections here lay out the thirteen factors that answer the question, the disclosures the Business and Professions Code forces into a contingency contract, and the amounts the Superior Court of Los Angeles County prints on its own civil fee schedule.
""", """\
### The California standard is unconscionability

Rule 1.5(a) of the California Rules of Professional Conduct draws the outer boundary of any fee arrangement: it may be neither unconscionable nor illegal. Georgia and Nevada use the milder yardstick of reasonableness. California picked the harsher word and then supplied a long list of considerations that decide whether a given arrangement crosses it. Neither the rule nor any statute attaches a percentage to a claim brought against a dog's owner, so a figure printed on a retainer arrived there by negotiation and not by legislation.

### Thirteen factors, and the ones that bite

Rule 1.5(b) fixes the moment of judgment at the time the bargain was struck, unless the two of them expected later events to move the fee, and then names thirteen considerations. Some look at conduct: overreaching in arriving at the number, or keeping back facts the client needed. Some look at proportion: the size of the fee set beside what the representation was actually worth, and the sum at stake measured against the outcome delivered. Some look at the two people signing: how sophisticated each of them was, how long and how closely they had dealt with one another, and what standing, track record and ability counsel brought to it. The rest look at the shape of the work itself, meaning how novel and hard the questions were, whether taking it shut out other paying clients, what deadlines pressed on it, how many hours it swallowed, whether payment was a set sum or rode entirely on the result, and whether the client knowingly agreed to the terms after being told what they meant.

### What section 6147 puts on the page

Business and Professions Code section 6147 governs the contingency contract itself. The agreed rate has to appear in the document, and for any claim outside section 6146 the contract must carry express notice that no law fixes that rate and the client is free to bargain over it. That notice is the reason a first number is never binding on anybody. Subdivision (b) gives the requirement teeth: omit a required element and the plaintiff may void the whole agreement, dropping counsel to nothing more than a reasonable fee. Rule 1.5(c) separately bars a contingency in a family law matter tied to a dissolution or to support, and bars one for a criminal defendant.

### The exception that does not reach a bite claim

Section 6146 is California's only percentage ceiling in injury work, and it applies exclusively to claims against a health care provider based on professional negligence. There the maximum is 25 percent of the amount recovered where all parties execute a settlement and release before a complaint or arbitration demand is filed, and 33 percent where the recovery comes after filing. An attorney may move for more than 33 percent in a tried or arbitrated case on evidence of good cause. Amounts recovered are net of disbursements and costs, and the statute expressly refuses to let medical care costs or office overhead be deducted first. A claim against a dog's owner is a straightforward negligence and strict liability matter, so none of that schedule applies to it.

### Stanley Mosk and the money the clerk collects

The Superior Court of Los Angeles County publishes its civil fee schedule with the Government Code section beside each line. A complaint or other first paper in an unlimited civil case, meaning one seeking more than $35,000, is $435 under section 70611, and each responding party pays the same. Keeping a jury requires a nonrefundable advance jury fee of $150 under Code of Civil Procedure section 631(b), with later daily deposits of $15 plus mileage of thirty-four cents a mile one way for each juror. A court reporter's per diem runs $764 for a session of four hours or more, $382 for more than one hour but under four, and $30 for an hour or less under Government Code section 68086.

### When a case is designated complex

Government Code section 70616 adds a complex case designation fee of $1,000 paid once for all plaintiffs and $1,000 for each defendant, with the total for the case stopping at $18,000. Most single-dog bite claims never see that designation, but a matter involving a landlord, a property manager, a homeowners association and several insurers occasionally does. Because these amounts are costs advanced rather than fees earned, the contingency contract should state who fronts them, whether they come out of the recovery before or after the percentage is applied, and what happens to them if the claim fails.

### The city's license amounts, and why records matter

Los Angeles Municipal Code section 53.15.3 sets a dog license processing fee of $91.50, dropping to $16.50 for a spayed female, a neutered male, or a dog a veterinarian certifies cannot breed. Section 53.15 adds an annual license tax of $8.50 per dog over four months, or $3.50 for an altered dog, with a reduced rate available at half the altered tax for a qualifying owner aged sixty-two or older or receiving disability benefits. Payment later than forty-five days after the renewal date carries a late fee of 25 percent of the license cost, and field collection at the property where the dog is kept adds $25.00. Failing to license within forty-five days is a misdemeanor, and license and rabies records are ordinary evidence in a bite claim.
""")

COPY["sacramentodogbitelawyerpros.com"] = ("""\
Fee arrangements in a Sacramento animal attack case answer to the State Bar rule on unconscionable fees, to two sections of the Business and Professions Code that dictate what the paperwork must say, and, where the injured person is a child, to a Rule of Court that hands the decision to a judge, with the county's own filing tiers layered on top.
""", """\
### No cap, but a hard limit on unconscionable fees

California Rule of Professional Conduct 1.5(a) prohibits an agreement for, a charge of, or the collection of an unconscionable or illegal fee. Nothing in the rule names a number. What the rule does instead is list thirteen non-exclusive factors, and factor (b)(3) is the one that carries the most weight in a routine claim: the amount of the fee in proportion to the value of the services performed. Factor (b)(4) looks at the relative sophistication of the two parties to the agreement, factor (b)(2) at whether material facts about the fee were disclosed, and factor (b)(13) at whether the client gave informed consent. Read together they mean a percentage is defensible when the work behind it is real and the client understood the deal.

### Section 6147 and the sentence about negotiation

Business and Professions Code section 6147 requires a contingency agreement to be reduced to writing, with a fully executed duplicate handed to the client at the time it is signed. Subdivision (a)(1) requires the agreed rate to be stated. Subdivision (a)(2) requires a statement of how disbursements and costs incurred in connection with the claim will affect both the fee and the client's recovery. Subdivision (a)(4) requires the contract to state, in terms, that the fee is not set by law but is negotiable. Where a defect exists, subdivision (b) makes the whole agreement voidable at the plaintiff's choice, leaving counsel entitled only to a reasonable fee. That remedy sits with the client, not with the lawyer.

### A child's recovery is decided by the judge

Most people bitten badly enough to bring a claim in this county are children, and that changes the fee analysis entirely. California Rule of Court 7.955(a)(1) provides that in matters under Code of Civil Procedure section 372 or Probate Code sections 3600 to 3601, unless the court approved the fee agreement in advance, the court must use a reasonable fee standard when approving fees payable from money paid for the benefit of a minor or a person with a disability. Subdivision (b) supplies fourteen factors, including the fact that a minor is involved, the fee against the value of the services, the amount involved and the result obtained, informed consent, and, where the fee is contingent, the risk of loss the attorney bore, the costs advanced, and the delay before payment. A declaration from counsel accompanies the petition.

### The thousand dollar writing threshold

Section 6148 covers work that is not on a contingency, which matters when a matter starts as advice or a demand letter billed hourly. Where it is reasonably foreseeable that total expense to the client, fees included, will pass $1,000, the contract must be in writing and a signed duplicate given to the client. It must set out the basis of compensation, meaning hourly rates, statutory fees, flat fees and other standard rates and charges; the general nature of the services; and the respective responsibilities of attorney and client. Every bill must state its basis, one must be produced within ten days of a request, and a client may repeat that request at intervals of not less than thirty days. Non-compliance again leaves the agreement voidable at the client's option.

### Filing tiers on H Street

The fee schedule posted by the Superior Court of California, County of Sacramento prices a first paper by the amount in controversy. A complaint seeking up to $10,000 costs $225 under Government Code section 70613(b). One seeking more than $10,000 and up to $35,000 costs $370 under section 70613(a). An unlimited civil complaint above $35,000 costs $435 under section 70611, and each party other than the plaintiff pays $435 to appear. Reclassifying a limited case as unlimited later on costs another $140 under section 70619, which is a real consideration when a wound turns out to need reconstructive surgery after the case was filed small.

### Motions, continuances and the rest of the docket

The same schedule prices what happens after filing. A motion or other paper requiring a hearing is $60 under Government Code section 70617(a). A motion for summary judgment or summary adjudication is $500 under section 70617(d), which is the largest single motion charge on the list and one reason those motions are not filed lightly. A continuance of a hearing or case management conference is $20, a stipulation and order $20, a change of venue processing charge $50, and a complex designation $1,000 with the statutory $18,000 ceiling per case. All of these are costs advanced in a contingency matter, and the agreement should say who carries them and when they are recouped.

### County license amounts and what they prove

Sacramento County Code chapter 8.24 requires every dog four months or older to be licensed and currently vaccinated against rabies. Animal Care charges $50 a year for an intact animal, $100 for two years and $150 for three, against $15, $30 and $40 for an altered animal, with a reduced $10 annual rate for an owner sixty-two or older keeping an altered pet. A late payment adds $25.00, a duplicate tag costs $5, and a qualifying competition animal or working ranch dog can be licensed unaltered for $45 a year. Galt and Isleton run their own lower amounts. Licensing and vaccination records are pulled routinely after an attack because they show what the owner had done, and had not done, before it happened.
""")

COPY["newyorkdogbitelawyerpros.com"] = ("""\
New York is the rare state where an appellate court publishes an actual fee schedule for personal injury work, and because a dog bite claim is a personal injury claim rather than malpractice, the schedule in 22 NYCRR 603.25 is the ceiling that governs a Manhattan case, with a different sliding scale in the Judiciary Law that applies only to medical claims.
""", """\
### The rule that controls a Manhattan bite claim

New York County lies within the First Judicial Department, and its Appellate Division has adopted 22 NYCRR 603.25(e). The provision reaches any claim or action for personal injury or wrongful death, resolved by judgment or by settlement, in which the attorney's compensation depends on the outcome, and it excludes claims alleging medical, dental or podiatric malpractice. A fee equal to or below the scheduled amount is deemed fair and reasonable. A fee above it, the rule says, constitutes the exaction of unreasonable and unconscionable compensation in violation of the Rules of Professional Conduct, unless a court has authorized it by written order.

### Schedule A, the graduated ladder

The first of the two options in the rule steps down as the recovery grows. Fifty percent of the first $1,000 recovered. Forty percent of the next $2,000. Thirty-five percent of the next $22,000. Twenty-five percent of any amount above $25,000. Because serious bite injuries settle well past that last breakpoint, the marginal rate on the bulk of a substantial recovery under this option is the twenty-five percent tier, and the blended rate across the whole recovery drops the larger the number gets. Someone comparing arrangements should do that arithmetic on the figure realistically in play rather than on the headline percentage at the top of the ladder.

### Schedule B, the flat alternative

The second option is a percentage not exceeding thirty-three and one third percent of the sum recovered, and it is available only if the initial contractual arrangement provides for it. There is a tradeoff written into the rule. Choosing the flat option removes access to the procedure by which counsel may later apply for additional compensation on grounds of extraordinary circumstances. Under Schedule A that route stays open: where counsel believes in good faith the scheduled fee is inadequate because of extraordinary circumstances, an application may be made on affidavit to the designated justice, with written notice and an opportunity to be heard given to the client and to anyone holding a lien.

### Net or gross, and the choice the client makes

Subdivision (e)(3) is the part of the rule most likely to change what actually lands in a client's account. The percentage may be computed one of two ways, and the client selects which in the retainer agreement or letter of engagement. Either on the net sum recovered after deducting expenses and disbursements for expert testimony and investigative or other services properly chargeable to the claim, or, where the attorney has agreed to pay those costs under Judiciary Law 488(2)(d), on the gross sum before any such deduction. The agreement must describe both methods, explain the financial consequences of each, and clearly show which one the client picked. Costs as taxed, including interest on a judgment, count as part of the amount recovered. No deduction is made in the computation for a lien or claim in favor of a hospital, for medical care and treatment by doctors and nurses, or of a self-insurer or an insurance carrier.

### The malpractice scale that does not apply here

Judiciary Law 474-a is frequently quoted as though it governed all injury work in New York. It does not. Its sliding scale reaches medical, dental and podiatric malpractice actions only, capping the fee at thirty percent of the first $250,000 recovered, twenty-five percent of the next $250,000, twenty percent of the next $500,000, fifteen percent of the next $250,000, and ten percent of anything above $1,250,000. A claim against the owner of a dog that bit someone on a sidewalk in Chelsea is an ordinary personal injury claim, so the First Department schedule applies and this one does not. If a hospital's handling of the wound became its own claim, that separate claim would fall under 474-a.

### A child's claim goes before the court

Judiciary Law 474 makes an agreement between an attorney and the guardian of an infant for compensation dependent on the success of the infant's claim, or for a percentage of the infant's recovery, invalid and unenforceable unless it was made subject to the court's power to fix the amount. On a recovery, award, compromise or settlement, the attorney applies on notice to the guardian, the court proceeds summarily to determine the value of the services by affidavit, reference or examination of witnesses, and then orders a suitable amount out of the money. Given how many bite victims in the city are children, this is the operative fee mechanism in a large share of cases.

### What the paperwork and the County Clerk cost

Rule 1215.1 of the Rules of the Chief Administrator requires a written letter of engagement before the representation begins, or within a reasonable time after where that is impracticable, explaining the scope of the services, the fees, expenses and billing practices, and, where it applies, the client's right to fee arbitration under Part 137. A signed retainer covering those subjects satisfies the requirement, and a significant change in scope calls for an updated letter. On the litigation side, CPLR 8018(a) fixes the index number fee at $190 payable in advance, plus $5 for records management and $15 for the cultural education account, so $210 opens the file. Filing a note of issue costs $125 where no request for judicial intervention was needed. City licensing runs $8.50 a year for a spayed or neutered dog and $34 for an unaltered dog older than four months, with a $2 fine for each year a license went unrenewed.
""")


def main():
    for domain, (lede, body) in COPY.items():
        p = SITES / domain / "copy.md"
        text = p.read_text()
        text = re.split(r"\n## pricing_lede", text)[0].rstrip("\n")
        text += "\n\n## pricing_lede\n\n" + lede.strip() + "\n\n## pricing_body\n\n" + body.strip() + "\n"
        p.write_text(text)
        print("appended pricing copy:", domain, len(body.split()), "body words")


if __name__ == "__main__":
    main()
