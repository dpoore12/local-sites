#!/usr/bin/env python3
"""Batch 15: add cost-mode pricing blocks + copy to 5 home-service sites."""
import json, pathlib, collections

ROOT = pathlib.Path(__file__).parent / "sites"
D = "read 2026-08-23"

def src(name, url):
    return {"name": f"{name}, {D}", "url": url}

# ---------------------------------------------------------------- COLORADO SPRINGS
CS = {
    "mode": "cost",
    "table_head": "Colorado Springs furnace work, job by job",
    "anchors": [
        {"label": "Furnace replacement permit, El Paso County",
         "value": "$50",
         "detail": "The regional building department prices a furnace or boiler replacement at $50, or $75 when the vent is replaced with it. A water heater swap on its own is $40, and an air conditioning condensing unit is $30.",
         "source_name": "Pikes Peak Regional Building Department fee schedule",
         "source_url": "https://www.pprbd.org/Information/FeeSchedule"},
        {"label": "Failed inspection, second and third visit",
         "value": "$100 and $200",
         "detail": "The first re-inspection is $50, the second $100, the third $200 and it cannot be scheduled for two working days. Plan examination, where it applies, is 28 percent of the building permit fee.",
         "source_name": "Pikes Peak Regional Building Department re-inspection fees",
         "source_url": "https://www.pprbd.org/Information/FeeSchedule"},
        {"label": "Municipal utility rebate, ENERGY STAR gas furnace",
         "value": "$900",
         "detail": "Colorado Springs Utilities pays $900 on a qualifying ENERGY STAR furnace, $1,200 on a boiler, and $1,500 or $3,000 on heat pumps depending on tonnage and cold-climate rating.",
         "source_name": "Colorado Springs Utilities residential HVAC rebates",
         "source_url": "https://www.csu.org/rebates-incentives/residential-hvac"},
        {"label": "Who is allowed to pull the permit",
         "value": "H-B or H-C-1 license",
         "detail": "Heating installation, replacement and repair plus gas piping in one and two family dwellings sits with a Mechanical Contractor B or a Gas Piping Contractor. Those are the license classes the department issues permits to.",
         "source_name": "Pikes Peak Regional Building Department license types",
         "source_url": "https://www.pprbd.org/Licensing/LicenseTypes"},
    ],
    "rows": [
        {"job": "Weekday diagnostic visit on a furnace that quit", "low": 89, "high": 120,
         "basis": "per visit",
         "note": "Four Colorado Springs shops post a flat trip and diagnosis fee. One credits it against the repair, the rest bill it either way.",
         "sources": [src("Highland Heating & Air, Colorado Springs, posted service call fee", "https://www.highlandheatingair.com/"),
                     src("Furnace World, Colorado Springs, posted service fee FAQ", "https://www.furnaceworld.com/faqs"),
                     src("Home Heating Service, Colorado Springs, posted service call FAQ", "https://www.homeheatingservice.com/faqs"),
                     src("Best Pro Appliance Repair, Colorado Springs, posted price list", "https://www.bestprorepair-cos.com/prices.html")]},
        {"job": "Smallest billable repair once a technician opens the cabinet", "low": 185, "high": 305,
         "basis": "flat",
         "note": "Best Pro posts a $120 HVAC trip charge and a separate $185 minimum labor fee, neither credited against the other, so both land on one invoice.",
         "sources": [src("Best Pro Appliance Repair, Colorado Springs, posted minimum labor fee", "https://www.bestprorepair-cos.com/prices.html"),
                     src("Cooper Heating & Cooling, Colorado Springs, posted furnace repair range", "https://www.coopergreenteam.com/colorado-springs/heating/furnace-repair")]},
        {"job": "Ignition side repair: flame sensor, igniter or thermocouple", "low": 75, "high": 500,
         "basis": "flat",
         "note": "Absolute Comfort posts $75 to $250 for a flame sensor and $150 to $400 for an igniter. Mitchell posts $100 to $500 for these common faults.",
         "sources": [src("Absolute Comfort, Colorado Springs, posted heating repair cost table", "https://www.absolutecomfort.com/understanding-heating-repair-costs-in-colorado-springs/"),
                     src("Mitchell Heating, Colorado Springs, posted repair cost range", "https://mitchellheating.com/furnace-replacement-colorado-springs-39789/"),
                     src("Cooper Heating & Cooling, Colorado Springs, posted furnace repair range", "https://www.coopergreenteam.com/colorado-springs/heating/furnace-repair")]},
        {"job": "Blower motor or another major component replaced", "low": 500, "high": 1600,
         "basis": "flat",
         "note": "Absolute Comfort posts $500 to $1,500 and up for a blower motor. Cooper puts its furnace repair ceiling at $1,600 with an average near $668.",
         "sources": [src("Absolute Comfort, Colorado Springs, posted heating repair cost table", "https://www.absolutecomfort.com/understanding-heating-repair-costs-in-colorado-springs/"),
                     src("Cooper Heating & Cooling, Colorado Springs, posted furnace repair range", "https://www.coopergreenteam.com/colorado-springs/heating/furnace-repair")]},
        {"job": "Cracked heat exchanger replaced instead of the furnace", "low": 1500, "high": 3500,
         "basis": "flat",
         "note": "Absolute Comfort posts $1,500 to $3,500 and up. Ascent puts the ceiling on any local furnace repair at $3,500, and this is the repair that reaches it.",
         "sources": [src("Absolute Comfort, Colorado Springs, posted heating repair cost table", "https://www.absolutecomfort.com/understanding-heating-repair-costs-in-colorado-springs/"),
                     src("Ascent HVAC & Home Solutions, Colorado Springs, posted repair cost range", "https://ascentmfs.com/how-much-does-furnace-repair-cost-in-colorado-springs-in-2026/")]},
        {"job": "Annual tune-up with a combustion safety check", "low": 99, "high": 249,
         "basis": "flat",
         "note": "Bergs posts $99 standard and $149 for the deeper clean, Solid Rock $149, and MSI puts single furnace tune-ups along the Front Range at $129 to $249.",
         "sources": [src("Bergs Heating & Air Conditioning, Colorado Springs, posted furnace service prices", "https://www.bergsheating.com/furnace-service"),
                     src("Solid Rock Heating and Air Conditioning, Colorado Springs, posted tune-up price", "https://solidrockheating.com/services/heating/furnaces/furnace-tune-up/"),
                     src("Mechanical Solutions Inc, Colorado Springs and Denver metro, posted tune-up range", "https://www.msicolorado.com/colorado-springs-co-residential-heating-services/furnace-maintenance-tune-ups/")]},
        {"job": "Mid efficiency 80 percent AFUE furnace changed out", "low": 3000, "high": 4750,
         "basis": "flat",
         "note": "Strong posts $3,750 single stage and $4,750 two stage variable speed installed, taxes and fees included. Mitchell posts $3,000 to $7,000 for a full replacement.",
         "sources": [src("Strong Heating and Cooling, Colorado Springs, posted furnace pricing", "https://strongheatingcooling.com/furnace-pricing"),
                     src("Mitchell Heating, Colorado Springs, posted replacement cost range", "https://mitchellheating.com/furnace-replacement-colorado-springs-39789/")]},
        {"job": "Condensing 96 to 97 percent AFUE furnace changed out", "low": 6300, "high": 12000,
         "basis": "flat",
         "note": "Bergs posts an installed figure beginning at $6,300, Strong $6,500 and $8,250 by stage, and Awesome Home Services a $4,600 to $12,000 replacement band.",
         "sources": [src("Bergs Heating & Air Conditioning, Colorado Springs, posted installed estimate", "https://www.bergsheating.com/online-estimate"),
                     src("Strong Heating and Cooling, Colorado Springs, posted furnace pricing", "https://strongheatingcooling.com/furnace-pricing"),
                     src("Awesome Home Services, Colorado Springs, posted pricing guide", "https://www.awesomeservice.com/pricing-guide/")]},
    ],
}

