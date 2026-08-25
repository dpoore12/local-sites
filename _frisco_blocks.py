#!/usr/bin/env python3
"""Insert phase 2 blocks into friscogaragedoorrepairexperts.com/copy.md."""
import re, pathlib

P = pathlib.Path("sites/friscogaragedoorrepairexperts.com/copy.md")
text = P.read_text()

SYMPTOMS = {
"symptom_1": """One flat bang overhead, and then a door that feels bolted to the concrete, is a counterbalance spring letting go. Cut power at the outlet, leave the panels resting down, and get anything you need out of the bay before the door is touched again. A wound torsion spring holds enough stored energy to break an arm, so leave the shaft and the winding cones alone.""",

"symptom_2": """A door that starts down, changes its mind, and climbs back up is obeying its reversing circuit rather than defying you. Clear the threshold, wipe both sensor lenses, and check whether a bumper or a bicycle has knocked one bracket off aim. Do not turn the closing force up to win the argument; the resistance is often in the door.""",

"symptom_3": """A low corner, a slack cable, or a roller sitting outside its rail means the panels are no longer evenly supported. Every further press of the button bends more steel. Park on the driveway instead of the bay, switch the opener off at the outlet, and resist the urge to prop the sections up with lumber or a floor jack.""",

"symptom_4": """Motor noise with no movement usually means the trolley and the door have parted company, or a drive part inside the head has stripped. Watch the rail, not the ceiling box. If the emergency release cord is hanging loose, leave it hanging until somebody has confirmed the door is still balanced, because reconnecting to a heavy door damages the operator.""",
}

NEW = {}

NEW["services_summary"] = """Four repairs sit behind nearly every call in this city, and they do not overlap. Counterbalance work restores the lifting force a door has lost. Opener work covers the machine on the ceiling, its reversing circuit and its safety beam. Off-track and cable work resets the geometry that carries the panels. Replacement changes the visible door, and it is the only one of the four that brings in a city permit and an architectural application. Guessing wrong is expensive on streets where every house received the same builder package: order a door when the drums needed retiming, and you pay for weeks of waiting plus an approval nobody needed."""

NEW["services_pick_head"] = """Start with the failure you can actually see"""

NEW["crosslink_head"] = """Something else wrong out there?"""

# ---------------------------------------------------------------- springs
NEW["svc_garage_door_spring_repair_lede"] = """Springs fail in cohorts here. When a whole phase of houses went up inside the same eighteen months, the counterbalance above your header is the same wire, wound to the same turn count, as the one three doors down that broke in March."""

