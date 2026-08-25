# arvadaemergencyplumber.com — Phase 2 conversion report

## Build status

```
[PASS] arvadaemergencyplumber.com -- home 1647 words, 4 symptoms, 3 local Q&As, 3 sourced facts
```
`python3 template/build.py --check-only arvadaemergencyplumber.com` → exit code 0.
`"phase": 2` set in `sites/arvadaemergencyplumber.com/site.json`.

## Per-page word counts (rendered)

| Page | Words |
|---|---|
| `/` | 1902 |
| `/pricing/` | 1647 |
| `/burst-pipe-repair/` | 1366 |
| `/emergency-plumbing-repair/` | 1363 |
| `/sewer-line-repair/` | 1315 |
| `/drain-cleaning/` | 1301 |
| `/contact/` | 601 |
| `/services/` | 573 |
| `/about/` | 348 |

Pricing came in at 1647 against the 1750 ceiling after six prose trims. Every dollar figure and fee was retained: $55, $34, $67, $20.50, $125 in `pricing_body`, plus all figures already in site.json facts.

## Collision check

Zero shared 15-word runs with any of the eight named siblings (San Jose, Tucson, Jacksonville, Kansas City, Phoenix, Denver furnace, Colorado Springs furnace, Denver divorce) and no duplicate-shingle error against the full 82-site network. Two Kansas City overlaps in the drain-cleaning body were found and rewritten.

## QC

`python3 qc.py arvadaemergencyplumber.com` returns no HIGH findings. Remaining items are dictionary gaps on real trade/legal terms (geotechnical, plat, sillcock, licensure, callout, timestamp) and one LOW flow flag on the pricing page's sourced-facts list, which is a citation list rather than prose.

## Three strongest verified local facts

1. **The homeowner owns the sewer service all the way to the city main, and Arvada will give a free second opinion on your camera footage.** The city states that care and maintenance of the sanitary sewer service is the homeowner's from the house up to and including the connection at the city main, that the city does not cut, clean or televise it, and that the Wastewater Division will review a homeowner's televised inspection by appointment — [City of Arvada Sewer Information](https://www.arvadaco.gov/439/Sewer-Information). Water runs the opposite way: city-owned main to meter pit, homeowner meter pit to foundation — [Arvada Service Line Inventory & Replacement Program](https://www.arvadaco.gov/647/Service-Line-Inventory-Replacement-Progr).
2. **Colorado licenses plumbers at the state level, with a three-apprentice supervision cap and a five-minute supervision rule.** The State Plumbing Board inside DORA licenses plumbers, apprentices and contractors statewide and does not regulate pipe fitters, drain cleaners or gas pipe installers — [DORA State Plumbing Board](https://dpo.colorado.gov/Plumbing). License classes and the definition of "plumbing" (inside the building or within five feet of the foundation, excluding the service line from the first joint to the property line) are in [C.R.S. 12-155-103](https://law.justia.com/codes/colorado/title-12/business-professions-and-occupations/article-155/section-12-155-103/); the three-apprentice cap is [C.R.S. 12-155-124](https://codes.findlaw.com/co/title-12-professions-and-occupations/co-rev-st-sect-12-155-124/); direct supervision as present at the permitted address or within five minutes, plus the 2021 IPC/IRC basis and the expansion-tank support rule, are in [3 CCR 720-1.2](https://www.law.cornell.edu/regulations/colorado/3-CCR-720-1.2). Arvada's Building Division verifies those credentials and can refer violations to the board — [Arvada policy on review of plumbing licenses](https://www.arvadaco.gov/1242/Policy-on-Review-of-Plumbing-Licenses).
3. **Freeze bursts happen away from the ice plug, and the local cold is more than sufficient to cause them.** Code-body guidance built on Building Research Council research at the University of Illinois states that the break does not typically occur at the blockage, that pressure builds in the confined column between the plug and a closed faucet, and that pipe in unconditioned space began icing at roughly 20°F — [ICC freeze/burst pipe report](https://www.iccsafe.org/wp-content/uploads/DIS-FreezeBurstPipe.pdf). NWS Denver/Boulder records an area low of −29°F on January 9, 1875, thirty occurrences of −20°F or colder since 1872, and −24°F on December 22, 2022 — [NWS Boulder low temperature extremes](https://www.weather.gov/bou/lowtempextremes); January normal lows of 18–19°F — [NWS Boulder January climate records](https://www.weather.gov/bou/Climate_Record_January).

## Things in the brief that did not hold up

1. **There is no single "Colorado Plumbing Code edition currently adopted statewide" that matches Arvada.** Three official pages cite three different editions: the state board rule (3 CCR 720-1) is built on **2021** IPC/IRC language and expressly excludes later editions; the **City of Arvada** adopted the **2024 IPC** as part of a code package effective **March 24, 2026**, replacing the 2018 set in force since October 2020 ([Arvada adopted building codes](https://www.arvadaco.gov/165/Adopted-building-codes-and-design-criter)); and the city's own plumbing-license policy page still references the **2015 IPC**. The copy states the state basis and the city adoption separately rather than pretending there is one number.
2. **NWS Boulder does not publish an Arvada-specific record low.** The −29°F record is the Denver-area record from the Denver/Boulder office. The copy attributes it as an area record, not a city record.
3. **The existing `pricing_body` reinspection fee of $77 was stale.** The current published [Arvada building fee schedule](https://www.arvadaco.gov/1263/Building-Fee-Schedule) lists reinspection at **$125**; the figure was corrected upward, with no fee removed.
4. **No verifiable build-era source exists for Allendale or Leyden Rock.** Those two site.json neighborhoods are named in existing copy but were deliberately not given a founding date or housing-era claim. Verified era anchors used instead: Stocke Addition platted 1904 and Walter subdivision 1920 ([Arvada historic neighborhoods](https://www.arvadaco.gov/425/Historic-Neighborhoods)) and Candelas home sales opening in 2012 (site.json).
5. **No site.json / brief conflict on the authority fields.** City, state, county and the four service slugs matched, so site.json's slugs were used as given and nothing had to be overridden.

Full research notes with every URL: `arvada-phase2-research.md`.