CS_LEDE = """These are the ranges Colorado Springs heating companies publish for their own furnace work, set beside the permit, inspection and rebate figures the regional building department and the municipal utility print in their own schedules. Nothing on this page is a quote for your furnace."""

CS_BODY = """### Why one furnace call has two prices

A furnace that shuts down in February produces one symptom and a dozen candidate causes. A dirty flame sensor and a cracked heat exchanger both end with a cold house, and they sit a factor of thirty apart on the invoice. That is why the bands here are wide at the top: the diagnosis decides which row you are in, and it happens after somebody puts a meter on the control board, not from the driveway.

Where inside a band a job lands comes down to three things. Whether the failed part is proprietary or a stocked universal. Whether nearby fittings crumble when touched, turning a one-part job into three. And whether the call lands on a quiet Tuesday or during the first hard freeze, when every truck in El Paso County is committed.

### Altitude, and the derate nobody mentions

This city sits above 6,000 feet, and gas equipment does not behave here the way its sea-level nameplate suggests. Input capacity has to be derated as elevation climbs, so a furnace sized off square footage alone tends to arrive oversized, short cycle all winter, and wear out its igniter, inducer and control board early. On a repeat failure the honest question is not only which part broke, but whether it broke because the equipment was mismatched to the elevation from the day it went in.

### What the building department charges

Replacing a furnace is permitted work, and the Pikes Peak Regional Building Department fee schedule states the numbers plainly: $50 for a furnace or boiler replacement, $75 when the vent goes with it, $40 for a water heater alone. Failed inspections escalate faster than the permit does, at $50, then $100, then $200, with the third re-inspection blocked for two working days. Heating and gas piping permits in one and two family dwellings go to Mechanical Contractor B and Gas Piping Contractor classes, so a changeout bid from an outfit that cannot pull a permit is not comparable to one that includes it.

### What an honest changeout estimate names

It states the manufacturer and model, the AFUE, the input rating at this elevation rather than at sea level, the stages, the blower type, the vent material and route, where the condensate goes and how it is kept from freezing, whether the gas line and circuit are adequate, the haul-away, the permit line and the inspection. The rebate belongs on the sheet as a separate line, not blended into the price: the utility pays $900 on a qualifying ENERGY STAR furnace.

### The replacement push, said plainly

A cracked heat exchanger is a genuine reason to stop repairing a furnace. The tell is being told about a crack that nobody shows you. A camera photograph, a combustion analyzer reading in parts per million, or a marked location takes two minutes to produce, and condemning an exchanger without one asks for four figures on faith. Igniters, flame sensors, pressure switches, inducers and boards are repairs, not death sentences, under fifteen years old. The other pattern worth naming is the tune-up that turns into an emergency: that visit is a $99 to $249 job here, and it should end with a written condition report.

### What a national calculator misses in this county

It prices equipment and a generic install. It does not carry the permit or a possible re-inspection, the chimney liner an orphaned water heater needs once a condensing furnace stops sharing the masonry flue, a sidewall vent penetration through brick or stucco, gas line resizing, altitude derating, or the second fault the first one caused. On a mid 1980s house, the median vintage here, it also skips the undersized return that has been cooking blower motors for years."""

