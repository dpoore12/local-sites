import re, pathlib

p = pathlib.Path('sites/coloradospringsemergencyplumber.com/copy.md')
t = p.read_text()

NEW = {}

NEW['symptom_1'] = """Clear water arriving after every tap in the house is closed means the pressure side has opened up somewhere. Close the main valve, then open the lowest cold faucet so the line drains down. If the split followed a cold night, look in a crawl space, a garage bay or an exterior wall rather than at the wet ceiling. Leave the finish alone until the pipe is visible."""

NEW['symptom_2'] = """Water climbing in a bowl or standing in a tub tells you where the restriction is not. Stop flushing, and stop running anything else, the washer included. If the tank keeps refilling, lift the lid and hold the flapper down. Note which fixtures react together before anyone arrives, because that pattern is what picks the machine."""

NEW['symptom_3'] = """Wastewater at the lowest opening in the building points downstream of everything inside it, out along the four-inch line the property owner maintains all the way to the utility main. Shut off every water use, keep people and pets off the wet floor, and leave the cleanout cap alone while the system is still holding water."""

NEW['symptom_4'] = """Nothing at any tap is a supply question. Check a second faucet, confirm whether hot and cold are both dead, then find out whether the block still has water. A dry street belongs to the utility, which takes emergency reports around the clock at (719) 448-4800. Do not keep forcing a stiff main valve."""

NEW['services_summary'] = """Four jobs sit behind nearly every after-hours call in El Paso County, and the money in them is nothing alike. Emergency repair is triage: name which system failed, isolate it, and settle whether the fault is even on the private side of the curb stop. Burst pipe work is pressure-side work, and in a high-pressure zone it repeats until somebody puts a gauge on a hose bib. Drain cleaning removes a blockage a machine can reach. Sewer repair starts only after a camera proves the buried four-inch line is broken. Guess wrong between them and you buy a second visit."""

NEW['services_pick_head'] = """Start with the failure your house is showing tonight"""

NEW['crosslink_head'] = """Facing a different failure?"""

NEW['svc_emergency_plumbing_repair_lede'] = """Water loose, taps dry, or wastewater coming back up. The first decision is which of three systems failed, and whether the fault sits on the private side of the curb stop or belongs to the utility at all."""

NEW['svc_emergency_plumbing_repair_body'] = """### Sorting supply, drain and sewer in the first few minutes

Three systems fail in houses, and each one sends a different truck. Clear water still arriving with every fixture closed is the pressure side. Dark water rising at the lowest opening in the building is drainage. Nothing at any tap, hot and cold alike, is a supply question that may not be on your property at all. Ask whether the block still has water before anyone opens a wall. A dry street is the utility's problem, and it takes emergency reports at (719) 448-4800 at any hour of the day.

### A gravity system stretched over two thousand feet of relief

Ground elevations across the utility's service area run from roughly 7,800 feet down to about 5,750 feet, and distribution is generally gravity fed, with pumped service to some areas. To keep that workable, the water system is divided into 52 pressure zones held by 260 system pressure regulating valves, with 38 storage tanks and five major service areas: Briargate, Templeton, Northfield, Highline and Lowline. Each lower level can be fed through regulators from the levels above it or from its own distribution storage. The utility's stated goal is consistent pressure to a standard of 60 pounds per square inch. What that means at your kitchen sink is that static pressure is a product of which zone you sit in and where your lot falls inside it, not one city-wide number.

### Where the utility's pipe ends and yours begins

Two boundaries, and they are drawn in opposite directions. On the water side, city code puts maintenance and replacement of the service line in the public right-of-way on the utility, generally from the connection at the distribution main to the property line or the curb stop, and puts everything past that point on the owner. The utility says the same thing in plainer words: the line inside your property, between the curb stop and the structure, is yours to maintain. Wastewater runs the other way. There, code makes the owner responsible from and including the connection to the collection line, all the way back to the building.

### Find the shutoff before you need it in the dark

The valve you want is usually where the service enters: a basement wall, a crawl space, or a mechanical closet toward the front of the house. Turn it, label it, and confirm that it actually seals, on an afternoon when nothing is wrong. Code also puts an ongoing duty on the owner to keep the service line and the pipes and fixtures on the premises in good repair so water is not wasted, and a main stop that no longer closes fails that test. Replacing a valve that will not seat is a small scheduled job. Discovering it at midnight is not.

### Water heaters and the discharge nobody watches

Tanks announce themselves in a short list of ways: a weeping seam, a corroded drain valve, a split flex connector, or a relief valve letting go. That last one is usually a pressure symptom rather than a defective part. A Colorado amendment to the plumbing code requires a means of capturing relief valve discharge and conveying it to the drainage system or the exterior of the structure, by gravity or by pumped discharge, with an exception written in for replacements of existing heaters. The regional building department's handout sets the relief valve at 150 psi maximum and fixes how close its discharge may terminate to the floor or waste receptor. Replacement is permitted and inspected work. Isolating a leaking heater tonight is a different, faster job.

### Backflow assemblies come with dates attached

Any backflow assembly on a property has to be tested at the user's expense when it is installed, repaired or replaced, and at least once a year after that. City code sets the annual deadline at July 1 where the assembly protects the water system from an irrigation connection, and October 1 where it does not. Colorado's adopted code requires that testing be done by a certified cross-connection control technician. In practice the requirement reaches businesses and multi-family buildings rather than single-family houses, and the utility backs it with per-assembly fines and suspension of water service.

### What the visit settles, and what moves the total

Flow gets stopped or the failed branch isolated first, before anything is diagnosed. Then the failure is named with evidence rather than guessed at: a gauge reading taken at a hose bib, a meter that will not come to rest with the house shut down, camera footage with a distance attached to it. Four things move the total from there. How much has to come apart to reach the fault. Whether the work stays inside the building or continues out toward the curb stop. Whether a permit and an inspection are attached to it. And what hour of what day it is when the phone rings."""

