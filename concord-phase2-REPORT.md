# concordcaraccidentlawyerpros.com — Phase 2 complete

## Build

```
[PASS] concordcaraccidentlawyerpros.com -- home 1610 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           377 words  /about/
          1311 words  /commercial-truck-collision-lawyer/
           553 words  /contact/
          1776 words  /
          1292 words  /injury-claim-negotiation/
          1610 words  /pricing/
          1392 words  /rear-end-collision-lawyer/
           570 words  /services/
          1354 words  /uninsured-driver-claim-lawyer/
```

Pricing landed at 1610 visible words, under the 1750 ceiling; no dollar figure or fee was removed (long pricing sentences were split, not cut).

Files changed: `sites/concordcaraccidentlawyerpros.com/copy.md` and `"phase": 1` -> `2` in that one `site.json`. Nothing else.

## Block word counts (post-edit)

symptom_1 65 / symptom_2 69 / symptom_3 61 / symptom_4 59 (40-80 window)
services_summary 110 · services_pick_head 7 · crosslink_head 5
rear-end lede 35 / body ~864 · uninsured lede 41 / body ~816 · truck lede 39 / body ~769 · negotiation lede 38 / body ~751

## Collision avoidance

`build.py` duplicate-run gate passes: zero shared 15-word runs with any of the 82 other sites, including all six same-niche siblings. Seven passages that initially collided with Modesto and Santa Barbara were rewritten from scratch.

`qc.py` findings reduced to 4 dictionary flags on statutory terms ("prima facie", "nonfleet", "setoff") and one pre-existing home-page list run.

## 3 strongest verified local facts

1. Cabarrus County recorded 5,928 reported crashes in 2023, with 2,125 people injured and 29 killed — NCDOT 2023 Crash Facts, county page: https://connect.ncdot.gov/business/DMV/CrashFactsDocuments/2023%20Crash%20Facts.pdf
2. For race weekends NCDOT plans for heavier volume on I-85, U.S. 29, N.C. 49 and Bruton Smith Boulevard, and states that "Bruton Smith Boulevard often has the most traffic volume because mobile direction services and GPS devices typically direct users to this route" — https://www.ncdot.gov/news/press-releases/Pages/2025/2025-09-29-charlotte-speedway-traffic.aspx
3. For policies new or renewed on or after July 1, 2025, NC minimum liability limits rose from 30/60/25 to $50,000/$100,000 bodily injury and $50,000 property damage, and underinsured motorist coverage is included in all new or renewed policies — https://www.ncdoi.gov/changes-rating-automobile-insurance-policies-effective-july-1-2025 (statute: https://www.ncleg.net/enactedlegislation/statutes/html/bysection/chapter_20/gs_20-279.21.html)

Full source ledger: `concord-phase2-research.md`; raw fetched text in `/home/user/workspace/concord_sources/`.