# ---------------------------------------------------------------- DENVER
DEN = {
    "mode": "cost",
    "table_head": "Denver metro furnace prices, part by part",
    "anchors": [
        {"label": "Mechanical permit on a $6,000 changeout",
         "value": "$67",
         "detail": "Denver charges $35 for the first $2,000 of valuation and $8 for each additional $1,000, so a $6,000 furnace replacement is $67. Mechanical work is a quick permit category, issued without a plan review charge.",
         "source_name": "Denver Community Planning and Development development fees",
         "source_url": "https://www.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Community-Planning-and-Development/Plan-Review-Permits-and-Inspections/Development-Fees"},
        {"label": "Mechanical contractor license, city of Denver",
         "value": "$250 per three years",
         "detail": "Every mechanical license type costs $250 for three years, and the supervisor certificate that has to stand behind it is $60 for the same term. A journeyman registration is $40.",
         "source_name": "Denver contractor licensing fee schedule",
         "source_url": "https://www.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Community-Planning-and-Development/Contractor-Licensing/CL-Resources-and-Downloads/Fees-for-Contractor-Licenses-and-Supervisor-Certificates"},
        {"label": "Xcel Energy rebate, 95 percent AFUE and above",
         "value": "$300",
         "detail": "Paid on an AHRI listed gas furnace at 95 percent AFUE or better, and only when the equipment coming out is non-condensing, which the program defines as 86 percent AFUE or lower.",
         "source_name": "Xcel Energy Colorado residential HVAC rebate application",
         "source_url": "https://www.xcelenergy.com/staticfiles/xe-responsive/Working%20With%20Us/Trade%20Partners/24-04-506_CO-Res_HVAC_OpenPrgms_app.pdf"},
    ],
    "rows": [
        {"job": "Weekday diagnostic visit on a dead furnace", "low": 60, "high": 180,
         "basis": "per visit",
         "note": "Rabbit posts $60 with no repair and nothing with one, UniColorado credits its $180 toward the work, Right Way and All Climate post $89 and $79 flat.",
         "sources": [src("Rabbit Heating and Air, Denver and Thornton, posted flat rate list", "https://rabbitheating.com/furnace-repair/"),
                     src("UniColorado, Denver, posted furnace repair pricing", "https://unicolorado.com/pricing/furnace-repair-cost/"),
                     src("Right Way Mechanical, west Denver metro, posted diagnostic fee", "https://rightwaymechanicalco.com/furnace-repair-denver/"),
                     src("All Climate Systems, Denver area, posted diagnostic fee", "https://allclimatesystems.net/special-offers/")]},
        {"job": "Hot surface igniter replaced", "low": 150, "high": 585,
         "basis": "flat",
         "note": "Gale Force posts $150 to $450, UniColorado $250 to $500, Rabbit a flat $485 to $585 with the weekday trip charge folded in when the repair proceeds.",
         "sources": [src("Gale Force Heating & Air, Denver metro, posted repair price guide", "https://www.galeforceheating-air.com/blog/how-much-does-furnace-repair-cost-in-denver-a-2026-homeowners-guide"),
                     src("UniColorado, Denver, posted component replacement prices", "https://unicolorado.com/pricing/furnace-repair-cost/"),
                     src("Rabbit Heating and Air, Denver and Thornton, posted flat rate list", "https://rabbitheating.com/furnace-repair/")]},
        {"job": "Draft inducer assembly replaced", "low": 500, "high": 1500,
         "basis": "flat",
         "note": "UniColorado posts $500 to $1,100, Gale Force $500 to $1,500, Rabbit $1,050 to $1,485 as a flat rate covering part and labor.",
         "sources": [src("UniColorado, Denver, posted component replacement prices", "https://unicolorado.com/pricing/furnace-repair-cost/"),
                     src("Gale Force Heating & Air, Denver metro, posted repair price guide", "https://www.galeforceheating-air.com/blog/how-much-does-furnace-repair-cost-in-denver-a-2026-homeowners-guide"),
                     src("Rabbit Heating and Air, Denver and Thornton, posted flat rate list", "https://rabbitheating.com/furnace-repair/")]},
        {"job": "Gas valve replaced", "low": 200, "high": 1275,
         "basis": "flat",
         "note": "Gale Force posts $200 to $800 and notes original manufacturer parts cost more than universal ones. UniColorado posts $500 to $1,100 and Rabbit $950 to $1,275.",
         "sources": [src("Gale Force Heating & Air, Denver metro, posted repair price guide", "https://www.galeforceheating-air.com/blog/how-much-does-furnace-repair-cost-in-denver-a-2026-homeowners-guide"),
                     src("UniColorado, Denver, posted component replacement prices", "https://unicolorado.com/pricing/furnace-repair-cost/"),
                     src("Rabbit Heating and Air, Denver and Thornton, posted flat rate list", "https://rabbitheating.com/furnace-repair/")]},
        {"job": "Integrated control board replaced", "low": 300, "high": 1450,
         "basis": "flat",
         "note": "Gale Force posts $300 to $950, UniColorado $500 to $1,000, Rabbit $950 to $1,450. Erratic fault codes make the diagnosis time as variable as the part.",
         "sources": [src("Gale Force Heating & Air, Denver metro, posted repair price guide", "https://www.galeforceheating-air.com/blog/how-much-does-furnace-repair-cost-in-denver-a-2026-homeowners-guide"),
                     src("UniColorado, Denver, posted component replacement prices", "https://unicolorado.com/pricing/furnace-repair-cost/"),
                     src("Rabbit Heating and Air, Denver and Thornton, posted flat rate list", "https://rabbitheating.com/furnace-repair/")]},
        {"job": "Variable speed or ECM blower motor replaced", "low": 600, "high": 2075,
         "basis": "flat",
         "note": "UniColorado posts $600 to $1,600, Gale Force $1,500 to $2,000 for an ECM, Rabbit $1,475 for an ECM and $2,075 for a variable speed motor.",
         "sources": [src("UniColorado, Denver, posted component replacement prices", "https://unicolorado.com/pricing/furnace-repair-cost/"),
                     src("Gale Force Heating & Air, Denver metro, posted repair price guide", "https://www.galeforceheating-air.com/blog/how-much-does-furnace-repair-cost-in-denver-a-2026-homeowners-guide"),
                     src("Rabbit Heating and Air, Denver and Thornton, posted flat rate list", "https://rabbitheating.com/furnace-repair/")]},
        {"job": "Heat exchanger replaced on a furnace worth keeping", "low": 1000, "high": 5000,
         "basis": "flat",
         "note": "Gale Force posts $1,000 to $3,500 and UniColorado $1,900 to $3,700. Plumbline posts $3,000 to $5,000 and up to eight hours on the job.",
         "sources": [src("Gale Force Heating & Air, Denver metro, posted repair price guide", "https://www.galeforceheating-air.com/blog/how-much-does-furnace-repair-cost-in-denver-a-2026-homeowners-guide"),
                     src("UniColorado, Denver, posted component replacement prices", "https://unicolorado.com/pricing/furnace-repair-cost/"),
                     src("Plumbline Services, Denver area, posted heat exchanger cost", "https://plumblineservices.com/help-guides/should-i-replace-my-heat-exchanger-or-buy-a-new-furnace")]},
        {"job": "Furnace changed out with the permit pulled", "low": 3200, "high": 12000,
         "basis": "flat",
         "note": "UniColorado posts $3,200 to $5,800, Right Way $3,800 to $10,500 by efficiency tier including permit and disposal, Plumbline $4,500 to $12,000 for this area.",
         "sources": [src("UniColorado, Denver, posted furnace replacement range", "https://unicolorado.com/pricing/furnace-repair-cost/"),
                     src("Right Way Mechanical, west Denver metro, posted installed price tiers", "https://rightwaymechanicalco.com/furnace-replacement-cost-colorado/"),
                     src("Plumbline Services, Denver area, posted gas furnace installation range", "https://plumblineservices.com/help-guides/should-i-replace-my-heat-exchanger-or-buy-a-new-furnace")]},
    ],
}

DEN_LEDE = """Denver metro heating companies publish flat rate books, and the numbers below are theirs, part by part, next to the permit, license and rebate figures the city and the gas utility publish for themselves. It is market context for reading an estimate, not a quote."""