NEW['svc_burst_pipe_repair_lede'] = """A supply line does not have to freeze to let go. Pressure alone will find the weakest crimp, stem and hose in a house, and the wet ceiling is almost always downhill from the actual split."""

NEW['svc_burst_pipe_repair_body'] = """### Reading the leak before any finish comes off

Clear water that keeps arriving after every fixture is closed puts the fault on the pressure side. The meter settles it: with the house shut down, a dial that will not come to rest says water is leaving the system somewhere. Water tracks along framing before it drops, so a stain marks elevation more reliably than it marks the break. Warm drywall, a hissing wall cavity and a warm patch on a slab each point somewhere different, and each one changes how much has to come apart.

### Eighty psi is a limit, not a target

The residential code Colorado has adopted is specific about this. Static water pressure shall be not greater than 80 psi, and where main pressure exceeds that figure an approved pressure-reducing valve conforming to ASSE 1003 or CSA B356 must be installed on the domestic water branch main or riser at the connection to the water service pipe. That valve lives on private plumbing, past the curb stop, which makes it a homeowner's device to know about. A threaded gauge on an outside hose bib settles in ten seconds what people spend years guessing at.

### The failures people blame on cheap parts

Pressure above the code ceiling does not announce itself. It shows up as a pattern instead: braided washer hoses that rupture at the crimp, toilet fill valves that will not shut cleanly, faucets dripping again a month after new cartridges, a water heater relief valve weeping every afternoon, and appliances that die years early. Swap the part and the pressure is unchanged, so the replacement fails the same way. The utility met the same physics from its own side of the meter on the west side of town. While raising pressure in a zone near Garden of the Gods Park, it assessed pressure reducing valves in roughly 675 homes and commercial buildings and replaced them as needed to prevent damage to plumbing and appliances, then scheduled another round of assessments once pressure was up.

### Winter splits happen in the rooms nobody heats

Weather service normals put January here at a 45.0 degree afternoon and an 18.5 degree night, with December nearly identical. Pipe in a vented crawl space, an attached garage, a soffit chase or an exterior wall spends that night much closer to outdoor temperature than the rest of the house does. The utility attributes most breaks on its own mains to the local freeze and thaw cycle, which shifts soil and loads the pipe. Private lines get the same treatment. Plenty of splits stay quiet until the plug thaws hours later and the water finally has a path.

### A closed system needs somewhere for hot water to go

Put a pressure-reducing valve, a check valve or a backflow preventer on the supply and the house becomes a closed system. Heated water then has nowhere to expand into, and pressure climbs every time the burner or the element runs. Code covers this in two parts. A control device is required where thermal expansion pushes pressure downstream of a reducing valve above the valve's setting, and again where a check valve or backflow device sits on a system using storage water heating equipment. The regional building department states it plainly for inspectors: an expansion tank or expansion device is required when a PRV, check valve or backflow preventer is in the water supply system. A missing tank behind high street pressure is why a relief valve drips on schedule.

### The bang in the wall is doing real damage

A washer or dishwasher solenoid closes in a fraction of a second, and the moving column of water behind it has to stop somewhere. Adopted code requires a water-hammer arrestor conforming to ASSE 1010 wherever quick-closing valves are used. Loose pipe straps make the noise louder while hiding what causes it. Shock loading repeated a few thousand times works on solder joints, crimp rings and hose ferrules until one of them gives up, usually the one behind a cabinet nobody checks.

### One repair, or a run that keeps failing

Sound pipe on both sides of a single break supports a cut-and-couple repair, a pressure test, and an honest look at everything the water touched. A branch that has split twice in three winters is a different conversation, and so is a house that eats supply hoses. Copper tends to fail at pinholes and at joints near dissimilar metal, galvanized fails at its threads, and crimped plastic fails at the crimp. Cost then follows access more than it follows the fitting. Exposed pipe in an open basement is quick work; a line inside a finished wall drags drywall, texture and paint behind it; a failure out toward the curb stop turns into a trench, a locate and a permit."""

