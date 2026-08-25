# Phase 2 report — tampafamilylawattorneypros.com

## Build result

```
[PASS] tampafamilylawattorneypros.com -- home 1746 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           381 words  /about/
          1547 words  /child-custody-attorney/
          1504 words  /child-support-attorney/
           617 words  /contact/
          2090 words  /
          1539 words  /paternity-attorney/
          1746 words  /pricing/
           571 words  /services/
          1543 words  /spousal-support-attorney/
```
`python3 template/build.py --check-only tampafamilylawattorneypros.com` exits 0. The duplicate-prose guard was run against all other sites in the portfolio and is clean.

## Files changed

- `sites/tampafamilylawattorneypros.com/copy.md` — symptoms 1–4 rewritten as teasers, plus 11 new blocks.
- `sites/tampafamilylawattorneypros.com/site.json` — `"phase": 1` → `"phase": 2`. Nothing else touched.

Research notes: `tampafamilylawattorneypros.com-phase2-research.md`. Working files: `_tampa_familylaw_blocks.md`, `_tampa_familylaw_merge.py`, `research-tampa-familylaw/`.

## Service page slugs written

`child-custody-attorney`, `child-support-attorney`, `paternity-attorney`, `spousal-support-attorney` — taken verbatim from `site.json`.

## Authored block word counts

| block | words |
|---|---|
| symptom_1 | 68 |
| symptom_2 | 70 |
| symptom_3 | 63 |
| symptom_4 | 68 |
| services_summary | 103 |
| services_pick_head | 8 |
| crosslink_head | 6 |
| svc_child_custody_attorney_lede | 41 |
| svc_child_custody_attorney_body | ~932 |
| svc_child_support_attorney_lede | 41 |
| svc_child_support_attorney_body | ~849 |
| svc_paternity_attorney_lede | 40 |
| svc_paternity_attorney_body | 887 |
| svc_spousal_support_attorney_lede | 38 |
| svc_spousal_support_attorney_body | ~890 |

Note on the body ceiling: the brief targets 700–900 authored words, but the binding gate is the rendered 900–1550 range, and the shared chrome on a service page is about 615 words. Bodies were tuned to land each page just under 1550 rather than to a bare word target; the custody body is the only one materially over 900 authored words and its page renders at 1547.

## Differentiator built into the site

Every service page is anchored on Florida's 2023 rewrite rather than generic family-law content:

- Custody page: the equal time-sharing presumption created by ch. 2023-301, the deleted "unanticipated" modification requirement, the statutory minimum contents of a parenting plan, and the military overlay.
- Child support page: the 20-percent overnight threshold and the gross-up method, imputed income, the 5-percent written-finding rule, the 55-percent deviation factor, and the 15-percent-or-$50 modification gate.
- Paternity page: the 60-day rescission window, the 2023 natural-guardianship amendment, the 95-percent testing presumption with its 10-day objection deadline, and 24-month retroactive support.
- Spousal support page: the four surviving forms, the removal of permanent alimony, the 50/60/75-percent duration caps, the 35-percent net-income ceiling, and the new retirement pathway.

## Three strongest verified local facts

1. **Equal time-sharing is now the statutory starting point in every Hillsborough County parenting case.** Fla. Stat. 61.13(2)(c)1 states there is a rebuttable presumption that equal time-sharing of a minor child is in the child's best interests, rebuttable by a preponderance of the evidence. It was created by CS/HB 1301 (2023), enacted as ch. 2023-301 and effective July 1, 2023. Statute: https://www.flsenate.gov/Laws/Statutes/2025/61.13 — bill: https://www.flsenate.gov/Session/Bill/2023/1301 — chapter law: https://laws.flrules.org/2023/301
2. **Florida law bars a Tampa judge from holding a MacDill parent's deployment against them.** Fla. Stat. 61.713, part of the Uniform Deployed Parents Custody and Visitation Act adopted as part IV of chapter 61 by ch. 2018-69, says a court may not consider a parent's past deployment or possible future deployment in determining the best interest of the child. The same part sets a 7-day notice duty on a deploying parent (61.709) and automatically terminates a temporary custodial-responsibility agreement 30 days after notice of return (61.761(3)). Chapter text: https://www.flhouse.gov/Statutes/2025/Chapter0061/All/ — MacDill's two joint command headquarters and refueling wing: https://www.macdill.af.mil/About-Us/Fact-Sheets/Article/4160667/macdill-air-force-base/
3. **The Thirteenth Judicial Circuit adds local gates a statewide checklist does not show.** Its standing temporary order in minor-children cases requires both parents to finish an approved parent-education course within 60 days of filing, will not permit a final judgment without both certificates, and requires mediation before a temporary-relief hearing and before a final hearing. The circuit's own case management page adds that mediation is a required step in all post-judgment cases not involving the Department of Revenue, that a respondent in a paternity case must answer within 20 days of service, and that parties must attempt agreement before a general magistrate hearing can be set. Standing order: https://www.fljud13.org/Portals/0/Forms/pdfs/family/StandingTempOrderWithMinorKidsOrd.pdf — case management unit: https://www.fljud13.org/Court-Services/Court-Programs/Domestic-Relations-Case-Management-Unit — courthouse: https://www.fljud13.org/CourthouseDirections.aspx

