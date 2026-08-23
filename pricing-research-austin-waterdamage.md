# Pricing research — waterdamageaustinco.com (water damage restoration, Austin, TX)

Mode: cost. All sources retrieved 2026-08-23. Build status: `python template/build.py waterdamageaustinco.com --check-only` → **[PASS]**, pricing page 1747 visible words.
(Note: `pricing-research-austin-wd.md` in this directory belongs to austinwrongfuldeathlawyerpros.com and was not touched.)

## Anchors (3)

### 1. Water categories under the industry standard — "Category 3"
- Primary source cited: IICRC position statement, *Category of Water Damage and Weather-related Events* (PDF) — https://iicrc.org/wp-content/uploads/2026/04/Weather-Related-Position-Statement_2026.pdf
- Stated: "Citations are specific to the **5th Edition ANSI/IICRC S500 (2021)**." Category 3 definition quoted verbatim on that page: "grossly contaminated and can contain pathogenic, toxigenic, or other harmful agents… Examples… include, but are not limited to: sewage; wasteline backflows that originate from beyond any trap regardless of visible content or color; all forms of flooding from seawater; rising water from rivers or streams; and other contaminated water entering or affecting the indoor environment, such as wind-driven rain from hurricanes, tropical storms, or other weather-related events." Also stated: categories (S500 §10.4.1) reflect the range of contamination considering originating source **and** quality after contact with materials, and "**Time and temperature can affect or retard the amplification of contaminants, thereby affecting its category**"; and "**Top-down water ingress, wind-driven rain and water from weather related events are not automatically considered Category 3 Water**."
- Supporting: https://iicrc.org/s500/ — designation ANSI/IICRC S500, *Standard for Professional Water Damage Restoration*, Fifth Edition 2021, currently under revision by a new consensus body (previous 4th Edition 2015); scope statement captured. https://iicrc.org/iicrcstandards/ lists the standard but defines nothing.
- **Unverifiable from IICRC's free pages:** the numeric definitions of Category 1 and Category 2 and of Classes 1–4. Those live in the paid standard, so the site copy describes the three-tier contamination structure and quotes only the Category 3 language actually published.

### 2. City residential plumbing permit — "$200.43"
- Source: City of Austin homeowner permitting fees, fiscal year 2026 ("Homeowner Permitting Fees-204") — https://services.austintexas.gov/budget/cbq/index.cfm?action=pushFile&popup=true&FILE_ID=2050CEDEC9
- Stated: Plumbing Fee **FY2026 $200.43** (FY2025 $184.70); the same figure applies to common residential building permits, express permits and small projects.
- Fee schedule index: https://www.austintexas.gov/development-services/fees — FY 2025-26 schedule effective **October 1, 2025**; credit card service fee 2.35% ($2 minimum); $30 ACH return fee.

### 3. Utility leak bill adjustment window — "90 days"
- Source: Austin Water, high water bill options — https://www.austintexas.gov/water/high-water-bill-options
- Stated: adjustment available under **City of Austin Code 15-9-141**; request **within 90 days** of repairing the leak; submit paid repair invoice, account number, service address, and date range of the high bills; a customer receiving an adjustment **may not also request an administrative hearing under Chapter 15, Article 12**; customer service 512-494-9400.
- Rates page https://www.austintexas.gov/water/rates-and-fees lists only PDF links (residential rates effective Nov 1, 2025); the residential rate PDF returned a client error, so no per-1,000-gallon rate was cited.

## Rows (7) — company-posted prices, with the arithmetic

Standing assumptions stated in the row `basis` fields: **500 sq ft affected area** for per-square-foot conversions, **4 drying days** for the equipment row.

