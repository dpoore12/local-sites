# Phase 2 conversion report — fortlauderdaledomesticviolencelawyer.com

## Build result (exit 0)

```
[PASS] fortlauderdaledomesticviolencelawyer.com -- home 1740 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           404 words  /about/
           652 words  /contact/
          1529 words  /domestic-violence-defense-lawyer/
          1943 words  /
          1436 words  /order-violation-defense/
          1740 words  /pricing/
          1430 words  /protective-order-defense/
          1331 words  /restraining-order-hearing/
           629 words  /services/
```

`site.json` `"phase": 2`. Only `copy.md` and the phase field were edited.

## Authored block sizes
- symptom_1 65, symptom_2 62, symptom_3 58, symptom_4 58 words (band 40–80)
- services_summary 113 (95–115); services_pick_head 7 ("Start with the document that arrived first"); crosslink_head 5 ("A different order or charge?")
- Ledes: 35 / 39 / 34 / 38 words (30–45)
- Service bodies: within the 700–900 authored band; rendered pages 1529 / 1430 / 1331 / 1436 (900–1550)
- Pricing 1740 of 1750 ceiling. Trimmed prose only; every dollar figure kept, and two figures were **added** ($40/month county misdemeanor supervision under 948.09; the 29-week/24-session program under 741.325).

## 3 strongest verified local facts
1. **No release before first appearance.** Fla. Stat. 903.011(6) lists domestic violence as defined in 741.28 among arrests where a person may not be released before first appearance or a bail determination ([Fla. Stat. 903.011](https://www.flsenate.gov/Laws/Statutes/2025/903.011)), and the Seventeenth Circuit's uniform bond schedule order records "Bond: None / First Appearance Required" for those arrests ([AO 2025-50-Crim](https://www.17th.flcourts.org/wp-content/uploads/2026/01/2025-50-Crim-with-Exhibit-A.pdf)); 741.2901(3) adds the statutory hold ([Fla. Stat. 741.2901](https://www.flsenate.gov/Laws/Statutes/2025/741.2901)) and Rule 3.130(a) the 24-hour limit ([Florida Courts first appearance material](https://www.flcourts.gov/content/download/1236503/file/FIRST%20APPEARANCE%20MATERIAL%209.29.23.pdf)).
2. **The alleged victim cannot end the case, and Broward says so procedurally.** Requests to drop charges or waive prosecution are not addressed at First Appearance Court; waivers go through the Victim Advocate Unit, and dockets run 9:00 a.m. and 12:30 p.m. in courtroom 04155, west wing, 201 SE 6th Street ([Broward State Attorney](https://browardsao.com/victim-advocate-unit-first-appearance-court/)), matching 741.2901(2)'s "over the objection of the victim, if necessary" ([Fla. Stat. 741.2901](https://www.flsenate.gov/Laws/Statutes/2025/741.2901)).
3. **Venue split and no filing fee.** Civil DV division judges sit on the tenth floor of the west wing with final hearings typically within 15 days, while felony DV court is in the north wing ([17th Circuit DV division](https://www.17th.flcourts.org/06-domestic-violence/)); the Clerk confirms no filing fee, ePortal or in-person filing, same-day judicial review, and roughly 1–1.5 hours of paperwork ([Broward Clerk](https://www.browardclerk.org/Divisions/DomesticViolence)).

## Things in the brief that were wrong
1. **BIP length.** Brief said 26 weeks. Fla. Stat. 741.325 requires **at least 29 weeks, including 24 weekly sessions** plus intake, assessment and orientation, funded by attendee user fees ([Fla. Stat. 741.325](https://www.flsenate.gov/Laws/Statutes/2025/741.325)). Copy uses 29.
2. **"Adjudication may not be withheld"** has no found statutory basis. 741.281 applies to a finding of guilt, a withheld adjudication, or a nolo plea (1 year probation + BIP) ([741.281](https://www.flsenate.gov/Laws/Statutes/2025/741.281)); 741.283's mandatory jail applies only where the person **is adjudicated guilty** and intentionally caused bodily harm ([741.283](https://www.flsenate.gov/Laws/Statutes/2025/741.283)).
3. **No-bond authority** is 903.011(6) plus the circuit bond-schedule AO, not the Rules of Criminal Procedure; Rule 3.130(a) supplies only the 24-hour deadline.
4. **Dismissed DV charge** is handled by **expunction under 943.0585**, not sealing under 943.059. 943.0584(2)(f) bars sealing/expunction of a *conviction* for assault or battery between family or household members, and defines conviction to include a plea with adjudication withheld ([943.0584](https://www.flsenate.gov/Laws/Statutes/2025/943.0584)).

No conflicts between site.json and the brief arose; site.json slugs, city/county and phone were used exactly.

Research notes with all sources: `fortlauderdale-dv-phase2-research.md`. Staged draft: `_ftl_dv_phase2_blocks.md`.
