#!/usr/bin/env python3
"""Phase 2 edit for coloradospringsfurnacerepair.com: shrink symptoms, add
services + four service pages, trim pricing prose, flip phase."""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
SITE = ROOT / "sites" / "coloradospringsfurnacerepair.com"
COPY = SITE / "copy.md"

text = COPY.read_text()

# --- split into blocks, preserving the header comment ---------------------
parts = re.split(r"^## (\S+)\s*$", text, flags=re.M)
head = parts[0]
blocks = {}
order = []
for i in range(1, len(parts), 2):
    key = parts[i]
    blocks[key] = parts[i + 1].strip("\n")
    order.append(key)

NEW = {}

NEW["symptom_1"] = """Confirm the thermostat sits in heat mode, is set above room temperature, and still has a live display. Then stand near the furnace and note what follows the request: silence, a draft fan, a clicking start attempt, a short flame, or a status light. Write that order down. Skip the repeated breaker resets, because each one wipes out the pattern a technician needs."""

NEW["symptom_2"] = """Either the burners lit or they never did, and that one fact splits the diagnosis in half. From a safe distance, watch whether the draft fan spins up, whether the igniter glows, whether flame appears, and how many seconds it survives before the cabinet goes quiet. Count the attempts before lockout. Keep hands away from burners, wiring, and the vent connection."""

NEW["symptom_3"] = """Check the fan switch first. Left on, it pushes room-temperature air between heat cycles and imitates a breakdown. If the switch reads auto and the supply air is still cool, the burners either never lit or dropped out early while the fan kept cooling the heat exchanger. Look at the filter, leave every panel closed, and note which rooms went cold."""

NEW["symptom_4"] = """Timing narrows a noise down faster than the noise itself. Note whether it arrives with the fan, during light-off, mid-burn, or at shutdown, and which cabinet or duct area seems to carry it. A squeal or scrape that begins exactly as air starts moving points toward the blower assembly. Shut the system off if a bang comes with soot or a gas odor."""

NEW["services_summary"] = """Four jobs share one search box in this market, and choosing wrong buys a second visit. Furnace repair is the wide fault-finding call: heat demand, draft, ignition, airflow, safety circuits, venting. Ignition repair narrows to lighting the burners and proving that flame exists. Blower motor repair begins once heat is being made but not delivered. A tune-up is measurement and cleaning on equipment that still runs safely. The overlap is real at 6,035 feet: a loaded filter trips a limit and reads like an ignition fault, and a furnace that was never derated for this elevation short cycles in a way that mimics a failing control board."""

NEW["services_pick_head"] = """Start from what the equipment is actually doing"""

NEW["crosslink_head"] = """Facing a different furnace fault?"""

# ---------------------------------------------------------------- furnace repair
NEW["svc_furnace_repair_lede"] = """A repair call answers one question before it touches a part: where did this furnace stop? Before draft, at light-off, while proving flame, or after a limit opened. At 6,035 feet the gas input the furnace is allowed to burn belongs in that answer."""