NEW["svc_garage_door_spring_repair_body"] = """### The bang first, then the weight

Spring failure announces itself. One flat crack carries through the kitchen wall, and afterward a door that used to glide feels anchored to the slab. With the panels fully down, stand back from the opening and look along the shaft above the header. A torsion spring that has parted shows an unmistakable gap between two slack coil ends, often with a bright twist of wire at each break. The opener may still hum and drag the door up a few inches. Treat that as a warning rather than a reprieve, because the cables, the bottom brackets and the operator are now carrying a load none of them were sized to hold.

### Why so many doors on one street go at once

Almost nothing in this market is old. City comprehensive-plan work counted 58,574 single-family units, of which 39.6 percent were finished between 2000 and 2009 and a further 31.2 percent between 2010 and 2019. Barely one unit in forty predates 1980. Builders do not order springs house by house. A phase gets one specification, and published sectional-door specifications commonly treat 10,000 cycles as the standard counterbalance rating, with longer-life wire available as an upgrade. A cycle is one trip up and one trip back down. Two drivers, a dog and a bicycle add up to about four cycles on an ordinary day, which spends a 10,000-cycle spring in under seven years. Streets finished together therefore begin snapping together, and the second wave arrives roughly a decade after the first round of replacements.

### A cycle rating is a laboratory number

The trade association that represents door manufacturers publishes a data sheet on what shortens spring life, and none of it appears on the label. A spring dropped or thrown during delivery can pick up a nick that becomes the fatigue crack. Surface rust reduces the effective area of the wire, and corrosion pits let cracks travel faster. Torch-cutting stock wire to length can leave brittle spots if the neighboring coils overheat. Winding to the wrong turn count loads every other counterbalance component. Weight added later, whether that is a coat of paint or a rack of storage hooks bolted to a section, pushes the door past what its spring was chosen for. The same association notes that spring cycle life and whole-door cycle life are measured separately, which is why a door can outlast three sets of springs.

### The part of the job that hurts people

A wound torsion spring stores enough energy to throw a winding bar across a garage. Cones slip, hardware-store bars bend, and a spring that lets go during winding takes the nearest hand with it. There is a second hazard that gets overlooked: with the counterbalance gone, the door itself is simply a few hundred pounds of steel held by two cables. Do not operate it, do not pull a car out from under it, and do not clamp the track to hold it while you work. This is a trained-technician repair with proper bars, a scale and a known door weight.

### The mistake that produces a second invoice

On a two-spring door, replacing only the broken one leaves a partner of identical age and identical cycle count on the shaft. It usually fails inside the same season. The parts that share those cycles are just as tired: end bearing plates, the center bearing, the cable drums and the lift cables themselves. A cable that unwound under load can score a drum groove, and a scored drum chews the replacement cable. A careful visit weighs the door, sizes the wire to that weight, and prices the worn hardware in the open rather than discovering it on the next call.

### Ground that will not hold still

Collin and Denton county subdivisions sit on Blackland Prairie clay. The federal soil description for the dominant black clay of this belt records dry cracks half an inch to four inches wide, open for 90 to 150 cumulative days in most years. The city takes that seriously enough that its residential submittal guide requires a design letter stating soil bearing capacity, plasticity index and potential vertical rise before a foundation is approved. When a garage slab and its jambs move a little out of square, the two cable drums no longer unwind evenly, one bottom corner meets the floor early, and the springs get asked to balance a door that is no longer hanging plumb. That shows up as premature wear rather than a dramatic failure, and it is worth measuring while the counterbalance is unloaded.

### What the appointment looks like

The door is secured so it cannot run while the shaft is being handled. The technician measures the opening, weighs the door, reads the existing spring for wire size, inside diameter and length, then selects replacements for the door in front of him instead of the door the invoice remembers. Bearings, drums and cables are inspected while the system is safely at rest. New springs go on, the drums are set with matched cable tension, and the shaft is wound with the correct bars. The last step is a hand balance check through the full travel: a balanced door stays roughly where you leave it rather than racing up or slamming down. Only then does the opener get reconnected and its travel confirmed. The range on this work is driven by spring count, wire size, cycle rating and door weight, plus any drum, bearing or cable that has to change with them. The figure is agreed before the old springs come off."""

# ---------------------------------------------------------------- opener
NEW["svc_garage_door_opener_repair_lede"] = """An opener is a motor, a drive, a control board and a federally mandated reversing system. Two very different complaints arrive under the same heading: a door that refuses to stay down, and a motor that runs while the door sits still."""

