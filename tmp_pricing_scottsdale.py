import json, pathlib

d = "scottsdalegaragedoorrepairpros.com"
p = pathlib.Path("sites") / d / "site.json"
s = json.loads(p.read_text())

s["pricing"] = {
    "mode": "cost",
    "table_head": "Scottsdale cost bands for the jobs that come up most",
    "anchors": [
        {
            "label": "Minimum permit, one discipline",
            "value": "$121",
            "detail": "The floor on any single-trade permit under the fee schedule adopted by Resolution 13391, effective July 1, 2025. A reinspection at a property carries the same $121.",
            "source_name": "City of Scottsdale Miscellaneous Permit Fee Schedule",
            "source_url": "https://www.scottsdaleaz.gov/docs/default-source/scottsdaleaz/planning---develpment/fees-fy25-26/permit-fee-schedule---miscellaneous.pdf?sfvrsn=8c6543cc_4"
        },
        {
            "label": "Contractor licensing threshold, aggregate contract price",
            "value": "$1,000",
            "detail": "State law exempts unlicensed work only when the whole job, labor and materials together, stays under a thousand dollars and no building permit is required. Splitting a job into smaller contracts to stay beneath it is expressly prohibited.",
            "source_name": "Arizona Revised Statutes 32-1121",
            "source_url": "https://www.azleg.gov/ars/32/01121.htm"
        },
        {
            "label": "Median hourly wage, carpenters, Phoenix metro",
            "value": "$29.00",
            "detail": "Midpoint hourly pay across the 12,710 carpenters counted in the Phoenix-Mesa-Chandler metro in May 2025. A large trade pool keeps routine labor competitive here, which shows up at the low end of every row.",
            "source_name": "BLS Occupational Employment and Wage Statistics, May 2025",
            "source_url": "https://www.bls.gov/oes/current/oes_38060.htm"
        }
    ],
    "rows": [
        {
            "job": "Summer service call on a door that stopped partway",
            "low": 85,
            "high": 195,
            "basis": "per visit",
            "note": "A July afternoon in an uncooled garage is slower, hotter work than the same visit in February, and after-hours calls sit highest."
        },
        {
            "job": "Torsion springs replaced as a matched pair",
            "low": 350,
            "high": 800,
            "basis": "flat",
            "note": "Wire size, drum wear and door weight decide the figure. A door hung over a casita or third bay may use two shafts."
        },
        {
            "job": "Roller set and hinges replaced after the bearings dried out",
            "low": 180,
            "high": 460,
            "basis": "per unit",
            "note": "Desert heat drives factory lubricant out of stamped rollers. Sealed-bearing nylon replacements cost more and survive a lot longer here."
        },
        {
            "job": "Opener control board or capacitor replaced",
            "low": 190,
            "high": 480,
            "basis": "flat",
            "note": "Attic-level garage temperatures cook boards and battery backups. A discontinued board turns the repair into a head replacement instead."
        },
        {
            "job": "Bottom weather seal and threshold reset",
            "low": 120,
            "high": 320,
            "basis": "per linear foot",
            "note": "Ultraviolet exposure hardens rubber until it cracks and lets dust and scorpions under. Uneven slabs need the threshold shimmed."
        },
        {
            "job": "Two sections replaced on a door bowed by monsoon wind",
            "low": 700,
            "high": 1900,
            "basis": "flat",
            "note": "Panel profile and color matching dominate the cost, and a twisted track or bent strut has to be corrected at the same time."
        },
        {
            "job": "Custom wood-look or full-view door installed on a larger home",
            "low": 3200,
            "high": 12000,
            "basis": "per unit",
            "note": "Insulated glass, cladding and heavier hardware drive it, plus association design review common in the ranch communities here."
        }
    ]
}
p.write_text(json.dumps(s, indent=1, ensure_ascii=False) + "\n")

