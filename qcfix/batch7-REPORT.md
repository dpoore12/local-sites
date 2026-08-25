# QC flow fixes — batch 7 report

All 8 domains edited. **44 of 44 assigned findings cleared, 0 findings remaining** (qc.py reports an empty finding set for all eight domains), and `template/build.py --check-only` prints `[PASS]` for each. No HIGH findings introduced. No dollar figure, statute citation, date, deadline, measurement, or source URL was changed.

| Domain | Assigned | Cleared | Left |
|---|---|---|---|
| fortworthgaragedoorrepairpros.com | 13 | 13 | 0 |
| modestocaraccidentlawyerpros.com | 11 | 11 | 0 |
| atlantadogbitelawyerpros.com | 7 | 7 | 0 |
| houstonmotorcycleaccidentlawyerpros.com | 5 | 5 | 0 |
| austinwrongfuldeathlawyerpros.com | 3 | 3 | 0 |
| carrolltongaragedoorrepairexperts.com | 2 | 2 | 0 |
| sandiegowrongfulterminationlaw.com | 2 | 2 | 0 |
| modestoacrepairpros.com | 1 | 1 | 0 |

## What was changed, by domain

### fortworthgaragedoorrepairpros.com (13)
- `site.json` `housing_vintage` claim (54 words) and `april_2026_hail_outbreak` claim (76 words) split into three sentences each. These two claims render on 5 pages, which accounted for 10 of the 13 findings.
- `copy.md`: opener-electronics sentence (59) split into three; belt-drive/battery-backup sentence (55) split at the concession; pricing "what the online average leaves out" sentence (62) split in two.
- Pricing page tripped the 1750-word ceiling after the split, so "It also leaves out lead time." became "Lead time is missing too." No facts removed.

### modestocaraccidentlawyerpros.com (11)
- Six runaway sentences split: Government Code 835 elements (63), uninsured-motorist trigger (55), Rule 1.5(a)/BPC 6147 paperwork (55), pricing lede (50), Li v. Yellow Cab passage (61), rear-end fee passage (50).
- The Li v. Yellow Cab sentence was long only because the checker cannot split after a quotation that ends a sentence (`justice." So expect…`). Reordered to `In Li v. Yellow Cab Co., the court called … "…fundamental justice," and that decision is where the instruction comes from.` Quote text unchanged.
- Five "5+ one-sentence paragraphs in a row" findings all came from the sourced-facts block (claim / why-it-matters pairs, each one sentence). Split the second `why_it_matters` into two sentences ("…which limits are relevant. A minimum limit is not a measure of the full loss.") which breaks the run on all five pages. The home page also had a run through the value blocks, fixed by making `value_1` two sentences.

### atlantadogbitelawyerpros.com (7)
- `site.json` DeKalb leash-code claim (60 words, on 5 pages) split at the semicolon into two sentences.
- /contact: three paragraphs opening "Keep" — middle one now opens "Hold on to treatment papers…".
- /pricing: four paragraphs opening "Rule" — the 1.5(c)(1) paragraph now opens "The provision worth reading before signing anything is Rule 1.5(c)(1)."

### houstonmotorcycleaccidentlawyerpros.com (5)
- Rule 1.04(b) eight-factor sentence (80) split into a lead-in plus two grouped sentences; paragraph (d)/(e) sentence (53) split; Property Code 55.004(b) three-part lien cap (59) split into three sentences with all three limbs intact.
- Home page: middle of three "Texas…" paragraphs reworded to "Recovery is barred under Texas Civil Practice and Remedies Code §33.001 when…".
- /lane-change-motorcycle-accident: middle of three "A…" paragraphs now opens "Riders also go down while avoiding a vehicle that never makes contact."
- Pricing exceeded the word ceiling after the splits; trimmed wording only (dropped "there is", "meaning", "in any accounting"; "Whether more exists depends on" → "More may exist through"). All figures and citations intact.

### austinwrongfuldeathlawyerpros.com (3)
- /pricing lede (65) split after "…governs the arrangement."
- Both "3 paragraphs open with 'a'" findings (home and /services) came from the same shared block; middle paragraph now opens "Much of what decides a case sits outside the family: …".

### carrolltongaragedoorrepairexperts.com (2)
- /pricing 87-word list sentence split into three sentences, every excluded cost item preserved.
- /garage-door-spring-repair: the 49-word "sentence" was two sentences the checker merged because the first ended in "no." (read as the abbreviation "No."). Reworded to "…and the honest answer is that it does not." so the break registers; meaning unchanged.

### sandiegowrongfulterminationlaw.com (2)
- Labor Code 218.5(a) fee sentence (49) split before the exception.
- Tameny passage (59): same quotation-end merge problem. Recast as "The refusal branch comes from the state Supreme Court's decision in Tameny v. Atlantic Richfield Co., which held that … 'to further its interests' ([Tameny](https://law.justia.com/cases/california/supreme-court/3d/27/167.html))." **Note:** the `[Tameny]` markdown link now sits at the end of the first sentence instead of the second, one sentence earlier in the same paragraph. Anchor text and URL are byte-identical; nothing else about the citation changed. Flagging it because it is the only link relocation in the batch.

### modestoacrepairpros.com (1)
- /pricing changeout-estimate sentence (56) split in two; every line item kept. Word ceiling then required three small trims elsewhere on the page (rebate sentence, leak-search sentence, oversell opener) — no figures, permits, or rebate amounts touched.

## Findings deliberately left
None. Every assigned finding is cleared.

## Factual issues noticed while editing
No factual errors found. Two observations worth a second look by whoever owns the copy (neither touched):
- modestoacrepairpros.com /pricing: "That is larger than most Texas or Arizona cities charge" is an unsourced cross-state comparison sitting next to sourced Modesto permit figures ($242 HVAC replacement, $139 water heater).
- modestocaraccidentlawyerpros.com /injury-claim-negotiation still carries a near-48-word Li v. Yellow Cab sentence (47 words by the checker's count) that survives only because it is one word under the threshold. It reads fine, but it is fragile if that block is ever re-edited.
