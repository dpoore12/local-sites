# Phase 2 conversion report — jacksonvillewrongfuldeathlawyerpros.com

## Build result

```
[PASS] jacksonvillewrongfuldeathlawyerpros.com -- home 1742 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           386 words  /about/
           618 words  /contact/
          1538 words  /fatal-car-accident-claim/
          1536 words  /fatal-work-accident-claim/
          1917 words  /
          1498 words  /medical-negligence-death-claim/
          1742 words  /pricing/
           603 words  /services/
          1472 words  /wrongful-death-damages-claim/
```
`python3 template/build.py --check-only jacksonvillewrongfuldeathlawyerpros.com` exits 0. `site.json` `"phase"` flipped 1 → 2 (only field changed).

Slugs used, exactly as in site.json: `fatal-car-accident-claim`, `fatal-work-accident-claim`, `medical-negligence-death-claim`, `wrongful-death-damages-claim`.

## Collision check

15-word shingle comparison against all 8 named siblings **and** every other site in `sites/`: **0 shared runs**. Script: `/tmp/collide.py` (uses `template/build.py:parse_copy`).

Deliberate deviation from the brief: `jacksonvilleemergencyplumberpros.com` already owns JEA (31 mentions), the Mathews Bridge, and the Riverside/Avondale/Springfield build-era history, so this site avoids JEA, Mathews Bridge, and neighborhood-history material entirely. Local texture instead comes from FDOT District Two Duval crash data, the city Vision Zero plan, the Fourth Judicial Circuit and Duval Clerk, and the District 4 medical examiner.

## qc.py findings (after rebuild)

Only two, both matching the Dallas baseline pattern: the pricing `table_head` h2 is 96 chars (comes from site.json, which I may not edit — Dallas's is 105), and a 5+ one-sentence-paragraph run inside the clerk fee table. No mechanics, claims, spelling, or flow findings.

## Three strongest verified local facts

1. **Duval County 2024: 38,584 crashes, 154 fatalities, 498 serious injuries, county population 1,055,159; lane departures tied to 63 deaths, impaired driving 53, pedestrians/bicyclists 51** — FDOT District Two Community Traffic Safety Program, [2024 Duval Crash Facts](https://trafficsafetyteam.org/wp-content/uploads/2025/04/CTSP-2024-Duval-Crash-Facts.pdf).
2. **Jacksonville 2018–2023: 921 traffic deaths across 196,453 crashes, 211 of them pedestrians; 60% of severe pedestrian/bicycle crashes at night; drugs or alcohol in 54% of fatal vehicle crashes** — City of Jacksonville [Vision Zero Action Plan](https://www.jacksonville.gov/departments/planning-department/transportation-planning/ped-bike-planning/vision-zero-action-plan-(vzap)).
3. **Duval County Clerk death-claim costs: formal administration $401, summary administration $346 (estate ≥ $1,000), guardianship of the property $400; circuit civil filing $401 plus $10 per summons** — [Duval County Clerk of Courts probate fees](https://www.duvalclerk.com/departments/civil-court-services/probate). Paired with the Fourth Judicial Circuit at 501 West Adams Street ([jud4.org](https://www.jud4.org/news/2021-03-30-welcome-to-the-official-website-of-the-4th-judicial-circuit-court)) and District 4 medical examiner at 4368 North Davis Street ([jacksonville.gov](https://www.jacksonville.gov/departments/finance/liaison-agencies/medical-examiner)).

## Where the brief was wrong or needed correction

1. **"the notorious FREE KILL provision … research what happened to it in 2025 legislation."** The 2025 story is only half of it, and the answer is that the provision **is still law**. Section 768.21(8) appears in the current statutes. HB 6017 (2025) passed the House 104–6 and the Senate 33–4 and was **vetoed on May 29, 2025** ([flsenate.gov bill history](https://www.flsenate.gov/Session/Bill/2025/6017); [Governor's veto statement](https://www.flgov.com/eog/news/press/2025/governor-ron-desantis-issues-veto-safeguard-florida-against-misuse-medical)). A second repeal, HB 6003 (2026), passed the House 88–17 on January 15, 2026 and then **died in Senate Rules on March 13, 2026** ([official House bill history PDF](https://www.leg.state.fl.us/data/session/2026/citator/Daily/hsehist.pdf)). Anything written only from 2025 coverage would have been wrong twice over.
2. **Sovereign immunity caps "and the claim bill process"** — correct, but the brief does not mention that the caps nearly moved. HB 145 (2026) passed the House 104–7 and the Senate 36–0, cleared concurrence 108–1, and was **vetoed on June 30, 2026** ([flsenate.gov](https://www.flsenate.gov/Session/Bill/2026/145)), so $200,000 / $300,000 still stand.
3. **"Florida's 2023 tort reform changing comparative negligence to a modified 51 percent bar"** — the statute is not phrased as a 51 percent bar. Section 768.81(6) bars a party found **greater than 50 percent** at fault, and it **expressly does not apply** to personal injury or wrongful death arising from medical negligence under chapter 766. The medical-negligence page says so explicitly; a "51 percent bar applies statewide" framing would have been inaccurate.
4. **Effective dates** — chapter 2023-15 was approved March 24, 2023; the 95.11 amendments apply to causes of action **accruing after** that date, so pre-3/24/2023 deaths can still sit under the old four-year negligence period. The brief asked me to verify this and the verification changes what the page can safely say.
5. **JEA / Mathews Bridge / neighborhood history** were suggested as local texture but are already used heavily by the same-city plumber site, so they were dropped (see above). Not an error in fact, but the two instructions conflicted.
6. Also worth flagging: **Florida has no OSHA-approved state plan** for private employers, so a workplace death is a federal 8-hour report ([osha.gov/report](https://www.osha.gov/report), [state plan list](https://www.osha.gov/stateplans)) — relevant to the work-accident page and not mentioned in the brief.

## Fee page

Written entirely as what the market and Florida's rules require, never as "our" price. Rule 4-1.5(f)(4)(B) tiers are given verbatim by subdivision — (i)a pre-answer 33 1/3 / 30 / 20; (i)b post-answer 40 / 30 / 20; (i)c liability admitted 33 1/3 / 20 / 15; (i)d appellate +5 percent — plus the (f)(4)(B)(ii) court-approval petition, the (f)(4)(A) three-business-day cancellation, the (f)(5) closing statement retained 6 years, the (f)(4)(D) 75/25 split, and the Art. I §26 constitutional 70/90 percent floor on the medical page. No dollar figure or fee was removed during trimming; only prose was shortened.

## Files touched

- `sites/jacksonvillewrongfuldeathlawyerpros.com/copy.md` (rewritten symptoms 1–4; added `services_summary`, `services_pick_head`, `crosslink_head`, 4 × `svc_*_lede`, 4 × `svc_*_body`; trimmed `pricing_lede` and `pricing_body` prose)
- `sites/jacksonvillewrongfuldeathlawyerpros.com/site.json` (`phase`: 2)
- Working artifacts left in place: `_jax_wd_blocks.md`, `_jax_wd_merge.py`, `jacksonvillewrongfuldeathlawyerpros.com-phase2-research.md`
