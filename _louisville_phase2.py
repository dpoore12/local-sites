#!/usr/bin/env python3
"""Phase 2 conversion for louisvillecaraccidentlawyerpros.com."""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
SITE = ROOT / "sites" / "louisvillecaraccidentlawyerpros.com"

SYMPTOMS = {
"symptom_1": """A rear-end hit can leave a bumper cover looking almost clean while the person inside took a hard snap. Photograph both vehicles before either leaves on a flatbed, keep the tow slip and the repair estimate, and note where traffic had already stopped. Get the report number. In this state the billing total matters as much as the dent, so treat the medical record as evidence.""",

"symptom_2": """A driver who leaves cannot be described accurately from memory a month later. Within the hour, write down direction of travel, color, body style, damage, lettering and any partial plate, then ask nearby businesses to hold exterior video before it cycles. Tell a police officer from the scene. Your own uninsured motorist coverage becomes the claim, and it lives on the declarations page.""",

"symptom_3": """An empty liability policy does not end a Jefferson County claim; it moves the claim onto your own contract. Kentucky places uninsured motorist coverage in a liability policy unless a named insured rejected it in writing, while underinsured coverage exists only if somebody asked for it. Count the vehicles on the declarations page, and do not cash a small liability check before reading that endorsement.""",

"symptom_4": """An early number usually lands before the treatment file is finished. Ask which coverage it comes from, because reparation benefits, property damage, bodily injury and underinsured benefits are four separate subjects with four separate rules. Read what the release closes. One signature on a liability settlement can wipe out underinsured coverage that had thirty days to answer the notice.""",
}