NEW["svc_furnace_repair_body"] = """### Reading the shutdown in the order it happened

A gas furnace is a sequence, and every sequence has a place where it quits. The draft inducer spins, a pressure switch confirms it, the igniter heats, the gas valve opens, burners establish, a sensor proves the flame is real, and only then does the blower push warm air into the ducts. Naming the step that failed is most of the diagnosis. Silence after a heat request sends testing to power, the door interlock and the thermostat circuit. A start that dies four seconds after light-off sends it to flame proving. Heat that never reaches the far bedroom sends it to airflow and duct delivery.

A blinking board light is a pointer, not a verdict. It says which circuit reported trouble; it does not say whether a switch failed or was telling the truth about a blocked drain.

### What 6,035 feet does to the gas input

The city's own budget profile puts the elevation at 6,035 feet. Fuel gas code language allows an appliance to use its nameplate input only to 2,000 feet. Above that, input must be reduced: four percent for each 1,000 feet above sea level before equipment is selected, or by a method the building department accepts, or as the manufacturer's instructions direct. Run the first version at this elevation and roughly a quarter of the nameplate rating disappears, so an 80,000 Btu-per-hour furnace is really delivering closer to 61,000. Several manufacturers write the rule as four percent per 1,000 feet above 2,000 feet, which lands nearer 67,000 on the same cabinet.

That gap matters when someone sized a replacement off square footage and a sea-level sticker. The result is an oversized furnace that satisfies the thermostat in short bursts, and short bursts are hard on igniters, inducers and control boards. Rheem's high altitude kit instructions add a second wrinkle worth knowing here: on ninety-plus furnaces installed above 5,000 feet, the pressure switch is supposed to be exchanged for the high altitude switch, and burner orifices may need changing depending on elevation and the heating value of the gas.

### The mechanical room that cannot breathe

Combustion needs air, and thin air carries less oxygen per cubic foot. Where the leakage rate of a house is unknown, the standard indoor-air calculation gives 50 cubic feet of room volume for every 1,000 Btu per hour of appliance input. Older homes usually satisfied that by accident. A newer or tightly sealed house frequently cannot, which is why the code turns to outdoor openings sized on input and count, or to a mechanical supply of at least 0.35 cubic feet per minute per 1,000 Btu per hour, interlocked to the equipment.

The regional building department lists a mechanical room without combustion air among the five mistakes its inspectors see most, and ties it directly to venting and carbon monoxide trouble. Federal researchers make the same point with numbers: a 2,000-square-foot house at 18,000 cubic feet, moderately tight, running one 300-cubic-foot-per-minute exhaust fan, can be pulled negative enough that no natural draft appliance drafts safely. A range hood is not a furnace problem until the furnace shares its air.

### A cracked heat exchanger needs proof, not a story

Condemning an exchanger is a four-figure conversation, so it deserves evidence: a photograph through a scope, a marked location, a measured temperature rise against the data plate, a combustion reading in parts per million. Manufacturer literature explains the failure path plainly. When input is not reduced for altitude, combustion turns inefficient or incomplete and excessive temperature rise can bring on premature heat exchanger failure. The same documents forbid derating by dialing manifold pressure below the nameplate value, because low air density and low pressure together stop the orifice from pulling in enough primary air.

### Carbon monoxide is its own decision

Colorado Springs Utilities describes a healthy burner flame as roughly ninety percent blue and calls yellow a sign the appliance is not working right. If an alarm sounds or people feel sick, the guidance is to get outside and call 911 or the utility's around-the-clock line, then leave the equipment alone until the source is found. The building department requires a working detector on any level with a bedroom whenever mechanical equipment is installed or replaced.

### When a repair turns into a replacement

Permits here do not come from a city office. The Pikes Peak Regional Building Department issues them for this city, unincorporated El Paso County, Fountain, Manitou Springs, Monument, Palmer Lake, Green Mountain Falls and Woodland Park over in Teller County. Furnaces sit on its list of work requiring a permit. A homeowner may pull one only for a residence they own and occupy, never for a rental and never when a contractor performs the work; a hired contractor has to be licensed and registered with the department and in good standing.

### What the visit looks like

Clear a path to the equipment, the filter rack and the thermostat. Expect the technician to run a controlled heat call, watch the sequence, measure rather than guess, and check the filter, returns, accessible venting and drainage before naming a part. You should hear what failed, what caused it, and the repair figure before anything is opened up further."""

# ------------------------------------------------------------------- tune up
NEW["svc_furnace_tune_up_lede"] = """A useful tune-up produces readings, not reassurance. Temperature rise against the data plate, manifold pressure, flame signal, draft, filter and return condition, and whether this cabinet was ever set up for the elevation it operates at."""

