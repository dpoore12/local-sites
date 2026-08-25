#!/usr/bin/env python3
"""Apply phase 2 copy blocks to mariettagaragedoorrepairpros.com."""
import json, re, pathlib

SITE = pathlib.Path("sites/mariettagaragedoorrepairpros.com")
COPY = SITE / "copy.md"

SYMPTOMS = {
"symptom_1": """A bang loud enough to carry into the house, then a door that barely lifts, is a broken counterbalance spring rather than a tired opener. From several feet back, look along the shaft above the opening for a coil split by a finger-width gap. Unplug the operator so nobody presses the wall button out of habit, and leave the door down on the slab.""",

"symptom_2": """The door starts down, thinks better of it, and climbs back to fully open. That is the safety circuit doing its job. Check the two photo eyes near the slab for pollen film, a leaning rake handle, or brackets knocked out of square, and wipe each lens dry. If both eyes read steady afterward and it still retreats, the door is dragging somewhere.""",

"symptom_3": """One corner riding low, a roller sitting outside its rail, or a section folded where a limb landed all mean the door is holding weight in an arrangement that will not stay put. Cut power at the outlet, keep the opening clear, and do not lever anything back with a pry bar. Pressing the button again is what bends the next section.""",

"symptom_4": """Motor noise with a motionless door is usually the trolley parted from its carriage after somebody pulled the red release cord. With the door flat on the floor, it re-latches in about a minute. A grinding rattle over a chain that never moves points instead at a chewed drive gear inside the head, which is a part swap.""",
}

NEW_BLOCKS = []

def add(key, text):
    NEW_BLOCKS.append((key, text.strip()))

add("services_summary", """
Four separate jobs get phoned in under one description. A counterbalance spring is a weight problem, an operator fault is electronics and the safety circuit, a derailed door is cables, rollers and rail geometry, and a replacement is a building project that can reach the permit counter at city hall and, on some streets near the square, a design review calendar. Sorting them wrong is what produces two visits. A technician routed for an opener cannot wind a spring he never loaded, and a household that authorizes a whole new door for a jamb that drags pays four figures for what a bearing, a roller set and a seal would have settled.
""")

add("services_pick_head", "Start from the failure you can actually see")

add("crosslink_head", "Something else going wrong?")

# ---------------------------------------------------------------- springs
add("svc_garage_door_spring_repair_lede", """
Spring failures arrive as noise. The door was fine on the way out and immovable on the way back, and the part that changed sits on a shaft over the opening holding more stored energy than anything else in the garage.
""")

