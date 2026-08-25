import re, io, os

P = os.path.join(os.path.dirname(__file__), "copy.md")
src = open(P, encoding="utf-8").read()

NEW = {}

NEW["symptom_1"] = """A dog clears a low fence in Highland Park, slips its collar outside a Koreatown market, or reaches the sidewalk through a gate nobody latched. Treat the wound first. Then write down the street address and unit, the dog's description, and the name of whoever was holding the lead, because the City measures restraint in feet and the address decides which agency opens a file."""

NEW["symptom_2"] = """Most children here are bitten by a dog they already knew, in a relative's yard or a courtyard they walk through every day. Care comes before any account of the afternoon. Ask the treating clinic which agency it notified, photograph the wound in the same light each day, and note which adults were present and why the child was at that address."""

NEW["symptom_3"] = """The dog belonged to a tenant, but the encounter happened on a shared stairway, at a gate, or in a courtyard the building owner maintains. Two separate questions follow and they run on different paper. Before the latch gets repaired or anyone moves out, photograph the enclosure and save every message to the manager with its date and recipient visible."""

NEW["symptom_4"] = """A letter or a call arrives while the stitches are still in, asking for a recorded statement, a signature, or open access to your file. Nothing has to be signed that week. Keep the claim number, the adjuster's name and every enclosure, and ask for the complete policy form instead of the fragment a letter quotes."""

# ---------------------------------------------------------------- new blocks

NEW["services_summary"] = """Four different jobs hide behind the words dog bite lawyer in Los Angeles. An adult injury claim runs on the state bite statute and the City's six-foot restraint ordinance. A child's claim adds a tolling rule and treatment nobody can price for years. A rental claim is a property negligence question the bite statute does not answer at all. An insurance claim is a contest over policy wording and dated agency records. Running them together costs money in a city where only 36 percent of housing units are owner occupied, because most bites here involve somebody else's building, somebody else's gate and somebody else's policy."""

NEW["services_pick_head"] = """Begin with the claim your facts actually create"""

NEW["crosslink_head"] = """Facing a different bite question?"""

# ---- service 1

NEW["svc_dog_bite_injury_claim_lede"] = """A bite on a Los Angeles sidewalk generates three separate records inside ten days: a Public Health file, an animal control file and a medical chart. The state statute is the straightforward part. Proving where you were standing is not."""

