# tampacriminaldefenselawyerpros.com — phase 1 writer report

Written 2026-08-21. Pre-tenant. No firm name, no attorney name, no case result,
no bar credential, no fee, no outcome prediction anywhere on the site.

## Three sourced local facts (in site.json `local_facts`)

1. **A judge is supposed to see an arrested person within 24 hours** —
   Florida Rule of Criminal Procedure 3.130 requires every arrested person not
   already lawfully released to be taken before a judicial officer within 24
   hours of arrest, in person or by electronic audiovisual device; the judge
   states the charge, provides the complaint, and advises of the right to remain
   silent and to counsel. Rule 3.133 sets a separate 48-hour limit for a
   nonadversary probable cause determination in custody. Rule 3.130(c)(2)
   requires reasonable time to send for retained counsel and an officer-carried
   message to a named lawyer inside the county at no cost.
   Source: https://www.flcourts.gov/content/download/217910/file/Florida-Rules-of-Criminal-Procedure.pdf

2. **The 2026 Hillsborough bond schedule binds the booking officer, not the
   judge** (Hillsborough/Tampa specific, dated) — Thirteenth Judicial Circuit
   Administrative Order S-2025-063 adopts the statewide uniform bond schedule
   for Hillsborough County without change, effective January 1 – December 31,
   2026, states it applies only to the booking officer, and excludes capital,
   life, first- and second-degree felonies, homicide, felony battery, domestic
   battery by strangulation, domestic violence under Fla. Stat. 741.28,
   stalking, robbery, burglary, carjacking, kidnapping, controlled-substance
   trafficking, injunction violations, anyone on probation/community
   control/pretrial release at the time of a felony arrest, and anyone with
   three or more arrests in the preceding six months. Those arrestees get an
   individualized determination by a judge under Fla. Stat. 903.011(6), 903.046
   and Rule 3.131.
   Source: https://www.fljud13.org/Portals/0/AO/DOCS/S-2025-063.pdf

3. **The arraignment date is mailed to the address you gave at arrest**
   (Hillsborough specific) — The Hillsborough County Clerk of Court states that
   after a felony arrest the jail sends initial paperwork to the Clerk's felony
   department, which builds the official court file (arrest document plus any
   release forms) and forwards it to the Office of the State Attorney, which
   decides whether to file formal charges. Once charges are filed the defendant
   is notified by mail of an arraignment date at the address provided at arrest,
   and the bail bond agent is notified if the defendant bonded out. The felony
   department cannot change a court date after notice.
   Source: https://www.hillsclerk.com/court-services/circuit-criminal

Supporting statute cited in copy (Q&A 3 and factor_1): Florida Statutes 775.15
limitation periods — 4 years first-degree felony, 3 years other felonies,
2 years first-degree misdemeanor, 1 year second-degree misdemeanor, clock starts
the day after the offense. https://www.flsenate.gov/laws/statutes/2025/775.15

## Neighborhoods

Ybor City, Seminole Heights, Hyde Park, Tampa Heights, Davis Islands, Palma Ceia

## Build output

    python3 template/build.py tampacriminaldefenselawyerpros.com   -> exit 0
    [WARN] phone (813) 555-0100 is a PLACEHOLDER  (expected)
    [PASS] home 3088 words, 4 symptoms, 3 local Q&As, 3 sourced facts
             405 words  /about/
             663 words  /contact/
            3088 words  /

    python3 template/build.py (all sites)  -> exit 0, no shared 15-word runs

## Photos

hero.jpg (1800px, Tampa county courthouse exterior with palms and plaza),
work-1.jpg (900px, documents/legal pad/desk detail), work-2.jpg (900px, empty
consultation room), work-3.jpg (900px, wet brick Ybor-style Tampa street at
dawn). No gavels, scales, handcuffs, lawyer portraits, arrests, text or logos.
