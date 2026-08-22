# Writer report — annarborgaragedoorrepairpros.com

**Scope:** Phase 1 garage door repair site for Ann Arbor, Michigan. Written 2026-08-21.

## Three sourced local facts

1. **Winter deicing exposure.** Ann Arbor says its Priority 1 and 2 routes cover 346 lane miles and are treated with anti-icing agents, plowing and salt to bare pavement; it also provides residents up to five gallons of sand/salt mix per winter visit. This supports the local materials angle: wet deicing residue is a sensible reason to inspect lower brackets, rollers, cables and vertical track closely when the lower door is rusty or noisy.  
   URL: https://www.a2gov.org/public-works/street-maintenance/street-snow-removal/

2. **Historic-district review.** The city says all exterior work in historic districts is regulated by the Historic District Commission and requires an application and approved Certificate of Appropriateness. It specifically directs people considering changes to existing accessory structures to check with staff on required review. A repair is therefore kept distinct from a visible door or material replacement in the copy.  
   URL: https://www.a2gov.org/planning/historic-preservation/applications/

3. **Rental housing and U-M context.** The City of Ann Arbor Downtown Housing Needs Assessment reports 76.7% renter occupancy in the 2020 downtown study area and 54.1% in the surrounding primary study area. It also explains the DDA district includes U-M Central Campus and cites nearly 48,000 U-M students in Ann Arbor in fall 2020. This supports the central split-reader scenario: the tenant reporting a failed door is frequently not the owner or manager authorizing the repair.  
   URL: https://www.a2gov.org/media/oo1kzbww/ann-arbor-mi-downtown-housing-needs-assessment.pdf

## Angle used

This site is deliberately about **road-salt residue as a lower-door materials problem**, not winter temperatures or cold-snap spring failure. The copy follows corrosion and wet debris from the threshold to bottom brackets, roller bearings, cable hardware and vertical track. It also treats historic-district exterior replacement as a different decision from repair, and repeatedly separates renter access/reporting from owner or manager authorization.

## Images

- `assets/hero.jpg` — 1800×1200 progressive JPEG; late-winter Ann Arbor historic-neighborhood garage and torsion-shaft inspection.
- `assets/work-1.jpg` — 900×600 progressive JPEG; broken torsion spring measurement.
- `assets/work-2.jpg` — 900×600 progressive JPEG; corroded bottom section and bent vertical track at a salty threshold.
- `assets/work-3.jpg` — 900×600 progressive JPEG; opener gear diagnosis.

All four were generated with domain-prefixed temporary filenames, then converted to JPEG at quality 80. Temporary PNGs were removed.

## Shared-template issue

`template/index.html` still contains a hardcoded steps-band heading and lede: “How it works,” “Three steps, one phone call,” and “There is nothing to fill in and nothing to buy. The call is the whole process.” The final sentence conflicts with the writer brief’s instruction to sell dispatched repair work rather than a phone conversation, and it cannot be localized from `copy.md`. It should become authored copy blocks, like the other corrected page-band headings.

## Could not source

I found no City of Ann Arbor source that directly attributes garage-door corrosion to road salt or quantifies corrosion of bottom sections/tracks. I therefore did not state that as a sourced municipal finding. The local fact is limited to documented city deicing/sand-salt exposure; the copy frames corrosion as a technician inspection judgment when rust, wet residue or noisy lower hardware is already present.

## Validation

- `python3 template/build.py annarborgaragedoorrepairpros.com` — PASS; home 2866 words, four symptom blocks, three local Q&As, three sourced facts. The placeholder phone warning is expected.
- `python3 template/build.py` — PASS across all currently written sites; 51 unwritten drafts skipped.

During the collection check I corrected two unrelated existing validation issues: Charlotte gutter symptom blocks exceeding the maximum word count, and an Overland Park garage-door banned phrase/duplicate prose run. The final full build passed.