NEW["svc_dog_bite_injury_claim_body"] = """### The statute does not ask what the dog did last year

[Civil Code section 3342](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=3342.&lawCode=CIV) makes the owner of any dog liable for damages suffered by a person bitten in a public place or lawfully in a private place, the owner's own property included, and it says this applies regardless of the former viciousness of the dog or the owner's knowledge of it. Nobody has to dig up an earlier bite. The same subdivision defines lawful presence on the owner's land: being there to perform a duty imposed by the laws of this state or by federal postal regulation, or being there on the owner's invitation, express or implied. Once ownership and a bite are settled, the argument narrows to where you stood and why.

### The City ordinance gives you a second theory

[Municipal Code section 53.06.2](https://codelibrary.amlegal.com/codes/los_angeles/latest/lamc/0-0-0-136443) keeps a dog on its keeper's premises and lets it leave only under the control of a competent person, restrained by a substantial chain or leash not exceeding six feet, or inside a dog exercise or training area established under section 63.44. [Evidence Code section 669](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=669.&lawCode=EVID) then presumes that a person failed to exercise due care where an ordinance was violated, the violation proximately caused the injury, the injury was of the kind the ordinance was written to prevent, and the injured person belonged to the class it protects. The presumption can be rebutted by proof that the person did what an ordinarily prudent person wanting to comply would have done, so the physical details matter: photograph the lead, measure it if you safely can, and record whether any posted exercise area covered that ground.

### The same afternoon can also be a misdemeanor

Under [section 53.34](https://codelibrary.amlegal.com/codes/los_angeles/latest/lamc/0-0-0-137068), a person who owns, controls, possesses or is in charge of a dog and permits it to be at large on a public street, sidewalk, park or other public property, or on someone else's private property, is guilty of a misdemeanor if the animal bites, attacks or injures a human being or another animal. A conviction bars that person from owning the same species for three years and directs the Department not to issue or renew a license for it. Ask early whether a citation or a filing exists. It is dated, official, and written by somebody other than the dog's owner.

### If the dog was working for a public agency

Subdivision (b) of section 3342 withdraws the statutory action against a governmental agency using a dog in military or police work where the bite happened while the dog defended itself from an annoying, harassing or provoking act, or assisted an employee in the apprehension or holding of a suspect on reasonable suspicion, the investigation of a crime or possible crime, the execution of a warrant, or the defense of a peace officer or another person. Subdivision (c) removes that shelter where the person bitten was not a party to, a participant in, or suspected of the conduct that prompted the dog's use. Subdivision (d) allows the shelter only where the agency has adopted a written policy on necessary and appropriate use. Where any public body sits in the facts, [Government Code section 911.2](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=911.2.&lawCode=GOV) requires a written claim no later than six months after the cause of action accrues, and [section 945.6](https://california.public.law/codes/ca_gov't_code_section_945.6) allows six months from the day a written rejection is delivered or mailed to get a suit on file.

### The first ten days belong to Public Health

County Veterinary Public Health puts the quarantine for a biting dog or cat at a minimum of ten days, holds biting livestock for thirty, and says the vast majority of quarantines are served in the animal's own home, while an animal impounded by an animal control agency finishes confinement in a shelter ([Reporting Animal Bites](http://publichealth.lacounty.gov/vet/biteintro.htm)). The County rabies manual describes the alternative: strict confinement under a licensed veterinarian, with release possible after five days where the veterinarian examines the animal on the fifth day or later and certifies no clinical signs ([quarantine guidance](http://publichealth.lacounty.gov/vet/rabiesmanual/quarantines.htm)). Public Health also states that a bite report does not mean the animal has been deemed dangerous, and that anyone who believes it is dangerous has to file a separate report with the local animal control agency. Pasadena, Long Beach and Vernon take their own reports.

### Two years, and the week that decides whether you keep them

[Code of Civil Procedure section 335.1](https://law.justia.com/codes/california/code-ccp/part-2/title-2/chapter-3/section-335-1/) allows two years for an action for injury to an individual caused by the wrongful act or neglect of another. That looks generous next to the six-month government claim rule, which is exactly why the public-entity question has to be answered in the first weeks rather than the twentieth month. Ordinary evidence ages on its own schedule anyway. Lobby and doorbell footage gets overwritten, torn clothing goes in the bin, and a puncture over a knuckle that looked shallow on Sunday can declare itself as an infection by Wednesday.

### What the first contact looks like, and how the money side is written

The productive first exchange is an inventory rather than a story: date, address and unit, the animal and its owner, the report number, treatment so far, and whether any agency touched the facts. On the fee side, California attaches no percentage to a claim against a dog's owner. [Business and Professions Code section 6147](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=6147.&lawCode=BPC) requires the contract to be written and signed by both people, with a duplicate handed over at signing, and to spell out the agreed rate, the way disbursements and costs will affect both the fee and what reaches the client, and, in plain words, that no law sets that rate and it is open to negotiation. A contract missing any of it is voidable at the client's option."""

# ---- service 2

NEW["svc_child_dog_bite_claim_lede"] = """A child's bite claim is not a smaller version of an adult's. The clock is different, the defense is different, and the injury is not finished being an injury for months or years after the wound closes."""