DEN_BODY = """### The same part, four flat rates

An igniter is an igniter. Yet the published flat rates for swapping one across this metro run from $150 at the low end of one company's range to $585 at the top of another's, and both companies are legitimate. The spread is not really about the part. It reflects whether the trip charge is folded in or billed separately, whether the shop stocks original manufacturer parts or universals, how long the labor warranty runs, and how far the truck drives. Reading a flat rate therefore means reading what it includes, because two identical dollar figures can describe very different obligations.

The one comparison worth making across quotes is the treatment of the diagnostic. One company posts $60 when no repair follows and nothing when one does. Another credits $180 toward the work. Two more post $79 and $89 as flat visit fees. Ask which model applies before the truck is dispatched, and the rest of the estimate becomes readable.

### A mile-high furnace is not a sea-level furnace

Equipment nameplates are written for sea level, and at 5,280 feet the derating rules change both the input rating and, on many models, the pressure switch that has to be fitted. That has two consequences on this page. First, an oversized furnace short cycles, and short cycling is what puts igniters, inducers and boards into early graves, which is part of why part replacement calls cluster in older changeouts done on square footage alone. Second, arctic outbreaks here arrive every few winters and expose undersized ductwork and marginal combustion air the moment the furnace runs continuously for three days.

### Permit arithmetic on a changeout

Denver prices permits off declared valuation: $35 covers the first $2,000, then $8 for every additional $1,000. A $6,000 furnace replacement therefore carries a $67 permit, and because mechanical work falls in the quick permit category it is issued without a plan review charge on top. That is a small number against a five figure job, which is exactly why its absence from a bid is informative. The license behind it is not free either. Every mechanical license class costs $250 for three years and the supervisor certificate standing behind it another $60, and an outfit avoiding the permit is usually avoiding the license too.

### After hours costs more, with the arithmetic shown

One Denver company publishes the whole structure: a $175 minimum service charge after hours, a basic repair at $149 during the week and $250 after hours. Both charges apply on a night call, so the floor for a small after-hours fix is $425 before any part goes in, against $149 for the same fix on a weekday when the trip is covered by the repair. Another publishes an after-hours call of $150 to $250 with emergency labor of $140 to $210 an hour on top. The largest single variable on a minor repair in this market is not the part. It is the hour on the clock, which is worth knowing at eleven at night with a space heater running.

### Where the pressure sits in this metro

The rebate structure creates it. Xcel pays $300 on a 95 percent AFUE or better furnace, and only when the unit coming out is non-condensing at 86 percent AFUE or below, so there is a standing incentive to frame any repair on an older 80 percent furnace as a replacement decision. Sometimes that is right. It is right on a cracked exchanger, a failed exchanger on a twenty year old cabinet, or a third major part in two seasons. It is not right on a $500 board failure in a twelve year old condensing furnace, and a rebate does not change that. Ask for the carbon monoxide reading in parts per million and a photograph of the crack before signing anything that starts with removal.

### What the online average leaves out

Chimney liner work when a condensing furnace orphans the water heater on an oversized masonry flue, return duct that was never sized for a modern blower, a dedicated circuit, condensate protection in an unconditioned crawlspace, sidewall venting through a brick 1950s wall, and the permit and inspection. On the repair side it leaves out the second failure the first one caused, which is the usual reason a job that was quoted mid range lands at the top of it."""

# ---------------------------------------------------------------- PHOENIX
PHX = {
    "mode": "cost",
    "table_head": "Phoenix leak work, job by job",
    "anchors": [
        {"label": "City position on customer side leaks",
         "value": "No forgiveness",
         "detail": "The code makes each customer responsible for all leaks downstream of the point of service delivery, and for full payment of charges for any water lost to those leaks. There is no water leak credit program to apply for.",
         "source_name": "Phoenix City Code section 37-27",
         "source_url": "https://phoenix.municipal.codes/CC/37-27"},
        {"label": "Water in the high use season",
         "value": "$6.13 per 100 cubic feet",
         "detail": "The June through September rate for an inside city account, against $4.93 in the low season, on top of a $4.64 monthly service charge on a five eighths inch meter. One hundred cubic feet is 748 gallons.",
         "source_name": "City of Phoenix water rates effective March 2025",
         "source_url": "https://www.phoenix.gov/content/dam/phoenix/waterservicessite/documents/rates_effective_march_2025.pdf"},
        {"label": "Sewer fee review window",
         "value": "60 days",
         "detail": "Sewer charges are recalculated each July from average January through March water use. A review requested more than 60 days after that July bill date is ineligible, with no exceptions stated.",
         "source_name": "City of Phoenix sewer fee review",
         "source_url": "https://www.phoenix.gov/administration/departments/waterservices/city-services-bill/submit-a-sewer-fee-review.html"},
        {"label": "Minimum residential permit fee",
         "value": "$195",
         "detail": "The schedule adopted in December 2025 sets a $195 minimum permit fee for single lot residential construction, includes the first re-inspection, and charges $195 for each re-inspection after that.",
         "source_name": "City of Phoenix development fee schedule",
         "source_url": "https://www.phoenix.gov/content/dam/phoenix/pddsite/documents/impact-fees/fee-schedule.pdf"},
    ],
    "rows": [
        {"job": "Electronic locate on a pressurized water line", "low": 150, "high": 600,
         "basis": "flat",
         "note": "Darrel's posts a flat $150 for about an hour, Miracle $150 to $400, American Leak Detection $375 for roughly two hours, Rapid Rooter $250 to $600.",
         "sources": [src("Darrel's Locating, Phoenix, posted water leak locate price", "https://www.darrelslocating.com/waterleaks.html"),
                     src("Miracle Plumbing & AC, Phoenix metro, posted detection cost", "https://miracleplumbingaz.com/2026/07/08/slab-leak-repair-in-queen-creek-and-phoenix-metro-signs-costs-and-methods/"),
                     src("American Leak Detection of Phoenix, posted flat rate", "https://www.americanleakdetection.com/phoenix/residential/plumbing/leak-detection/"),
                     src("Rapid Rooter Plumbing, Phoenix, posted leak detection range", "https://rapidrooteraz.com/leak-detection")]},
        {"job": "Slab leak opened and repaired at one spot", "low": 450, "high": 4000,
         "basis": "flat",
         "note": "ASAP posts $450 to $750 caught early and $2,000 to $4,000 standard, Miracle $500 to $1,500 for an open slab spot repair, Patrick Riley $600 to $4,000.",
         "sources": [src("ASAP Plumbing, Phoenix valley, posted slab leak repair costs", "https://asapplumbingaz.com/leak-detection/slab-leak-repair/"),
                     src("Miracle Plumbing & AC, Phoenix metro, posted spot repair cost", "https://miracleplumbingaz.com/2026/07/08/slab-leak-repair-in-queen-creek-and-phoenix-metro-signs-costs-and-methods/"),
                     src("Patrick Riley, greater Phoenix, posted slab leak repair range", "https://patrickrileyservices.com/residential-plumbing-services/slab-leak-detections-repairs")]},
        {"job": "Line rerouted through walls or attic instead of the slab", "low": 1500, "high": 4000,
         "basis": "flat",
         "note": "Miracle posts $1,500 to $4,000 with no concrete broken after detection. Patrick Riley posts $2,000 to $4,000 where the leak is extensive enough to warrant rerouting.",
         "sources": [src("Miracle Plumbing & AC, Phoenix metro, posted reroute cost", "https://miracleplumbingaz.com/2026/07/08/slab-leak-repair-in-queen-creek-and-phoenix-metro-signs-costs-and-methods/"),
                     src("Patrick Riley, greater Phoenix, posted rerouting range", "https://patrickrileyservices.com/residential-plumbing-services/slab-leak-detections-repairs")]},
        {"job": "Whole house repipe after repeat failures", "low": 4000, "high": 24000,
         "basis": "flat",
         "note": "Miracle posts $4,000 to $10,000. Simba prices by size and material, from $4,500 for PEX in a small house to $24,000 for copper in a large one.",
         "sources": [src("Miracle Plumbing & AC, Phoenix metro, posted repiping cost", "https://miracleplumbingaz.com/2026/07/08/slab-leak-repair-in-queen-creek-and-phoenix-metro-signs-costs-and-methods/"),
                     src("Simba Plumbing, Phoenix and the Valley, posted repipe price table", "https://www.simbaplumbingphx.com/blog/how-much-does-it-cost-to-repipe-a-house")]},
        {"job": "Sewer or drain camera inspection on its own", "low": 250, "high": 500,
         "basis": "flat",
         "note": "Rapid Rooter posts $250 to $450 for a standalone inspection. American Home Water posts $250 to $500, rising where access is hard or the run is long.",
         "sources": [src("Rapid Rooter Plumbing, Phoenix, posted camera inspection price", "https://rapidrooteraz.com/plumber/sewer-camera-inspection-phoenix/"),
                     src("American Home Water & Air, Phoenix, posted camera inspection cost", "https://americanhomewater.com/how-much-plumbing-camera-inspection-cost/")]},
        {"job": "Pool leak located and pinned down", "low": 100, "high": 1200,
         "basis": "flat",
         "note": "Phoenix Leak Detectors posts $100 to $600 a visit, American Leak Detection $250 to $700 by plumbing configuration, AE Outdoor $350 to $1,200 by method.",
         "sources": [src("Phoenix Leak Detectors, Phoenix and Maricopa County, posted detection cost", "https://www.phoenixleakdetectors.com/faqs.html"),
                     src("American Leak Detection of Phoenix, posted pool detection rates", "https://www.americanleakdetection.com/phoenix/residential/pools-spas-fountains/leak-detection/"),
                     src("AE Outdoor Living, Phoenix metro, posted pool leak pricing", "https://aeoutdoorliving.com/pool-leak-detection-phoenix")]},
    ],
}