NEW['svc_drain_cleaning_lede'] = """A blockage has an address. A trap, a fixture arm, the building drain under the slab, and the four-inch line running out to the utility main are four separate jobs, and only the first one is small."""

NEW['svc_drain_cleaning_body'] = """### Which fixtures react, and what that rules out

One slow lavatory is its own trap or the arm behind it. A kitchen sink that ponds while everything else behaves is usually grease in that branch. Once a flush lifts water into a tub, or the washer discharge brings up a basement floor drain, the restriction sits below the point where those fixtures join. Testing further from there only adds volume to a system with nowhere to put it. The useful report is short: what was running, where water came back, and how long it took to fall on its own.

### The four-inch line and the two-year interval

The utility is direct about both the boundary and the maintenance. Customers are responsible for maintaining the four-inch service line that runs between the utility main and the house, and the published advice is to have that line professionally cleaned every two years. It adds that homes in older neighborhoods with large trees may need it more often than that. Scope matters as much as frequency. Cleaning the full four-inch diameter all the way out to the main is a different piece of work from punching a channel through a blockage and calling it open.

### Old trees standing over old yard lines

Age is concentrated in particular blocks. The Old North End district covers about 392 acres and 1,001 buildings, 903 of them contributing, with a period of significance running from 1885 to 1965 and very little construction after that. Patty Jewett and Old Colorado City carry similar decades of housing stock. Street trees planted alongside those houses have had a century to mature over the yard lines, which is precisely the condition the utility's cleaning advice is written for. Newer ground is not exempt, though. A Briargate or Rockrimmon line with a sag in it holds water between cleanings just as effectively.

### Knowing where your cleanout is

An accessible cleanout is the difference between a machine in the line within ten minutes and a toilet pulled off its flange first. In houses remodeled twice, that fitting often ends up under a deck, a raised bed, or a patio someone poured over it. Locating yours on a dry afternoon costs nothing and saves an hour on the worst night of the year. One more thing worth writing down: if a machine stops at the same measured distance on every visit, that is not bad luck, it is a defect with a location.

### Pouring things into a line that is already full

Caustic and acid drain products do not open a blocked main line. They sit in the standing water, wait for whoever opens the cleanout, and can attack older pipe on the way past. Enzyme treatments do nothing at all to roots. Forcing a garden hose down a stack just raises the level of what is already trapped. Whatever has gone down should be said out loud, because it changes how the person arriving protects themselves and your fixtures.

### Cable and jetter are not interchangeable

A drum or sectional machine with a cutting head belongs on a root mass or a hard obstruction, because it cuts through and gets flow back quickly. A jetter scours the full circumference and does better on grease, sludge and soft scale in pipe that is still structurally sound. The failure mode picks the tool. Sending high-pressure water through cracked clay or badly deteriorated cast iron can wash out the bedding beneath the pipe and turn a blockage into a repair.

### How the visit runs, and what moves the figure

Access comes first, then the blockage, then a real test with fixtures run under load rather than one hopeful flush, with the tool used written on the paperwork. Length of run, number of bends, whether a toilet has to come up, and whether standing wastewater has to be handled all move the figure. Footage afterward is a separate step, and it is worth paying for once on any line that has backed up twice. It replaces a hopeful verdict with a measured distance, a depth, and the name of the defect. Whatever repair that evidence calls for stays a separate decision made in daylight."""

