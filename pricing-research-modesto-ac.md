# Pricing research — modestoacrepairpros.com (Modesto, CA, AC repair)

All figures retrieved **2026-08-23**. Mode: `cost`. 3 anchors, 6 rows.

## Anchors

| Figure | Value | Source | URL |
|---|---|---|---|
| "Mechanical Plumbing Electrical – Minor" permit (covers HVAC replacements and new systems) | **$242.00**; water heater replacement permit **$139.00** | City of Modesto Building Safety Division development user fees, fiscal year 2025-26 | https://www.modestogov.com/DocumentCenter/View/19115/Building-Safety-Division-Development-User-Fees-Fiscal-Year-25-26-PDF |
| MID residential rebates | Central AC **$350** (tier HC100) / **$600** (HC110); central heat pump **$450** / **$700**; smart thermostat $50; equipment max 65,000 Btu/h | Modesto Irrigation District residential rebate catalog | https://middev-tomcat.azurewebsites.net/rebates/home/documents/MID_residential_catalog.pdf |
| BLS OEWS May 2025, HVAC mechanics and installers (49-9021), Modesto (MSA 33700) | **$31.13** median hourly, 470 employed | BLS OEWS May 2025 | https://www.bls.gov/oes/current/oes_33700.htm |

BLS series ID: **`OEUM003370000000049902108`**. Extracted from the OEWS May 2025 flat file (`MSA_M2025_dl.xlsx`); bls.gov HTML 403s to scripts and the keyless API was over quota.

**MID rebate caveat:** the amounts appear only in the rebate-catalog PDF, which MID serves from `middev-tomcat.azurewebsites.net`. The human-facing page https://www.mid.org/saving-energy-money/rebates/residential-rebates/ links to the catalog but posts **no dollar amounts**, so the PDF is cited as `source_url`. The amounts are independently corroborated by a Modesto/Turlock/Ceres contractor page listing the same MID figures ($600 high-efficiency central AC, $350 standard central AC, $700 / $450 central heat pump): https://tmchvac.com/rebates.html

## Rows and the posted figures behind them

1. **Diagnostic visit, $65–$99**
   - Irish Heat and Air (San Joaquin / Stanislaus, serves Modesto): **$65** diagnostic fee for all repair work. https://www.irishheatandair.com/service-area/
   - De Hart Plumbing Heating and Air (Modesto): **$89** AC repair diagnostic, waived with a paid repair. https://www.dehartinc.com/modesto/hvac/air-conditioning/ac-repair-maintenance
   - Geske Air Conditioning and Heating (Modesto, 95355): **$99** AC diagnostic, stated as not applying to repairs, refrigerant or labor. https://www.geskeair.com/
2. **Seasonal tune-up, $79–$150**
   - Geske: residential AC tune-up **$79.99**.
   - GS Home Services (Modesto / Stockton): AC tune-up special **$79** → low = $79. https://www.gshomeservices.com/stay-cool/
   - Valley Air Pro (Turlock, 1665 Peacock Dr.): residential AC tune-up and inspection **"Reg. $150"** → high = $150. https://valleyairpro.com/pricing
3. **Common summer repair (capacitor, contactor, thermostat, recharge), $100–$600**
   - De Hart: most common repairs **$100–$500** → low = $100.
   - Wally Falke's Heating and Air (Modesto / Turlock / Merced): most common repairs, including capacitor replacement, refrigerant recharge or thermostat swap, **$150–$600** → high = $600. https://wallyfalkes.com/air-conditioning-repair/
   - Comfort Experts (Modesto): average AC repair **around $316**. https://www.comfort-experts.com/air-conditioning/ac-repair-maintenance/
4. **Refrigerant leak located and system recharged, $200–$1,600**
   - Wally Falke's: refrigerant leak repair **$200–$1,500**; refrigerant recharge $150–$400 → low = $200. https://wallyfalkes.com/5-common-a-c-repairs/
   - Comfort Experts: refrigerant leak detection and repair **$225–$1,600** → high = $1,600.
5. **Compressor or corroded coil replaced, $600–$2,000**
   - Wally Falke's: replacement of a physically damaged or corroded coil that cannot be cleaned **$600–$2,000** → low = $600, high = $2,000.
   - Comfort Experts: compressor replacement **$1,350–$1,800** (sits inside the band).
   - Row label names both jobs because each source states a figure for one of them. Comfort Experts' **$90–$400** "evaporator coil replacement" figure was **not** used — it is inconsistent with every other posted coil-replacement figure and reads as coil cleaning.
6. **Full changeout with the Modesto permit, $4,500–$15,000** (installed)
   - NorCal Repairs (Modesto / Stanislaus County): AC replacement **$4,500–$15,000**, states permit cost is included in quotes → low = $4,500. https://norcalrepairs.com/hvac/ac-replacement/modesto
   - Wally Falke's: straightforward Central Valley replacement "starts in the upper $7,000s to low $8,000s"; many full replacements **$9,000 to $15,000 or higher** → high = $15,000. https://wallyfalkes.com/central-valley-ac-replacement-cost/

## Could not verify / dropped
- No Modesto-area operator publishes a standalone capacitor, contactor, fan motor or blower price with labor, so no component-level rows beyond the grouped "common summer repair" row were built. `ihvaconline.com/pricing` posts component prices but states no service city (national) and `accurateheat.com` is Franklin, MA — both rejected.
- `chrispairhvac.com`, `lovesair.com`, `scullysair.com`, `mclaughlin-air.com`: no posted prices.
- `absolutebestair.com` is McDonough, GA — rejected.
- NorCal Repairs mentions SMUD rebates; SMUD does not serve Modesto, so that figure was not used. The MID rebate is the correct local utility anchor.

Build: `python template/build.py modestoacrepairpros.com --check-only` → **[PASS]**, pricing page 1744 visible words.
