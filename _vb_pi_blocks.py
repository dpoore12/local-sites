import re, pathlib

P = pathlib.Path("sites/virginiabeachpersonalinjurylawyerpros.com/copy.md")
text = P.read_text()

def set_block(txt, name, body):
    pat = re.compile(r"(## " + re.escape(name) + r"\n)(.*?)(?=\n## |\Z)", re.S)
    assert pat.search(txt), name
    return pat.sub(lambda m: m.group(1) + body.strip() + "\n\n", txt, count=1)

SYM = {
 "symptom_1_title": "You were injured at a hotel, restaurant, parking deck or other property",
 "symptom_1": """A wet lobby floor, an unlit stairwell, a loose handrail, a broken chair on a patio. Write down the street address, the exact spot inside or outside the building, the time, the lighting, and any warning sign that was or was not there. Ask for an incident report number before you leave. Spills get mopped and camera footage is overwritten on a schedule.""",
 "symptom_2_title": "Something went wrong during treatment and the new harm looks separate",
 "symptom_2": """Keep the sequence rather than the conclusion. Save admission and discharge paperwork, visit summaries, imaging reports, medication lists and every message sent through the patient portal, then start a dated log of symptoms and appointments. A bad outcome is not the same finding as a departure from the standard of care, and the difference gets decided by records and a qualified expert opinion.""",
 "symptom_3_title": "A product, part or piece of equipment failed and someone was hurt",
 "symptom_3": """Stop using the item and put it somewhere safe. Do not repair it, throw it out, hand it back to the seller or ship it to an adjuster before its condition has been photographed and written down. Keep every broken fragment, the packaging, the manual, the receipt and the serial or lot number. If a landlord, employer or rental shop holds it, ask in writing that it be preserved.""",
 "symptom_4_title": "The injury now affects work, mobility, family care or everyday tasks",
 "symptom_4": """Money is not the only thing a severe injury changes, but the file has to show the change. Keep therapy plans, work restrictions, leave paperwork, wage records and equipment receipts in date order, and add a plain calendar of appointments, missed shifts and tasks somebody else had to do for you. Specific entries carry weight later; broad statements about how hard life became do not.""",
}
for k, v in SYM.items():
    text = set_block(text, k, v)

NEW = {}

NEW["services_summary"] = """Four different jobs sit under one heading here, and their rules diverge quickly. A fall at an Oceanfront hotel turns on who controlled that walking surface and whether a court calls the hazard open and obvious. A treatment claim cannot even be served until a signed expert opinion exists, and one statute caps the entire recovery. A failed-product claim has to trace the defect back to the moment the item left a particular defendant's hands. A life-altering injury raises caps, short notice deadlines and, near the jet base, a federal filing route instead. Choosing the wrong frame burns the two-year clock, and nothing restarts it."""

NEW["services_pick_head"] = "Start with the injury you are actually dealing with"

NEW["crosslink_head"] = "A different injury question?"

NEW["svc_slip_and_fall_lawyer_lede"] = """Millions of visitors a year move through this city's hotel lobbies, decks, stairwells and parking areas. A fall claim here turns on two things: who controlled that surface, and whether a court treats the hazard as open and obvious."""

