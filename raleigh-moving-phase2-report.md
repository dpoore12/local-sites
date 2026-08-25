# Phase 2 conversion report — raleighmovingcompanypros.com

## Build result

```
[PASS] raleighmovingcompanypros.com -- home 1745 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           334 words  /about/
          1351 words  /apartment-moving/
           595 words  /contact/
          1713 words  /
          1446 words  /local-moving/
          1442 words  /long-distance-moving/
          1339 words  /packing-services/
          1745 words  /pricing/
           524 words  /services/
EXIT=0
```

Full-corpus run (`python3 template/build.py --check-only`, all sites) also reports
`[PASS] raleighmovingcompanypros.com` with **no 15-word shingle collisions** against any sibling,
including the Orlando moving site, both Concord legal sites, Charlotte gutter cleaning, Houston
motorcycle and Birmingham truck. (An unrelated pre-existing failure exists on
jonesboropersonalinjurylawyerpros.com; untouched.)

## Files changed

- `sites/raleighmovingcompanypros.com/copy.md` — symptom_1..4 trimmed to teasers (59/48/52/51 words);
  8 new blocks added (`svc_local_moving_lede/_body`, `svc_long_distance_moving_lede/_body`,
  `svc_apartment_moving_lede/_body`, `svc_packing_services_lede/_body`); light prose trims to
  `pricing_body` to hold the 1750 ceiling after phase-2 chrome was added (no dollar figure or fee
  removed — verified by diffing the dollar-token list before and after).
- `sites/raleighmovingcompanypros.com/site.json` — `"phase": 1` → `"phase": 2` only.

Authored block word counts: local-moving body 894, long-distance 895, apartment 807, packing 795;
ledes 44 / 39 / 37 / 40. Each body carries 7 `###` subheads.

Research notes with every URL: `raleigh-moving-phase2-research.md`.
Draft of the appended blocks (kept for reference): `svc_blocks_raleigh.md`.

## Three strongest verified local facts

1. **North Carolina's overage cap is 120 percent, and it has two exceptions that void it.**
   Maximum Rate Tariff No. 2, Rule 13: "the final billed charges shall not exceed 120% of the
   estimate amount" absent a signed change order, but the requirement does not apply if the estimate
   is requested fewer than **5 business days** before the move or the shipment is under
   **1,000 pounds**. Rule 15 binding not-to-exceed estimates were retired effective **1-1-2026**.
   https://www.ncuc.gov/industries/documents/maxrate.pdf
   The federal counterpart for an interstate move is **110 percent**, plus a duty to relinquish the
   shipment on payment of that amount — 49 CFR 375.405(b)(5) and 375.407(a).
   https://www.ecfr.gov/current/title-49/part-375

2. **A missing signature converts the coverage.** Tariff Rule 7(E): if the carrier fails to obtain
   the shipper's signature in the valuation section, the shipment is deemed released to coverage of
   up to **$15,000 at no additional cost**. Default liability otherwise is **60 cents per pound**
   per damaged article, which the tariff itself illustrates with a 50-pound, 65-inch television
   worth **$30**. https://www.ncuc.gov/industries/documents/maxrate.pdf

3. **Raleigh's curb rule is narrower than "you need a permit."** A right-of-way permit is required
   to occupy the street, sidewalk or sidewalk shoulder, but a moving-van parking pass is obtained
   **directly from Raleigh Parking** and, for timed or paid spaces, picked up at 310 W. Martin
   Street and displayed for the duration.
   https://raleighnc.gov/permits/services/right-way-occupancy
   Meters are paid 8 a.m.–6 p.m. weekdays downtown (8 a.m.–8 p.m. in the Hillsborough district),
   free on weekends, but **enforcement runs 24 hours every day**; a meter violation is $20 with a
   $20 late fee after 21 days.
   https://raleighnc.gov/parking/services/parking-customer-service/parking-frequently-asked-questions

Runner-up worth keeping: Wake County reached **1,257,235** on July 1, 2025, up **27,760** in a year
and **5th** in the nation for numeric growth; the Raleigh-Cary metro hit **1,595,720**, up
**2.4 percent**, 10th nationally by rate.
https://www.census.gov/newsroom/press-releases/2026/2025-popest-metro-micro-counties.html

## Where the brief was wrong or imprecise

1. **"Maximum Rate Tariff No. 2" is right; the estimate rule is not the federal one.** The brief
   called the estimate overage limit "the rule limiting what a mover may collect above an estimate."
   In North Carolina intrastate that number is **120 percent** (tariff Rule 13), not the widely
   quoted federal **110 percent** (49 CFR 375.407). Both are on the site, contrasted deliberately.

2. **The NCUC's own consumer page is stale and contradicts the tariff.** The HTML "Moving 101" page
   at https://www.ncuc.gov/industries/transportation/movingguide.html still shows superseded figures
   — $0.75 per $100 full value protection, a $4.00-per-pound minimum, 500-pound and 35/36-mile
   thresholds, and phone 919-733-7766. The current PDF
   (https://www.ncuc.gov/industries/documents/moving.pdf) and Tariff No. 2 give $1.00 per $100,
   $5.00 per pound, a 1,000-pound threshold, a 50-mile threshold, and 919-733-4036. Nothing from the
   HTML page was used.

3. **Claim timing differs by rulebook, not by carrier.** The brief asked for the federal 30-day
   acknowledgment and 120-day resolution (49 CFR 370.5, 370.9), which is correct for interstate. NC
   intrastate is **15 days to acknowledge and 60 days to resolve** under tariff Rule 52, with a
   9-month filing window and suit within 2 years and 1 day of a written denial. The site states both.

4. **Raleigh publishes no moving-van pass fee or lead time.** The city documents the process and the
   display requirement only; construction-vehicle permits are priced as days requested × the daily
   rate of each space. No fee figure was invented — the copy describes the process.
   Also, the brief's premise that the city requires a permit "for parking a moving truck" is only
   partly true: an ordinary truck in an unrestricted residential space needs neither a pass nor a
   right-of-way permit.

5. **NC uses two names for the same authority.** The statute and Commission pages refer both to a
   "certificate" (a C-number under Commission Rule R2-37, G.S. 62-262) and to a "certificate of
   exemption" (G.S. 62-261(8), the tariff's own bill-of-lading requirement in Rule 28). The copy
   uses both carefully rather than picking one.

6. **Hurricane-remnant rain was verifiable only as an event, not a normal.** No NWS Raleigh page
   states an average tropical-remnant rainfall figure, so the site cites the office's post-tropical
   cyclone report for Tropical Storm Ophelia (September 22–23, 2023: 3.66 inches at a gauge 4.5 miles
   NNW of Raleigh, 3.53 inches at the Lake Wheeler Road field lab) instead of a manufactured average.
   https://www.weather.gov/media/rah/TropicalEventSummary/PSHRAH_2023AL16_Ophelia_Summary.pdf

7. **site.json vs. brief:** no conflict found. City, state, county, the four slugs, the neighborhood
   list and the three local_facts were used exactly as site.json has them, and site.json's own NCUC
   and Raleigh right-of-way facts match what was verified from primary sources.

## Notes on tooling

- Census QuickFacts returns Access Denied to fetches and api.census.gov requires a key; the Vintage
  2025 press release was used instead.
- eCFR HTML section pages return navigation text only. The versioner API works:
  `curl -sL "https://www.ecfr.gov/api/versioner/v1/full/2026-08-01/title-49.xml?part=375"`.
