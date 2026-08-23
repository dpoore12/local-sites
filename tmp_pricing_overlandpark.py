import json, pathlib

d = "overlandparkgaragedoorrepairpros.com"
p = pathlib.Path("sites") / d / "site.json"
s = json.loads(p.read_text())

s["pricing"] = {
    "mode": "cost",
    "table_head": "Going rates for garage door work across Overland Park",
    "anchors": [
        {
            "label": "Building permit, repair or remodel valued under $5,000",
            "value": "$30",
            "detail": "Overland Park publishes a flat building permit fee of thirty dollars for permitted projects valued below five thousand dollars, and fifty dollars once the valuation lands between five and nineteen thousand.",
            "source_name": "City of Overland Park common permit fees",
            "source_url": "https://www.opkansas.gov/common-permit-fees"
        },
        {
            "label": "Plan review, flat fee due at application",
            "value": "$30",
            "detail": "The master fee schedule adds a flat thirty-dollar plan review payable when the application goes in, on top of the permit fee, taking the small-project total to sixty dollars.",
            "source_name": "Overland Park Master Fee Schedule effective August 1, 2025",
            "source_url": "https://content.civicplus.com/api/assets/ks-overlandpark/5c2ef6d8-b38f-41aa-999c-0537f894e89c?cache=1800"
        },
        {
            "label": "Median hourly wage, carpenters, Kansas City metro",
            "value": "$29.72",
            "detail": "Half of the 4,540 carpenters counted across the Kansas City metro earned more than this per hour in May 2025. That figure is the floor under every hour billed on a driveway here.",
            "source_name": "BLS Occupational Employment and Wage Statistics, May 2025",
            "source_url": "https://www.bls.gov/oes/current/oes_28140.htm"
        }
    ],
    "rows": [
        {
            "job": "First visit to diagnose a door that quit mid-cycle",
            "low": 80,
            "high": 185,
            "basis": "per visit",
            "note": "Scheduled daytime calls land low. A subzero morning after a Johnson County snow event, or a Sunday, lands high."
        },
        {
            "job": "Torsion spring pair renewed on a sixteen-foot door",
            "low": 340,
            "high": 760,
            "basis": "flat",
            "note": "Both springs are replaced together because the second one is the same age. Heavier insulated sections need thicker wire."
        },
        {
            "job": "Extension springs and safety cables redone on an older single door",
            "low": 220,
            "high": 520,
            "basis": "flat",
            "note": "Common in this city's 1970s and 1980s garages. Missing containment cables have to be added, which is code work rather than an extra."
        },
        {
            "job": "Bent track section and flattened rollers replaced",
            "low": 210,
            "high": 540,
            "basis": "flat",
            "note": "Low-headroom garages here often use a reduced radius rail that is not stocked on every truck, so a return trip is possible."
        },
        {
            "job": "Bottom section replaced after a bumper strike",
            "low": 520,
            "high": 1450,
            "basis": "flat",
            "note": "Depends entirely on whether the manufacturer still makes that panel profile and color, and on whether the strut behind it survived."
        },
        {
            "job": "Opener swapped for a belt or wall-mount unit",
            "low": 470,
            "high": 900,
            "basis": "per unit",
            "note": "Wall-mount heads cost more but free up ceiling space in a shallow garage. Old rail removal and a new outlet add labor."
        },
        {
            "job": "Insulated double door replaced, permitted and hauled away",
            "low": 1500,
            "high": 4200,
            "basis": "per unit",
            "note": "Insulation value, window inserts and a hardware upgrade move it. Winters here make the thicker section a practical choice, not a luxury."
        }
    ]
}
p.write_text(json.dumps(s, indent=1, ensure_ascii=False) + "\n")

copy = pathlib.Path("sites") / d / "copy.md"
t = copy.read_text().rstrip() + "\n\n" + """## pricing_lede

Here is what garage door work costs around Overland Park right now, with the city's own permit and plan review fees and the metro wage data behind those figures named, so a homeowner can judge an estimate before agreeing to anything.

## pricing_body

### Two housing eras, two different bills

The median Overland Park home was finished in 1989, which sounds tidy until you realize how the city grew. Streets north of about 95th were built when extension springs, wooden sections and shallow headroom were normal. Everything south and west of them went up with wide sectional doors on torsion shafts and a chain opener bolted to the ceiling. A price list that treats both as one job is guessing. Extension hardware is cheaper to buy and slower to make safe, since containment cables often have to be added where none exist. Torsion work on a modern wide door costs more in parts and less in improvisation. So when an estimate arrives without anybody having looked at which system is actually hanging over the car, the number underneath it is a coin flip.

### Why every row has two ends

The failed component sets the floor and the collateral damage sets the ceiling. A spring is the clearest example. On its own it is a known part and a practiced procedure. But springs almost never fail alone at this housing age: the bearing plates squeal, the cables have started to fray at the drum, and the opener has been compensating for a heavy door long enough to have worn its gear. Fixing only the visible break puts a customer back in the same driveway before the next winter. The other end of the range is the hardware choice. A door can be rehung on the parts a builder used or on parts rated for two or three times the cycles, and the second option costs more on the invoice and less over a decade.

### Winter is the local pricing pressure

Cold does not create fatigue on its own, but it finds it. In late January 2026 the weather service put Johnson County under a winter storm warning with wind chills forecast near seventeen below and several more inches of snow. Mornings like that stack resistance on top of an aged system: lubricant thickens, the bottom seal freezes to the slab, and the first lift of the day asks a spring at the end of its cycle life to break loose a stuck door. That is why call volume and after-hours labor peak in the same week, and why the top of the diagnostic row is a January number rather than an average one. It also explains why insulated replacement sections are worth their premium in this climate: an attached garage that stays above freezing is easier on every moving part in it.

### The paperwork, and who is allowed to pull it

The city's fees on this work are modest and public. A permitted repair or remodel valued under five thousand dollars carries a thirty-dollar building permit fee, and the master fee schedule adds a flat thirty-dollar plan review due when the application is filed. Sixty dollars total will not change a decision. What matters more is the requirement behind it: Overland Park will not issue a building permit to a contractor without an active Johnson County contractor license. Routine service on existing hardware, meaning springs, cables, rollers, sensors and opener parts, is not permit work at all. Anything that changes framing or widens an opening is, and that scope is worth settling before a door gets ordered rather than on installation morning.

### How to read an estimate

Ask for the spring specification in writing: wire diameter, inside diameter, length and cycle rating. Vague words like heavy duty describe nothing. Ask how many rollers, and whether they carry sealed bearings or the stamped steel kind. On an opener, get the model number, the drive type and whether hauling the old head and rail away is included. On a replacement door, get the insulation value, the panel style, the window option, the permit line, and the disposal line separately, because a single lump total is where surprises hide. Trip charges and labor belong on their own lines too. Any estimate produced over the phone, sight unseen, for a system nobody has measured, is a sales number rather than a price.

### What the national average does not carry

Published averages assume one door type, one climate and a technician five minutes away. They leave out the containment cables an older single door needs, the reduced-radius rail a low-headroom garage takes, the reinforcement strut an opener requires before it starts pulling on a thin section, and the second visit when a discontinued panel color has to be ordered. They also leave out labor economics: federal wage data puts the median metro carpenter at $29.72 an hour, and a stocked service truck with insurance and parts inventory bills a multiple of that hourly figure. None of the ranges above is a quote. They are what this market has been paying, and the actual number comes from whoever measures the door.
"""
copy.write_text(t)
print("written")
