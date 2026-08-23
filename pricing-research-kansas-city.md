# Pricing research — kansascityemergencyplumber.com (Kansas City, MO, Emergency Plumbing)

Retrieval date: 2026-08-23. Mode: `cost`.

## Anchors used on the page

| Anchor | Value | Source (fetched) | Exact wording found |
| --- | --- | --- | --- |
| Plumbing permit, one- and two-family dwellings | $52.00 minimum | [Kansas City Code of Ordinances § 18-20, Fees](https://kansascity-mo.elaws.us/code/coor_ch18_arti_sec18-20) | "One- and two-family detached dwelling building, mechanical, plumbing, electrical, elevator and fire protection permit fees": $0.00–$1,000.00 → **$52.00**; $1,001–$2,000 → **58.00**; first $2,000 → 58.00 plus **4.33** for each additional $1,000 to $100,000; $100,001+ → 483.00 plus 1.41 per additional $1,000. Minimum fee **$52.00** |
| Water service permit, KC Water | $100.00 per permit | [KC Water Rate Book FY 2027, Schedule of Fees and Charges (PDF)](https://www.kcwater.us/wp-content/uploads/2026/03/Rate-Book-FY-2027_031726-1.pdf) | Sec. 78-28 permit fee "$100.00 per each such permit" for taps and new services; existing service "altered, extended, renewed, or repaired from the first valve to the building improvement or fixtures"; abandonment/replacement with a larger service; disconnection at the main |
| Restoring service after a meter or tap is pulled | $610.00 | [KC Water Rate Book FY 2027 (PDF)](https://www.kcwater.us/wp-content/uploads/2026/03/Rate-Book-FY-2027_031726-1.pdf) | "Restoration of terminated service after the water services department has removed a meter or a tap to the main — $610.00 ... in addition to any permit, tap, or other charges" |

## Supporting figures cited in body copy

- KC Water FY2027 rate book, same PDF: water service plan review **$110.00** for up to 10 service connections, **$12.00** per connection above 10, **$65.00** resubmission charge after a rejection, duplicate permit **$10.00**. Rates effective with billings on and after **May 1, 2026**. Residential sanitary sewer service charge **$32.02/month**; water service charge **$21.15/month** on a 3/4-inch meter (not used on the page).
- The FY2025 rate book (https://www.kcwater.us/wp-content/uploads/2024/04/Rate-Book-FY-2025.pdf) carries the identical $100 permit fee, confirming the figure is stable across years.
- February 2021 minimums (−6 °F, −10 °F, −13 °F on Feb 14/15/16), cast iron DWV standard in homes built 1950s–early 1980s, and the two-state permitting/water-authority split are pre-existing sourced `local_facts` in this site's `site.json`.

## Cost rows (market ranges, not advertiser prices)

8 rows: off-hours callout $170–500; frozen/split pipe repair $350–1,600; main line rodded $210–625; sewer camera + locate $235–675; sump or ejector pump replaced $550–2,100; 40–50 gal water heater $1,400–3,500; cast iron stack section replaced $1,800–7,500; lateral or water service replaced to the main $5,200–19,000.

Local cost logic: frost-depth trenching, limestone and hills, century-old housing with plaster and cast iron, and basement-backup diagnostics that determine whose line failed.

## Could not verify

- **BLS OEWS metro wage, SOC 47-2152, Kansas City MO-KS MSA.** Intended series `OEUM0028140000000047215208`. BLS public data API returned `REQUEST_NOT_PROCESSED — daily threshold ... reached` on 2026-08-23 (v1 and v2); `bls.gov/oes/current/oes_28140.htm` and the OEWS flat files return 403 to scripts. No wage anchor published.
- `kcmo.gov` (the Building and Development Fee Schedule page and the Permits Division page) is disallowed to the fetcher by robots. A screenshot of the fee-schedule page confirmed it only points readers to "Article 1 Section 18 of the Building Code", which is why § 18-20 is cited directly instead.
- KC Water publishes no dollar figure for a sanitary sewer connection permit or for meter connection charges by size; the rate book states meter connection charges are "based on the current price of the meter installed and related appurtenances plus the current cost of such setting", so no amount is quoted.


## Published price sources, 2026-08-23

Every row in `pricing.rows` was rebuilt from prices published by companies working this market.
Retrieval date for every URL below: 2026-08-23. No aggregator, lead-gen or cost-guide domain on the
build's banned list was used, and pages that publish no dollar figure were not cited.

### Figures read (Kansas City metro)

| Company | Job as posted | Figure | URL |
|---|---|---|---|
| A-1 Sewer & Septic Service | standard drain cleaning (1 hr, 100 ft cable, one drain, accessible cleanout); extra time; pull/reset toilet incl. wax ring; +50 ft cable; additional line; two-tech drain cleaning; crawlspace or 150-200 ft; mini-jetter; residential large jetter; commercial jetter; milling; video inspection; onsite evaluation; trip charge for a visual estimate; 40-gal tank-only install; 50-gal | $175; $43.75/15 min; $135; $125; $95; $350; $525; $255; $525; $1,050; $350/hr; $175; $225/hr; $0; $1,968 + tax; $1,992 + tax | https://a-1sewerandsepticservice.com/kansas-city-plumbing-prices/ |
| Poor John's Plumbing | drain cleaning with access / all drains; camera & locate; PRV replacement (labor $300-400 + materials $175); main supply valve replacement; water heater replacement; toilet replacement labor; flapper; expansion tank; "No Service Charge" | $229; $200; $475-600; $450-600; $1,700-1,900; $350; $150 + $15; $350-450; $0 | https://poorjohns.com/plumber-in-kansas-city-missouri/ |
| Poor John's Plumbing | water service line page: PRV replacement all-in; main shutoff valve replacement | $500-600; $475-650 | https://poorjohns.com/water-service.html |
| John the Plumber | faucet; drain snaked; toilet repair/replace incl. fixture; tank water heater incl. heater and install; sump pump install incl. pump and labor; water/sewer line repair; full line replacement; residential hourly; diagnostic/trip fee | $150-350; $150-500; $150-600; $1,500-3,500; $1,000-3,000; $50-250/ft; $3,000-15,000+; $90-150/hr; $0-100 | https://johntheplumberkansascity.com/how-much-does-a-plumber-cost-the-average-prices-you-should-be-paying/ |
| LBA Services | fixture drain unclog; mainline snaking | $100-275; $150-500 | https://www.lbaservices.com/drain-cleaning/ |
| KC Water Heaters | standard replacement packages incl. unit and install; Bradford White packages; 75-gal; tankless; pan; PRV upgrade | $1,595-1,900; $1,695 / $1,825; $3,000-3,500; $4,500-6,000; $25; $75 | https://kcwaterheater.com/pricing/ |
| All-n-One Plumbing | standard 40-50 gal gas tank replacement total incl. unit, labor, materials, disposal; tankless; hybrid | $1,800-2,500; $4,500-5,600+; $3,500-4,500+ | https://www.allnoneplumbing.com/post/water-heater-installation-replacement-in-kansas-city-mo-ks |
| Climate Control | sump pump installation; battery backup | ~$1,100-2,400; $600-1,200 | https://www.climatecontrolkc.com/blog/plumbing/sump-pump-installation-cost-in-kansas-city/ |
| Bright Side Plumbing | residential sewer line replacement, can exceed $30,000; cast iron descaling | $10,000-15,000; $3,500-5,500 | https://www.callbrightside.com/blog/how-much-does-sewer-line-replacement-cost/ |
| Anthony Plumbing Heating Cooling | water line repairs; sewer line repairs | $500-3,000; $1,000-7,500 | https://anthonyphc.com/plumbing/sewer-water-installation-and-repair/ |
| KC Pier | sump pump replacement, complete system | ~$2,500 | https://www.kcpier.com/how-much-does-sump-pump-replacement-cost-2025-pricing-kansas-city/ |

### Arithmetic for itemized totals

- **Off-hours call, $90-250:** John the Plumber posts a diagnostic/trip fee of $0-100 plus a residential hourly rate of $90-150 -> $0 + $90 = **$90** at the low, $100 + $150 = **$250** at the high. A-1's $225/hr onsite evaluation rate and Poor John's "no service charge, no trip charge" flat-rate model sit inside that band.

### Row-by-row mapping

1. Off-hours call $90-250 - itemized above.
2. Row replaced. Was "frozen or split pipe repaired in a basement or crawlspace"; no Kansas City company publishes a price for that job. Now **toilet pulled and reset, or a running toilet rebuilt** $135-600: A-1 $135 pull and reset including the wax ring, Poor John's $350 toilet replacement labor and $150 + $15 flapper, John the Plumber $150-600 toilet repair or replacement including the fixture.
3. Main line rodded $150-500 - LBA mainline snaking $150-500; John the Plumber $150-500; A-1 $175 flat; Poor John's $229 flat.
4. Camera + locate $175-200 - A-1 $175 video inspection; Poor John's $200 camera and locate. Both flat and posted; the range is genuinely narrow in this market.
5. Sump or ejector pump replaced $1,000-3,000 - John the Plumber $1,000-3,000 including the pump; Climate Control ~$1,100-2,400. KC Pier's ~$2,500 complete-system figure corroborates but was dropped from the row to keep the page inside its word budget.
6. Water heater 40/50-gal $1,500-3,500 - KC Water Heaters $1,595-1,900 packages including the unit; All-n-One $1,800-2,500 total including the unit; Poor John's $1,700-1,900; John the Plumber $1,500-3,500 including the heater. A-1's $1,968 is tank-only labour plus tax on parts and sits inside the band.
7. Sewer lateral or water service replaced $3,000-30,000 - John the Plumber $3,000-15,000+ and $50-250/ft; Bright Side $10,000-15,000 and "can exceed $30,000". Anthony Plumbing's repair figures ($500-3,000 water line, $1,000-7,500 sewer) describe repairs, not replacement, so they are recorded here but not used to set the row.

### Row deleted

- **"Cast iron drain stack section replaced" was deleted.** The only Kansas City figure found for cast iron is Bright Side's descaling price of $3,500-5,500, and descaling is not replacement. Rather than price a replacement off a cleaning figure, the row was dropped.

### Emergency pricing in this market

No Kansas City operator publishes an after-hours or emergency surcharge. Poor John's advertises no service charge and no trip charge; A-1 posts $0 trip charge for a visual estimate and hours of 8am-8pm weekdays; Roto-Rooter Kansas City states it charges no additional fee for nights, weekends or holidays. The off-hours row therefore prices the trip fee plus a first hour rather than a premium.
