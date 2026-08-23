# Pricing research — mesquiteacrepairpros.com (Mesquite, TX, AC repair)

All figures retrieved **2026-08-23**. Mode: `cost`. 3 anchors, 7 rows. Operators are **eastern Dallas County and east-side** shops only (Mesquite, Balch Springs, Garland, Rowlett, Forney, Rockwall) — no overlap with the Collin County set used for Allen.

## Anchors (deliberately different authorities from Allen — no BLS wage here)

| Figure | Value | Source | URL |
|---|---|---|---|
| Residential mechanical permit (includes condenser and furnace replacement), Sec. 12-104; residential plumbing permit Sec. 12-102 | **$65.00** each | City of Mesquite code of ordinances, permit fee sections 12-102 and 12-104 | https://apps.cityofmesquite.com/city_secweb/ordinances/5136.pdf |
| Oncor Home Energy Efficiency 2025 residential HVAC replacement incentive caps | 2 ton **$2,000**, 2.5 **$2,200**, 3 **$2,600**, 3.5 **$2,900**, 4 **$3,200**, 5 **$3,400** | Oncor 2025 Home Energy Efficiency SOP program manual (rev. 01/23/25) | https://www.oncor.com/content/dam/oncorwww/eepm/documents/residential-resources/2025/2025%20HEE%20SOP%20Program%20Manual%20012325.pdf.coredownload.pdf |
| TDLR insurance minimums, air conditioning and refrigeration contractor | Class A **$300,000 / $600,000 / $300,000**; Class B $100,000 / $200,000 / $100,000 | Texas Department of Licensing and Regulation, ACR contractor requirements | https://www.tdlr.texas.gov/acr/contractor-apply.htm |

## Rows and the posted figures behind them

1. **Service call and diagnosis, $75–$150**
   - Call Eric's Air Conditioning (Mabank shop serving Balch Springs / Mesquite / Dallas County): service call + diagnostic **$79–$129**. https://callerics.com/pricing.html
   - Frosty's Heating and Air (Mesquite page): diagnostic **$85**, charged separately. https://frostyshvac.com/locations/mesquite
   - Forney HVAC Pros: diagnostic **$75–$150** → low = $75, high = $150. https://forneyhvacpros.com/blog/ac-repair-cost-forney-tx-2026
   - HVAC Repair Rockwall: diagnostic $75–$150. https://hvacrepairrockwall.net/guides/ac-repair-cost-rockwall
2. **After-hours / overnight premium, $150–$250** (surcharge on top of the repair)
   - Frosty's (Mesquite): after-hours **$250** ($0 for members) → high = $250.
   - Forney HVAC Pros: emergency add **$150–$250** → low = $150.
   - This row is the premium alone, stated as such in `basis` and `note`.
3. **Run capacitor replaced, diagnosis included, $150–$850** (parts and labor)
   - Expedition HVAC (Garland): capacitor **$150–$300** → low = $150. https://expeditionhvac.com/ac-repair-cost-garland-tx/
   - Forney HVAC Pros: capacitor $180–$380.
   - HVAC Repair Rockwall: capacitor $150–$350 (diagnostic $75–$150 billed separately → up to ~$500 all-in).
   - Call Eric's: capacitor **$350–$850** → high = $850.
   - Frosty's DFW page corroborates a complete capacitor service at **$500**. https://frostyshvac.com/blog/how-much-does-ac-repair-cost-in-dfw
4. **Condenser fan motor replaced, $400–$2,800**
   - Frosty's (DFW): condenser fan motor **$650**, ECM up to **$2,800** including parts and labor → high = $2,800.
   - HVAC Repair Rockwall: condenser fan motor **$400–$750** parts and labor → low = $400.
5. **Blower motor replaced, $450–$4,200**
   - Call Eric's: blower **$800–$4,200** (includes ECM module) → high = $4,200.
   - HVAC Repair Rockwall: blower **$450–$900** → low = $450.
   - Frosty's (DFW): PSC blower $750–$1,000.
   - *Excluded:* Expedition HVAC's $250–$600 figure is blower **repair**, not replacement — kept off this row.
6. **R-22 leak found and refrigerant replaced, $350–$1,500** (leak search plus refrigerant)
   - Frosty's (Mesquite): R-22 recharge **$200 per lb** installed vs R-410A **$100 per lb**; R-22 leak repair total **$650–$1,000**.
   - Forney HVAC Pros: refrigerant leak detection + recharge **$350–$1,200** → low = $350.
   - HVAC Repair Rockwall: leak search and repair **$500–$1,500+** → high = $1,500.
7. **Whole system replaced with city permit, $5,200–$20,000** (installed)
   - Elite Clean DFW (Rowlett): replacement **$5,200–$8,500 installed including city permit and inspection**, up to $12,000+ → low = $5,200. https://elitecleandfw.com/ac-replacement-cost-rowlett/
   - Frosty's (Mesquite): AC replacement **$8,000–$20,000+** → high = $20,000.

## Non-convergence measures vs. allenacrepairpros.com
- Different operator set (east Dallas County / Rockwall / Forney vs. Allen / McKinney).
- Different anchors: Mesquite city ordinance permit fee + Oncor incentive + TDLR insurance minimums; **no BLS wage anchor** (the DFW wage is used on Allen only).
- Different page structure: Mesquite is built around 1960s–70s housing stock, R-22 economics and the flat-fee/after-hours structure; Allen is built around the diagnostic-fee treatment, 1990s attic-installed equipment and city registration/reinspection fees.
- Different row set: Mesquite has an after-hours premium row and an R-22 row and no compressor row; Allen has compressor, coil and contactor rows and no standalone after-hours row.

Build: `python template/build.py mesquiteacrepairpros.com --check-only` → **[PASS]**, pricing page 1731 visible words.
