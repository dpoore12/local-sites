## From RESEARCH-NOTES.md

# San Jose emergency plumbing — sourced facts (verified 2026-08-21)

## 1. Housing / plumbing vintage
Median San Jose home built **1975**; 63,300 units built 1960–69 and 80,937 in 1970–79 out of
343,058 total (~42% of the city plumbed in those two decades). The city's adopted housing
element states ~80% of the stock was built 1960 or later, ~20% pre-1960. Era is geographic:
Willow Glen 1910s–40s, Cambrian mid-century 1950s–60s tracts, Eichler tracts 1952–1963,
Almaden Valley / Evergreen from the 1970s on.
- https://www.point2homes.com/US/Neighborhood/CA/Santa-Clara-County/San-Jose-Demographics.html
- https://www.hcd.ca.gov/housing-elements/docs/san_jose_5th_draft100314.pdf
- https://npgallery.nps.gov/GetAsset/2f497523-3628-4d23-aa75-28b253cc33ab

Why it matters: pre-1960 stock = galvanized steel supply + cast iron drains; 1960s–70s = copper
pitting at solder joints. Decides section repair vs repipe vs camera-after-cable.

## 2. Water hardness (San Jose Water)
Groundwater **11–26 grains/gal**, mountain surface water 5–12, imported surface water 4–9.
SJW's own hard-water threshold is 7 gpg / 120 ppm.
- https://www.sjwater.com/water-faqs/
- https://www.sjwater.com/media/ixleehrg/ca4310011_ca4310018-sjw-2025-ccr-002.pdf

Why it matters: scale on tank bottoms and valve seats — early water heater failure, consumed
anode rods, seized angle stops and pressure regulators.

## 3. City permit rule + sewer lateral responsibility (San Jose specific)
Plumbing permit required to install/replace a water heater; for repipe and water service
projects; and to repair/replace a building drain or building sewer or install a property line
cleanout. Sanitary sewer FAQ: the property owner is responsible for the **entire** lateral; the
city maintains the lower portion to the main only as a **courtesy**, and only where an approved
property-line wye cleanout exists **within five feet of the property side of the sidewalk**.
- https://www.sanjoseca.gov/businesses/development-services-permit-center/start-your-project/water-heaters
- https://www.sanjoseca.gov/businesses/development-services-permit-center/start-your-project/repipe-water-service-projects
- https://www.sanjoseca.gov/businesses/development-services-permit-center/start-your-project/sewer-projects
- https://www.sanjoseca.gov/your-government/departments-offices/transportation/sewers-storm-drains/sanitary-sewer/frequently-asked-questions-about-sanitary-sewer-services

## Neighborhoods used
Willow Glen, Cambrian Park, Almaden Valley, Berryessa, Evergreen, Rose Garden

## Build result
`python3 template/build.py sanjoseemergencyplumberpros.com` → PASS
home 3073 words · /about/ 396 · /contact/ 651 · 4 symptoms · 3 Q&As · 3 sourced facts
Only warning: PLACEHOLDER phone (expected).
Full-network `python3 template/build.py` → no FAIL lines; no shared 15-word runs.
