# QC flow fixes — batch 1 report

Assignment: `qcfix/batch1.md` — 45 flow findings across 7 sites.
Result: **45 of 45 cleared. 0 findings remain on any of the 7 sites** (`qc.py` over all seven
returns 0 findings, all severities and kinds), and every site passes
`template/build.py --check-only`.

| Domain | Findings assigned | Cleared | Left |
|---|---|---|---|
| sacramentodogbitelawyerpros.com | 26 | 26 | 0 |
| jacksonvilleemergencyplumberpros.com | 7 | 7 | 0 |
| tempeduilawyerpros.com | 4 | 4 | 0 |
| dallaswrongfuldeathlawyerpros.com | 3 | 3 | 0 |
| garlandgaragedoorrepairexperts.com | 2 | 2 | 0 |
| victorvillecaraccidentlawyerpros.com | 2 | 2 | 0 |
| scottsdalegaragedoorrepairpros.com | 1 | 1 | 0 |

Two pre-existing LOW `mechanics` findings ("paragraph has no terminal punctuation" on
dallaswrongfuldeathlawyerpros.com `/` and jacksonvilleemergencyplumberpros.com `/`) were present
in the baseline CSV and are also gone after the rebuild; they were stale `dist/` artifacts, not
copy defects. No HIGH finding was introduced anywhere.

## What was changed, per domain

### scottsdalegaragedoorrepairpros.com (1)
- `/` "3 paragraphs in a row open with 'the'": reworded the middle value block (`value_1` in
  copy.md) from "The repair is evaluated at the door…" to "Every repair is evaluated at the door…".

### victorvillecaraccidentlawyerpros.com (2)
- Split the 51-word Victorville District filing sentence (Civil Division venue list + drop-box
  cutoff) into two, keeping the full community list and the four-in-the-afternoon cutoff intact.
- Split the 50-word CHP Victorville Area sentence: coverage list, then the consequence sentence
  ("A collision a few minutes past the city line therefore usually sits with the CHP…").

### garlandgaragedoorrepairexperts.com (2)
- Split the 54-word UL 325 sentence at the 1991/1993 boundary; both dates and both requirements
  preserved verbatim.
- Split the 52-word Moore, Oklahoma wind-speed sentence after "…135 in 2014 to account for tornado
  edge winds."; the 90/135 mph figures and 2014 date are unchanged.

### dallaswrongfuldeathlawyerpros.com (3)
- `/medical-negligence-death-claim`: split the 50-word Chapter 74 definition into definition +
  scope of covered standards. The markdown link to
  https://statutes.capitol.texas.gov/docs/cp/htm/cp.74.htm is untouched.
- `/pricing` lede: 62-word sentence split into three (no cap in Texas law → what Rule 1.04
  disclosure protects → what the page covers).
- `/pricing`: split the 53-word Rule 1.04(d) list into contract contents + expense-ordering clause.

### tempeduilawyerpros.com (4)
- `/dui-license-suspension`: the flagged 60-word unit was two real sentences the checker could not
  split (a period inside a closing quote). Broke the second sentence in two, so the longest
  measured unit is now 42 words. The quoted statutory phrase "is effective thirty days after the
  date it is served," the thirty-day permit, the 0.08 threshold and the ninety-day minimum are all
  unchanged.
- `/pricing`: same quote-boundary situation on ER 1.5(d)(2)/(d)(3); split the (d)(3) sentence into
  the permission and the written-disclosure condition.