PHX_LEDE = """Below are the figures Phoenix area leak companies publish for locating and repairing water leaks, alongside the city's own water rate, code language and permit fees. None of it is a quote, and none of it can be priced honestly from the curb."""

PHX_BODY = """### Two invoices, not one

Finding a leak and fixing it are separate jobs with separate prices, and this table keeps them apart deliberately. A locate is an hour or two of acoustic listening, tracer gas, pressure isolation and thermal imaging that ends with a mark on the floor and a photograph. The repair is whatever the mark turns out to require. A few valley companies credit the locate against the repair when they do both, and one that serves Phoenix and Scottsdale says so in writing. Most of the flat rate locators do not credit anything, and their published figures sit lower for exactly that reason. Any repair number produced before the locate is the average of every possible repair, which is another way of saying it is not about your house.

### The city bills you for water you never used

This is the part that changes the math on waiting. Phoenix City Code section 37-27 makes each customer responsible for all leaks downstream of the point of service delivery, and for full payment of charges for any water lost to them. There is no leak forgiveness program to apply for. Water in the June through September window runs $6.13 per hundred cubic feet, which is 748 gallons, on top of the monthly meter charge, so a line weeping under a slab in July is a bill that compounds weekly rather than a rounding error.

The one adjustment the city does publish is the sewer fee review, and it works on a fixed calendar. Sewer charges are recalculated each July from average January through March water use, and a request that lands more than 60 days after that July bill is ineligible. A leak running through the winter therefore affects a full year of sewer billing, and the window to contest it closes fast.

### Copper, caliche and 1980s slabs

Valley water is hard, and hard water moving fast through soft copper produces pinholes from the inside out. Add a recirculating hot water loop, decades of thermal cycling under a heated slab, and soils that shift and fissure across Maricopa County, and the failures cluster in predictable places: hot lines first, elbows and transitions next, the loop return after that. Two consequences follow. A leak found in a hot line raises a fair question about the rest of that line. And a house on its second slab leak is a different conversation from a house on its first, which is why the reroute and repipe rows exist above.

### Reading a leak estimate line by line

A usable estimate names the detection method, states plainly whether the detection fee is credited, and separates the spot repair from the reroute so the two can be compared. It includes the concrete cut and the patch, says who repairs the drywall and whether texture and paint are included, and states whether a permit is being pulled. The city's fee schedule sets a $195 minimum permit fee on residential work and charges $195 for every re-inspection after the first, so that line is real money on a small job. It also says what happens if opening the slab reveals a second failure in the same run, because that is the single most common reason a job lands at the top of its band.

### The reroute against repipe pitch

Both are legitimate. A reroute is right for aging pipe, poor access, or a second failure in the same line. A repipe is right when the system is failing along its length. What should raise an eyebrow is a whole house repipe proposed off one located leak with no camera evidence of wall thinning and no history of prior failures. Published valley repipe prices run from roughly $4,000 to $24,000 depending on square footage and whether the material is PEX or copper, so the difference between this line and the whole house is the largest number anyone will put in front of you. Ask for the evidence, and ask what the spot repair would cost as a comparison.

### What the online calculator never includes

Cutting and patching concrete. Flooring that cannot be matched once it comes up. Drywall texture and paint. The pool equipment loop and the irrigation manifold, which are frequently the actual source. The permit and its re-inspection. And the water that already ran, which under section 37-27 is on the account holder no matter who finds the leak."""

