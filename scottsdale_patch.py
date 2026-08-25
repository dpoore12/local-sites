import re, pathlib, json

P = pathlib.Path("/home/user/workspace/local-sites/sites/scottsdalegaragedoorrepairpros.com")
cm = P / "copy.md"
txt = cm.read_text()

NEW = {}

NEW["symptom_1"] = """That report usually means a counterbalance spring let go. The opener is built to guide a nearly balanced door, not to hoist its full weight, so it may hum, pull an inch, and quit. Sight along the shaft above the header for a coil split into two loose halves. Leave the door where it sits, keep everyone out of the opening, and stop pressing the button."""

NEW["symptom_2"] = """A door that starts down and climbs straight back up is obeying its own reversing circuit. Dust film on the two lenses near the slab, a bracket nudged out of aim, or hard late sun into the receiving eye will each cancel a close cycle. Wipe both lenses, clear the beam path, and note whether each indicator holds steady or blinks."""

NEW["symptom_3"] = """One corner riding low, a slack cable at the jamb, or a wheel sitting outside its rail means the door has stopped carrying its weight evenly, and every press of the button drives the damage deeper. Kill power at the outlet if you can reach it from outside the opening. Leave the bottom brackets and the release cord alone."""

NEW["symptom_4"] = """Sound without motion usually means the trolley has parted from its carriage, often after somebody pulled the red cord and never relatched it. A grinding rattle points at a chewed drive gear instead. A head that answers at sunrise and ignores the wall button by four in the afternoon is an electronics question, so ask for it to be tested while the garage is still hot."""

NEW["services_summary"] = """Four different repairs arrive under one phrase in this city. Counterbalance springs fail most often and punish improvisation hardest. Opener work runs from the two photo eyes near the slab out to logic boards and relays that have spent a decade in an uncooled garage. Cable, roller and track work is the urgent one, because a racked door keeps injuring itself on every cycle it is asked to run. Replacement is the only one of the four that brings in a city permit, an energy rating on any glazing, and in the ranch communities an association design file. Naming the right job early is what gets the correct part onto the truck."""

NEW["services_pick_head"] = """Start with what the door is actually doing"""

NEW["crosslink_head"] = """Something else going wrong"""

NEW["svc_garage_door_spring_repair_lede"] = """Springs carry the entire weight of the door, and a Sonoran summer loads them in ways the cycle count alone does not show. This work is measured, matched and replaced in pairs, never eyeballed."""

NEW["svc_garage_door_spring_repair_body"] = """### The bang, and what comes after it

Homeowners describe two events in the same order. A hard metallic crack somewhere in the house, usually overnight, and then a door that refuses to rise the next morning. The motor labors, lifts an inch, and stops. Sight along the steel shaft above the opening from a safe spot on the floor. A failed torsion coil separates into two loose halves with a finger-wide gap between them. Older garages here carry extension springs alongside the horizontal rails instead, and a break there leaves one hanging slack with only its containment cable holding the pieces together.

### What a hundred-and-ten-degree summer does to a coil

The Weather Service office for the Valley has kept Phoenix records since 1896, and the totals describe the working environment. The year 2024 brought 70 days at or above 110 degrees, the most in the record, and 2020 brought 145 days at or above 100 degrees. One stretch held at 100 or hotter for 113 straight days, from May 27 to September 16, 2024. Another held at 110 or hotter for 31 straight days, from June 30 to July 30, 2023. The hottest reading on the books is 122 degrees, set June 26, 1990.

Steel does not snap because a garage got warm. It fails from fatigue, and heat governs the variables around fatigue. Every expansion and contraction of a wound coil, every hour of grease sitting thin on the shaft, and every degree of extra drag in a dry bearing adds to the count the metal is actually keeping. The trade literature is direct about it. The DASMA data sheet on spring cycle life notes that a door left open for long periods exposes its springs to wider swings in temperature, moisture and air quality, and recommends keeping doors closed where possible in climates subject to extreme heat. The same sheet warns that anything making a door heavier than its maker specified, repainting included, pushes the counterbalance outside the range it was sized for. In a city where a bleached door often gets a fresh coat rather than a new skin, that is a live risk rather than a footnote.

### Why the winding bars never leave the truck

A wound torsion spring holds the door's stored energy in a few inches of cone and set screw. Sockets, screwdrivers and lengths of rebar are the three improvised tools that put people in the emergency room, because none of them stay seated when the cone slips. Tension comes out in controlled quarter turns on correctly sized bars, and only then can a cable, bearing or drum be touched. Anyone quoting this work should be able to say how the door will be secured while the shaft is unloaded.

### The repair that comes back in a year

Replacing one spring of a matched pair is half a repair. Both were wound on the same afternoon, both have absorbed the same cycles, and both have lived through the same summers, so the survivor is generally near the end of its own service life. Sizing matters just as much. Wire diameter, inside diameter, overall length, wind direction and drum size all have to answer to the measured weight of the door rather than to whatever is on the shelf. That weight can be checked directly with the counterbalance disabled, which is also how a door that has gained a coat of paint gets caught before a new spring is wound to the wrong specification.

### Grit, thinned grease and the wrong can

Fine dust is the local accelerant. Forecasters documented an outflow dust storm on August 31, 2023 that crossed most of the metro, cut visibility to a quarter mile or less, and carried winds in excess of 55 miles an hour. The regional technical memorandum on blowing dust records that such a wall can span up to 160 kilometers across and reach 2.4 kilometers high, and that blowing dust ranked third among deadly Arizona weather hazards across 1955 to 2013. Whatever crosses the yard settles on the shaft, the bearings and the coils.

Mixed with grease that summer heat has thinned, that dust turns into a grinding paste. Penetrating sprays make it worse, because they carry off what lubricant is left and leave nothing behind on the wire. The manufacturer's own instruction is the reference point, and DASMA ties regular lubrication directly to getting the rated cycle life out of a spring.

### What the visit looks like

The shaft is unloaded first, then the wire is measured and the coils counted, the door is weighed, and the cables, drums and end bearings are inspected while there is no tension on them. The matched spring or pair goes on, the drums are reset so both cables pull evenly, and the door is balanced by hand. Off the opener, it should hold roughly where it is set rather than sinking or running for the ceiling. Cost follows the specification, whether one spring or two, the state of the bearings and cables, and how hard the door was run after the break.
"""

