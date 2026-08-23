"""Pricing blocks for garage door batch 1. Anchors fetched 2026-08-23."""

PRICING = {
"annarborgaragedoorrepairpros.com": {
  "copy": "pricing-copy-annarbor.md",
  "pricing": {
    "mode": "cost",
    "table_head": "What garage door work runs in Ann Arbor",
    "anchors": [
      {
        "label": "Building permit, project cost up to $1,000",
        "value": "$100",
        "detail": "Ann Arbor prices a residential permit from estimated project cost, and the first tier includes one rough and one final inspection. A nonrefundable $15 base application fee is added to every permit.",
        "source_name": "City of Ann Arbor building permit fee sheet, revised July 2025",
        "source_url": "https://www.a2gov.org/media/xoynsgau/building_fees_2025v1.pdf"
      },
      {
        "label": "Each extra inspection on an open permit",
        "value": "$35",
        "detail": "Charged per inspection added to an open permit, billed after the inspection happens. A failed rough on a new opener circuit is what usually triggers it.",
        "source_name": "City of Ann Arbor permit fees page",
        "source_url": "https://www.a2gov.org/building-rental-and-inspection-services/construction-and-building/permits/fees/"
      },
      {
        "label": "Median hourly wage, maintenance and repair workers",
        "value": "$23.64",
        "detail": "May 2025 median hourly pay in the Ann Arbor metro for the occupation that covers door and opener service. A billed hourly figure carries truck, spring inventory, insurance and drive time on top of that wage.",
        "source_name": "BLS Occupational Employment and Wage Statistics, May 2025, Ann Arbor metro",
        "source_url": "https://www.bls.gov/oes/current/oes_11460.htm"
      }
    ],
    "rows": [
      {"job": "Service call to diagnose a door that will not open",
       "low": 79, "high": 195, "basis": "per visit",
       "note": "A weekday morning slot sits at the bottom. Evenings, weekends and a car sealed inside during a January storm sit at the top."},
      {"job": "Broken torsion spring replaced on a two-car door",
       "low": 245, "high": 640, "basis": "flat",
       "note": "Both springs together, oversized wire, or cones seized onto a shaft in an unheated detached garage move it upward."},
      {"job": "Both lift cables replaced after the door hangs crooked",
       "low": 175, "high": 470, "basis": "flat",
       "note": "Salt-corroded bottom brackets that shear off during removal turn a cable job into bracket and track work as well."},
      {"job": "Rollers and hinges replaced across a 16-foot door",
       "low": 165, "high": 445, "basis": "per unit",
       "note": "Sealed-bearing rollers and hinges rusted into the stiles on a 1960s door both push this toward the high end."},
      {"job": "Door lifted back onto a bent track",
       "low": 210, "high": 720, "basis": "flat",
       "note": "Straightening is cheap; replacing a kinked vertical section, a top fixture and a flag bracket after a bumper strike is not."},
      {"job": "Opener gear kit or logic board replaced",
       "low": 185, "high": 590, "basis": "flat",
       "note": "Parts for a discontinued unit, a ceiling too high to reach from a stepladder, or a second trip for landlord approval add cost."},
      {"job": "Single bottom section replaced on a steel door",
       "low": 360, "high": 1250, "basis": "per unit",
       "note": "Matching a discontinued profile and color is the whole cost here. An unmatchable section pushes the decision to a full door."},
      {"job": "Sectional door replaced, insulated steel, opener reused",
       "low": 1450, "high": 4400, "basis": "per unit",
       "note": "Low-headroom track, a historic district review on a street-facing door, or an oversized opening reach the top."}
    ]
  }
},

"bocaratongaragedoorrepairpros.com": {
  "copy": "pricing-copy-boca.md",
  "pricing": {
    "mode": "cost",
    "table_head": "Boca Raton market ranges for garage door work",
    "anchors": [
      {
        "label": "Minimum permit fee, alteration or repair including garage doors",
        "value": "$100",
        "detail": "Covers the first $500 of construction valuation in a category the schedule expressly applies to garage doors, then 1.75 percent of the remaining valuation, plan check and sub-permits included.",
        "source_name": "City of Boca Raton user fee schedule, building permit section",
        "source_url": "https://myboca.us/DocumentCenter/View/22579/User-Fees-Schedule-Building-Permit-Section-PDF"
      },
      {
        "label": "Garage door permit, storm damage repair within one year of a named storm",
        "value": "$99",
        "detail": "Its own line on the city schedule for repairing damage after a named storm event or declared state of emergency. Retrofitting is excluded, and a reinspection is $79.",
        "source_name": "City of Boca Raton user fee schedule, building permit section",
        "source_url": "https://myboca.us/DocumentCenter/View/22579/User-Fees-Schedule-Building-Permit-Section-PDF"
      },
      {
        "label": "Design wind velocity used for a single family residence",
        "value": "170 mph",
        "detail": "The figure the city applies to openings on a single family home, with product approval or Notice of Acceptance documents for every installed product required on site for inspection.",
        "source_name": "City of Boca Raton over-the-counter windows, doors and shutters affidavit",
        "source_url": "https://www.myboca.us/DocumentCenter/View/22225/Single-Family-Windows-Doors-Shutters-Affidavit-PDF"
      }
    ],
    "rows": [
      {"job": "Trip charge and diagnosis on a door that stopped working",
       "low": 89, "high": 225, "basis": "per visit",
       "note": "Bottom of the band is a scheduled weekday call. Top is after hours, or the week a named system is tracking toward the coast."},
      {"job": "Torsion spring set replaced on a wind-rated double door",
       "low": 280, "high": 780, "basis": "flat",
       "note": "A rated door weighs more, so wire sizes run heavier. Drums seized by salt corrosion on the shaft add removal time."},
      {"job": "Cables and drums replaced after strands corroded through",
       "low": 220, "high": 620, "basis": "flat",
       "note": "Chloride off the shoreline eats cable where it wraps. Set screws welded into the drum by corrosion decide the top of this range."},
      {"job": "Photo eyes, bottom seal and roller service on a door that reverses",
       "low": 140, "high": 420, "basis": "flat",
       "note": "Sand and salt crust packed into the astragal, plus a loosened photo eye bracket, are the usual pair behind this complaint."},
      {"job": "Opener replaced, existing rail and rated door reused",
       "low": 420, "high": 1150, "basis": "per unit",
       "note": "Battery backup, a taller ceiling needing a rail extension, and hardwiring a receptacle that was never installed move it up."},
      {"job": "Wind-rated sectional door and track replaced, permitted",
       "low": 2300, "high": 8200, "basis": "per unit",
       "note": "Impact-rated glass, a masonry fastening pattern into tie columns, association-approved styling and inspection scheduling reach the ceiling."}
    ]
  }
},

"carrolltongaragedoorrepairexperts.com": {
  "copy": "pricing-copy-carrollton.md",
  "pricing": {
    "mode": "cost",
    "table_head": "Carrollton cost ranges, job by job",
    "anchors": [
      {
        "label": "Residential remodel permit, when one is required",
        "value": "$125",
        "detail": "The city also charges a nonrefundable $125 application processing fee, and where a permit would cost less than $125 the permit fee is charged as that application fee.",
        "source_name": "City of Carrollton building inspection fee list",
        "source_url": "https://www.cityofcarrollton.com/departments/departments-a-f/building-inspection/fees"
      },
      {
        "label": "Single-trade electrical permit, opener circuit",
        "value": "$75 minimum",
        "detail": "Priced at $4 per $1,000 of value with a $75 floor, in the single-trade category that covers electrical work. A reinspection is $50.",
        "source_name": "City of Carrollton building inspection fee list",
        "source_url": "https://www.cityofcarrollton.com/departments/departments-a-f/building-inspection/fees"
      },
      {
        "label": "Miscellaneous construction permit, residential accessory structures",
        "value": "$50",
        "detail": "The category a detached garage structure falls into when work goes beyond a same-size door swap. Investigation fees for work started before a permit issues equal the permit fee.",
        "source_name": "City of Carrollton building inspection fee list",
        "source_url": "https://www.cityofcarrollton.com/departments/departments-a-f/building-inspection/fees"
      }
    ],
    "rows": [
      {"job": "Diagnostic visit on a door that quit mid-cycle",
       "low": 69, "high": 185, "basis": "per visit",
       "note": "Scheduled daytime calls sit low. After a spring storm night, when every route is full, calls sit high."},
      {"job": "Torsion spring replaced on a double-wide door",
       "low": 230, "high": 610, "basis": "flat",
       "note": "Undersized original springs on a late-1980s door often need a resize, and doing both at once costs more today and less later."},
      {"job": "Cable and drum reset on a door that racked in high wind",
       "low": 190, "high": 540, "basis": "flat",
       "note": "Straight-line wind leaves one side dragging. Uneven wear on both drums and a tweaked flag bracket set the upper figure."},
      {"job": "Rollers, hinges and bearing plates replaced",
       "low": 155, "high": 430, "basis": "per unit",
       "note": "Worn hinges tearing out of stiles on an original builder-grade door add section repair time to a hardware job."},
      {"job": "Opener repaired or replaced, rail reused",
       "low": 175, "high": 720, "basis": "flat",
       "note": "A gear kit is the low figure. A new unit with a permitted circuit, plus the electrical minimum and inspection, is the high one."},
      {"job": "Bottom section replaced after a vehicle contact",
       "low": 340, "high": 1150, "basis": "per unit",
       "note": "Matching a discontinued panel profile and paint, and correcting a bent track behind it, decide where this lands."},
      {"job": "Same-size sectional door replaced, no permit needed",
       "low": 1250, "high": 3900, "basis": "per unit",
       "note": "Insulation value, window inserts, association styling rules and a low-headroom conversion account for the whole spread."}
    ]
  }
},

"danvillegaragedoorrepairpros.com": {
  "copy": "pricing-copy-danville.md",
  "pricing": {
    "mode": "cost",
    "table_head": "Danville and San Ramon Valley market ranges",
    "anchors": [
      {
        "label": "Minimum building permit and inspection fee, any permit",
        "value": "$122",
        "detail": "The Town's floor for a permit, applied per inspection where no other fee is listed, and also the minimum for a reinspection. Building permit fees themselves start at $25.08 for the first $500 of valuation.",
        "source_name": "Town of Danville Master Fee Schedule 2026/27",
        "source_url": "https://www.danville.ca.gov/DocumentCenter/View/836/Master-Fee-Schedule-PDF"
      },
      {
        "label": "Electrical sub-permit, opener circuit",
        "value": "20 percent of the building permit fee",
        "detail": "Charged on top of the building permit when a circuit is added or altered. Structural and architectural plan review, where drawings are reviewed, runs 65 percent of the building fee.",
        "source_name": "Town of Danville Master Fee Schedule 2026/27",
        "source_url": "https://www.danville.ca.gov/DocumentCenter/View/836/Master-Fee-Schedule-PDF"
      },
      {
        "label": "California contractor license bond",
        "value": "$25,000",
        "detail": "The bond amount every licensed California contractor has carried since January 1, 2023, along with a $25,000 bond of qualifying individual where that applies. Compliance overhead is priced into every market in the state.",
        "source_name": "Contractors State License Board bond requirements",
        "source_url": "https://www.cslb.ca.gov/contractors/maintain_license/bond_information/bond_requirements.aspx"
      }
    ],
    "rows": [
      {"job": "Diagnostic call on a door that stopped part-way",
       "low": 95, "high": 260, "basis": "per visit",
       "note": "Weekday daytime is the floor. Evening and weekend work, or a hillside address with nowhere to park a truck, is the ceiling."},
      {"job": "Torsion springs replaced on a two-car door",
       "low": 290, "high": 780, "basis": "flat",
       "note": "Tuck-under garages with short headroom and a shaft crowded against framing add time that flat pads do not."},
      {"job": "Cables, drums and bearing plates replaced",
       "low": 235, "high": 660, "basis": "flat",
       "note": "Uneven drum wear from a door that has been running out of level for months widens the scope beyond the snapped cable."},
      {"job": "Door reset on track after coming off one side",
       "low": 250, "high": 850, "basis": "flat",
       "note": "A clean reset is the low figure. Replacing a kinked track, top fixture and a torn end stile reaches the high one."},
      {"job": "Weatherseal and perimeter gasketing replaced for ember resistance",
       "low": 180, "high": 620, "basis": "per unit",
       "note": "Full-width bottom seal contact plus side and top stripping on a slab that has settled unevenly sets the top of this row."},
      {"job": "Opener replaced with the existing door and rail",
       "low": 480, "high": 1300, "basis": "per unit",
       "note": "Battery backup is required on new residential openers statewide, and a permitted new circuit adds the sub-permit and an inspection."},
      {"job": "Insulated sectional door and hardware replaced",
       "low": 1900, "high": 6800, "basis": "per unit",
       "note": "Custom panel designs answering a design review comment, low-clearance track and a steep driveway haul-off account for the range."}
    ]
  }
},

"edenprairiegaragedoorrepairpros.com": {
  "copy": "pricing-copy-edenprairie.md",
  "pricing": {
    "mode": "cost",
    "table_head": "Eden Prairie garage door costs by job",
    "anchors": [
      {
        "label": "Building permit fee, valuation $1 to $500",
        "value": "$40.00",
        "detail": "The city's lowest valuation tier. Work valued between $2,001 and $25,000 is $105.25 for the first $2,000 plus $19.75 per additional $1,000, with plan checking at 65 percent and reinspection at $50.00 per hour.",
        "source_name": "City of Eden Prairie fee schedule for administration of official controls, City Code Chapter 25",
        "source_url": "https://mcclibraryfunctions.azurewebsites.us/api/ordinanceDownload/15776/1059792/pdf"
      },
      {
        "label": "Minnesota construction surcharge on a fixed-fee permit",
        "value": "$1 or 0.0005",
        "detail": "State surcharge collected by the city on every permit for construction, addition or alteration: one-half mill of the permit fee or one dollar on fixed-fee permits, and 0.0005 of valuation on valuation-based permits.",
        "source_name": "Minnesota Statutes section 326B.148",
        "source_url": "https://www.revisor.mn.gov/statutes/cite/326B.148"
      },
      {
        "label": "Median hourly wage, maintenance and repair workers",
        "value": "$29.07",
        "detail": "May 2025 median hourly pay across the Minneapolis-St. Paul-Bloomington metro for the occupation covering door and opener service. Loaded labor on an invoice runs a multiple of the wage figure.",
        "source_name": "BLS Occupational Employment and Wage Statistics, May 2025, Minneapolis-St. Paul-Bloomington metro",
        "source_url": "https://www.bls.gov/oes/current/oes_33460.htm"
      }
    ],
    "rows": [
      {"job": "Service visit to find out why the door will not move",
       "low": 89, "high": 210, "basis": "per visit",
       "note": "Bottom is a booked daytime appointment. Top is a subzero morning with a vehicle shut in and every truck already dispatched."},
      {"job": "Broken torsion spring replaced, two-car door",
       "low": 260, "high": 690, "basis": "flat",
       "note": "Springs break on the coldest mornings, when demand peaks. Replacing the pair and resizing undersized wire raises the figure."},
      {"job": "Bottom bracket and cable replaced after the seal froze down",
       "low": 195, "high": 560, "basis": "flat",
       "note": "Meltwater and road salt corrode the lower bracket. If the bolt shears in the stile, the section needs repair too."},
      {"job": "Bottom seal and perimeter weatherstripping replaced",
       "low": 130, "high": 390, "basis": "per unit",
       "note": "A slab lifted by frost needs a thicker astragal or a retainer swap so the door meets concrete across the full width."},
      {"job": "Rollers, hinges and end bearings replaced",
       "low": 160, "high": 450, "basis": "per unit",
       "note": "Sealed-bearing rollers cost more and survive cold better than open bearings packed with grease that stiffens each winter."},
      {"job": "Opener repaired, gear kit or control board",
       "low": 180, "high": 620, "basis": "flat",
       "note": "A stripped gear is the low end. A discontinued unit needing parts sourced, or a second visit for wiring, is the high end."},
      {"job": "Insulated sectional door replaced, opener reused",
       "low": 1500, "high": 4600, "basis": "per unit",
       "note": "Higher insulation value, oversized openings on newer Bearpath and Homeward Hills homes, and permitted framing changes push it up."}
    ]
  }
}
}
