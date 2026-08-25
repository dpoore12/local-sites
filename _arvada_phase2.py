import json, re, pathlib

d = pathlib.Path("sites/arvadaemergencyplumber.com")
p = d / "copy.md"
text = p.read_text()

B = {}

B["symptom_1"] = """Clean water still arriving with every tap closed is a pressure-side failure, and the clock is running on drywall and subfloor. Close the house main, then open a low fixture to bleed off what is left in the pipe. If the split followed a cold snap, expect the break in an unheated space rather than at the ice itself. Leave the wall shut until the pipe is exposed."""

B["symptom_2"] = """One sink holding water is a trap or a fixture arm. A tub that fills when a toilet flushes puts the restriction below the point where those two fixtures meet, and every further flush adds to whatever surfaces first. Stop running water and stop testing. Skip the caustic bottle: it sits in the standing water and becomes a hazard for whoever opens the cleanout."""

B["symptom_3"] = """Sewage surfacing at a basement floor drain or the lowest toilet means the blockage sits downstream of the whole house. Shut off every water use, including the washer and the dishwasher, and keep people and pets off the wet floor. Here the homeowner owns that line all the way to its connection at the city main, so clearing it comes first and the pipe's condition is the next question."""

B["symptom_4"] = """Nothing at any fixture is a supply question, not a fixture question. Check a second tap, then check whether hot and cold are both dead, then find out whether the block still has water. A dry street points upstream of the meter pit, and the city takes water and sewer break reports at 720-898-7070 around the clock. Do not keep working a stiff main valve."""

B["services_summary"] = """Four jobs sit behind most after-hours calls in this part of Jefferson County, and they are priced nothing alike. Emergency repair is triage: find the failed system, stop the water, then decide whether the fault is even on your side of the meter pit. Burst pipe work is pressure-side work, and in a Front Range winter it usually starts in a garage wall or a crawl space. Drain cleaning removes a blockage that a machine can reach. Sewer line repair begins only after a camera proves the buried pipe itself is broken. Guess wrong and you pay for a second visit, or for a replacement you did not need."""

B["services_pick_head"] = "Pick the failure that matches your house tonight"

B["crosslink_head"] = "Seeing something else go wrong?"

B["svc_emergency_plumbing_repair_lede"] = """Water is loose, the taps have gone dry, or the heater has quit, and the first job is deciding which system failed. That decision governs the shutoff, the tools, and whether the trouble even sits on your side of the meter pit."""

B["svc_emergency_plumbing_repair_body"] = """### Sorting the symptom before anyone opens a wall

Cold and hot dead at every fixture is a supply problem: the service, the meter pit, or the main valve. Hot alone missing points at the heater or its shutoff. Water that keeps arriving with the house closed down is pressure-side. Dark water climbing out of the lowest drain is drainage, and the two send different trucks. Ask a neighbor whether they still have pressure. If the block is dry, the fault is upstream of your property and belongs to a utility crew, not to a plumber cutting into your wall.

### Where city pipe stops and your pipe starts

The city owns the water line from the drinking water main to the meter pit, and you own it from the meter pit to your foundation. Sewer runs the other way: care of the sanitary sewer service is yours from the house up to and including the connection at the city main. State law draws a third boundary that decides who may legally work where. Colorado defines plumbing as the work inside the building or within five feet of the foundation, and excludes the service line running from the first joint out to the property line.

### Colorado licenses the plumber, the city inspects the job

Most states hand plumbing licensure to individual cities. This one does not. The State Plumbing Board, inside the Department of Regulatory Agencies, licenses plumbers, apprentices and plumbing contractors for the whole state, and it deliberately does not regulate pipe fitters, drain cleaners or gas pipe installers. Three license classes exist. A master plans, lays out and supervises work, a journeyman installs and repairs it, and a residential license is limited to dwellings of one to four families that rise no more than two stories aboveground. One licensed plumber may supervise no more than three apprentices at the same job site, and board rule puts that supervisor at the permitted address or within five minutes of the apprentice. The Building Division checks those credentials against the statute before issuing a permit, and can take a violation to the board.

### The code edition an inspector will be holding

Board rule builds the state plumbing code on 2021 International Plumbing Code and International Residential Code language, and says later editions are not swept in. The city runs its own adoption cycle on top of that. Its 2024 International Plumbing Code arrived with the March 24, 2026 code package, replacing the 2018 books that had governed since October 2020. A water heater swap is not paperwork anyone can skip because the tank failed on a holiday. State rules require a licensed plumbing contractor, a permit and an inspection, with an exception for an owner who occupies the home. Inspections are weekday work, which is why finished and closed out are two different dates.

### Water heaters, closed systems and thermal expansion

Tanks fail in a short list of ways: a perforated shell weeping at a seam, a relief valve discharging, a corroded drain valve, a rotted nipple or flex connector. State rule requires relief valve discharge to be captured and carried to the drainage system or outside the building. One detail gets skipped constantly on the Front Range. Where cold supply reaches the heater through a check valve, a pressure reducing valve or a backflow preventer, the system is closed, heated water has nowhere to expand, and the code calls for a thermal expansion tank downstream of those devices. Colorado's rule adds that the tank be supported the way its maker specifies instead of hung from the piping. Any backflow assembly on the property also needs a certified tester every year, with a July 31 deadline in this city.

### Renting, and what state law counts as uninhabitable

Habitability statute lists running water at all times, plus hot water in the amount a tenant needs for cleanliness and health, among the characteristics a rental must have. Plumbing facilities kept in good working order sit on the same list. After notice, a landlord has to make contact within twenty-four hours and begin remedial work. The clock is twenty-four hours where the condition materially interferes with life, health or safety, and seventy-two hours where the unit is uninhabitable. Give that notice in writing and keep a copy with dated photographs.

### What the visit settles, and what moves the total

Flow stops first, or the failed branch gets isolated. Then the failure is identified rather than guessed at, tested under real load, and explained with the price attached before anything is cut. Four things move the number: how much has to come apart to reach the fault, whether the work stays inside that five foot envelope or continues out toward the meter pit, whether a permit and an inspection are involved, and what hour of the week it is."""

