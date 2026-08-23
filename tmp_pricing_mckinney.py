import json, pathlib

d = "mckinneygaragedoorrepairpros.com"
p = pathlib.Path("sites") / d / "site.json"
s = json.loads(p.read_text())

s["pricing"] = {
    "mode": "cost",
    "table_head": "What the seven common door jobs run in McKinney",
    "anchors": [
        {
            "label": "Residential alteration permit, per square foot",
            "value": "$0.68",
            "detail": "The city prices a residential alteration at $0.68 per gross square foot of affected area, so a 16-by-7 door works out near seventy-six dollars. Doors and windows are listed among repairs that need a permit.",
            "source_name": "City of McKinney building permit fee schedule for new construction, remodels and repairs",
            "source_url": "https://www.mckinneytexas.org/DocumentCenter/View/358/Fee-Schedule"
        },
        {
            "label": "First reinspection, failed inspection",
            "value": "$50",
            "detail": "Charged when an inspector has to return to the same address a second time. A door replacement that is not ready when the slot arrives pays this and waits for the next opening.",
            "source_name": "City of McKinney reinspection fee line",
            "source_url": "https://www.mckinneytexas.org/DocumentCenter/View/358/Fee-Schedule"
        },
        {
            "label": "Median hourly wage, carpenters, Dallas-Fort Worth-Arlington",
            "value": "$23.44",
            "detail": "May 2025 median hourly pay across the 9,480 carpenters counted in this metro, the occupation group door hanging falls under. Loaded onto a truck, insurance and parts stock, the billed hour runs several times that.",
            "source_name": "BLS Occupational Employment and Wage Statistics, May 2025",
            "source_url": "https://www.bls.gov/oes/current/oes_19100.htm"
        }
    ],
    "rows": [
        {
            "job": "Trip out to find why the door will not open",
            "low": 75,
            "high": 175,
            "basis": "per visit",
            "note": "Weekday mornings sit at the bottom. Storm weeks, weekends and after-dark slots sit at the top, and distance north of 380 adds drive time."
        },
        {
            "job": "One snapped torsion spring replaced over a double-wide door",
            "low": 235,
            "high": 525,
            "basis": "flat",
            "note": "Wire size and drum condition decide it. A spring that failed after twenty years usually took the bearings and cables with it."
        },
        {
            "job": "Both springs swapped for a higher cycle-rated set",
            "low": 360,
            "high": 780,
            "basis": "flat",
            "note": "Builder springs on this city's boom-decade streets are rated near ten thousand cycles; a longer-life pair costs more up front."
        },
        {
            "job": "Cables and drums reset after the door jumped its rails",
            "low": 180,
            "high": 460,
            "basis": "flat",
            "note": "A single wrapped cable is quick. A door hanging crooked with a bent flag bracket needs the section squared before it lifts again."
        },
        {
            "job": "Nylon rollers and worn hinges replaced end to end",
            "low": 150,
            "high": 380,
            "basis": "per unit",
            "note": "Sealed-bearing rollers cost more than the stamped ones a builder used. A short-panel door has more hinges to reach."
        },
        {
            "job": "Opener logic board or gear kit replaced",
            "low": 170,
            "high": 450,
            "basis": "flat",
            "note": "Parts for a common chain head are stocked. A discontinued board on a twenty-year-old unit pushes toward replacing the head instead."
        },
        {
            "job": "Two dented sections replaced on a hail-struck door",
            "low": 600,
            "high": 1700,
            "basis": "flat",
            "note": "Matching a discontinued panel profile and color is the hard part; a bowed strut or twisted vertical rail has to be corrected too."
        }
    ]
}
p.write_text(json.dumps(s, indent=1, ensure_ascii=False) + "\n")