NEW["svc_garage_door_opener_repair_body"] = """### Sort the complaint before anyone buys a machine

Start by watching the rail rather than the ceiling box. If the chain or belt travels while the panels stay put, the trolley has been released from the carriage, or the drive connection has failed. If the motor grinds and the rail never moves, suspicion falls on the drive gear, the sprocket or a start component. If the door closes a foot and returns, the operator is doing its job and something else in the opening is triggering it. Those three observations lead to three different parts lists, and a homeowner who reports which one happened has already saved a visit.

### What the reversing system is legally required to do

Residential operators sold in this country are built to a federal standard, 16 CFR part 1211, and the numbers in it explain behavior that homeowners read as faults. A closing door that meets a one-inch object on the floor must begin reversing within two seconds and then return to the fully open position, with the operator pulling at least twenty-five pounds-force during the test and passing fifty open-and-close cycles. The first foot of travel down from full open is excluded from that requirement. A door that has not reached its close limit within thirty seconds must reverse and go back up. On top of that inherent protection, the operator carries a second layer: an external photoelectric sensor, an edge sensor on the bottom section, or an equivalent internal door sensor. A protection device mounted three feet or less above the floor has to survive a hose splash test, which tells you how much water the standard expects on a garage floor.

### Which unit is on your ceiling, and why that matters

With four fifths of the housing stock finished after 2000, the operator overhead is very often the one the builder installed, chosen the same week as the door and by the same purchasing decision. That has two consequences. Parts availability is usually good, so a gear kit, a logic board, a capacitor or a safety-eye pair is frequently the right answer instead of a new head. But it also means the unit is exactly as old as the springs, the rollers and the sensor brackets, and a house at the twenty-year mark can present three unrelated symptoms in one month that all trace to the same install date.

### What not to do while it misbehaves

Do not raise the force setting to push a door past resistance. Force is the safety margin, and cranking it turns a binding roller into a stripped gear or a section pulled out of the track. Do not tape, bypass or aim the photo eyes at each other from bad angles to get one last close, and do not disconnect them. Reconnecting the trolley to a door that is heavy, crooked or held by one cable risks a sudden drop and a damaged carriage. Opening the motor housing to spray lubricant into it is not maintenance either; the parts that want attention are the hinges, roller bearings and the counterbalance hardware, and the tracks want to be clean rather than greased.

### The reversal that has nothing to do with electronics

A door reversing off the floor with clean lenses and steady indicator lights is usually reporting mechanical drag. Bent vertical track, a cracked nylon roller, a loose hinge, a frayed cable, or a counterbalance drifting out of balance all make the operator work harder than its limits allow. Clay-driven slab movement in this part of North Texas contributes here too: a floor that has heaved a fraction of an inch at one corner can hold the bottom seal early, and a jamb that has shifted takes the sensor brackets out of alignment with it. The honest sequence is to make the door move freely by hand, then align the safety devices, then set travel and force. Reversing the order sells a machine to cover for a rail.

### The trap a hurried operator falls into

Replacing a head unit on an unbalanced door is the classic second visit. The new opener lifts a dead-weight door for a few weeks because it has more muscle than the old one, then strips its own gear and gets blamed. Any competent opener call includes disengaging the trolley and lifting the door by hand to see whether the springs are still doing their share. The other shortcut worth refusing is a board replaced on suspicion without testing supply voltage, the safety circuit, the wall control and the receiver, because an intermittent connection in a hot attic space can imitate a dead board convincingly.

### The visit, and what moves the number

The technician confirms trolley engagement, checks the door by hand, tests the safety circuit and the controls, then works inward to the drive and the board. Repair is often reasonable: gear kits, sprockets, capacitors, receivers, sensors, wiring and rail hardware are all serviceable items. Replacement makes more sense when a critical board is no longer made, the housing is cracked, or the unit predates working entrapment protection. What moves the range is drive type, horsepower class, whether battery backup and a keypad are included, rail length for a tall opening, and whether the existing wiring and outlet position can be reused. Elective upgrades belong on their own line so the necessary work can be read separately, and the total is set before anything is unbolted."""

# ---------------------------------------------------------------- off track
NEW["svc_off_track_garage_door_repair_lede"] = """An off-track door is an unstable load. A cable that jumped its drum, a roller out of the rail, or a section knocked askew leaves the remaining hardware holding weight unevenly, and every extra cycle spreads the damage further."""

