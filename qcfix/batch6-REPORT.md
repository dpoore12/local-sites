# QC flow fixes — batch 6 report

All 8 domains in `qcfix/batch6.md` were edited, rebuilt, and re-checked.
Final state: `template/build.py --check-only` = **[PASS]** on all 8; `qc.py` over the
8 domains = **0 findings** (no MED/LOW/HIGH remaining, none introduced).

| Domain | Findings assigned | Cleared | Left |
|---|---|---|---|
| oceansidepersonalinjurylawyerpros.com | 15 | 15 | 0 |
| tampacriminaldefenselawyerpros.com | 11 | 11 | 0 |
| tampatileroofrepair.com | 6 | 6 | 0 |
| overlandparkgaragedoorrepairpros.com | 4 | 4 | 0 |
| atlantaemergencyplumberpros.com | 3 | 3 | 0 |
| allenacrepairpros.com | 2 | 2 | 0 |
| salinascaraccidentlawyer.com | 2 | 2 | 0 |
| losangelesacinstall.com | 1 | 1 | 0 |
| **Total** | **44** | **44** | **0** |

## What was changed, by domain

### oceansidepersonalinjurylawyerpros.com (copy.md)
- 14 runaway sentences split into two or three sentences each, always at a clause
  boundary that already existed (statute lists, quoted holdings, semicolons):
  home rail-corridor answer; catastrophic page (document-set list, Civ. Code 3333.4,
  Camp Pendleton FTCA/MCA routing); medical-malpractice page (Feres/CRS, 10 U.S.C.
  2733a, Bus. & Prof. Code 6146); pricing page (rule 1.5(b) factor list);
  product-liability page (Greenman, Camp Pendleton claims, CACI 405 / Civ. Code
  1431.2); slip-and-fall page (Ortega, Gov. Code 915, NCTD corridor ownership).
- Runaway paragraph (246 words) on /medical-malpractice-lawyer split at the topic
  shift from active-duty service members to "Dependents, retirees, and civilians."
- Home-page fix note: the checker was reading two sentences as one because the first
  ended with a closing curly quote (`tracks.”`), which its splitter cannot break on.
  Reworded so the quoted label sits mid-sentence.
- Word-band pressure: the catastrophic page (max 1550) and pricing page (max 1750)
  went a few words over after splitting, so three wordy connectors were tightened
  ("The first thing to settle is what the state does not do" → "Start with what the
  state does not do"; "the work actually performed" → "the work performed";
  "The list runs on:" → "Add"). No fact, figure, citation, or link was touched.

### tampacriminaldefenselawyerpros.com (site.json facts, copy.md pricing lede)
- The 86-word bond-schedule sentence and the 57-word Clerk-of-Court sentence lived in
  two `facts[].claim` fields that render on five pages each, so 10 of the 11 findings
  came from two source strings. Each was split into shorter sentences with the
  statute references, charge list, and Administrative Order number intact.
- /pricing 49-word lede split after "never as a share of the result."

### tampatileroofrepair.com (copy.md)
- Six runaway sentences split: F.S. 553.844 exception (pricing and /tile-roof-repair
  SB 4-D version), the leak entry-point list, the slope/underlayment sentence, the
  SB 2-D roof-deductible sentence at 627.701(10), and the 706.7 deck/secondary-water-
  barrier sentence. All percentages, section numbers, and dates preserved verbatim.
- Incidental grammar repair inside the 706.7 split: the original read "roof-decking
  attachment and a secondary water barrier requirements come with it"; the split
  version drops the stray "a".

### overlandparkgaragedoorrepairpros.com (copy.md)
- Three runaway sentences split (permit-exemption list, insulated-section sentence,
  the 1960/1970 population + subdivision sentence). Every population figure, house
  count, street name, and square-footage threshold kept as written.
- Runaway paragraph (186 words) on /garage-door-replacement split before "What the
  code does say is that ordinary repairs need no application" — the natural shift from
  the exemption list to the ordinary-repairs definition.

### atlantaemergencyplumberpros.com (copy.md, site.json)
- Two runaway paragraphs on the home page were FAQ answers (`qa_1_answer`,
  `qa_2_answer`). The template renders each whole answer inside a single `<p>`, so the
  blank line already in the copy does not create a second paragraph — the only way to
  clear the finding was to compress each answer below 170 words. Both were tightened
  by 20+ words of wordy phrasing only; the 387 miles of consent-decree sewer work, the
  January 2026 Georgia Avenue SE sinkhole, the Arborist Meeting requirement, the
  technical-permit and fixture-exemption rules, and the Office of Buildings reference
  all remain.
- /pricing "3 paragraphs in a row open with 'atlanta'": the middle item's `detail`
  field now opens "The city doubles the permit fee…". The $1,000 cap and $50
  reinspection fee are unchanged.

### allenacrepairpros.com (copy.md)
- /ac-refrigerant-leak-repair 71-word EPA/TACL sentence split into three.
- /pricing 51-word "what the online average leaves out" sentence split in two. The
  pricing page then sat 3 words over its 1750 cap, so the trailing filler "in the
  first place" was dropped — no fact removed.

### salinascaraccidentlawyer.com (copy.md)
- /rear-end-collision-lawyer: Route 68 sentence split after "the most common type
  occurring in the project area"; post miles 4.8–13.7, the 2045 delay projection, the
  $189,200,000 estimate, and the March 2028–November 2030 window are untouched.
- /commercial-truck-collision-lawyer: Bulletin 20-07 installation-direction sentence
  split into three (shoulders / rural facilities with the four-foot clearance and
  35 mph threshold / monitoring-program locations).

### losangelesacinstall.com (copy.md)
- Home page had step_1/step_2/step_3 all opening with "The". step_2 now opens
  "An itemized proposal lists…" — same content, different opener.

## Findings deliberately left
None. All 44 assigned findings are gone and no new finding of any severity appears.

## Factual issues noticed while editing
- No incorrect facts found. Two writing defects were repaired in passing, both noted
  above: the stray article in tampatileroofrepair.com's 706.7 sentence ("a secondary
  water barrier requirements"), and a subject/verb mismatch left in place on
  oceansidepersonalinjurylawyerpros.com /catastrophic-injury-lawyer ("the hours a
  husband, a wife, or a grown child now spends"), which I did not change because it
  sits inside the clause I was splitting and rewording it further risked the page's
  1550-word cap.
- Structural note for the portfolio, not a factual error: because FAQ answers render
  inside one `<p>`, any `qa_N_answer` authored as two paragraphs will always be flagged
  as a runaway paragraph. Sites with long two-paragraph FAQ answers will keep
  producing this finding until either the template emits paragraph breaks or answers
  are kept under 170 words.
