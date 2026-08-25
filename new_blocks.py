import re, pathlib

p = pathlib.Path("/home/user/workspace/local-sites/sites/mesquiteacrepairpros.com/copy.md")
t = p.read_text()

sym = {
1: """This is the call that starts with a house that is fine at breakfast and unbearable by four o'clock. Before the equipment gets called undersized, take a reading: thermometer in the return grille, second reading at a supply register near the indoor unit, subtract. Something in the high teens is ordinary work. Six degrees is not. Put in a clean filter, then open the repair page.""",
2: """Plenty of air at the registers and none of it cold usually means the sealed circuit is short of charge. Look for frost collaring the tubing at the metering device and an oily smudge on the copper by the outdoor service valves. Nothing in that loop gets consumed, so the defect that let it out is the repair. Shut cooling off and read the leak page.""",
3: """Set the thermostat to off rather than to a lower number, because a loaded coil keeps making condensate for as long as the blower turns. Then work out where the water lands. A damp closet floor is a nuisance. A brown ring spreading on a ceiling below an attic air handler is drywall already being destroyed, and that version should not wait for Monday.""",
4: """Nothing hums, nothing clicks. Work through the cheap possibilities in order: thermostat batteries, cool mode, a setpoint below what the room reads, the service switch by the indoor equipment, the pull-out beside the condenser. If the breaker snaps back off the instant it is set, leave it alone. A stalled compressor pulls locked-rotor current, and every attempt bakes the windings further.""",
}

for n, body in sym.items():
    pat = re.compile(r"(## symptom_%d\n\n)(.*?)(?=\n## )" % n, re.S)
    assert pat.search(t), n
    t = pat.sub(lambda m: m.group(1) + body + "\n", t)