NEW["svc_slip_and_fall_lawyer_body"] = """### Two duties, and the excuse gets measured against both

The premises rule in the Commonwealth is short. An owner owes an invitee ordinary care to keep the place reasonably safe for the visit that was invited, and ordinary care to warn of an unsafe condition it knew about or should have known about. That is the formulation the Supreme Court of Virginia used in Fobbs v. Webb Building Limited Partnership, a rainy-morning fall in front of an elevator bank. Notice is where most of the fight sits. A property does not have to have seen the spill land: in Memco Stores v. Yeatman the court held constructive notice sufficient, alongside a duty to get foreign objects off the floor within a reasonable time. So the useful questions are how long the hazard sat there and who walked past it.

### The open and obvious exception is where these claims die

That duty comes with a carve-out which swallows a great many falls. There is no duty to warn of a condition open and obvious to a reasonable person exercising ordinary care for his own safety. Defense counsel will therefore build a record about what you could have seen: the lighting, the color contrast of a step edge, whether your arms were full, whether a cone already stood next to the mop bucket. Photograph the sightline from where you were walking, not only the hazard from above. An image shot straight down at a puddle proves the puddle and hands the other side its best argument.

### A share of the blame ends the case rather than shrinking it

Most states would cut a recovery by a percentage. This is one of the last places where an injured person's own failure to use reasonable care, once it helped cause the harm, defeats the claim outright. Notice how narrowly the General Assembly has moved off that position. Section 8.01-58 substitutes proportional reduction only for railroad employees suing a common carrier, and diminishes damages in proportion to that employee's negligence. One industry, one statute. Everybody else stands on the older rule, which is why a casual "I wasn't really looking" said to a duty manager can outweigh the photographs.

### Assumption of risk is a separate defense with a personal test

In Amusement Slides Corporation v. Lehmann the court called the doctrine venturousness and applied a subjective standard: what this particular plaintiff in fact saw, knew, understood and appreciated. Two things must be shown. The nature and extent of the risk has to have been fully appreciated, and the risk has to have been voluntarily incurred. That same opinion drew the line that matters in a resort setting. A man who rode a steep slide accepted its speed; he did not accept an attendant's failure to keep the waxed surface watered. Accepting an activity is not accepting somebody else's carelessness inside it.

### A fall on city ground starts a six-month clock

Trip on a public walkway, a municipal lot or a city-run facility and the ordinary two-year deadline is not what ends the claim. Under § 15.2-209 a negligence claim against a city is forever barred unless written notice of the nature of the claim, with the time and place of the injury, reaches the locality within six months. The City Attorney's Office publishes what belongs in that letter: claimant name and address, the date, the individuals involved if known, the location, and a description of what happened and why the City is said to be responsible. It goes to the City Attorney at 2401 Courthouse Drive and is forwarded to Risk Management, which investigates and decides whether anything is paid voluntarily. A claim against a state agency instead needs written notice within one year under § 8.01-195.6, and the claimant carries the burden of proving it arrived.

### The resort strip is a crowd of separate defendants

The Oceanfront district carries a three-mile boardwalk, the Atlantic and Pacific Avenue corridors behind it, and more than 40 beachfront hotels and resorts. The city counted 14.3 million visitors in 2024, and 58.8 percent of them came for the day, so parking decks, beach accesses, public restrooms and restaurant patios absorb enormous foot traffic in a short season. "At the beach" identifies nobody. One hotel lobby, the deck stairs of the next building, a leased restaurant space inside a third and the public walkway between them can involve four different parties responsible for upkeep. Away from the water the mix changes rather than thins: shopping-center pavement at Hilltop, apartment stairwells in Kempsville, waterfront decks off Great Neck and Bayside, and Sandbridge rental houses where owner, management company and cleaning contractor are three separate names.

### Where it gets filed, and how the fee is set

A claim up to $50,000 can be heard in the city's General District Court; above that the Circuit Court question opens, and this is an independent city with its own courthouse rather than a county seat. That court's stated goal is to conclude a civil case within 18 months of filing, and it wants a civil cover sheet with the first pleading plus a praecipe to get a trial date. The suit deadline itself is two years from accrual for the injury and five years for damaged property. On fees, the Commonwealth publishes no percentage. Rule 1.5 requires a reasonable fee, and a contingent agreement must state in writing how the fee is computed, the percentages attaching at settlement, trial and appeal, and which expenses come off the recovery."""

NEW["svc_medical_malpractice_lawyer_lede"] = """A malpractice claim in the Commonwealth cannot be served until a signed expert opinion already exists, and one statute caps everything recoverable rather than only the noneconomic part. Both rules bite long before anyone argues about the chart."""

