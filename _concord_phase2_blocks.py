#!/usr/bin/env python3
"""Patch concordcaraccidentlawyerpros.com copy.md to phase 2."""
import re, pathlib, json

SITE = pathlib.Path("/home/user/workspace/local-sites/sites/concordcaraccidentlawyerpros.com")
copy = SITE / "copy.md"
txt = copy.read_text()

SYMPTOMS = {
1: """A vehicle striking yours from behind does not settle the fault question here, because a defense that pins even a sliver of the blame on you can end a claim outright. Photograph both bumpers, the reinforcement bar behind the plastic cover, and the stopped line of traffic before anything is towed. Get the report number, and leave your estimate of speed and following distance blank.""",
2: """A driver who leaves turns this into a coverage question, and the answer sits on your own declarations page: uninsured motorist coverage in this state reaches hit-and-run vehicles too. The police department here will not take a hit-and-run through its online form or its telephone reporting line, so the call has to be dispatched. Write down the partial plate, the decal, the damaged side, and the direction of travel.""",
3: """Since July 1, 2025 every new or renewed policy in the state carries underinsured motorist coverage alongside uninsured coverage, and whether the other vehicle counts as underinsured now turns on your total damages rather than a comparison of limits. Ask for declarations pages instead of an insurance card. Get written consent from your own carrier before anyone endorses a liability check.""",
4: """An early number is priced on the thin file the adjuster already holds, and the release stapled to it can close the coverage on your own policy at the same moment. Before answering, list the care still recommended, the shifts already missed, and every carrier that has written to you. Then ask what that document releases, line by line.""",
}

for i, body in SYMPTOMS.items():
    pat = re.compile(r"(## symptom_%d\n)(.*?)(\n## )" % i, re.S)
    assert pat.search(txt), i
    txt = pat.sub(lambda m: m.group(1) + body.strip() + "\n" + m.group(3), txt)