# ---------------------------------------------------------------- SAN DIEGO
SD = {
    "mode": "cost",
    "table_head": "San Diego leak work, job by job",
    "anchors": [
        {"label": "Leak adjustment filing window",
         "value": "120 days",
         "detail": "Public Utilities considers a credit only for a concealed leak in a non-irrigation pipe. Irrigation, pool and fixture leaks are excluded, the request has to arrive within 120 days of the first high bill, and review takes six to ten weeks.",
         "source_name": "City of San Diego leak adjustment policy",
         "source_url": "https://www.sandiego.gov/public-utilities/customer-support/leak-adjustment"},
        {"label": "Water at the top tier",
         "value": "$11.89 per HCF",
         "detail": "Effective January 2026 a single family account pays a $35.53 monthly base fee on a three quarter inch meter, then $8.51 for the first 10 units, $9.50 through 22, and $11.89 above that.",
         "source_name": "City of San Diego water billing rates",
         "source_url": "https://www.sandiego.gov/public-utilities/customer-support/water-billing-rates"},
        {"label": "Permit to repair or replace water and waste pipe",
         "value": "$264.25",
         "detail": "Charged per dwelling unit, with $87.68 for each additional unit. Private water or sewer utility work is $264.25 for the first 100 linear feet plus $52.39 for each additional 10 feet, and a $12.16 mapping fee.",
         "source_name": "San Diego Information Bulletin 103, plumbing permit fees",
         "source_url": "https://www.sandiego.gov/development-services/forms-publications/information-bulletins/103"},
    ],
    "rows": [
        {"job": "Concealed leak located in a slab, wall or ceiling", "low": 249, "high": 495,
         "basis": "flat",
         "note": "Best San Diego posts $249 and $495 and credits it against a repair. West Plumbing's $129 call plus $238 an hour in slab totals $367 for one hour.",
         "sources": [src("Best San Diego Leak Detection, San Diego, posted detection prices", "https://bestsandiegoleakdetection.com/free-leak-detection/"),
                     src("West Plumbing Services, San Diego, posted detection rate card", "https://www.wpsexpert.com/professional-gas-and-water-leak-detection/"),
                     src("Tri Express Plumbing, San Diego County, posted leak detection price", "https://triexpressplumbing.com/leak-detection/")]},
        {"job": "Leak in a wall or ceiling opened and repaired", "low": 350, "high": 650,
         "basis": "flat",
         "note": "Almco posts $350 to $650. Tri Express prices pipe patching from $400 and a hot water line repair from $600, both before any drywall goes back.",
         "sources": [src("Almco Plumbing, San Diego, posted water leak repair prices", "https://almcoplumbing.com/water-leak-repair/"),
                     src("Tri Express Plumbing, San Diego County, posted repair prices", "https://triexpressplumbing.com/leak-detection/")]},
        {"job": "Slab leak repaired by cutting the concrete", "low": 900, "high": 2800,
         "basis": "flat",
         "note": "San Diego Plumbing and Pipelining posts $900 to $1,200 average for jackhammer access, Almco $1,600 to $2,800, Tri Express from $1,500.",
         "sources": [src("San Diego Plumbing and Pipelining, San Diego, posted slab repair options", "https://sandiegoplumbingandpipelining.com/leak-detection/san-diego-slab-leak-detection/"),
                     src("Almco Plumbing, San Diego, posted slab leak repair price", "https://almcoplumbing.com/water-leak-repair/"),
                     src("Tri Express Plumbing, San Diego County, posted slab leak price", "https://triexpressplumbing.com/leak-detection/")]},
        {"job": "Single line rerouted instead of reopening the slab", "low": 1500, "high": 4200,
         "basis": "flat",
         "note": "San Diego Plumbing and Pipelining posts $1,500 to $1,700 average, texture and paint excluded. Almco posts $1,800 to $4,200 for a water line reroute.",
         "sources": [src("San Diego Plumbing and Pipelining, San Diego, posted reroute price", "https://sandiegoplumbingandpipelining.com/leak-detection/san-diego-slab-leak-detection/"),
                     src("Almco Plumbing, San Diego, posted rerouting price", "https://almcoplumbing.com/water-leak-repair/")]},
        {"job": "Failing line lined from the inside rather than replaced", "low": 3750, "high": 3950,
         "basis": "flat",
         "note": "San Diego Plumbing and Pipelining posts $3,750 average for epoxy lining and $3,950 for sleeving. Clearwater prices lining at $150 to $250 per linear foot.",
         "sources": [src("San Diego Plumbing and Pipelining, San Diego, posted lining and sleeving prices", "https://sandiegoplumbingandpipelining.com/leak-detection/san-diego-slab-leak-detection/"),
                     src("Clearwater Plumbing and Drains, San Diego County, posted lining price per foot", "https://www.clearwaterplumbinganddrains.com/plumbing-blog/cost-to-repipe-a-house-in-san-diego-county")]},
        {"job": "Whole house repipe when the system is failing", "low": 4500, "high": 20000,
         "basis": "flat",
         "note": "Repipe Home Hero and Clearwater both post $4,500 to $15,000, Clearwater to $20,000 and up on large homes, Almco $8,000 to $20,000, Tri Express from $6,500.",
         "sources": [src("Repipe Home Hero, San Diego County, posted repipe range", "https://repipehero.com/faq/"),
                     src("Clearwater Plumbing and Drains, San Diego County, posted repipe prices by size", "https://www.clearwaterplumbinganddrains.com/plumbing-blog/cost-to-repipe-a-house-in-san-diego-county"),
                     src("Almco Plumbing, San Diego, posted repiping price", "https://almcoplumbing.com/water-leak-repair/"),
                     src("Tri Express Plumbing, San Diego County, posted repiping price", "https://triexpressplumbing.com/plumber-san-diego/")]},
    ],
}

SD_LEDE = """What follows is what San Diego County plumbers publish for finding and repairing hidden water leaks, set next to the city's own water rates, its leak credit rules and the permit fees Development Services charges. It is market context for reading a bid, not a quote."""

SD_BODY = """### Detection and repair are two different invoices

There are two pricing models in this county and they are worth telling apart before anyone visits. Flat rate detection quotes a single figure for the visit, commonly published between $249 and $495, and several shops credit that figure against the repair when they do the work. Hourly detection quotes the visit and then charges for time by where the leak is: one San Diego company publishes a $129 service call plus $199 an hour in a wall or ceiling, $218 in a basement and $238 in ground or concrete slab, so a one hour slab locate totals $367 with nothing credited back. Neither model is wrong. They are different bets about how long a particular leak takes to find, and the estimate should say which bet you are taking.

### The 120-day clock on your water bill

The City of San Diego leak adjustment policy is narrower than most homeowners assume, and it runs on a deadline. A credit is considered only for a concealed leak in a non-irrigation pipe: irrigation lines, pools and running fixtures are excluded outright. The request has to reach Public Utilities within 120 days of the first high bill or it is not considered at all, it has to be supported by a repair invoice showing when the leak was discovered and when it was fixed, and the review itself takes six to ten weeks.

That makes the plumbing paperwork part of the financial recovery. Water here is billed at $8.51, $9.50 and $11.89 per hundred cubic feet as consumption climbs, over a $35.53 monthly base fee on a typical three quarter inch meter, so a hidden leak pushes an ordinary household into the top tier quickly. Keep the invoice, keep the dates, and ask the plumber to write both on it.

### Why slabs here leak the way they do

Postwar tract housing across this county ran copper in and under the slab. From the outside, expansive soils and a marine chloride load work on that copper; from the inside, hot recirculating water and high static pressure do the rest. Pressure is the cheap variable: the city notes that service pressure is regulated at the house, and a failed regulator quietly shortens the life of every fitting and flex line behind it. Sewer laterals are the other local surprise. The private lateral belongs to the property owner, so a camera inspection that finds a break in the yard is the homeowner's repair, not the city's.

### What the permit costs before anyone opens the floor

Development Services prices a residential water or waste pipe repair or replacement at $264.25 per dwelling unit and $87.68 for each additional unit. Private water or sewer utility work is $264.25 for the first 100 linear feet plus $52.39 for each additional 10 feet, with a small mapping fee on top. On a repipe, one county contractor publishes permit costs of $200 to $1,500 depending on scope and wall repairs of $500 to $2,000 for patching and paint. Those are the lines most often missing from the lowest bid, and their absence is usually what closes the gap between two quotes that looked far apart.

### Where the number gets padded

The move to watch is a whole house repipe proposed from a single located leak. Before agreeing, ask for camera or borescope evidence of wall thinning, or a record of prior failures in the same system. Lining and sleeving are real published alternatives at roughly $3,750 and $3,950 for a line, or $150 to $250 a foot, and they suit some pipe and not other pipe. A company that sells only one method will find that method necessary, so the useful question on any slab leak is what the spot repair, the reroute and the repipe each cost on this house, in writing, side by side.

### What a national average leaves out on a coastal lot

Slab thickness and rebar. Tile or hardwood that cannot be matched once it is cut. Texture and paint. The permit and the mapping fee. Access under a raised foundation in an older neighborhood. And the possibility that the leak located today is the second failure in a line that is corroding along its whole length, which is the difference between the bottom of a band and the top of it."""

