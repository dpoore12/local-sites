#!/usr/bin/env python3
"""Batch 8: add /pricing/ (mode cost) to five Emergency Plumbing sites."""
import json, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parent
SITES = ROOT / "sites"

DATA = {}

# ---------------------------------------------------------------- Arvada, CO
DATA["arvadaemergencyplumber.com"] = {
  "pricing": {
    "mode": "cost",
    "table_head": "What the common emergency plumbing jobs run in Arvada",
    "anchors": [
      {
        "label": "Building permit, water heater replacement",
        "value": "$55",
        "detail": "The flat amount Arvada lists for a water heater permit. It is pulled before the old tank leaves the house, and it buys an inspection rather than a piece of paper.",
        "source_name": "City of Arvada building permit fee schedule",
        "source_url": "https://www.arvadaco.gov/1263/Building-Fee-Schedule"
      },
      {
        "label": "Right-of-way permit, one sewer service",
        "value": "$67",
        "detail": "Charged per sewer service when the work crosses the public right of way, which is the same figure as the minimum right-of-way permit fee in Arvada.",
        "source_name": "City of Arvada rights of way fee schedule",
        "source_url": "https://www.arvadaco.gov/DocumentCenter/View/294/Right-of-Way-Fee-Schedule-PDF"
      },
      {
        "label": "Pavement degradation fee, per foot of trench",
        "value": "$20.50",
        "detail": "Added for every linear foot of trench opened in a city street, plus twenty feet of required resurfacing, which is why a dig under pavement is priced apart from a dig in a lawn.",
        "source_name": "City of Arvada rights of way fee schedule",
        "source_url": "https://www.arvadaco.gov/DocumentCenter/View/294/Right-of-Way-Fee-Schedule-PDF"
      }
    ],
    "rows": [
      {"job": "Night or weekend callout for water that will not stop",
       "low": 165, "high": 495, "basis": "per visit",
       "note": "Midnight, holidays and a house already flooding sit high; a scheduled weekday morning slot sits at the bottom."},
      {"job": "Main drain cabled open through the cleanout",
       "low": 225, "high": 675, "basis": "flat",
       "note": "A yard cleanout keeps this cheap. Pulling a toilet or going through a crawlspace access adds an hour before the cable turns."},
      {"job": "Sewer line scoped on camera and the trouble spot located",
       "low": 245, "high": 695, "basis": "flat",
       "note": "Longer runs from older blocks north of Olde Town, plus a surface locate and a written report, push this up."},
      {"job": "Split supply line or frozen hose bib opened up and repaired",
       "low": 385, "high": 1650, "basis": "flat",
       "note": "Copper in an open crawlspace is quick. A line inside a finished wall or under a slab means cutting, patching and a return trip."},
      {"job": "Water heater changed out, 40 or 50 gallon gas tank",
       "low": 1450, "high": 3600, "basis": "per unit",
       "note": "Expansion tank, new venting, a pan and drain, code-required seismic strapping and a tight closet all move the number."},
      {"job": "Sewer lateral spot repair dug from the yard",
       "low": 3200, "high": 9800, "basis": "flat",
       "note": "Depth, bedrock, tree roots and mature landscaping decide it. Crossing the sidewalk or street adds permits and resurfacing."},
      {"job": "Water service line replaced from the meter pit to the house",
       "low": 4600, "high": 15500, "basis": "flat",
       "note": "Boring under a driveway costs less to restore than trenching it. Winter ground and a street cut are the expensive combination."}
    ]
  },
  "pricing_lede": "This page lays out what emergency plumbing work actually costs around Arvada, what the city charges in permit and right-of-way money on top of it, and which parts of a Jefferson County lot decide whether a repair sits at the low or the high end.",
  "pricing_body": """### What decides where a job lands in its range

An Arvada plumbing invoice is built out of three things: how long water has been loose in the building, what has to come apart before anybody can touch the failure, and whether the fix stays inside the house or continues out under a driveway. A weeping angle stop under a Candelas vanity is contained and reachable. The same fitting buried in a slab on an older Stocke-Walter lot turns into concrete cutting, a rerouted line and drywall repair afterward. The leak did not change. The path to it did.

Hour of the week is the second lever. A callout at eleven on a Sunday night in February is priced differently from a Wednesday morning appointment, and February is exactly when hose bibs and crawlspace runs along the Front Range actually split open.

The third lever is what shows up behind the first fault. Drain stacks in the older blocks near Olde Town were not installed last decade, and a stoppage there is often a symptom of a pipe that has lost its bottom rather than a wad of wipes. Cabling clears the water; the camera says whether that is the end of the story.

### The paperwork sitting behind the number

Swapping a water heater in Arvada is permitted work at $55 on the city's building permit fee schedule, and most other plumbing permits are figured from the actual contract value of the work under the city's Table 18-1, which starts at $34 for the smallest jobs. Neither figure is large. What matters is the inspection each one schedules, because an inspection is a calendar slot and calendar slots are why a two-hour repair can span two days.

Digging is where local cost structure really shows. Work in the public right of way takes its own permit, listed at $67 for a single sewer service, and the moment a trench crosses pavement the city adds a pavement degradation fee of $20.50 for each linear foot of trench plus twenty feet of required resurfacing. A repair in a lawn and the identical repair under a paved street are two different projects before a shovel moves. Reinspection at $77, traffic control plan review, and overtime inspection billed hourly with a two-hour minimum live in that same schedule, and all of it lands in the estimate somebody hands you.

### Soil and water, which is why some repairs repeat

Arvada's own permit records are blunt about ground conditions. A 2022 soils and foundation summary filed with the city for a townhome project identified expansive soil and bedrock and recommended pressure-testing under-slab plumbing, flexible couplings, and isolating pipe where it passes through a slab. Clay that swells and shrinks with moisture pulls on joints for years, so under-slab drain failures here are a pattern rather than bad luck. City water runs soft to moderately hard, averaging about 84 mg/L or roughly five grains per gallon, so heavy scale is not the usual villain in a failed water heater around here. Freeze-thaw cycling and sediment are.

### What a quote should spell out

A trustworthy estimate names the failed component and the evidence for the call: the pressure reading, the camera footage timestamp, the depth and distance to the defect measured from the cleanout. It separates the diagnostic visit from the repair and states plainly whether the first amount applies against the second. It lists the permit as its own line, names who pulls it, and says which inspections are included. On any excavation it identifies the restoration standard: compacted backfill, concrete or asphalt patch to city spec, sod or seed, and who calls in the utility locate. Vague language on an excavation estimate almost always reappears later as an extra.

### The trap in this trade

The costly pattern in emergency plumbing is the jump from one clogged line to a full replacement proposal, signed at midnight while a basement floor is wet. A stoppage cleared on Tuesday and scoped on Thursday is the same information with a clear head attached. Two other habits deserve suspicion: hydro jetting sold before anyone has looked inside the pipe, and a monthly membership pitched during the crisis that quietly changes what the visit costs. Caustic drain chemicals poured into an old cast iron stack while waiting for help make the eventual repair worse, not cheaper.

### What the number found online leaves out

National cost pages quote parts and labor for a tidy version of the job. They leave out the Arvada permit and its inspection, the right-of-way permit, the pavement degradation charge, the concrete or asphalt patch, replacing landscaping torn up by a trench, and any drywall or paint that follows an interior repair. On winter work they also leave out frozen ground, which is slower to open and slower to compact back. The figure a homeowner remembers is the equipment. The figure that hits the invoice includes putting Arvada back the way it was found."""
}