NEW["svc_garage_door_opener_repair_lede"] = """An opener is a motor, a gear train and a circuit board living in an uncooled room through a Sonoran summer. Most calls here turn out to be the safety circuit or the door itself rather than a dead motor."""

NEW["svc_garage_door_opener_repair_body"] = """### What the federal rule requires of the head

Residential operators built on or after January 1, 1993 fall under the Consumer Product Safety Commission's rule at 16 CFR Part 1211. It is worth knowing what that buys, because several complaints that read like a broken opener are the rule working. Past the first foot of downward travel, an operator that meets an obstruction has to begin reversing within two seconds of contact and carry the door back to the fully open position. Where the control uses solid-state circuits for entrapment protection, those circuits must pass UL 991, including environmental stress testing. A mechanical switch or relay in the entrapment circuit has to survive 100,000 cycles and still do its job. If one of those parts fails in a way that costs the operator its entrapment protection, the rule says the operator must become inoperative and hold the door within one foot of the uppermost position. That clause explains a specific and frightening call: a door parked high, a head that answers nothing, and no obvious damage anywhere.

### Heat is written into the test, and into the failures

The same rule sets the temperatures its samples endure. The composite operational and cycling test runs 14 days at extremes of 158 degrees and 31 below zero. Endurance conditioning runs 14 days at 140 degrees, or 18 degrees above the control's own operating temperature, whichever is higher. Those figures describe a qualification bench, not a promise about a decade of Scottsdale afternoons. A garage attached to a house in this county spends a large share of the year unconditioned, with the head hanging in the hottest air in the room.

Electrolytic capacitors and control boards give up gradually under sustained heat, and the report that follows is consistent: the door works at dawn, then the wall button does nothing by four in the afternoon, then it works again after dark. Diagnosing that at nine in the morning tells you almost nothing. It has to be tested while the space is hot, at the unit, with the remote taken out of the question first.

### The two lenses down near the slab

DASMA's guidance on photoelectric sensor placement puts the lowest lens so its beam sits no higher than six inches above the garage floor, within six inches of the door's path, with the pair as much as 20 feet apart. Six inches off a dusty slab is exactly where blown grit, spider silk and a bumped bracket live. Hard low sun through a west-facing opening does the same thing to the receiving eye that a bag of mulch does. The same guidance asks for a monthly check: obstruct the beam during a close cycle and confirm the door returns fully open. Test that with an object, never a foot, and never by taping over a lens to force a close.

### Force limits hide mechanical drag

When a door binds, turning up the force setting is the change that makes the symptom disappear and the hazard grow. The added force lets the operator push through resistance that the reversing logic was supposed to notice. Dry rollers, a hinge gone stiff, a section rubbing the header on a hot afternoon, and a spring losing tension all read the same way at the wall button. The order of operations is to fix the drag, then set the force, then confirm the reversal.

### The trolley, the gear and the red cord

Motor noise with a motionless door is usually the trolley sitting free of its carriage after someone used the emergency release and never relatched it. Grinding with no travel at all is more often a stripped drive gear, and in a hot garage a nylon gear that has been running against a dry worm shaft wears faster than the same part would in a cooler climate. Neither of those needs a new opener.

### When replacement is the honest answer

A head with no photo eyes at all, a cracked housing, a discontinued board, or a third failure in two summers is a replacement conversation rather than another part. So is a unit whose entrapment protection cannot be verified. What decides it is the inspection and the stated price for each path, not the age printed on the label. Cost tracks the specific fault, the parts still available for the model, and whether the door itself has to be brought back into balance first.
"""