# ---------------------------------------------------------------- TAMPA
TPA = {
    "mode": "cost",
    "table_head": "Tampa appliance repair, job by job",
    "anchors": [
        {"label": "Tax on a repair that includes any part",
         "value": "6 percent state",
         "detail": "Florida taxes the entire repair charge, labor included, whenever the shop supplies a part that becomes part of the machine, even if parts are not itemized. Labor only work is exempt only when the invoice documents that no parts were used.",
         "source_name": "Florida Department of Revenue guide GT-800010",
         "source_url": "https://floridarevenue.com/Forms_library/current/gt800010.pdf"},
        {"label": "Hillsborough County surtax on top",
         "value": "1.5 percent",
         "detail": "The county's discretionary sales surtax for 2026 brings the combined rate on a taxable repair invoice in Tampa to 7.5 percent.",
         "source_name": "Florida DR-15DSS discretionary sales surtax rates for 2026",
         "source_url": "https://floridarevenue.com/Forms_library/current/dr15dss_26.pdf"},
        {"label": "State license for appliance repair",
         "value": "None required",
         "detail": "The county tax collector lists small appliance repair among tasks that do not require a contractor license, and issues no handyman receipt at all. Business tax receipts run to September 30 and are delinquent October 1.",
         "source_name": "Hillsborough County Tax Collector business tax license categories",
         "source_url": "https://www.hillstaxfl.gov/taxes/business-tax-services/license-categories/"},
        {"label": "City permit when a hookup actually changes",
         "value": "$120",
         "detail": "Tampa charges $120 for a general residential plumbing, electrical or mechanical permit and $162 for natural or LP gas piping. Every permit carries a state building surcharge of 2.5 percent of permit value, with a $4 floor.",
         "source_name": "City of Tampa trade permit fee schedule",
         "source_url": "https://www.tampa.gov/sites/default/files/document/2023/trade_permit_fee_schedule_02.16.23.pdf"},
    ],
    "rows": [
        {"job": "Service call and diagnosis on one appliance", "low": 65, "high": 120,
         "basis": "per visit",
         "note": "Professional posts $65 and Teodor $79, both waived when the repair is approved. Smart deducts its $89 from the bill, and Hartman's $120 is waived on approval.",
         "sources": [src("Professional Appliance Service, Tampa Bay, posted service call fee", "https://www.profapplianceservice.com/pricing"),
                     src("Teodor Appliance Repair, Tampa Bay, posted service call fee", "https://appliancerepairteodor.com/how-much-does-appliance-repair-cost-in-tampa-bay/"),
                     src("Smart Appliance Services, Tampa, posted diagnostic prices", "https://smartapplianceservices.com/prices/"),
                     src("Hartman's Appliance Repair, Tampa Bay, posted diagnostic fee", "https://tampaappliancerepair.services/")]},
        {"job": "Diagnosis on a luxury or sealed system brand", "low": 119, "high": 185,
         "basis": "per visit",
         "note": "Smart posts $119 for premium brands. Hartman's posts $185 for Sub-Zero, Wolf, Viking and Bosch, for LG and Samsung refrigerators, and for stacked laundry.",
         "sources": [src("Smart Appliance Services, Tampa, posted premium brand diagnostic", "https://smartapplianceservices.com/prices/"),
                     src("Hartman's Appliance Repair, Tampa Bay, posted brand diagnostic prices", "https://tampaappliancerepair.services/")]},
        {"job": "Refrigerator that stopped cooling", "low": 190, "high": 500,
         "basis": "flat",
         "note": "Teodor posts $200 to $450, DiChristopher $200 to $500, Professional $190 to $470 across most repairs. All three describe parts and labor together.",
         "sources": [src("Teodor Appliance Repair, Tampa Bay, posted refrigerator repair costs", "https://appliancerepairteodor.com/how-much-does-appliance-repair-cost-in-tampa-bay/"),
                     src("DiChristopher Appliance Repair, Tampa, posted repair cost ranges", "https://dichristopherappliance.com/is-appliance-repair-worth-it-in-2026-a-tampa-cost-breakdown/"),
                     src("Professional Appliance Service, Tampa Bay, posted repair range", "https://www.profapplianceservice.com/pricing")]},
        {"job": "Compressor or sealed system work on a refrigerator", "low": 400, "high": 800,
         "basis": "flat",
         "note": "Teodor posts $400 to $800 and up for a compressor replacement. Professional posts $490 to $800 for compressor and sealed system repairs by brand and model.",
         "sources": [src("Teodor Appliance Repair, Tampa Bay, posted compressor price", "https://appliancerepairteodor.com/how-much-does-appliance-repair-cost-in-tampa-bay/"),
                     src("Professional Appliance Service, Tampa Bay, posted sealed system range", "https://www.profapplianceservice.com/pricing")]},
        {"job": "Washer that will not drain, spin or stay quiet", "low": 120, "high": 600,
         "basis": "flat",
         "note": "Teodor posts $120 to $350 for common faults and $300 to $600 and up for a motor or transmission. DiChristopher posts $150 to $400 for motor and seal work.",
         "sources": [src("Teodor Appliance Repair, Tampa Bay, posted washer repair costs", "https://appliancerepairteodor.com/how-much-does-appliance-repair-cost-in-tampa-bay/"),
                     src("DiChristopher Appliance Repair, Tampa, posted washer repair range", "https://dichristopherappliance.com/is-appliance-repair-worth-it-in-2026-a-tampa-cost-breakdown/")]},
        {"job": "Dryer that tumbles but will not heat", "low": 100, "high": 350,
         "basis": "flat",
         "note": "Teodor posts $150 to $300 for no heat, $180 to $350 for a heating element and $100 to $200 for a thermal fuse. DiChristopher posts $120 to $350.",
         "sources": [src("Teodor Appliance Repair, Tampa Bay, posted dryer repair costs", "https://appliancerepairteodor.com/how-much-does-appliance-repair-cost-in-tampa-bay/"),
                     src("DiChristopher Appliance Repair, Tampa, posted dryer repair range", "https://dichristopherappliance.com/is-appliance-repair-worth-it-in-2026-a-tampa-cost-breakdown/")]},
        {"job": "Oven, range or cooktop brought back into service", "low": 100, "high": 600,
         "basis": "flat",
         "note": "Teodor posts $100 to $250 for a burner igniter and $250 to $600 and up for a control board. DiChristopher posts $150 to $400 for element, igniter and control work.",
         "sources": [src("Teodor Appliance Repair, Tampa Bay, posted oven and range costs", "https://appliancerepairteodor.com/how-much-does-appliance-repair-cost-in-tampa-bay/"),
                     src("DiChristopher Appliance Repair, Tampa, posted range repair range", "https://dichristopherappliance.com/is-appliance-repair-worth-it-in-2026-a-tampa-cost-breakdown/")]},
    ],
}

