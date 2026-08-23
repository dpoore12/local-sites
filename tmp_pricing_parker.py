import json, pathlib

d = "parkergaragedoorrepairexperts.com"
p = pathlib.Path("sites") / d / "site.json"
s = json.loads(p.read_text())

s["pricing"] = {
    "mode": "cost",
    "table_head": "Parker market ranges, door by door",
    "anchors": [
        {
            "label": "Building permit fee, project valued at $500 or less",
            "value": "$23.50",
            "detail": "The Town's valuation schedule starts at $23.50, adds plan review at 65 percent of the permit fee, and collects construction use tax calculated as half the valuation times 4.0 percent.",
            "source_name": "Town of Parker Building Permit Fee Valuation Schedule",
            "source_url": "https://www.parkerco.gov/DocumentCenter/View/736"
        },
        {
            "label": "Class D building contractor registration",
            "value": "$75",
            "detail": "Annual registration for the class that covers garages, alterations and remodels. Parker issues permits only to a registered contractor or an authorized representative, so an unregistered crew cannot legally file the door.",
            "source_name": "Parker Municipal Code Chapter 11.19, Contractor Registration",
            "source_url": "https://library.municode.com/co/parker/codes/municipal_code?nodeId=TIT11BUCO_CH11.19CORE"
        },
        {
            "label": "Median hourly wage, carpenters, Denver metro",
            "value": "$31.21",
            "detail": "The May 2025 midpoint across 7,250 carpenters in the Denver metro area, and one of the highest of any large inland market. Front Range labor is the single biggest reason numbers here sit above national averages.",
            "source_name": "BLS Occupational Employment and Wage Statistics, May 2025",
            "source_url": "https://www.bls.gov/oes/current/oes_19740.htm"
        }
    ],
    "rows": [
        {
            "job": "Come out and diagnose a door that stopped working",
            "low": 85,
            "high": 190,
            "basis": "per visit",
            "note": "A booked weekday appointment is cheapest. Evening calls, holiday weekends and the first hard freeze push toward the ceiling."
        },
        {
            "job": "Pair of torsion springs replaced on a builder-installed double door",
            "low": 370,
            "high": 820,
            "basis": "flat",
            "note": "Most doors in this town still carry their original springs. Both go together, since a matched pair keeps the door balanced."
        },
        {
            "job": "Upgrade from a ten thousand cycle spring set to a long-life set",
            "low": 480,
            "high": 980,
            "basis": "flat",
            "note": "Thicker wire and larger drums cost more now and roughly double the lifts before the next failure on a heavily used door."
        },
        {
            "job": "Cables re-spooled and drums reset after the door came off crooked",
            "low": 200,
            "high": 490,
            "basis": "flat",
            "note": "Straightforward if only a cable slipped. A door that dropped on one side may have racked a section or bent a bracket."
        },
        {
            "job": "Safety sensors, wiring and travel limits sorted out",
            "low": 120,
            "high": 340,
            "basis": "flat",
            "note": "Sun glare and a loose staple in a builder wire run cause most of it. Replacing a discontinued sensor pair costs more."
        },
        {
            "job": "Opener replaced with a quiet head and battery backup",
            "low": 520,
            "high": 980,
            "basis": "per unit",
            "note": "Bedrooms sit over most garages in this town, so the quiet belt or wall-mount unit is usually the practical pick."
        },
        {
            "job": "Insulated steel double door installed, permitted and use tax paid",
            "low": 1700,
            "high": 4800,
            "basis": "per unit",
            "note": "Windows, a thicker section and a hardware upgrade drive it. Town permit, plan review and construction use tax ride on top."
        }
    ]
}
p.write_text(json.dumps(s, indent=1, ensure_ascii=False) + "\n")