| Row | Low | High | Sources | Arithmetic |
|---|---|---|---|---|
| Clean-water loss, ~500 sq ft | 1500 | 4000 | texascertifiedrestoration.com (Austin $3–$7.50/sq ft overall; **Category 1 clean $3–4/sq ft**), puroclean.com (clean $3–4/sq ft, excludes reconstruction), thesteamteam.com (by water type **$3.50–$8/sq ft**; restoration $1,200–$6,000) | 500 × $3.00 = **$1,500**; 500 × $8.00 = **$4,000** |
| Gray-water loss, same 500 sq ft | 2000 | 3575 | texascertifiedrestoration.com (**$4–$6.50/sq ft plus 10% contamination markup**), puroclean.com ($4–$6.50/sq ft) | 500 × $4.00 = **$2,000**; 500 × $6.50 = $3,250 × 1.10 = **$3,575** |
| Sewage backup cleaned and sanitized | 1200 | 10000 | capitalcitywaterrepairpros.com (sewage backup cleanup and sanitation **$1,200–$5,000**), pennysrestoration.com (smaller sewage jobs from **$2,500**, larger jobs from **$10,000**), texascertifiedrestoration.com (**$7–$7.50/sq ft plus 20% markup** plus material replacement), puroclean.com ($7–$7.50/sq ft) | Per-sq-ft route: 500 × $7.00 = $3,500 → ×1.20 = $4,200; 500 × $7.50 = $3,750 → ×1.20 = **$4,500** (stated in `basis`). Row low = Capital City's posted floor; row high = Penny's posted large-job figure. Penny's figures are "start at" numbers, used as a low within their own tier, and the $10,000 large-job start is carried as the row ceiling with the note saying so |
| Standing water extracted, one room, <200 sq ft | 500 | 2500 | ablewaterdamage.net (basic water extraction **$500–$1,500**; complete cleanup and drying $2,000–$5,000; full restoration $5,000–$10,000+), texascertifiedrestoration.com (small projects under 200 sq ft **$1,000–$2,500 per project**) | Extraction only; no material replacement |
| Three air movers + one dehumidifier, 4 days | 448 | 1031 | premieratx.com (compact blower $18/day, low profile $26, high speed $32; standard dehumidifier $58, large LGR $79, XL $118; setup and breakdown $65 for rentals under $150 or $175 over $150), allnationrestoration.com (air mover Dri-Eaz Velo $35.75/day, LGR dehumidifier $100/day; secondary table $33 and $61/day) | **Low:** (3 × $18) + $58 = $112/day × 4 = $448 + $65 setup = **$513**, floor taken as the pre-setup $448 equipment total. **High:** (3 × $32) + $118 = $214/day × 4 = $856 + $175 setup = **$1,031**. Cross-check with All Nation: (3 × $35.75) + $100 = $207.25/day × 4 = $829; low table (3 × $33) + $61 = $160/day × 4 = $640 |
| Multi-room mitigation, 200–800 sq ft | 1200 | 7000 | texascertifiedrestoration.com (medium projects 200–800 sq ft **$2,500–$7,000 per project**; large 800+ sq ft $7,000–$15,000+), thesteamteam.com (restoration **$1,200–$6,000**; by area $1,000–$10,000+) | Excludes finish rebuild |
| Rebuild after dry-out | 3000 | 30000 | baileybearconstruction.com (single-room rebuild **$3,000–$10,000**; multi-room **$10,000–$30,000**; major/structural $30,000–$75,000+; budget shares: demo 8–15%, drywall/paint 18–28%, flooring 15–25%, trim/doors 10–18%, cabinetry/fixtures 10–20%, plumbing/electrical 8–15%, permits/protection/cleanup 4–8%), ablewaterdamage.net (full restoration **$5,000–$10,000+**) | Priced after the space is dry; separate contract |

Material drying times used in the copy (all from texascertifiedrestoration.com): hardwood $10–15/sq ft restoration, 5–7 days; carpet and pad $1–11/sq ft, 2–3 days; drywall $1–3/sq ft, 3–5 days; tile $2–5/sq ft, 1–2 days; laminate $3–8/sq ft, usually replaced.

Captured but not used as row sources: thesteamteam.com mold remediation page (small isolated $500–1,500; moderate $1,500–5,000; large $5,000+; projects run 1–5 days) — https://www.thesteamteam.com/guides/mold/mold-remediation-cost; lonestarplumbing.org emergency cleanout pricing ($150–250 drain cleanout, $300–500 hydro-jetting, $400–800 sewer line); texasrestorationgroup.com (not fetched for figures).

Rejected sources: austinrestorationservice.com (self-described "Local Service Guide" with no company identity — lead-gen doorway); bluestarrest.com (equipment day rates but no city or address); swivl.tech, homeyou, promatcher, restorationcost.com, waterdamagerestorationpricing.com, homecostcalc.com, contractorplus.app, moldcostguide.com (modeled cost calculators); all banned-list domains (angi, thumbtack, homeguide, etc.).

Local-conditions support already in the site's `local_facts`: Austin Watershed Protection FloodPro and the ~10% of city land in floodplain; the October 31, 2013 Halloween Flood (Onion Creek at US 183 reached a record 41 ft, rising 11 ft in 15 minutes, 659 homes damaged); more than 9,000 buildings in the 100-year floodplain.

## Unverified / open
- IICRC's free pages do not publish the Category 1 / Category 2 definitions or the Class 1–4 definitions; only the Category 3 language and the S500 5th Edition (2021) designation are citable.
- Austin Water's residential per-1,000-gallon rate PDF would not fetch, so no volumetric rate figure was used.
- BLS OEWS Austin metro wage series was not retrieved (oes_*.htm blocks scripts; keyless API over quota); three government/utility/standards anchors were sufficient.
