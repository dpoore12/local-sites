# Writer Report — kansascityemergencyplumber.com

## Build result

**PASS.** The focused build and the full batch build both passed on 2026-08-21.

- Home: 2,995 visible words
- About: 367 visible words
- Contact: 634 visible words
- Home includes four 200–360-word symptom cards, three local Q&As, three sourced local facts, and six Kansas City, Missouri neighborhoods.
- Generated and installed `assets/hero.jpg` at 1800px wide and `assets/work-1.jpg` through `assets/work-3.jpg` at 900px wide.

The expected placeholder-phone warning remains unchanged.

## Assigned angle used

The site leads with practical freeze/burst triage rather than generic cold-weather claims: Kansas City’s documented 2021 February lows, where a frozen pipe can open while thawing, and safe containment before a repair starts. The drain-backup material then shifts to older homes with possible cast-iron drain piping and uses a camera/material check rather than assuming every backup is a routine clog. The Missouri/Kansas boundary is treated as an operational fact: this site is explicitly for Kansas City, Missouri, and does not blend KCMO permits with Kansas City, Kansas water service.

## Three sourced local facts

1. **Hard-freeze exposure:** National Weather Service Kansas City records list minimum temperatures of -6°F on February 14, -10°F on February 15, and -13°F on February 16, 2021. This supports the freeze-to-thaw burst-pipe framing.  
   URL: https://www.weather.gov/eax/kcrecnorm-feb

2. **Older drain material:** A Kansas City home-inspection source says cast-iron drain, waste, and vent piping was standard from the 1950s through the early 1980s and documents original lead and cast-iron piping in a 60-year-old Bannister Slopes home. This supports checking material and condition after a recurring backup is cleared.  
   URL: https://bulldoginspect.com/cast-iron-drain-lines-kansas-city-mo-homes/

3. **The state line changes the responsible local system:** Kansas City, Missouri states that permits are needed before most plumbing work; the Board of Public Utilities states that it serves water customers in Kansas City, Kansas. This supports asking for the complete address and not treating the metro as one permitting/water-service jurisdiction.  
   URLs:  
   https://www.kcmo.gov/city-hall/departments/city-planning-development/electrical-plumbing-and-mechanical-permits  
   https://www.bpu.com/forhome/waterservice.aspx

## Source limitation

I did not find a city, county, or utility primary source that establishes a precise residential cast-iron installation era for Kansas City, Missouri. The cast-iron-vintage fact is therefore attributed only to the named local home-inspection source above; the site avoids presenting it as a municipal finding or diagnosing a line solely from a home’s age.

## Shared-template findings

- `template/index.html` hardcodes **“Three steps, one phone call”** and **“The call is the whole process.”** This conflicts with the brief’s instruction to sell the on-site work rather than a phone interaction. The phrase is trade-neutral rather than a garage-door leak, but it frames every service as a call product.
- `template/build.py` hardcodes **“One number, answered by a Kansas City technician”** on the contact page and **“Local [city] technician”** in the hero note even when `tenant.status` is `none`. That is not supportable for an unsigned tenant and can also be the wrong professional noun for non-trades.
- I found no Kansas City copy duplication in the full build and no remaining garage-door wording in this site’s rendered copy.
