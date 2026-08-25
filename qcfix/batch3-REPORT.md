# QC flow fixes — batch 3 report

All 9 domains in `qcfix/batch3.md` (45 assigned findings) are now clean:
`python3 template/build.py --check-only <domain>` prints [PASS] and `python3 qc.py <domain>` reports 0 findings
(no MED, no LOW, no HIGH) for every domain in the batch. Verified individually and in one combined run.

| domain | assigned | cleared | left |
|---|---|---|---|
| losangelesdogbitelawyerpros.com | 18 | 18 | 0 |
| tucsonemergencyplumberpros.com | 8 | 8 | 0 |
| longbeachpersonalinjurylawyerpros.com | 6 | 6 | 0 |
| orlandomovingcompanypros.com | 5 | 5 | 0 |
| garagedoorrepairnapervillepros.com | 3 | 3 | 0 |
| neworleansmotorcycleaccidentlawyerpros.com | 2 | 2 | 0 |
| austinroofinspectionpros.com | 1 | 1 | 0 |
| concordpersonalinjurylawyer.com | 1 | 1 | 0 |
| parkergaragedoorrepairexperts.com | 1 | 1 | 0 |

## What was changed, per domain

### losangelesdogbitelawyerpros.com (18)
- The five "5+ one-sentence paragraphs in a row" findings (home, /child-dog-bite-claim, /dog-bite-injury-claim,
  /dog-bite-insurance-claim, /landlord-dog-bite-liability) all came from the shared sourced-facts block, where three
  one-sentence claims alternate with three one-sentence "Why it matters" lines. Split the second claim in
  `site.json` (`county_dangerous_dog_process`) at the semicolon into two sentences. One edit cleared all five pages.
  No wording, citation, URL or number changed.
- Runaway sentences split on /dog-bite-injury-claim (Civil Code 3342 liability sentence; the 74-word section 3342(b)
  police/military carve-out, now three sentences; the ten-day quarantine sentence), /dog-bite-insurance-claim
  (Business and Professions Code 6147 contract requirements), /landlord-dog-bite-liability (Civil Code 1714 root;
  the 83-word pre-1978 housing sentence, now three sentences; section 53.34.4 dangerous-dog evidence; the license
  conditions list), /pricing (pricing lede; the "thirteen factors" work-itself list).
- Runaway paragraphs broken at topic shifts: the City hearing paragraph on /dog-bite-insurance-claim (break before
  "The Examiner then reports…") and the dangerous-animal paragraph on /landlord-dog-bite-liability (break before
  "A license can be issued or reissued…").
