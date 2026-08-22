# Writer Report — carrolltongaragedoorrepairexperts.com

## Status
PASS — site-only build and full repository build both passed on 2026-08-21. The home page renders at 2,737 visible words; About renders at 352 words and Contact at 586 words.

## Local angle
Carrollton’s late-1980s housing baseline means many garages may have original-era springs, rollers, tracks, limited headroom, and opener equipment. The page connects that hardware mix with the City’s same-size-door permit distinction and the documented May 28, 2024 straight-line-wind event. It uses storm damage as an inspection reason for tracks, struts, hinges and rollers rather than reusing the 2016 Wylie storm.

## Sourced local facts
1. **Housing age:** The 2020–2024 ACS estimate lists Carrollton’s median year structure built as 1988. Sources: https://www.point2homes.com/US/Neighborhood/TX/Carrollton-Demographics.html and https://data.census.gov/table/ACSDT5Y2024.B25035?g=160XX00US4813000
2. **Permit rule:** Carrollton says same-size replacement doors or windows do not require a permit; changing the size of an opening does. Source: https://www.cityofcarrollton.com/departments/departments-a-f/building-inspection/my-home/remodels-additions
3. **Dated storm condition:** The City reports that its May 28, 2024 storm produced 80–95 mph straight-line winds and affected all 37.1 square miles of Carrollton. Source: https://www.cityofcarrollton.com/Home/Components/News/News/4848/27

Neighborhood names used: Castle Hills, Country Place, Indian Creek, Josey Ranch, Oak Creek Estates, and Rosemeade. Directory source: https://www.viprealestate.com/carrollton-neighborhood-directory.php

## Shared-template issue
`template/index.html` still hardcodes the steps-band lines “How it works,” “Three steps, one phone call,” and “There is nothing to fill in and nothing to buy. The call is the whole process.” This is a template leak: it is not authored in `copy.md`, and “the call is the whole process” conflicts with the brief’s requirement to sell the on-site work rather than a phone interaction. The same template also hardcodes the work-band eyebrow/head/caption sentence. Those should be supplied by copy blocks so different niches do not inherit process language.

## Limits / unsourced items
No Carrollton-specific NWS event-summary page that directly tied hail size to a Carrollton address was used. The page relies on the City’s documented May 28, 2024 80–95 mph straight-line-wind event for the dated local storm condition. No license, business identity, reviews, operating hours, prices, or business-age claims were added because there is no signed tenant.


## From research_carrollton_local_facts.md

# Carrollton research notes — 2026-08-21

1. Housing age: Point2Homes reports Carrollton median year built 1988, based on Census data. Census table link: https://data.census.gov/table/ACSDT5Y2024.B25035?g=160XX00US4813000
2. Permit: City of Carrollton says same-size door/window replacement does not require a permit; changing the opening does. https://www.cityofcarrollton.com/departments/departments-a-f/building-inspection/my-home/remodels-additions
3. Weather: City reports May 28, 2024 straight-line winds of 80–95 mph, affecting all 37.1 square miles of Carrollton. https://www.cityofcarrollton.com/Home/Components/News/News/4848/27
4. Neighborhood names: Castle Hills, Country Place, Indian Creek, Josey Ranch, Oak Creek Estates, and Rosemeade appear in this local directory: https://www.viprealestate.com/carrollton-neighborhood-directory.php