copy = pathlib.Path("sites") / d / "copy.md"
t = copy.read_text().rstrip() + "\n\n" + """## pricing_body_PLACEHOLDER
"""
# build the real sections
sections = """## pricing_lede

What follows is the going cost of garage door work in Parker, alongside the Town's published permit, plan review and use tax figures and the Denver metro wage data that sits underneath every labor hour on the invoice.

## pricing_body

### Front Range labor is the headline number

Start with the wage, because it explains most of the gap between what a Parker homeowner pays and what a national cost article promises. Federal survey data puts the midpoint for a Denver metro carpenter at $31.21 an hour, well ahead of most inland markets. Add a truck, fuel across a town that stretches from The Pinery to Stonegate, liability coverage, and a parts inventory deep enough to finish the job on the first trip, and the hourly rate a customer sees is a multiple of that wage. None of that is markup for its own sake. It is why a company that answers on a Sunday evening exists at all, and it is why the ceiling of each row above is usually a scheduling decision rather than a parts decision.

### An entire town's hardware is aging on the same clock

Parker's median home was completed in 2003, and the population climbed nearly twelve percent between 2020 and 2024, so the housing here arrived in waves. Doors installed in the same wave carry the same builder specification: one torsion spring set rated for about ten thousand cycles, stamped rollers, and an entry-level chain opener. A household that opens the door four times a day burns through ten thousand cycles in under seven years, which is why so many original systems in this town are now failing within a season or two of each other. Practically, that means a spring call in a Canterberry Crossing or Clarke Farms garage is rarely a spring call alone. The bearings, the cables, the rollers and the opener gear are all the same age, and the honest repair is a short list.

### What the Town charges, and what it will not let happen

Parker states plainly that permits are required for all window and door replacements. The fee itself is small: the valuation schedule opens at $23.50, plan review runs 65 percent of the permit fee, and Colorado adds a wrinkle most states do not, a construction use tax figured as half the project valuation multiplied by four percent. Two other rules matter more than the dollars. First, the Town issues permits only to a registered contractor or an authorized representative, and the Class D registration that covers garages and alterations costs seventy-five dollars a year, so any crew that cannot produce registration cannot file the job at all. Second, a homeowner association may ask for a plan showing the proposed improvement, which is worth checking while the door is still being measured rather than after a panel profile has been ordered. Repair work on existing hardware, meaning springs, cables, rollers, sensors and opener parts, is service and does not enter that process.

### Where the range moves once someone is on site

Two variables do most of the work. One is weight. A single-layer builder door and an insulated replacement of the same width need different spring wire, and hanging the second on hardware sized for the first is the most common cause of a repeat failure. The other is altitude and sun. Parker sits above six thousand feet with intense ultraviolet exposure and dramatic daily temperature swings, which hardens rubber bottom seals, dries out factory lubricant, and cooks the plastic gear in an opener sooner than a milder climate would. A door that has been running dry and out of balance for two years has already worn parts that a technician then has to include, and that is the difference between the low and high column.

### Reading the estimate like somebody who has done the work

The spring specification should be written down: wire diameter, inside diameter, overall length, and rated cycles. Anything described only as heavy duty is a description of nothing. Roller count and bearing type should appear, along with cable diameter. For an opener, insist on the model number, the drive type, whether battery backup is included, whether the old head and rail leave with the crew, and whether a reinforcement strut is needed before a motor starts pulling on a thin section. For a replacement door, the permit, plan review, use tax and disposal each deserve their own line. A single number with no breakdown is not a bargain; it is a place for extras to appear later.

### The pattern worth refusing

The upsell in this trade is the jump from a broken part to a whole door. A snapped spring gets diagnosed in the driveway as a system at the end of its life, and a four-figure replacement proposal follows before anybody has weighed the door or checked whether the track is plumb. Sometimes replacement genuinely is the right call, on a rotted wood door or one that has been hit hard. But a straight steel door with sound sections and a bent rail is a repair, and the way to tell the difference is to ask what specifically cannot be corrected. The second pattern is the advertised inspection priced below anybody's cost of showing up, which is a lead-generation number rather than a service. Nothing on this page is a quote from anyone; these are researched market ranges, and the real figure comes from whoever puts hands on the door.
"""
copy.write_text(copy.read_text().rstrip() + "\n\n" + sections)
print("written")