NEW["svc_off_track_garage_door_repair_lede"] = """A door off its rails, a cable off its drum, or a section rubbing steel is the urgent version of this trade. Every extra cycle bends more metal, so the first job is to secure it where it stands."""

NEW["svc_off_track_garage_door_repair_body"] = """### Stop the door where it stands

A door that looks level from the driveway can be badly unsupported from inside. The signs worth acting on are a low corner, a cable gone slack at one jamb, a roller sitting outside its rail, and the sound of a section dragging against track. At that point the load is being carried unevenly by whatever is left, and running the opener to see whether it clears is what turns a cable reset into bent sections and a damaged car. Cut power at the outlet if it can be reached without walking under the door. Leave the emergency release alone while the door is up, because pulling it transfers the whole weight to a system that is no longer holding it correctly.

### Three ways a door leaves its rails

The first is the drum. A cable that unwinds after a spring break, or after the opener dragged the door against an obstruction, leaves one side with little lift and pulls the top corner inward. The second is a seized roller, which stops rolling and starts sliding, then climbs out of the rail where the horizontal track curves. The third is geometry: a rail that has been struck, a loose lag in the jamb, or a support hanger that has shifted lets the wheel find an opening it should never have. Reading which of the three happened decides whether this is a short repair or a rebuild of the hardware on that side.

### Grit is the local accelerant

Blowing dust is a documented hazard here, not a nuisance. Forecasters recorded an outflow dust storm on August 31, 2023 that covered most of the Phoenix metro, dropped visibility to a quarter mile or less, and carried winds over 55 miles an hour. The regional study of the phenomenon puts 34 percent of Arizona blowing-dust events in June through August, with 36 percent arriving between four and six in the afternoon, and ranks the hazard third among deadly weather in the state across 1955 to 2013. That timing lines up with the hour most people open the door and drive in.

What comes in settles in the bottom of the track and on the roller stems. On its own it is harmless. Combined with lubricant that summer heat has thinned and run out of the bearing, it grinds nylon into a flat spot, and a flat-spotted wheel is the one that climbs.

### The door that bows in the sun

Insulated sections with a bonded core react to a temperature difference between the outside skin and the inside skin by bowing toward the warmer one. DASMA treats this as an inherent characteristic of the construction rather than a defect, and notes that a darker door in direct sun bows more than a white one, and that without reinforcement the bow on a 20-foot-wide door could exceed several inches. The field symptoms are exactly what gets reported on a west-facing Scottsdale garage in July: the top section rubbing the header, or a gap opening at the header while the rest of the door sits flat. Horizontal struts across the back of the section are the standard remedy, and adding one is a far smaller job than replacing a section that has been ground against the header all summer.

### What straight means in the standard

The trade standard for residential sectional doors gives numbers for this. A section tested in the horizontal position should not deflect more than one part in 120 of the door's width, and the horizontal track assembly should not deflect more than one part in 240 of the door's height. Those tolerances are why a bent rail gets measured and replaced rather than persuaded back with a hammer. A rail that has lost its shape keeps eating rollers, and the second failure usually arrives within a season of the first.

### What the visit looks like

The door gets clamped or supported before anything is loosened. Cables come off the drums with the tension controlled, damaged rollers and hinges are replaced rather than reused, the track is checked against the door and the jamb, and the drums are set so both cables take up together. Bottom brackets are treated as tensioned hardware, because they are. The door is then cycled and balanced by hand off the opener, and the reversing sensors are tested before anyone leaves.

Cost on this work depends on how many parts the derailment took with it: cables and rollers alone, a section that has been creased, a rail that has to be replaced, or a full hardware set on one side. Running the door after it came off the track is the single choice that moves this job from the low end of that range to the high end.
"""

NEW["svc_garage_door_replacement_lede"] = """Panel replacement and whole-door replacement are different decisions with different paperwork. This is also the one job on the site where the city, the code edition and the community design file all get a say."""