NEW["svc_furnace_tune_up_body"] = """### What a measured visit records

Maintenance earns its keep when it leaves numbers behind. The plate on the furnace states an allowable temperature rise across the heat exchanger, and the reading either falls inside that window or explains itself: a loaded filter, a closed return, a blower speed tap chosen for cooling and never revisited. Manifold pressure gets checked against the plate rather than adjusted by feel. Flame signal, draft, burner appearance, wiring, drainage on condensing equipment and the condition of accessible vent joints all belong on the same sheet.

Federal guidance for putting gas equipment into service lists the same steps a good annual visit repeats: adjust the input, including the derate for high altitude, adjust primary air, then check safety shutoffs, ignition devices, limit controls and draft. That order is worth noticing. The safety devices come after the combustion setup, because a furnace burning wrong will keep tripping devices that are working correctly.

### Cold that shows up in one evening

This is a cold, dry climate zone rather than a mild one, and the winter arrives in pulses. Normals for 1991 through 2020 put January at a 31.7-degree mean, with a normal low of 18.5 and a normal high of 45. December averages the same as January. Annual snowfall runs 32.5 inches on 15.91 inches of total precipitation, so a long stretch of dry cold is more typical here than deep snow cover.

The record book is where equipment gets tested. December 9, 1919 bottomed out at 27 below zero at the Colorado Springs station, and the January column holds two readings of 26 below, in 1913 and again in 1951. A furnace that is marginal in October will not stay marginal through a night like that, which is the practical argument for doing this work before the first hard freeze rather than after.

### Wind and hail leave marks on the vent

Westerly downslope flow is a fact of life against the foothills. The Pueblo forecast office writes that warm, dry Chinook winds can exceed 100 mph in extreme cases and that gusts of 60 to near 100 mph occur in and near the foothills in and around this city, with cold-season Bora events capable of similar numbers. Regional structural criteria assume a 130 mph ultimate wind speed and require the more punishing Exposure C category across the area, which tells you how routine strong wind is here.

The municipal utility adds hail to the list: after a hailstorm, have someone check the appliance vent cap, since a damaged cap can make an appliance vent improperly and raise indoor carbon monoxide. Accessible terminations, supports, screens and slope are all cheaper to correct during a scheduled visit than during a no-heat call in January.

### Depressurization, and the radon fan in the same room

Basements here often hold two systems that both move air: the furnace, and a radon fan. El Paso County carries the highest zone designation on the federal radon map, meaning a predicted average indoor screening level above 4 picocuries per liter, and the state health department reports that about half of Colorado homes exceed that action level. Soil gas gets in because the house sits warmer and at lower pressure than the ground around it, drawing air through the joint between wall and slab, sump openings, construction joints and plumbing penetrations.

That pressure relationship is the link back to combustion. Code air-tightness limits in this climate zone reach three air changes per hour at 50 pascals, and a mitigation fan, a dryer, a range hood and a bath fan all pull in the same direction. A tune-up that ignores the pressure the appliance actually operates under has skipped the interesting part. Sealing a combustion air opening to cure a draft complaint is exactly the wrong move.

### Filters, dust and the dry season

Dry air, sanding drywall in a basement finish, a new dog, an open window in April: filter loading has no calendar. What matters is using the size and orientation the rack was built for, and looking at the filter more often during long runtime stretches. A dense filter forced into a slot designed for a thinner one restricts air and can trip the same limit switch a technician was called out to explain.

### What should be on paper afterward

A condition report, not a verdict. Readings taken, parts cleaned or replaced, anything found on the vent or drainage side, and any recommendation with a reason attached. If a tune-up turns into a safety finding, that changes the visit from maintenance to inspection, and it should be said out loud rather than buried in a line item."""

# --------------------------------------------------------------- ignition repair
NEW["svc_furnace_ignition_repair_lede"] = """Ignition work covers draft, light-off and flame proving. A furnace that clicks and never lights, lights and drops out in seconds, or locks out after three tries has stopped at a specific step, and that step decides which part is actually involved."""

