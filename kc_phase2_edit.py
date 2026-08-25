import re, json, io, sys

P = "sites/kansascityemergencyplumber.com/copy.md"
src = open(P, encoding="utf-8").read()

def block(name, text):
    return f"## {name}\n\n{text.strip()}\n\n"

# --- parse into ordered blocks ---
parts = re.split(r"(?m)^## (\S+)\s*$", src)
head = parts[0]
blocks = {}
order = []
for i in range(1, len(parts), 2):
    k = parts[i]; v = parts[i+1].strip()
    blocks[k] = v; order.append(k)

SYM = {
1: """A pressurized line that has opened up is a shutoff problem before it is a repair. Close the valve nearest the leak if it turns freely; otherwise close the main where the service enters the basement. Stay away from water that has reached an outlet, a cord, or a panel. Never put a flame on a suspect frozen pipe. The burst pipe page covers the thaw sequence and the repair choices.""",
2: """One toilet climbing toward the rim is usually blocked at that fixture. Close the small stop valve behind the bowl and stop flushing to test it. If a tub or a basement floor drain reacts at the same moment, the restriction sits farther along the building drain, so stop all water use. Cabling, jetting, and camera work are laid out on the drain cleaning page.""",
3: """Wastewater at the lowest floor drain, or a sewage smell that will not clear, points outdoors rather than at a trap. Stop every fixture in the building, keep people and pets off the wet floor, and report the backup to KC Water so the public main is checked before anyone digs. Roots, clay joints, and lateral ownership are on the sewer line page.""",
4: """No water at a single faucet is local to that fixture. Nothing anywhere, hot or cold, is a supply problem. Check whether the main valve was left closed after recent work, then look for a wet strip of ground along the service route from the meter. Do not start opening pipe to find out. The emergency repair page sorts one from the other.""",
}
for i, t in SYM.items():
    blocks[f"symptom_{i}"] = t.strip()

NEW = {}

NEW["services_summary"] = """Four separate jobs hide behind one late-night phone call. Emergency plumbing repair sorts the hazard: what is wet, what is still pressurized, and what has to be isolated tonight. Burst pipe repair is pressure-side work, and February in this city generates most of it. Drain cleaning removes a blockage a cable or a jetter can physically reach. Sewer line repair begins only after a camera proves the lateral itself is broken, offset, or packed with roots. Mixing those up gets expensive on the Missouri side, because a basement backup can belong to a public combined sewer, to your own buried lateral, or to both at once."""

NEW["services_pick_head"] = "Start with the failure your basement is actually showing"

NEW["crosslink_head"] = "Something else going wrong downstairs?"

NEW["svc_emergency_plumbing_repair_lede"] = """Emergency plumbing repair is the first hour of the job: find what is wet, decide what has to be shut off, and separate a supply failure from a drainage failure before anybody opens a wall in a century-old midtown house."""

NEW["svc_emergency_plumbing_repair_body"] = """### Sorting the call before anything gets cut

Three questions do most of the diagnostic work. Is clean water still arriving with every fixture closed, which points at the pressure side? Does the wet spot only appear while a shower or a washer runs, which points at drainage? Is one fixture involved, or the whole building? A basement puddle in this city can come from a split supply line, a water heater that failed at the tank, a floor drain receiving sewage, or groundwater working through a foundation crack. Those are four different repairs, and two of them are not plumbing work at all.

### Where your responsibility starts and the utility's ends

KC Water states the boundary plainly: the customer maintains and repairs the private residential sewer lateral from its connection at the sewer main all the way to the building plumbing. The utility keeps up the sanitary mains, which usually run beneath the street or through back yards. On the supply side, a KC Water permit governs work on a service line from the first valve to the building. Establishing which pipe is yours before a shovel appears is what keeps a homeowner from paying for the public half of the system.

### A permit question worth answering before the estimate

The city requires permits before most plumbing work, and the exempt list is short. Clearing a stoppage is exempt. So are repairs to the working parts of a faucet or valve, swapping a defective fixture when no piping is altered or extended, and replacing a lavatory or sink trap. Anything that alters or extends piping needs a permit and an inspection. An owner who occupies a single-family house may pull that permit for work performed personally. Anyone else doing the work has to hold a city contractor license, which starts with a trade Certificate of Qualification.

### Cold here has a documented ceiling

The weather service puts the coldest temperature ever recorded in Kansas City at 23 below zero, on December 22 and 23 of 1989, and the coldest December-through-February season on record averaged 21.5 degrees in 1978 and 1979. Numbers like that explain why emergency plumbing here is seasonal in a way it is not in milder markets. When a hard snap lands, supply houses run out of couplings inside a week and every truck in the metro is booked at the same hour. That timing is a cost driver, not a sales tactic.

### Four things not to try while help is coming

Do not hold a torch or a heat gun against a frozen line, especially inside a joist bay behind lath and plaster. Do not stand in water to reach a breaker panel. Do not keep flushing a bowl that is already near the rim. Do not pour a caustic product into standing wastewater that somebody will have to reach into an hour later. If a gas water heater is leaking, close its gas valve and its cold inlet before you worry about the puddle.

### The shortcut that turns one repair into three

A skipped diagnosis is the pattern that costs people real money here. A floor drain surges during a downpour and gets quoted that same night as a full lateral replacement, before anyone has run a camera or asked whether the public line is clear. KC Water asks customers to report backups so it can verify the main serving the property, and its published guidance is that if the backup continues after that check, the next call belongs to a plumber. Following that order costs one phone call and can save an excavation.

### How the visit runs, and what sets the number

Flow stops first, by a valve, a cap, a clamp, or a cleared line. Then the system gets tested under real use instead of being declared fixed. Then the scope should arrive in writing with evidence attached: a photograph of the failed fitting, or footage with a distance and a depth on it. Access drives the figure more than anything else. Exposed copper above a laundry sink is a short visit. The identical failure inside plaster and lath is a repair, plus demolition, plus a plasterer on a later day."""