# --------------------------------------------------------------- Atlanta, GA
DATA["atlantaemergencyplumberpros.com"] = {
  "pricing": {
    "mode": "cost",
    "table_head": "What Atlanta homeowners pay for the common plumbing emergencies",
    "anchors": [
      {
        "label": "Minimum residential plumbing permit fee",
        "value": "$50",
        "detail": "The floor for a residential plumbing permit in the city's fee appendix. Individual line items sit under it: each fixture at $10, and a house sewer newly laid or replaced also at $10.",
        "source_name": "Atlanta Code of Ordinances, Appendix B fee schedule",
        "source_url": "https://library.municode.com/ga/atlanta/codes/code_of_ordinances/483906?nodeId=COORATGEVOII_APXBFE"
      },
      {
        "label": "Penalty for work started without a permit",
        "value": "Double, up to $1,000",
        "detail": "Atlanta doubles the permit fee when work begins before the permit issues, capped at a thousand dollars, and charges $50 for each reinspection trip after a written correction notice.",
        "source_name": "Atlanta Code of Ordinances, Appendix B fee schedule",
        "source_url": "https://library.municode.com/ga/atlanta/codes/code_of_ordinances/483906?nodeId=COORATGEVOII_APXBFE"
      },
      {
        "label": "Watershed review and site inspection, single-family sewer connection",
        "value": "$230",
        "detail": "Charged by the Department of Watershed Management for plan review and site inspection, with another $250 sewer inspection fee when the connection is a new tap. Installation is separate and falls to the owner.",
        "source_name": "City of Atlanta ATL311 sewer connection permit cost article",
        "source_url": "https://www.atl311.com/en-us/knowledgearticle/?code=KB0011799"
      }
    ],
    "rows": [
      {"job": "Kitchen or laundry line snaked back open",
       "low": 185, "high": 525, "basis": "flat",
       "note": "Accessible cleanout, one line, daylight hours is the floor. Second-story cast iron reached from a roof vent is the ceiling."},
      {"job": "After-hours visit for an overflowing drain or a leak with no shutoff",
       "low": 175, "high": 525, "basis": "per visit",
       "note": "Weeknight and weekend windows carry a premium, and so does a callout during the storms that flood intown basements."},
      {"job": "Sewer lateral camera inspection with a locate and report",
       "low": 250, "high": 725, "basis": "flat",
       "note": "Long laterals on deep Grant Park and Kirkwood lots take more line, and root-filled clay often needs a clearing pass first."},
      {"job": "Galvanized supply pipe section cut out and replaced",
       "low": 450, "high": 2400, "basis": "flat",
       "note": "One accessible run is quick work. Chasing rusted galvanized behind plaster in a 1920s bungalow keeps climbing."},
      {"job": "Water heater replaced, 40 or 50 gallon tank",
       "low": 1500, "high": 3800, "basis": "per unit",
       "note": "Attic and closet installs need a pan, drain line and often new venting. Tight stairwells add two people to the job."},
      {"job": "Root-blocked clay sewer lateral opened and spot repaired",
       "low": 2900, "high": 9500, "basis": "flat",
       "note": "Depth drives it. Add the arborist review when a protected tree sits over the trench and the timeline stretches."},
      {"job": "Sewer lateral relined or replaced end to end",
       "low": 7500, "high": 27000, "basis": "flat",
       "note": "Steep intown lots, long runs to the main, street cuts and repaving carry the top of this range."}
    ]
  },
  "pricing_lede": "Here is what plumbing emergencies actually cost across Atlanta, what the city and the Department of Watershed Management add in permit and inspection money, and why an intown lot full of clay and tree roots prices differently from a newer house out toward the county line.",
  "pricing_body": """### Three things move an Atlanta plumbing number

Start with access. A clogged branch line with a cleanout inside the crawlspace is a straightforward visit. The same clog in a Virginia-Highland duplex, where the only way at the stack is through a second-floor roof vent, is a longer and more careful job. Second, material age: intown houses carry galvanized supply and cast iron or clay drainage, and old pipe rarely fails politely. Third, the clock. A leak that started at nine on a Friday night and a leak reported Monday at ten are the same repair with different labor attached.

That is also why an honest range stays wide. A cleared line and a failed line look identical from the sink. Only the camera tells you which one you have, and the difference between those two answers is the difference between a few hundred dollars and five figures.

### Roots, clay and hills: the local reason

Atlanta's drainage problems are largely a story about trees and slope. The city's own field work makes the point: in early January 2026 the Department of Watershed Management traced a Georgia Avenue SE sinkhole to a 24-inch clay combination sewer about eighteen feet down. Clay joints and thirsty roots find each other, and Atlanta has both in abundance on the same lots where the housing stock is oldest. Hilly intown parcels also put the house well above or well below the main, so laterals here run longer and deeper than a flat subdivision would need, and depth is the single biggest multiplier on any dig.

Trees add a second layer that is procedural rather than physical. Since June 2025 the city has required a completed arborist meeting before a permit application involving possible tree impacts is even submitted, and applications without that documentation are not accepted. Nobody prices that as a line item, but it lengthens the schedule on exactly the excavations that root damage causes. Meanwhile the sewer system itself is under federal consent decrees dating to 1998 and 1999, with an estimated four billion dollars of water and sewer work behind them. Public money has gone into mains. Private laterals stayed private.

### What the city's paperwork costs, and what it enforces

The fee appendix is modest on its face: a $50 minimum for a residential plumbing permit, $10 for each fixture, $10 for a house sewer newly laid or replaced. The enforcement side is where the money lives. Starting work before the permit issues doubles the fee, up to a thousand dollars, and each reinspection trip after a written correction notice adds $50. On the utility side, a single-family sewer connection carries $230 for Watershed plan review and site inspection, plus a $250 sewer inspection fee when a new tap is involved, and the department is explicit that the installation itself is the owner's cost. Work inside the public right of way can require a separate qualified contractor permit from Public Works.

### Reading an estimate like somebody who has seen a few

An estimate worth signing states the diagnosis and the evidence behind it: footage from the camera, distance and depth to the defect, and whether the pipe is clay, cast iron, Orangeburg or plastic. It puts the permit on its own line and says who applies for it. On any dig it specifies restoration in writing, which in this city means concrete or asphalt to city spec, backfill compaction, and what happens to shrubs and sod. It separates the diagnostic charge from the repair and says whether one credits against the other. If a proposal quotes lining and excavation as a single blended number, ask which one is actually planned.

### The upsell to watch for

The pressure play in this market is a full lateral replacement proposed from a single blocked line, presented while somebody is standing in an inch of water. Roots at one joint are a repair. A pipe that has lost its shape along most of its length is a replacement. Those are different findings and the camera distinguishes them, so ask to watch the footage rather than a summary. Two smaller traps: jetting sold before any inspection, which can finish off already fragile clay, and enzyme or chemical treatments billed as prevention on a line whose actual problem is a broken joint.

### What the online average never includes

The national figures skip Atlanta's specifics almost entirely. They leave out the permit and reinspection structure, the Watershed review and inspection fees, the arborist step when a protected tree is in the way, pavement restoration on a street cut, and the drywall and paint that follow an interior repair. They also assume a lateral of ordinary length at ordinary depth, which describes very few lots inside the city. Depth, distance and what is growing overhead are the local variables, and every one of them is missing from a national average."""
}

