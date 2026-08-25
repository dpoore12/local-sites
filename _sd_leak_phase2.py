#!/usr/bin/env python3
"""Phase 2 edit for sandiegoleakdetectionpros.com: shrink symptoms, add service blocks."""
import json, re, pathlib

SITE = pathlib.Path("sites/sandiegoleakdetectionpros.com")
copy = SITE / "copy.md"
text = copy.read_text()

SYM = {
1: """Public Utilities publishes a plain version of this test. Shut every fixture and water-using appliance, note where the dial sits, and wait half an hour. Movement means water is crossing the meter on your side of it. Check hose connections, toilets and appliance lines first. When those are clean and the dial still creeps, the department's own wording is that the leak may be concealed underground.""",
2: """A baseboard that never dries, a grout line going dark, or one plank cupping usually means a supply line failing inside the concrete rather than a spill. Photograph the wet edge and mark it lightly so you can see whether it grows. Keep cords and outlets out of it. Do not chip or core the floor, because the tendon layout in a post-tensioned slab has to be identified first.""",
3: """One slow shower normally begins at that fixture. A change felt at several taps points instead at the regulator, the main valve, or a line losing water on the way to the house. Public Utilities will send a crew to read pressure at the hydrant nearest you, which separates a neighborhood condition from a private one. Leave the regulator alone until it has been measured.""",
4: """Reference evapotranspiration at the county's coastal stations averages close to 5.7 inches in July, so roughly a fifth of an inch a day leaves a pool with nothing wrong. Mark the tile line, set a bucket of pool water on a step at the same level, and compare both drops after a day. Note whether the pump ran and whether auto-fill was switched on.""",
}

for i, body in SYM.items():
    pat = re.compile(r"(## symptom_%d\n\n).*?(?=\n## )" % i, re.S)
    assert pat.search(text), i
    text = pat.sub(lambda m: m.group(1) + body.strip() + "\n", text)