copy = pathlib.Path("sites") / d / "copy.md"
t = copy.read_text().rstrip() + "\n\n" + """## pricing_lede

This page lays out what garage door work actually runs in McKinney, what the city charges to permit and inspect a door replacement, and which features of a Collin County house drive a repair toward the top of its range.

## pricing_body

### Where the spread in each row comes from

Three things set the number, and the brand stamped on the door is not one of them. The first is which part gave out. A snapped torsion spring is hardware plus careful, practiced labor. A door that has walked off its rails has usually chewed a cable, flattened two rollers and bent a hinge on the way down, so what looks like one failure is a short list of parts. The second is the door itself: width, weight, and whether it is insulated. A sixteen-foot insulated door weighs enough that it needs different spring wire than the single-layer door a builder hung on the same street, and the correct spring costs more than the convenient one. The third is when somebody is standing in the driveway. A Wednesday morning slot and a Saturday afternoon during a storm week are not the same labor, because the second one pulls a technician off a booked route.

### What a boom-decade city does to a repair bill

The city's own housing profile reports that 85 percent of homes here went up after 1990 and 40 percent of them between 2000 and 2009. That concentration shows up in pricing in a way most markets do not share. Entire streets received the same builder package, generally one torsion spring rated near ten thousand cycles carrying a double-wide door, and identical packages wear out on roughly the same schedule. So when a spring lets go on a house of that vintage, the bearings, the cables and the opener gearbox are exactly as old, and the repair that actually holds covers two or three items rather than one. That is the difference between the bottom and the top of the spring row. The small pre-war pocket near the downtown square inverts the problem: parts are inexpensive, headroom is shallow, hardware is often side-mounted, and the time on site is what costs.

### The permit money is small, the sequence behind it is not

McKinney lists doors and windows among the repairs that require a permit, and prices a residential alteration at sixty-eight cents per gross square foot of affected area. On a standard double door that is about the price of a roller set, which is to say irrelevant next to the door. The calendar is the real cost. A replacement carries a filing, an inspection window somebody has to be home for, and a fifty-dollar charge if the inspector arrives to work that is not ready. A job sold as a two-hour installation with none of that in the schedule quietly becomes two appointments. Repairs sit outside all of it: a spring, a cable, a roller set or an opener head is service on the existing door, not a door replacement.

### The trap in this market is hail

Collin County storms bruise door skins, and a dent count is the easiest thing in this trade to sell against. Skin damage is cosmetic and can wait on an adjuster. What actually stops a door is a vertical rail knocked out of plumb or a strut bowed across the back of a section, and both keep destroying rollers on every cycle until somebody corrects them. So the pattern to refuse is a full replacement proposal written from photographs of dents while nobody has put a level on the track. The smaller version is the cheap tune-up call that arrives as an advertised inspection and leaves as a spring, opener and roller package agreed in a driveway in ninety-eight-degree heat.

### What a real quote spells out

A quote worth signing names the spring by wire size, inside diameter and cycle rating rather than calling it heavy duty. It gives the cable diameter, the roller count and whether those rollers carry sealed bearings. On an opener it names model, drive type and horsepower, says whether the old head and rail leave with the truck, and states whether a strut has to be added before an opener pulls on a single-layer door. On a replacement it lists the permit, the inspection, disposal of the old sections, and any architectural review a community such as Stonebridge Ranch expects before a different panel style shows up on a street. Labor and trip charges belong on their own lines, not folded into a part.

### What the number found online leaves out

National averages assume a technician who is already nearby. This city sprawls from Trinity Falls to the south side, and drive time is real money on a one-truck operation. They also skip disposal, the reinforcement strut, the second fault that the first fault caused, and the wage floor underneath all of it: federal wage data puts the median carpenter in this metro at $23.44 an hour across 9,480 workers, and a stocked truck with insurance bills a multiple of that. Finally, they never include the wait. An inspection slot is a calendar item rather than a line item, and after a hailstorm every roofing and door crew in the county is booked against the same week.
"""
copy.write_text(t)
print("written")