NEW['svc_sewer_line_repair_lede'] = """Clearing a line gets flow back tonight. Replacing or lining it is what happens once footage shows the pipe has lost a joint, a slope or a wall, because no machine puts any of those three back."""

NEW['svc_sewer_line_repair_body'] = """### Signs that point past the foundation

Backups that return within weeks of a clearing that seemed to work. The lowest opening in the house filling first, every time. A strip of lawn along the run that stays soft, greens up early, or has settled into a shallow trough. A machine that stops at the same distance on every visit. Those all point outdoors, past the foundation wall. A single misbehaving fixture while everything else drains normally almost never does.

### This line is yours all the way to the main

The two service lines are not symmetrical, and the difference catches people out. On the water side, the utility carries the right-of-way portion up to the property line or the curb stop. On the wastewater side, city code makes the owner responsible from and including the connection to the collection line, back to the premises served. The tee at the main sits on your side of that boundary. The same section requires the owner to replace any portion that has disintegrated, and the utility's own policy describes the four-inch line between its main and the home as the customer's to maintain.

### Roots find joints, not pipe walls

A root does not drill through sound pipe. It finds a joint that has shifted or a crack already weeping, follows the moisture out of it, and then fills the bore with fine growth that catches paper and grease until flow stops entirely. Clay tile laid in short sections gives roots a joint every few feet, and scaled cast iron gives them plenty of texture to hold. Cutting that growth back gets the house working again by evening. It does nothing about the opening that let the root in, which is why the same line closes again the following spring.

### What the camera has to produce

Footage is evidence, not decoration. A scope run with a surface locate should yield the distance from the cleanout to the defect, the depth, the pipe material, and the kind of defect it is: root intrusion at a joint, an offset, a longitudinal crack, a low section holding water, or a missing length. Watch the video rather than reading a summary of it. Roots at one joint thirty feet out is a spot repair; a crushed run under a driveway approach is a different project with a different number attached.

### A permit comes before the repair, not after

City code requires a permit from the utility before any repair or alteration of a wastewater service line, and an inspection follows the work. The owner also carries responsibility for returning the public right-of-way and the street to city standards afterward. Utility locates come before any excavation. Those requirements are the reason finished and closed out land on different days, and they belong in an estimate: who pulls the permit, who calls the locate, and what the restoration standard is where the trench crosses pavement.

### If wastewater has already come inside

Stop every water use in the building and keep people and pets off the affected floor. Report it, because the utility inspects its own main first. It will address damage caused by a verified blockage in its main line, while a blockage in the service line between that main and the house stays with the customer, and there is a published assistance path for denied residential claims. Cleanup, drying and material replacement are separate decisions made once the line is flowing again. The plumbing visit exists to stop the return and restore the pipe.

### Choosing a method, and why the range is wide

Footage picks the method, not preference. One bad joint can be dug and replaced in a day. A structurally sound run that is leaking at joints can take a cured-in-place liner. A section that has lost its grade has to be reopened and reset on new bedding, since lining a belly preserves the belly. Depth is the largest single driver of cost, followed by whatever sits on top of the line: lawn, mature landscaping, a concrete drive, or street pavement the city expects restored. Decomposed granite and rock slow the digging, and a sloped lot needs shoring before anyone works down in the trench."""

# Replace existing blocks
for k, v in NEW.items():
    pat = re.compile(r'(^## ' + k + r'\n\n)(.*?)(?=\n## |\Z)', re.S | re.M)
    if pat.search(t):
        t = pat.sub(lambda m: m.group(1) + v.strip() + "\n", t)
    else:
        t = t.rstrip() + "\n\n## " + k + "\n\n" + v.strip() + "\n"

p.write_text(t)
print("written")