NEW["svc_medical_malpractice_lawyer_body"] = """### A poor outcome and a standard-of-care failure are separate findings

Care is measured against a statewide standard: the degree of skill and diligence practiced by a reasonably prudent practitioner in that field or specialty in the Commonwealth. Section 8.01-581.20 allows a locality standard only where a party proves by a preponderance that local facilities and customary practice supply a more appropriate measure. The statute also screens the witness. An expert must demonstrate knowledge of the defendant's specialty and must have had active clinical practice in that specialty or a related field within one year of the act complained of. That requirement quietly ends some claims, because a long-retired or purely academic reviewer will not qualify.

### Nothing gets served until a signed opinion is in hand

Under § 8.01-20.1, asking that a defendant be served is itself a certification that the plaintiff already holds a written opinion, signed by a qualified expert, stating that this defendant deviated from the applicable standard of care and that the deviation proximately caused the injuries claimed. Each defendant covered has to be identified in the certification. Within 21 days of an answer, the plaintiff must certify compliance to that defendant. Where the opinion did not exist when service was requested, the court shall impose sanctions and may dismiss with prejudice. One exception exists, for the rare theory whose alleged negligence lies inside the jury's common knowledge, and it is narrower than clients assume. No separate pre-suit notice statute sits in front of this; the certification tied to service is the gate, and the section was amended again in 2025.

### The cap covers the whole recovery, not the noneconomic slice

This is the rule described wrongly most often. Section 8.01-581.15 limits the total amount recoverable for any injury to, or death of, a patient in an action against a health care provider. Not general damages: the total. Medical bills, lost earnings, future attendant care and everything else land inside one figure. It rises $50,000 a year and is keyed to the date of the malpractice rather than the date of suit or verdict. An act occurring between July 1, 2026 and June 30, 2027 carries a ceiling of $2.75 million, where the preceding year sat at $2.70 million, and the schedule keeps stepping until acts on or after July 1, 2031, which are capped at $3 million. Punitive damages are limited separately to $350,000 by § 8.01-38.1, which also directs that the jury never hear about the limit.

### The review panel that almost nowhere else has

Within 30 days of the responsive pleading, either side may request a medical malpractice review panel. The request goes to the Clerk of the Supreme Court of Virginia, which designates the panel within 60 days, and proceedings are stayed while the review runs. Membership is fixed by statute: two impartial attorneys, two impartial health care providers licensed and actively practicing here, and a circuit judge who presides without a vote. Within 30 days of receiving the evidence, the panel issues one or more of four listed opinions, ranging from no support for a standard-of-care failure through support for both failure and causation. The written opinion is admissible at trial but not conclusive, and either side may call a panelist other than the judge as a witness at its own cost.

### Two years, and the four ways it stretches

Section 8.01-243 gives two years from accrual, and then names the exceptions. A retained foreign object with no diagnostic or therapeutic purpose adds one year from the date it is discovered or reasonably should have been. Fraud, concealment or intentional misrepresentation that prevented discovery adds one year from discovery. A negligent failure to diagnose a malignant tumor, cancer, or an intracranial, intraspinal or spinal schwannoma adds one year from the day that diagnosis is communicated to the patient. None of these may push the period past ten years from accrual, apart from tolling for a person under a disability.

### The patient's own conduct gets examined too

Because a contributing share of fault bars a claim here instead of trimming it, the defense reads hard for missed follow-up appointments, an incomplete history given at intake, medication not taken as directed and discharge instructions not followed. That does not make the chart the last word on anything. It does mean the record you keep now matters: dates of calls to the office, portal messages, pharmacy pickups, and what you were told to do and when you did it.

### Two things that sit outside the ordinary claim

Treatment delivered by federal employees, including at a military medical facility in this city, is generally not a state-court matter at all. It runs through the Federal Tort Claims Act, which requires a written claim presented to the agency within two years of accrual and suit within six months of a mailed final denial.

Fees are the other. The Commonwealth sets no percentage; Rule 1.5 requires a reasonable fee and requires a contingent agreement to spell out in writing the method of computation, the percentages and how expenses are handled. The statutory cap constrains the judgment, not what a fee may be."""

NEW["svc_product_liability_lawyer_lede"] = """Nothing about a product claim in this state is automatic. The injured person has to prove the item was unreasonably dangerous for its ordinary use and that the condition existed when it left the hands of the defendant being sued."""