## Things in the brief I found to be wrong or imprecise

1. **"Whether Florida still has any waiting period."** Florida has no separation or cooling-off period at all. The only timing rule is Fla. Stat. 61.19, which bars a final judgment until at least 20 days have elapsed from the filing of the original petition unless the court finds injustice would result from the delay. That is a floor on the judgment, not a waiting period before filing. https://www.flsenate.gov/Laws/Statutes/2025/61.19
2. **"Mandatory mediation before a contested hearing."** There is no single statewide rule to that effect. What is verifiable is narrower and local: the circuit's standing order in minor-children cases requires mediation before a temporary-relief hearing and before a final hearing, and the circuit states separately that mediation is required in all post-judgment cases not involving the Department of Revenue. The pages are written to that precision rather than to the broader claim.
3. **`61.13002` is no longer the military time-sharing statute.** It appears in older editions of chapter 61 and is a common citation in secondary sources, but it is absent from the current chapter. The operative law is part IV, ss. 61.703–61.773. Worth flagging for any future family-law site in this portfolio.
4. **"Contingency fees are prohibited in domestic relations matters" is true but incomplete.** R. Regulating Fla. Bar 4-1.5(f)(3)(A) bans a fee contingent on securing a divorce or on the amount of alimony, support, or property settlement in lieu thereof — and it expressly carves out a contingent arrangement for collecting a post-judgment balance already due under a support, alimony or other financial order. Both halves are on the site.
5. **The brief warned the pricing page would be over its 1750-word ceiling.** It was not. It came in at 1729 in the phase-1 baseline and 1746 after phase 2 added a band to the page. No dollar figure or fee was removed. What I did change on that page was editorial: three sentences of 53–55 words were split to satisfy the section 12 sentence-length rule, with word count held essentially flat.

## Pre-existing defect the parent agent should fix (outside my edit scope)

`site.json` has `"brand": "Tampa Family Law Law Pros"` — a doubled word. It renders in the call bar, the aria-label and the footer on all nine pages, and `qc.py` flags it nine times as a HIGH "doubled word" finding. It is the only HIGH finding on the site. I was instructed to change only the `phase` field, so I left it; the fix is deleting one "Law" from the brand string.

The 10 remaining MED findings are all spelling-dictionary misses on statutory vocabulary: `durational`, `nonmarital`, `payor`, `servicemember`, `dissolutions`. Those are the words the Florida statutes use and were left as written. No flow, structure, claims or mechanics findings remain in the copy I authored.

## Collision avoidance

Read in full before writing: `tampacriminaldefenselawyerpros.com/copy.md` and `denverdivorcelawyerpros.com/copy.md`. Subhead inventories were pulled for `orlandoduilawyerpros.com`, `jacksonvillewrongfuldeathlawyerpros.com` and `sandiegowrongfulterminationlaw.com` to steer clear of their heading patterns. Denver's "how you know" / "the mistake that costs the case" / "what the other side does" / "how fees work under Colorado's rule" shapes were deliberately reworded. Tampa geography here leans on Davis Islands, Ybor City and Seminole Heights, and cites the courthouse and the case management unit by room number rather than repeating the criminal defense site's clerk sequence.

One real collision surfaced and was fixed: the phrase "contingent on securing a divorce or on the amount of alimony, support or a property settlement" tripped a 3-run overlap with `atlantadogbitelawyerpros.com`. Both occurrences were rephrased. The final check is clean against all other sites.