new = r'''
## services_summary

Four separate visits hide inside the phrase air conditioner repair on this side of Dallas County. General repair covers a house that never reaches the number on the thermostat and an attic unit sending water through a ceiling. Compressor work proves whether the outdoor pump still starts and still builds a pressure difference. Leak work finds where the charge escaped, which now decides whether an older machine is worth keeping at all. A tune-up is measurement and cleaning, booked ahead of the first long hot stretch. Choosing wrong costs a homeowner twice, because refrigerant weighed into a punctured coil leaves the same way it left before.

## services_pick_head

Start with the failure your system is actually showing

## crosslink_head

Looking at a different failure?

## svc_air_conditioner_repair_lede

Two very different complaints land on this page: a house that never reaches the number set on the thermostat, and water appearing under an attic unit. Airflow, drainage and heat transfer get measured before any part is named.

## svc_air_conditioner_repair_body

### The reading that settles the argument

Hold a thermometer in the return grille for two minutes, read a supply register close to the indoor unit, and subtract one from the other. Equipment doing its job takes the air down by something in the high teens on a hot afternoon here. A difference of six or seven degrees means the machine has stopped carrying the load, and no thermostat setting changes that. The opposite result is worth just as much. A wide difference in a house that keeps warming after lunch points at heat getting in faster than the system can remove it, or at cooled air leaking into an attic before it ever reaches the far bedroom.

### Condensate is the other half of this call

A cooling coil pulls moisture out of household air all day, and that water has exactly one intended path out. Plug the primary line, let the trap dry or foul, crack the pan, or stop the pump, and it finds another route. The mechanical code this city adopted in 2026 requires one of four protections anywhere an overflow could damage the building. Choices are an auxiliary pan with its own drain running to a spot you will notice, an overflow line tied in above the primary connection, an auxiliary pan carrying a listed water-level device that shuts the equipment down, or that device on its own. A pan has to be at least an inch and a half deep and three inches larger than the unit it sits under. When a ceiling stains, one of those four was missing, defeated, or already rusted through.

### Attic equipment is the local default, and the code says how it gets reached

Adopting the 2024 mechanical code, effective in July 2026, the city rewrote the attic appliance section outright. A passageway to the equipment must run at least 30 inches high and 22 inches wide, no more than 20 feet from the opening, with continuous solid flooring at least 24 inches wide and a level service space of 30 inches by 30 inches at the service side. Access comes by permanent stair, a pull-down stair rated for at least 300 pounds, or a door from an upper floor. Read that as a description of the working conditions above your ceiling. A coil or blower change up there is slow, careful, two-person work in punishing air.

### Two things to skip while you wait

Leave the breaker alone after the first trip, and stay off the attic ladder if the insulation is wet. Soaked drywall will not hold weight, the platform around an air handler is often minimal, and July attic air in this county is genuinely dangerous. Turning the thermostat to off is the whole of the useful response. It stops the coil producing water and it spares a compressor that may be cycling on its own overload.

### What shortens a part's life on the east side

Housing here came from two building waves. City records count 17,076 units, close to 31 percent of the stock, in the 1980s alone, another 8,158 from the 1970s, and roughly a fifth of the city standing before 1970. Mesquite Park, developed through the 1950s and early 1960s, has a median build year of 1959 and more than half its houses finished before 1960. Casa View Heights and Truman Heights went up in the same era along the Dallas line, and Sherwood Forest holds large lots built one at a time, some from the 1940s. Out at Falcon's Lair, on both sides of Interstate 20, the land was still farmland in 2000, so equipment there is a generation newer. What matters is less the decade than what got added later: a coil squeezed into an old closet, a return nobody enlarged, wiring reworked twice.

### Heat that finds the weak part

The weather office serving this area logged 23 days at or above 100 degrees in 2024 and reached 107 degrees on August 19 that year. In 2011 it recorded 71 such days, and the city's hazard plan notes a local high of 112 degrees back in 1980. First triple-digit readings keep no schedule: July 7 in 2026, June 23 in 2024. A capacitor or blower that coasted through a mild season is exactly the part that quits on the third afternoon of a long one.

### The order a competent visit follows

A useful sequence starts at the thermostat and ends at the gauges, not the other way around. Power gets verified at the disconnect and again on the low-voltage side of the board. The filter comes out for inspection, blower amps go against the nameplate, and static pressure tells whether air can move at all. At the condenser, a start attempt is watched while capacitance is metered and contact faces are examined for pitting. Both coil surfaces get looked at properly. Then the drainage path: pan, trap, line and float switch, tested rather than eyeballed. Refrigerant pressures come last, because a starved coil reads low no matter how much charge is in the circuit.

### What moves the figure

Small electrical parts, a float switch, a cleared trap: one trip, a tight range, nothing filed with the city. Anything above the ceiling costs labor before it costs parts. A leak search is priced on its own, apart from whatever repair follows it. Once equipment is being replaced rather than repaired, the job becomes permitted mechanical work with a duct rough-in and a mechanical final inspection behind it, and that belongs on the written estimate.

## svc_ac_compressor_repair_lede

A compressor is a pump, and it is the costliest thing inside the outdoor cabinet, which is why it takes the blame for failures that belong to a small part bolted a few inches away from it. A meter settles that question.

## svc_ac_compressor_repair_body

### Four descriptions that justify looking hard at the pump

A low hum lasting a second or two, a click, then nothing, repeating every few minutes while an internal overload trips and resets. A breaker that will not stay set. Cooling that behaves in the morning, gives up by late afternoon, and returns overnight. An outdoor fan spinning happily above a cabinet rejecting no heat whatsoever. Each of those has a cheap explanation and an expensive one, and the cheap explanation is the more common of the two.

### Measurements taken before anyone says the word

Line voltage gets read at the disconnect and again across the closed contactor while a cooling call is in place. Capacitance is metered and set against the value printed on the case, because a part that has drifted below its tolerance band will turn a motor on a mild morning and refuse at 104 degrees. Contact faces come under a light for pitting or welded spots. The compressor's draw gets compared with its rated load amperage, then winding resistance is measured and each winding checked against the shell for a ground. Suction and liquid pressure are recorded with the outdoor temperature written next to them, since that pair shows whether the pump develops a difference at all. Ask to hear those figures out loud.

### Why it fails in August and not in April

Head pressure climbs with outdoor temperature, and a compressor needs the most help starting exactly when the air around the condenser is hottest. A fading start component behaves for weeks, then strands a household on the day that matters. The station record shows how uneven the load is from year to year: 71 days at or above 100 degrees in 2011, 55 in 2023, 7 in 2025. A mild summer repairs nothing. It postpones the bill.

### Stop resetting it, and refuse the can

A compressor that cannot turn pulls several times its running current until something opens the circuit, and each reset drives that current back through insulation already damaged by heat. If the breaker trips the instant it is set, leave it open and mention it when scheduling. Turn down sealant sold in an aerosol can as well. It travels into the metering device and into the recovery equipment of the next person on the job, turning a repairable circuit into scrap.

### What the unit was dying of before it died

Compressors seldom fail alone. They fail from conditions: fins packed with mower clippings and cottonwood seed, a lazy condenser fan, a cabinet boxed in by a fence, or a charge that leaked out months earlier and left the pump running hot. Fitting a new one into those same conditions buys the same outcome a second time. Anyone proposing that repair should name the surrounding fault and correct it during the same visit.

### The federal rule that decides whether one box or two get replaced

Here is where a condenser failure gets interesting. The technology transitions program, at 40 CFR 84.54(c)(1), bars installing a new residential system that uses a refrigerant of 700 global warming potential or greater, with January 1, 2025 as the date. R-410A sits far above that ceiling. What the agency did not restrict is the market in replacement parts. A condensing unit counts as a specified component, and components produced for service work carry a permanent label reading "For servicing existing equipment only." Putting a new condensing unit onto an existing indoor coil is not treated as installing a new system. Replace that coil afterward and it is, and the refrigerant then has to sit under the limit. A final rule published on May 26, 2026 and effective that July removed the installation deadline for equipment built or imported before 2025, so remaining stock is not stranded. Manufacturing this class of equipment above the limit stayed prohibited.

### The A2L side of the decision, and what the city adopted

Anything installed new now runs a lower-GWP refrigerant that is mildly flammable. The agency lists R-454B at 470 and R-32 at 675 as acceptable subject to use conditions for this equipment class. Appliances holding them are certified to UL 60335-2-40, and many carry an integral refrigerant detection system with sensors mounted low in the cabinet, since the vapor is heavier than air. Minimum room area enters the calculation above roughly two pounds of charge in sealed factory equipment. Council adopted the 2024 mechanical code in May 2026, effective that July, and the amendments define a refrigerant detection system, send A2L high-probability systems to ASHRAE 15, and rework the machinery room and refrigerant shaft language. None of that pushes anyone off working equipment. It does mean a changeout is no longer the job it was three summers ago.

### Texas licensing, and what a changeout turns into here

Offering air conditioning and refrigeration work to the public in this state requires a contractor license from the Texas Department of Licensing and Regulation. A Class A license covers any size unit. Class B stops at 25 tons of cooling and 1.5 million BTU per hour of heating. The environmental air conditioning endorsement is the residential one, and the number reads TACL followed by class, digits and endorsement. Anyone performing non-exempt maintenance has to hold technician registration at minimum and work through that licensed contractor. The Building Inspection Division states that mechanical installations on new or remodel projects are to be installed and permitted by a state-licensed mechanical contractor, with duct rough-in and mechanical final inspections listed. Ask which credential is being used and who pulls the paperwork.

## svc_ac_refrigerant_leak_repair_lede

A cooling circuit is sealed, so refrigerant is not a supply that runs down. Low charge means a defect let it out, and finding that defect is the work. Anything short of that is a recharge with an expiry date on it.

## svc_ac_refrigerant_leak_repair_body

### The pattern that says charge is escaping

Most of these announce themselves before a gauge goes on. Air keeps arriving at the registers with no bite to it while the condenser runs and runs. Frost collars the tubing at the metering device and works outward along the insulated line. There is an oily film on copper, or a dark patch on the pad, because compressor oil rides out with whatever escapes. Strongest signal of all: the house got a little worse across each of the past three summers instead of failing on one particular day.

### Where these systems give up

Begin at the evaporator coil, which in most houses here sits in the attic. Tubing that spends five months a year wet develops pinhole corrosion, and that coil is both the likeliest source and the worst one to reach. Next come the brazed joints at the condenser, worked by thermal cycling through a season that ran 23 triple-digit days in 2024. Then the line set where it passes through brick or hides behind shrubs nobody has moved in a decade. Then the Schrader cores under the service caps, a genuine leak in a part that costs almost nothing. Last, factory fittings on equipment that has already been swapped once, which describes plenty of streets in Casa View Heights and Mesquite Park.

### No federal rule orders this repair, and that is the point

Two rules reach a house system, and neither one requires fixing the hole. Venting refrigerant during service, repair or disposal is prohibited, so what comes out must be recovered. Opening the circuit calls for Section 608 certification, and refrigerant may be sold only to certified technicians or their employers. Attaching gauges to read pressure is itself enough to make someone a technician under that rule. The corrective-action deadlines people quote apply to appliances holding 50 pounds or more, which no split system in a house here does. Repair is therefore not a legal duty. It is arithmetic, and the arithmetic moved.

### Why a leaking R-410A machine is now a money decision

Supply is the reason. The phasedown enacted under the AIM Act cut production and consumption allowances to 60 percent of baseline for 2024 through 2028, steps down to 30 percent for 2029, and heads toward 85 percent below baseline by 2036. Equipment above the 700 ceiling stopped being built for this class at the start of 2025, though components for existing systems are still made and sold, labeled for service work only. Charge for a legacy system remains legal to buy and use. It also gets scarcer and dearer as allowances shrink. That is why a pinholed attic coil beneath a fifteen-year-old condenser deserves both prices side by side, and why an accessible joint on newer equipment is simply worth fixing.

### What a real search looks like

The first number is standing pressure, written down, because a circuit holding nothing and one that is merely low get different treatment. Where no pressure is left, nitrogen goes in dry and the system is split so the losing half can be identified. Where the loss is gradual, the tool is an electronic detector rated for that refrigerant. It gets run slowly across the coil face, every joint and the whole length of the line set with the blower switched off. Anything it flags is confirmed with bubbles before it gets called a leak. After the repair comes evacuation to a micron target that has to hold with the pump valved off, since trapped moisture turns acidic inside the circuit. Charge is weighed in to the data plate figure and a fresh temperature split gets measured at a register.

### Corners that get cut

Dye injected with no return visit ever scheduled to look for it. A detector swept over a coil for twenty seconds. Soap bubbles used alone on a system that only leaks while it runs. A vacuum pulled for ten minutes with nothing but a compound gauge on the manifold. Charge judged by pressure on a fixed-orifice system, which is guesswork with an instrument attached to it.

### What the cost depends on

Where the leak hides sets nearly all of it. A valve core or an exposed joint at the outdoor unit is a short visit and a trivial part. A coil inside an attic air handler, or a line set buried behind masonry, is hours of labor before any refrigerant is weighed in, and refrigerant is billed by the pound with the type named. Should the coil or the outdoor unit end up replaced instead of repaired, the work turns into permitted mechanical work with city inspections attached to it.

## svc_ac_tune_up_lede

Maintenance earns its money only when it leaves behind readings you can compare next spring. A page of check marks says nothing about whether this system survives a Dallas County August with its capacitor and its drain intact.

## svc_ac_tune_up_body

### Numbers that belong on the invoice

A maintenance visit is worth what it measures. Ask for the return and supply air temperatures and the split between them, the static pressure the blower is working against, and the draw of both motors set beside their nameplate ratings. Ask for compressor amps against rated load, the measured capacitance of each run capacitor next to the value printed on its case, and suction and liquid pressure with the outdoor temperature recorded alongside. Superheat or subcooling depends on which metering device the system uses. A figure logged in March is what proves in July that something has drifted.

### Book it against the local calendar, not the thermometer

The window is shorter than most people think. This station recorded 7 triple-digit days in 2025 and 23 in 2024, with the first 100-degree reading landing on July 7 in 2026 and June 23 in 2024. A cool year hides weak parts rather than curing them. March and April are when a truck is available and a capacitor sliding toward failure can still be caught. Once a long hot stretch settles over the county, every shop in the area is already committed.

### Fins have to be able to pass air

Heat collected indoors leaves through the outdoor coil, and only if air can travel through the fins. Clippings thrown by a mower, cottonwood seed and dust pack that surface until head pressure rises, capacity drops and current climbs. Cleaning it properly often restores most of a missing temperature split with no parts at all. Homeowner limits are worth knowing. Power off at the disconnect and a gentle hose rinse, working from inside the coil outward, is reasonable. A pressure washer lays the fins over permanently, and a screwdriver does the same damage faster.

### Prove the float switch actually shuts it off

Equipment above a finished ceiling makes condensate directly over the rooms you live in, so drainage deserves more attention here than the coil does. Pan, trap and line get flushed. The float switch gets lifted by hand to show it truly stops the system, since that one inexpensive part stands between a plugged line and destroyed drywall. A rusting secondary pan gets flagged before it fails rather than after. The code adopted this year spells out the alternatives: a pan with its own drain to a visible discharge point, an overflow line above the primary, or a listed water-level device that shuts the equipment off.

### Parts get changed because an instrument said so

Contactors and capacitors work on every start, and both wear in ways a meter can see. Capacitance slides down from its rating. Contact faces pit and eventually weld. Motor bearings tighten and pull more current. That is the correct basis for replacing something. A line item reading preventive replacement with no measurement beside it is a sale. The reverse holds too. A new buzz, a repeated trip, a burnt smell or a stopped fan is a repair to be scoped and quoted, not folded quietly into a maintenance ticket.

### What A2L equipment adds to the visit

Systems going in new today use lower-GWP refrigerants that are mildly flammable, which changes the checklist rather than the calendar. Appliances built for them are certified to UL 60335-2-40, and many include an integral refrigerant detection system whose sensors sit low in the cabinet because the vapor is heavier than air. On those units a visit should confirm the sensor is the specified part number, mounted where the manufacturer requires, wired to the board, and not defeated by anyone. Detection tools and recovery gear have to be rated for the refrigerant present. The 2024 mechanical code in force here carries the definitions and points these systems at ASHRAE 15.

### What maintenance cannot do

It finds conditions. It does not cure a pinholed coil, a failed compressor, scorched wiring, or duct that was never sized for the house, and it cannot promise a season without a breakdown. Maintenance is flat-rate work in this market, priced as a visit rather than by the machine, and the range moves with the season instead of with the equipment. Anything measured by the pound, and any part swap, sits outside that price. Each is a separate scope, quoted on its own, for you to approve or decline.
'''

t = t.rstrip() + "\n" + new
p.write_text(t)

# flip phase
sj = pathlib.Path("/home/user/workspace/local-sites/sites/mesquiteacrepairpros.com/site.json")
s = sj.read_text()
assert '"phase": 1' in s
sj.write_text(s.replace('"phase": 1', '"phase": 2', 1))
print("done")
