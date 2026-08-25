# phoenixleakdetectionpros.com — Phase 2 completion report

## Build result

```
[PASS] phoenixleakdetectionpros.com -- home 1748 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           348 words  /about/
           580 words  /contact/
          1916 words  /
          1368 words  /pool-leak-detection/
          1748 words  /pricing/
           573 words  /services/
          1405 words  /slab-leak-detection/
          1405 words  /underground-leak-detection/
          1355 words  /water-leak-detection/
exit=0
```

`site.json` `"phase"` is now `2` (nothing else in site.json changed). Pricing came in over the 1750 ceiling twice (1794, then 1766) and was trimmed to 1748 by tightening prose only — every dollar figure and fee is intact ($6.13/100 cf June–Sept, 748 gal, 60-day sewer review, $195 minimum residential permit fee + $195 per re-inspection, $4,000–$24,000 repipe range).

`qc.py` after rebuild: 11 findings, 0 flow, 0 markup. The 5 HIGH "review/rating claim" hits are all one false positive — the site-wide sourced fact from `site.json` about the City's **Sewer Fee Review**, repeated in the facts strip on 5 pages. It is a government program name, not a rating claim, and it lives in site.json which I was told not to edit beyond `phase`. The 6 MED are spelling-dictionary misses on legitimate trade terms: geotechnical, subgrade, unbonded, backfills, correlator, paver.

## What was written

- `symptom_1`–`symptom_4` rewritten to 58 / 59 / 56 / 55 words (titles and order untouched).
- New `services_summary` (98 w), `services_pick_head` ("Start with the water loss you can actually see"), `crosslink_head` ("Another kind of water loss?").
- Four `svc_*_lede` + `svc_*_body` sets, 7 `###` sections each, using the exact site.json slugs: `water-leak-detection`, `slab-leak-detection`, `underground-leak-detection`, `pool-leak-detection`.
- Differentiator carried through the whole site: the post-tensioned slab as the constraint that decides whether concrete can be opened at all; caliche and subsidence as the reason buried pipe fails and the reason trenching is expensive; the meter as the boundary of financial responsibility.
- Sources are named in prose inside the bodies (city code section numbers, code sections 1907.5 / 1803.5.13, ARS sections, USGS, UA Extension, NWS), matching sibling-site style; no markdown URLs in body copy.

## 3 strongest verified local facts

1. **Post-tensioned slabs are written into Phoenix's own building code, with the injury risk stated.** The 2024 Phoenix amendments require every post-tensioned slab on ground to be permanently stamped or marked in a conspicuous location (entrance porches, slab at garage doors, patio slabs), because "many structures have been, and continue to be, constructed with post-tensioned slabs on ground," "if a tendon is cut throughout the life of the structure, it can cause serious injury," and the stamp lets a contractor "identify tendon locations before cutting or drilling into the slab." §1803.5.13 also requires a geotechnical investigation and expansive-soil values em/ym on the drawings. Adopted by Ordinance G-7397, effective August 1, 2025.
   https://www.phoenix.gov/content/dam/phoenix/pddsite/documents/codes-ordinances/amendmentcodes/2024-ibc.pdf
   https://www.phoenix.gov/administration/departments/pdd/tools-resources/codes-ordinance/building-code.html
2. **The money fact: the customer owns every gallon lost past the meter, and the boundary is defined.** City Code 37-27 makes each customer responsible for all leaks downstream of the point of service delivery and for full payment for water lost, requires pipes/valves/sprinklers to be kept in good repair, and allows termination after 10 days' written notice. Code §37-1 defines "point of service delivery" as the terminal end of the service connection — where a meter exists, the downstream (customer's) side of the meter.
   https://phoenix.municipal.codes/CC/37-27
   https://www.phoenix.gov/content/dam/phoenix/pddsite/documents/trt/external/dsd_trt_pdf_00634.pdf
3. **Renters have a defined, dollar-bounded self-help remedy.** ARS 33-1324 requires the landlord to maintain plumbing in good and safe working order and supply running water at all times; ARS 33-1363 permits tenant self-help where the cost is under $300 or half of one month's rent, whichever is greater, after written notice and ten days, with work done by a licensed contractor and deduction after an itemized statement and waiver of lien.
   https://www.azleg.gov/ars/33/01324.htm
   https://www.azleg.gov/ars/33/01363.htm

Supporting: caliche as calcium-carbonate-cemented soil, loose lumps to layers several feet thick, restricting drainage (UA Extension az1281, https://extension.arizona.edu/publication/managing-caliche-home-yard); West Salt River Valley declines over 50 ft (locally 300+), compaction/subsidence up to 18 ft east of the White Tank Mountains by 1995, silt/clay lenses over 80% fine near Goodyear and Glendale (USGS PP1781 §7, https://pubs.usgs.gov/pp/1781/pdf/pp1781_section7.pdf); earth fissures in Maricopa County (AZGS, https://azgs.arizona.edu/earth-fissures-ground-subsidence/more-arizonas-earth-fissures); monsoon season officially June 15–September 30 (NWS Phoenix, https://www.weather.gov/psr/monsoonawarenessweek); ~6 ft/yr average evaporation around Phoenix and Tucson, roughly a 16,000-gallon pool per year (https://www.arizonawaterfacts.com/tips-resources/be-cool-your-pool); ARS 32-1121(A)(14) licensing exemption capped at $1,000 and void whenever a local building permit is required (https://www.azleg.gov/ars/32/01121.htm).

## Errors found in the brief

1. **There is no City of Phoenix water leak adjustment or high-bill credit program.** The brief called it "a concrete, verifiable money fact." It does not exist. Code 37-27 assigns all downstream loss and full payment to the customer. The only published adjustment is the **Sewer Fee Review** (sewer recalculated each July from average Jan–Mar use; requests more than 60 days after the July bill date are ineligible; prior years are not adjusted) — https://www.phoenix.gov/administration/departments/waterservices/city-services-bill/submit-a-sewer-fee-review.html. site.json already says "No forgiveness," so **site.json wins** and the copy states plainly that no forgiveness program exists to apply for.
2. **No primary source supports a percentage of Phoenix homes on post-tensioned slabs, or a build-year cutoff.** I used the city amendment's own wording ("many structures have been, and continue to be, constructed with post-tensioned slabs on ground") instead of inventing a share.
3. **No government source quantifies under-slab copper failure rates or attributes them to flux or soil chemistry.** Those mechanisms are described qualitatively (hardness range from the city's own report, thermal cycling, expansive/cemented subgrade) with no invented numbers.
4. **Phoenix publishes no plumbing spot-repair-versus-repipe permit threshold.** I used the verifiable rules instead: a permit is required to move or add fixtures but not to replace existing ones, the $195 minimum residential permit fee, and ARS 32-1121's permit trigger for licensing.

## Collision avoidance

The 15-word shingle check in `build.py` against all 82 sibling sites passes. Tucson (same state, same trade family) was read closely; its Arizona statute, ROC and caliche phrasing was deliberately not reused — Tucson covers caliche/monsoon/meter boundary via Tucson Water and AAC R18-5-101, while this site is built on the post-tensioned slab and Phoenix City Code 37-1/37-27, which Tucson does not touch.