NEW["svc_burst_pipe_repair_lede"] = """A burst pipe here is usually a February pipe: a line in an unheated crawlspace, a garage wall, or an exterior kitchen run that froze, split at its weakest point, and began spraying only as the ice plug let go."""

NEW["svc_burst_pipe_repair_body"] = """### How you know a supply line let go

Clean water that keeps coming with every tap closed is pressure-side water. Watch the meter with the house shut down; a dial that will not settle means water is leaving the system somewhere between the meter and the last fixture. A frozen line usually gives two signs in sequence. First no flow at one fixture during the snap, then water appearing hours later once the ice melts and the split behind it opens. Because the stain forms below the break, a wet ceiling tells you about elevation, not location.

### Find the main shutoff before the night you need it

On most houses here the main valve sits where the service enters the basement, near the meter and ahead of the branch to the water heater. It closes clockwise. Older gate valves in Northeast and midtown basements have sat untouched for decades and can seize or shear at the stem, which makes them worth replacing on a dry afternoon rather than during a flood. After closing the main, open the lowest fixture in the building to drop residual pressure. The curb side is not a homeowner's valve; KC Water treats work on the service from the first valve to the building as permitted work.

### What the decade of the house suggests

Housing stock in the neighborhoods where these calls cluster is genuinely old. Pendleton Heights was platted in the early 1880s and the National Archives at Kansas City calls it the city's first suburb. In the South Hyde Park district, 522 buildings went up between 1900 and 1910, roughly 67 percent of the district, and city water and sewer lines were complete there in 1905. Brookside's plats followed shortly after, with Rockhill Park and Rockhill Place platted in 1908. Galvanized steel supply, cast iron waste, later copper repairs, and a stray plastic transition often coexist in one such basement.

### The freeze records behind the call volume

Cold here is not folklore. In a Kansas City record that runs back to 1889, February daily record lows reach 22 below on the 12th, set in 1899. The 2021 event took three consecutive date records with lows of 6 below, 10 below, and 13 below on the 14th, 15th, and 16th. Normal lows through the first half of February sit in the low twenties. Pipe in a garage bay, an uninsulated crawlspace, or a north-facing kitchen wall spends a snap like that at very nearly outdoor temperature.

### What not to do with a frozen or split line

No open flame, no propane torch, no unattended space heater shoved against framing. A torch behind old plaster starts fires and cooks concealed wiring you cannot see. Do not raise the thermostat and leave town for the weekend on the theory that the line will thaw quietly on its own. Do not try to tape or clamp a joint while it is still under pressure. And do not close the main and walk away without opening a faucet, since trapped water in a wall that is still freezing keeps expanding.

### Section repair or a planned repipe, decided honestly

Sound pipe on both sides of a single failure supports a cut-and-couple repair, followed by a pressure test and a look at everything the water reached. A run that has produced three pinholes across two winters is a different conversation. Threaded galvanized fails at its joints. Copper fails at pinholes and at solder joints near dissimilar metal. A crimped plastic fitting fails at the crimp. An honest version of this discussion names which of those you actually have and prices the affected branch, unless the evidence really does implicate the whole house.

### Insulation, heat, and the outdoor version of this job

Once the pipe is repaired, what keeps it repaired is heat and insulation in the space that froze, plus a way to isolate that run next time. If the failure turns out to be outdoors on the water service, the work changes character completely: a trench dug below frost, limestone in plenty of local trenches, a utility permit, and restoration of whatever the trench crossed. Buried work also carries a legal step. State law requires notifying utilities at least 48 hours before excavation, and KC Water's own sewer regulations restate that requirement."""

