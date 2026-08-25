import re, pathlib

SITE = pathlib.Path("/home/user/workspace/local-sites/sites/parkergaragedoorrepairexperts.com")
p = SITE / "copy.md"
txt = p.read_text()

SYMPTOMS = {
"symptom_1": """That bang was almost certainly a torsion spring letting go above the opening. The opener did not weaken overnight; the counterbalance that carried the door's weight is gone. From the floor, look along the steel shaft for a clean gap in one coil. Leave the shaft, the winding cones, the cables and the bottom brackets alone. Unplug the operator so nobody presses a button out of habit, and let the door stay down.""",

"symptom_2": """The door is obeying its own safety circuit rather than failing. Two photo eyes sit near the slab facing each other, and anything crossing that beam ends the close cycle. Look at the indicator lamps, wipe each lens dry, and move whatever leans against the brackets. Never tape a wall button down or twist an eye off its aim to force the door shut.""",

"symptom_3": """A corner sitting low means the door is no longer traveling as one supported unit. A cable has left its drum, a roller has jumped the rail, or something has bent the track. Every further press of the button spreads that damage further. Stop operating it, keep people and vehicles out from under the opening, and leave a slack cable hanging exactly where it is.""",

"symptom_4": """Noise without movement usually means the two halves have come apart. With the door flat on the slab, watch the rail while somebody presses the wall control. A rail that travels alone says the carriage released, often from a yanked emergency cord. A motor that only hums while the rail sits still points instead at a drive gear or a capacitor.""",
}

NEW = {}

NEW["services_summary"] = """Four separate jobs share one search phrase in Parker, and sending the wrong one up a driveway is how a single failure becomes two appointments. Spring repair restores the counterbalance that makes a double door liftable by hand. Opener work covers drive gears, boards, capacitors, travel settings and the entrapment sensors federal rules require. Off-track and cable repair covers drums that unspooled, rollers out of the rail, and vertical track knocked out of plumb by a windstorm. Door and panel replacement is the only one of the four that reaches the Town's permit counter, because Parker requires a permit for every door replacement."""

NEW["services_pick_head"] = """Start with the failure that matches your door"""

NEW["crosslink_head"] = """Other work on this door"""

NEW["svc_garage_door_spring_repair_lede"] = """The counterbalance above the opening does the lifting, and when it parts a double door becomes several hundred pounds of dead steel. This is the most common failure in a Parker garage and the one most likely to hurt somebody attempting it alone."""