B["svc_burst_pipe_repair_lede"] = """A split supply line rarely announces itself while it is still frozen. The water shows up hours later, in a room nobody heats, and often at a spot where no ice ever formed. Finding that spot is the work."""

B["svc_burst_pipe_repair_body"] = """### The sequence that tells you a line froze

Two symptoms arrive in order. During the cold, one fixture loses flow while the rest of the house behaves normally, because ice has closed a single run. Later, once the weather turns and the plug melts, water appears. That second stage is when a ceiling stains or a crawl space starts dripping. Water travels along framing before it drops, so the wet spot marks elevation rather than the break. Clean water that keeps coming with every tap shut is pressure-side, and the meter settles the question: with the house closed down, a dial that will not come to rest means water is leaving the system somewhere.

### Why the pipe splits where there is no ice

Most people have this backwards. Ice pressing outward on the pipe wall is not what breaks copper. Code-body guidance built on research from the Building Research Council at the University of Illinois says it plainly: a break does not typically occur at the blockage. Once ice closes the bore completely, continued freezing squeezes the trapped water between that plug and a closed faucet, and pressure climbs in the confined column. Upstream of the plug, water can retreat toward its source, so nothing builds on that side. The pipe lets go in the section holding pressurized water, which is frequently somewhere with no ice in it at all. That mechanism is also why a faucet left dripping protects a run: an open outlet gives the pressure a way out.

### What winter on this side of the metro actually does

Cold here is documented, not folklore. The area record is twenty-nine below, set on January 9, 1875, and readings of twenty below or colder have occurred thirty times since 1872. Recent ones count too, including twenty-four below on December 22, 2022. Normal January lows sit at eighteen to nineteen degrees, and February normals only climb from nineteen into the low twenties. Freezing research on unheated spaces found uninsulated pipe beginning to ice up once outdoor air dropped to about twenty degrees, and a survey of plumbers put burst calls in the teens. Those are ordinary numbers for Jefferson County, not exceptional ones.

### Hose bibs, vacuum breakers and the hose nobody unhooked

The outdoor faucet is the single most common failure of the season. Plumbing code requires a sillcock, hose bibb or wall hydrant to carry a vacuum breaker, either an atmospheric or pressure type assembly or one permanently attached at the connection. That device keeps drinking water from being siphoned back out of a hose. It also holds water on the outlet side. A hose left connected through a freeze keeps water against the bib, and a frost-proof bib cannot drain the way it was designed to, so the split often lands back inside the wall where the stem seat sits. Pull hoses in the fall and close the interior isolation valve if the bib has one.

### The rooms that lose heat first

Garage walls take the worst of it, especially where a laundry or a bathroom was added on the far side of an uninsulated bay. Crawl spaces under the older blocks near Olde Town and the Stocke-Walter addition, where the Stocke plat dates to 1904 and the Walter subdivision to 1920, often carry plumbing through vented space with insulation that has slipped off the joists. Newer west-side subdivisions are not immune either. A soffit chase above a garage, or a run out to an exterior kitchen island, spends a January night at nearly outdoor temperature.

### What not to try while the water is off

No torch and no open flame behind plaster or in a crawl space, ever. A propane flame in a joist bay lights insulation and cooks wiring nobody can see. Do not leave a space heater unattended against framing. Do not clamp or tape a joint that still has pressure behind it. And do not close the main and walk away without opening the lowest fixture, because trapped water in a run that is still freezing keeps building the very pressure that split the pipe.

### One repair, or a branch that has failed twice

Sound pipe on both sides of a single break supports a cut and couple repair, a pressure test, and a careful look at everything the water reached. A run that has split twice in two winters is a different conversation, and being honest about which one you have separates a fair invoice from an oversold one. Copper fails at pinholes and at solder joints near dissimilar metal, galvanized fails at its threads, and crimped plastic fails at the crimp. Cost follows access. Exposed pipe in an open basement is quick, a line inside a finished wall brings drywall and paint behind it, and a failure out toward the meter pit turns into a trench, a permit and restoration."""