NEW["svc_child_dog_bite_claim_body"] = """### One bite, two claims, two clocks

[Code of Civil Procedure section 352](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=352.&lawCode=CCP) provides that where the person entitled to bring an action was under the age of majority when the cause of action accrued, the time of that disability is not part of the time limited for starting it. The child's own injury claim therefore has room to run past the eighteenth birthday. What a parent spent does not get the same treatment, and evidence keeps aging regardless. Subdivision (b) is the part families are never told: the tolling rule does not apply to an action against a public entity or public employee where a claim has to be presented under the Government Code. A bite at a public facility puts the family back on the six-month schedule in [Government Code section 911.2](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=911.2.&lawCode=GOV) no matter how young the child is.

### The provocation argument, and what the law expects of a child

Someone will suggest the child started it. [Evidence Code section 669](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=669.&lawCode=EVID) measures a child's conduct against the care ordinarily exercised by people of that maturity, intelligence and capacity, and it closes off even that argument where the violation occurred during an activity normally engaged in only by adults. Provocation shows up on the City's side of the file too. When the Department weighs whether to declare an animal dangerous, the presence or absence of provocation is one of the eleven categories of evidence it considers, alongside the place where the injury happened and the number of victims involved ([section 53.34.4](https://codelibrary.amlegal.com/codes/los_angeles/latest/lamc/0-0-0-137100)). Whatever a child says in week one tends to become the version everyone works from afterward, so take the account down once, carefully, and stop asking for it.

### Where children in this city meet dogs

Los Angeles is a renter's city built mostly before the current rules. Census figures put the owner-occupied share of housing units at 36.0 percent for 2020 through 2024 ([QuickFacts](https://www.census.gov/quickfacts/fact/table/losangelescitycalifornia/HSG445221)), and the Housing Department counts roughly 624,000 units across about 118,000 properties under the Rent Stabilization Ordinance, which generally reaches buildings first built on or before October 1, 1978 ([RSO coverage](https://housing.lacity.gov/residents/what-is-covered-under-the-rso)). In practice that means courtyard apartments, duplexes and bungalow courts in Echo Park, West Adams, Highland Park and Boyle Heights, and in Koreatown a residential density the Times measured at 42,611 people per square mile ([Mapping L.A.](https://maps.latimes.com/neighborhoods/neighborhood/koreatown/)). Children in buildings like those meet dogs on interior stairs, in laundry corridors and at gates rather than in fenced back yards. Photograph the route the child took and the sight lines from where the adults were standing.

### The dog may be quarantined down the hall

County Veterinary Public Health says most quarantines are performed in the biting animal's home and that dogs and cats are held for a minimum of ten days ([Reporting Animal Bites](http://publichealth.lacounty.gov/vet/biteintro.htm)). In a shared building that means the animal spends a week and a half behind a door on the same landing. Ask the agency in writing where confinement is being served and on what conditions, keep the answer, and route anything further through the agency rather than through the hallway.

### What the pediatric record has to contain

The provider's own words on body area, depth, repair method and any note about nerve, tendon or infection concern. Referrals for scar management, surgical revision or counseling. Dated photographs taken in consistent light as the swelling drops. The hours, mileage and missed school days that appointments consume. Ask the treating clinic which agency it notified, because reporting duties reach beyond the family, and get the report number in writing.

### The mistake that quietly shrinks a child's claim

Finishing it while the child is still growing. Revision work on a face or a hand is often deferred until growth allows it, so a figure discussed in week three is a figure set before anyone knows what the injury is. The second mistake is public. A post carrying photographs and a narrative becomes material the other side is entitled to read, and a child asked to retell the event weekly ends up remembering the retelling.

### The hearing that puts the dog on the record

If Animal Services sets a hearing, the machinery is worth knowing, because it produces sworn and transcribed material about the animal. Notice must be served at least ten days ahead and state the reason for the hearing and the remedy or penalty sought. A Hearing Examiner appointed by the General Manager presides, a recording or transcript is taken, the Department carries the burden by a preponderance, and hearsay may supplement direct evidence but cannot on its own support a finding ([hearing ordinance text](https://www.laanimalservices.com/sites/default/files/documents/PERMITS/LAMC53.18.5.pdf)). That is a public-safety proceeding about the dog's future, not a decision about a child's damages. On fees, [Business and Professions Code section 6147](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=6147.&lawCode=BPC) requires a written contract signed by both sides, a duplicate handed over at signing, the agreed rate on the page, a statement of how costs affect both the fee and the recovery, and language saying no law sets the rate."""