NEW["svc_drain_cleaning_lede"] = """Drain cleaning means locating where flow actually stops: a fixture arm, the building drain under the basement slab, or the lateral running out toward the main. In an old Kansas City house those three carry very different price tags."""

NEW["svc_drain_cleaning_body"] = """### Which fixtures react, and how far down that puts it

A single slow lavatory is a trap or a fixture arm. A kitchen sink that fills while everything else drains normally is a branch loaded with grease. When a flush raises water in a tub, or a washer discharge brings up the basement floor drain, the restriction sits below the point where those fixtures join, which means the building drain or the lateral. Stop testing once you see that. Every extra cycle adds gallons to whatever overflows first, and the lowest opening in the house is where it will land.

### What an old drain here is actually made of

Cast iron drain, waste, and vent piping was standard in houses built from the 1950s into the early 1980s, and local inspection work still turns up original cast iron and lead in homes of that vintage. Go back further and the yard line is often clay tile in short sections with mortared or gasketed joints. Cast iron scales inward until the bore is a fraction of its original diameter, while clay stays smooth and separates at the joints instead. A cable will punch through either kind of blockage without telling you which one you own.

### Cable, jetter, and the choice between them

A sectional machine or a drum cable with a cutting head is the right tool for a root mass or a hard obstruction. It cuts a channel and gets flow back. A jetter uses water to scour the full circumference and is better against grease, scale, and sludge in a pipe that is structurally sound. Failure mode decides which one belongs in the line. Jetting an already-cracked clay joint or badly deteriorated cast iron can wash out bedding and enlarge the defect. Anyone quoting a jetting before looking inside the pipe is guessing with your money.

### Roots find the joints, not the pipe

Roots do not drill through clay tile. They locate a joint that has shifted, follow the moisture leaking out of it, and then fill the bore with fine hair growth that catches paper and grease. Blocks in Brookside and Waldo, laid out on plats from around 1908 and now shaded by mature street trees, produce this on a seasonal cycle. KC Water's own maintenance advice for private lines suggests cleaning with a three-inch blade about every six months where trees or large shrubs sit near the lateral. Cutting roots is maintenance; the joint that admitted them is a separate decision.

### Rain, and the combined sewer under older neighborhoods

Combined sewers serve an area of about 56 square miles south of the Missouri River, carrying sanitary flow and, during rainfall, stormwater in the same pipe. A floor drain that surges during a downpour and then clears on its own is telling you something different from a drain that stays sluggish in dry weather. City law prohibits connecting gutters, downspouts, driveway sump pumps, and yard area drains into the sanitary system, because that inflow is what pushes flow past capacity. Ruling those out on your own property is worth doing before blaming the pipe under the lawn.

### What not to put down it

Caustic and acid drain products do not clear a main line. They pool in standing water and hand a chemical burn hazard to whoever opens the cleanout next. Enzyme products accomplish nothing against a root mass. A garden hose forced into a stack pressurizes a system that is already backed up. Running a wet vacuum on sewage creates a contamination problem in the room you were trying to protect. Wipes sold as flushable remain the most common single reason a cleared line closes again.

### How the visit runs and what sets the cost

Access comes first. An accessible cleanout is the difference between a straightforward clearing and pulling a toilet to get a machine into the line. Then the blockage is removed, the affected fixtures are run under real load, and the tool used gets named on the invoice. In market terms, rodding through a basement cleanout sits in a fairly tight band, camera work is priced as its own step, and a lateral repair belongs to a different category entirely. Length of run, number of bends, and whether a second pass is needed all move the figure."""

NEW["svc_sewer_line_repair_lede"] = """Sewer line repair starts where cleaning stops: a lateral that is cracked, offset, root-packed, or sagging, and that will keep sending wastewater into the basement no matter how many times a cable goes through it."""