B["svc_drain_cleaning_lede"] = """Clearing a drain is a location problem before it is a machine problem. A trap, a branch, the building drain under the slab, and the buried line out to the main are four different jobs, and only one of them is cheap."""

B["svc_drain_cleaning_body"] = """### Which fixtures react, and what that rules out

A single slow lavatory is a trap or the arm behind it. A kitchen sink that fills while everything else drains is a branch loaded with grease. When a flush raises water in a tub, or washer discharge brings the basement floor drain up, the restriction sits below the point where those fixtures join, which puts it in the building drain or the buried service. Stop testing there. The useful report is short: what was used, where water came back, and how long it took to go down on its own.

### What the drain under an older house here is made of

City records put the water and sewer systems back in the early twentieth century, with the components in service now installed starting in the 1950s, and pipe funded between the 1960s and the 1980s is reaching the end of its useful life. Private drains follow the same eras. Cast iron scales inward until the bore is a fraction of its original diameter, and that rough surface catches paper. Older yard lines are frequently short clay sections joined every few feet. A cable will punch through a blockage in either material without telling anyone which one is buried out there, which is why the camera matters as much as the clearing.

### Cable, jetter, and the order that protects the pipe

A sectional machine or a drum cable with a cutting head is right for a root mass or a hard obstruction, because it cuts a channel and gets flow back. A jetter scours the full circumference with water and does better against grease, sludge and soft scale in a pipe that is structurally sound. Failure mode picks the tool. Sending high pressure water down a cracked clay joint or badly deteriorated cast iron can wash out the bedding beneath the pipe and enlarge the defect. Anyone selling a jetting before anything has looked inside the line is spending your money on a guess.

### Scale, and what local water does and does not explain

The city reports its supply as soft to moderately hard, from about 20 to 100 milligrams per liter and averaging 84, which is roughly five grains per gallon. It comes from Ralston Reservoir and Arvada Reservoir through two treatment plants. That is enough mineral to leave residue at aerators and to crust a heater fitting. It is not enough to be the reason a main drain closed. Deposits around a valve are a clue about the age of the fixture, while grease, wipes, roots and a sagging pipe are what actually stop flow.

### The cleanout decides how the day goes

An accessible cleanout is the difference between a machine in the line within ten minutes and a toilet lifted off its flange to get access. In houses remodeled twice, that cleanout is often buried under a deck, a flower bed or a new slab of patio concrete. Finding yours on a dry afternoon is worth more than most maintenance anyone could buy. If a machine stops at the same distance on every visit, that is neither the cable's fault nor bad luck; it is a defect with a measurable location.

### What not to put into a line that is holding water

Caustic and acid drain products do not open a main line. They pool in the standing water, hand a chemical burn to whoever opens the cleanout next, and can attack older pipe on the way past. Enzyme products do nothing to a root mass. A garden hose forced into a stack pressurizes a system that is already backed up. Running a shop vacuum on sewage moves contamination into the room you were protecting. Wipes labeled as flushable remain the most common reason a cleared line closes again within a month.

### How the visit runs, and what sets the number

Access comes first, then the blockage, then a real test: fixtures run under load rather than one hopeful flush, with the tool used named on the invoice. Length of run, number of bends, whether a toilet has to come up, and whether sewage has to be handled all move the figure. A camera pass afterward is its own step and worth buying once, because it turns "it drains for now" into a distance, a depth and a named defect. Repair, if the footage calls for one, is a separate scope and a separate decision."""