add("svc_garage_door_spring_repair_body", """
### The bang, and what the shaft shows

A counterbalance spring letting go is loud, and the sound is most of the diagnosis. Afterward the door either refuses to rise or comes up a few inches and stalls, because the springs were carrying the weight of all that sheet steel and the operator was only steering it. Walk in and look along the shaft above the header from a few feet back. A failed torsion spring shows a clean break with both halves relaxed and slightly unwound, leaving a visible gap in what used to be a continuous coil. In an older detached garage you may find extension springs instead, stretched back beside the horizontal rails with one of them hanging slack. The trade's own inspection checklist asks whether extension springs are contained by a cable running through the center of each one, because that cable is what keeps broken parts from flying across the garage.

### What the counterbalance on your street probably is

The age of the garage decides this more reliably than the age of the house. Marietta's Church Cherokee homeowners' handbook records that attached garages debuted in the 1940s and gained popularity through the 1950s, and that before the middle of the century most families kept a single car in a small secondary structure with one bay and one door. Those detached garages and carriage houses are still standing across the blocks covered by the Church-Cherokee and Whitlock Avenue districts, and they frequently pair shallow headroom above the opening with original extension hardware. Later subdivisions read differently. Charlton Forge, the Westside streets and the newer pockets out along the Loop are sectional-and-torsion, usually two bays wide, with room over the header for a full-length shaft. Arriving with the wrong assumption costs a second appointment.

### Wet air is a spring problem, and the industry says so

Manufacturers are blunt about moisture. The association data sheet on spring cycle life says springs must be kept dry to prevent surface rust, because rust reduces the effective area of the spring wire and with it the wire's strength. It goes further: corrosion pits become the place fatigue cracks start and accelerate, which cuts cycle life outright. The same sheet notes that a door parked open for long stretches leaves its springs exposed to swings in temperature, moisture and air quality. Now set that against the Weather Service climatology for this part of the state. Rain runs 50 to 55 inches in a typical year, falls on roughly 120 days, and thunder is heard on 50 to 60 of them, with summer arriving as long spells of warm humid air. Spring wire here is aging on a schedule that wire in a dry state never sees.

### Winding bars, and why nothing in the toolbox substitutes

A broken torsion spring is still dangerous, because the surviving half remains partly loaded and the shaft can turn. Winding bars sized to the cone are the only correct tool. Screwdrivers, rebar and socket extensions slip out under load and become projectiles. The published checklist says it without hedging: with a broken spring, do not operate the door, and do not attempt to remove, repair or adjust springs, cables, brackets or the wood and steel they mount to. Until help arrives, cut power to the operator, keep the door on the slab, and keep vehicles and people out from under the opening.

### Two springs, one age, one decision

When a two-spring door loses one, the survivor has logged the same openings in the same damp garage and is not a fresh part. Fitting both at once costs a little more steel and removes an entire return trip. The cycle life sheet also warns that a spring has to match the door's counterbalance requirement, which is where a repainted door gets people. Adding coats to a real wood door can push it past the weight the manufacturer specified, and a technician can put a scale under it once the counterbalance is disabled rather than guess. That is a live question on the older streets, where doors are wood and get refinished on a cycle.

### Where a hurried swap goes wrong

Two things separate a spring job that lasts from one that comes back. The first is turn count, which the door maker specifies for that height: too much torque loads every other counterbalance part, and too little leaves the door drifting down out of its open position. The second is everything the failure touched on the way down. A spring breaking drops the door hard enough to unseat a cable from its drum and bruise the bottom brackets, so cables, drums and bearings get inspected while the tension is off, not after new springs are wound.

### What the visit looks like, and where the number lands

Wire diameter, inside diameter, length and wind direction come off the failed spring or its stamped cone, and replacements are matched to the door's measured weight instead of a chart. Both springs come off, the drums are reset, and the new pair is wound to the specified turns. Corroded fasteners often have to be cut out rather than turned, which is where the extra minutes in a humid garage go. Then the operator is disconnected and the door is lifted by hand: it should hold near waist height rather than sinking or climbing. Ask to watch that. Pricing is quoted before a tool comes out, and the spread inside it comes from spring count, wire size, cycle rating, and whether cables, bearings or drums go with them.
""")

# ---------------------------------------------------------------- opener
add("svc_garage_door_opener_repair_lede", """
Two unrelated complaints reach the phone with the same label. A door that retreats partway down is the safety circuit doing exactly what it was built to do, and a motor running while the door sits still is often a one-minute fix.
""")