NEW["svc_garage_door_replacement_body"] = """### When one section is enough

A single creased bottom section on a door whose springs, track and hardware are sound is a section job. What kills that plan is usually not the steel. It is availability and finish. A profile and embossment that a manufacturer has discontinued cannot be matched, and a door that has faced south or west through a decade of Sonoran sun will not match a new section's paint even when the color code is identical. Ultraviolet exposure and heat chalk a finish gradually across the whole face, so the fresh panel reads as a repair from the street. Weighing the door before and after also matters, because DASMA warns that added weight, including paint an owner applied, can carry a door past what its counterbalance was sized for.

### The permit Scottsdale asks for

Scottsdale runs a minimum-permit category for window and door replacement at a single-family residence, issued over the counter rather than through a plan submittal. The conditions attached to it are specific: the unit goes into the existing opening, and no structural change is made. Change the opening and the job leaves that category for a formal submittal. The city's home-improvement guidance also lists what needs no permit, and that list covers replacing non-structural items such as glass in a door or window and interior doors, with an explicit exception for work affecting a pool enclosure or garage. The city fee schedule sets a floor for a single-discipline permit, and a failed reinspection is charged at the same rate, which is a reason to have the inspection scheduled by whoever did the work. A spring, cable, roller or opener repair is maintenance on existing equipment and does not sit in the replacement category at all.

### The code edition the work has to answer to

Scottsdale adopted the 2021 International Residential Code and the 2021 International Building Code by Ordinance 4550 on September 20, 2022, along with the 2020 National Electrical Code. The 2021 International Energy Conservation Code followed under Ordinance 4576 on December 6, 2022. That energy edition is why glazing matters on this trade: the minimum-permit conditions for a door replacement cap solar heat gain coefficient at 0.25 and U-factor at 0.40. If the new door carries a row of windows, leave the energy stickers on the glass until the inspector has seen them. Openers are a separate matter, governed by the federal entrapment rule rather than by the building code.

### Who actually reviews how it looks

This is the point where the brief most people arrive with turns out to be wrong. Scottsdale's Development Review Board reviews architectural and urban design for all development types except single-family homes, so the city is not passing judgment on the appearance of a house's garage door. Two narrower city rules do bite. Buildings on the Scottsdale Historic Register fall under the Historic Property Ordinance, which requires Historic Preservation Commission review and approval of exterior alterations and demolition, with a denial appealable to City Council and the process starting from a pre-application request. Separately, exterior painting inside the Environmentally Sensitive Lands and Historic Property zoning districts needs planning department approval even though no permit is issued, and the sensitive-lands overlay covers 134 square miles of desert and mountain area north and east of the Central Arizona Project canal.

Everything else about appearance is private, not municipal. In McCormick Ranch, Scottsdale Ranch, Gainey Ranch, McDowell Mountain Ranch, DC Ranch and Desert Mountain, the constraint on color, panel style, window layout and hardware comes from recorded covenants and an architectural committee. Its timeline is independent of the city's, and it is the one that most often sends a custom order back. Ask for the approved color and profile in writing before anything is fabricated.

### Licensing that covers this work

Arizona's Registrar of Contractors publishes no garage-door classification. The classification that reaches this work is carpentry: residential R-7, commercial C-7, or dual CR-7, whose scope includes hardware, millwork, and metal doors or door frames. Residential remodeling under R-61 covers projects of fifty thousand dollars or less. State law also draws the line for unlicensed work at an aggregate contract price of one thousand dollars including labor and materials, only where no permit is required, and forbids splitting a project into smaller pieces to stay under it. A permitted door replacement therefore is not handyman work by definition.

### Specifying a door for this climate

The choices that pay for themselves here are the boring ones. Lighter finishes bow less than dark ones and hold their color longer under ultraviolet load. Horizontal struts control the thermal bow that insulated sections develop on a sun-facing wall. Sealed nylon rollers survive grit better than open bearings. The bottom weatherseal and the jamb seals are consumables in this climate rather than permanent parts, because vinyl hardens and cracks under sustained sun and heat. Cost tracks door construction and insulation, whether new track and springs come with it, glazing, and whether the opening itself is being altered.
"""