- /contact "'angeles' used 13x": reworded two prose openers ("Los Angeles adds a jurisdiction question" → "This city
  adds…", "For a Los Angeles bite" → "For a bite here"). The remaining mentions are in the brand line, footer,
  trust bar and template-generated coverage sentence, which are name/geography strings and were left alone.
- Two secondary findings my edits introduced were fixed in the same pass: a 174-word paragraph on
  /dog-bite-injury-claim (split before "Subdivision (c)…") and a "3 paragraphs open with 'the'" run on
  /dog-bite-insurance-claim (middle paragraph now opens "City hearing procedure…").

### tucsonemergencyplumberpros.com (8)
- Seven runaway sentences split: /burst-pipe-repair (the "four things" cost sentence), /drain-cleaning (the 74-word
  housing-era sentence, now four sentences; the cost-range sentence), /emergency-plumbing-repair (permit-exemption
  sentence; the 68-word residential-code pan/relief-valve sentence, now three; the pressure-control sentence),
  /sewer-line-repair (permit/2024 IPC sentence). Every figure, code reference and date preserved verbatim.
- /pricing "'tucson' used 34x": replaced seven prose instances with "local", "this city", "here" or "the utility".
  "Tucson Water", "Tucson metro", "Tucson basin", the permit fee schedule name and all source labels were kept
  because they are proper names or citation text.

### longbeachpersonalinjurylawyerpros.com (6)
- Five runaway sentences split: /pricing (33 U.S.C. 928(a) fee sentence), /product-liability-lawyer (933(g)(1)
  settlement-approval sentence; the Cal/OSHA jurisdiction sentence), /slip-and-fall-lawyer (903(a) situs sentence;
  CACI No. 1009B elements sentence).
- /pricing runaway paragraph broken before "Approval is mandatory on every track…".

### orlandomovingcompanypros.com (5)
- Home page: split the hurricane-planning sentence and the crew-sizing/accessorials sentence.
- Home page runaway paragraph: the Q&A answer field renders as a single `<p>`, so a paragraph break there does not
  reach the page. Instead the paragraph was tightened from 176 to under 170 words by removing wordy phrasing
  ("the hardest windows to get in this city" → "the hardest windows here"; "does not make a September move a bad
  idea, but it does change" → "does not rule out a September move, but it changes"). No fact removed.
- /about: split the "lease ending in nine days" sentence and the 61-word "what Orlando actually is" sentence.

### garagedoorrepairnapervillepros.com (3)
- /about and /pricing runaway sentences split.
- /off-track-garage-door-repair "3 paragraphs open with 'a'": middle bolded lead-in changed to "One cable came off
  the drum."
- The pricing split pushed that page 3 words over its 900-1750 band, so two wordy phrases in the permit paragraph
  were tightened ("should be describing" → "should describe"; "the delay of discovering the requirement afterward"
  → "the delay of discovering it afterward"). All dollar figures, the ordinance number and the fee list are intact.

### neworleansmotorcycleaccidentlawyerpros.com (2)
- /lane-change-motorcycle-accident: the flagged 53-word "sentence" was actually two sentences joined by the
  checker, because the first ends in "no." (read as an abbreviation). Reworded the ending to "…frequently that
  there was nowhere", which reads better and removes the ambiguity. Pavement rating, the $5 billion figure and all
  subsidence measurements untouched.
- /uninsured-motorist-motorcycle-claim "3 paragraphs open with 'revised'": middle paragraph now opens "The floor
  for a motor vehicle liability policy sits in Revised Statute 32:900: …" — citation and all limits preserved.

### austinroofinspectionpros.com (1)
- /pricing: split the TREC standards-of-practice sentence after "where it is safe to do so."

### concordpersonalinjurylawyer.com (1)
- /product-liability-lawyer "3 paragraphs open with 'g'" (G.S. citations): middle paragraph now opens "Another bar
  sits in G.S. 99B-3."

### parkergaragedoorrepairexperts.com (1)
- Home "5+ one-sentence paragraphs in a row": the run was the four value cards plus two lead-ins, all template
  fields, so merging paragraphs was not possible. Split `value_2` into two short sentences ("The technician
  inspects the door at the house and explains the fault. You get the number for the repair before the work
  begins."), which varies the rhythm and breaks the run.

## Findings deliberately left
None. All 45 assigned findings are cleared, and no new MED/LOW/HIGH finding was introduced on any of the nine sites.

## Things noticed while editing (not fixed, outside this batch's scope)

1. **Template CTA calls a lawyer a "technician" on every service page.** `template/service.html` line 23-24 hard-codes
   "Call {{ s.phone_display }} and a technician is dispatched with the parts on the truck. You get the price before
   the work starts." That renders verbatim on legal service pages, e.g.
   `/dog-bite-insurance-claim` on losangelesdogbitelawyerpros.com and every page of
   longbeachpersonalinjurylawyerpros.com, neworleansmotorcycleaccidentlawyerpros.com and
   concordpersonalinjurylawyer.com. It is factually wrong copy for a law-firm referral site (no truck, no parts, no
   technician). It is in the shared template, so fixing it touches all 83 sites and was left for the owner of
   `template/`. QC does not flag it.
2. **Word-count bands are tight on pricing pages.** garagedoorrepairnapervillepros.com /pricing was 1748 of a
   1750 maximum before editing, so any sentence split there requires an offsetting trim. Worth knowing for later
   batches.
3. **Checker quirk, not a copy defect:** `qc.sentences()` treats a sentence-final "no." as the abbreviation "No.",
   so two sentences get measured as one runaway sentence (the New Orleans case above). Other batches may hit the
   same false positive.

## Verification commands run
```
cd /home/user/workspace/local-sites
timeout 300 python3 template/build.py --check-only <domain>     # [PASS] for all 9
timeout 300 python3 qc.py <domain>                              # 0 findings for all 9
```
Helper used for the loop: `qcfix/_b3check.sh <domain>` (build check, build, qc, print flow/HIGH rows).