NEW["svc_garage_door_spring_repair_body"] = """### How you know the counterbalance is what let go

A broken torsion spring announces itself, often at two in the morning with nobody near the garage, because a fatigue crack finishes on its own schedule rather than during use. What follows barely varies. The operator strains, raises the door two inches, and quits, or the door will not budge under a hand that expects it to feel almost weightless. Look along the steel shaft above the opening from the floor rather than from a ladder. A failed coil shows a clean gap where the wire parted, with both halves relaxed and sitting slightly apart on the shaft.

### What a Parker builder hung above your opening

The Town spans 22.4 square miles and counted roughly 72,147 residents inside its boundaries at the start of 2026, and the median house here was finished in 2003. Housing that arrives in phases wears out in phases. On most streets in Canterberry Crossing, Clarke Farms, Cottonwood and Stonegate the working assumption is a sectional steel door on a single torsion set chosen to a builder's cost target, with the identical package repeating down the block. Anthology's newer sections and the larger custom openings out toward The Pinery pull in opposite directions, which is why wire sizes get discussed before a truck is loaded.

### Winding bars, and nothing else that happens to be in the garage

The surviving half of a broken spring is still partly loaded, and a two-spring shaft with one break holds a serious amount of stored energy. Winding bars sized to the cone are the only correct tool for releasing it. Screwdrivers, rebar and hex keys slip out under load and travel across the garage at speed. If a spring has gone, cut power to the operator, leave the door resting on the slab, and keep the bay clear until somebody with the right bars arrives.

### The weight question that follows a replacement door

Springs are sized to the door hanging there now, not to the one the builder installed. Insulated sections, a row of windows, extra horizontal struts and heavier gauge steel all raise the load the counterbalance carries. The industry body that publishes standards for this hardware warns that reinforcement a manufacturer never specified adds weight and can cause tracks or other components to fail. It also warns that fitting a spring without confirming the door's counterbalance requirement shortens the service life of the door assembly and of the motor. Paint and anything bolted to a section count as well, and weighing the door with the counterbalance released settles the argument in a minute.

### Cycle counts, not calendar years, at 5,900 feet

The published sectional door standard defines one cycle as travel from closed to fully open and back to closed again, and that is the unit spring life is measured in. Usage therefore does the deciding. A garage that serves as the household's real front entrance works through a rating years ahead of one that opens on weekends. Parker's own adopted design table summarizes the environment those coils live in: a winter design temperature of 3 degrees, a summer figure of 90, a daily range classed high, and an altitude of 5,900 feet. Federal guidance on ultraviolet exposure puts the increase at roughly two percent for every thousand feet of elevation, so seals, bushings and plastic parts around the shaft age faster than a sea-level manual assumes. Lubricant that has dried out of the bearing plates makes the spring work harder on every one of those cycles.

### What the visit looks like on site

Measurements come first. Wire diameter, inside diameter, overall length and wind direction get read from the failed spring or its stamped cone, then checked against the door's actual height and weight. Both springs come off a two-spring shaft, because the survivor has logged the same cycles in the same air and is no bargain to keep. Cables get inspected with the tension released, since a spring rarely lets go without scoring one on the way down. Drums are reseated, new springs are wound to the turn count for the door height, and the balance check happens before the operator is reconnected. Released from the opener, the door should hold still near waist height rather than drifting down or climbing.

### Where the money goes on a spring job

This is a parts-and-labor repair with a reasonably predictable range along the Front Range, and the figure gets settled before anything is wound. What moves it is spring count, wire size, whether cables, bearings or drums are renewed at the same time, and whether the appointment is a weekday morning or a Sunday night. A higher cycle rating is the upgrade that repays itself on the door a family uses daily. Researched Parker ranges sit on the pricing page beside the Town's published fees, so the shape of a fair number is visible before anyone knocks."""

NEW["svc_garage_door_opener_repair_lede"] = """Two unrelated complaints both arrive labeled as opener trouble: the door that retreats to the ceiling on the way down, and the head that runs cheerfully while the door sits still. Neither one usually means buying a motor."""