NEW["svc_product_liability_lawyer_body"] = """### What has to be proved, and the accident alone is not it

Whatever label sits on the count, the burden is the same here. In Logan v. Montgomery Ward the Supreme Court of Virginia held that a plaintiff must show the goods were unreasonably dangerous for the ordinary purposes they would be put to, or for a special use brought to the defendant's attention, and that the condition existed when the goods left that defendant's hands. The same opinion refused res ipsa loquitur where an unexplained accident could be attributed to one of several causes, some of them nobody's responsibility. A gas range that exploded was not, standing alone, evidence of a defect. That is why an intact item and a documented chain of custody do more for a claim than a vivid account of the failure.

### Keep the item, and keep every piece of it

The failed thing is the case. Do not repair it, discard it, return it to the store, trade it in or mail it to an adjuster before its condition has been recorded. Keep separated fragments, the packaging, the manual, the receipt or order confirmation, the serial or lot number, and any recall or service notice that arrives afterward. Photograph it at a distance and close up, including labels and printed warnings, since the adequacy of a warning is frequently the entire dispute. Where a landlord, employer, rental operator or repair shop has possession, note who holds it and ask in writing that it be preserved.

### Several limitation periods, and they do not start together

Injury to a person is two years from accrual whatever the theory of recovery, under § 8.01-243(A). Damage to property, including the house or vehicle a product destroyed, gets five years under subsection B. A claim on the sale itself runs four years under § 8.2-725, and it usually accrues at tender of delivery rather than at the failure, unless the warranty explicitly reaches future performance. A signed written agreement, a service contract or extended warranty among them, carries five years under § 8.01-246(A)(2), while an unwritten one carries three. Section 8.01-246(C) then routes the personal-injury part of a products case back to the two-year rule. Somebody who waits on the injury claim because the warranty paperwork looks generous has misread which clock governs.

### Misuse, modification and the risk taken on purpose

Two defenses do most of the work in this category. A contributing share of the injured person's own negligence defeats the claim here rather than reducing it, so how the item was assembled, maintained and operated gets examined line by line. Assumption of risk is separate and personal. Amusement Slides Corporation v. Lehmann described the doctrine as venturousness, applied a subjective test of what the particular plaintiff saw, knew and appreciated, and required both full appreciation of the risk and voluntary exposure to it. Running a tool with its guard removed is the familiar version. That same case marks the limit: accepting an ordinary hazard of an activity is not accepting a hazard the operator created.

### Rented, borrowed and resort-issue equipment

A destination city puts a great deal of unfamiliar equipment into unfamiliar hands. With 14.3 million visitors counted in 2024, the thing that failed was often rented, borrowed or supplied rather than bought: a bicycle, a beach chair, a grill on a hotel deck, a pool gate latch, a ladder on a Hilltop jobsite, an appliance in a Sandbridge rental house. That changes the list of names on the pleading. Manufacturer, importer, distributor, retailer, installer, rental operator and whoever serviced the item last can each be a separate defendant holding separate records, and a rental operator's maintenance log may be the only document showing what the item had been through.

### Where the case sits and who has to be reached

Claims up to $50,000 may be heard in the General District Court of this independent city; past that figure the Circuit Court analysis opens, and that court's stated goal is to conclude a civil case within 18 months of filing. Manufacturers are often somewhere else entirely, so process must go outside the Commonwealth, which is slower and carries a higher statutory service charge than reaching someone in the city. Take the corporate name from the plate, the label or the registration rather than the brand on the box, because the seller, the maker and the entity that must be served are frequently three different companies.

### What the fee rule requires before anything is signed

No percentage for injury work is published by the Commonwealth. Rule 1.5 of the Rules of Professional Conduct requires that a fee be reasonable and lists eight factors for testing one. A contingent agreement must state in writing how the fee is computed, the percentages attaching at settlement, at trial and on appeal, which litigation expenses come off the recovery, and whether the fee is figured before or after those expenses. Expert examination of a failed item is usually the largest expense line in this kind of case, so that ordering is not a technicality."""

NEW["svc_catastrophic_injury_lawyer_lede"] = """A catastrophic claim gets shaped by numbers written down early: the sum pleaded, the cap attached to whoever caused the harm, and a notice deadline that runs from the injury rather than from the day the prognosis becomes clear."""