NEW["svc_off_track_garage_door_repair_body"] = """### Reading a crooked door from a safe distance

Stand back and look for three things: whether one bottom corner sits lower than the other, whether either lift cable has gone slack or looped near a jamb, and whether a roller stem has left the track. Any one of those means the panels are no longer evenly supported, and the remote will not square them up. What it will do is pull harder on the side that still lifts, which is how a repairable misalignment becomes creased sections and bent vertical track. Switch the opener off at the outlet, keep the bay clear of cars and people, and do not brace the door with lumber, a ladder or a jack.

### Four faults that look alike from the driveway

A cable fault usually shows as slack wire and one low corner, and it often follows a spring failure or an obstruction under the door. A roller fault announces itself first as grinding: nylon cracks, steel seizes, and worn hinges hold the stem at an angle until it walks out at the curve. A track fault comes from impact, loose lag screws at the jamb, or storm force, and it is measured against the door rather than judged from one visible dent. A hinge fault concentrates load at one panel joint and shows as a section starting to fold. Each of those repairs needs the counterbalance safely unloaded before anything is reset, which is the part that keeps a pry bar out of the job.

### Ground movement is a local variable, not an excuse

Subdivisions across Collin and Denton counties sit on the deep clays of the Blackland Prairie. The federal description of the black clay that dominates this belt records shrinkage cracks from half an inch to four inches wide, staying open for 90 to 150 cumulative days in a typical year. The city's own residential submittal guide requires a soils report and design letter stating soil bearing capacity, plasticity index and potential vertical rise before a foundation drawing is accepted, which is a plain admission that the ground here rises and falls. In an attached garage that appears as a slab corner sitting a little high, a jamb no longer plumb, or a header that has taken a slight twist. Rollers then run tight at one side of the opening, the two drums stop unwinding evenly, and a door that has been quietly fighting its own frame for a year finally jumps the rail on a cold morning.

### After a storm, the dents are the least of it

Weather service records for the April 3, 2014 outbreak include trained-spotter reports of hail up to two inches across in this city. Steel skins take that badly and look terrible afterward. Appearance, though, is not what stops a door. The questions that matter are whether the vertical tracks are still plumb, whether a horizontal strut across the back of a section has bowed, whether hinge fasteners have pulled, whether the top section still meets the header evenly, and whether the photo-eye brackets took a hit. A door with a field of dimples may run perfectly for years. A door with a bowed strut destroys rollers on every cycle until somebody straightens the geometry.

### This is the repair that keeps you out of the approval queue

The city lists replacement doors and windows among the residential jobs that need a permit, and this is not one of them: resetting cables, drums, rollers, hinges and track is service on the door you already own. The same logic applies to your neighborhood documents. With more than two hundred associations in town, a homeowner who saves the original panels and the original finish has nothing to submit to an architectural committee, because the street-facing appearance has not changed. That is worth knowing before agreeing to a proposal that jumps from a derailed section straight to a new carriage-style door with glass, which is a permit, an application and a lead time rather than an afternoon.

### What a careless job leaves behind

The shortcuts are recognizable. Rollers pushed back into the rail without being replaced. A bent track section hammered roughly straight and re-bolted through the old holes. A cable rewound onto a drum whose groove has already been scored, so the new cable frays at the same spot. Set screws taken up on a shaft that has moved sideways, leaving the springs to snake against each other. Any of those buys a few weeks. The test that separates real work from cosmetic work is a hand cycle: with the trolley disengaged, the door should travel smoothly, stay where it is left, and show even gaps at both jambs.

### How the visit runs, and what sets the price

The door is secured against movement, the counterbalance load is relieved in the right order, and the damaged parts are identified individually rather than pushed back into place. Tracks come off if they are bent, fasteners are checked at the jamb and the header, drums are reset with matched tension, and the panels are guided back through the path under control. Then comes the hand cycle, the balance check, and only after that the opener, with its travel and reversing behavior tested again. The range depends on how far the door traveled off the rail, how many rollers, hinges, cables and track sections actually need replacing, whether one section has lost its rigidity, and how much of the counterbalance has to be dismantled to get at the rest. That figure is set at the opening, before the work starts."""

# ---------------------------------------------------------------- replacement
NEW["svc_garage_door_replacement_lede"] = """Replacing the door is the one job on this list that involves paperwork twice: a city permit for the work, and an architectural application for the appearance. Both are cheap. Neither is quick if you start them on installation morning."""