NEW["svc_garage_door_opener_repair_body"] = """### The door that refuses to finish closing

That behavior is entrapment protection working, and the federal rule is specific about how it must behave. Residential operators built for sale in this country since the start of 1993 have to begin reversing within two seconds of contact with an obstruction and then carry the door back to the full open position. The same rule requires the head to check for its secondary sensing device at least once during every close cycle. Lose a photo eye to a cut wire, a short, or an interrupted wireless signal, and a closing door must open, while an open door may not travel more than a foot below the top. So a door that comes down a hand's width and climbs back is frequently a sensor circuit reporting itself.

### What to look at before anyone is dispatched

Begin at the two eyes near the slab. Wipe both lenses, watch for a steady indicator lamp, and move the snow shovel, recycling bin or bag of ice melt leaning against a bracket. The federal test procedure places its obstruction at three points across the opening, a foot in from each end and at the midpoint, which is a sensible sweep for a homeowner as well. If the beam is clean and lit and the door still refuses, the resistance is in the door itself. Raising the close-force setting hides that resistance and blunts the protection that just did its job.

### Heads that lose track of where the door is

Some operators watch door position and some only watch the clock. A design that monitors position has to do it in increments no greater than an inch and reverse when travel departs from its learned profile. A design that does not monitor position has to reverse if the lower limit device is never reached within thirty seconds of starting down. That distinction explains two very different complaints on the same street. One door stops at a random height every third attempt; another closes fully and then reverses in the last inch. Neither is cured by a new remote.

### Altitude, temperature swing and the electronics on the ceiling

Parker's adopted design figures put the outdoor winter design temperature at 3 degrees and the summer figure at 90, with the daily range classed high. A logic board screwed to an uninsulated garage ceiling passes through that spread twice a day, year after year. The federal endurance procedure for these products conditions them for fourteen days at 140 degrees and impact-tests outdoor devices after three hours near 31 degrees below zero, which indicates what the hardware is expected to survive. In practice the symptoms turn strange rather than obvious. A head answers every button at breakfast and ignores the remote by late afternoon, limits forget themselves, a unit reboots in mid-travel. Boards, receivers and capacitors are separate parts on most residential units, so heat and cold damage is usually a component swap.

### Wind, outages and the release cord

Downslope windstorms take the grid down along the Front Range. During a December 2025 event the weather service logged a 102 mph gust at Rocky Flats, closed Highway 93, and recorded schools canceled for planned power outages. What happens next in a garage is predictable. Somebody pulls the emergency cord to get a car out, the trolley never re-engages, and the motor then runs an entire cycle in an empty rail. Reconnecting it takes seconds. On a raised door, or a door whose spring has already broken, that cord hands the full weight to gravity, so it belongs to a door resting on the slab. The trade guidance is also explicit that doors should not be operated while a high wind event is underway.

### When a new head is the honest answer

Replacement earns its place when a unit predates external entrapment protection, when the board or gear is no longer manufactured, when the housing is cracked, or when a second failure would cost more than the difference. It is not a way around balancing a door. A motor coupled to an unbalanced door inherits the same problem and wears out early. Battery backup is worth discussing in a town where wind events pull the power down, though that is an upgrade being offered rather than a repair anybody needs.

### What the work runs in this market

A gear kit, a capacitor or a sensor pair is a modest parts-and-labor repair. A full head swap is a larger number, and drive type moves it further: chain, belt and wall-mount jackshaft units all price differently, with the jackshaft earning its premium where headroom is short. Diagnosis comes before the figure and the figure comes before the tools, because the same complaint can be a five-dollar alignment or a new motor. Researched Parker ranges for each of those paths are laid out on the pricing page."""

NEW["svc_off_track_garage_door_repair_lede"] = """A door hanging crooked, a cable off its drum or a roller out of the rail is no longer a supported assembly. One more press of the button is what turns a contained repair into a replacement project."""