NEW["svc_furnace_ignition_repair_body"] = """### Where the sequence stopped

Watching one heat call from across the room answers more than a phone description ever will. Did the draft inducer spin at all? Did the igniter glow? Did burners carry across, and for how long? Did the cabinet lock out after a set number of attempts? A furnace that never reaches the igniter is reporting a problem with demand, power, the door switch, a rollout or limit circuit, the inducer, the pressure switch or the board. A furnace that lights and quits has already proved the igniter and the gas valve work.

### Flame proving is an electrical measurement

The sensor in the burner path is not a temperature device. Flame conducts a tiny current, the control measures it in microamps, and if the number falls short the valve closes because unproven gas is unacceptable. A weak signal comes from a coated sensor, a poor ground, a cracked porcelain, damaged wiring, misaligned burners or an incorrect combustion picture. Cleaning a sensor and calling it finished is only honest when the signal was measured before and after and the rest of the cycle was watched again.

### Running rich at altitude wears out ignition parts

Thin air is the local complication. Manufacturers require the input to come down as elevation rises, and they are specific about how. One high altitude kit swaps main burner orifices from 2.15 millimeters to 2.05, supplying one orifice per 20,000 Btu per hour of input and calling for 50 inch-pounds of torque on installation. The same manual bans the shortcut of lowering manifold pressure below the specified value, because reduced air density plus reduced pressure at the orifice prevents proper aspiration of primary air. Another maker ships a high altitude pressure switch for ninety-plus furnaces above 5,000 feet and prints an orifice table that steps a natural gas orifice up in size as elevation increases and gas heating value falls.

A furnace burning rich shows it in the parts that fail repeatedly: sooted burners, a sensor that needs cleaning every few weeks, a flame that lifts and drops. Replacing that sensor a third time treats the symptom of a setup problem.

### Pressure switch faults and the weather outside

The switch that proves draft is a reporter. When it opens, the useful question is what it saw: an inducer losing performance, a plugged port or tube, water standing in a condensate trap, a screen packed with debris, or a vent termination that took a hit. Wind matters here because gusts of 60 to near 100 mph occur in and near the foothills around this city, and the airport recorded a 92 mph gust during the extreme wind event on December 15, 2021. If the trouble started the morning after a windstorm, say so when the visit is scheduled and let someone look at the whole vent path from the ground up.

### Short cycling is a finding, not a quirk

Three-minute burns that satisfy nothing are worth chasing. A furnace oversized for the house, or sized on a sea-level rating in a city 6,035 feet up, spends the winter starting and stopping. Every start is a thermal shock to the igniter and a load on the inducer and board. Add a restricted filter or an undersized return and the high limit begins ending cycles too, which drops the blower into a cool-down run that homeowners describe as cold air. The fix is rarely the last part that broke.

### What not to try from the hallway

Do not jumper a safety switch, tape a pressure tube, or keep cycling power to force another attempt. Lockout is the control protecting the house, and repeated resets destroy the evidence a technician would have used. A gas odor changes everything: leave, do not stop to open windows, avoid light switches, garage door openers and anything else that can spark, and call 911 or the utility's twenty-four-hour number from outside. The utility responds to indoor and outdoor gas odor calls at no charge, and its own guidance notes that a meter still turning with every appliance off means gas is going somewhere.

### How the visit runs

Expect a controlled heat call, a meter on the control board and the flame circuit, a look at burners and the drainage and vent path, and a check of the setup against the data plate for this elevation. The regional building department also requires the manufacturer's installation instructions to stay with the equipment, and that booklet in the cabinet is often the fastest route to the model's own high altitude table. You should get the failed component named, the reason it failed, and the number before the work goes ahead."""

# ------------------------------------------------------------ blower motor repair
NEW["svc_furnace_blower_motor_repair_lede"] = """Blower work is about delivery. The burners can be perfect while rooms stay cold, the limit keeps tripping, the fan squeals at startup, or air keeps moving long after the flame is out. The motor is one candidate among several."""

