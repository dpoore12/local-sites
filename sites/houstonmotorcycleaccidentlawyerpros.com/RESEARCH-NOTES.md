# Houston Motorcycle Accident Lawyer — research notes and verification

Written 2026-08-21. Pre-tenant legal site: no firm, no attorney, no case result,
no settlement figure, no win record, no bar credential anywhere in the copy.

## The three sourced local facts (in site.json local_facts)

1. **Harris County leads Texas in motorcycle-versus-vehicle crashes.** TxDOT's
   Crash Records Information System (CRIS), queried 2025-04-17 for the state's
   FY2026 highway safety grant application, ranks Harris County first in Texas
   for crashes involving a motorcycle and another motor vehicle in 2024: 908.
   Dallas 438, Bexar 433, Tarrant 402, Montgomery 139, Galveston 95,
   Fort Bend 74.
   Source: https://egrants.bts.txdot.gov/eGrantsHelp/Reports/FY26AGA.pdf
   (page 237-equivalent motorcycle safety program area table; the FY2025 edition
   of the same table shows Harris 826 for 2022, Dallas 405, Fort Bend 59:
   https://egrants.bts.txdot.gov/eGrantsHelp/Reports/FY25AGA.pdf)
   This is the Houston/Harris-County-specific fact.

2. **Two-year limitations period.** Texas Civil Practice and Remedies Code
   16.003(a): suit for personal injury not later than two years after the day
   the cause of action accrues; 16.003(b): two years for injury resulting in
   death, accruing on the death of the injured person.
   Source: https://statutes.capitol.texas.gov/Docs/CP/htm/CP.16.htm
   (verbatim text confirmed via the site's DocViewer render of CP.16)

3. **Proportionate responsibility and the 51% bar.** CPRC 33.001: a claimant
   may not recover damages if their percentage of responsibility is greater
   than 50 percent. CPRC 33.012(a): if not barred, the court reduces damages by
   a percentage equal to the claimant's percentage of responsibility.
   Sources: https://statutes.capitol.texas.gov/Docs/CP/htm/CP.33.htm
            https://statutes.capitol.texas.gov/Docs/TN/htm/TN.661.htm
   Transportation Code 661.003(c) is carried in the same fact: the helmet
   requirement has an exception for riders at least 21 who completed a
   Chapter 662 operator training and safety course or are covered by a health
   insurance plan for motorcycle crash injuries, and 661.003(c-1) bars a stop
   made solely to check that. Text cross-checked verbatim at
   https://texas.public.law/statutes/tex._transp._code_section_661.003

## Other facts used in the copy, each verified

- Transportation Code 545.152: an operator turning left must yield to a vehicle
  approaching from the opposite direction that is close enough to be an
  immediate hazard. Verified verbatim:
  https://codes.findlaw.com/tx/transportation-code/transp-sect-545-152/
- Transportation Code 545.060(a): stay as nearly as practical within a single
  lane; do not leave the lane unless the movement can be made safely. Verified:
  https://law.justia.com/codes/texas/transportation-code/title-7/subtitle-c/chapter-545/subchapter-b/section-545-060/
- Texas minimum auto liability 30/60/25; carriers must offer uninsured/
  underinsured motorist coverage and PIP, and a customer must decline either in
  writing. Texas Department of Insurance:
  https://www.tdi.texas.gov/pubs/consumer/cb020.html
- 24 civil district courts, Harris County Civil Courthouse, 201 Caroline,
  Houston 77002. Harris County District Courts: https://www.justex.net/courts/civil/
- Statewide context (not used as a numbered fact): 557 motorcyclist deaths and
  2,468 serious injuries in Texas in 2025; 37% of motorcycle fatalities occur at
  an intersection. https://www.txdot.gov/safety/traffic-safety-campaigns/motorcycle-safety.html

## Neighborhoods (6, real Houston super neighborhoods)

The Heights, Montrose, East End, Gulfton, Sharpstown, Spring Branch.

## Photos

- hero.jpg (1800px) — Houston freeway interchange with elevated flyovers and a
  one-way feeder road, humid late-afternoon light, one motorcycle in traffic.
- work-1.jpg (900px) — crashed street bike in a fenced impound yard, scraped
  fairing, bent fork, gouged footpeg.
- work-2.jpg (900px) — downtown Houston county civil courthouse exterior,
  limestone and glass, live oaks, faces turned away.
- work-3.jpg (900px) — desk detail: official form paperwork with unreadable
  lettering, notebook, pen, motorcycle key, riding gloves.
No text, logos or brand names in any image. No gavels, no scales, no lawyer
portraits.

## Build

    python3 template/build.py houstonmotorcycleaccidentlawyerpros.com  -> PASS
    python3 template/build.py                                         -> PASS (12 written sites, 0 FAIL)

Home 2,859 visible words; /about/ 354; /contact/ 606. Phase-1 symptom cards run
267-296 words each. The only warning is the expected PLACEHOLDER phone.

## One template-level note for the parent agent (not fixed here)

`template/build.py` still hardcodes garage-door language that renders on every
non-garage site: the /contact/ body ("describe what the door is doing", "a
garage door problem is faster to describe out loud", "If a spring has snapped or
the door is off its track"), the three gallery captions ("Torsion spring
replacement", "Sectional door installation", "Opener and rail repair"), and
`hero_note`/`disclosure` calling the reader's contact a "technician". On this
legal site that reads badly and, in the disclosure, inaccurately. build.py is
not in template/LOCKED.md's frozen list, but it is shared by every site being
written in parallel, so I left it alone rather than editing it mid-batch. It
needs one central fix — most cleanly by moving those strings into copy.md
blocks.
