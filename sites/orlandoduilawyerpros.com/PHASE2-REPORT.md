# orlandoduilawyerpros.com — phase 2 writer report

## Build status

`python3 template/build.py --check-only orlandoduilawyerpros.com` → exit 0

```
[PASS] orlandoduilawyerpros.com -- home 1749 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           372 words  /about/
           600 words  /contact/
          1493 words  /dui-breath-test-defense/
          1458 words  /dui-license-suspension/
          1477 words  /felony-dui-defense/
          1468 words  /first-offense-dui-defense/
          1797 words  /
          1749 words  /pricing/
           575 words  /services/
```

`site.json` → `"phase": 2`.

## Service slugs

1. first-offense-dui-defense
2. dui-license-suspension
3. dui-breath-test-defense
4. felony-dui-defense

## Strongest verified local facts

- Orange County Booking and Release Center handles booking, first appearance and release in one 592-bed facility with three public-gallery courtrooms; first appearance runs weekdays at 9 a.m. or 1 p.m., posted at 4:30 a.m., with a single 11 a.m. session on weekends and court holidays — https://netapps.ocfl.net/BestJail/Home/Facilities and https://netapps.ocfl.net/BestJail/Home/FirstAppearance
- Bureau of Administrative Reviews for this metro is at 4101 Clarcona-Ocoee Road, Suite 152, Orlando 32810, weekdays 8–5, and the formal review / hardship forms can be completed and emailed without visiting the office — the pivotal detail for out-of-state defendants inside the 10-day window of Fla. Stat. 322.2615 — https://www.flhsmv.gov/locations/orange/ and https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0300-0399/0322/Sections/0322.2615.html
- FLHSMV 2023 Traffic Crash Facts: Orange County recorded 26,263 crashes, 172 fatalities, 19,618 injuries, of which 267 crashes / 24 fatalities / 190 injuries were "alcohol confirmed" — a label the report defines as BAC greater than 0.00, not the 0.08 criminal threshold — https://www.flhsmv.gov/pdf/crashreports/crash_facts_2023.pdf

Full source list for every statutory and local claim is inside the `## RULES` block at the top of `copy.md` (popped by `parse_copy`, so it neither renders nor enters the duplicate corpus).
