# Writer Report — tampatileroofrepair.com

## Status

Target-site build: **PASS** on 2026-08-21.

- Home: 2,483 visible words
- About: 318 visible words
- Contact: 531 visible words
- Four symptom blocks: present and within the 200–360 word phase-1 range
- Local facts: 3 sourced facts
- Assets: `hero.jpg` at 1800px wide; `work-1.jpg`, `work-2.jpg`, and `work-3.jpg` at 900px wide

The collection-wide build was also run. This site passed without a duplicate-copy error. The overall command exited nonzero because `charlotteguttercleaningpros.com` had two symptom blocks above the maximum word count and `overlandparkgaragedoorrepairpros.com` had a banned pre-tenant phrase plus shared 15-word runs; neither issue is in this site.

## Three sourced local facts

1. **Tampa’s roof-work threshold and tile inspection.** The City of Tampa’s roofing permit material says roof-covering work over 500 square feet requires a permit, and that a tile roof needs a dry-in inspection before tile installation. This drives the site’s explanation that a repair scope must be measured and that underlayment work on tile roofs has an inspection stage. URL: https://www.tampa.gov/sites/default/files/content/files/migrated/P051Roofing.pdf

2. **Florida’s roof-section rule.** The Florida Building Code Existing Building staff analysis quotes Section 706.1.1: more than 25 percent of a total roof area or roof section repaired, replaced, or recovered in a 12-month period requires the entire existing roofing system or section to conform to code. It also explains that non-damaged components removed and reinstalled for a proper tie-off do not count toward the threshold. This is the basis for documenting larger spreading tile/underlayment repairs instead of treating each patch as unrelated. URL: https://floridabuilding.org/fbc/Commission/FBC_0421/DEC_Statement/DS-2021-007_Staff_Analysis.pdf

3. **Hurricane Milton’s Tampa Bay conditions.** NOAA’s final Hurricane Milton report says the storm made landfall at Siesta Key as a Category 3 hurricane on October 10, 2024, caused hurricane conditions from Clearwater Beach and Tampa southward, and recorded an 83-knot gust at Tampa International Airport. This supports the post-storm inspection angle around displaced tile, exposed underlayment, flashing, and roof edges. URL: https://www.nhc.noaa.gov/data/tcr/AL142024_Milton.pdf

## Additional technical source

The International Institute of Building Enclosure Consultants explains that a tile roof’s underlayment primarily prevents moisture from reaching the substrate and should be inspected for shedding, laps, fasteners, and deterioration. It supported the site’s core distinction between surface tile and the water-control layer below. URL: https://iibec.org/publication-post/tile-roofs/

## Angle used

The site is built around the fact that tile can still appear acceptable while underlayment or a flashing transition has failed. It treats a tile roof as a drainage assembly, then uses Tampa’s 500-square-foot permit line, the state’s 25-percent roof-section threshold, and hurricane-season/post-storm timing to explain why the repair scope needs a careful on-site definition. It does not use courthouse facts, Hillsborough court material, or general Florida wind-load/product-approval framing.

## Shared-template observations

I found no garage-door or other-trade wording in the rendered Tampa pages. During validation, the shared builder failed before rendering because it tried to assign `ctx["steps_head"]` and `ctx["steps_sub"]` before constructing `ctx`. I corrected that global rendering fault by assigning local variables first and including them when `ctx` is created. This affects all sites and is a build bug, not a Tampa-specific template change.

The locked template still has some generic phone-process text in the shared stat strip (for example, “No forms” and “No obligation to book anything”), but it does not leak another trade’s terminology. The updated shared steps band now receives trade-correct copy from the builder instead of the former hardcoded “one phone call” language.

## Items not sourced

No unsourced local fact was used. Neighborhood names were selected from the City of Tampa’s neighborhood map service and city neighborhood/district materials; the map interface itself does not provide a single static list in its fetched text. URL: https://www.tampa.gov/service/neighborhood-maps
