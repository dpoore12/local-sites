# Phase 2 conversion report — louisvillecaraccidentlawyerpros.com

## Build result

```
[PASS] louisvillecaraccidentlawyerpros.com -- home 1548 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           356 words  /about/
          1494 words  /commercial-truck-collision-lawyer/
           575 words  /contact/
          1861 words  /
          1450 words  /injury-claim-negotiation/
          1548 words  /pricing/
          1462 words  /rear-end-collision-lawyer/
           557 words  /services/
          1500 words  /uninsured-driver-claim-lawyer/
```
`python3 template/build.py --check-only louisvillecaraccidentlawyerpros.com` → exit 0.

`site.json` "phase" flipped 1 → 2. Nothing else in site.json touched.

Independent post-checks run on copy.md: zero shared 15-word runs with ANY sibling site (full `sites/*/copy.md` sweep, not just the eight named); zero sentences over 44 words anywhere in the file; no doubled words; no duplicate or back-to-back headings; no heading over 89 chars; no run of 5+ one-sentence paragraphs; no bare decimals (the only `.\d` hits are statute cites like KRS 24A.120). City/state density: "Louisville" 0.26%, "Kentucky" 0.47% of the file.

Block word counts added/changed: symptom_1 66, symptom_2 63, symptom_3 65, symptom_4 59; services_summary 104; services_pick_head 9; crosslink_head 4; ledes 38–40 each; bodies — rear-end 889, uninsured ~900, truck ~915, negotiation 877.

## 3 strongest verified local facts

