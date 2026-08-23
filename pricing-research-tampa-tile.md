# Pricing research — tampatileroofrepair.com (tile roof repair, Tampa, FL)

Mode: cost. All sources retrieved 2026-08-23. Build status: `python template/build.py tampatileroofrepair.com --check-only` → **[PASS]**, pricing page 1739 visible words.

## Anchors (3)

### 1. Residential roofing trade permit — "$177.00"
- Source: City of Tampa trade permit fee schedule (PDF, effective Oct 1 2018, revised 2/16/2023) — https://www.tampa.gov/sites/default/files/document/2023/trade_permit_fee_schedule_02.16.23.pdf
- Stated: **Roofing residential $177.00**; roofing commercial $220.00; building general trade permit $120.00; HVAC equal change-outs $120 residential / $162 commercial; plumbing general $120; stucco/siding $177.

### 2. Permit threshold and tile inspection — "500 square feet"
- Source: City of Tampa roofing permit requirements, document P051 (PDF) — https://www.tampa.gov/sites/default/files/content/files/migrated/P051Roofing.pdf
- Stated: a permit is required for new roof, re-roof, re-cover, or **repair in excess of 500 square feet** (work of 500 sq ft or less is exempt); a **tile roof requires a dry-in inspection before tile installation**; a final inspection is required; single-family homes permitted before **March 1, 2002** must comply with hurricane mitigation retrofit requirements under F.S. 553.844.

### 3. The 25 percent roof rule and its statutory exception — "25 percent"
- Source: Florida Statutes section 553.844 (2025) — https://www.flsenate.gov/Laws/Statutes/2025/553.844
- Stated at §553.844(5): where an existing roofing system or roof section **was built, repaired or replaced in compliance with the 2007 Florida Building Code or any subsequent edition**, and **25 percent or more** of the roof is being repaired, replaced or recovered, **only the repaired, replaced or recovered portion must be constructed to meet the current code**. The Commission shall adopt this by rule, and **a local government may not adopt an administrative or technical amendment to this exception**.
- Code text corroboration: FBC Existing Building (2023, 8th Edition) **§706.1.1** — https://up.codes/viewer/florida/fl-existing-building-code-2023/chapter/7/alterations-level-1 — "Not more than 25 percent of the total roof area or roof section of any existing building or structure shall be repaired, replaced or recovered in any 12-month period unless the roof covering on the entire existing roof system or roof section is replaced or recovered to conform to the requirements of this code," followed by the identical statutory exception.
- Site `local_facts` also cite floridabuilding.org staff analysis DS-2021-007 for §706.1.1.

### Answer to the brief's question — what the Florida 25% rule currently says, and whether the carve-out applies
The base rule is unchanged in the 8th Edition (2023) FBC Existing Building §706.1.1: no more than 25% of a total roof area **or roof section** may be repaired, replaced or recovered in any 12-month period unless the covering on the entire existing roof system or section is replaced/recovered to current code. The amendment that homeowners hear about is the **statutory exception at Fla. Stat. §553.844(5)**, now mirrored in the code: if the existing roofing system or section was built, repaired or replaced under the **2007 FBC or any later edition**, then crossing 25% obliges only the **repaired portion** to meet current code — no whole-roof upgrade. Local governments are expressly barred from amending that exception, so it applies uniformly in Tampa and unincorporated Hillsborough County. **So: the carve-out applies to roofs whose last permitted roof work was under the 2007 code or later; roofs older than that remain exposed to the full-system requirement once repairs cross 25% within twelve months.**

## Rows (7) — company-posted prices

