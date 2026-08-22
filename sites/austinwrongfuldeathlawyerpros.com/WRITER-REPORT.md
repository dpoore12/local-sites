## From build-results.md

# Austin wrongful-death site validation

Validated 2026-08-22.

## Site build

`python3 template/build.py austinwrongfuldeathlawyerpros.com` passed with zero errors.

- `/` — 2,643 words
- `/about/` — 317 words
- `/contact/` — 562 words

The home page has four substantive symptom blocks (259, 269, 269, and 283 words), three local Q&As, and three sourced local facts.

## Local facts used

1. Texas Civil Practice and Remedies Code § 71.021 preserves a personal-injury cause of action after the injured person’s death for the heirs, legal representatives, and estate.  
   https://statutes.capitol.texas.gov/StatutesByDate.aspx?code=CP&level=SE&value=71.021&date=3/12/2015

2. Travis County lists Civil and Family Courts at 1700 Guadalupe Street in Austin; the District Civil Courts have original jurisdiction over civil matters involving damages of $200 or more, and the District Clerk states that attorneys must e-file civil documents.  
   https://www.traviscountytx.gov/courts/civil/district  
   https://www.traviscountytx.gov/district-clerk/civil-division

3. TxDOT’s 2024 *Crashes and Injuries by County* table records 139 fatal crashes and 155 traffic fatalities in Travis County.  
   https://www.txdot.gov/content/dam/docs/division/trf/crash-records/2024/13.pdf

## Full build

The required full `python3 template/build.py` run was also completed. The Austin site passed. The full repository command exited nonzero only because unrelated sites already had missing-block or shared-copy errors; none named this Austin site.


## From research-notes.md

# Austin wrongful-death site research notes

Verified 2026-08-22 for phase-1 copy and `site.json`.

1. **Texas survival action** — Texas Civil Practice and Remedies Code § 71.021 says a personal-injury cause of action does not abate because of the injured person’s death and survives to the heirs, legal representatives, and estate. It supports explaining the distinction between a survival action and a wrongful-death claim without repeating the Dallas site’s § 71.004 standing angle.  
   https://statutes.capitol.texas.gov/StatutesByDate.aspx?code=CP&level=SE&value=71.021&date=3/12/2015

2. **Travis County civil-court structure** — Travis County lists its Civil and Family Courts at 1700 Guadalupe Street, Austin. Its District Civil Courts have original jurisdiction in civil matters involving damages of $200 or more; the District Clerk states that attorneys must e-file civil documents.  
   https://www.traviscountytx.gov/courts/civil/district  
   https://www.traviscountytx.gov/district-clerk/civil-division

3. **Travis County traffic deaths** — TxDOT’s 2024 *Crashes and Injuries by County* table reports 139 fatal crashes and 155 fatalities in Travis County.  
   https://www.txdot.gov/content/dam/docs/division/trf/crash-records/2024/13.pdf

Neighborhoods used: Hyde Park, Mueller, East Cesar Chavez, Clarksville, Zilker, Bouldin Creek. City of Austin neighborhood materials confirm these local area names.  
https://www.austintexas.gov/planning/neighborhood-plans-and-resources