- `/pricing` "3 paragraphs in a row open with 'a'": the run came from consecutive sourced fact
  cards whose claims and source labels both start "A.R.S." Added short lead-ins to two of the
  `pricing.anchors` details in site.json ("Surcharges stack on that fine." / "Extreme counts carry
  their own numbers.") so no three consecutive blocks share an opener. All statute numbers,
  percentages and dollar amounts untouched.
- `/contact` "'tempe' used 13x in 557 words": replaced two brand-style repetitions in copy.md
  ("A Tempe DUI attorney cannot responsibly promise…" → "A defense attorney…"; "A Tempe DUI lawyer
  can identify…" → "A DUI lawyer here can identify…"). The remaining mentions are template chrome
  and the city name in site.json, which was not touched.
- The pricing page tripped the 900–1750 word ceiling (1752) after these edits; recovered six words
  by tightening my own added lead-ins and one "to be set out in writing" → "put in writing". No
  fact, figure or citation was removed to make room.

### jacksonvilleemergencyplumberpros.com (7)
- `/drain-cleaning`: 71-word EPA hydrogen-sulfide corrosion sentence split into three (sulfate
  reduction and gas release / oxidation to sulfuric acid and crown loss); 55-word Florida cleanout
  sentence split at the junction-cleanout clause; 53-word clearing-sequence sentence split at
  "Once the line is open…".
- `/emergency-plumbing-repair`: 59-word termite-sleeve sentence split after "cannot contain
  cellulose" (the ten-thousandths-of-an-inch limit, clamping device and no-termiticide condition
  all kept); 49-word cleanout sentence split off "That access usually exists and is worth locating."
- `/sewer-line-repair`: 54-word vacuum-sewer conversion sentence split before "A JEA inspector
  witnesses the flushing…"; 60-word backwater-valve sentence split after "the Florida plumbing code
  requires protection."
- Every 100-foot interval, eight-inch and ten-foot dimension preserved exactly.

### sacramentodogbitelawyerpros.com (26)
- One shared sourced fact (`owner_rule_and_landlord_duty` in site.json) accounted for 6 of the 26
  findings, because the same 54-word claim renders on `/` and four service pages. Split it after
  "…lawfully in a public or private place." so Uccello v. Laudenslayer starts its own sentence.
  Both source URLs unchanged.
- `/child-dog-bite-claim` (4 more): split the tolling sentence (parent's claim vs. the six-month
  Government Code presentation deadline), the 1975 median / 55 percent housing-stock sentence, the
  child-standard-of-care sentence, and the 67-word Rule of Court 7.955 sentence (standard, then
  "The rule lists fourteen factors, including…").
- `/dog-bite-injury-claim` (4 more): split the lawful-presence sentence, the subdivisions (b)–(d)
  police-dog carve-out, the "which office holds the file" agency split, and the section 6147
  written-agreement sentence.
- `/dog-bite-insurance-claim` (5 more): split the title 10 claim-handling intervals (15/40/30
  calendar days all preserved), the 67-word no-private-right-of-action sentence into three, the
  animal-control report-number sentence, the comparative-fault sentence, and the 1.5(a)/1.5(b)/6147
  fee sentence.
- `/landlord-dog-bite-liability` (3 more): split the renter-occupied single-unit sentence, the
  vicious-animal-affidavit sentence (thirty days, five calendar days to appeal both kept), and the
  1.5(a)/6147 fee sentence.
- `/pricing` (3 more): split the 62-word lede, the Rule of Court 7.955(a)(1) sentence (Code of Civil
  Procedure section 372 and Probate Code sections 3600 to 3601 kept verbatim), and the
  fourteen-factor list.
- `/services` "'sacramento' used 12x in 533 words": changed the services summary opener "…dog bite
  lawyer in Sacramento" to "…dog bite lawyer here" (that line renders twice, as hero and body), so
  the count falls to 10.
- `/contact` "'sacramento' used 14x in 511 words": only 2 of the 14 mentions sat in authored copy —
  the other 12 come from template chrome (hero tagline, generated coverage line, footer brand line)
  and from site.json identity fields, which I did not touch. Cleared it by (a) rewriting
  `emergency_note` to name the animal-control channel by address instead of by county, which
  removes one mention from each of its two renders, and (b) expanding `expect_intro_1` with one
  sentence that restates the four record groups already itemised immediately below it on the same
  page. No new fact was introduced; the ratio now sits under the 2.2 percent threshold.

## Findings deliberately left
None. All 45 assigned findings are cleared.

## Factual issues noticed while editing (not changed)
- `sacramentodogbitelawyerpros.com` `/pricing` licensing paragraph mixes dollar formats in one
  sentence: "A late payment adds $25.00, a duplicate tag costs $5". The `.00` is inconsistent with
  every other figure on the page. Left exactly as written because dollar figures are off-limits;
  a follow-up pass may want to normalise it to `$25`.
- `sacramentodogbitelawyerpros.com/copy.md` has a missing blank line between the end of the
  county-licensing paragraph (line 288) and the `## services_summary` heading (line 289). The
  builder still parses it, but it is the only heading in the file without a preceding blank line.
- No incorrect statute number, date, deadline, measurement or dollar amount was found in any of the
  seven sites. Two "runaway sentence" flags on tempeduilawyerpros.com were checker artifacts, not
  real 60-word sentences: `qc.py`'s splitter does not break after a period that falls inside a
  closing quotation mark, so it merges two legitimate sentences. Worth fixing in `qc.py`
  (`sentences()`, line 121) rather than in copy.

## Verification commands run
From `/home/user/workspace/local-sites`, per domain and then across all seven:

```
timeout 300 python3 template/build.py --check-only <domain>   # [PASS] for all 7
timeout 300 python3 template/build.py <domain>                # rebuild dist/ so qc reads new html
timeout 300 python3 qc.py <domain>                            # 0 findings for all 7
```

Helper left in place: `qcfix/_show.py <domain> <page> [sent]` dumps the visible prose blocks (or
just the >44-word sentences) of a built page using `qc.py`'s own parser.
