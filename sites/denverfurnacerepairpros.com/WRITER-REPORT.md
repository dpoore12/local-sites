# Writer Report — denverfurnacerepairpros.com

## Result

**Site status: PASS.** Targeted build passed on 2026-08-21.

- Home: **2,749 visible words**
- About: 433 visible words
- Contact: 494 visible words
- Four generated photos are present: `hero.jpg` at 1800 × 1200 and `work-1.jpg` through `work-3.jpg` at 900 × 600.

The complete repository build was run after the target build. This site passed its own cross-site phrase check; the repository command exited nonzero only because two other writers' sites had unrelated validation errors: `charlotteguttercleaningpros.com` had two symptom blocks over the 360-word limit, and `overlandparkgaragedoorrepairpros.com` had an unverifiable claim plus shared wording with Boca Raton. No duplicate run was reported for this Denver site.

## Assigned angle used

The site is built around Denver’s mile-high gas-furnace setup: altitude derating and model-specific high-altitude components, combined with the city’s replacement-permit route and a large base of 1950s housing. The repair copy repeatedly distinguishes a diagnosed no-heat component repair from a replacement project, which may add sizing, gas-piping and permit work.

## Three sourced local facts

1. **Older furnace footprint.** Denver built roughly 31,000 single-family detached homes during the 1950s—the city’s leading decade for that type of construction. The source identifies Harvey Park, Virginia Village and Washington-Virginia Vale among the areas developed in that period. This supports copy about mid-century equipment locations, retrofit duct paths and altered return-air arrangements. [Denver Urbanism: Denver’s Single-Family Homes by Decade—1950s](https://denverurbanism.com/2012/05/denvers-single-family-homes-by-decade-1950s.html)

2. **Mile-high setup and permit rule.** Denver’s official elevation is 5,280 feet. A manufacturer’s high-altitude instructions for its covered furnaces state that units above 2,000 feet are derated by 4% per 1,000 feet, require a pressure-switch change at 5,000 feet, and may need an orifice change based on elevation and gas heating value. The City’s code briefing says that like-for-like gas-furnace replacements are not Quick Permits as of March 1, 2023 except for emergency replacement, and identifies sizing, gas-piping testing and an electrification feasibility report among the relevant replacement requirements. [CU Denver—About Denver](https://www.ucdenver.edu/international-admissions/about-cu-denver/about-denver-co) · [Rheem high-altitude kit instructions](http://pts.myrheem.com/docstore/webdocs/ServiceDocs/HistLib/pdfs/Accessories/RXGY/92-24096-01-06_RXGY-F04_F05_F06_F07.pdf) · [City and County of Denver code-adoption briefing](https://denver.prelive.opencities.com/files/assets/public/v/1/community-planning-and-development/documents/ds/building-codes/code-adoption/2022-building-code-adoption-briefing-presentation.pdf)

3. **Documented extreme cold.** NWS Boulder reports that the December 21, 2022 Arctic front dropped DIA 37°F in one hour; December 22 reached a low of -24°F and averaged -15°F, Denver’s second-coldest day on record. This grounds the no-heat and long-runtime guidance in a dated local condition rather than a generic winter claim. [National Weather Service Boulder—2022 Denver Climate Summary](https://www.weather.gov/media/bou/2022DenverClimateSummary.pdf)

## Template review

- **No other-trade wording rendered on this furnace site.** The previously problematic service-band text is supplied by per-site copy blocks and rendered correctly.
- **Template issue to keep in view:** the shared hero note derives a claim such as “Local Adams County technician” from the first county in `site.json`, even when no tenant exists. That is a pre-tenant assertion about who serves the call and can also name a county before Denver itself. It is not another-trade leakage, but it conflicts with the otherwise cautious no-tenant disclosure. I did not modify the locked shared template.
- `template/LOCKED.md` is also stale documentation: it describes an eight-page phase-2 map, whereas this phase-1 site correctly builds only home, about and contact pages.

## Unresolved sourcing limits

No unsupported local claim was left in the copy. The high-altitude source is expressly model-specific, so the website language limits its examples to covered equipment and directs technicians to the furnace rating plate and applicable manufacturer instructions rather than asserting a universal conversion rule.


## From RESEARCH-SOURCES.md

# Research sources — Denver Furnace Repair Pros

Verified 2026-08-21

1. Denver Urbanism says roughly 31,000 single-family detached homes were built in Denver from 1950 through 1959, including development in Harvey Park, Virginia Village and Washington-Virginia Vale. https://denverurbanism.com/2012/05/denvers-single-family-homes-by-decade-1950s.html
2. CU Denver identifies Denver's official elevation as 5,280 feet. Rheem's high-altitude-kit instructions state furnaces above 2,000 feet require 4% per 1,000-foot derating, a pressure-switch change at 5,000 feet for covered models, and possible orifice changes based on elevation and gas heating value. https://www.ucdenver.edu/international-admissions/about-cu-denver/about-denver-co and http://pts.myrheem.com/docstore/webdocs/ServiceDocs/HistLib/pdfs/Accessories/RXGY/92-24096-01-06_RXGY-F04_F05_F06_F07.pdf
3. Denver's building-code briefing says that, since March 1, 2023, a like-for-like gas-furnace replacement cannot use a Quick Permit except for an emergency replacement; it also lists sizing, gas-piping testing and an electrification feasibility report as the relevant replacement requirements. https://denver.prelive.opencities.com/files/assets/public/v/1/community-planning-and-development/documents/ds/building-codes/code-adoption/2022-building-code-adoption-briefing-presentation.pdf
4. National Weather Service Boulder documented that the December 21–22, 2022 Arctic front dropped DIA 37°F in one hour, with a December 22 low of -24°F and average of -15°F, Denver's second-coldest day on record. https://www.weather.gov/media/bou/2022DenverClimateSummary.pdf
