# Pricing research — allenacrepairpros.com (Allen, TX, AC repair)

All figures retrieved **2026-08-23**. Mode: `cost`. 4 anchors, 8 rows. Operators are **Collin County** shops only (Allen, McKinney) to keep this page separate from Mesquite.

## Anchors

| Figure | Value | Source | URL |
|---|---|---|---|
| Complete HVAC system permit | **$175** (water heater and OTC trade permits $75) | City of Allen fee schedule, June 2025 | https://cms3.revize.com/revize/allentx/Images/Documents/Business/City%20of%20Allen%20Fee%20Schedule%20(June%202025).pdf |
| Contractor / inspector registration, annual | **$50 per year** | same schedule | same URL |
| Inspection outside normal hours | **$75 per hour, 2 hour minimum**; reinspections $75 / $100 / $125 | same schedule | same URL |
| BLS OEWS May 2025, HVAC mechanics and installers (49-9021), Dallas-Fort Worth-Arlington (MSA 19100) | **$28.63** median hourly, 10,910 employed | BLS OEWS May 2025 | https://www.bls.gov/oes/current/oes_19100.htm |

BLS series ID: **`OEUM001910000000049902108`**. Extracted from the OEWS May 2025 flat file (`MSA_M2025_dl.xlsx`); bls.gov HTML 403s to scripts and the keyless API was over quota. **The DFW wage anchor is used on Allen only** — Mesquite deliberately uses city permit, utility incentive and state licensing anchors instead, so the two DFW pages do not converge.

## Rows and the posted figures behind them

1. **Diagnostic visit, $59–$150**
   - The Perfect Climate (McKinney): **$59** service fee. https://theperfectclimatehvac.com/pricing/
   - Trusted Heat and Air: **$95** diagnostic, stated as charged separately and **not** credited. https://trustedheatac.com/pricing/
   - Jupitair HVAC (Allen): flat **$89** diagnostic, waived with repair; emergency diagnostic $149. https://jupitairhvac.com/blog/ac-capacitor-guide/
   - Air Repair Pros (McKinney): diagnostic **$85–$150** → high = $150. https://airrepairpros.com/ac-repair-cost/
2. **Run capacitor replaced, $150–$450** (parts and labor)
   - HVAC Services Pro (Allen page): capacitor **$150–$450**. https://hvacservicespro.com/allen-tx-ac-repair/
   - Trusted Heat and Air: capacitor from **$135** + separate **$95** diagnostic = **$230** honest total (stated in the row note).
   - Jupitair: complete capacitor job **$180–$400** including parts and labor.
   - Air Repair Pros: capacitor $150–$300.
3. **Contactor replaced, $175–$500** (parts and labor)
   - HVAC Services Pro (Allen): contactor **$175–$500**.
   - Trusted Heat and Air: contactor from **$180** (+ $95 diagnostic = $275).
   - *Excluded:* The Perfect Climate posts a 2-pole contactor at $375 **plus labor** — a part-only figure, so it was not put into a parts-and-labor row.
4. **Condenser fan motor replaced, $395–$1,200**
   - Trusted Heat and Air: condenser fan motor from **$395**.
   - HVAC Services Pro (DFW page): condenser fan motor **$450–$1,200** → high = $1,200. https://hvacservicespro.com/ac-repair-cost-in-dfw/
5. **Refrigerant leak found and circuit recharged, $200–$3,500**
   - Air Repair Pros: leak repair **$200–$1,600**; recharge $100–$600 → low = $200.
   - HVAC Services Pro (Allen): refrigerant leak **$500–$3,500** → high = $3,500.
   - Trusted Heat and Air: refrigerant **$99 per pound**.
6. **Evaporator coil replaced, $600–$2,500**
   - HVAC Services Pro (DFW): evaporator coil replacement **$600–$900** → low = $600.
   - Trusted Heat and Air: coil from **$1,550**.
   - Air Motions HVAC (Allen): major repairs including coil/blower **$800–$2,500** → high = $2,500. https://airmotionshvac.com/ac-repair-allen/
7. **Compressor replaced, $1,000–$5,000**
   - Air Repair Pros: compressor replacement **$1,000–$2,500** → low = $1,000.
   - HVAC Services Pro (Allen): compressor **$2,000–$5,000** → high = $5,000.
8. **Condenser and coil changed out with the Allen permit, $3,200–$13,500** (installed)
   - HVAC Services Pro (Allen): central AC replacement **$3,200–$5,500** → low = $3,200; the DFW page runs to $13,500 by tonnage → high = $13,500.
   - Jupitair: full AC replacement **$3,800–$12,500 installed, permit included**, typical $5,500–$8,000. https://jupitairhvac.com/blog/new-ac-cost-installed-north-texas/

## Accuracy checks applied
- Capacitor row: totals, not headline part prices. The $135 + $95 non-credited diagnostic = $230 arithmetic is stated in the row note.
- Compressor row uses **compressor replacement** figures only; the $1,500–$1,700 "condenser replacement" figure from Air Repair Pros was kept off this row.
- Emergency figures from Jupitair ($199 / $250 surcharges, $299–$800 emergency repair) were **not** used as a row here — the after-hours structure is the Mesquite page's organizing idea, and Allen's is the diagnostic-fee treatment.

Build: `python template/build.py allenacrepairpros.com --check-only` → **[PASS]**, pricing page 1747 visible words.
