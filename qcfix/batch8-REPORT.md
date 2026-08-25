# QC flow fixes — batch 8 report

Assigned: 44 flow findings across 8 sites (`qcfix/batch8.md`).
Result: **44 of 44 cleared. 0 findings remain on all 8 sites. All 8 sites `[PASS]` on `template/build.py --check-only`.**

Verification artifacts: `qcfix/batch8-before.csv` (44 rows), `qcfix/batch8-after.csv` (header only — no findings).
Helper used while editing: `qcfix/_b8_scan.py` (lists sentences over N words in a site's `copy.md` / `site.json`).

## Per domain

### orlandoduilawyerpros.com — 12 assigned, 12 cleared
All 12 were runaway sentences (49–69 words) in `copy.md`, split into two or three sentences each:
- `/dui-breath-test-defense` x4 — implied consent under 316.1932, the pre-test warning, the 316.1934 affidavit checklist, the FDLE records list.
- `/dui-license-suspension` x1 — the questions the hearing officer decides.
- `/felony-dui-defense` x3 — subsection (2)(b)2 penalties, the downtown courthouse description, the second-conviction revocation ladder.
- `/first-offense-dui-defense` x2 — the 316.193(1) definition, the Orange County bond payment methods.
- `/pricing` x2 — the Fla. Stat. 938.07 cost destinations, the department's revocation timeline.
Note: splitting sentences pushed `/pricing` to 1753 words against a 1750 max, so three wordy phrases were tightened (`Of that total` → `Of that`; `which is the figure that appears when` → `the figure appearing when`; `has to be finished` → `must be finished`). No dollar figure, statute cite, date or deadline was touched.

### santabarbaracaraccidentlawyer.com — 12 assigned, 12 cleared
All 12 were runaway sentences (50–76 words), all in `copy.md`; every markdown link and URL preserved intact:
- `/pricing` x2 — the thirteen Rule 1.5(b) factors (split mid-list), the section 6146 percentage ceiling.
- `/rear-end-collision-lawyer` x4 — the four named collision segments, the Government Code 911.2/945.6 pairing, the CHP report-request sentence, Rule 1.5.
- `/injury-claim-negotiation` x3 — pure comparative fault after Li v. Yellow Cab Co., the Civil Code 3040 lien cap, Rule 1.5.
- `/uninsured-driver-claim-lawyer` x2 — Insurance Code 11580.2, the two-year trigger.
- `/commercial-truck-collision-lawyer` x1 — Vehicle Code 34501.12 terminal identification.
Again the `/pricing` page ran 1 word over its band after splitting, fixed with two one-word trims (`It rises to` → `It is`; `The list continues with` → `The others are`).

### bellevuebathroomremodeling.com — 7 assigned, 7 cleared
- 6 runaway sentences (50–62 words) split: `/bathtub-replacement` x3 (when replacement beats refinishing, getting a cast-iron tub out, what is behind the surround), `/pricing` x1 (what a usable bid spells out), `/shower-remodel` x1 (assembly-failure symptom list), `/walk-in-shower-installation` x1 (the Sarpy County radon figures and slab sealing).
- `/contact` LOW "5+ one-sentence paragraphs in a row": broke the run by splitting the `expect_1` block ("The initial review covers…") into two sentences, so the run is now 1 + 3 rather than 5. No new facts added.

### mckinneygaragedoorrepairpros.com — 5 assigned, 5 cleared
- `/about` 81-word sentence split into three (the hardware inventory behind the city's garage doors).
- `/services` 57-word semicolon chain split into three sentences (Stonebridge Ranch / downtown outbuilding / hail-damaged door).
- `/pricing` 49-word sentence split before the BLS wage figure.
- `/garage-door-replacement` "3 paragraphs open with 'the'": middle paragraph reopened as "A door's weight matters as much as its fit."
- `/pricing` "3 paragraphs open with 'prosper'": the run was three *identical* source labels ("Prosper Door Repair, McKinney, posted price list, read 2026-08-23") on three different URLs in `site.json`. Relabelled two of them to name the page each URL actually is ("Opener price list posted by…", "Panel replacement price list from…"). Company name, city and read date preserved on all three; no URL changed.

### birminghamtruckaccidentlawyerpros.com — 3 assigned, 3 cleared
- `/delivery-truck-accident-lawyer` 195-word paragraph split at the natural topic shift, right before "That ordinance describes the streets where most of these collisions happen." Ordinance subsections stay in paragraph one; the historic-district listings stay in paragraph two.
- `/pricing` x2 runaway sentences: the nine Rule 1.5(a) factors split across two sentences (four then five), and Ala. Code 25-5-90(a) split after the judge-approval clause.

### friscogaragedoorrepairexperts.com — 2 assigned, 2 cleared
- `/off-track-garage-door-repair` "3 paragraphs open with 'the'": middle paragraph reopened as "Shortcuts on this repair are recognizable."
- `/pricing` "3 paragraphs open with 'prosper'": two identical "Prosper Garage Door Repair, Plano, posted opener price page" labels relabelled to "Opener price page posted by Prosper Garage Door Repair, Plano, read 2026-08-23". Read date and URLs unchanged.

### sanjosemovingcompanypros.com — 2 assigned, 2 cleared
- `/local-moving` "3 paragraphs open with 'item'": the middle paragraph now opens "Under Item 104 a mover may collect before releasing the load…" so the run is Item 128 / Under / Item 88.
- `/apartment-moving` 51-word sentence split at the colon (interstate mechanism vs. the in-state change-order rule).

### sanjoseduilawyerpros.com — 1 assigned, 1 cleared
- `/pricing` "3 paragraphs open with 'government'": the run was three bullets in the assessments list. Middle bullet reworded to "Sections 76104.6 and 76104.7 of the Government Code add $1 and then $4 per $10 for DNA identification funding." Both code sections and both dollar amounts preserved.

## Findings deliberately left
None. All 44 assigned findings are cleared and no new finding of any severity was introduced on the 8 sites.

## Factual errors noticed while editing
No factual error found. Two things worth a second pair of eyes, neither changed by me:

1. **orlandoduilawyerpros.com `/dui-breath-test-defense`** — after the 316.1934 affidavit list, the next sentence reads "Each of those five items points at a separate record." The statutory list as written on the page can be read as five or six items depending on whether "the type of test and the procedures followed" is counted as one item or two. I split the list into two sentences but left "five" alone rather than guess at the count.
2. **bellevuebathroomremodeling.com `/walk-in-shower-installation`** — the radon figure is cited two ways on the site: "5,649 tests between October 2019 and September 2024" on `/pricing` and "5,649 tests through September 2024" here. Same source and same number, just a shorter window description in one place. Not an error, but the fuller phrasing is the clearer one if anyone standardises it later.

## Rules honoured
- No dollar figure, statute or code citation, date, deadline, or measurement was altered, rounded, or dropped.
- No markdown link or source URL was changed; link text was only moved across a new sentence boundary.
- No new facts introduced; every rewrite reshapes text already on the page.
- City and state names left exactly as `site.json` has them.
- No new sentence exceeds 44 words; no heading was touched; no bare decimal, doubled word, or trailing period on a single-sentence heading introduced.
