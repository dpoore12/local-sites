## From WRITER-NOTES.md

# dallaswrongfuldeathlawyerpros.com — writer notes (phase 1 complete)

Written 2026-08-21. No tenant, no attorney, no firm, no case result, no settlement
figure, no win record, no bar credential anywhere on the site. The CTA is a review
with a Texas wrongful death attorney being arranged — never an outcome.

## The three sourced local facts

1. **Who Texas allows to file.** CPRC § 71.004 — the action is for the exclusive
   benefit of the surviving spouse, children and parents; one may bring it for the
   benefit of all; if no eligible relative files within three calendar months the
   executor or administrator must. Siblings are not on the list. § 71.021 keeps the
   deceased person's own claim alive as a separate survival action for the heirs,
   legal representatives and estate.
   - https://statutes.capitol.texas.gov/Docs/CP/htm/CP.71.htm
   - https://law.justia.com/codes/texas/civil-practice-and-remedies-code/title-4/chapter-71/subchapter-a/section-71-004/
   - https://law.justia.com/codes/texas/civil-practice-and-remedies-code/title-4/chapter-71/subchapter-b/section-71-021/

2. **Dallas County traffic deaths, 2024 (TxDOT).** 305 fatal crashes, 331 deaths;
   133 of the fatal crashes on city streets vs 81 on interstates.
   - https://www.txdot.gov/content/dam/docs/division/trf/crash-records/2024/13.pdf
   - https://www.txdot.gov/content/dam/docs/division/trf/crash-records/2024/12.pdf

3. **Dallas County filing venue.** Thirteen civil district courts listed (14th, 44th,
   68th, 95th, 101st, 116th, 134th, 160th, 162nd, 191st, 192nd, 193rd, 298th) at the
   George L. Allen, Sr. Courts Building, 600 Commerce Street, plus five county courts
   at law with concurrent civil jurisdiction above $500 and no ceiling; the filing
   party chooses.
   - https://www.dallascounty.org/government/courts/civil_district/
   - https://www.dallascounty.org/government/county-clerk/civil-courts/faqs.php

## Other statutes used in the copy (verified, cited in prose by section number)

- § 71.002 liability language (wrongful act, neglect, carelessness, unskillfulness, default)
- § 71.009 exemplary damages for a wilful act or omission or gross negligence
- § 71.010 jury apportionment among eligible relatives alive at that time
- Chapter 74: § 74.051 60-day pre-suit notice with records authorization;
  § 74.351 expert report within 120 days of each defendant's original answer,
  dismissal with prejudice plus fees if missed, one 30-day cure for a deficient report;
  § 74.301 noneconomic caps $250k per claimant (physician/non-institutional provider),
  $250k per institution, $500k across institutions
- Texas Labor Code § 408.001 exclusive remedy and the exemplary damages exception
- CPRC § 101.023 Tort Claims Act caps (municipality $250k per person / $500k per occurrence)

## Collision avoidance

Built on the wrongful-death-specific statutes (Ch 71, § 71.021, Ch 74 caps) rather
than the Texas two-year limitations period or proportionate responsibility, which the
Houston motorcycle site uses. Full-network build shows zero shared 15-word runs.

## Neighborhoods

Oak Cliff, Lakewood, Pleasant Grove, Preston Hollow, Oak Lawn, Lake Highlands.

## Photos

hero.jpg (1800px) mid-century Dallas county courts building exterior, overcast.
work-1.jpg blank paperwork and folders on a desk. work-2.jpg quiet Dallas surface
arterial, no crash, no people. work-3.jpg empty meeting room. All muted, no text,
no logos, no gavels, no scales, no portraits, nothing depicting grief.

## Build result

`python3 template/build.py dallaswrongfuldeathlawyerpros.com` → PASS
home 3023 words / about 395 / contact 662. Only WARN is the PLACEHOLDER phone.
`python3 template/build.py` → exit 0, all 12 written sites PASS, no shared runs.
