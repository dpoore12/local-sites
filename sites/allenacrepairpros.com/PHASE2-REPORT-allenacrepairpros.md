# Phase 2 complete — allenacrepairpros.com

Build check: `python3 template/build.py --check-only allenacrepairpros.com` → **[PASS]**, exit 0.

## Page word counts (rendered visible)
| Page | Words |
|---|---|
| / (home) | 1755 |
| /pricing/ | 1749 |
| /air-conditioner-repair/ | 1287 |
| /ac-compressor-repair/ | 1274 |
| /ac-refrigerant-leak-repair/ | 1300 |
| /ac-tune-up/ | 1222 |
| /services/ | 665 |
| /contact/ | 541 |
| /about/ | 330 |

Also: 4 symptom blocks (40–80 words each), 3 local Q&As, 3 sourced facts, `services_summary` 114 words, `services_pick_head` 8, `crosslink_head` 4, four `svc_*_lede` 39–42, four `svc_*_body` 738–809.

## Service slugs
1. `air-conditioner-repair`
2. `ac-compressor-repair`
3. `ac-refrigerant-leak-repair`
4. `ac-tune-up`

## Strongest verified local facts
1. **Allen housing age from the city's own 2045 Comprehensive Plan** — roughly one-third of the housing stock built 2000–2009, citywide median home age 23 years (ACS 2022), 46% of existing housing over 25 years old as of 2025, tract medians 12–46 years: https://publicrecords.cityofallen.org/WebLink/DocView.aspx?id=994503&dbid=0&repo=Allen
2. **EPA HFC technology transitions** — 700 GWP limit for residential AC/heat pumps effective January 1, 2025, with components used to repair existing systems exempt from the installation restrictions: https://www.epa.gov/hfcs/technology-transitions-hfc-restrictions-sector ; R-454B listed at GWP 470, ASHRAE A2L, acceptable with use conditions: https://www.epa.gov/snap/substitutes-residential-and-light-commercial-air-conditioning-and-heat-pumps
3. **NWS Fort Worth climate data** — normal 20.2 days/year at or above 100°F and 2,825 annual cooling degree days (https://www.weather.gov/fwd/dfw_records_normals), against 55 triple-digit days in 2023 vs 7 in 2025 (https://www.weather.gov/fwd/d100data)

Supporting: City of Allen $175 complete HVAC system permit, $50 annual contractor registration, inspections printed on the permit (https://www.cityofallen.org/1939/Contractor-and-Commercial-Services); Allen adopted 2021 IMC/IRC (https://cms3.revize.com/revize/allentx/Images/Documents/Departments/Community%20Development/Building%20and%20Permitting/Adopted%20Codes/Adopted%20Building%20Codes.pdf); TDLR ACR licensing structure, TACL number classes/endorsements and the unenforceable-contract rule (https://www.tdlr.texas.gov/media/pdf/ACR%20at%20a%20Glance.pdf); ERCOT all-time peak 91,089 MW on July 22, 2026 (https://www.ercot.com/static-assets/data/news/content/a-peak-demand/all-time-records.htm).

Census ACS B25035 could not be fetched directly (API key / JS-gated); Allen's own comprehensive-plan housing-age figures were used instead.

## Files changed
- `sites/allenacrepairpros.com/copy.md` (phase-2 blocks added; symptom blocks rewritten to 40–80 words; `pricing_body` prose trimmed to clear the 1750-word ceiling — no numbers removed)
- `sites/allenacrepairpros.com/site.json` (`"phase": 1` → `2` only)

Working draft moved out of the site folder to `/tmp/draft.md`.

## Collision handling
One 15-word overlap with modestoacrepairpros.com surfaced on the tune-up exclusions sentence and was rewritten; the final run reports zero shingle collisions across all 82 other sites. Texas expansive clay and Texas Occupations Code angles were avoided per brief.