NEW["svc_off_track_garage_door_repair_body"] = """### Reading a door that has come out of line

One corner sits lower than the other, a gap opens along the top section, or the door binds at the same point on every pass. Look for a cable hanging in a loose loop at one drum, a roller stem clear of the track, and the place where vertical rail curves into the horizontal run. That curve is where most rollers leave, because the load changes direction there. Do not lift one side by hand, pull on slack cable, or leave a vehicle parked under a door in that condition.

### The three ordinary causes, and the order they arrive in

A spring lets go, the door drops unevenly, and one cable unspools its drum into a loose coil. A roller stem wears or a nylon wheel cracks until it slides instead of rolling, then climbs out at the curve. Or a bumper nudges the vertical track at the jamb by a quarter inch, which is enough to pop a roller at the same spot on every pass until somebody finds the bend. The sequence also runs backward, since bent rail can cut a cable and a failed cable can bend rail.

### The Parker version of this failure is wind

Here is where a Front Range garage differs from one in a sheltered inland market. Warm dry Chinook winds pour down the eastern slopes and, in the weather service's own wording, can exceed 100 mph in extreme cases. A cold high crossing the Rockies produces a Bora off the same slopes that can do likewise. Measurements near this town support the warning. On May 6, 2024 the weather service logged gusts of 79 and 78 mph near Greenland in Douglas County, along with a 65 knot gust at Centennial Airport that overturned one parked aircraft and damaged eleven more. A thunderstorm gust of 66 knots was measured at Highlands Ranch on June 22, 2023, and an automated station near Greenland reached 69 mph in October 2022.

### Why the largest opening in the house tries to lift itself

Federal mitigation guidance is blunt about the geometry. A garage door is one of the largest openings in a building, and its size leaves it vulnerable to being blown in, pulled out, or twisted off its tracks. The trade data sheet on securing doors during wind events explains the mechanism precisely. Vertical track is deliberately tilted back so the sections do not rub in normal use, and the top rollers rest in the curved portion of the track when the door is shut. Wind pressure pushes the sections against that tilted track, and the geometry converts part of the push into an upward force. The harder it blows, the harder the door works to open itself. After Hurricane Andrew, investigators found doors along the storm path that the wind had opened with no help from anyone inside.

### Hail, and the inspection sequence that actually matters

Douglas County collects large stones. Storm records list hail of one and three-quarter inches at Parker on August 7, 2018, two inches on July 4, 2019, and one and three-quarter inches again on June 9, 2024, with two and a half inch reports at Castle Rock in June 2019. The published post-event checklist for this hardware sets an order of inspection, and the panel face is not the top of it. Door alignment comes first, then the opening frame and how the jambs and header are attached to the structure, then the track for loose fasteners, twisting, or rails that have opened up, then rollers, brackets and hinges. Where stress or fatigue has compromised the system's ability to survive another event, that written assessment is what an insurer needs to see.

### What the repair involves

The door gets clamped and blocked so it cannot travel before anything is loosened. Load comes off in the correct order, sections return to the rails one at a time, and damaged rollers, hinges and brackets are replaced rather than persuaded back into shape. Both cables are respooled to matched tension so the drums start and finish together, and vertical track is checked for plumb and spacing against the jamb. The counterbalance gets examined as a cause rather than a coincidence. Then the door is run by hand, and only afterward is the operator reconnected and its travel reset.

### What it costs to put a door back in its tracks

The failed part sets the floor and the collateral damage sets the ceiling. A single roller and a short length of rail is a small job with a narrow range. A cable that unspooled and racked the whole assembly brings in hinges, brackets, sometimes a section, and the counterbalance work that started it. Storm visits carry one extra element, which is the written assessment a homeowner may need for a claim. Ranges for each of those cases are broken out on the pricing page."""

NEW["svc_garage_door_replacement_lede"] = """This is the only one of the four jobs that begins at the Town's permit counter. In Parker it is also the job where wind rating, association design rules and a heavier door all show up in the same conversation."""

