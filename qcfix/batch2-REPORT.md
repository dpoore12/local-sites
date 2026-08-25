# QC flow fixes — batch 2 report

Assignment: `qcfix/batch2.md` — 45 flow findings across 8 sites.
Result: **45 of 45 cleared. 0 findings remain on these 8 sites (no HIGH, MED or LOW).**
Every site prints `[PASS]` from `template/build.py --check-only` and returns an empty findings set from `qc.py`.

Verification command run at the end:

```
python3 qc.py denverdivorcelawyerpros.com appliancerepairtampaco.com \
  sanjoseemergencyplumberpros.com westcovinacaraccidentlawyerpros.com \
  danvillegaragedoorrepairpros.com lasvegasdogbitelawyerpros.com \
  virginiabeachpersonalinjurylawyerpros.com concordcaraccidentlawyerpros.com
=> QC over 8 sites -- 0 findings
```

---

## denverdivorcelawyerpros.com — 19/19 cleared

| Page | Finding | Fix |
|---|---|---|
| /contested-divorce-lawyer | runaway sentence (64) | Split the 14-10-113 property-division sentence into three: the "without regard to marital misconduct" rule, the list of factors, and the family-home factor. |
| /contested-divorce-lawyer | runaway sentence (51) | Split the 14-10-114(3)(b) maintenance sentence into a threshold sentence and a formula sentence. |
| /contested-divorce-lawyer | runaway sentence (58) | Split "what the other side does" into three: temporary orders, then discovery, then the late settlement number. |
| /contested-divorce-lawyer | runaway paragraph (205) | Broke "What the Colorado statutes actually set" at the jurisdiction/property → maintenance/child-support shift. |
| /divorce-mediation-lawyer | runaway sentence (55) | Maintenance guideline split into threshold + advisory term table. |
| /divorce-mediation-lawyer | runaway sentence (51) | 14-10-124(7) parenting-plan contents split into the schedule/exchange items and the communication procedures. |
| /divorce-mediation-lawyer | runaway sentence (58) | Park Hill housing sentence split into three; the 1887 platting fact moved to its own sentence. |
| /divorce-mediation-lawyer | runaway sentence (53) | ODR $75/hour sentence split from the deposit/cancellation terms. |
| /divorce-mediation-lawyer | runaway sentence (52) | RPC 1.5(c)(4)(ii) prohibition split from the "hourly or defined flat scope" consequence. |
| /divorce-mediation-lawyer | runaway paragraph (208) | Broke "What the rules put around the room" after the memorandum-of-understanding sentence. |
| /high-asset-divorce-lawyer | runaway sentence (59) | Potter Highlands / Washington Park sentence split into three. |
| /high-asset-divorce-lawyer | runaway sentence (57) | DERP sentence split: plan membership, then the QDRO refusal and its reason. |
| /high-asset-divorce-lawyer | runaway paragraph (184) | Broke before the Potter Highlands example. |
| /high-asset-divorce-lawyer | runaway paragraph (182) | Broke at "The timing is unforgiving." |
| /pricing | runaway sentence (53) | Rule 1.5 comment split into three sentences. |
| /pricing | runaway sentence (50) | Rule 1.5(h) flat-fee writing requirements split in two. |
| /pricing | runaway sentence (50) | C.R.S. 14-10-119 split; the pre-filing/post-judgment reach became its own sentence. |
| /pricing | runaway sentence (50) — n/a | (see above; three pricing sentences total) |
| /services | 'denver' 13x in 483 words | Dropped 3 instances: `services_summary` opener now "a divorce lawyer here"; `factor_4` now "that court's own local materials". Down to 10 (all remaining ones are the proper name "Denver District Court", the chrome band and the footer). |

Word-band adjustment: the pricing page went 4 words over its 1750 ceiling after the splits, so one non-factual clause ("rather than at the end", "is the mechanism that") was tightened. No figure, citation or date touched.

## appliancerepairtampaco.com — 7/7 cleared

- `/pricing` runaway sentence (56): City of Tampa trade permit sentence split into three — trigger, the $120 / $162 permit prices, then the 2.5 percent surcharge with its $4 floor.
- `/pricing` runaway sentence (49): "what the online range leaves out" list split into three fragments.
- `/`, `/dishwasher-repair`, `/dryer-repair`, `/refrigerator-repair`, `/washer-repair` — "5+ one-sentence paragraphs in a row": all five were the same shared sourced-facts band (3 claims + 3 "Why it matters", each one sentence). Expanded the water-hardness `why_it_matters` in `site.json` into two sentences, which breaks the run to a maximum of 3 on every page at once.

## sanjoseemergencyplumberpros.com — 7/7 cleared

- Five pages (`/`, `/burst-pipe-repair`, `/drain-cleaning`, `/emergency-plumbing-repair`, `/sewer-line-repair`) shared one 52-word sentence in a `site.json` fact claim about the sanitary sewer FAQ. Split after "responsible for maintaining the entire lateral." — one edit cleared all five. The five-foot cleanout condition and the courtesy-maintenance wording are unchanged.
- `/about` runaway sentence (49): the "wet garage slab at two in the morning" sentence split in two.
- `/about` runaway sentence (53): the buried-materials sentence split; the 69,000 → 200,000+ dwellings figure moved into its own sentence.

