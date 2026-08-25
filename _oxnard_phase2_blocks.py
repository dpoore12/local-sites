import re, json, pathlib

SITE = pathlib.Path("/home/user/workspace/local-sites/sites/oxnardcaraccidentlawyerpros.com")
copy = (SITE / "copy.md").read_text()

sym = {
1: """A rear impact can feel survivable at the roadside and hurt badly by dinner. Get seen, then protect the sequence: photograph both bumpers, the lane, and whatever had stopped or slowed the traffic ahead of you. Note the agency that wrote the report and its number. If a trailer, tractor, or orange triangle was involved, write that down first.""",
2: """Oxnard recorded 119 hit-and-run collisions with a fatality or injury in 2023. When the other vehicle is gone, the file begins with what only you saw: direction of flight, body style, lettering, a ladder rack, a partial plate. Report it the same day. Then chase video, because packing house, apartment, and fuel canopy cameras overwrite themselves within days.""",
3: """An expired card, a borrowed pickup, or a crew van registered to a labor contractor all point the same way: coverage is a paperwork question, never a roadside one. Photograph the plate, the registration tab, any company lettering, and any inspection sticker inside the windshield. Then find your own declarations page before accepting the news that nothing responds.""",
4: """A first offer prices whatever thin file the adjuster is holding, usually one emergency bill and a repair estimate. Before endorsing a check, list the care still recommended, the shifts already gone, and whether a work assignment put you in that vehicle. Signing can close a second coverage path and a reimbursement question in one stroke.""",
}

for n, text in sym.items():
    pat = re.compile(r"(## symptom_%d\n\n)(.*?)(?=\n## )" % n, re.S)
    assert pat.search(copy), n
    copy = pat.sub(lambda m: m.group(1) + text.strip() + "\n\n", copy)