NEW["svc_garage_door_replacement_body"] = """### When a section is the repair and when the door is the repair

A shallow dent in a steel skin changes nothing mechanical and can wait for an adjuster. A section that has lost its stiffness is a different matter, and so is a wood door with rot along the bottom rail or an assembly that has been racked hard. Availability decides many of these calls. Matching one section on a discontinued profile can cost more than that money would contribute toward a new door, so the count of sound sections and the status of the profile are the first two questions asked.

### The permit is the Town's, not the County's

Two jurisdictions publish design criteria for this area, which is where confusion starts. Douglas County's building codes are adopted and enforced in unincorporated Douglas County. Inside town limits the Town of Parker's Building Division holds the file, applications are submitted through the Town's online eTRAKiT system, and the Town lists all window and door replacements among work that requires a permit. Town Council adopted the 2024 edition of the international codes, in effect as of June 30, 2026, with the 2023 electrical code running to the end of that year. An address a mile outside the boundary is a county permit instead, and establishing which applies belongs at the start rather than after a door is ordered.

### Registration, and why the crew's paperwork becomes your problem

Parker issues permits only to a registered contractor or that contractor's authorized representative. The registration classes appear in the municipal code, and Class D covers garages, alterations, remodels and decks, which is where a door replacement lands. Registrations expire a year from issue, and no permit may be pulled or work continued until one is renewed. A property owner may act as owner-builder on their own residence, though the code allows that for a single dwelling in any twelve-month period. A crew that cannot produce current registration cannot file the job, whatever number appears on its estimate.

### What the wind figures mean for the door you order

The Town's residential design table lists a 115 mph wind speed, a 30 psf ground snow load and an altitude of 5,900 feet. Exposure is where it gets interesting. That table names exposure category B with a footnote returning the question to a site-specific determination, while the Town's building code amendment states that exposure C shall be used for the design of all structures in Parker. The distinction is not academic. Trade guidance on exposure categories notes that the category alone can change the design pressure on a vehicular door by thirty percent or more. Exposure also shifts as a subdivision fills in, since the code bases it on the site conditions that will exist once adjacent houses have been built, which describes half the neighborhoods in this town.

### The label to insist on, and the reinforcement to refuse

The residential code requires a garage door to be tested against a recognized static pressure standard and to carry a permanent label from its manufacturer. That label identifies the maker, the model or series, the positive and negative design wind pressure ratings, the installation drawing reference and the test standard applied. Two consequences follow. Not every door sold is wind-load rated, and an unrated door carries no label at all. The rating is also expressed in pounds per square foot rather than in miles per hour, so a wind speed quoted at the door is the wrong unit for the question. Homemade stiffening is the other half of this. Reinforcement the manufacturer never specified adds weight and can cause tracks or other components to fail, a vertical post transmits load into the header and the slab, and a qualified design professional should look at the structure before one goes in. Parking a car against a door is specifically discouraged. The building official remains the final authority on what an opening needs.

### Why this opening is the one the wind finds

Mitigation guidance describes a garage door as one of the largest openings in a building and generally the largest single product in a house. Losing it has consequences well past the door. A mitigation assessment team report cited garage door damage as a key contributor to pressurization inside a building that ended with the roof assembly blowing off. The bracing recommended for a storm works by shortening the unbraced span of the door, anchored into the garage slab and the ceiling framing above. That is also why the jamb connection deserves as much attention as the leaf. Anchoring a door's jambs to the framing is an engineered schedule, with minimum fastener spacings in concrete and masonry and published allowable loads for each anchor.

### What an association can and cannot require in Colorado

Parker is association-heavy newer construction, and the Town's own homeowner resources note that an association may ask for a plan showing the proposed improvement. State law draws the boundaries around that. Under the common interest ownership act, a decision approving or denying an owner's application for an architectural change must follow the standards and procedures in the declaration or in duly adopted rules, and may not be made arbitrarily or capriciously. The declaration sits at the top of the governing document hierarchy, above bylaws, policies and design guidelines. The statute also lists what an association may not prohibit, including flags, xeriscape, rain barrels, renewable energy devices and electric vehicle charging. Garage door appearance is not on that list, so panel style, color and window layout remain inside the association's design authority, while the process used to decide has to be the published one.

### What a replacement costs, and what a national average leaves out

Insulation level, section style, window inserts, hardware grade and door width move the total most, and haul-away belongs on the estimate as its own line. A wind-rated door with additional struts weighs more than the one coming down, so springs, drums and occasionally the opener bracket are part of the same job instead of a surprise a month later. Where framing changes, the Town's permit, plan review and construction use tax figures go on top, and those are itemized on the pricing page. Lead time is the factor an online average never carries, because a specific color and window pattern is ordered rather than stocked."""

