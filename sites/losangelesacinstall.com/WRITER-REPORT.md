## From research-and-validation.md

# Los Angeles AC Installation — Research and validation

Prepared: 2026-08-22

## Local facts used

1. **LADWP rebate records and final permit:** LADWP’s residential Consumer Rebate Program requires an active LADWP electric meter, application after purchase and installation, and supporting records including a paid itemized invoice, matching AHRI certificate, and final approved Building and Safety permit. It may inspect and verify the work. Source: https://www.ladwp.com/residential-services/assistance-programs/consumer-rebate-program

2. **HVAC permit and California verification:** LADBS requires a mechanical HVAC permit for any installation or modification of heating/cooling systems. The California Energy Commission says Energy Code field verification and diagnostic testing now reside in the Energy Code compliance program; depending on scope, HERS testing may be mandatory and properly permitted work triggers necessary testing. Sources: https://dbs.lacity.gov/services/plan-review-permitting/mechanical-hvac-permits and https://www.energy.ca.gov/programs-and-topics/programs/home-energy-rating-system-hers-program

3. **Coastal-to-Valley sizing condition:** California Energy Commission climate material lists Los Angeles Airport in Climate Zone 6 and Burbank in Climate Zone 9, and requires official hourly weather data adapted to local design conditions for compliance calculations. Sources: https://efiling.energy.ca.gov/GetDocument.aspx?tn=202693 and https://www.energy.ca.gov/programs-and-topics/programs/building-energy-efficiency-standards/climate-zone-tool-maps-and

## Neighborhoods

Highland Park; Echo Park; Silver Lake; Koreatown; West Adams; Sherman Oaks.

## Images

Generated with domain-prefixed temporary names, then converted as progressive JPEGs at quality 80:

- assets/hero.jpg — 1800 × 1013
- assets/work-1.jpg — 900 × 507
- assets/work-2.jpg — 900 × 507
- assets/work-3.jpg — 900 × 507

## Validation

`python3 template/build.py losangelesacinstall.com` passed with zero errors:

- `/` — 2,933 words
- `/about/` — 329 words
- `/contact/` — 595 words

The subsequent full `python3 template/build.py` run passed this site, but exited nonzero for unrelated sites only:

- waterdamageaustinco.com — unverifiable pre-tenant claim “thousands of”
- westcovinacaraccidentlawyerpros.com — shares 13 fifteen-word runs with oxnardcaraccidentlawyerpros.com

No files outside `sites/losangelesacinstall.com/` were changed to address those failures.
