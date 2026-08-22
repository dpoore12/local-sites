# Writer Report — friscogaragedoorrepairexperts.com

## Status

PASS — `python3 template/build.py friscogaragedoorrepairexperts.com` passed with the expected placeholder-phone warning.

The home page renders at 2,609 visible words. The supporting pages render at 373 words (`/about/`) and 514 words (`/contact/`). The full `python3 template/build.py` run also passed on August 21, 2026.

## Sourced Frisco facts used

1. **New single-family housing, not McKinney-style post-1990 stock.** Frisco's 2023 comprehensive-plan appendix reports 58,574 single-family units: 39.6% built in 2000–2009, 31.2% in 2010–2019, and 11.4% in 2020 or later. This supports the framing that many garage doors are still original builder installations now approaching their first substantial mechanical repairs.
   - https://www.friscotexas.gov/DocumentCenter/View/36063/2040-Comp-Plan-Appendices-PDF

2. **Exterior replacement is both a permit and association question.** Frisco's residential permit page includes replacement doors in its self-service permit categories. The City's neighborhood page says Frisco has more than 200 HOAs. The copy distinguishes hidden mechanical repair from visible panel or full-door changes that can require a homeowner to check the local process and governing documents.
   - https://www.friscotexas.gov/1696/Residential-Permits
   - https://www.friscotexas.gov/977/Neighborhoods

3. **Documented local severe weather.** NWS Fort Worth's April 3, 2014 severe-outbreak page records trained-spotter hail reports up to two inches in Frisco. The site uses this only to support a post-storm check of the door's moving system, not a blanket damage claim.
   - https://www.weather.gov/fwd/storms040314

## Assigned angle

This site uses Frisco's extreme newer-home buildout, original builder-grade hardware nearing normal cycle wear, and the city’s unusually large HOA footprint. It treats a garage door as both a moving mechanical system and a front-elevation component in a subdivision. That avoids the McKinney site's post-1990 stock, historic-overlay certificate, and 2016 Wylie-storm framing.

## Shared-template / scaffold finding

No visible phase-1 template wording leak was found. The inherited `site.json` service objects still contain **Naperville** phrases in their future service-page `keyword` fields. Phase 1 does not render or link to those services, and the brief instructed writers not to change anything else in `site.json`, so this was left unchanged. It should be corrected before this site moves to phase 2.

## Sourcing limitations

I could source Frisco's more-than-200 HOA count, but not a citywide rule saying every garage-door exterior change requires architectural approval. The site therefore tells homeowners to check their own association documents for a visible replacement rather than making that broader claim.

## Assets

Created `assets/hero.jpg` at 1800 pixels wide and `assets/work-1.jpg`, `assets/work-2.jpg`, and `assets/work-3.jpg` at 900 pixels wide, all progressive JPEGs at quality 80.