B["svc_sewer_line_repair_lede"] = """Repair enters the conversation when the buried line itself is the defect: a joint pulled apart, a belly holding water, a root ball rebuilt every spring. Cabling that pipe open again only buys a few weeks."""

B["svc_sewer_line_repair_body"] = """### The signs that point out into the yard

Backups returning weeks after a clearing that seemed to work. The lowest opening in the house filling first. A soft or sunken strip of lawn along the pipe's route. A machine that stops at the same measured distance on every visit. All of those point outdoors. One fixture misbehaving while everything else drains normally almost never does. Getting that distinction right is worth real money, because the two repairs are not in the same category.

### Where your responsibility ends on this side of the county

The city is blunt about it. Care and maintenance of the sanitary sewer service belongs to the homeowner from the house up to and including the connection at the city main, and the city does not cut, clean or televise that portion. What it does offer is unusual and badly underused. The Wastewater Division checks its own lines, and it will also sit down with a homeowner's televised inspection by appointment and give a second opinion on what the footage shows. Before anyone signs a replacement contract, that review carries none of the contractor's incentive. City crews maintain more than 450 miles of public sewer pipe behind the connection point where your responsibility ends.

### Clay tile, joints and the roots that find them

Roots do not bore through pipe. They locate a joint that has shifted, follow the moisture leaking out of it, then fill the bore with fine growth that catches paper and grease until nothing moves. Older sections of the city give them plenty to work with. The Stocke Addition was platted in 1904 and the Walter subdivision in 1920, and the blocks around Olde Town and the Reno Park Addition have had a century of street trees maturing over their yard lines. A cable cuts that growth back. It does not close the opening that admitted it.

### Ground that moves, and pipe that pays for it

Soil belongs in the diagnosis here. A soils and foundation summary filed in the city's own permit system for a townhome project identified expansive soil and bedrock, and recommended pressure testing under-slab plumbing, using flexible couplings, and isolating pipe where it passes through a slab. Clay that swells when wet and shrinks when dry works on joints for decades. Add settlement where bedding washed out from under a section and you get a belly, a low spot that holds water and solids between cleanings. None of that is visible from a basement floor drain.

### What a camera pass should actually produce

Footage is evidence, not decoration. A scope run with a surface locate should give you the distance from the cleanout to the defect, the depth, the pipe material, and the kind of defect: root intrusion at a joint, an offset, a crack, a belly, or a missing section. Watch it yourself instead of reading somebody's summary of it. Roots at one joint forty feet out is a spot repair. A collapsed length under a driveway approach is a different project, with a different price and a different permit path.

### Permits, licenses and the two days before a shovel

Digging here is regulated in layers. Work in the public right of way goes only to a contractor holding an active general municipal contractor license with the city, while a locally licensed plumbing contractor may permit work that stays on private property. An owner may repair their own line on private property and still needs the permit. Colorado law requires notice to the notification association at least two business days before excavation, not counting the day notice is given, and within eighteen inches of a marked utility the work has to go nondestructive. A locate confirmation number is required before the permit is approved, traffic control plans apply in the right of way, and a street under the cut moratorium adds a pre-construction meeting.

### Choosing a method, and why the range is so wide

Footage picks the method. One bad joint can be dug up and replaced. A sound but leaking run can take a cured-in-place liner. A pipe that has lost its grade has to be reopened and rebedded, because no liner rebuilds a slope. Depth is the largest single cost driver, followed by whatever sits on top of the line: lawn, mature landscaping, a concrete driveway, or pavement the city requires be restored to its own standard. A yard repair and a street cut are not the same project, and any estimate should name the restoration standard and say who calls in the locate."""

