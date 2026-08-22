# Writer report — modestoacrepairpros.com (Air Conditioner Repair, Modesto, CA)

Phase 1 (home + about + contact). Written 2026-08-21. Status: pre-tenant, phone is PLACEHOLDER.

## The three local facts

**1. Half of Modesto's housing predates 1980 (`housing_vintage`)**
Median Modesto housing unit built 1979. The 1970s alone account for 18,432 of 75,882 units — the largest single decade — and roughly 51% of the stock predates 1980 (ACS table B25034/B25035, latest release). Spread is wide: College Area streets around Modesto Junior College (opened 1921) were laid out in the 1920s–30s; Village One on the northeast side is mostly 1990s–early 2000s.
- https://censusreporter.org/profiles/16000US0648354-modesto-ca/
- https://data.census.gov/table/ACSDT5Y2024.B25035
- https://en.wikipedia.org/wiki/College_Area,_Modesto,_California

**2. Modesto-specific heat plus San Joaquin Valley particulate (`valley_heat_and_dust`)**
NWS Sacramento's Modesto climate summary for July 2026: 26 days at or above 90°F, monthly high 104°F on July 14 and 15, 0.00 inches of precipitation, cooling degree days 1,017 year-to-date against an 882 normal (1991–2020). Modesto Airport (USW00023258) logged 45 days at or above 100°F in 2024 via xmACIS2/ACIS. San Joaquin Valley air basin is federal nonattainment for PM2.5 and state nonattainment for both PM10 and PM2.5 (SJVAPCD). Stanislaus County harvested 217,352 acres of almonds in 2024, its top commodity at $824.2M, with harvest shakers and sweepers running August–October.
- https://forecast.weather.gov/product.php?site=CRH&issuedby=MOD&product=CLM&format=CI&version=1&glossary=0
- https://www.weather.gov/sto/
- https://www.valleyair.org/air-quality-information/ambient-air-quality-standards-valley-attainmnet-status/
- https://www.stanag.org/pdf/cropreport/cropreport2024.pdf
- (100°F day counts queried from ACIS: https://xmacis.rcc-acis.org/ , station MODESTO AP / USW00023258)

**3. A changeout here needs a permit and a HERS test (`permit_rule`)**
City of Modesto Building Safety Division, 1010 Tenth Street, 3rd Floor, issues the mechanical permit; the city's expedited program lets a properly licensed contractor apply for, pay for and obtain an HVAC permit online. Modesto is in California Building Climate Zone 12, and Title 24 requires refrigerant charge verification by an independent HERS rater on air-cooled AC alterations in Climate Zones 2 and 8–15 — so Modesto is inside the range.
- https://www.modestogov.com/2102/Expedited-Permits
- https://www.modestogov.com/1281/Building-Permits
- https://www.calbo.org/sites/main/files/file-attachments/residential_hvac_regulations.pdf?1525201917
- https://www.energy.ca.gov/sites/default/files/2021-03/2019_Chapter%204%20-%20Building%20HVAC%20Requirements_ADA.pdf

## Neighborhoods (6)
College Area, La Loma, Bret Harte, Sherwood Forest, Sylvan, Village One.

## Build output
```
[PASS] modestoacrepairpros.com -- home 3031 words, 4 symptoms, 3 local Q&As, 3 sourced facts
         360 words  /about/
         699 words  /contact/
        3031 words  /
```
symptom_1 282 · symptom_2 290 · symptom_3 290 · symptom_4 279 words (band 200–360).

Full `python3 template/build.py` passes with zero shared 15-word runs against
sacramentoacrepair.com (which was written concurrently and now also PASSes), and
zero against every other written site including the two garage-door references.

## Note for the parent agent (not fixed — template concern, network-wide)
`template/build.py` hardcodes garage-door prose that renders on every non-garage
site: the three work-gallery captions ("Torsion spring replacement", "Sectional
door installation", "Opener and rail repair") and the /contact/ body ("describe
what the door is doing", "a garage door problem is faster to describe out loud",
"If a spring has snapped or the door is off its track"). Left untouched per the
brief's "change nothing else", but it is wrong on this AC site and on all other
non-garage sites in the batch. It does not trip the dup guard because that guard
only shingles copy.md.