NEW = r"""
## services_summary

Four jobs hide behind one phrase in this city, and they run on different clocks. A rear-end file is decided by sequence and by whatever had slowed traffic ahead. An uninsured or hit-and-run file is decided by policy language and by same-day reporting. A farm freight or crew transport file is decided by certificates, inspection dates, and who owned the vehicle. A negotiation file is decided by documents and by whether the trip was work. Send the wrong question down the wrong path and the loss is concrete: a camera cycles, a six-month notice period closes, or a signature ends coverage nobody had found yet.

## services_pick_head

Begin with the part of the crash that is stuck

## crosslink_head

Facing a different crash question?

## svc_rear_end_collision_lawyer_lede

Rear impacts on the Oxnard plain are produced by things that halt or crawl: a signal cycle on Rose Avenue, a queue backed up from the Rice Avenue tracks, a loaded implement moving at fifteen miles an hour. What slowed traffic is the first fact to record.

## svc_rear_end_collision_lawyer_body

### Read the damage before the car goes anywhere

Crush at the back and crush at the front puts you in the middle of a chain, and the middle vehicle is the one both other drivers will describe worst. Look past the bumper cover, which can hide a folded absorber behind a shallow scuff. Check whether a seat back moved, whether a head restraint is now at a different height, and whether the trunk still shuts. Photograph the odometer and the dashboard warning lights too. Once a tow yard has the vehicle, none of that is available to anyone.

### What was ahead of you, and how slowly it was moving

Farm equipment shares these roads legally, under equipment rules most drivers have never read. A vehicle designed and operated at 25 miles an hour or less must show a slow-moving vehicle emblem on its rearmost unit: a truncated triangle at least 14 inches high, red reflective border no thinner than 1 3/4 inches, orange center, mounted base down three to five feet off the ground. Implements of husbandry sit outside much of the lighting chapter, yet they remain subject to that emblem and to [Vehicle Code section 25803](https://codes.findlaw.com/ca/vehicle-code/veh-sect-25803/), which after dark wants a red light visible 500 feet behind and reflectors mounted between 16 and 60 inches high. Loads wider than 120 inches call for flashing amber warning lamps, amber turn signals, or 16-inch red daylight flags at the outer edges. So the useful question is not only how fast you were going. It is whether the thing you struck was marked and lit the way the code requires.

### Where the queues form here

The city's own safety work names the places. Five hot spot corridors were chosen for grant development in the Local Road Safety Plan, among them Ventura Road from Fifth Street to Wooley Road and Saviers Road from Laurel Street to Pleasant Valley Road. Ten collision profiles sit alongside them, including unsafe speed on four and five lane roadways and broadside crashes at signals lacking fully protected left turns. The companion travel plan puts most injury collisions between 2016 and 2020 on Oxnard Boulevard, Rose Avenue, C Street, Victoria Avenue, Gonzales Road, and Channel Islands Boulevard. Highway 101 adds its own stopping points through the same ground, since the state's corridor plan treats the ramp and weaving areas near Victoria, Vineyard, Rose, and Rice as the pressure points.

### Which clock runs out first

Two years is the outside limit for an injury action under [Code of Civil Procedure section 335.1](https://law.justia.com/codes/california/code-ccp/part-2/title-2/chapter-3/section-335-1/), and almost nobody loses a rear-end case on that one. The dangerous deadline appears when a public body is anywhere in the story: a signal that stayed green too long, faded striping, a pavement edge, a city or district vehicle. Government Code section 911.2 then requires the claim to be presented within six months after the cause of action accrues, with one year for most other kinds of loss. Six months disappears while people wait for records.

### The first week, in order

Photograph everything before repair. Identify which agency took the report, because a collision on the freeway or in unincorporated ground near the fields usually belongs to the Highway Patrol while a city street collision usually does not. Ask for treatment that matches the symptoms rather than the paperwork. Then go after video quickly, since the cameras that cover these corridors belong to businesses and households, not to an archive. Keep the tow receipt, the storage invoice, and the rental agreement together, because those documents fix dates that memory will blur.

### The theory the other side will build

Expect a percentage argument rather than a denial. California reduces damages by the injured person's own share of responsibility instead of barring the claim, which gives an adjuster every reason to hunt for a fraction: your following distance in the chain, a brake lamp, a lane change nobody saw, a stop made harder than it needed to be. Low visible damage gets offered as proof that no one could be hurt. Answering "I did not measure that" is accurate and safe; guessing at speeds and seconds hands over a fact that gets read back later.

### What follows contact, and how a fee is fixed

Early work is clerical rather than dramatic: the report, the photographs, both declarations pages, a treatment chronology, and preservation requests aimed at whatever video still exists. Fees follow state rules instead of a schedule. Rule of Professional Conduct 1.5(a) forbids an unconscionable or illegal fee, and Business and Professions Code 6147 requires an injury agreement to be written, signed by both sides, handed over as a duplicate copy, and to say plainly that the rate is not fixed by law and can be negotiated. Court charges belong in a separate column, since they go to the county and the state regardless.

## svc_uninsured_driver_claim_lawyer_lede

Nobody argues about fault in these files. The argument is whether a policy exists, whose name sits on it, and whether the vehicle carrying you was ever certified and insured to carry anyone at all.

## svc_uninsured_driver_claim_lawyer_body

### The three shapes this takes on the Oxnard plain

One driver hands over nothing and admits there is no policy. A second produces a card whose carrier later says coverage had lapsed. A third has real insurance at the statutory floor, which the hospital passes in a week. A fourth version is common in an agricultural city and often missed: the vehicle was somebody's work vehicle, and the person who owns it, the person who dispatched it, and the person driving it are three different names on three different documents.

### The floor moved, and it still runs out

For policies issued or renewed on or after January 1, 2025, California's minimum liability limits are $30,000 for injury to one person, $60,000 for two or more, and $15,000 for property damage. Those figures replaced numbers set in 1967 and are scheduled to rise again to $50,000, $100,000, and $25,000 on January 1, 2035. The alternative cash deposit with the Department of Motor Vehicles moved to $75,000. Uninsured motorist coverage must be offered at matching bodily injury limits, though the insurer need not offer more than $30,000 and $60,000. Read a limit as a ceiling on one policy, not as a measure of what a broken wrist and eight lost weeks actually cost.

### The provision that can delete half the claim

[Civil Code section 3333.4](https://codes.findlaw.com/ca/civil-code/civ-sect-3333-4/), passed by voters as Proposition 213, blocks recovery of noneconomic loss in a motor vehicle case in three situations. It reaches an injured person convicted of drunk or drugged driving in that crash, an injured person who owned an uninsured vehicle involved in the crash, and an injured operator who cannot establish financial responsibility. Insurers are separately barred from indemnifying those noneconomic losses. One exception survives: an uninsured owner hurt by a driver who was convicted of drunk driving in the same collision keeps that category. Medical charges, wage loss, and other economic items are untouched in every version. Note who the section does not describe. A passenger who owns no vehicle involved in the crash, including a worker riding in an employer's van, is outside its three categories.

### When the vehicle was a crew vehicle

State law calls a motor vehicle designed, used, or maintained to carry nine or more farm workers plus the driver a farm labor vehicle, and it cannot lawfully be driven without a current inspection certificate displayed inside. The Highway Patrol inspects each one at least annually, and the certificate must show an inspection within 13 months of the day it is being driven. Responsibility for that inspection rests with the owner and with any farm labor contractor who rents or otherwise uses the vehicle to move people. That single rule opens doors a roadside conversation closes, because a vehicle with an expired sticker has an owner, a contractor, a grower on the far end of the trip, and usually commercial paper behind all three.

### What has to be recorded in the first day

The city logged 119 hit-and-run collisions involving a fatality or injury in 2023, so a vanished driver is not an unusual event here. Write the direction of travel, the color and body style, any lettering or logo, a plate fragment, and any distinguishing damage. Report the crash promptly to the agency with jurisdiction, since coverage for an unidentified driver turns partly on a timely report. Then photograph anything bolted to the other vehicle: registration tab, inspection sticker, company name, unit number, and the visible identification number.

### The mistake that quietly closes a second door

Endorsing a modest payment from one carrier before every policy has been identified is how good claims shrink. Auto policies routinely condition benefits on notice and on the insurer's written agreement before you release anybody who might be liable. That means the order of operations matters more than speed. Identify each policy, put the notice in writing, ask for consent in writing, and only then decide what to do with the money on the table.

### What happens after contact, and how fees are governed

The file opens with documents rather than a retelling: both declarations pages, the policy's uninsured and underinsured provisions, the report and the agency that took it, registration and ownership records for every vehicle, and a treatment chronology. Fee terms follow the same state rules that govern any injury representation here. Rule 1.5(a) of the California Rules of Professional Conduct bars an unconscionable or illegal fee, and Business and Professions Code 6147 makes the written agreement carry the weight, including a statement that the percentage is negotiable. Arbitration or filing charges sit on their own line, separate from any percentage.

## svc_commercial_truck_collision_lawyer_lede

Farm freight and worker transport dominate the heavy vehicle files in this county. The opening question is rarely how large the vehicle was. It is which rulebook it was operating under, and whether its own paperwork was current that morning.

## svc_commercial_truck_collision_lawyer_body

### Photograph the paperwork, not only the damage

A federal carrier number on a door, a company name on the tractor that differs from the name on the trailer, a lease decal, a bin trailer riding low with produce: each changes who answers for the crash. Inside a crew vehicle there is more to find. A certified farm labor vehicle carries an inspection approval certificate posted in the passenger area, serialized stickers on the front and rear showing the certification date, and a notice sticker at eye height with the Highway Patrol's reporting hotline. Photographs of those three items, taken the same day, are worth more than any later description of them.

### What certification actually requires

The category is defined by capacity. A vehicle designed, used, or maintained to transport nine or more farm workers in addition to the driver falls inside it, and the Highway Patrol will not certify one without approved seat belts installed. Every passenger position needs a lap or three-point assembly built and anchored to the federal standards, and seating positions themselves must meet the federal seat standard. Cutting tools ride in latched containers fixed to the vehicle, nothing may block an aisle or an emergency exit, and both headlamps stay lit regardless of the hour. Renewal is not casual either. An operator must request the annual inspection no later than four weeks before the current certificate expires, and three business days ahead for a first inspection.

### Who answers when the certificate is missing

Penalties here are written in dollars, which tells you how the Legislature viewed the risk. Driving a farm labor vehicle after notice that it is unsafe, while it presents an immediate safety hazard, is a misdemeanor carrying a fine of no less than $1,000 and no more than $5,000, up to six months in county jail, and no part of the fine may be suspended. Knowingly allowing operation in violation adds a fine of at least $1,000 per violation plus $500 for each passenger aboard, to a $5,000 ceiling. Officers may impound the vehicle. None of that pays an injured passenger, but every one of those findings identifies a defendant with records.

### The driver's own credential

A person may not operate one of these vehicles without a license of the appropriate class endorsed for passenger transportation and, when farmworker passengers are aboard, a certificate issued by the Department of Motor Vehicles. Getting that certificate requires completing a state-approved driver training course and passing examinations administered by the Highway Patrol, with a $12 fee. Commercial licensing rules add that the operator needs a Class A or Class B commercial license. Whether the driver held all of it is a records question answered in weeks, not a judgment made at the scene.

### One local crossing, documented in unusual detail

At 5:42 in the morning on February 24, 2015, a southbound Metrolink train carrying 48 passengers struck a pickup and utility trailer that had been turned onto the Union Pacific tracks at Rice Avenue, 68 feet short of Fifth Street. The truck belonged to an agricultural management company based in Arizona, and federal investigators recorded that the driver had been on duty and driving nearly 24 consecutive hours. Impact speed was 57 miles an hour. Twenty-six passengers and all three crew members were hurt, and the locomotive engineer died a week later. Equipment damage was put at $14 million. The [federal accident report](https://railroads.dot.gov/sites/fra.dot.gov/files/fra_net/16960/HQ-2015-1016%20Final_Oxnard,%20CA.pdf) found the warning system worked as designed, with 28 seconds of warning time. Hours of service, dispatch pressure, and a road that hands a tired driver two nearly parallel choices are the parts a civil file examines. The city broke ground in March 2025 on a six-lane Rice Avenue bridge over that crossing and the Fifth Street intersection, on a crossing state rail regulators had ranked fourth in California for needed safety work.

### Why a state safety citation is not your case

Workplace regulators and civil courts ask different questions. California's agricultural safety orders permit no riders on farm equipment except people needed for instruction or assistance, with one narrow exception for tractor-mounted carriers used in irrigation work, capped at five miles an hour and forbidden within 10 feet of a paved public road. An employer must report a serious injury or death to the state division immediately, and a violation of that reporting duty draws a civil penalty of at least $5,000. A citation, though, resolves a regulatory question about an employer. It does not decide who owes an injured passenger money, and an uncited employer is not thereby cleared.

### What early work looks like, and how the money is arranged

Preservation comes before storytelling: a letter identifying the tractor, trailer, date, and driver, and asking that logs, dispatch records, driver qualification files, maintenance records, inspection reports, and any onboard video be held. Vehicle inspection happens before repair or release. Those steps are costs, paid to third parties, and they behave differently from a fee. On fees, no California statute sets a percentage for a vehicle case. The professional conduct rule bars an unconscionable or illegal fee, and the contract statute makes the written agreement disclose the rate, explain how costs bear on the recovery, and state that the rate is negotiable.

## svc_injury_claim_negotiation_lede

An offer is a number a stranger assembled from a thin file. What moves it is documents rather than argument, and the first document question in an agricultural county is often whether the trip you were on was work.

## svc_injury_claim_negotiation_body

### Which system owns the claim before anyone talks money

Two paths exist and they pay for different things. Workers' compensation covers a work injury without regard to fault and stands in place of other liability against the employer. A civil claim reaches everyone else, and Labor Code section 3852 says plainly that a compensation claim does not affect the right of action for all damages against any person other than the employer. Which path opens usually turns on the commute. Under the going and coming rule an ordinary daily trip to a fixed workplace sits outside compensation, and that rule was never written by the Legislature.

### The transport exception that decides farm cases

In 1972 the California Supreme Court took up a farm laborer who worked seven or eight scattered ranches for one operator, owned no car, and paid a coworker three dollars a week to ride. He was hurt heading home; two coworkers in the same car died. The court held the rule "composes no formula of automatic application" and covered the injury, because the job was built around travel between fields and the car was an essential requirement of it. The opinion in [Hinojosa](https://law.justia.com/cases/california/supreme-court/3d/8/150.html) also collects the triggers that pull a trip back inside employment: the employer provides the transportation, pays substantially for travel time, controls the route, sends the worker on a special errand, or expressly or impliedly requires the worker to furnish the ride. Read that list against a crew van, a labor contractor's pickup, or a carpool a foreman arranged, and the answer stops being obvious.

### Passenger in employer transport, or struck by it

The distinction changes the whole file. A worker riding in employer-arranged transport may be inside the compensation system for benefits and still hold a civil claim against a third party, such as the driver of the other vehicle, the vehicle's owner if it is not the employer, or a contractor who supplied an uncertified vehicle. A member of the public struck by a crew vehicle or a produce truck has no compensation route at all and an ordinary negligence claim against the driver and whoever employed him. Both files can involve the same crash and the same intersection, and they will not settle on the same terms.

### A citation is a regulatory answer, not a verdict

After a work-related crash a state inspection may follow, and its output is not evidence of who owes what. The employer must report a serious injury or death to the state division immediately, and failing that duty carries a civil penalty of at least $5,000. Any citation that follows measures compliance with safety orders. It does not fix damages, does not name your compensable losses, and its absence does not mean the conduct was reasonable. Treat the file it generates as a source of documents and witness names rather than as a decision.

### What the damages list must contain

Bills already generated are the easiest item and the least complete one. Add treatment still recommended, mileage to appointments, prescriptions, braces and devices bought out of pocket, whole and partial shifts lost, work somebody else covered, and specific household tasks now done differently. Where compensation benefits have been paid, the employer or carrier has a reimbursement interest in a third-party recovery, so those numbers belong in the file from the start rather than as a surprise at the end. Keep it as a dated chronology. A chronology can be checked against records; a round total cannot, and an adjuster gives nothing to a figure that cannot be checked.

### Read the release the way the carrier wrote it

Property damage, injury, loss of use, future treatment, and other people insured under the same policy are separate items that do not have to travel together. A policy commonly requires notice and the insurer's written agreement before you release a party who might be liable, so a quick check from one carrier can foreclose a claim on another. Ask for consent in writing, keep the original of everything, and diary the response date.

### Where a Ventura County case lives, and how a fee is set

Filing is not the first step in most claims, but it shapes how the paperwork should look. General civil matters for this county are filed and heard at the Hall of Justice on South Victoria Avenue in Ventura, where records sit in Room 218 and attorney filings in limited and unlimited civil cases go through electronic filing. The juvenile courthouse on Vineyard Avenue in Oxnard is not the venue for a crash case. Trauma care travels too, since the county's designated Level II trauma centers are in Ventura and Thousand Oaks rather than in this city, so records for one patient often sit in three institutions. Fees follow the state rules described on the pricing page: no percentage ceiling for a traffic claim, a professional conduct rule against an unconscionable or illegal fee, and a contract statute that voids an agreement missing a required term.
"""

copy = copy.rstrip("\n") + "\n" + NEW.rstrip("\n") + "\n"
(SITE / "copy.md").write_text(copy)

sj = (SITE / "site.json").read_text()
sj2 = sj.replace('"phase": 1,', '"phase": 2,', 1)
assert sj2 != sj
(SITE / "site.json").write_text(sj2)
print("done")
