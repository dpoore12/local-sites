# Writer Report — overlandparkgaragedoorrepairpros.com

**Status:** PASS

## Build result

- Target build: PASS — 2,810 home words, 340 about words, 575 contact words; four symptom cards, three local Q&As, and three sourced facts.
- Full repository build: PASS. Placeholder-number warnings are expected and were left unchanged.
- Images: generated four original, unbranded documentary images and saved them as `assets/hero.jpg`, `assets/work-1.jpg`, `assets/work-2.jpg`, and `assets/work-3.jpg`.

## Three sourced local facts

1. **Housing vintage.** Overland Park's median year built is 1989. That supports a broad mix of established-garage hardware and later sectional/torsion installations, rather than assuming a single housing era. Sources: [Point2 Homes demographic table](https://www.point2homes.com/US/Neighborhood/KS/Overland-Park-Demographics.html) and [U.S. Census Bureau ACS 2024 table B25035](https://data.census.gov/table/ACSDT5Y2024.B25035?tid=ACSDT5Y2024.B25035).
2. **Permit path.** The City of Overland Park says it reviews residential construction plans and documents that require a building permit, and requires an active Johnson County contractor license to receive a building permit for work in the city. Source: [City of Overland Park Building + Construction](https://www.opkansas.org/city-services/building-construction/).
3. **Dated cold condition.** NWS Kansas City/Pleasant Hill included Overland Park in its January 24, 2026 Winter Storm Warning and Cold Weather Advisory, which forecast wind chills as low as 17 below zero and four to six inches of additional snow. Source: [NWS warning and advisory](https://forecast.weather.gov/showsigwx.php?warnzone=KSZ105&warncounty=KSC091&firewxzone=KSZ105&local_place1=Overland+Park+KS&product1=Winter+Storm+Warning).

## Angle used

This is a mechanics-first cold-weather site, not a generic winter/frozen-pipe story. The main spring card explains the sequence: normal cycle fatigue leaves a weak point; a cold snap contracts steel slightly; old lubricant thickens around bearings and drums; a sticky bottom seal adds resistance; and the first lift creates the failure moment. The NWS January 2026 event supplies the local, dated cold condition. The copy keeps the distinction clear: cold exposes an aging spring's fatigue rather than magically creating the defect.

Johnson County / Overland Park housing vintage is used to justify asking about garage age, clearance, and spring system before dispatch. Permit copy is tightly limited to altered openings and city permit requirements; it avoids claiming that a like-for-like residential garage-door replacement is exempt or required because I could not verify that exact rule on a live city page.

## Shared-template / seed leak found

The shared `template/assets/theme.css` includes a non-visible comment using the location-specific example `"Naperville Garage Door Pros"`. It does not render on the Overland Park pages, but the comment is a location leak in a shared template asset and should be changed to a generic example.

The target's inherited phase-2 `site.json` service records also still contain **Naperville** in all four `keyword` values. They are inert in phase 1 and do not render or link on the finished site. I did not change them because the brief explicitly permits changing only `local_facts` and `neighborhoods` in `site.json`; they should be corrected before a phase-2 service build.

## Could not source

I could not find a live Overland Park municipal page that explicitly says whether a straightforward like-for-like residential garage-door replacement itself needs no permit or needs a permit. The site deliberately does not make that claim. Instead, it directs opening or structural changes to the city's permit-review process and says to confirm scope before ordering.