1. **Jefferson County crash volume.** 25,417 crashes in 2024 against 14,830 in 2020 — 44.4% above the prior four-year average, with 4.2% injury-or-fatal ([KYTC 2020–2024 traffic crash analysis](https://transportation.ky.gov/HighwaySafety/KYTrafficCrashAnalysis/AnalysisTrafficCrash2020-2024.pdf)).
2. **Watterson Expressway reconstruction.** $130M on I-264 MP 21.1–22.7 (KY 1447/Westport Road to I-71), two lanes each way widened to three, U.S. 42 rebuilt as a single-point urban interchange, two 11-foot lanes maintained, completion anticipated fall 2027 ([KYTC District Five project page](https://transportation.ky.gov/DistrictFive/Pages/I-264-and-U.S.-42-Improvement-Project-(Construction-Phase).aspx)).
3. **Ohio River tolling corridor, rates effective July 1, 2026.** $2.79 transponder / $5.57 standard for a car and $16.62 for 5+ axles after a 3.8% CPI adjustment ([RiverLink toll rate notice](https://riverlink.com/2026/06/15/reminder-new-toll-rates-effective-july-1-5/)), with the Clark Memorial and I-64 Sherman Minton crossings free ([RiverLink non-tolled alternatives](https://riverlink.com/about/non-tolled-alternatives/)).

Runners-up used on the pages: Kennedy Interchange reconfigured under the Downtown Crossing at $1,478 million YOE, six northbound I-65 lanes on the Lincoln Bridge and six southbound on the Kennedy ([FHWA project profile](https://www.fhwa.dot.gov/ipd/project_profiles/ky_downtown_crossing.aspx)); Circuit/Family at the Judicial Center, 700 W. Jefferson St., District plus clerk at the Hall of Justice, 600 W. Jefferson St. ([Kentucky Court of Justice, Jefferson County](https://kycourts.gov/Courts/County-Information/Pages/Jefferson.aspx)); statewide 9,446 truck-related crashes in 2024 including 73 fatal (same KYTC analysis).

## Corrections to the writer brief

1. **The limitations instruction conflated two statutes.** The brief said "Kentucky's very short ONE-YEAR limit for injury and the wrinkle that it runs two years from the last PIP payment in a motor vehicle case." Those are separate provisions, and the one-year rule is not the operative deadline for a motor vehicle tort claim. [KRS 413.140(1)(a)](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=58050) sets one year for personal injury generally. [KRS 304.39-230(6)](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=45816) governs a tort claim not abolished by KRS 304.39-060 and allows **two years** after the injury, the death, **or the date of issuance of the last basic or added reparation payment by any reparation obligor, whichever occurs later** — so the floor in a crash case is two years, not one, and it can run longer. Two details the brief omitted and the pages now carry: a *replacement* payment (reissued in the same amount because the original was lost, stolen or undelivered) does not extend the period past the original payment date, and the obligor must answer a written request stating whether a payment was a replacement. The site therefore never presents "one year" as the car-crash deadline.
2. **"BRB/PIP amount" is one number, not two, and it is an aggregate economic-loss cap.** [KRS 304.39-020(2)](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=57854) caps basic reparation benefits at **$10,000 for all economic loss to one person from one accident** regardless of how many obligors might owe, with funeral/cremation/burial capped at $5,000 per person. It is not a per-category or per-carrier figure.
3. **The rejection form is filed with the Department of Insurance, not the insurer, and its name is fixed by regulation.** [806 KAR 39:030](https://apps.legislature.ky.gov/law/kar/titles/806/039/030/) prescribes the Kentucky No-Fault Rejection Form (original plus one copy, or the online version), effective on the department's file stamp, with a file-stamped copy then sent to the insurer. Also worth flagging: 304.39-060(7) includes a **deemed rejection** for a person who carried no basic reparation insurance and filed no rejection but had security equivalent to KRS 304.39-110 in force — full rejection of the tort limitations, "for that accident only."
4. **UM and UIM are not a single "UM/UIM rule."** Uninsured motorist coverage is mandatory in every liability policy on a Kentucky-registered or principally-garaged vehicle unless a named insured rejects it in writing ([KRS 304.20-020](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=45737)), at the [KRS 304.39-110](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=45803) limits of $25,000/$50,000/$25,000 or $60,000 single. Underinsured coverage exists only "upon request" under [KRS 304.39-320](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=45822), which also imposes the certified-mail notice and 30-day consent-or-pay procedure before a liability release. Treating them as one rule would have produced a wrong page.
5. **"Circuit vs district dollar line" is a floor for District Court, phrased as exclusive jurisdiction.** [KRS 24A.120](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=45261) gives District Court exclusive civil jurisdiction where the amount in controversy does not exceed **$5,000 exclusive of interest and costs**; Circuit Court is general jurisdiction above that.
6. **Naming constraint vs. local texture.** The brief asked for "Jefferson County Circuit Court filing" detail, but the no-named-person rule meant the clerk could not be named. The pages carry the filing economics instead ($188 civil filing fee under CR 3.02(1) as amended for 2026, plus the $20 court technology fee) and the two courthouse addresses.
7. **eCFR was unusable** (repeated timeouts). Federal citations were verified against govinfo XML for 49 CFR 390.15, 382.303 and 395.8 instead. Anyone re-verifying should go straight to govinfo.

## Editorial notes

- Fee content states only what Kentucky's rules require and what the market/court charges: [SCR 3.130(1.5)](https://www.kycourts.gov/Courts/Supreme-Court/Supreme%20Court%20Orders/200905.pdf) sets no percentage and bars unreasonable fees and expenses under eight factors, requires a signed writing with percentages at settlement/trial/appeal, an expenses-owed-either-way warning and a closing statement, and bars result-based fees in criminal and most domestic matters. Contrasted with the one place Kentucky *does* print numbers, [KRS 342.320](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=45525) workers' compensation tiers of 20/15/10 percent capped at $18,000. No "we charge" framing anywhere.
- Pricing page never went over its 1,750 ceiling (1,548). Sentence-length trims there split long sentences; **no dollar figure or fee was removed**.
- Collision avoidance required one rewrite: an initial "a driver produces no card at all…" passage tripped four 15-word runs against Harrisburg and was rewritten. No overlap remains with any sibling, including Cincinnati.