NEW["svc_catastrophic_injury_lawyer_body"] = """### The figure in the complaint becomes a ceiling

People learn this one late. Section 8.01-379.1 lets any party tell the jury the amount of damages the plaintiff seeks, in opening statement or closing argument or both, and lets the plaintiff request less than the ad damnum. What it does not do is let a verdict rise above the sum pleaded. In a matter where future surgeries, attendant care and a lifetime of lost earning capacity are still being estimated, that pleading has to leave room the medicine has not yet confirmed. Punitive damages are limited separately and sharply: § 8.01-38.1 caps the total against all defendants at $350,000, and the jury is not told the limit exists.

### Who the defendant is decides what is recoverable

The same injury carries different ceilings. Against a private business or an individual there is no statutory cap on compensatory damages. Against a health care provider, § 8.01-581.15 puts everything recoverable for the patient's injury or death inside one figure, $2.75 million for acts between July 1, 2026 and June 30, 2027. Against the Commonwealth or a transportation district, § 8.01-195.3 limits recovery to $100,000 or the maximum limits of any liability policy in force, whichever is greater, and rules out punitive damages and prejudgment interest altogether. Working out which employer stands behind the person who caused the harm is therefore a damages question as much as a liability question.

### Notice deadlines run long before the prognosis is known

Where a locality is involved, § 15.2-209 requires a written statement of the nature of the claim, with the time and place, within six months of accrual, filed with the local attorney, chief executive or mayor. The City Attorney's Office here asks for the claimant's name and address, the incident date, the individuals involved if known, the location and an account of why the City is contended to be responsible, then routes the letter to Risk Management for investigation. Where the defendant is a state agency, § 8.01-195.6 gives one year, and the statement goes to the Director of the Division of Risk Management or the Attorney General, or to the Commissioner of Highways where the agency is the transportation department. In a contested case the claimant must prove the notice was received, which is an argument for a signed delivery receipt.

### A federal connection replaces the whole procedure

Naval Air Station Oceana was commissioned in August 1943 and now runs more than seven miles of runways, with over 14,600 military personnel, 2,000 civilians and 19 fighter and attack squadrons, plus Dam Neck Annex and the Fentress landing field. Where a federal employee's negligence is involved, the Federal Tort Claims Act governs and its sequence is unforgiving. A written claim must be presented to the agency within two years of accrual. No suit may be filed until the agency denies the claim in writing, though six months of silence may be treated as a denial at the claimant's option, and suit must follow within six months of a mailed final denial. Under 28 U.S.C. § 2675(b) the action cannot seek more than the sum stated on that administrative claim, absent newly discovered evidence or proof of intervening facts. On a brain or spinal cord injury, a cautious number written on the form early can cost more than any argument made later.

### Fault remains all or nothing in a severe case

Catastrophic harm does not soften the fault rule one bit. Where the injured person's own lack of reasonable care helped bring about the event, the claim can be defeated rather than discounted, which is why the defense in a serious case invests so heavily in reconstructing the seconds beforehand. Statements made in an emergency department, posted on social media or given to a claims representative are read with that in mind. The answer is not silence. It is precision about what is actually known, and candor about what is not.

### Building the damages record while treatment continues

Keep it in date order and keep it dull. Therapy plans and discharge instructions, work restrictions and leave paperwork, wage and benefit records, treatment mileage, equipment and home-modification receipts, and a log of the tasks family members absorbed and the hours they spent on them. Photographs of a ramp, a widened doorway or a lift installed at home document a loss that a bill alone does not explain. Two years is the outer limit for filing the injury claim and five years for damaged property, and neither period waits for a stable prognosis.

### What the fee rule requires when the numbers are large

Percentages for injury work are not set by the Commonwealth. Rule 1.5 requires a reasonable fee tested against eight listed factors, and requires a contingent agreement to put in writing the method of computing the fee, the percentages attaching at settlement, at trial and on appeal, the expenses charged against the recovery, and whether the fee is calculated before or after those expenses come off. In a case carrying life-care planning, vocational and economic experts, that ordering moves real money. When the matter ends, the client is entitled to a written statement of the outcome and of how any remittance was figured."""

for k, v in NEW.items():
    if re.search(r"^## " + re.escape(k) + r"\n", text, re.M):
        text = set_block(text, k, v)
    else:
        text = text.rstrip() + "\n\n## " + k + "\n\n" + v.strip() + "\n"

P.write_text(text)
print("ok", len(text.split()))