# ------------------------------------------------------- Colorado Springs, CO
DATA["coloradospringsemergencyplumber.com"] = {
  "pricing": {
    "mode": "cost",
    "table_head": "Researched ranges for plumbing emergencies in Colorado Springs",
    "anchors": [
      {
        "label": "Regional building permit, water heater replacement",
        "value": "$40",
        "detail": "Pikes Peak Regional Building Department's individual residential permit for a water heater swap. It rises to $75 when the vent is replaced along with the appliance.",
        "source_name": "Pikes Peak Regional Building Department fee schedule",
        "source_url": "https://www.pprbd.org/Information/FeeSchedule"
      },
      {
        "label": "Wastewater permit, repair or alteration on a single-family line",
        "value": "$200",
        "detail": "What Colorado Springs Utilities charges for a repair, alteration or additional install on a single-family wastewater service, with return inspection trips billed at $100 each.",
        "source_name": "Colorado Springs Utilities development charges and fees",
        "source_url": "https://www.csu.org/hubfs/Document-Library/2025DevelopmentCharges.pdf?hsLang=en"
      },
      {
        "label": "Water service line inspection, new install or repair",
        "value": "$160",
        "detail": "The utility inspects the water service line itself, separately from the building permit, and charges $100 again for every return trip after the first.",
        "source_name": "Colorado Springs Utilities development charges and fees",
        "source_url": "https://www.csu.org/hubfs/Document-Library/2025DevelopmentCharges.pdf?hsLang=en"
      }
    ],
    "rows": [
      {"job": "Emergency callout, water loose in the house",
       "low": 160, "high": 480, "basis": "per visit",
       "note": "Overnight and weekend arrival costs most. A daytime appointment during a normal week costs least."},
      {"job": "Burst or frozen pipe cut out and repaired",
       "low": 375, "high": 1750, "basis": "flat",
       "note": "Exposed pipe in a basement is fast. Pipe in an exterior wall or unheated crawlspace on the west side is slow and wet."},
      {"job": "Kitchen, laundry or bathroom branch line cleared",
       "low": 195, "high": 560, "basis": "flat",
       "note": "One accessible line during business hours anchors the low end; multiple fixtures backing up together means a bigger machine."},
      {"job": "Water heater replaced with permit and inspection",
       "low": 1400, "high": 3500, "basis": "per unit",
       "note": "Expansion control, relief valve discharge routing, combustion air and new venting are the checks that lift the price."},
      {"job": "Main sewer line camera inspection and locate",
       "low": 240, "high": 660, "basis": "flat",
       "note": "Older Old North End and Patty Jewett runs are long. A locate marked on the surface for excavation adds time."},
      {"job": "Pressure-reducing valve replaced on the house side",
       "low": 425, "high": 1250, "basis": "flat",
       "note": "Steep Rockrimmon and westside pressure zones wear these out; a corroded galvanized connection means rebuilding both sides."},
      {"job": "Sewer service line dug up and repaired at one point",
       "low": 3300, "high": 10500, "basis": "flat",
       "note": "Depth plus decomposed granite and rock make digging slow here, and a sloped lot needs shoring before anyone climbs in."},
      {"job": "Water service line replaced to the main",
       "low": 4800, "high": 16000, "basis": "flat",
       "note": "Distance to the tap, driveway and sidewalk crossings, utility inspection scheduling and frozen winter ground drive the top."}
    ]
  },
  "pricing_lede": "What follows is a researched picture of plumbing emergency costs in Colorado Springs, together with the permit and utility inspection amounts published for this region and the reasons a house at six thousand feet fails differently than one at sea level.",
  "pricing_body": """### Two houses, one job description, two prices

Take a failed water heater. In a Briargate garage with clearances on every side, the appliance comes out, the new one goes in, and the inspector has room to look at everything. Take the same failure in a hillside Old Colorado City house where the heater sits in a closet with an undersized vent and a floor drain nowhere near it, and the same job now includes venting, a drain pan with a routed discharge, and expansion control that was never there. The label on the work order is identical. The scope is not.

That gap is what a range is for. The variables that decide where a job sits are reach, condition of the pipe already in place, and how much of the code catch-up the old installation postponed. Pikes Peak Regional Building Department's own water heater handout tells you what an inspector actually checks: an appliance listed for the application, safe venting and combustion air, shutoffs, relief valve discharge, and expansion control. Anything on that list that is missing today becomes part of the price tomorrow.

### Altitude, freeze-thaw and the local failure calendar

Colorado Springs Municipal Airport sits at 6,147 feet, and the thirty-year normals for January pair a 45 degree afternoon with an 18.5 degree night. That daily swing, not a single deep freeze, is what breaks pipe here. Water in an exposed line thaws, moves, refreezes and expands again on the same twenty-four hour cycle, so failures cluster in exterior walls, crawlspaces, garages and irrigation stub-outs rather than in the middle of a heated house. It also means the busiest hours for emergency work land in the coldest part of the night, when labor is at its most expensive.

Ground conditions do the same thing to buried lines. Digging through decomposed granite and rock is slower than digging through loam, sloped lots need shoring before anybody works in a trench, and winter ground has to be broken before it can be moved. Depth and soil, not pipe diameter, decide the cost of an excavation in El Paso County.

### One utility, several separate fees

Colorado Springs Utilities delivers electricity, natural gas, water and wastewater as a single community-owned enterprise, which makes the billing simpler and the permitting less so, because the utility inspects service lines on top of the building department's permit. A repair, alteration or additional install on a single-family wastewater service carries a $200 utility permit; the water service line inspection for a new installation or repair runs $160; and each return trip after the first costs $100 again. Separately, the regional building department charges $40 for a water heater replacement permit, $75 when the vent goes with it, $50 for a furnace or boiler replacement, and $30 for a lawn sprinkler backflow device or a water softener install.

None of those amounts is large. What they buy is scheduling, and scheduling is the thing that turns a one-day repair into a three-day one. A return inspection trip caused by an unfinished detail costs both the fee and another slot on the calendar.

### What belongs in a written estimate

Ask for the failure named, not the symptom repeated. On a leak that means the location and how it was found; on a drain that means camera footage with distance and depth marked; on a pressure complaint that means the actual static reading at a hose bib. Permits and utility inspections belong on their own lines with the fee shown, because they are pass-through amounts published by the building department and the utility. On any excavation the estimate should state trench depth, shoring, how the surface gets restored, who calls in the locates, and what happens to the yard. Diagnostic labor and repair labor should be separate figures with a clear statement about whether one applies against the other.

### The trap here

Cold snaps produce two predictable sales pitches. The first is whole-house repiping proposed after a single frozen break, when the actual fix is a repair plus insulation and a heat source in the space that froze. The second is a same-night replacement of a water heater that failed on a relief valve or a thermocouple, sold before anyone tested the part. Both are easier to sell at two in the morning than at noon. If water is contained and the shutoff holds, the honest move is a temporary repair now and a decision in daylight. Also watch for jetting proposed sight unseen on old lines and for membership plans presented as a condition of the visit.

### What a national average leaves on the floor

Cost pages built for the whole country miss most of what has been listed above: the regional building department permit, the two separate utility inspections, the return trip charges, shoring on a sloped lot, rock in the trench, and restoration of a driveway or sidewalk crossing. They also assume the old installation met current code, which around here is exactly the assumption that fails. The equipment is the predictable part of the invoice. Everything published on this page is the part people find out about afterward."""
}