NEW_BLOCKS = r"""
## services_summary

Four unrelated jobs reach this office under one label. A rear-end file turns on the queue, the report number, and the medical expense total that decides whether pain and suffering is claimable here at all. A file with a missing or uninsured driver runs on your own declarations page, where one coverage is automatic and the other exists only because somebody requested it. A truck file reaches federal paperwork with retention clocks as short as six months. A negotiation file is about subtractions, releases and written consent. Filing a claim under the wrong one of those is how a reparation benefit runs dry unnoticed.

## services_pick_head

Start with the part of the claim that stalled

## crosslink_head

Another Louisville crash question?

## svc_rear_end_collision_lawyer_lede

Blame is rarely the fight in a rear-end file. The fight is the medical expense figure that unlocks noneconomic damages in this state, the queue that had formed before impact, and which deadline the reparation payments have quietly moved.

## svc_rear_end_collision_lawyer_body

### The gate before damages are even discussed

Kentucky asks a question most states never reach. Under KRS 304.39-060(2)(b), a plaintiff may recover for pain, suffering, mental anguish and inconvenience only where medical expense benefits payable for the injury exceed $1,000. The statute also opens the door for a listed injury: permanent disfigurement, a bone fracture, a compound, comminuted, displaced or compressed fracture, loss of a body member, permanent injury within reasonable medical probability, permanent loss of bodily function, or death. Someone entitled to free medical and surgical benefits can satisfy the same requirement by showing treatment of equivalent value. That is why an unbilled emergency visit, an unread imaging order, or three skipped therapy sessions can matter more here than the depth of the crush on your trunk lid.

### Where this county turns a fast road into a wall

Rear-end impacts need speed followed by a sudden stop, and the county keeps building both. On the Watterson Expressway, the Transportation Cabinet is reconstructing I-264 from KY 1447 at Westport Road to I-71, mile point 21.1 through 22.7, widening two lanes each direction to three and rebuilding the U.S. 42 interchange as a single-point urban interchange. It is a $130 million job carrying two eleven-foot lanes through its phases, with completion anticipated in fall of 2027. Downtown, the Kennedy Interchange where I-65, I-64 and I-71 converge was rebuilt in the Downtown Crossing at $1,478 million in year-of-expenditure dollars including financing, leaving six northbound I-65 lanes on the Lincoln Bridge and six southbound on the rehabilitated Kennedy Bridge. Tolls then redistribute the traffic. Crossing on a transponder account costs $2.79 against a standard toll of $5.57, so the free Clark Memorial and Sherman Minton spans collect the drivers avoiding both.

### Two deadlines, and the one almost nobody counts

The general injury period in KRS 413.140(1)(a) is one year after the cause of action accrued, which is the figure people find first and misapply. A crash claim runs on KRS 304.39-230(6) instead. An action for tort liability not abolished by KRS 304.39-060 may be commenced no later than two years after the injury, the death, or the date of issuance of the last basic or added reparation payment made by any reparation obligor, whichever occurs later. Read the last clause twice. A reparation check issued in month eleven can push the filing date well past the anniversary of the wreck. Two carve-outs matter. A replacement payment, meaning one reissued in the same amount because the original was lost, stolen or never delivered, does not extend anything past the original payment date. And the obligor must tell a claimant or the claimant's attorney, on written request, whether a payment was a replacement.

### Reporting duties, and what the report costs

KRS 189.635(3)(a) requires immediate notification of a law enforcement officer having jurisdiction when a crash causes personal injury or leaves a vehicle inoperable, and if the driver cannot do it, the duty shifts to the owner or any occupant. Where no officer investigates and property damage passes $500, subsection (5)(a) puts a written report on the driver within ten days. Officers file through the E-CRASH system described in 502 KAR 15:010, and the originating agency stays responsible for releasing the report to authorized parties. A copy runs $5 on paper or $10 through the state police website, and the agency asks people to allow ten days before looking for it.

### Guesses become quotations

A recorded statement invites three estimates: how fast you were closing, how many car lengths back you were, how long the vehicle ahead had been stopped. Each guess is written down and read back later as though it were measured. Not knowing is an honest answer. Two other habits cost cases in the same week. One is releasing the vehicle for salvage before its condition is documented. The other is describing your injuries as fine because standing in a roadway is a poor place to notice a shoulder.

### The percentage the other side wants

Expect a theory that you share the blame. KRS 411.182 has the fact finder answer interrogatories setting the damages as if contributory fault were disregarded, then the percentage of total fault allocated to each claimant and defendant, after which the court states each party's equitable share. No percentage cuts a claimant off, so the argument is arithmetic rather than survival. There is a second subtraction people miss: tort liability is abolished to the extent reparation benefits are payable, and those benefits are capped at $10,000 for one person's economic loss from one accident under KRS 304.39-020(2).

### What follows first contact, and how the fee is measured

The opening work is a list rather than a story: crash date and location, the report number and agency, photographs, witnesses, both declarations pages, and a dated treatment timeline. Requests then go out together for the report, for camera footage while it exists, and to each carrier. Where a case belongs is a dollar question. District Court holds exclusive jurisdiction up to $5,000 exclusive of interest and costs under KRS 24A.120, and above that line the case sits in Circuit Court, which convenes at the Judicial Center on West Jefferson Street. Fees are governed by SCR 3.130(1.5)(a), which fixes no percentage and instead bars an unreasonable fee and unreasonable expenses under eight listed factors.

## svc_uninsured_driver_claim_lawyer_lede

When the other driver leaves, carries nothing, or carries a limit that runs out during the imaging bill, your own policy becomes the case. Kentucky treats its two motorist coverages very differently, and one of them exists only on request.

## svc_uninsured_driver_claim_lawyer_body

### Nobody in this file is arguing about who caused it

Liability is usually admitted, irrelevant or untraceable. What is actually disputed is which policy answers. Three versions arrive from Jefferson County roads. A driver produces no card at all. A driver produces a card and the carrier reports the policy had lapsed before the crash date. Or the coverage is real but thin, because KRS 304.39-110 sets the floor at $25,000 for bodily injury to one person, $50,000 for everyone hurt in one accident and $25,000 for property damage, with a single-limit alternative of $60,000. An ambulance run and one night of observation can consume the first of those figures.

### One coverage is automatic, the other has to be asked for

This is the distinction that decides most of these claims. Under KRS 304.20-020, no liability policy may be issued for a vehicle registered or principally garaged in the Commonwealth unless uninsured motorist coverage is included at the KRS 304.39-110 limits, subject to a named insured's right to reject it in writing. That rejection binds every insured under the policy, and once made, the coverage need not reappear on a renewal unless a named insured requests it in writing. Underinsured coverage works the opposite way. KRS 304.39-320 says every insurer shall make it available upon request, which means a policy without it is perfectly lawful, and defines an underinsured motorist as a party carrying liability coverage in an amount less than a judgment recovered against that party.

### The definition also reaches insured cars

Do not treat a card as the end of the inquiry. The uninsured motorist statute deems a vehicle uninsured where the liability carrier cannot pay because of insolvency, where the applicable liability amounts fall below the KRS 304.39-110 limits, and to the extent the liability insurer denies coverage. Insolvency protection carries a condition worth diarying: it applies where the tortfeasor's liability insurer becomes insolvent within one year after the accident.

### Thirty days sit between you and any release

Signing too early is the classic way to erase the coverage that was going to carry the rest of the loss. KRS 304.39-320 requires written notice by certified or registered mail to every underinsured motorist carrier when a proposed liability settlement would not fully satisfy the claim. The carrier then has thirty days to consent or to preserve subrogation. If it consents or simply does not respond, the claimant may execute a full release of the liability insurer and finalize that settlement without prejudice to the underinsured claim. If it refuses in order to keep subrogation, it must pay the amount of the liability insurer's written offer within thirty days of receiving the notice. Sequence, in other words, is worth money.

### When no reparation coverage answers at all

A hit-and-run leaves the reparation side unanswered too, and Kentucky planned for that. KRS 304.39-160 allows basic reparation benefits through the assigned claims plan where reparation insurance is not applicable to the injury, cannot be identified, is inadequate because the obligor cannot meet its obligations, or where a claim was rejected for some reason other than non-entitlement. Vehicles whose insurance cannot be identified is the branch that fits an unidentified driver. Subsection (4) closes the door on one group: an owner who was required to carry security on the vehicle occupied and failed to have it in effect cannot use the plan.

### The election on file changes what the driver can claim

Kentucky presumes acceptance of the reparations act by anyone who registers, operates, maintains or uses a vehicle on public roadways. Rejecting that presumption takes the form the Department of Insurance prescribes, filed before the accident it is meant to govern, and 806 KAR 39:030 names it: the Kentucky No-Fault Rejection Form, mailed as an original plus one copy or submitted through the online version, effective on the department's file stamp, with a file-stamped copy sent to the insurer. The form itself must state in bold print that accepting this insurance denies the applicant the right to sue a negligent motorist unless policy requirements are met. There is also a proviso worth checking against the other driver. Someone who had no basic reparation insurance, never filed a rejection, yet had security equivalent to KRS 304.39-110 in effect is deemed to have fully rejected the tort limitations for that accident only.

### What your own carrier does once it becomes the opponent

Expect it to behave like an adverse party, because on this claim it is one. Reparation benefits are payable monthly as loss accrues and become overdue if unpaid thirty days after the obligor receives reasonable proof of the fact and amount of loss, with a partial claim of $100 or more capable of going overdue by itself. Overdue payments bear interest at twelve percent a year, and eighteen percent where the delay was without reasonable foundation, under KRS 304.39-210. The unfair claim settlement practices listed in KRS 304.12-230 include refusing to pay without conducting a reasonable investigation and compelling insureds to sue by offering substantially less than what those insureds ultimately recover.

### After first contact, and how fees are set here

Work starts with the contract rather than the story: limits, the number of insured vehicles, any written uninsured rejection, any request that produced underinsured coverage, notice provisions, and the consent language. Requests go to the investigating agency for the report, to the carrier for the complete policy, and to providers for records and billing. On money, no Kentucky statute prints a percentage for a crash claim. SCR 3.130(1.5)(c) requires a contingent agreement in a writing signed by the client, stating the percentages at settlement, trial and appeal, which expenses are deducted, whether that subtraction happens before the fee is figured, and a plain warning about expenses owed whether or not the client prevails.

## svc_commercial_truck_collision_lawyer_lede

A tractor-trailer case is a records case against a company, not an argument with a driver. The documents that decide it sit on federal retention clocks, and the shortest of them are measured in hours rather than months.

## svc_commercial_truck_collision_lawyer_body

### Why a company file looks nothing like a car file

Two vehicles collide and the paperwork multiplies. Behind the driver stand an employer, a dispatcher, a maintenance program, a drug and alcohol testing policy, a shipper, and often a broker or an equipment provider. Each of those relationships generates records that either support or contradict what the driver said at the roadside. That is also why fault can be shared several ways: KRS 411.182 has the fact finder allocate a percentage of total fault to every party in the action, including third-party defendants and anyone released, and a release reduces the claim by the released party's equitable share rather than by whatever that party paid.

### The paperwork with the shortest life

Federal retention rules are generous to nobody in a hurry. Driver records of duty status and their supporting documents need be kept only six months from the date of receipt under 49 CFR 395.8(k), and the driver carries just the previous seven consecutive days in the cab. The same section gives the driver thirteen days to submit a record covering a 24-hour period to the carrier, so a log may not yet exist on the company's server the week you call. One register lasts longer. Under 49 CFR 390.15(b) a motor carrier must maintain an accident register for three years, listing the date, the city or town and state, the driver's name, the number of injuries, the number of fatalities, and whether hazardous materials other than spilled fuel were released, together with copies of accident reports required by state authorities or insurers. Subsection (a) obliges the carrier to make all records and information pertaining to an accident available to authorized representatives.

### The testing window shuts the same day

Post-accident testing under 49 CFR 382.303 runs on a clock nobody can reopen later. Alcohol and controlled substance testing is required after a fatality, and also where the driver receives a citation for a moving violation arising from the crash if there was bodily injury needing immediate treatment away from the scene, or disabling damage requiring a tow. The citation must land within eight hours for the alcohol test and thirty-two hours for the controlled substance test. If the alcohol test is not administered within two hours, the employer has to record why; attempts stop at eight hours for alcohol and thirty-two hours for drugs, each requiring a written explanation. Law enforcement breath, blood or urine results can satisfy the rule where the employer obtains them, and a driver who does not remain available may be deemed to have refused.

### The corridor that puts this traffic here

Freight geography explains the caseload. Three tolled crossings link Louisville Metro with southern Indiana, the Abraham Lincoln and Kennedy bridges on I-65 and the Lewis and Clark Bridge on KY 841, where a rig with five or more axles pays $16.62 per crossing after the 3.8 percent adjustment that took effect on the first of July in 2026. The Clark Memorial and Sherman Minton crossings are free, which shapes route choices before a truck ever reaches the Kennedy Interchange, the point where I-65, I-64 and I-71 all land in the same downtown junction. Add a live work zone: I-264 is down to two eleven-foot lanes in places between Westport Road and I-71 while the U.S. 42 interchange is rebuilt. Statewide, the Transportation Cabinet counted 9,446 truck-related crashes in 2024, including 73 fatal ones.

### Kentucky rules still govern the recovery

Federal regulations describe the duty; state law sets what the claim is worth. The reparations act applies to any vehicle transporting persons or property on public highways, so the threshold in KRS 304.39-060(2)(b) still has to be met before pain and suffering is claimable, whether the other vehicle was a sedan or a semi. Reparation benefits remain capped at $10,000 for one person's economic loss from one accident, and tort liability is abolished to the extent those benefits are payable. The filing deadline is the same two-year measure from KRS 304.39-230(6), running from the injury, the death, or the issuance date of the last reparation payment, whichever falls later.

### The first two weeks matter more than the first two months

Ask in writing that the vehicle, the electronic control module data, the logs, the dispatch records, the maintenance file and the driver qualification file be preserved, and date the request. Photograph the trailer markings, the placards, the door lettering and the number on the tractor before anything is repaired or repainted. Obtain the collision report for $5 on paper or $10 online, and note that the investigating agency, not the state police, remains the custodian when a local officer wrote it. Keep every bill and explanation of benefits, since the reparation ledger sets both the threshold and the deadline.

### What happens after contact, and what the process costs

The first pass identifies the parties: driver, employing carrier, vehicle owner, trailer owner, broker, and the insurer behind each. Preservation letters go out, then records requests, then the report. A suit above the $5,000 District Court line under KRS 24A.120 belongs in Circuit Court, where the civil filing fee is $188 under CR 3.02(1) as amended for 2026, with a $20 court technology fee and other required charges collected by the clerk. Kentucky sets no percentage for a fee in this work. SCR 3.130(1.5)(a) instead forbids an unreasonable fee or an unreasonable amount for expenses, measured against eight factors that include the customary charge in the locality and the result obtained.

## svc_injury_claim_negotiation_lede

Negotiation in this state is arithmetic before it is persuasion. What the reparation carrier paid, what the threshold requires, what a release closes and what a percentage of fault removes all change the number before anyone argues about pain.

## svc_injury_claim_negotiation_body

### What is actually being negotiated

Start with the subtraction nobody explains. Tort liability for bodily injury is abolished to the extent basic reparation benefits are payable, so the portion of medical bills and lost wages those benefits cover is not chargeable to the at-fault driver. Those benefits stop at $10,000 for all economic loss to one injured person from one accident under KRS 304.39-020(2), regardless of how many carriers might owe them, and the same section caps funeral, cremation and burial charges at $5,000 per person. Above the reparation ceiling, the liability claim has to carry the remaining economic loss plus the human loss, and only if the threshold in KRS 304.39-060(2)(b) is satisfied by medical expense benefits above $1,000 or by a listed injury such as a fracture or a permanent injury within reasonable medical probability.

### The clock the offer is riding on

An adjuster who knows the file better than you do knows the deadline too. For a motor vehicle tort claim, KRS 304.39-230(6) allows two years measured from the injury, the death, or the date of issuance of the last basic or added reparation payment by any obligor, whichever comes later. A replacement payment reissued in the same amount because the first was lost, stolen or undelivered does not move the date, and the obligor must answer a written request about whether a payment was a replacement. There is a second period in the same statute: where benefits have been paid, a claim for further benefits may be brought within two years of the last payment. Both dates come off the payment ledger, which is a document to request rather than a fact to assume.

### Before the liability carrier gets its release

A release is a one-way door and Kentucky puts a step in front of it. Where a proposed liability settlement will not fully satisfy the claim, KRS 304.39-320 requires written notice by certified or registered mail to every underinsured motorist carrier, which then has thirty days to consent or to keep its subrogation rights. Consent or silence lets the claimant sign a full release of the liability insurer and close that settlement without prejudice to the underinsured claim. A refusal obliges that carrier to pay the amount of the written liability offer within thirty days. Skipping the notice is how a modest check ends a much larger claim.

### What the reparation carrier owes, and when it owes interest

Benefits are payable monthly as loss accrues, not in a lump at the end. They become overdue if unpaid within thirty days after the obligor receives reasonable proof of the fact and amount of the loss, and a part of a claim totaling $100 or more can be overdue on its own. Overdue amounts carry twelve percent annual interest under KRS 304.39-210, rising to eighteen percent where the delay was without reasonable foundation. Two more details from that statute shape the ledger: a provider generally has to submit a charge within 180 days of rendering the product or service, and a medical expense submitted in accordance with the statute is presumed reasonable.

### The statutory list to read before the next call

KRS 304.12-230 defines unfair claim settlement practices, and several of them describe familiar behavior. Failing to acknowledge and act reasonably promptly on communications about a claim. Refusing to pay without conducting a reasonable investigation based on all available information. Failing to affirm or deny coverage within a reasonable time after proof of loss statements are complete. Not attempting in good faith to reach a prompt, fair and equitable settlement where liability has become reasonably clear. Failing to promptly settle one portion of a policy's coverage in order to influence settlement under another portion. Keeping a dated log of what was requested and when it was answered turns a frustration into a record.

### Where the percentage argument lands

The other side will argue you contributed. KRS 411.182 sets the mechanics: damages are first determined as if contributory fault were disregarded, then a percentage of total fault is allocated to each claimant, defendant, third-party defendant and released person, and the court states each party's equitable share of the obligation. No cutoff exists, so a share of blame reduces a recovery rather than ending it. Note subsection (4) when several parties are involved, because releasing one reduces the claim against the others by that person's equitable share, not by the money actually paid.

### If the file has to move, and what the market charges

Two dollar figures decide where a suit goes. District Court has exclusive civil jurisdiction to $5,000 exclusive of interest and costs under KRS 24A.120, and Circuit Court is the court of general jurisdiction above it, sitting at the Judicial Center while the clerk's office and District Court occupy the Hall of Justice a block away. Filing costs $188 under CR 3.02(1) as amended for 2026, plus a $20 technology fee and other required charges. Collision report copies run $5 on paper and $10 online. Fees on the representation itself have no percentage ceiling in Kentucky; SCR 3.130(1.5) bars an unreasonable fee, requires a signed writing and a closing statement showing the outcome and remittance, and bars result-based fees in criminal and most domestic matters.
"""


def replace_block(text: str, key: str, body: str) -> str:
    pattern = re.compile(r"(## " + re.escape(key) + r"\n\n)(.*?)(?=\n## )", re.S)
    if not pattern.search(text):
        raise SystemExit("block not found: " + key)
    return pattern.sub(lambda m: m.group(1) + body.strip() + "\n\n", text, count=1)


def main() -> None:
    copy_path = SITE / "copy.md"
    text = copy_path.read_text()
    for key, body in SYMPTOMS.items():
        text = replace_block(text, key, " ".join(body.split()))
    text = text.rstrip("\n") + "\n" + NEW_BLOCKS.rstrip("\n") + "\n"
    copy_path.write_text(text)

    cfg_path = SITE / "site.json"
    raw = cfg_path.read_text()
    raw = raw.replace('"phase": 1,', '"phase": 2,', 1)
    cfg_path.write_text(raw)
    assert json.loads(raw)["phase"] == 2
    print("done")


if __name__ == "__main__":
    main()