NEW["SOURCES"] = """Every local claim on this site traces to a page that was read and quoted.

- Town elevation of 5,900 feet, 22.4 square miles and about 72,147 residents inside town limits as of January 1, 2026: https://www.parkerco.gov/159/About-Parker
- Adoption of the 2024 edition of the international codes, in effect June 30, 2026, and the 2023 electrical code through December 31, 2026: https://www.parkerco.gov/445/Building-Codes
- Residential design criteria table with the 115 mph wind speed, 30 psf ground snow load, exposure category B with a site-specific footnote, altitude 5,900, winter design temperature 3 degrees, summer 90 and daily range H: https://www.parkerco.gov/DocumentCenter/View/22597
- Town building code amendment requiring exposure C for the design of all structures in Parker, and the 30 psf snow load with drifting: https://www.parkerco.gov/DocumentCenter/View/22590
- Permits required for all window and door replacements: https://www.parkerco.gov/451/When-Permits-are-Required
- Applications submitted through the Town's eTRAKiT system and contractor licensing in the Town of Parker: https://www.parkerco.gov/457/Obtaining-Permits
- Permits issued only to a registered contractor or an authorized representative, the Class D scope covering garages and alterations, one-year registrations and the owner-builder limit of one dwelling per twelve months, Parker Municipal Code Chapter 11.19: https://library.municode.com/co/parker/codes/municipal_code?nodeId=TIT11BUCO_CH11.19CORE
- An association may require a plan showing proposed improvements: https://www.parkerco.gov/2361/HOA-Resources
- Douglas County building codes adopted and enforced in unincorporated Douglas County: https://www.douglas.co.us/building-division/
- County design information, 115 mph ultimate wind speed and exposure C below 7,000 feet: https://www.douglas.co.us/building-division/design-information/
- Chinook and Bora downslope winds exceeding 100 mph in extreme cases along the eastern slopes: https://www.weather.gov/bou/highwind
- Gusts of 79 and 78 mph near Greenland in Douglas County and the 65 knot gust at Centennial Airport on May 6, 2024: https://www.ncei.noaa.gov/stormevents/eventdetails.jsp?id=1166101
- The 66 knot thunderstorm gust measured at Highlands Ranch on June 22, 2023: https://www.ncei.noaa.gov/stormevents/eventdetails.jsp?id=1108974
- The 69 mph peak gust at an automated station near Greenland in October 2022: https://www.ncei.noaa.gov/stormevents/eventdetails.jsp?id=1061286
- The 102 mph gust at Rocky Flats, the closure of Highway 93 and schools canceled for planned power outages in December 2025: https://www.ncei.noaa.gov/stormevents/eventdetails.jsp?id=1300862
- Hail of 1.75 inches at Parker on August 7, 2018: https://www.ncei.noaa.gov/stormevents/eventdetails.jsp?id=770278
- Hail of 2.00 inches at Parker on July 4, 2019: https://www.ncei.noaa.gov/stormevents/eventdetails.jsp?id=824724
- Hail of 1.75 inches at Parker on June 9, 2024: https://www.ncei.noaa.gov/stormevents/eventdetails.jsp?id=1175874
- Hail of 2.50 inches at Castle Rock on June 8, 2019: https://www.ncei.noaa.gov/stormevents/eventdetails.jsp?id=818497
- Ultraviolet radiation increasing about two percent per 1,000 feet of elevation: https://www.epa.gov/sites/default/files/documents/uviguide.pdf
- Garage doors as one of the largest openings in a building, vulnerability to being blown in, pulled out or twisted off the tracks, and bracing that reduces the unbraced length of the door, FEMA P-2181 Fact Sheet 3.2: https://www.fema.gov/sites/default/files/documents/fema_p-2181-fact-sheet-3-2-wall-openings.pdf
- Garage doors as the largest product in a single-family home, and the mitigation assessment team finding on cascading pressurization and roof blow-off: https://www.iccsafe.org/building-safety-journal/bsj-technical/garage-door-provisions-in-the-international-residential-code/
- Both positive and negative pressure ratings, the warning against reinforcement not specified by the manufacturer, and the advice against parking a vehicle against a door or operating one during a high wind event, DASMA Technical Data Sheet 152: https://www.dasma.com/wp-content/uploads/2024/01/TDS152.pdf
- Vertical posts transmitting wind load into the header and floor, and the need for a qualified design professional, DASMA Technical Data Sheet 153: https://www.dasma.com/wp-content/uploads/2022/05/TDS153.pdf
- Tilted vertical track, top rollers in the curved section, the resulting upward force, and the post-Hurricane Andrew finding that doors were opened by the wind, DASMA Technical Data Sheet 192: https://www.dasma.com/wp-content/uploads/2021/12/TDS192.pdf
- Exposure category alone changing design pressure by 30 percent or more, and exposure based on site conditions once adjacent structures are built, DASMA Technical Data Sheet 193: https://www.dasma.com/wp-content/uploads/2022/03/TDS193.pdf
- Jamb anchorage schedules, minimum fastener spacing in concrete and masonry, and the requirement for a registered professional engineer on supporting structural elements, DASMA Technical Data Sheet 161: https://www.dasma.com/wp-content/uploads/2024/05/TDS-161.pdf
- The wind load label contents, testing to ASTM E330 or ANSI/DASMA 108, ratings stated in pounds per square foot rather than miles per hour, unrated doors carrying no label, and the building official as final authority, DASMA Technical Data Sheet 1502: https://www.dasma.com/wp-content/uploads/2025/01/TDS-1502.pdf
- Reinforcement weight, counterbalance matching and its effect on the life of the door assembly and the motor, DASMA Technical Data Sheet 190: https://www.dasma.com/wp-content/uploads/pubs/TechDataSheets/CommercialResidential/TDS190.pdf
- The post-event inspection order covering door alignment, opening frame, track, rollers and hinges, and forwarding a fatigue assessment to an insurer, DASMA Technical Data Sheets 174 and 175: https://www.dasma.com/wp-content/uploads/2022/09/TDS174.pdf
- Definition of one door cycle, ANSI/DASMA 102: https://www.dasma.com/wp-content/uploads/2021/01/ANSIDASMA102.pdf
- Reversal within two seconds, the one foot limit near the top, monitoring the secondary device once per close cycle, position monitoring in one inch increments, the thirty second lower limit rule, the three obstruction positions across the opening, and the endurance conditioning at 140 degrees and cold impact near 31 degrees below zero, 16 CFR Part 1211: https://www.govinfo.gov/content/pkg/CFR-2025-title16-vol2/pdf/CFR-2025-title16-vol2-part1211.pdf
- Architectural approval decisions that may not be arbitrary or capricious under C.R.S. 38-33.3-302(3)(b), and the governing document hierarchy placing the declaration highest: https://dre.colorado.gov/hoa-frequently-asked-questions
- The statutory list of things an association may not prohibit, which does not include garage door appearance: https://content.leg.colorado.gov/sites/default/files/homeowners-rights-in-ccioa.pdf"""