# ----------------------------------------------------------- Jacksonville, FL
DATA["jacksonvilleemergencyplumberpros.com"] = {
  "pricing": {
    "mode": "cost",
    "table_head": "Cost ranges for plumbing emergencies across Duval County",
    "anchors": [
      {
        "label": "Minimum plumbing permit fee",
        "value": "$60",
        "detail": "The floor for a plumbing permit under the city's fee schedule, regardless of how the itemized formula adds up on a small repair.",
        "source_name": "City of Jacksonville fee schedule, Section 320.409",
        "source_url": "https://www.jacksonville.gov/departments/finance/city-fees"
      },
      {
        "label": "Permit line for each fixture or sewer connection",
        "value": "$11",
        "detail": "Charged per roughed-in fixture or plugged outlet, per building sewer connection, and per $100 of estimated cost on repairs to waste, soil, vent or building drain pipe.",
        "source_name": "City of Jacksonville fee schedule, Section 320.409",
        "source_url": "https://www.jacksonville.gov/departments/finance/city-fees"
      },
      {
        "label": "JEA sewer tap, six-inch connection",
        "value": "$8,330",
        "detail": "What the utility charges to set a six-inch sewer connection, with a $2,894 tap extension fee where an existing tap only needs bringing to the property line.",
        "source_name": "JEA water and sewer system tariff",
        "source_url": "https://www.jea.com/Pdf/Download/12884909745"
      },
      {
        "label": "JEA water tap and meter set, three-quarter inch service",
        "value": "$1,360 plus $300",
        "detail": "The tap fee for a one-inch tap serving a three-quarter inch line, plus the meter set fee, charged before any plumbing contractor touches the house side of the meter.",
        "source_name": "JEA water and sewer system tariff",
        "source_url": "https://www.jea.com/Pdf/Download/12884909745"
      }
    ],
    "rows": [
      {"job": "Same-day emergency visit for a leak or a backed-up drain",
       "low": 155, "high": 465, "basis": "per visit",
       "note": "Nights, weekends and the days after a storm run high; a routine weekday appointment runs lowest."},
      {"job": "Toilet or shower line cleared through an accessible cleanout",
       "low": 175, "high": 495, "basis": "flat",
       "note": "One fixture and a working cleanout is the floor. Old cast iron with a scale-narrowed bore fights back."},
      {"job": "Camera inspection of a cast iron drain under the slab",
       "low": 265, "high": 750, "basis": "flat",
       "note": "Cleanout access, multiple branches and a written report with depths and distances set the price."},
      {"job": "Slab leak located and the supply line repaired or rerouted",
       "low": 900, "high": 4800, "basis": "flat",
       "note": "Rerouting overhead usually beats opening the floor twice. Tile, terrazzo and finished flooring drive the top end."},
      {"job": "Water heater changed out, 40 or 50 gallon tank",
       "low": 1350, "high": 3400, "basis": "per unit",
       "note": "Garage and utility-room installs are simplest; a pan, drain routing and updated shutoffs add to the total."},
      {"job": "Section of failed cast iron drain line replaced under the slab",
       "low": 4200, "high": 16500, "basis": "flat",
       "note": "Length of the run, concrete thickness, high groundwater in the trench and flooring restoration all push this upward."},
      {"job": "Sewer lateral repaired or replaced from house to city main",
       "low": 5500, "high": 22000, "basis": "flat",
       "note": "Sandy soil caves in and needs shoring, the water table shows up early, and a street cut adds permit and repaving cost."}
    ]
  },
  "pricing_lede": "This page explains what plumbing emergencies cost in Jacksonville, what the city and JEA publish in permit, tap and inspection fees, and why sand, a shallow water table and mid-century cast iron under a slab shape almost every number on it.",
  "pricing_body": """### The variables that actually set the price

Ask two questions about any plumbing emergency in Duval County and you can usually predict which half of a range it lands in. First: is the failed pipe reachable, or is it under concrete? Second: is it supply or drainage? A supply leak announces itself, holds pressure and can be isolated at a valve. A drainage failure under a slab announces itself slowly, through a damp spot or a smell, and by then the repair involves flooring, concrete and a schedule.

Hours matter too, though less than people expect. The bigger multiplier is whether the crew can work in one trip or has to break the job into demolition, repair, inspection and restoration. Every added trip is mobilization billed again.

### Cast iron, sand and a water table five feet down

Two local facts explain most of the expensive work in this city. The first is the drain material in mid-century housing: cast iron was standard in Jacksonville homes for decades, and after fifty or sixty years in Florida soil it scales inward, cracks along the bottom and separates at joints. In Riverside, Avondale, San Marco and Springfield that pipe frequently runs beneath a slab, and the pipe cannot be inspected without a camera or replaced without concrete work.

The second is water. A U.S. Geological Survey report puts the water table within five feet of the surface across most of Duval County, with as much as five feet of seasonal swing. That single fact raises the cost of every excavation here: trenches in saturated sand slump and need shoring, water has to be pumped while somebody works, and city residential inspection guidance requires underground plumbing to be tested and observed before it is buried. Add the septic tank phase-out, where a 2024 city presentation counted roughly 23,000 failing septic tanks across 35 failure areas, and there is a whole category of work in this market that ends in a new sewer connection rather than a repair.

### What the published fees add

The city's schedule is itemized rather than flat. A plumbing permit carries a $60 minimum, and the arithmetic underneath it is $11 per roughed-in fixture or plugged outlet, $11 per building sewer connection, $11 per water service connection, and $11 for each $100 of estimated cost on repairs to water, waste, soil, vent or building drain pipe. Water softeners and solar water heaters are listed at $21. That is small money next to the trench, but it comes with inspection appointments, and on under-slab work an inspection has to happen before concrete goes back.

Utility fees are the ones that surprise people, because they arrive when a septic-to-sewer conversion or a new service is involved rather than on a repair. JEA's tariff lists a six-inch sewer connection at $8,330, a sewer tap extension at $2,894 where an existing tap needs to reach the property line, and a water tap at $1,360 with a $300 meter set for a three-quarter inch service. Water plant capacity charges sit on top of that for a new connection. None of those amounts belongs to the plumbing contractor, and none of them appears in a national cost estimate.

### How to read the estimate you are handed

A useful estimate answers three questions in writing. What failed, and what is the evidence: camera footage with footage marks and depths, or a leak location and the method used to find it. What is the plan: repair a section, reroute overhead, reline, or replace end to end, and why that choice over the others. What is restoration: concrete replaced to what thickness, flooring put back or left to the homeowner, sod or seed, and who pumps and dewaters the trench. Permits should appear as their own line with the fee stated. If under-slab work is proposed without a camera inspection first, that is a proposal built on a guess.

### The trap in this market

Under-slab cast iron is where the pressure selling lives. A single failed section becomes a whole-house repipe proposal, quoted at the kitchen table while a wet spot dries on the floor. Sometimes a full replacement really is the right call, and a camera survey of the whole system is what proves it. Ask for footage of every branch, not one clip. Be equally careful with the reverse trap: patching one joint on a line that is visibly failing along its length buys a few months and then charges for the same demolition twice. The third pattern to watch is jetting sold on old cast iron without an inspection, which can open a hole in pipe that was already thin.

### What the number found online skips

An average cost page assumes a repair reached from above, in dry soil, with no permit and no inspection wait. Jacksonville rarely provides that. Missing from those figures: dewatering, shoring in sand, the required inspection before backfill or concrete, floor covering nobody can match, the septic abandonment steps when a house converts to sewer, and the utility tap and capacity fees that arrive with a new connection. The pipe and the fittings are cheap. Getting to them, and putting the house back, is the invoice."""
}