add("svc_garage_door_opener_repair_body", """
### Down a couple of feet, then straight back up

Federal rules put that behavior in writing. Part 1211 of title 16 requires a downward moving residential door to begin reversing within two seconds of meeting an obstruction, then return the door to the fully open position and stop there. So an operator that backs off and parks itself open is not malfunctioning in any obvious sense. It is reporting that something interrupted the close. The whole job is figuring out what it believes it touched, and the answer is almost never the motor overhead.

### What the rule actually requires of the box on your ceiling

The same federal standard applies to every residential operator manufactured on or after January 1, 1993. Each one has to carry inherent primary entrapment protection built into the drive. On top of that, a vertically moving door needs a second layer: either constant pressure on a control installed within sight of the door, or a connection for an external secondary device, meaning a photoelectric sensor or an edge sensor mounted on the door. The rule also governs the red handle. It must be visually distinct from the rest of the operator, adjustable to six feet above the garage floor, and able to release an obstructed door under a pull of no more than fifty pounds. The industry checklist adds the measurement nobody takes: that photo eye beam should sit no higher than six inches above the floor.

### Pollen, condensation and two lenses near the slab

Humid air here does not break an operator, but it reliably confuses the two eyes bolted beside the jambs. Warm moist air meeting a cool lens leaves droplets on it, which is the same mechanism the door industry describes for condensation on panels and glazing, and a wet car parked inside raises the humidity that feeds it. Spring pollen sticks to the film. Grit blown under the door builds up in the small brackets, and years of the door shaking the jamb walks those brackets out of square. Wipe both lenses dry with a soft cloth, sight the brackets at each other, and look for a steady indicator on both housings before suspecting anything electronic.

### Turning the force up is not a repair

When a door binds, the operator reads the resistance as an obstruction and reverses, which is the protection working correctly on a mechanical fault. A swollen wood bottom section, a bearing that has rusted dry, a cracked roller or a bottom seal grabbing the slab will all do it. Raising the close force setting hides the symptom for a while and spends the safety margin that caught the problem. The honest test is the one the checklist describes: lay a solid object an inch and a half thick flat under the center of the door and close it. The door should reverse on contact and return fully open. If it does not, that operator needs service before anyone talks about force settings.

### Motor noise, and a chain that never moves

Watch the rail while somebody presses the button. Chain or belt traveling with the door standing still means the trolley has come off the carriage, usually because the emergency release was pulled or snagged. With the door flat on the floor and moving freely by hand, it re-engages in about a minute. A grinding rattle with nothing traveling is different: that is normally a nylon drive gear with its teeth rounded off, which is a part inside the head rather than grounds for a new unit. A short hum followed by silence points instead at a starting capacitor or the board.

### Wiring in a detached garage is a separate trade

Behind the older houses, the garage often sits at the end of a narrow linear drive, sometimes past a porte-cochere, and it may have no dedicated circuit at the ceiling at all. That is not a door problem. Marietta requires an electrical permit for work done on electrical systems, and the state minimum electrical code adopted by the Georgia Department of Community Affairs is the 2023 National Electrical Code with Georgia amendments. The city also runs stand-alone trade inspections in occupied homes over a video call, scheduled by phone with an installer standing at the equipment, which keeps a small electrical scope from turning into a week of waiting.

### When a new head is honest, and what you should be told

An operator old enough to have no secondary entrapment protection at all should be replaced rather than nursed, and so should one with a cracked housing or a board nobody stocks. Two repairs inside two years is a fair signal as well. Short of that, most heads on houses here are worth fixing, and the answer you should get is a named fault, the price of the part, and a straight read on whether spending it makes sense given the age of the unit. Battery backup and a belt drive are real improvements in a place where storm outages happen, and they should be offered as upgrades in exactly those words rather than folded into a repair.
""")

# ---------------------------------------------------------------- off track
add("svc_off_track_garage_door_repair_lede", """
A door sitting crooked in its opening is a cable, roller or rail problem, and it is the one failure that gets measurably worse while somebody stands in the driveway pressing the button to see how bad it is.
""")