def replace_block(text, name, body):
    pat = re.compile(r"(## " + re.escape(name) + r"\n\n)(.*?)(?=\n## |\Z)", re.S)
    m = pat.search(text)
    assert m, name
    return text[:m.start(2)] + body.strip() + "\n\n" + text[m.end(2):]


for k, v in SYMPTOMS.items():
    txt = replace_block(txt, k, v)

# insert services_summary before about_summary
txt = txt.replace("## about_summary\n", "## services_summary\n\n" + NEW["services_summary"] + "\n\n## about_summary\n", 1)

# insert svc blocks before urgency_bullet
svc = ""
for key in ["garage_door_spring_repair", "garage_door_opener_repair",
            "off_track_garage_door_repair", "garage_door_replacement"]:
    svc += "## svc_%s_lede\n\n%s\n\n## svc_%s_body\n\n%s\n\n" % (
        key, NEW["svc_%s_lede" % key].strip(), key, NEW["svc_%s_body" % key].strip())
txt = txt.replace("## urgency_bullet\n", svc + "## urgency_bullet\n", 1)

# heads before pricing_lede
txt = txt.replace("## pricing_lede\n",
                  "## services_pick_head\n\n%s\n\n## crosslink_head\n\n%s\n\n## pricing_lede\n"
                  % (NEW["services_pick_head"], NEW["crosslink_head"]), 1)

# sources at end
txt = txt.rstrip() + "\n\n## SOURCES\n\n" + NEW["SOURCES"].strip() + "\n"

p.write_text(txt)
print("written", len(txt.split()))