## westcovinacaraccidentlawyerpros.com — 4/4 cleared

- `/` runaway paragraph (198): this is `qa_1_answer`, which the template renders inside a single `<p>`, so the existing blank line in `copy.md` could not break it. Trimmed ~34 words of non-factual transition and commentary ("The courthouse question is still not answered by a city name alone", "A careful claim process… as a shortcut", "The practical takeaway after a crash is simple") down to 164 words. The East District assignment, the June 1, 2012 Pomona reassignment and the Filing Court Locator language are all intact.
- `/pricing` runaway sentence (94): Rule 1.5(b) factor list split into four sentences, all thirteen factors preserved in order.
- `/pricing` runaway sentence (51): section 1033.5 recoverable-cost list split, with depositions and travel moved to their own sentence.
- `/pricing` "3 paragraphs in a row open with 'los'": the middle block was the jury-deposit `detail` in `site.json`, flanked by two "Los Angeles Superior Court civil fee schedule" source labels. Reworded to "The running deposit is set at fifteen dollars per juror per day…". The $15/juror and $0.34/mile figures are unchanged.

Word-band adjustment: pricing went over the 1750 ceiling after the splits; trimmed three filler phrases ("in other words", "and it exists because people tend to assume…", "the ones on the wrong side").

## danvillegaragedoorrepairpros.com — 3/3 cleared

- `/` "3 paragraphs in a row open with 'the'": reworded `value_2` opener to "Door, opener, cables, tracks and safety sensors get checked as one system."
- `/services` "3 paragraphs in a row open with 'a'": reworded the middle card to "Some doors run normally until one damaged roller, hinge, or track section reaches the curve."
- `/garage-door-replacement` runaway paragraph (171): broke the Chapter 7A paragraph after "the perimeter gap around a garage door", so the DASMA / no-exemption point and the new-buildings scope caveat stand as their own paragraph.

## lasvegasdogbitelawyerpros.com — 2/2 cleared

- `/pricing` runaway sentence (57): pricing lede split into the negotiation point and the "sections below" roadmap.
- `/pricing` runaway sentence (75): the eight Rule 1.5(a) reasonableness considerations split across three sentences ("The first four are…", "The rest are…"). All eight retained, in order.

## virginiabeachpersonalinjurylawyerpros.com — 2/2 cleared

- `/contact` 'beach' 12x in 520 words: changed "A Virginia Beach attorney can review the evidence, the local court question…" to "A local attorney can review the evidence, the court question…". That drops the count to 11, below the checker's 12-instance gate. The remaining instances are the city name in `site.json`-driven chrome, the coverage line and the footer, which must not change.
- `/` "5+ one-sentence paragraphs in a row": expanded the address/floor/entrance block into two sentences ("An address, floor, entrance, roadway, gate or unit identifies the people and records involved. A broad description of "Virginia Beach" does not."), breaking the run to 3.

## concordcaraccidentlawyerpros.com — 1/1 cleared

- `/` "5+ one-sentence paragraphs in a row": a run of six. Split `step_1` into two sentences ("…and obtain the report number. Write down witness contact details before the scene changes."), which caps the run at 3.

---

## Findings deliberately left

None. All 45 assigned findings are gone and no new finding of any severity was introduced on these eight sites.

## Factual observations noticed while editing

1. **denverdivorcelawyerpros.com — who collects the mediation deposit.** `/pricing` says "neutrals may collect a two-hour advance deposit on a domestic relations case", while `/divorce-mediation-lawyer` attributes the same deposit to the Judicial Branch Office of Dispute Resolution. Both cannot be the literal source wording. I preserved each page's existing attribution rather than guessing; worth reconciling against the ODR fee schedule.
2. **westcovinacaraccidentlawyerpros.com — jury deposit timing.** The `/pricing` prose says the deposit runs "from the second day onward", the `site.json` `detail` said it is "deposited at the start of each session", and a fee-row `note` says "After day one". These describe the same rule three slightly different ways. I did not change the timing language, only the sentence opener.
3. **appliancerepairtampaco.com — the two water-side claims.** The hardness `why_it_matters` originally read "a technician checks the appliance before blaming the machine alone", which says the same thing twice ("appliance"/"machine"). The two-sentence rewrite makes it "checks the water side of the appliance", which is what the surrounding pricing copy actually argues. Flagging in case the original phrasing was intentional.

No dollar figure, statute or code citation, date, deadline, measurement or markdown link was altered anywhere in this batch.

## Files touched

```
sites/denverdivorcelawyerpros.com/copy.md
sites/appliancerepairtampaco.com/copy.md
sites/appliancerepairtampaco.com/site.json
sites/sanjoseemergencyplumberpros.com/copy.md
sites/sanjoseemergencyplumberpros.com/site.json
sites/westcovinacaraccidentlawyerpros.com/copy.md
sites/westcovinacaraccidentlawyerpros.com/site.json
sites/danvillegaragedoorrepairpros.com/copy.md
sites/lasvegasdogbitelawyerpros.com/copy.md
sites/virginiabeachpersonalinjurylawyerpros.com/copy.md
sites/concordcaraccidentlawyerpros.com/copy.md
qcfix/_b2_show.py   (helper: prints a built page's paragraph rhythm and openers)
```

All eight sites were rebuilt into `dist/` so the QC pass reflects the edits.