# ---- service 3

NEW["svc_landlord_dog_bite_liability_lede"] = """A bite in the courtyard of a Los Angeles apartment building produces two claims, not one. The bite statute reaches the dog's owner. Reaching the building owner is an entirely separate proof about knowledge, authority and the condition of the property."""

NEW["svc_landlord_dog_bite_liability_body"] = """### The deed and the lead are separate documents

[Civil Code section 3342](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=3342.&lawCode=CIV) fixes liability on the owner of the dog. It says nothing about whoever owns the walls around the dog. A claim aimed at a building owner, an ownership entity or a management company is ordinary negligence, and its statutory root is [Civil Code section 1714](https://law.justia.com/codes/california/code-civ/division-3/part-3/section-1714/), which makes everyone answerable for an injury occasioned to another by want of ordinary care or skill in the management of that person's property. So the questions change shape. What did the property side actually know about this particular animal before the bite, what authority did it hold over the animal or the space, and what condition of the building let the encounter happen at all.

### This is a rental city, and mostly an old one

Only 36.0 percent of Los Angeles housing units were owner occupied over 2020 through 2024 ([QuickFacts](https://www.census.gov/quickfacts/fact/table/losangelescitycalifornia/HSG445221)). The Housing Department reports approximately 624,000 units in about 118,000 properties covered by the Rent Stabilization Ordinance, which generally applies where the property was first built on or before October 1, 1978 ([RSO coverage](https://housing.lacity.gov/residents/what-is-covered-under-the-rso)). Pre-1978 stock is why so many bites here happen in space the tenant does not control: interior stairwells and light wells in Koreatown, whose density the Times put at 42,611 people per square mile ([Mapping L.A.](https://maps.latimes.com/neighborhoods/neighborhood/koreatown/)), bungalow courts and side driveways in West Adams and Highland Park, shared front steps on the older lots of Boyle Heights, and the public stairways and retaining walls that hillside parcels in Echo Park and Silver Lake attach to the building rather than to any one unit.

### When a manager becomes the person in charge

The City ordinances are not written around registered ownership. Section 53.06.2 speaks to every person owning or having charge, care, custody or control of a dog, and [section 53.34](https://codelibrary.amlegal.com/codes/los_angeles/latest/lamc/0-0-0-137068) reaches a person who owns or is in charge of or controls or possesses one. A resident manager who walked the animal, held it during a unit showing, or moved it between units can fall inside that language even though the bite statute never names him. Write down who physically had the animal, on what day, and at whose instruction.

### The City hearing writes things down about the property

The dangerous animal procedure is the strongest paper a property claim can borrow. Under [section 53.34.4](https://codelibrary.amlegal.com/codes/los_angeles/latest/lamc/0-0-0-137100), the Department may declare a dog dangerous after a hearing whenever it has bitten, attacked or caused injury, and the evidence it weighs includes the place where the injury occurred, the manner in which the animal had been maintained by its owner or custodian, and whether public safety can be protected in future if the animal stays in the City. The remedies are physical and property-shaped. A license can be issued or reissued on conditions selecting locations on the property where the dog may not be kept, setting the size, construction or design of an enclosure, requiring removal of one or more dogs from the premises, or requiring restraint, muzzling, identification or sterilization ([hearing ordinance text](https://www.laanimalservices.com/sites/default/files/documents/PERMITS/LAMC53.18.5.pdf)). The Department has run these hearings under ordinances adopted in July 1987 ([Administrative Hearing Guide](https://www.laanimalservices.com/administrative-hearing-guide)). A finding there is an animal control decision, not a damages decision, but it is dated, on the record, and frequently describes the gate, the yard or the enclosure that a landlord will later say was fine.

### The wrong agency wastes weeks

All six neighborhoods named on this site sit inside City of Los Angeles limits, so the Municipal Code track above is the one that applies. The County chapter is different machinery: outside the City, the Director may petition the Superior Court or serve a petition for an administrative hearing, and the hearing is held promptly between five and ten working days after service, before a neutral hearing officer, with no jury ([County Code 10.37.110](http://lacounty-ca.elaws.us/code/coor_title10_div1_ch10.37_sec10.37.110)). Two adjoining addresses can run on the two systems, so pin the exact address and unit before requesting anything. Where the property or the operator is public, [Government Code section 911.2](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=911.2.&lawCode=GOV) puts a written claim inside six months of accrual and [section 945.6](https://california.public.law/codes/ca_gov't_code_section_945.6) allows six months after a written rejection is mailed or delivered to file suit.

### The paper that leaves when the tenant leaves

Collect the lease and any pet addendum, the community rules, every message to the manager or owner in original form with its date and recipient visible, portal tickets, maintenance requests about the fence or the gate, and any notice served on the tenant. Photograph the latch, the hinge, the gap the animal used, the posted signs and the common area from several distances. In an older courtyard building the repair is often the first thing done after the ambulance pulls away, and a complaint written by neighbors after the attack proves nothing about the week before it.

### What the other side leads with, and what the contract must say

A property defense usually opens on duty rather than on the wound, arguing that nobody on the ownership side knew anything about this animal and that the bite happened inside space the tenant possessed exclusively. Expect the tenant's own renters coverage to go unmentioned while the building's carrier does the talking. On fees, no California statute fixes a percentage for this work. [Section 6147](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=6147.&lawCode=BPC) instead requires a written contract signed by both people with a duplicate given at signing, the agreed rate stated, an explanation of how costs bear on the fee and on the client's recovery, and a statement that the rate is negotiable rather than set by law."""

