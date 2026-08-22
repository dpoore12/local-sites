# Writer Report — coloradospringsfurnacerepair.com

**Status:** PASS for the assigned site. The individual build passed on 2026-08-21:

- Home: 2,877 visible words
- About: 318 visible words
- Contact: 629 visible words
- Four 200–360-word symptom cards
- Three sourced local facts
- Placeholder phone warning remains intentionally unchanged

## Assigned angle used

The site leads with the **Pikes Peak Regional Building Department** as the mechanical permit authority for Colorado Springs, and treats **downslope/high-wind conditions** as an inspection-context fact: exterior intake/exhaust terminations and vent connections are relevant to inspect when a furnace fault begins after a wind event. It does **not** lead with high-altitude furnace derating, which is reserved for the Denver furnace site.

## Three sourced local facts

1. **PPRBD is the regional permitting authority.** Pikes Peak Regional Building Department says it issues and manages building permits for Colorado Springs, and lists furnace construction, installation, and replacement as requiring a permit. This informs the copy’s distinction between a diagnostic repair and a furnace replacement project.
   - https://www.pprbd.org/Information/HomeownerPermit

2. **Dated wind condition.** The National Weather Service documented an extreme-wind event on December 15, 2021, including a 92 mph gust at Colorado Springs Airport at 12:54 PM MST. The site uses that fact to explain why a post-wind furnace failure can warrant an accessible intake/exhaust termination and venting check; it does not assert wind caused every fault.
   - https://www.weather.gov/pub/ExtremeWindEvent_20211215

3. **Housing vintage.** The City of Colorado Springs housing-needs fact sheet reports a median year of construction of 1986. The copy uses this only as context for mixed equipment, duct, thermostat, and insulation histories—not as a diagnosis or a replacement trigger.
   - https://coloradosprings.gov/system/files/2025-07/hna_co_springs_factsheet_2025_07_10a_lv.pdf

Six neighborhood names were taken from the City of Colorado Springs PlanCOS framework map: Briargate, Old Colorado City, Patty Jewett, Downtown, Broadmoor Hills, and Northgate.
- https://mayor.coloradosprings.gov/system/files/plancos_ch2_neighborhoods_framework_map.pdf

## Image assets

Generated four original documentary-style images and installed optimized progressive JPEGs:

- `assets/hero.jpg` — 1800 × 1013
- `assets/work-1.jpg` — 900 × 507
- `assets/work-2.jpg` — 900 × 507
- `assets/work-3.jpg` — 900 × 507

## Shared-template notes

No remaining garage-door or other-trade wording leaks were found in the rendered template. One general copy concern remains: the locked template hardcodes “Three steps, one phone call” and “The call is the whole process.” It is generic, not another-trade leakage, but it somewhat conflicts with the writer instruction to sell dispatched onsite work rather than a phone conversation. Site-specific blocks clearly state that the technician inspects the equipment and quotes the repair before work begins.

## Full-build result

`python3 template/build.py` was run after the individual pass. This site passed the repository-wide cross-site duplicate comparison with no shared-word-run error. The full command currently exits nonzero because of independent errors in other assigned sites:

- `charlotteguttercleaningpros.com`: `symptom_3` and `symptom_4` exceed the phase-1 360-word maximum.
- `overlandparkgaragedoorrepairpros.com`: an unverifiable “thousands of” claim and shared 15-word runs with `bocaratongaragedoorrepairpros.com`.

No facts required by this site were left unsourced.
