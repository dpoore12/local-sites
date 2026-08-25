# QC flow fixes — batch 5 report

44 findings across 8 sites. **All 44 cleared. 0 findings left, 0 HIGH introduced.**
Final state: `python3 template/build.py --check-only` prints [PASS] for all 8 domains, and
`python3 qc.py <domain>` returns 0 findings for all 8.

---

## sandiegodogbitelawyerpros.com — 16 / 16 cleared
- The two most-repeated runaway sentences lived in `site.json` sourced facts, so each
  fix propagated across all five pages that render them (10 of the 16 findings).
  - `county_bite_reporting` claim (52 words) split into three sentences: the reporting duty,
    the list of people it names, then the 24-hour violation. Statute cite 62.615 untouched.
  - `grand_jury_bite_data` claim (59 words) split after "the 2020 to 2022 period"; the
    40 percent / under-reporting material became its own sentence. All figures kept.
- `/pricing`: 63-word lede split at "California fixes no number for that share."
- `/pricing`: 78-word Rule 1.5(b) sentence rewritten as three sentences ("start with… /
  They take in… / They also cover…"), all thirteen considerations preserved.
- `/pricing`: 52-word section 6146(a) sentence split into three; 25 percent, 33 percent
  and the 6146(a)(3) good-cause motion all kept verbatim.
- `/` 3 paragraphs opening with "a": middle paragraph reopened as "Familiar dogs can still…".
- `/about` and `/contact` "diego" overuse: the shared closing CTA now reads "For a local
  dog-bite inquiry". That single change took /about to 11 uses and /contact to 13 (2.2%),
  both under threshold. Remaining uses are the brand line, the coverage line and the
  disclaimer, which are city/state authority text in `site.json` and were not touched.

## arlingtonbathroomremodelingpros.com — 9 / 9 cleared
- `/bathroom-remodel`: 50-word Houston Black clay sentence split after "Grand Prairie clay";
  crack widths, depths and the 90–150 day figure preserved.
- `/bathroom-remodel`: 49-word bid-contents sentence split into two ("It also names…").
- `/bathtub-replacement`: 57-word replacement-criteria sentence split into two.
- `/bathtub-replacement` 3 paragraphs opening with "the": the one-bathroom paragraph now
  opens "Almost 40 percent of houses in the Heart of Arlington plan area…"; the 40 percent
  figure and the source attribution are intact.
- `/pricing`: 55-word exclusions sentence split into two.
- `/pricing` 3 paragraphs opening with "the": the second scope driver now opens "Second:".
- `/shower-remodel`: 50-word TCNA EJ171 sentence split; the twenty-five foot and eight-to-
  twelve foot spacings and the perimeter soft joint all kept.
- `/walk-in-shower-installation`: 53-word Texas plumbing-license sentence split into two.
- `/contact` 5+ one-sentence paragraphs: the "Scope before selections" item gained a short
  second sentence, breaking the run into 2 + 2. No new facts added.

## foundationrepairaustinco.com — 7 / 7 cleared
- `/basement-waterproofing`: 50-word below-grade drainage sentence split ("Other options are…").
- `/crawl-space-repair`: 49-word NRCS soil-group sentence split after "shed rather than absorb".
- `/foundation-crack-repair`: 52-word USGS Del Rio / Taylor beds sentence split; 80–100 feet
  and roughly 540 feet preserved.
- `/foundation-crack-repair`: 52-word injection sentence split into two.
- `/house-leveling`: 65-word Texas Engineering Practice Act sentence rewritten as three
  sentences (exemption / what it does not cover / the IRC expansive-soil standard).
- `/house-leveling`: 49-word DTPA sentence split; the 60-day notice and treble damages kept.
- `/pricing`: 52-word ASCE Version 2 sentence split into two.
- Note: the pricing page tripped the 1750-word ceiling on the first pass at 1751 words.
  Trimmed three words of connective tissue ("They add that") — no fact removed.

## modestopersonalinjurylawyerpros.com — 4 / 4 cleared
- `/product-liability-lawyer`: 61-word Johnson / Webb sentence split into three; the
  sophisticated-user and sophisticated-purchaser holdings and the "general awareness is not
  knowledge of the specific hazard" qualifier all preserved.
- `/product-liability-lawyer` 172-word paragraph broken at "Component makers have their own
  shelter", the natural shift from sellers to component makers.
- `/slip-and-fall-lawyer` 194-word paragraph broken before "It does not always work that way",
  separating the Huckey factors from the Stack v. City of Lemoore counterexample.
- `/slip-and-fall-lawyer` 172-word paragraph broken before the Streets and Highways Code
  section 5610 sentence, splitting "who is the defendant" from the notice and immunity rules.

## annarborgaragedoorrepairpros.com — 3 / 3 cleared
- `/garage-door-opener-repair`: 54-word permit sentence split; the $100 first tier, the
  nonrefundable $15 base fee and the $35 re-inspection fee kept exactly.
- `/off-track-garage-door-repair`: 56-word IRC adoption sentence split after the
  February 8, 2022 effective date; R 408.30500, Table R301.2(5), 20 psf and 25 psf all kept.
- `/pricing`: 57-word exclusions sentence split into two ("Nor do they cover…").

## sandiegoleakdetectionpros.com — 3 / 3 cleared
- `/pricing`: 51-word hourly-model sentence split into three; $129, $199, $218, $238 and the
  $367 total kept.
- `/pricing`: 54-word leak-adjustment sentence split into three; the 120-day deadline and the
  eight-to-ten-week review kept.
- `/underground-leak-detection`: 52-word council-policy sentence split into two; every listed
  category of assistance preserved.

## coloradospringsfurnacerepair.com — 1 / 1 cleared
- `/pricing`: 54-word estimate-contents sentence split into two ("It also states where the
  condensate goes…"). The $900 ENERGY STAR rebate line was not touched.

## fresnowrongfuldeathlawyerpros.com — 1 / 1 cleared
- `/about`: 49-word sentence split; the wrongful death / survival action distinction and the
  B. F. Sisk Courthouse reference stay in the first sentence, the local-economy material moved
  to a second.

---

## Findings deliberately left
None. All 44 assigned findings are gone.

## Factual issues noticed while editing
No factual errors found. Two things worth flagging to the parent agent, neither changed:
1. **arlingtonbathroomremodelingpros.com** — the tub page cites InterNACHI life expectancy
   for cast iron tubs as "a hundred years" while the same page's drain discussion cites
   cast iron *waste pipe* at 50–60 years. Both are plausibly correct (different products),
   but the two numbers sit close together and a reader may read them as contradictory.
2. **sandiegodogbitelawyerpros.com** — `/about` and `/contact` still carry a high density of
   "San Diego" purely from template furniture (brand line, coverage line, disclaimer, the
   "Written for San Diego · San Diego County" trust strip renders twice per page). Those are
   `site.json` city/state authority text, so the only durable fix would be a template change,
   not a copy change. Both pages are now under the QC threshold regardless.