add("svc_off_track_garage_door_repair_body", """
### Read it from the doorway and leave it there

Whatever cables and rollers are still engaged are the only things holding a derailed door up, and that geometry stops being stable the moment a section leaves its rail. Cycling the operator to see how bad it is turns a partial derailment into a door across a hood. Kill power at the outlet, keep everyone out of the opening, and put the pry bar down. This is the failure that gets pulled to the front of the day rather than scheduled for later in the week.

### The three ways a door leaves its rail

A lift cable can jump its drum. Each cable anchors at a bottom bracket and winds into grooves on a drum at the end of the torsion shaft, and when a spring failure drops the door hard, one cable can leave those grooves. That half of the door loses its lift and racks in the opening, with loose cable coiled near the jamb as the tell. A roller can also come out. Nylon wheels crack and steel ones seize once their bearings run dry and grit packs in, and a seized roller skids until it climbs out, almost always at the curve where the vertical rail turns horizontal. Or the rail itself is bent, from a bumper, a fallen limb, or a section that has already been forced back once.

### Red clay, a sloping lot, and a jamb that moved

Most of this county sits on Piedmont uplands, and the soil series mapped across that landscape is Cecil, described by the federal soil survey as occupying interstream divides, ridges and side slopes at grades from level to twenty-five percent. Under a sandy loam surface it turns to red clay that the official description calls firm, sticky and plastic, running well past sixty inches before bedrock. Two consequences land on a garage. Surface runoff is rated medium and the lots are graded, so a garage at the low end of a drive receives the water coming off it, roughly fifty inches a year. And every roller and rail in that opening is referenced to a jamb bolted to framing at the slab edge. Manufacturers treat that connection as being as important as the door, publishing anchor spacing schedules from ten to sixty pounds per square foot of wind load and recommending engineering advice for the attachment. A jamb that has settled or rotated a fraction of an inch out of plumb shows nothing from the street. It shows up as one roller climbing at the radius.

### The bottom two feet take the weather

Water sitting at the slab edge does its damage low. On a wood door, the bottom section wicks moisture and receives more of it than any other part, which is why the trade's wood door guidance asks for inspection every twelve to eighteen months and a close look at the wood behind every hardware attachment point. Loose hardware on a swollen section is not a tightening job, it is a structural question. The bottom brackets carry full cable tension, so corroded fasteners there usually get cut out instead of turned. Grit ground into rollers, a seal no longer meeting the slab, and a rusted bearing plate all show up first as drag, then as a door that comes off.

### What not to attempt in the meantime

Nothing on a derailed door is a homeowner repair, and the reason is that the counterbalance and the cables are still loaded even when the door looks slack. Do not clamp, wedge or rope it into position, do not lift one corner to reseat a roller, and do not run the opener to test whether it caught. Park vehicles outside the bay. If the door is standing partly open, keep the whole opening clear until somebody has secured it below the lowest roller.

### How the repair proceeds

The door gets clamped so it cannot travel, then sections come back into line one at a time. Rollers are reseated or replaced, cables are respooled with matched tension at both drums, and rail is straightened only where its shape and mounting holes are still sound. A rail with a hard crease gets replaced rather than persuaded, because a forced rail binds again within weeks. Hinges are checked at every joint, since a section that came out usually took one with it. The jamb, the header attachment and the plumb of both vertical rails get verified, which is the step that matters on an opening that has moved. Then the door comes off the operator and is balanced by hand.

### What decides the number

Rollers, cables and hinges are inexpensive parts, and rail sections are moderate. What actually moves the total is how far the door traveled out of line, whether any section bent in the process, and whether the framing behind the rail has to be repaired before anything is anchored back to it. A section damaged past sensible repair should be named as that on site, before the work, rather than billed as a repair and then a replacement.
""")

# ---------------------------------------------------------------- replacement
add("svc_garage_door_replacement_lede", """
Replacement is the only garage door job here that can put a household in front of two counters. One is the permit desk at city hall. The other, on certain streets, is a board that reviews how the finished door will look.
""")