NEW["svc_garage_door_replacement_body"] = """### When repair stops being the honest answer

Some doors are past saving, and the signs are structural rather than cosmetic. A section that has folded around a hinge line has lost the stiffness the whole assembly relies on. A profile that is no longer manufactured turns a one-panel swap into a hunt, and a mismatched replacement panel is visible from the street forever. Rusted-through bottom sections, repeatedly re-straightened track, and a door whose weight has crept past what its hardware was designed for all point the same way. Everything else on this site is an argument for repair first, because a mechanical fix keeps the existing exterior and skips both approval paths described below.

### The city's side of it is small and specific

Frisco puts replacement doors and windows on its self-service permit list, alongside roofs in the same material, water heaters and heating and cooling swaps. The consolidated fee schedule prices a window or door replacement permit at $75, adding $25 for each additional element up to a $150 ceiling. An inspection outside normal business hours is priced at $150 on residential work. Contractors register with the Building Inspections Division before they can pull it, and the registration number they receive expires the day their general liability coverage does, which is a quiet way of verifying insurance. Inspection requests go through the city's online permit system before 7 a.m. for same-day service. If no contractor is attached to the permit, the homeowner can email a request, and one received before 4 p.m. is scheduled for the next business day. Work is inspected against the adopted residential code with local amendments, and the city moved to the 2024 edition effective March 1, 2026.

### The association side is where the calendar goes

More than two hundred homeowner associations operate in this city, and the City keeps a voluntary directory of their management companies and board contacts. A garage door is usually the largest single element on a front elevation, so panel style, window layout, color and decorative hardware are exactly the things a neighborhood's documents speak to. Assume an application is required for any change to material, color, glass or profile, and read your own declaration rather than a neighbor's summary of it. The mechanical work never has to wait for that: a door that is unsafe gets stabilized now, and the visible replacement gets ordered once the committee has answered.

### What Texas law lets a committee do, and what it must do

Chapter 209 of the Property Code, the Texas Residential Property Owners Protection Act, sets the procedure. In an association of more than forty lots, outside the declarant's development period, the architectural review authority cannot include a current board member, that member's spouse, or anyone living in that member's household. A denial has to reach the owner in writing, by certified mail, hand delivery or electronic delivery. It must describe the basis for refusal in reasonable detail and state what changes would earn approval, and it must tell the owner that a hearing may be requested within thirty days. The board then has thirty days to hold that hearing and must give ten days notice of it, and afterward it may affirm, modify or reverse the committee, in whole or in part. Either side can ask for one postponement of up to ten days. The 2025 legislature revisited this section through Senate Bill 711, so an owner reading an older printout should check the current text.

### Where the leverage actually sits

Two things surprise owners. First, chapter 202 tells courts to construe restrictive covenants liberally to give effect to their purpose, and it presumes that an association's discretionary decision is reasonable unless a court finds by a preponderance of the evidence that it was arbitrary, capricious or discriminatory. That is the standard an owner has to meet, and it is why a written, specific, on-the-record denial matters so much. Second, the legislature has protected particular exterior items by statute, including wind and hail resistant shingles, solar devices, flags and certain pool enclosures. Garage doors are not among them. There is no state exemption that lets a homeowner install any door they like, and any claim otherwise deserves a citation before you rely on it. The practical route is the application, a specification sheet with the panel profile and color, and a paper trail. Enforcement runs the other direction too: a court may assess damages up to $200 for each day a covenant is violated.

### Measure the opening before choosing a door

Width and height are the easy part. A complete measurement records headroom above the header, side room at each jamb, backroom depth to the rear wall, ceiling obstructions, the opener location, the jamb condition and whether the slab is still level. Clay movement makes that last item a real question in this county pair rather than a formality. Weight then drives the counterbalance: insulated sections, glass inserts, heavier gauge steel and decorative overlays all add pounds, and springs sized for the door coming down will not balance the door going up. New spring specification, and often new drums and cables, belong in the same conversation as the door.

### What the quote should itemize

Ask for the door by manufacturer, model, gauge, insulation value, color, glass option and hardware style, because those are the fields an architectural application asks for anyway. Ask whether the price includes new track, new springs sized to the finished weight, disposal of the old sections, and reuse or replacement of the operator and its rail. Ask for the permit as its own line, the association paperwork as another, and a delivery window rather than a promise. Full-door replacement covers a wide range in this market, driven mostly by insulation, glass and how much of the elevation is door. A quote that folds any of the above into one lump sum is the quote most likely to grow."""


def replace_block(txt, key, body):
    pat = re.compile(r"(## %s\n\n)(.*?)(?=\n## )" % re.escape(key), re.S)
    assert pat.search(txt), key
    return pat.sub(lambda m: m.group(1) + body.strip() + "\n", txt, count=1)


for k, v in SYMPTOMS.items():
    text = replace_block(text, k, v)

add = "\n".join("## %s\n\n%s\n" % (k, v.strip()) for k, v in NEW.items())
marker = "## pricing_lede"
assert marker in text
text = text.replace(marker, add + "\n" + marker, 1)
P.write_text(text)
print("written")