TPA_LEDE = """These are the diagnostic fees and repair ranges Tampa Bay appliance companies publish for their own work, set next to the tax, permit and licensing rules the state, the county and the city publish for theirs. Nothing here is a quote for your machine."""

TPA_BODY = """### The diagnosis comes first, and it is usually credited

Four Tampa Bay shops publish the same structure with different numbers: a flat fee to come out, diagnose the fault and put a written estimate in your hand, then that fee waived or deducted once the repair is approved. The published figures are $65, $79, $89 and $120. Read the wording rather than the number, because one company publishes both a $19 service call and a separate $120 diagnostic fee that goes away on approval, which means the trip itself is not free even when the diagnosis becomes free.

The same reading habit sets the realistic floor on a small job. One shop publishes an $89 diagnostic that is deducted from the total, plus a $185 minimum labor fee. Because the diagnostic is deducted rather than added, the smallest invoice once a part is actually fitted is $185 plus the part, not $274. Stacking a credited diagnostic on top of minimum labor overstates the bill by the diagnostic, and it is the most common arithmetic error in comparing two estimates.

### The tax line on the invoice

Florida's rule catches people out. If the shop supplies any part that becomes part of the machine, the entire repair charge is taxable, labor included, and it stays taxable even when parts are not listed separately. Labor only work is exempt, but only when the invoice documents that no parts were used. The state rate is 6 percent and Hillsborough County adds 1.5 percent, so a taxable repair invoice in Tampa carries 7.5 percent. On a $500 refrigerator repair that is another $37.50, and no national cost page carries it.

### Nobody licenses appliance repair in this state

There is no state appliance repair license to check. The Hillsborough County Tax Collector business tax license categories page lists small appliance repair among the tasks that do not require a contractor license, and the office issues no handyman receipt at all. That pushes the screening onto the homeowner: a written estimate before any part is ordered, the manufacturer part number on the invoice, and the warranty term stated in writing on both the part and the labor.

The permitted trades are the bright line. Once a repair turns into moving a water line, replacing a gas range connection or altering a circuit, the City of Tampa trade permit fee schedule prices a general residential plumbing, electrical or mechanical permit at $120 and natural or LP gas piping at $162, each with a state surcharge of 2.5 percent of permit value and a $4 floor. If someone proposes gas or plumbing alteration as part of an appliance repair with no permit line, that is the moment to ask who is pulling it.

### The fifty percent rule, and what humidity does here

The usual guideline is to repair when the repair costs less than half of a comparable new machine, and one local shop states it in exactly those terms. Two local factors bend it. Tampa water is hard enough to scale heating elements and clog ice makers and dishwasher solenoids well before the rest of the appliance is worn out, which makes several of the least expensive repairs on this page the ones most likely to recur if the underlying water quality is ignored. This is also a humid coastal market, hard on dryer transitions, vent runs and control boards in unconditioned laundry closets and garages.

Housing tenure matters too. Roughly half of the housing units in this county are renter occupied, so many machines being diagnosed belong to a landlord rather than the person standing in the kitchen. Sorting out who authorizes the repair beforehand saves a diagnostic fee nobody wants to pay twice.

### Reading the estimate before the part is ordered

A usable estimate names the diagnostic fee and how it is treated, the part number and whether it is a manufacturer part or an aftermarket equivalent, the labor separately from the part, the tax, and the warranty on each. It says whether the repair involves the sealed system, because that is the row where prices roughly double and where refrigerant handling rules apply. It also says what happens if the first part does not fix the fault, which on a modern board controlled machine is a real possibility.

### What the online range leaves out

Brand premiums on diagnosis, parts that have gone out of production on a ten year old model, the extra labor to pull a stacked laundry pair apart, second faults found once the panel is off, and the 7.5 percent that lands on the total the moment a part is involved."""

# ---------------------------------------------------------------- write
JOBS = [
    ("coloradospringsfurnacerepair.com", CS, CS_LEDE, CS_BODY),
    ("denverfurnacerepairpros.com", DEN, DEN_LEDE, DEN_BODY),
    ("phoenixleakdetectionpros.com", PHX, PHX_LEDE, PHX_BODY),
    ("sandiegoleakdetectionpros.com", SD, SD_LEDE, SD_BODY),
    ("appliancerepairtampaco.com", TPA, TPA_LEDE, TPA_BODY),
]

for domain, pricing, lede, body in JOBS:
    d = ROOT / domain
    sj = d / "site.json"
    site = json.loads(sj.read_text(), object_pairs_hook=collections.OrderedDict)
    site["pricing"] = pricing
    sj.write_text(json.dumps(site, indent=2, ensure_ascii=False) + "\n")

    cp = d / "copy.md"
    txt = cp.read_text().rstrip("\n")
    if "## pricing_lede" in txt:
        txt = txt.split("## pricing_lede")[0].rstrip("\n")
    txt += "\n\n## pricing_lede\n\n" + lede.strip() + "\n\n## pricing_body\n\n" + body.strip() + "\n"
    cp.write_text(txt)
    print("wrote", domain, "rows", len(pricing["rows"]), "anchors", len(pricing["anchors"]),
          "copy words", len((lede + " " + body).split()))