# -------------------------------------------------------- Kansas City, MO
DATA["kansascityemergencyplumber.com"] = {
  "pricing": {
    "mode": "cost",
    "table_head": "What plumbing emergencies cost on the Missouri side of Kansas City",
    "anchors": [
      {
        "label": "Plumbing permit, one- and two-family dwellings",
        "value": "$52 minimum",
        "detail": "The city's valuation table sets $52 for work valued up to $1,000, $58 for the first $2,000, then $4.33 for each additional $1,000 of job value.",
        "source_name": "Kansas City Code of Ordinances Sec. 18-20",
        "source_url": "https://kansascity-mo.elaws.us/code/coor_ch18_arti_sec18-20"
      },
      {
        "label": "Water service permit, KC Water",
        "value": "$100",
        "detail": "Charged per permit whether a tap is made, a new service installed, or an existing service altered, extended, renewed or repaired from the first valve to the building.",
        "source_name": "KC Water rate book, schedule of fees and charges",
        "source_url": "https://www.kcwater.us/wp-content/uploads/2026/03/Rate-Book-FY-2027_031726-1.pdf"
      },
      {
        "label": "Restoring service after a meter or tap is pulled",
        "value": "$610",
        "detail": "What the utility charges to restore terminated service once it has removed a meter or a tap at the main, in addition to any permit or tap charges owed.",
        "source_name": "KC Water rate book, schedule of fees and charges",
        "source_url": "https://www.kcwater.us/wp-content/uploads/2026/03/Rate-Book-FY-2027_031726-1.pdf"
      }
    ],
    "rows": [
      {"job": "Off-hours call for a burst line or an active leak",
       "low": 170, "high": 500, "basis": "per visit",
       "note": "Deep-winter nights and the first thaw weekend are the busiest and priciest windows for this call."},
      {"job": "Frozen or split pipe repaired in a basement or crawlspace",
       "low": 350, "high": 1600, "basis": "flat",
       "note": "Open joists keep it quick. A break inside a plaster wall or above a finished basement ceiling costs more to reach and patch."},
      {"job": "Main line rodded open through a basement cleanout",
       "low": 210, "high": 625, "basis": "flat",
       "note": "Clay tile joints full of roots in Brookside and Waldo may need two passes before the line runs clear."},
      {"job": "Sewer line inspected on camera with a surface locate",
       "low": 235, "high": 675, "basis": "flat",
       "note": "Long runs from older Hyde Park and Pendleton Heights houses to the main add time, as does clearing before the camera fits."},
      {"job": "Sump pump or ejector pump replaced",
       "low": 550, "high": 2100, "basis": "per unit",
       "note": "Battery backup, a sealed basin for an ejector, and a new check valve and discharge line raise the total."},
      {"job": "Water heater replaced, 40 or 50 gallon tank",
       "low": 1400, "high": 3500, "basis": "per unit",
       "note": "A basement with tight stair access, plus new venting and an expansion tank on a pressure-regulated service, adds hours."},
      {"job": "Cast iron drain stack section replaced",
       "low": 1800, "high": 7500, "basis": "flat",
       "note": "Stacks buried in walls of century-old houses mean demolition, temporary drainage and plaster repair afterward."},
      {"job": "Sewer lateral or water service replaced out to the main",
       "low": 5200, "high": 19000, "basis": "flat",
       "note": "Depth below the frost line, limestone in the trench, steep lots and a street cut with repaving set the ceiling."}
    ]
  },
  "pricing_lede": "Below are researched market ranges for plumbing emergencies in Kansas City, alongside the permit and utility fees the city and KC Water actually publish, and the local reasons an old house on the Missouri side costs what it does to fix.",
  "pricing_body": """### Where a job sits in its range, and why

Three questions decide it. How old is the pipe that failed? How much finished construction stands between a technician and that pipe? And how far from the street does the work have to go? A pinhole in accessible copper above a basement laundry is a short visit. The same pinhole inside a plaster wall in a century-old Hyde Park house is a repair plus demolition plus patching, done by different hands on different days.

Material history explains a lot of the spread here. Cast iron drain, waste and vent piping was standard in homes built from the 1950s into the early 1980s, and local inspection work still turns up original lead and cast iron in houses of that vintage. Older neighborhoods add clay tile laterals to the mix. Those materials do not fail at a single point; they fail along a length, which is why a rodding visit and a camera survey often produce two very different conversations about money.

### Winter is the local cost driver

Kansas City freezes hard enough to break plumbing on a schedule. National Weather Service records for the February 2021 event show minimums of minus six, minus ten and minus thirteen degrees on three consecutive days. In that kind of cold, pipe in an unheated crawlspace, a garage wall or an exterior kitchen run does not survive, and everyone calls at once. Two things follow. Emergency labor is at its most expensive precisely when the failures cluster, and materials for the routine repairs run short at supply houses during the same week.

Frost depth matters just as much for buried work. A lateral or a water service has to be replaced below the frost line, which means a deeper trench than a milder city would dig, and limestone shows up in plenty of trenches around here. Hills add shoring. Winter ground adds hours. Those are the reasons excavation numbers in this market start where they do.

### Two states, and the fees on the Missouri side

The metro's shared name hides two separate permitting and water authorities. Kansas City, Missouri requires permits before most plumbing work, while water customers in Kansas City, Kansas are served by a different utility with its own rules. On the Missouri side the city's own fee table for one- and two-family dwellings starts at $52 for work valued up to $1,000, moves to $58 for the first $2,000, and adds $4.33 for each additional $1,000 of job value.

KC Water bills separately. A water service permit costs $100 per permit, and that applies not only to a new tap but to altering, extending, renewing or repairing an existing service from the first valve to the building. Plan review runs $110 for up to ten service connections, and a resubmission after a rejection costs $65. If a meter or tap has already been removed, restoring service costs $610 on top of any permit or tap charge. On a straightforward repair those are small amounts. On a service line replacement they are real, and they belong on an estimate rather than in a surprise.

### What a real estimate contains

Look for the diagnosis in writing with the evidence attached: the leak location and how it was found, or camera footage with distances and depths for a drain. Look for the plan stated as a choice among options, since a spot repair, a stack replacement and a full lateral replacement are three different projects with three different prices. Permits and utility fees should be their own line items at published amounts. On any dig, the estimate should say how deep, whether shoring is needed, how the trench is backfilled and compacted, what happens to the driveway or street cut, and who calls in the locates. Diagnostic and repair labor should be listed separately with a clear rule about whether the first applies against the second.

### The pattern that costs people money

Basement backups are the pressure point in this market. When a floor drain surges during a heavy rain, a full lateral replacement is easy to sell on the spot. Sometimes the pipe is genuinely finished. Often it is roots at one clay joint, or a mainline problem that is not the homeowner's line at all, which is worth checking with the utility before signing anything. A rodding today and a camera survey tomorrow costs a fraction of a wrong decision made tonight. Two smaller habits to watch: jetting quoted before any inspection on old clay or cast iron, and a maintenance membership pitched at the moment of highest stress. And in a freeze, a repair plus real insulation and a heat source in the space that froze usually beats a repipe proposal written the same night.

### What a national average leaves out

Cost guides written for the whole country assume shallow trenches, unfrozen ground, no permits and no restoration. Missing here: the city permit and its inspection wait, the KC Water service permit, plan review and restoration fees, frost-depth excavation, rock and shoring, street cut repaving, and the plaster, tile and paint that follow work inside an old house. On a backup they also leave out the diagnostic step that tells you whose pipe actually failed, which is the best money spent on the entire problem."""
}


def main():
    for domain, payload in DATA.items():
        sd = SITES / domain
        sj = sd / "site.json"
        data = json.loads(sj.read_text(), object_pairs_hook=collections.OrderedDict)
        data["pricing"] = payload["pricing"]
        sj.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")

        cm = sd / "copy.md"
        text = cm.read_text().rstrip("\n")
        # drop any previous pricing sections so the script is re-runnable
        idx = text.find("\n## pricing_lede")
        if idx != -1:
            text = text[:idx].rstrip("\n")
        text += (
            "\n\n## pricing_lede\n\n" + payload["pricing_lede"].strip()
            + "\n\n## pricing_body\n\n" + payload["pricing_body"].strip() + "\n"
        )
        cm.write_text(text)
        print("wrote", domain)


if __name__ == "__main__":
    main()