NEW["SOURCES"] = """- Phoenix records for days at or above 100 and 110 degrees, the 113-day and 31-day streaks, and the 122-degree all-time high: https://www.weather.gov/psr/ExtremeTemps
- Average and extreme first and last dates for 100 and 110 degree readings in Phoenix: https://www.weather.gov/psr/FirstandLastTemperatures
- Maricopa County Excessive Heat Warning day counts and the August 31, 2023 metro dust storm with quarter-mile visibility and winds over 55 mph: https://www.weather.gov/psr/2023MonsoonSeasonReview
- Haboob dimensions, seasonal and hourly distribution of Arizona blowing-dust events, and the hazard ranking for 1955 to 2013: https://www.weather.gov/media/wrh/online_publications/TMs/TM-290.pdf
- August 22, 2024 storm reports near Scottsdale: https://www.weather.gov/psr/Aug222024
- Operator scope from January 1, 1993, two-second reversal, UL 991 testing of solid-state entrapment circuits, the 100,000-cycle switch requirement, the inoperative-within-one-foot rule, and the 158 and 140 degree conditioning temperatures: https://www.govinfo.gov/content/pkg/CFR-2015-title16-vol2/pdf/CFR-2015-title16-vol2-part1211.pdf
- Spring cycle life, keeping doors closed in extreme-heat climates, added paint weight, and lubrication: https://www.dasma.com/wp-content/uploads/pubs/TechDataSheets/CommercialResidential/TDS190.pdf
- Thermal bowing of bonded-core sections, dark colors, several inches of bow on a 20-foot door, header rubbing, and struts: https://www.dasma.com/wp-content/uploads/2021/12/TDS185.pdf
- Photoelectric sensor beam height of six inches, spacing up to 20 feet, and monthly testing: https://www.dasma.com/wp-content/uploads/2021/12/TDS364.pdf
- Section and horizontal track deflection limits of one part in 120 and one part in 240: https://www.dasma.com/wp-content/uploads/2021/01/ANSIDASMA102.pdf
- Scottsdale minimum permit for window and door replacement at a single-family residence, existing opening, and the 0.25 solar heat gain coefficient and 0.40 U-factor limits: https://eservices.scottsdaleaz.gov/bldgresources/minimumpermit
- Scottsdale no-permit list and its exception for work affecting a pool enclosure or garage, progress and final inspection, and planning approval for exterior painting in ESL and Historic Property districts: https://www.scottsdaleaz.gov/planning-development/home-improvement
- Adoption of the 2021 IRC and IBC and 2020 NEC by Ordinance 4550 on September 20, 2022, and the 2021 IECC by Ordinance 4576 on December 6, 2022: https://www.scottsdaleaz.gov/docs/default-source/scottsdaleaz/codes---ordinances/building-codes/code-adoption-history.pdf?sfvrsn=12050a91_2
- Development Review Board scope excluding single-family homes: https://www.scottsdaleaz.gov/planning-development/about-planning-and-development
- Historic Property Ordinance review of exterior alterations and demolition, and appeal to City Council: https://www.scottsdaleaz.gov/historic-preservation-program
- Environmentally Sensitive Lands overlay covering 134 square miles north and east of the Central Arizona Project canal: https://www.scottsdaleaz.gov/codes-and-ordinances/eslo
- Arizona ROC carpentry classifications R-7, C-7, CR-7 and R-61 remodeling for projects of fifty thousand dollars or less: https://roc.az.gov/license-classifications
- Unlicensed-work threshold of one thousand dollars and the bar on splitting a project: https://www.azleg.gov/ars/32/01121.htm
"""

# --- replace existing blocks -------------------------------------------------
def set_block(txt, key, body):
    pat = re.compile(r"(^## " + re.escape(key) + r"\n\n)(.*?)(?=\n## |\Z)", re.S | re.M)
    if pat.search(txt):
        return pat.sub(lambda m: m.group(1) + body.strip() + "\n\n", txt, count=1)
    return txt + "\n## " + key + "\n\n" + body.strip() + "\n"

order = ["symptom_1", "symptom_2", "symptom_3", "symptom_4",
         "services_summary", "services_pick_head", "crosslink_head"]
for k in order:
    txt = set_block(txt, k, NEW[k])

for svc in ["garage_door_spring_repair", "garage_door_opener_repair",
            "off_track_garage_door_repair", "garage_door_replacement"]:
    for suf in ["lede", "body"]:
        k = f"svc_{svc}_{suf}"
        txt = set_block(txt, k, NEW[k])

txt = set_block(txt, "SOURCES", NEW["SOURCES"])
cm.write_text(txt)

sj = P / "site.json"
s = json.loads(sj.read_text())
s["phase"] = 2
sj.write_text(json.dumps(s, indent=2) + "\n")

for k in order + [f"svc_{s2}_{suf}" for s2 in ["garage_door_spring_repair", "garage_door_opener_repair", "off_track_garage_door_repair", "garage_door_replacement"] for suf in ["lede", "body"]]:
    print(k, len(NEW[k].split()))
