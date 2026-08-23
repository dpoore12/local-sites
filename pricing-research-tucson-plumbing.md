# Pricing research — tucsonemergencyplumberpros.com (Tucson, AZ, emergency plumbing)

All figures retrieved **2026-08-23**. Mode: `cost`. 4 anchors, 6 rows.

## Anchors

| Figure | Value | Source | URL |
|---|---|---|---|
| Residential trade permit (water heater like-for-like; sewer line / building drain repair or replace; water service line; plumbing fixture), includes ½ hr review + 2 inspections | **$118.51** each | City of Tucson adopted development services fee schedule (adopted year 1) | https://www.tucsonaz.gov/files/sharedassets/public/v/1/pdsd/documents/fee-schedule/adopted-year-1-fee-schedule.pdf |
| Each additional item on the same trade permit | **$20.70** (2+ items = $118.51 + $20.70 each additional) | Same fee schedule | same URL |
| New water service line + 5/8" meter | **$2,700** with pavement replacement, **$1,740** without; new 5/8" meter on existing service **$450** / **$560** | Tucson Water meter installation fees | https://www.tucsonaz.gov/Departments/Water/Your-Water-Bill/Misc.-Rates/Water-Meter-Installation-Fees |
| BLS OEWS May 2025, plumbers/pipefitters/steamfitters (47-2152), Tucson (MSA 46060) | **$28.40** median hourly, 1,170 employed | BLS OEWS May 2025 | https://www.bls.gov/oes/current/oes_46060.htm |

BLS series ID: **`OEUM004606000000047215208`**. Same retrieval workaround as the San Jose note (OEWS May 2025 flat file `MSA_M2025_dl.xlsx`; bls.gov HTML 403s to scripts, keyless API over quota).

## Rows and the posted figures behind them

1. **Plumber to the door and the fault identified, $49–$170** (per visit)
   - Arico Plumbing: diagnostic **$49**; repairs $85 first half hour then $95/hr; permit $155. https://aricoplumbing.com/plumbing-prices/
   - Sivart AZ Plumbing: diagnostic **$88**; camera inspection $49; same-day in town $79 plus cost of service; Tucson trip fee free. https://sivartazplumbing.com/pricing/
   - Right Now Plumbing and Heating: trip fee **$80–$170** charged before work starts; labor $80–$200/hr. https://rightnowplumbingtucson.com/how-much-does-a-plumber-in-tucson-cost/ → high = $170.
2. **Clogged drain cleared, lavatory line to main, $29–$800**
   - iDesign Air and Plumbing: drain clearing special **$28.88** for new customers → low = $29. https://www.idesignac.com/
   - Right Now Plumbing: standard unclog $110–$500; simple sink/tub $110–$215; **main line behind a wall or under a slab $400–$800** → high = $800. https://rightnowplumbingtucson.com/how-much-for-a-plumber-to-unclog-a-drain-in-tucson/
   - Advantage Air Mechanical: standard drain cleaning $130, average $150–$240. https://advantageairmechanical.com/plumbing/drain-cleaning/
3. **40 gal water heater replaced with permit and inspection, $900–$4,000** (unit included)
   - Just Water Heaters Tucson: 40-gal electric installed **$915** all-in with permit and inspection ($795 + tax headline). https://justwaterheaterstucson.com/
   - Plumber of Tucson: water heater install **$900–$1,500** including the unit → low = $900. https://plumberoftucson.com/prices/
   - Right Now Plumbing: water heater swap **$1,200–$4,000** depending on unit (40–50 gal $1,200–$1,800; tankless $2,500–$3,500; permit + inspection $150–$300) → high = $4,000.
   - Done Rite Services: tank water heater $1,400–$2,500 all-in including the unit. https://doneritesvcs.com/plumbing/water-heaters/
4. **Slab leak located and line rerouted, $1,075–$3,875** (detection plus reroute)
   - Plumber of Tucson: water leak detection **$375**; reroute simple $700–$1,200, moderate $1,300–$2,200, challenging **$2,300–$3,500**.
   - Arithmetic: low = $375 + $700 = **$1,075**; high = $375 + $3,500 = **$3,875**.
   - AB Plumbing: slab leak detection from $250, slab repair from $1,500 (i.e. from $1,750 combined). https://abplumbingllc.com/slab-leak-repair-tucson/
   - Tucson Plumber Services: leak detection and repair $1,500–$3,500. https://tucsonplumberservices.com/
5. **Sewer line replaced, spot repair through full line, $280–$15,000**
   - Advantage Air Mechanical: sewer replacement **$280–$8,050**, average $5,000; conventional $60–$150 per ft; trenchless $60–$280 per ft → low = $280. https://advantageairmechanical.com/plumbing/sewer-line-repair/
   - Tucson Plumbing and Drain: trenchless $3,000–$15,000; full replacement **$8,000–$15,000**; CIPP $80–$250/lf; City of Tucson permits $100–$500 → high = $15,000. https://tucsonplumbinganddrain.com/trenchless-sewer-repair-tucson/
   - Tucson Plumber Services: residential sewer $50–$150 per linear foot.
6. **Whole house repipe, PEX or copper, $4,500–$25,000**
   - iDesign Air and Plumbing: PEX **$4,500–$8,000** for a typical 3 bed / 2 bath (includes materials, labor, permits, inspections, drywall patching); larger homes $8,000–$15,000; copper $8,000–$15,000 typical and **$15,000–$25,000+** for larger/complex → high = $25,000. https://www.idesignac.com/services/repipe-tucson
   - Repipe Specialists Tucson: repipe **$4,500–$15,000** including patching and permits. https://tucson.repipe.com/

## Could not verify / dropped
- `woodsplumbing.com`, `picturerockscooling.com`, `goodfellasac.com` — no usable posted job prices at retrieval time.
- Right Now Plumbing states it does **not** add an after-hours surcharge, so no emergency-surcharge row was built for Tucson (unlike San Jose, where two operators publish one).

Build: `python template/build.py tucsonemergencyplumberpros.com --check-only` → **[PASS]**, pricing page 1738 visible words.
