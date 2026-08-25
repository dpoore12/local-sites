# QC flow fixes — batch 4 report

All 44 assigned findings across 8 sites are cleared. Every site prints `[PASS]` on
`template/build.py --check-only` and returns **0 findings** on `qc.py` (no new HIGH, MED or LOW).

| Domain | Findings assigned | Cleared | Left |
|---|---|---|---|
| sacramentoacrepair.com | 17 | 17 | 0 |
| cincinnatipersonalinjurylawyerpros.com | 9 | 9 | 0 |
| oxnardcaraccidentlawyerpros.com | 6 | 6 | 0 |
| virginiabeachcaraccidentlawyerpros.com | 5 | 5 | 0 |
| jonesboropersonalinjurylawyerpros.com | 3 | 3 | 0 |
| newportbeachduilawyerpros.com | 2 | 2 | 0 |
| charlotteguttercleaningpros.com | 1 | 1 | 0 |
| denverfurnacerepairpros.com | 1 | 1 | 0 |
| **Total** | **44** | **44** | **0** |

## What changed, per domain

### sacramentoacrepair.com (17)
Most findings were the same two shared blocks repeating across five pages, so two edits in
`site.json` cleared 12 of them.
- `site.json` `local_facts[housing_vintage].why_it_matters`: split the 53-word
  pre-war-housing sentence after "no cooling ducts at all."
- `site.json` `local_facts[permit_rule].claim`: split the 70-word permit sentence into three —
  permit requirement / same-location plus screening rule / landmark-and-historic-district
  exclusion. All citations and the energy-code sentence untouched.
- `copy.md`: split the express-exemption sentence at its semicolon (`qa_1_answer`); split the
  climate-normals sentence after "in a single day" and made the delta breeze its own sentence
  (92.6 / 59.2 figures preserved); split the about-page 54-word sentence; reworked the
  refrigerant-leak lede into three sentences (also moved the closing curly quote off the
  sentence end, which is what kept the checker from seeing two sentences there); split the BLS
  wage sentence ($32.06, 2,940 preserved); split the "what the number found online leaves out"
  sentence and the repair/replacement sentence on `/pricing`.

### cincinnatipersonalinjurylawyerpros.com (9)
- `/slip-and-fall-lawyer`: split the 58-word section 2315.18 damages sentence into three; all
  caps ($250,000 / $350,000 / $500,000) intact.
- `/medical-malpractice-lawyer`: split the 2323.43 cap sentence at the tier change; split the
  Rule 1.5 / 1.5(c)(1) / R.C. 4705.15 sentence into three.
- `/product-liability-lawyer`: split the 60-word 2315.18 sentence into three.
- `/catastrophic-injury-lawyer`: split the 51-word documentation list; broke the 183-word
  tri-state paragraph into two at the topic shift ("A serious crash up there is a Kentucky
  case"), so Ohio-v.-Kentucky geography and Kentucky no-fault law are separate paragraphs.
- `/pricing`: split the eight-factor Rule 1.5(a) sentence 4+4; split Rule 1.5(c)(1) contents
  sentence; split the Hamilton County Civil Rule XVIII fee list after certified mail service
  (every fee amount preserved verbatim).

### oxnardcaraccidentlawyerpros.com (6)
- `/pricing`: split the B&P 6146 quarter/third sentence; split the 6147 contract-contents
  sentence into three; split the small-claims fee sentence after "$12,500 for a natural person."
- `/rear-end-collision-lawyer`: split the comparative-fault sentence at "instead of barring the
  claim."
- `/uninsured-driver-claim-lawyer`: split the 6147 sentence into three.
- `/injury-claim-negotiation`: split the employer-transport sentence at the third-party list.

### virginiabeachcaraccidentlawyerpros.com (5)
- `/`: split the safety-belt sentence ($25 penalty and the no-negligence/no-mitigation/
  not-admissible language kept whole).
- `/` "3 paragraphs open with 'the'": the middle block is `step_2` in `copy.md` — changed
  "The police report, photographs..." to "A police report, photographs...".
- `/pricing`: split the 81-word Rule 1.5 eight-factor sentence into three; split Rule 1.5(c)
  contents sentence; split the Circuit Court fee-component sentence after "writ tax." All
  component amounts ($9, $5, $4, $2, $1, $10) preserved.

### jonesboropersonalinjurylawyerpros.com (3)
- `/pricing`: split the eight-factor Rule 1.5(a) sentence 4+4; split the Article 5, section 32
  sentence after "for injured workers."
- `/product-liability-lawyer` "3 paragraphs open with 'the'": changed the middle paragraph's
  opener to "That same opinion also struck § 16-55-212(b)…" (statute cites unchanged).

### newportbeachduilawyerpros.com (2)
Both findings sat in the same statutory-assessment bullet list on `/pricing`. Merged the
Government Code 70372(a)(1) bullet and the 76104.6 / 76104.7 bullet into one two-sentence
bullet. That single change (a) breaks the run of one-sentence blocks below five and (b) removes
the three-in-a-row "Government" openers. Every per-$10 figure kept exactly as written.

### charlotteguttercleaningpros.com (1)
- `/gutter-repair`: split the 56-word repair-sequence sentence into three (clear and test /
  fall and hangers / miters and outlet). The $40,000 general-contractor license threshold
  sentence was not touched.

### denverfurnacerepairpros.com (1)
- `/furnace-repair` "3 paragraphs open with 'the'": reworded the middle paragraph opener from
  "The work begins with basic conditions:" to "Diagnosis begins with basic conditions:".

## Findings deliberately left
None. All 44 were fixed.

## Factual/editorial observations (not changed — flagging only)
1. **charlotteguttercleaningpros.com `/gutter-repair`** writes the license threshold as
   "40,000 dollars" in prose while the rest of the portfolio uses "$40,000". Style
   inconsistency, not a wrong number — left alone because the instruction forbids altering
   dollar figures.
2. **cincinnatipersonalinjurylawyerpros.com** describes the R.C. 2315.18 unlimited tier as
   "permanent and substantial deformity" on `/slip-and-fall-lawyer` but "permanent and
   substantial *physical* deformity" on `/product-liability-lawyer` and
   `/catastrophic-injury-lawyer`. The statute says "physical deformity"; the slip-and-fall
   wording drops one word. Not a numeric or citation error, so left as-is for a copy owner
   to confirm.
3. **cincinnatipersonalinjurylawyerpros.com `/catastrophic-injury-lawyer`** cites Kentucky
   basic reparation benefits "limited to $500 under 2026 legislation" without naming the bill;
   worth a source check on a future pass, but the figure was left untouched.

## Verification commands run per domain
```
timeout 300 python3 template/build.py --check-only <domain>   # [PASS] on all 8
timeout 300 python3 template/build.py <domain>                # rebuild dist/ so qc sees edits
timeout 300 python3 qc.py <domain>                            # 0 findings on all 8
```
Combined final run: `python3 qc.py <all 8 domains>` → **QC over 8 sites -- 0 findings**.