NEW = r"""
## services_summary

Four different jobs arrive as one call about water going missing. A pressurized line inside the house, a supply pipe cast into the slab, a buried run between the meter box and the wall, and pool plumbing under the deck each need their own test before a surface is opened. Mixing them up is unusually expensive in this city. Metered water is billed in rising tiers, the single-family sewer charge is calculated from 95 percent of that same metered water, and the city's bill credit is written for a concealed pipe leak only. Irrigation, fixtures and pools are excluded, and the filing window is 120 days.

## services_pick_head

Start with the failure the evidence actually points to

## crosslink_head

A different water loss?

## svc_water_leak_detection_lede

Water keeps crossing the meter with the house shut down, and the bill has already moved. What follows is how that loss gets separated from a fixture, an irrigation valve and the buried service run, and what the city wants documented before it will credit anything.

## svc_water_leak_detection_body

### The half-hour meter test the utility publishes itself

Public Utilities sets out the sequence on its own leak page. Turn off all faucets and water-using appliances so nothing in the building is drawing water, note the position of the meter dial, and wait. If the dials have not moved in thirty minutes, the department calls the home relatively water-tight. If the dial has moved, its list of next suspects is hose connections, faucets, toilets, dishwashers, washing machines, water heaters and refrigerators. When those are all quiet and the dial still turns, the department's own conclusion is that a concealed leak in an underground pipe is likely. It adds one more clue that gets ignored constantly: a meter box standing in water may mean the leak is at the meter itself.

Reading the register is simpler than it looks. City meters count cubic feet, and billing works in units of one hundred cubic feet, so the last two digits are dropped from the read. A unit is roughly 748 gallons, which is worth knowing before deciding whether a jump in consumption is a habit or a hole.

### Why concealed water costs more here than the gallons suggest

The rate design does the damage. Single-family accounts pay a first-tier rate up to 10 units a month, a middle rate from 11 through 22, and a third-tier rate above that, and the third tier runs about 40 percent above the first. The sewer side then charges again for the same water: the single-family sewer service charge is calculated from 95 percent of monthly metered use, capped at 20 units a month. Until that cap is reached, every leaked unit is billed twice.

Rate history explains why an old bill is a bad benchmark. Water rates rose 14.7 percent on January 1, 2026 and wastewater rose 6 percent, both approved by the City Council on October 28, 2025, following a 5.5 percent pass-through in May 2025. A further water adjustment of up to 14.5 percent is approved for January 2027. Under the appellate decision in Patz v. City of San Diego the tiers are also going away, replaced by one volumetric rate for every customer, which removes the low-use discount that quiet households have been enjoying.

### The credit is real, and narrower than almost everyone assumes

One remedy exists and it has hard edges. An adjustment is considered only for a non-irrigation concealed pipe leak. Irrigation leaks, pool leaks and leaking plumbing fixtures are excluded by name. The request has to reach Public Utilities within 120 days of the first high bill connected to that concealed leak, and requests arriving later are not considered.

What the department asks for is a short list: account holder name, service address, phone and email, the date the leak was discovered, the date repairs were made, and a copy of the repair invoice. Two of those dates live on the plumber's paperwork, not yours, so ask for both in writing while the work is happening. Review time is stated as eight to ten weeks in the instructions and six to eight weeks in the same page's questions, so plan around the longer figure.

### Where the city's water stops being the city's problem

The boundary is one fitting. The department's plumbing guidance says the property owner maintains any portion of the water system from the meter onward, and its water emergency material narrows that further: on the property side of the meter the city keeps up the gasket and washer, nothing else. State licensing language draws the same line, since the plumbing classification covers water piping from the owner's side of the utility meter to the structure.

Records help and they have limits. Development Services holds records of when a water line was installed and can produce a map of where it connects to the main. The city states plainly that it has no diagrams showing where lines run inside your property, which is exactly the part a locate has to establish.

### Do not wait for a smart meter to raise the alarm

The citywide Smart Metering Infrastructure project covers roughly 280,000 meters, and the adopted capital program says implementation of the deployment plan is anticipated to begin in fiscal 2027 after a pilot of about 11,000 connections in fiscal 2013 through 2015. Most accounts are therefore still read periodically rather than continuously, and a concealed leak can run for a whole billing cycle before anything reaches you. The half-hour dial test is still the fastest alarm available.

### Isolation first, microphones second

Competent work narrows the field mechanically. A gauge on a hose bib gives static pressure, then the house main is closed to see whether the meter settles. Irrigation is valved off separately, hot is split from cold at the heater, and each section is held under pressure while the gauge is watched for decay over a timed interval. Only then do acoustic listening, sensor correlation, tracer gas and thermal imaging earn their keep, because by that point they are searching a short list. Local water is hard, averaging about 16 grains per gallon and ranging to 18, so scale at stops and connections can disguise a slow seep.

### What the visit leaves you, and what moves the figure

A finished locate produces a marked position, a photograph, the method used and an honest account of what is still uncertain. Access drives the labor far more than pipe does: a fitting in a laundry wall, a run under bathroom tile and a service line beneath a driveway apron are three unrelated jobs. Repairs to water or sewer piping qualify for the city's simple no-plan plumbing permit, which is priced per dwelling unit, and that line belongs in the estimate rather than in a surprise later.

## svc_slab_leak_detection_lede

A supply line fails inside or beneath the concrete and the floor becomes the only witness. Here the next question is not where to cut. It is what the slab is carrying, and what the clay beneath it does once it gets wet.

## svc_slab_leak_detection_body

### Reading a slab-on-grade floor honestly

The loud version is a hot-water failure: a patch or narrow band of tile that stays warm while nobody is drawing hot water. Cold-side failures are quieter and get missed for months. A grout line darkens, a baseboard never dries out, a wood plank cups in one direction, a closet turns musty, and none of it sits directly over the break. Water spreading under concrete follows the path of least resistance and surfaces where the finish is weakest, sometimes a room away. A meter dial that refuses to settle with the building shut down is what confirms the loss is active.

### Tendons change the order of operations

Foundation drawings matter before concrete tools do. The city's project submittal requirements make the foundation plan show slab thickness, reinforcing steel size and spacing, and the tendon layout for a post-tension slab, and require the plan to use the foundation system recommended in the project's geotechnical investigation report. That report has to be project-specific, stamped by licensed professionals, and no more than three years old unless it is updated.

Practical consequence for a leak: the record of where stressed strand runs already exists on paper for slabs built that way, and finding it is part of the job. Cutting a tendon releases stored force and removes compression the slab was designed to keep. That is a structural decision belonging to whoever carries the foundation, informed by the drawings and by scanning, not a call made with a rented hammer.

### Mesa-top clay reacts to your leak, not just to the weather

The city's own geologic hazard work on the mesa communities is blunt about this. Very old paralic deposits, which cap the mesas, typically carry a thick clayey weathering profile that forms expansive, highly plastic residual clay. Expansion can produce unacceptable settlement or heave in slabs supported on grade. The listed causes of the moisture change that triggers it include precipitation, landscape irrigation, roof drainage, perched groundwater, drought and, in the report's own words, utility leakage.

So a slow leak under a slab is a soil event as well as a plumbing one. Floors that crack or lift months after a repair often reflect the moisture cycle the leak set off, which is a reason to fix a slab leak on evidence rather than to keep watching it. The same deposits are locally cemented, so the trenching around a house is often slower than the homeowner expects.

### What not to do while you wait

Do not chip an exploratory hole where the wet shows, because the wet is downstream of the failure. Do not run hot water to see whether the warm patch spreads, since every gallon travels under the floor into insulation and cabinet bases. Keep away from outlets, floor registers and appliance connections in a wet area, and stay out of standing water rather than reaching a valve through it. Closing the main from dry ground is worth doing, though a corroded stop should not be forced hard enough to snap.

### The pipe that produced most of these failures

Age explains the pattern. Census figures reproduced in the city's housing element put 7.3 percent of local units at 1939 or earlier, 16.6 percent in the 1940s and 1950s, and 33.7 percent between 1960 and 1979. The pre-war streetcar districts sit at the older end. North Park's original subdivisions were recorded just after the turn of the twentieth century, Kensington's pioneering subdivision dates to 1910, and Talmadge was established in 1925. Houses of that vintage began life with threaded steel supply and hubbed iron drainage, and both fail at the joint from the inside outward.

The mesa tracts are a different problem. Mira Mesa's first tract opened in 1969, and roughly 8,685 dwellings went up there between October 1969 and October 1976, an era of soft copper run in and under the slab. Hard water and a recirculating hot loop work on that copper from within while damp expansive clay works on it from outside.

### Penetration against reroute

Two honest answers exist. Opening the floor above the located point replaces the failed section, then leaves you patching concrete and matching a finish that may no longer be made. A reroute abandons the buried section, rebuilds the run overhead or through walls, avoids stressed strand entirely, and lifts the pipe out of the ground that failed it. A single failure in otherwise sound copper can justify the spot repair. A second failure on the same line, irreplaceable tile above it, or a tendon pattern with no clean window all argue the other way. Be equally skeptical of a whole-house repipe proposed from one located leak with no evidence of thinning anywhere else.

### The sequence, and what moves the total

Hot is split from cold, each side is pressure-tested and watched for decay, ground microphones walk the floor, two sensor positions are correlated, and tracer gas goes into the drained section when carpet or thick tile defeats acoustics. Thermal imaging confirms the picture where the temperature difference supports it. The point is marked with measured offsets from two walls and photographed. Four things move the number: whether finished floor has to come up, whether one fitting or a rebuilt run is the answer, whether scanning and an engineer come first, and who restores tile, texture and paint.

## svc_underground_leak_detection_lede

Between the meter box and the house wall, and onward through valves and drip line, water can run a whole billing cycle without showing at the surface. On a canyon lot it may never surface where it left the pipe at all.

## svc_underground_leak_detection_body

### What a buried line does leave at the surface

Outdoor evidence is indirect. A strip of unusually green growth in September, soil still soft a week after watering stopped, a paver settling, water tracking into a gutter, or a meter that creeps with the house main closed all point outside the walls. Pressure sagging at every indoor fixture belongs on the list too, because a service line losing water bleeds pressure and consumption at the same time.

Season is the strongest filter available here. About 85 percent of seasonal rainfall arrives between November and March, and only around 2 percent falls from June through August against a long-term normal near 10.77 inches. Wet ground in July is therefore somebody's water, not the weather's.

### Canyon rims and shale slopes send water sideways

Geology decides where the surface clue lands. The city's hazard categories treat the Ardath Shale, exposed in most canyon slopes across the mesas, as a slope problem in its own right: weathered, it desiccates into weak sheared clay that is expansive and unstable on slopes, and the categories separate favorable structure from unfavorable. Slide-prone Friars Formation carries its own category. The city's guidance is that all slopes underlain by that shale should be treated as potentially unstable.

Two named neighborhoods show what that means for a locate. Kensington occupies a narrow peninsula isolated on three sides by steep slopes, and Talmadge is ringed by canyons. Water escaping a buried pipe on ground like that follows fracture and bedding, comes out well downslope, and adds load to a slope whose stability was already conditional. The wet patch is a clue about drainage paths, not a marker over the break.

### Seepage that has nothing to do with your pipe

Not every damp slope is a leak. Perched groundwater appears in the city's own list of moisture sources, irrigation runoff moves along the same paths, and a wet winter leaves canyon faces weeping for weeks. The way to tell them apart is behavior rather than appearance: does the flow stop when the meter is closed, does it change when irrigation zones are isolated, is it continuous or does it track a controller schedule. Public Utilities also sends a crew to test pressure at the hydrant nearest an address on request, which settles whether a pressure complaint is private.

### When the break belongs to the city

There is a staffed route for that. The water emergency line runs 24 hours a day for main breaks, service leaks, valve leaks, hydrant knockovers and pressure problems. The operator takes the location, nearby landmarks, a description and any damage, then dispatches a unit that isolates the water while a construction crew excavates, repairs, backfills and lays a temporary patch.

Money afterward follows a written council policy on claims from main breaks and sewer backups. If a third party caused the loss, or the owner or tenant did, the claim is denied. Where the city had control and the property owner was an innocent party, the listed assistance includes emergency cleanup, an adjustment for personal property, additional living expense when a home is found unfit, real property restoration, and reimbursement of reasonable plumbing bills spent identifying the problem once a main stoppage is confirmed. Private lateral stoppages are excluded from that help, and the lateral is the owner's all the way to the main.

### Digging into ground that was never soft

Excavation cost tracks geology and access more than pipe diameter. The cemented layers in the mesa deposits are called out by the city's evaluation as difficult conditions for utility trenches, and a terraced hillside lot adds its own constraint, since a retaining wall over six feet needs a geotechnical report of its own. A trench that opens in an hour through landscape fill can take a day where the ground is cemented, and a run beneath a driveway apron, a slope face or mature roots is a different day again.

### Licensing and paperwork before a trench opens

State rules are specific and easy to check. Any contract for construction work valued at $1,000 or more in combined labor and materials requires a state license, the license number has to appear in advertising, and status can be verified at the licensing board's site or by phone before anyone starts. The plumbing classification is the one that covers water and gas piping from the owner's side of the utility meter to the structure. On residential work the down payment is limited to 10 percent or $1,000, whichever is less, a written contract is required above $500, changes need a signed change order before the work, and the contract has to say who pulls the permits.

### What the locate is supposed to produce

The deliverable is a position, not a theory. Expect a marked point with offsets to fixed features, a photograph, the method that found it, and the reason for any remaining uncertainty. Expect the estimate to separate the locate from the repair, to name the surface being opened, and to say who restores landscape, concrete or asphalt afterward. A locate that ends in a shrug and a proposal to replace the whole run has skipped the part you were paying for.

## svc_pool_leak_detection_lede

A pool in this climate loses water every single day without anything wrong with it. So the first task is arithmetic, not excavation: separate ordinary loss from a real one, then test the shell, the plumbing and the equipment as three different things.

## svc_pool_leak_detection_body

### What evaporation alone takes in July

Numbers make this argument, not opinion. The county's water-efficient landscape manual reproduces long-term reference evapotranspiration from the state's irrigation stations: about 46.5 inches a year at the San Diego station and about 5.7 inches in July alone. That is close to a fifth of an inch a day at the peak, before wind, swimmers, splash-out or a backwash cycle. Rain will not make it back either, since roughly 2 percent of seasonal precipitation falls from June through August.

The bucket comparison exists to cancel weather out. Mark the tile at the waterline, stand a bucket of pool water on a step with its level matched to the pool's, then read both after 24 hours. Equal drops mean the climate is doing it. A pool that drops noticeably more has a candidate for a leak, and that is a screening result rather than a diagnosis.

### The city's bill credit will not cover this one

Worth knowing before the water bill arrives. The leak adjustment policy excludes pool leaks by name, alongside irrigation and leaking fixtures, and only a concealed non-irrigation pipe leak is considered at all. Meanwhile the fill water is metered like any other water, climbing the tiers, and the single-family sewer charge is figured from 95 percent of metered use up to its monthly cap. A leaking pool therefore produces a bill with no remedy behind it, which is the practical reason to measure early.

Automatic fill equipment makes it worse by hiding the symptom. With auto-fill running, a leak stops showing as a falling level and shows only as consumption. If the level never moves but the meter never rests, suspect the fill valve and the pool plumbing together.

### Reading the loss against equipment operation

Rate of loss is the most useful clue on the pad. A drop that speeds up while the pump runs points at pressure-side plumbing after the pump, where lines are under load. Loss that continues with everything switched off points instead at a suction line, the skimmer, a light niche, a fitting or the shell. Air in the pump basket, unexplained bubbles at a return, filter pressure drifting, and damp ground around the equipment are all supporting evidence and none of them are proof.

### Salt air at the equipment pad comes first

There is a local reason to look at metal before deck. The city's water facility design guidelines note that much of this area sits in a marine environment where airborne salts and wet-dry cycling in chlorides create significant corrosion activity on exposed metal surfaces. Unions, clamps, valve stems, heater connections and the backflow assembly are cheap to inspect and frequently the answer. Opening decking before that inspection is a way to spend money on the wrong end of the system.

### How the plumbing actually gets isolated

Testing is line by line. Each suction and return line is plugged and pressurized separately with a gauge held for a timed interval, so the failing line declares itself instead of the whole system being condemned. Accessible fittings, skimmer throats and light niches get dye with the pump off and the water dead still. Listening equipment can hear a pressurized escape, and a line can be traced to give the repair a position rather than a guess. One safety rule overrides all of it: a pump run below its safe water level damages the equipment, so stop filling to test and let the level stand.

### What the deck and the local rules add

Restoration is often the bigger half of the invoice. Coping, tile, bond beam work and matching an older deck finish drive a repair number more than the pipe itself does, and a reroute around a failed line is sometimes cheaper than reaching it. City plumbing requirements also constrain where equipment can sit, since pool equipment is not permitted in required side or rear yards in residential zones unless it meets the referenced municipal code provision. For pool contracts the state adds its own paperwork: a plan and scale drawing showing shape, dimensions, construction specifications and equipment specifications, plus the same limit on any down payment.

### What the visit should leave behind

A useful pool leak visit ends with the loss quantified, the system it belongs to named, and the suspected point marked and photographed. It should say which lines held pressure and which did not, whether the shell was ruled out, and what still needs confirming once water is lowered or a small area is opened. Anything less turns into deck demolition financed by hope.
"""

text = text.rstrip() + "\n" + NEW.rstrip() + "\n"
copy.write_text(text)

sj = SITE / "site.json"
d = sj.read_text()
assert '"phase": 1' in d
sj.write_text(d.replace('"phase": 1', '"phase": 2', 1))
print("ok")