NEW["svc_furnace_blower_motor_repair_body"] = """### Heat made and heat delivered are two different problems

Start by separating them. If flame establishes and holds, the furnace is making heat, and cold rooms point at what happens after that: filter, returns, blower wheel, motor, capacitor or module, duct leakage and register balance. If the fan runs when nothing is burning, look at the thermostat fan setting, a control protecting the cabinet after a limit event, or a board output stuck on. The order of questions saves a wasted part.

### Thin air carries less heat per cubic foot

Air at 6,035 feet is less dense than the air a sea-level rating book assumes, and less dense air holds less heat for the same volume. To move a given number of Btu into the house, the blower has to shift more cubic feet per minute than the same equipment would at sea level. That is the quiet reason airflow problems bite harder here. A filter one month past due, a return grille behind a sofa, or a flex duct crushed against a joist takes a system that had no margin and pushes temperature rise past the range printed on the data plate. The high limit then opens, burners stop, the fan keeps running to cool the exchanger, and the complaint arrives as cool air rather than as an airflow fault.

Manufacturers describe the same physics from the combustion side: the induced draft blower keeps moving nearly constant volume while the oxygen in that volume drops with elevation. Air quantity and heat capacity are not the same thing, and altitude separates them.

### Where the duct systems in this city came from

The median construction year across local housing is 1986, which is another way of saying most of these systems are neither original nor new. The city's own golf course neighborhood grew up around a course built in 1898 that the city has owned from 1919 onward, so Patty Jewett blocks carry gravity-era basements later fitted with forced air. Old Colorado City predates annexation into Colorado Springs in 1917 and includes small homes where the return path is a single central grille. Briargate came off a master plan drawn in 1978 and built out over the following decades, which means two-story layouts, long trunk runs and upstairs rooms fed last. Northgate sits at the top of the city, near an Air Force Academy campus whose cadet area is at 7,258 feet, and hillside addresses toward Broadmoor Hills often put equipment in crawlspaces with tight service access.

None of that diagnoses a motor. It does tell a technician where to look for the restriction before condemning one.

### Sounds, and exactly when they appear

A squeal or scrape that starts the instant air begins moving belongs to the blower assembly: bearings, a wheel rubbing its housing, a loose mount. A thump usually means debris or an out-of-balance wheel. A hum with no rotation points at a starting component or a jammed motor. A rattle that only shows up at full airflow is often a cabinet panel or a duct transition, and panels transmit sound so well that the noise you hear rarely sits where you think it does.

### The trap on a motor replacement

The second-visit failure in this trade is a new motor working against the same restriction that killed the first one. Static pressure across the air handler is the measurement that separates a bad motor from a bad duct system, and it takes minutes. Skipping it produces an expensive part swap, a furnace that still trips on limit in February, and a homeowner who now believes the furnace itself is finished. A variable-speed module and a fixed-speed motor also fail in different ways and are not interchangeable by eye; the wiring, the taps or the programming have to match what the cabinet actually shipped with.

### Filters, returns and the things people cover up

Filter and return access is the part a homeowner controls. Use the dimensions the rack was designed around, keep the airflow arrow pointed at the blower, and leave return grilles uncovered. Basement finishes are a frequent culprit in this market: a framed wall closes off the old return chase, a door gets weatherstripped, and the equipment loses the air it was commissioned with. Say so when scheduling if a remodel, new flooring or a filter cabinet change came shortly before the trouble started.

### What the repair covers, and what moves the number

Testing includes motor electrical readings, wheel and housing condition, capacitor or module operation, filter and return restriction, temperature rise and static pressure. Cleaning a wheel, replacing a capacitor, correcting a wiring or speed-tap error, fitting a compatible motor, or opening up a strangled return are separate scopes with separate costs. Access, equipment age, parts availability and how much duct correction the job needs move the figure more than the motor itself does. Whichever it turns out to be, the finding and the price come before the work."""

for k, v in NEW.items():
    if k not in blocks:
        order.append(k)
    blocks[k] = v

out = [head.rstrip("\n"), ""]
for k in order:
    out.append(f"## {k}")
    out.append(blocks[k])
    out.append("")
COPY.write_text("\n".join(out).rstrip("\n") + "\n")

sj = SITE / "site.json"
raw = sj.read_text()
raw = raw.replace('"phase": 1,', '"phase": 2,', 1)
sj.write_text(raw)
print("phase 2 ok")
for k in ["symptom_1", "symptom_2", "symptom_3", "symptom_4", "services_summary",
          "services_pick_head", "crosslink_head"]:
    print(k, len(blocks[k].split()))
for k in order:
    if k.startswith("svc_"):
        print(k, len(blocks[k].split()))