add("svc_garage_door_replacement_body", """
### Which desk your address answers to

Cobb County's Community Development Agency carries a Marietta mailing address on Powder Springs Street, and it permits the unincorporated county. A property inside the city limits files instead with the city's own permits and inspections office and submits through the city's online portal. Same postal city, two different jurisdictions, and confirming which one applies is step one rather than an afterthought. The published city answer to when a permit is needed covers an owner or contractor who intends to construct new, enlarge, alter, repair, move or demolish a building or structure, with new window installation and outdoor accessory structures among the listed examples. No garage-door-only exemption appears there, so scope and address get confirmed before a door is ordered. Where a permit does apply to residential work, the fee is calculated from construction value, labor and materials together, at $5 per $1,000 with a $50 base and no plan review charge. Failed inspections escalate from $50 to $75 to $100.

### Historic review comes before the order, not after

In August 2013 a stretch of Kennesaw Avenue became the city's first locally designated historic district, and properties inside it need a Certificate of Appropriateness before starting the categories of work listed in the preservation article of the development code. Downtown, exterior work goes to the Historic Board of Review on a Certificate of Approval application, and the city states that a building permit will not be issued without an approved certificate where one is required. Five more districts, Atlanta-Frasier Street, Church-Cherokee, Northwest Marietta, Washington Avenue and Whitlock Avenue, are listed on the National Register. The city's Church Cherokee guidelines are explicit about the buildings this trade works on: garages, carriage houses and other accessory structures are important elements of a historic residential district, should get the same aesthetic care as the house when they are visible from the public right-of-way, should stay secondary in scale, and should be retained and repaired where the original is significant. That guidance also notes those garages historically had a single bay and one door. A wide flush steel panel on a 1920s carriage house is a review problem long before it is a taste problem.

### The code the inspector is working from

Georgia adopts construction codes at the state level. The Department of Community Affairs lists the mandatory residential code as the 2024 International Residential Code with Georgia amendments, and city inspectors work from that adopted edition rather than a local rewrite. Licensing sits at the state as well. The Secretary of State's policy statement on traditional specialty contractors names overhead doors as a specialty category, and says specialty contractors working inside their own specialty are not required to hold a residential or general contractor license, while still having to comply with every applicable national, state and local code and ordinance. On the city side, a residential permit application asks for a copy of the general contractor's state license and business license. A homeowner pulling the permit personally signs a notarized property owner's affidavit under the conditions in the state licensing statute.

### One section, or the whole door

A single crushed section can often be replaced on its own, and that is the cheaper and faster answer when the door is a common steel profile still in production, the remaining sections are sound, and a color match is achievable or acceptable. Matching gets harder with age, and an embossed pattern discontinued fifteen years ago will not blend. Full replacement earns its keep when the stiles of a wood door have gone soft, when several sections are creased, when the door has been rebuilt more than once, or when the panel weight has drifted so far from the original that the counterbalance can no longer be sized honestly.

### Measuring an older opening

Nothing about a replacement can be quoted from a photograph. The measurements that decide the order are the finished opening width and height, headroom between the header and the ceiling, backroom for the horizontal rails, the condition and plumb of both jambs, and the level of the slab across the threshold. Older detached garages are where this bites. Headroom is often short enough to force low-clearance hardware, the jamb has usually been repaired at least once, and a slab that has settled at one corner leaves a gap the new bottom seal has to close. Any jamb or header rebuilding belongs in the written scope, not in a conversation on installation morning.

### Specifying a door for wet summers

Material choice is where a local specification differs from a catalog. A wood or wood-clad door should be finished on all six sides before it is hung, because a door finished after installation leaves faces exposed and can void the manufacturer's warranty, and wood doors want inspection and maintenance every twelve to eighteen months here. Insulated doors and glazing bring condensation into the conversation, and the industry answer is ventilation, tight seals at the glazing perimeter and around each section, and cleaning products the glazing maker approves. Sealed rollers, galvanized or coated hardware and a bottom seal sized to the actual slab profile are worth naming line by line in the quote.

### Lead time, and what moves the total

Stock steel doors in common sizes move quickly. A made-to-order wood or carriage-house door is a lead time measured in weeks, and if the address needs design review, that clock starts only after the certificate is approved. Costs track construction and size more than brand: single bay against double, insulation, glass, real wood against clad or steel, custom hardware, plus jamb repair, removal of the old door, and the permit where one applies. The order should not be placed until the opening has been measured, the jurisdiction confirmed, and any review approved in writing.
""")


def main():
    text = COPY.read_text()
    for key, body in SYMPTOMS.items():
        pat = re.compile(r"(?ms)^## " + key + r"\n.*?(?=^## )")
        new = "## %s\n%s\n\n" % (key, body.strip())
        text, n = pat.subn(lambda m: new, text, count=1)
        assert n == 1, key
    # insert new blocks before ## pricing_lede
    chunks = "".join("## %s\n\n%s\n\n" % (k, v) for k, v in NEW_BLOCKS)
    idx = text.index("## pricing_lede")
    text = text[:idx] + chunks + text[idx:]
    COPY.write_text(text)

    sj = SITE / "site.json"
    raw = sj.read_text()
    assert '"phase": 1' in raw
    sj.write_text(raw.replace('"phase": 1', '"phase": 2', 1))
    print("done")

if __name__ == "__main__":
    main()
