## From RESEARCH.md

# virginiabeachcaraccidentlawyerpros.com — phase 1 complete

Car Accident Lawyer · Virginia Beach, VA · $2,000/mo · keyword `virginia beach car accident lawyer`
Written 2026-08-21. No tenant signed: no firm name, no attorney name, no case result, no
settlement figure, no win record, no bar credential anywhere in the copy.

## Build result

    python3 template/build.py virginiabeachcaraccidentlawyerpros.com   -> [PASS]
    python3 template/build.py                                          -> exit 0, 12/12 written sites PASS

Only warning is the expected `phone (757) 555-0100 is a PLACEHOLDER`.

Per-page visible word counts from the build output:

| Page | Words |
|---|---|
| `/` (home) | 2804 |
| `/about/` | 412 |
| `/contact/` | 606 |

Symptom card lengths: 4 cards, all inside the 200–360 phase-1 band. 3 local Q&As. 3 sourced facts.

## The three local facts (as written into site.json)

1. **Any fault of your own can bar the claim entirely** — Virginia still applies contributory
   negligence: where a plaintiff fails to exercise reasonable care contemporaneously or concurrently
   with the defendant's negligence, that contributory negligence bars recovery (Court of Appeals of
   Virginia opinion, quoting *Chandler v. Graffeo*, 268 Va. 673, 681 (2004) and *Sawyer v. Comerci*,
   264 Va. 68, 75). The General Assembly had to enact Virginia Code § 8.01-58 as a statutory
   exception just to stop contributory negligence barring injured railroad employees' claims.
   Counterweight cited in the same fact: Virginia Code § 46.2-1094 — a safety belt violation does not
   constitute negligence, may not be considered in mitigation of damages, and is not admissible in a
   civil case.
   - https://www.vacourts.gov/opinions/opncavwp/1521221.pdf
   - https://law.lis.virginia.gov/vacode/title8.01/chapter3/section8.01-58/
   - https://law.lis.virginia.gov/vacode/title46.2/chapter10/section46.2-1094/

2. **Two years to file, and $50,000 decides the courthouse** — Virginia Code § 8.01-243(A): every
   action for personal injuries, whatever the theory of recovery, must be brought within two years
   after the cause of action accrues. Virginia Code § 16.1-77: general district courts hear personal
   injury claims up to and including $50,000 (exclusive below $4,500), so larger claims go to circuit
   court — here the Virginia Beach Circuit Court at 2425 Nimmo Parkway, whose published goal is to
   conclude civil cases within 18 months of filing.
   - https://law.lis.virginia.gov/vacode/title8.01/chapter4/section8.01-243/
   - https://law.lis.virginia.gov/vacode/title16.1/chapter6/section16.1-77/
   - https://courts.virginiabeach.gov/circuit-court-clerks-office/circuit-court-civil

3. **Virginia Beach logged 4,965 crashes and 3,102 injuries** (the Virginia Beach specific fact) —
   Virginia DMV *2025 Virginia Traffic Crash Facts*, jurisdiction table: Virginia Beach City, 4,965
   crashes, 28 fatalities, 3,102 injuries; within that, 304 alcohol-related crashes causing 10 of the
   deaths and 610 speed-related crashes. Verified by pulling the PDF and reading the Virginia Beach
   City rows directly, not from a snippet.
   - https://www.dmv.virginia.gov/sites/default/files/documents/VA-traffic-crash-2025.pdf
   - https://www.dmv.virginia.gov/safety/crash-data/traffic-crash-facts

## Extra sourced material used inside the copy (not in the 3 fact cards)

- Uninsured Motor Vehicle Fee eliminated effective July 1, 2024; every registered vehicle must now
  carry insurance meeting Virginia's limits — https://www.dmv.virginia.gov/news/new-laws-take-effect-today-july-1-2024
- Minimum liability limits, Virginia Code § 46.2-472: $30,000/$60,000/$20,000 for policies effective
  Jan 1 2022–Dec 31 2024; $50,000/$100,000/$25,000 for policies effective on or after Jan 1 2025 —
  https://law.lis.virginia.gov/vacode/title46.2/chapter6/section46.2-472/
- Mandatory uninsured/underinsured motorist coverage at limits equal to liability unless rejected,
  plus at least $20,000 UM property damage, Virginia Code § 38.2-2206 —
  https://law.lis.virginia.gov/vacode/title38.2/chapter22/section38.2-2206/
- Duty to stop, report and render assistance after a crash; Class 5 felony where anyone is injured,
  Virginia Code § 46.2-894 — https://law.lis.virginia.gov/vacode/title46.2/chapter8/section46.2-894/

## Neighborhoods (6)

Kempsville, Great Neck, Hilltop, Bayside, Thalia, Sandbridge. Kempsville, Great Neck, Bayside and
Sandbridge all appear as named places on City of Virginia Beach sites (rec centers, parks, the
Sandbridge beach facility); Hilltop and Thalia are long-established Virginia Beach neighborhood names.

## Photos

`hero.jpg` (1800px) wide Virginia Beach–style multi-lane commercial arterial, overcast coastal light.
`work-1.jpg` collision damage detail on a sedan's rear quarter. `work-2.jpg` documents-and-desk
detail. `work-3.jpg` municipal courthouse exterior. No gavels, no scales, no lawyer portraits, no
text, no logos, no faces. All JPEG quality 80 progressive; PNG originals deleted.

## Two template-level notes for the parent (not changed — template is LOCKED)

- `template/inner.html` line 49 hardcodes the eyebrow **"Before the truck arrives"** above
  `expect_head`. It renders on the contact page of this legal site and reads as trade language.
- `hero_note` in `build.py` renders "Virginia Beach City County" because `counties` is
  `["Virginia Beach City"]` and the template appends "County". Virginia Beach is an independent city,
  so this reads awkwardly on every page of this site.