NEW["svc_sewer_line_repair_body"] = """### The symptoms that point at the yard

Repeat backups after a cabling that seemed to work, the lowest drain in the house filling first, a soft or sunken strip of lawn along the line's route, and a sewage smell downstairs after rain all point outdoors. So does a machine that stops at the same distance every visit. One fixture backing up while everything else drains normally almost never means the lateral. Getting that distinction right matters, because the two repairs differ by an order of magnitude in what they cost.

### Where the city's pipe ends and yours begins

The utility puts it directly: the customer is responsible for the private residential sewer lateral from its point of connection at the sewer main to the building plumbing. KC Water maintains the mains themselves, typically under the street or in back yards. When a plumber cannot open a lateral, the published procedure has that plumber call the utility's investigations and inspections line to verify where the blockage sits, and any push-camera footage must be presented for review. In limited cases the director may authorize repair of a defective portion of a private line inside the city's right-of-way or easement, with a total blockage or a no-relief situation among the listed conditions.

### The consent decree running in the background

Sewers here operate under federal supervision. A judge signed the original Clean Water Act consent decree on September 27, 2010, after the EPA counted roughly 1,300 illegal overflows since 2002. That count included combined sewer overflows, sanitary sewer overflows, and private property backups, together discharging about 6.5 billion gallons of untreated sewage a year. The work began as a 25-year, $4.7 billion Overflow Control Program, renamed KC Smart Sewer in 2017. A third amendment signed on March 3, 2021 pushed final compliance from 2035 out to 2040 and reduced the cost through 2035 to $2.3 billion. Two things follow for a homeowner. A backup on private property is inside the federal count, so reporting one is not a nuisance call. And cracked combined sewer pipe 12 inches and smaller is being rehabilitated, so the main outside your house may already be on a list.

### Camera first, then the choice of method

No lateral should be replaced on the strength of a machine operator's opinion. A camera pass with a surface locate should produce the distance from the cleanout to the defect, the depth, the type of defect, and the pipe material, and you should watch the footage rather than read a summary of it. Roots at a joint forty feet out is a different project from a collapsed section beneath the driveway apron. What the footage shows decides the method: a spot repair at one joint, a cured-in-place liner through a sound but leaking run, a pipe burst pulling new material along the old path, or open trench where grade has to be rebuilt. Depth, length, what sits on top of the pipe, and whether the street has to be cut and repaved are what make the honest range for this work so wide.

### Clay tile and a century of settlement

Yard lines in the older districts are frequently short clay sections. Pendleton Heights dates from plats of the early 1880s. South Hyde Park had city water and sewer complete by 1905, with most of its 700-plus houses finished between 1900 and 1910. The Brookside plats came in 1908 and 1909, and two-thirds of the surveyed blocks near the Plaza went up during the 1910s. A century of frost cycles, shifting clay soil, street tree roots, and settlement moves those joints a fraction of an inch, which is all a root needs to get in. Bellies form where bedding washed out beneath the pipe. None of it is visible from the basement.

### Permits, licensing, and the 48 hours before a shovel

A permit is required before an existing sewer service is altered, extended, repaired, or renewed, covering the run from the main to a point one foot inside the property line. Work begun without that permit carries a tripled fee, and a permit lapses after 180 days. A sewer service connecting to a pressurized or surcharged main needs a backflow permit for the required prevention assembly, which is the mechanism that protects a basement from a surcharged pipe. Excavation requires notice to utilities at least 48 hours ahead under state law. Plumbing permits go to licensed contractors, with owner-occupants of single-family houses the narrow exception for their own labor.

### Renting here, and what Missouri actually allows

A sewage backup in a rented duplex is the landlord's problem, and the state's self-help remedy is narrow. Missouri's repair-and-deduct statute requires the tenant to have lived there six consecutive months with rent paid, and the condition must violate a local housing or building code. The reasonable cost has to stay under three hundred dollars or half the periodic rent, whichever is greater, and it can never exceed one month's rent. The landlord gets fourteen days after written notice, or as promptly as required in case of an emergency. Deductions cannot total more than one month's rent in any twelve-month period. A lateral replacement sits far outside those limits, so a tenant's practical move is written notice and a call to the city rather than a contract with a plumber."""

for k, v in NEW.items():
    blocks[k] = v.strip()
    if k not in order:
        order.append(k)

out = io.StringIO()
out.write(head if head.strip() else "# Copy — kansascityemergencyplumber.com\n\n")
for k in order:
    out.write(block(k, blocks[k]))
open(P, "w", encoding="utf-8").write(out.getvalue())
print("written", len(order), "blocks")