NEW = r"""
## services_summary

Four different jobs arrive in Cabarrus County wearing one label. A rear-end file is decided by the sequence of impacts and by whether the other side can pin any share of the blame on you, which in this state is not a discount but a wall. An uninsured or hit-and-run file is decided by your own declarations page and the notice terms printed inside it. A truck file reaches federal records a carrier may lawfully discard six months after receipt. A negotiation file is about damages, liens, and the exact wording of a release. Sorting a claim into the wrong one of those is how a coverage path quietly closes.

## services_pick_head

Which of these four is your claim?

## crosslink_head

Another kind of crash file?

## svc_rear_end_collision_lawyer_lede

A rear-end claim here rarely comes apart over who struck whom. It comes apart over one sentence about following distance, a bumper structure nobody photographed, and a guess about seconds that the metal never supported.

## svc_rear_end_collision_lawyer_body

### Read the damage before the car leaves on a flatbed

Walk the vehicle while it is still sitting where it stopped. Crush at the back and crush at the front means you were a middle link in a chain, and the middle vehicle is the one both other drivers will describe least accurately. If the plastic cover already hangs loose, photograph the reinforcement bar behind it. A shallow scuff on the outside can sit in front of a folded absorber, which is the part that shows how hard the hit really was. Shoot the head restraints and seat backs too. A seat that moved on impact stops being evidence the day a salvage yard takes the car.

### Following too closely is a traffic rule, not a fault finding

G.S. 20-152(a) tells a driver not to follow another vehicle more closely than is reasonable and prudent, measured against the speed of both vehicles and the condition of the road. That is the rule most citations in these cases rest on. It is not a civil verdict. An officer may write nothing at all and an adjuster will still argue distance, and a citation against the other driver does not stop the same argument from being aimed at you.

### A sliver of blame is the whole fight in this state

Most of the country reduces a recovery by the injured person's share of fault. North Carolina still bars the recovery when that person's own negligence joined with the defendant's in producing the harm, even where the contribution looks small next to the other driver's. One thing sits on the defense side of the ledger: G.S. 1-139 puts the burden of proving contributory negligence on the party asserting it. One narrow escape sits on yours. The pattern jury instruction on last clear chance asks the injured person to prove four things by the greater weight of the evidence. You were negligently put in a peril you could not escape by reasonable care, the other driver knew or should have discovered it, that driver had the time and means to avoid the harm, and the failure to use them caused it.

### Where this county stores its stop-and-go

Rear-end impacts need a fast road that stops without warning, and the corridor supplies them twice over. NCDOT is rebuilding I-85 through the county as an eight-lane divided facility across roughly 6.8 miles, from south of Bruton Smith Boulevard and Concord Mills Boulevard to north of N.C. 73, with interchange modifications along the way. Then the race calendar arrives. Before NASCAR weekends the department plans with local agencies for heavier volume on I-85, U.S. 29, N.C. 49 and Bruton Smith Boulevard, and it has said plainly that Bruton Smith often carries the most traffic because navigation apps route everyone onto it. The county recorded 5,928 reported crashes in 2023, with 2,125 people injured and 29 killed.

### Which report exists, and who is holding it

A crash counts as reportable when someone is hurt or killed, or when total property damage reaches $1,000. An investigating officer has to produce a written report within 24 hours, and a local agency that receives one must forward it to the Division within 10 days. The city police portal will search accident reports by name, driver license, date of occurrence, accident number, or insurance policy number. NCDMV sells individuals a redacted copy only, ordered in person or by mail on form TR-67A, with 10 business days allowed for mail requests and Huntersville the nearest listed counter. One distinction matters later: a crash report written by someone other than an officer is without prejudice and cannot be used as evidence, while an officer's report is a public record and may be used as the rules of evidence allow.

### The first days, in a workable order

Get treated, and let the record show the gap between the wreck and the first visit is short. Back up every original photo and dash-camera file before sharing copies. Ask the businesses along the boulevard for their footage in writing within days, because those systems recycle quickly. Keep the vehicle intact until the bumper structure and seats have been photographed. Decline to estimate speed, distance, or seconds in a recorded statement; "I did not measure that" is a complete answer and a true one.

### The clocks, and how a fee gets measured

Three years is the ordinary limit under G.S. 1-52(16), running from when bodily harm became apparent or reasonably should have, with no claim accruing more than 10 years after the last act or omission. A death claim is shorter: two years under G.S. 1-53(4), accruing at the date of death. On fees, this state fixes no percentage for a driving case. Rule of Professional Conduct 1.5(a) forbids a clearly excessive fee and lists eight factors for testing one, and 1.5(c) requires a signed writing giving the calculation method, the percentages at settlement, trial and appeal, and whether expenses come off before or after the share is figured. Court charges are separate and public: $200 to open a superior court civil case, $150 in district court, and $30 for each item the sheriff serves.

## svc_uninsured_driver_claim_lawyer_lede

When the other driver has no policy, no identity, or a limit that stops short of the hospital bill, the claim moves onto your own coverage. Two provisions of that policy carry deadlines, and one of them is measured in days.

## svc_uninsured_driver_claim_lawyer_body

### The tell is that nobody is arguing about fault

In these files the other driver admits it, left the scene, or was never identified, and the conversation is entirely about which policy responds. Three versions show up around the county. The driver who produces no card at all, the driver whose carrier says the policy had already lapsed, and the driver whose limit is genuine but small. All three send you to the same two documents: your declarations page and the endorsement almost nobody opens.

### What the Financial Responsibility Act puts inside your policy

G.S. 20-279.21 requires uninsured motorist coverage in a bodily injury liability policy issued here, and it names hit-and-run vehicles alongside uninsured ones. The uninsured motorist limit is set equal to the highest bodily injury liability limit on any one vehicle under the policy, subject to a ceiling of $1,000,000 per person and $1,000,000 per accident, and a named insured may buy more or less so long as the floor set by the statute holds. There is property damage coverage too, matched to the highest property damage limit on the policy, with the first $100 of damage excluded. A written statement from the other vehicle's liability insurer saying the vehicle was uninsured operates as a prima facie presumption of exactly that.

### July 2025 changed both numbers and the arithmetic

For every policy written or renewed on or after July 1, 2025, the compulsory liability minimums here are $50,000 for one person, $100,000 per accident, and $50,000 for property damage, up from 30/60/25. The Department of Insurance also confirms what the statute now requires: underinsured motorist coverage is included in all new or renewed policies, where before it was absent from policies carrying the old minimum limits. The definition changed as well. A vehicle is underinsured when the liability limits available at the time of the crash come to less than the total damages the injured person sustained, rather than being judged by a comparison of policy limits. The underinsured amount is not reduced by a setoff or credit against other coverage, workers' compensation aside.

### What may be added together, and what may not

Two policies can help; two cars on one policy cannot. Where a claimant is insured for underinsured coverage under separate or additional policies, the total is figured by combining the highest limit available under each policy, for nonfleet private passenger vehicles. The same statute then shuts the other door: limits applicable to one vehicle under a policy may not be combined with or added to the limits applicable to another vehicle under that same policy. Read the endorsement before assuming a three-car household has three times the protection. Policies covering only commercial vehicles or only fleets are not required to carry either coverage at all.

### Two steps that run on their own clocks

Before suit is filed against an uninsured motorist, notice goes to your insurer, and no action may be started until 60 days after that notice is posted or delivered. Missing it does not get the case dismissed, but it extends the insurer's answer time to 60 days. The second step protects the coverage. Where the carrier receives written notice before you settle with the underinsured driver, it loses its right of subrogation and its right to approve that settlement if it does not advance a payment equal to the tentative settlement within 30 days. Notice first, endorsement second, in that order.

### Why the driver with no policy may go quiet

The Division acts on a lapse the moment it gets notice of a terminated policy. The owner has 10 days to respond, and a penalty follows: $50 where there was no other lapse in the previous three years, $100 with one, $150 with two or more, plus a $50 restoration fee when a revoked registration is put back. Operating or permitting operation without the required coverage is a Class 3 misdemeanor under G.S. 20-313. None of that pays your medical bills, and all of it explains why the person who caused the wreck may become hard to reach.

### The report, the deadline, and the rule that still applies

Traffic crashes and hit-and-run reports cannot be filed through the city police department's online form or its telephone reporting unit, so the call goes through the communications center and an officer is dispatched. That dispatch is what produces the report your carrier will ask for, searchable afterward by name, license, date, accident number, or policy number. The three-year injury limit under G.S. 1-52(16) keeps running while coverage questions are sorted out, and two years applies to a death claim. Contributory negligence does not disappear either. Your own insurer steps into the shoes of the driver who caused the harm, which means the defense that would have been raised by that driver can be raised across the table by the company you pay.

## svc_commercial_truck_collision_lawyer_lede

A tractor-trailer claim is a records claim with a timer on it. The federal logs describing the driver's day may be destroyed six months after the carrier received them, which puts the preservation letter ahead of nearly everything else.

## svc_commercial_truck_collision_lawyer_body

### Photograph the equipment, not only the damage

Doors and trailers carry the information that decides who answers for the crash. A USDOT number, a carrier name, a lease decal, a different name on the tractor than on the box, a placard, an axle count, a load that shifted: each of those can point at a separate company. Tractor, trailer, freight and driver are frequently four contracts rather than one business, and paperwork is the only thing that sorts them out. Photograph all of it before the equipment is moved, and note whether a second name appeared anywhere on the rig.

### Why this corridor carries what it carries

I-85 is the freight spine through the county, and NCDOT is widening roughly 6.8 miles of it to an eight-lane divided facility between the Bruton Smith Boulevard area and a point north of N.C. 73, with interchange work included. Heavy vehicles share that stretch with distribution traffic around Concord Mills and, several weekends a year, with race crowds that NCDOT plans for on I-85, U.S. 29, N.C. 49 and Bruton Smith Boulevard. Work zones, ramp queues and unfamiliar drivers arrive together. Against that background the county logged 5,928 reported crashes in 2023, with 2,125 injuries and 29 deaths.

### The insurance behind a truck is set by schedule

State law borrows the federal figure. G.S. 20-309(a1) requires the owner of a commercial motor vehicle to carry financial responsibility equal to what a for-hire carrier hauling nonhazardous property in interstate commerce must carry under 49 C.F.R. 387.9. That schedule sets $750,000 for nonhazardous property in vehicles rated at 10,001 pounds or more. Oil and most listed hazardous materials sit at $1,000,000, and bulk hazardous substances at $5,000,000. Deeper coverage cuts both ways, because a carrier with that exposure will spend on reconstruction and on an argument that some of the fault belongs to you.

### The paperwork that ages out first

Federal rules put a floor under the records, not a promise. A motor carrier must keep records of duty status and their supporting documents for each driver for not less than six months from the date of receipt. The driver qualification file lasts longer, held while the driver is employed and for three years after, and it contains the employment application, the motor vehicle record from each licensing authority, the road test certificate or an accepted equivalent, the annual inquiry and review, and the medical examiner's certificate. A preservation demand should name the tractor, the trailer, the date and the driver, and ask for electronic logging data, dispatch records, maintenance and inspection files, and any onboard video.

### The gap in the policy on the truck

If you were hurt while driving for work, check whose policy you were under before counting on your own protections. A motor vehicle liability policy written only for commercial vehicles, or only for a fleet, is not required to provide uninsured or underinsured motorist coverage. That exemption can leave a company vehicle without the second layer a family car would carry, and it is the reason a household policy has to be read alongside the business one.

### What the defense does with a strict fault rule

It aims at the small things. Because a recovery here can be barred outright when the injured person's own negligence helped produce the harm, an adjuster gains far more from a theory about your following distance, your lane change or your brake lamps than a comparative fault state would allow. G.S. 1-139 does place the burden of proving that defense on the party raising it, and the last clear chance doctrine offers a narrow route back for someone who could not escape a peril the other driver had time and means to avoid. Neither makes a loose statement at the scene harmless.

### What follows contact, and what the courthouse costs

The early work is documentary. Preservation letters go out, the crash report is requested, the vehicles are examined before repair or release, and the electronic data is considered while it still exists. Deadlines run alongside: three years for injury under G.S. 1-52(16), two for a death claim under G.S. 1-53(4). Costs are public and separate from any fee. Opening a superior court civil case runs $200, district court $150, and the sheriff charges $30 for each item served, so a tractor owner, a trailer owner and a corporate registered agent are billed three times. As for the share itself, no percentage is fixed by statute here. Rule 1.5(a) bars a clearly excessive fee against eight listed factors, and 1.5(c) requires the terms in a signed writing.

## svc_injury_claim_negotiation_lede

An offer is a number attached to a document. The number reflects only what the adjuster has read so far, and the document usually closes every claim from that crash, including the coverage sitting on your own policy.

## svc_injury_claim_negotiation_body

### Check what the file could possibly contain

If the adjuster holds a repair estimate and one emergency department bill, the offer is priced on paperwork rather than on an injury. Four questions expose it. Has imaging happened, is any care still being recommended, has anyone written down the work restrictions, and does the carrier have the officer's report yet. An offer that arrives before the treating notes do is a bet on impatience, not a valuation.

### Build the damages in dated order

Billed charges are the easiest line and the least complete one. Care still recommended, mileage to appointments, prescriptions, braces and devices bought out of pocket, whole and partial days of lost pay, shifts other people covered, and the household tasks now done differently all belong on the list. Put them in date order rather than as a total, because a timeline can be checked against records and a round number cannot. Adjusters give weight to what they can verify.

### The lever is a bar, not a fraction

In most states the argument is about percentages. Here the other side is reaching for something stronger, since a recovery can be defeated when the injured person's own negligence joined with the defendant's in causing the harm. That is why an adjuster will press for an admission about speed, a glance at a phone, or a sudden stop. Two things push back. The party asserting contributory negligence carries the burden of proving it under G.S. 1-139, and the last clear chance doctrine can excuse the injured person's negligence where the other driver knew of an inescapable peril and had both the time and the means to avoid the collision.

### Insurance points explain some of the resistance

The Safe Driver Incentive Plan gives the at-fault driver a financial reason to dispute what happened. Under G.S. 58-36-75 an at-fault crash counts as major when it causes injury or death, or property damage of $3,850 or more, as intermediate above $2,300, and as minor at $2,300 or less. Recent changes sharpened the consequences. A conviction carrying four or more insurance points is now surcharged for five years instead of three, the lookback periods for a prayer for judgment continued and for speeding 10 mph or less moved from three years to five, and the inexperienced operator surcharge stretches to eight years for drivers first licensed on or after July 1, 2025.

### The release, and the consent your own carrier needs

The signature is where good claims are lost. Send your underinsured carrier written notice before settling with the driver who caused the crash. Once it has that notice, it loses its right to approve the settlement and its subrogation right unless it advances a payment matching the tentative settlement within 30 days. Read what the paper covers as well. Property damage, bodily injury, loss of use, future care, and claims belonging to other insureds are separate items and do not have to be released together.

### What comes off the top before anyone sees a check

A treating provider asserting a claim against the recovery is limited by G.S. 44-50 to half of the damages recovered, figured apart from attorneys' fees. On a modest settlement with a long course of treatment, that ceiling is often the only reason money reaches the injured person at all. Where workers' compensation paid, uninsured and underinsured coverage insures the part of the loss it left uncompensated plus the employer's lien amount, and a fee on the compensation side needs Industrial Commission approval under G.S. 97-90. Ask early who negotiates each of those reductions, because that work moves the final figure more than a percentage does.

### If it does not resolve here

Cabarrus County sits in Superior Court District 25 and District Court District 25, with the courthouse on Union Street South in the city. Filing is a public cost, not a fee: $200 in superior court, $150 in district court, $96 for a magistrate small claims filing, and $30 for every item of civil process the sheriff serves. Two deadlines govern whether that door is still open, three years for injury and two years for a death claim, and negotiation pauses neither. On the fee itself, no percentage is set by statute. Rule 1.5(a) prohibits a clearly excessive fee and measures it against eight factors, and 1.5(c) requires a signed writing stating the method, the percentages at settlement, trial and appeal, and whether expenses are deducted before or after the share is computed.
"""

txt = txt.rstrip() + "\n" + NEW.rstrip() + "\n"
copy.write_text(txt)

sj = SITE / "site.json"
s = sj.read_text()
assert '"phase": 1' in s
sj.write_text(s.replace('"phase": 1', '"phase": 2', 1))

# report word counts of constrained blocks
import collections
blocks = {}
cur = None
for line in txt.splitlines():
    if line.startswith("## "):
        cur = line[3:].strip(); blocks[cur] = []
    elif cur:
        blocks[cur].append(line)
for k in ["symptom_1","symptom_2","symptom_3","symptom_4","services_summary","services_pick_head","crosslink_head"] + [f"svc_{n}_{p}" for n in ["rear_end_collision_lawyer","uninsured_driver_claim_lawyer","commercial_truck_collision_lawyer","injury_claim_negotiation"] for p in ["lede","body"]]:
    print(k, len(" ".join(blocks[k]).split()))