| Row | Low | High | Sources | Basis / arithmetic |
|---|---|---|---|---|
| 1–5 cracked or broken field tiles | 150 | 850 | westroofingfl.com ($150–400 for 1–3 tiles), vnpsroofing.com ($150–400 single tile), jaeofamerica.com ($300–800 for 1–5 cracked/broken), integrityroofingofflorida.com ($450–850 isolated tile replacement) | Flat per visit; area small enough to stay under the 500 sq ft permit threshold |
| Slipped/lifted tiles reset and re-secured | 250 | 2500 | jaeofamerica.com ($250–600 slipped/displaced), vnpsroofing.com ($300–900 small replacement/resetting), integrityroofingofflorida.com ($850–2,500 multi-area tile re-secure) | Priced by tile count lifted, cleaned, refastened, rebedded |
| Leak traced, underlayment patched, tile relaid | 400 | 3500 | vnpsroofing.com ($400–1,200 leak repair), jaeofamerica.com ($600–1,800 localized; $1,500–3,500 larger leak/valley), westroofingfl.com ($800–2,500 leak involving underlayment) | Includes tile removal and reinstallation over the patch |
| Section of underlayment replaced, original tile relaid | 1700 | 8500 | integrityroofingofflorida.com ($3,500–8,500 partial underlayment replacement with tile re-lay), pitchroofing.com ($1,700–4,000 to replace tile roof underlayment in Florida, up to $8,000) | Per section; 10–15% breakage of lifted tile belongs in scope |
| Flashing, valley metal or ridge cap replaced | 300 | 2500 | westroofingfl.com (flashing $300–1,200; ridge cap $500–1,500), vnpsroofing.com (flashing $300–900), integrityroofingofflorida.com ($850–2,500 flashing/valley replacement) | Per run or per penetration |
| Whole roof stripped, new underlayment, existing tile reset | 8000 | 35000 | integrityroofingofflorida.com ($18,000–35,000 tile re-underlay preserving original tile, posted at 40–60% of full replacement), jaeofamerica.com ($8,000–18,000+ full underlayment replacement reusing tile) | Whole-roof project |
| Full tile roof replacement with new tile | 15000 | 75000 | suncoastroofingsolutions.com ($15,000–$35,000+ complete tile replacement), steadfastroofingfl.com (**$1,200–$2,500 per square** of 100 sq ft for a full tile reroof; $25,000–$75,000+ total; 35–45 squares complex roof $22,000–35,000+), integrityroofingofflorida.com (concrete $24,000–55,000 at $10–16/sq ft on 2,500 sq ft; clay $30,000–75,000 at $12–22/sq ft) | **Per-square arithmetic:** $1,200–$2,500 per square × 30 squares (3,000 sq ft roof) = **$36,000–$75,000**, stated in the row basis. Low taken from Suncoast's posted whole-job floor |

Other captured figures not used as row sources: westroofingfl.com unit rates (concrete tile $2–5 each, clay $5–15+, underlayment $1–3/sq ft, rotted decking $1.50–4/sq ft, labor $3–8/sq ft; partial re-roof at 25%+ damage $5,000–12,000+); vnpsroofing.com secondary page "most tile repairs $400–$1,500"; rnroof.com Tampa repair averages ($250–1,500; labor $45–75/hr) which posted no tile-specific figures; jaeofamerica.com full tile replacement page ($18,000–35,000 concrete, ~$12/sq ft). Excluded: local.icasstormrestoration.com (subdomain doorway) and all banned-list domains (angi, homeguide, etc.).

Local-conditions support already in the site's `local_facts`: NOAA final report on Hurricane Milton (AL142024) — landfall at Siesta Key as a Category 3 on October 10, 2024, hurricane conditions from Clearwater Beach and Tampa southward, 83-knot gust reported at Tampa International Airport — https://www.nhc.noaa.gov/data/tcr/AL142024_Milton.pdf

## Unverified / open
- Hillsborough County's building permit fee amounts are published only in a downloadable schedule; both the HTML page (https://hcfl.gov/businesses/permits-and-records/permit-fees/building-permit-fees) and the media PDF path returned no usable figures, so no county fee was cited. The site is a City of Tampa site and uses the city schedule.
- Florida windborne debris and uplift requirements are described qualitatively in the copy; no numeric design-pressure figure was cited because no primary source stating one was fetched.
