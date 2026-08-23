# Pricing research — sanjoseemergencyplumberpros.com (San Jose, CA, emergency plumbing)

All figures retrieved **2026-08-23**. Mode: `cost`. 4 anchors, 8 rows.

## Anchors

| Figure | Value | Source | URL |
|---|---|---|---|
| Water heater replacement permit, Permit Center | $56 (online $0) | City of San Jose adopted fee schedule, Resolution RES2024-230 (effective July 1, 2024) | https://records.sanjoseca.gov/Resolutions/RES2024-230.pdf |
| Plumbing permit adding no building area | greater of itemized fee or **$315.00 per hour** of actual plan review / inspection time | Same resolution | https://records.sanjoseca.gov/Resolutions/RES2024-230.pdf |
| Sanitary sewer connection fee, single family & duplex, lot <9,780 sq ft | **$447 per lot** (>9,780 sq ft = $1,991 per acre) | City of San Jose Environmental Services, sewer connection fees | https://www.sanjoseca.gov/your-government/departments-offices/environmental-services/water-utilities/regional-wastewater-facility/sanitary-sewer-service-charges/sewer-connection-fees |
| BLS OEWS May 2025, plumbers/pipefitters/steamfitters (47-2152), San Jose-Sunnyvale-Santa Clara (MSA 41940) | **$51.71** median hourly, 3,830 employed | BLS OEWS May 2025 | https://www.bls.gov/oes/current/oes_41940.htm |

BLS series ID for the wage: **`OEUM004194000000047215208`** (area 0041940, occ 47-2152, datatype 08 = median hourly). Wage extracted from the OEWS May 2025 flat-file release (`MSA_M2025_dl.xlsx`, downloaded to /tmp/oes25/oesm25ma/) because `bls.gov/oes/current/oes_41940.htm` returns 403 to scripts and the keyless API was over quota. The human-readable OEWS metro page is cited as `source_url`.

**Rejected:** `sjgov.org` building-fee-schedule.pdf — that is San Joaquin County, not Santa Clara County/San Jose. Not used.

## Rows and the posted figures behind them

1. **Night or weekend callout, $275–$800** (per visit, surcharge included)
   - Natan Plumbing (San Jose): emergency service $200–$500, plus **$75** evenings and **$150** nights/weekends. https://www.natanplumbing.com/blog/emergency-plumber-san-jose
   - Arithmetic: low = $200 + $75 = **$275**; that company's ceiling = $500 + $150 = $650.
   - CPI Plumbing (San Jose): emergency plumbing **$300–$800+** → high = **$800**. https://cpiservice.com/plumber-san-jose/
2. **One fixture drain cleared, $125–$400**
   - Local Rooter and Plumbing: basic snaking $125–$350. https://localrooterandplumbing.net/drain-cleaning-san-jose/
   - Superior Plumbing and Drain: standard snaking $150–$400; single fixture $150–$300. https://superiorplumbing.net/drain-cleaning/
   - Natan's Plumbing: snaking $179–$299. https://natansplumbing.com/blog/drain-cleaning-san-jose
3. **Main sewer line cabled, $250–$600**
   - Superior Plumbing: main line cable $250–$600. Local Rooter: main line clog $250–$600. Natan's: main line $299–$399.
4. **Hydro jetting, $120–$1,200**
   - CPI: hydro jetting **$120–$1,100+** → low = $120. Superior: main line jetting $500–$1,200 → high = $1,200. Natan's: $400–$800. Local Rooter: $300–$800.
5. **Slab leak located and rerouted, $1,700–$5,150**
   - Advanced Plumbing and Rooter (San Jose): leak detection $200–$650; single line reroute $1,500–$4,500. https://ai.advancedplumbingandrooter.com/
   - Arithmetic: low = $200 + $1,500 = **$1,700**; high = $650 + $4,500 = **$5,150**.
   - CPI: leak detection $75–$700 (corroborates the detection step). https://cpiservice.com/plumber-san-jose/
6. **40–50 gal gas water heater swapped with permit, $1,200–$4,500** (unit included)
   - Arcune Plumbing: water heater installation $1,200–$3,500; standard tank from $1,200. https://arcuneplumbing.com/water-heater-installation-san-jose/
   - Venture Plumbing: tank water heater $2,000–$4,500 installed. https://ventureplumbinginc.net/water-heater-installation-san-jose/
   - City permit of $56 (anchor) sits inside these installed figures per the sites' own descriptions of permitted work; it is called out separately in the page body rather than added to the row.
7. **Whole house repipe, $4,000–$15,000**
   - Repipe Champions: Bay Area repipe **$4,000–$15,000**, states permits, inspections and patching included. https://repipechampions.com/
   - CPI: repiping **$4,000–$15,000+**. https://cpiservice.com/plumber-san-jose/
8. **Sewer lateral replaced or lined, $1,000–$18,000**
   - CPI: sewer services $1,000–$10,000+; sewer line replacement $50–$250 per linear foot → low = $1,000.
   - Advanced Plumbing and Rooter: sewer under slab, trenchless $4,500–$18,000 → high = $18,000.

## Could not verify / dropped
- `superbrothers.com` and `idesignac` repipe pages returned 403 on this run — not cited.
- `gladiatorrepipe.com` publishes no prices — not cited.
- CPI's "$150 to $400 plumbing inspection" was **not** used as a sewer camera row; the job did not match.

Build: `python template/build.py sanjoseemergencyplumberpros.com --check-only` → **[PASS]**, pricing page 1748 visible words.
