## From WRITER-NOTES-orlando-moving.md

# orlandomovingcompanypros.com — phase 1 delivery notes

Written 2026-08-21. Status: pre-tenant, phone still PLACEHOLDER (321) 555-0100.

## The three sourced local facts (in site.json `local_facts`)

1. **Florida mover registration (Chapter 507 / FDACS).** Every mover doing an
   intrastate household move must register with the Florida Department of
   Agriculture and Consumer Services before operating or advertising. The
   registration number must appear on each estimate and contract, in
   advertising, and on a sign on the driver's-side door of the truck in
   lettering at least 1.5 inches tall. Unregistered operation draws an immediate
   cease and desist order plus a civil penalty of up to $5,000. Withholding
   delivery of goods after the shipper has paid what the estimate states is a
   listed prohibited practice (s. 507.07(5)).
   - https://www.fdacs.gov/Business-Services/Moving-Companies
   - https://www.flsenate.gov/Laws/Statutes/2024/507.03
   - https://www.flsenate.gov/Laws/Statutes/2024/507.07

2. **Orange County growth.** 1,528,002 residents as of July 1, 2025, up 6.9%
   from the 1,429,910 counted in the 2020 census. The Orlando Economic
   Partnership reports the region added 37,690 residents in the year ending
   July 1, 2025, sixth fastest among large U.S. regions.
   - https://www.census.gov/quickfacts/fact/table/orangecountyflorida/PST045225
   - https://news.orlando.org/blog/orlando-population-growth-again-among-highest-in-nation/

3. **Rental and multifamily mix (Orange County specific).** Owner-occupied rate
   56.8% (2020–2024), so roughly 43–44% of occupied homes are rented. Orange
   County's own fair-housing analysis counts 209,073 renter-occupied of 444,543
   occupied units (~44%) and puts apartment complexes at about 28% of the
   housing stock against 56.5% single-family detached. This is what drives the
   certificate-of-insurance / reserved-elevator / gate-access reality of
   Orlando apartment and condo moves.
   - https://www.census.gov/quickfacts/fact/table/orangecountyflorida/PST045225
   - https://www.orangecountyfl.net/Portals/0/resource%20library/neighbors%20-%20housing/2016-2020%20Orange%20County%20Analysis%20of%20Impediments%20to%20Fair%20Housing%20Choice.pdf

Also used in copy (named in prose, not a facts entry): National Hurricane Center
Atlantic season June 1 – November 30, most activity mid-August to mid-October,
statistical peak September 10 — https://www.nhc.noaa.gov/climo/

## Neighborhoods (all confirmed on City of Orlando neighborhood maps)

College Park, Baldwin Park, Thornton Park, Audubon Park, Lake Nona, MetroWest
(https://www.orlando.gov/Our-Government/Records-and-Documents/Map-Library/Neighborhood-Maps)

## Tone note

Moving is scheduled work, not an emergency. Nothing in the copy frames the
reader as panicking; the value is a booked date, a crew sized to the access at
both addresses, and a written estimate carrying the state registration number
before load day. `emergency_note` is a plain practical line about what a truck
cannot legally carry (propane, fuel, paint, solvents, pool chemicals, aerosols,
ammunition primers) rather than an invented hazard.

## Build

- `python3 template/build.py orlandomovingcompanypros.com` → PASS,
  home 3,035 words / about 355 / contact 616. Only warning is the expected
  PLACEHOLDER phone.
- `python3 template/build.py` (all sites) → exit 0, no cross-site 15-word runs.

## Images

hero.jpg 1800px (Orlando stucco/barrel-tile house, palms, unmarked white box
truck with ramp down), work-1.jpg (dresser being padded and stretch-wrapped),
work-2.jpg (loaded truck interior, ratchet straps), work-3.jpg (cartons staged
in an apartment hallway with padded doorframe and floor runner). No text, logos
or brand names; no faces.