# --- rewrite existing blocks / append new ones -------------------------------
def set_block(text, key, body):
    pat = re.compile(r"(^## " + re.escape(key) + r"\n\n)(.*?)(?=\n## |\Z)", re.S | re.M)
    if pat.search(text):
        return pat.sub(lambda m: m.group(1) + body.strip() + "\n\n", text, count=1)
    return text.rstrip() + "\n\n## " + key + "\n\n" + body.strip() + "\n"

for k, v in B.items():
    text = set_block(text, k, v)

# pricing trims: shorten prose, keep every dollar figure; fix stale reinspection fee
trims = [
 ("Neither figure is large. What matters is the inspection each one schedules, because an inspection is a calendar slot and calendar slots are why a two-hour repair can span two days.",
  "Neither figure is large. What matters is the inspection each one schedules, because that slot is why a two-hour repair can span two days."),
 ("Reinspection at $77, traffic control plan review, and overtime inspection billed hourly with a two-hour minimum live in that same schedule, and all of it lands in the estimate somebody hands you.",
  "Reinspection at $125, traffic control plan review, and overtime inspection billed hourly with a two-hour minimum sit in the same schedules, and all of it lands in the estimate."),
 ("Clay that swells and shrinks with moisture pulls on joints for years, so under-slab drain failures here are a pattern rather than bad luck. City water runs soft to moderately hard, averaging about 84 mg/L or roughly five grains per gallon, so heavy scale is not the usual villain in a failed water heater around here. Freeze-thaw cycling and sediment are.",
  "Clay that swells and shrinks with moisture pulls on joints for years, so under-slab drain failures here are a pattern rather than bad luck. City water runs soft to moderately hard, averaging about 84 mg/L, so scale is rarely the villain in a failed water heater here. Freeze cycling and sediment are."),
 ("A trustworthy estimate names the failed component and the evidence for the call: the pressure reading, the camera footage timestamp, the depth and distance to the defect measured from the cleanout. It separates the diagnostic visit from the repair and states plainly whether the first amount applies against the second. It lists the permit as its own line, names who pulls it, and says which inspections are included. On any excavation it identifies the restoration standard: compacted backfill, concrete or asphalt patch to city spec, sod or seed, and who calls in the utility locate. Vague language on an excavation estimate almost always reappears later as an extra.",
  "A trustworthy estimate names the failed component and the evidence: the pressure reading, the footage timestamp, the depth and distance to the defect from the cleanout. It separates diagnosis from repair and says whether the first amount applies against the second. It lists the permit as its own line and names who pulls it. On excavation it identifies the restoration standard and who calls in the utility locate. Vague wording there reappears later as an extra."),
 ("The costly pattern in emergency plumbing is the jump from one clogged line to a full replacement proposal, signed at midnight while a basement floor is wet. A stoppage cleared on Tuesday and scoped on Thursday is the same information with a clear head attached. Two other habits deserve suspicion: hydro jetting sold before anyone has looked inside the pipe, and a monthly membership pitched during the crisis that quietly changes what the visit costs. Caustic drain chemicals poured into an old cast iron stack while waiting for help make the eventual repair worse, not cheaper.",
  "The costly pattern is the jump from one clogged line to a full replacement proposal, signed at midnight on a wet basement floor. A stoppage cleared Tuesday and scoped Thursday is the same information with a clear head attached. Two habits deserve suspicion: jetting sold before anyone has looked inside the pipe, and a membership pitched mid-crisis that quietly changes what the visit costs."),
 ("National cost pages quote parts and labor for a tidy version of the job. They leave out the Arvada permit and its inspection, the right-of-way permit, the pavement degradation charge, the concrete or asphalt patch, replacing landscaping torn up by a trench, and any drywall or paint that follows an interior repair. On winter work they also leave out frozen ground, which is slower to open and slower to compact back. The figure a homeowner remembers is the equipment. The figure that hits the invoice includes putting Arvada back the way it was found.",
  "National cost pages quote parts and labor for a tidy version of the job. They leave out the city permit and its inspection, the right-of-way permit, the pavement degradation charge, the patch, landscaping torn up by a trench, and drywall or paint after an interior repair. Winter work also brings frozen ground, slower to open and slower to compact back. The invoice includes putting the site back as it was found."),
]
for a, b in trims:
    if a not in text:
        raise SystemExit("trim target missing: " + a[:60])
    text = text.replace(a, b)

p.write_text(text)

sj = d / "site.json"
s = sj.read_text().replace('"phase": 1,', '"phase": 2,', 1)
sj.write_text(s)
print("done")