copy = pathlib.Path("sites") / d / "copy.md"
sections = """## pricing_lede

This page shows what garage door repairs and replacements are running in Scottsdale, with the city's permit floor, the state licensing threshold and Phoenix metro wage figures named, so an estimate can be judged against something real.

## pricing_body

### Heat is the variable that sets this market apart

Nearly every figure in the table above is shaped by garage temperature. In July 2023 Phoenix logged thirty straight days at or above 110 degrees, and Maricopa County recorded forty-two excessive heat warning days that year. An attached garage with no cooling runs hotter still. Grease migrates out of stamped roller bearings, the rubber bottom seal hardens and splits, the plastic drive gear in an opener softens under load, and the sealed lead battery in a backup unit gives up years early. That is why the roller and opener rows above are not maintenance trivia in this city, and why a component that would last a decade in a mild climate shows up as a failure here in half the time. It also changes the labor: an afternoon service call inside a closed garage in August is genuinely slower work than the identical call in winter.

### The second local force is wind

Monsoon cells arrive fast and hit hard. On one August afternoon in 2024 the weather service documented uprooted trees, downed power lines and more than half an inch of rain inside thirty minutes over Scottsdale. A gust against a wide, lightly insulated door bows sections and shifts vertical rails, and the door that still opens afterward is often the expensive one, because it keeps grinding rollers and cables against misaligned track on every cycle. A post-storm inspection should look at rail plumb, strut straightness, threshold debris and sensor alignment before anyone counts dents. Skin damage is cosmetic and can wait; geometry cannot.

### Why the low end and high end are so far apart

Two things stretch the ranges here more than in most markets. The first is what is hanging in the opening. This city has plenty of ordinary steel sectional doors, and it also has a large stock of custom wood-look, full-view and clad doors on larger homes in the ranch and mountain communities. Those doors weigh more, use heavier springs and hardware, and their panels are not stocked anywhere nearby, so a single damaged section becomes a special order. The second is scope discipline. A cable that slipped off a drum is one job; the same cable failure that dropped a corner and racked a section is three. What lands an invoice at the top of a row is almost always the collateral damage rather than the original part.

### Permits, licensing and what those numbers actually mean

Scottsdale's fee schedule sets a floor of $121 on a single-discipline permit and charges the same amount for a reinspection, and the city's own list of work that needs no permit excludes anything affecting a garage. Arizona layers a rule on top of that: under state statute, unlicensed contracting is permitted only when the aggregate price of the whole undertaking, labor and materials included, stays under one thousand dollars and no building permit is required, and dividing a project into smaller contracts to squeeze beneath that ceiling is specifically barred. Read together, those two figures explain the market. Almost any full door replacement in this city sits above the state threshold, which means the work belongs with a licensed registrant, and a replacement at a property on the Scottsdale Historic Register carries a design review step ahead of ordering as well. Routine service on existing hardware sits outside all of this.

### What belongs on an itemized estimate

Ask for the spring wire diameter, inside diameter, length and cycle rating in writing. Ask for the roller count and whether the bearings are sealed, because in this climate that single choice decides whether the same repair comes back. On an opener, get the model, drive type, whether a battery backup is included, and whether the old head and rail go away with the truck. On a replacement, expect separate lines for the door, the insulation value, glass or cladding options, the track and hardware, the permit, disposal of the old sections, and labor. Trip charges belong stated, not buried. Anything quoted over the phone for a door nobody has measured or weighed is a sales figure.

### What a national cost page will not tell you

Published averages are built for a temperate climate and a mid-range steel door, so they understate two things badly in Scottsdale: the pace at which heat consumes rollers, seals, lubricant and electronics, and the ceiling on a custom door in a market with a lot of them. They also leave out the permit floor, the reinspection charge if a slot is missed, association design review, and the disposal of heavy clad sections. Underneath everything sits the labor market: half of the 12,710 carpenters in this metro earn more than $29.00 an hour, and a stocked truck with insurance bills well above the wage it pays. Everything above is a market range for this city, sourced, and not a price set by anybody.
"""
copy.write_text(copy.read_text().rstrip() + "\n\n" + sections)
print("written")