# ---- service 4

NEW["svc_dog_bite_insurance_claim_lede"] = """Almost every dog bite payment in this city comes out of a residential liability policy. That makes the policy wording and the dated City and County records the real subject matter, long before anyone discusses a number."""

NEW["svc_dog_bite_insurance_claim_body"] = """### What the adjuster is actually arguing about

Because [Civil Code section 3342](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=3342.&lawCode=CIV) removes the question of the dog's former viciousness and the owner's knowledge of it, a residential liability file rarely turns on whether the animal had a reputation. It turns on four narrower things: who owned the dog, whether the policy answers for that person at that address, whether the person bitten was in a public place or lawfully in a private one, and what the injury is worth once treatment finishes. Work out which of the four a letter is really about before answering it, because a paragraph about coverage and a paragraph about liability call for completely different responses.

### Three dated files the insurer did not write

The first is the Public Health bite record, which fixes the date, the location, the animal and the owner. The second is the animal control file, including anything generated by a hearing. The third is the licensing and rabies record for the dog. None of them was drafted by a party to your claim, which is precisely their value. Ask each agency for its number in writing and keep the request alongside the answer, because a records request with a date on it is itself evidence of when you asked.

### Why the hearing record carries weight

The City's hearing process is built to produce a usable record. A Hearing Examiner appointed by the General Manager presides. Relevant evidence is admitted if it is the sort responsible people rely on in serious affairs, hearsay may supplement direct evidence but cannot alone support a finding, oral evidence is taken only on oath or affirmation, and a recording or transcript of the proceeding is made. The Department carries the burden of showing its allegations true by a preponderance. The Examiner then reports to the General Manager within fifteen days with a summary of the evidence including oral testimony, plus findings and recommendations, and that report is a public record served on the dog's owner. The General Manager's written decision follows within fifteen days of receiving it, becomes final when served, and may be appealed to the Board of Commissioners within fifteen days on a form the Department supplies ([hearing ordinance text](https://www.laanimalservices.com/sites/default/files/documents/PERMITS/LAMC53.18.5.pdf)). Reports of dangerous animals go to the nearest shelter, and officers investigating menacing behavior may impound an animal for observation ([Administrative Hearing Guide](https://www.laanimalservices.com/administrative-hearing-guide)).

### The paperwork attached to the animal

Licensing is not housekeeping trivia. [Municipal Code section 53.15.3](https://codelibrary.amlegal.com/codes/los_angeles/latest/lamc/0-0-0-136780) charges a $91.50 processing fee for a dog license, dropping to $16.50 for a spayed female, a neutered male, or a dog a veterinarian certifies cannot breed. Failing to pay the license tax and fee within forty-five days of acquiring a dog four months or older, of the dog reaching four months, of a license expiring, of a notice being mailed, or of an anti-rabies vaccination expiring is a misdemeanor. A lapsed license or an expired vaccination is therefore a dated public fact about how the animal was kept, and it sits in a file the owner cannot revise after the fact.

### What a bite report does not decide

County Veterinary Public Health is explicit that a report of a bite does not mean the animal has been deemed dangerous, and that a resident who believes an animal is dangerous must file a separate report with the local animal control agency ([Reporting Animal Bites](http://publichealth.lacounty.gov/vet/biteintro.htm)). Expect that sentence to be used in both directions: the existence of a report offered as proof of a vicious animal, or the absence of a dangerous declaration offered as proof of a harmless one. Neither is what the record says. The report establishes an event, a date and an animal, and the quarantine file records where the animal spent the following ten days.

### Read before signing, and send records once

A medical authorization can be drafted broadly enough to open years of unrelated history. A statement recorded in week one becomes the account the file treats as settled. A release can close more than the amount printed on the draft attached to it. Where a letter quotes an exclusion in fragments, ask for the complete form and the endorsement by its number, and ask whether every page of the policy has been produced. Send treatment records when the treatment is documented rather than in installments, because a partial chart invites a valuation built on the emergency room bill alone.

### Two calendars that do not pause while you negotiate

[Code of Civil Procedure section 335.1](https://law.justia.com/codes/california/code-ccp/part-2/title-2/chapter-3/section-335-1/) gives two years for an injury action. If any public agency is in the facts, [Government Code section 911.2](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=911.2.&lawCode=GOV) requires the written claim within six months of accrual and [section 945.6](https://california.public.law/codes/ca_gov't_code_section_945.6) then allows six months after a written rejection is mailed or delivered. [Code of Civil Procedure section 352](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=352.&lawCode=CCP) tolls the period during a claimant's minority but expressly withholds that tolling from claims that must be presented to a public entity. Correspondence with an adjuster moves none of these dates.

### What the first contact covers, and how the fee agreement reads

Bring the declarations page, the letters with their envelopes or headers, the report numbers, the medical file, the photographs and a dated contact log. On fees, [Business and Professions Code section 6147](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=6147.&lawCode=BPC) requires the contract in writing, signed by both, with a duplicate handed over at signing, and requires it to state the agreed rate, how disbursements and costs will affect the fee and the client's recovery, and that the fee is negotiable and not fixed by law. Where any of that is missing, the plaintiff may void the agreement."""

# ---------------------------------------------------------------- rebuild

parts = re.split(r"(?m)^## (\S+)[ \t]*$\n", src)
head = parts[0]
out = [head]
seen = set()
i = 1
while i < len(parts):
    key = parts[i]
    body = parts[i + 1]
    if key in NEW:
        body = "\n" + NEW[key].strip() + "\n\n"
        seen.add(key)
    out.append("## " + key + "\n" + body)
    i += 2

missing = [k for k in NEW if k not in seen]
for k in missing:
    out.append("## " + k + "\n\n" + NEW[k].strip() + "\n\n")

open(P, "w", encoding="utf-8").write("".join(out))
print("replaced:", sorted(seen))
print("appended:", missing)
