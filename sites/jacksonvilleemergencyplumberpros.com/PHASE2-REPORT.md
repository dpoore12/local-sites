# Phase 2 report — jacksonvilleemergencyplumberpros.com

Build: `python3 template/build.py --check-only jacksonvilleemergencyplumberpros.com` → **[PASS], exit 0**

## Page word counts (rendered visible words)
| Page | Words |
|---|---|
| / (home) | 1806 |
| /emergency-plumbing-repair/ | 1501 |
| /burst-pipe-repair/ | 1403 |
| /drain-cleaning/ | 1504 |
| /sewer-line-repair/ | 1543 |
| /pricing/ | 1747 |
| /services/ | 559 |
| /about/ | 355 |
| /contact/ | 556 |

## Service slugs (from site.json, unchanged)
1. emergency-plumbing-repair
2. burst-pipe-repair
3. drain-cleaning
4. sewer-line-repair

## Files changed
- `sites/jacksonvilleemergencyplumberpros.com/copy.md` (rewritten: symptom teasers trimmed to 40–80 w, added services_summary / services_pick_head / crosslink_head, added 8 svc_* blocks, added SOURCES block, trimmed pricing_body prose only)
- `sites/jacksonvilleemergencyplumberpros.com/site.json` — `"phase": 1` → `2` only (verified by git diff)

Research notes: `/home/user/workspace/jacksonville-plumbing-research-notes.md`

## Strongest verified local facts
1. JEA states the property owner owns the water service line from the JEA meter box, usually located at the property line, to the plumbing inside the structure — the ownership boundary is a physical object in the yard. https://www.jea.com/about/water_supply/water_service_line_verification_project/
2. The water table sits within 5 feet of land surface across most of Duval County and swings as much as 5 feet seasonally (USGS); soil survey descriptions used in Army Corps permitting put Leon fine sand's high water table at 6–18 inches January through October and Lynn Haven fine sand at or near the surface. https://fl.water.usgs.gov/PDF_files/wri93_4130_phelps.pdf and https://www.saj.usace.army.mil/Missions/Regulatory/Public-Notices/Article/1964031/saj-2019-03371-sp-mre/
3. September 3–14, 2024 rainfall of 10–15 inches (upwards of 20 in places) drove flow into JEA's wastewater system 58% above its 80-million-gallon daily average and produced twelve sanitary sewer overflows. https://jaxtoday.org/2024/09/18/12-sewer-backups-due-to-heavy-rain-this-month-that-overwhelmed-jeas-system/

Also verified and used: Duval County permit exemptions (leak stopping, faucet after the stop excluding water heaters, stoppage clearing that does not replace or rearrange pipe), Jacksonville Code §320.408 ($5,000 repipe threshold, double fee for unpermitted starts), FBC 8th Edition (2023) in force since December 31, 2023, Fla. Stat. 489.105(3) plumbing contractor scope, FPC 708 cleanout intervals, FPC 714 backwater valve elevation rule, FPC 305.1.1 termite sleeve, FPC 305.4 12-inch cover, FPC 307.5 footing bearing plane, EPA hydrogen sulfide corrosion mechanism, HUD DWV "age alone is not indicative", JEA what-not-to-flush / fatbergs, septic phase-out counts (~43,000 Duval; ~65,000 across JEA areas; ~22,000 parcels into 35 areas; 70% threshold; DEP took over OSTDS July 1, 2021), NWS 53.40-inch annual normal, and neighborhood build eras for Riverside, Avondale, Springfield, San Marco, Arlington and Mandarin.

## Notes
- No median-year-built figure is claimed anywhere: Census API/table access failed, so the copy treats pipe material as something a camera establishes rather than asserting cast iron was standard.
- Fla. Stat. 559.905 is not referenced.
- Cross-site duplicate guard: three 15-word runs originally overlapped tucsonemergencyplumberpros.com (one sentence about camera assessment); rewritten, now zero overlaps with all 82 sites.
