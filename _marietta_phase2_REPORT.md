# Marietta Garage Door Repair Pros — Phase 2 conversion report

Site: `mariettagaragedoorrepairpros.com` (Marietta, GA — Cobb County — Garage Door Repair)
Files changed: `sites/mariettagaragedoorrepairpros.com/copy.md`, `sites/mariettagaragedoorrepairpros.com/site.json` (`"phase": 1` → `2`). Nothing else touched.

## Build check — PASS

```
[PASS] mariettagaragedoorrepairpros.com -- home 1746 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           324 words  /about/
           557 words  /contact/
          1466 words  /garage-door-opener-repair/
          1539 words  /garage-door-replacement/
          1539 words  /garage-door-spring-repair/
          1838 words  /
          1464 words  /off-track-garage-door-repair/
          1746 words  /pricing/
           549 words  /services/
EXIT=0
```

Slugs: `garage-door-spring-repair`, `garage-door-opener-repair`, `off-track-garage-door-repair`, `garage-door-replacement`.

- Pricing landed at 1746 of the 1750 ceiling. Trimmed prose only — every dollar figure and fee retained ($5 per $1,000, $50 base/minimum, $50/$75/$100 reinspection escalation, $23.86 metro Atlanta median hourly wage).
- `python3 qc.py mariettagaragedoorrepairpros.com` → **0 findings** (the 8 initial MED findings — 3 spelling, 5 flow — were all fixed: "porte-cochere", "interstream", "unapprovable" removed; two 52/62-word runaway sentences split; two ~190-word runaway paragraphs split).
- 15-word-run collision check against all 82 sibling `copy.md` files → **0 shared runs**. Three passages were rewritten to clear collisions with Ann Arbor (cable/drum sentence), Boca Raton (DASMA rust wording and winding-bar warning), and Fort Worth (off-track lede).

## 3 strongest verified local facts

1. **Marietta permits and inspects inside the city limits; Cobb County covers the unincorporated remainder — and the city's fee is valuation-based.** A permit is required whenever an owner or contractor intends to construct, enlarge, alter, repair, move or demolish a building or structure; residential fees run **$5 per $1,000 of total construction cost (labor + materials) with a $50 base fee and no plan review fee**, and reinspections escalate **$50 → $75 → $100** for the third and each additional visit. https://www.mariettaga.gov/443/Building-Permits (jurisdiction split confirmed at https://www.cobbcounty.gov/community-development)

2. **Historic review precedes the permit, and the city's own guidelines specifically address garages.** In **August 2013** a portion of Kennesaw Avenue became Marietta's **first locally designated historic district**, requiring a Certificate of Appropriateness; five further districts (Atlanta–Frasier Street, Church–Cherokee, Northwest Marietta, Washington Avenue, Whitlock Avenue) are on the National Register. https://www.mariettaga.gov/398/Historic-Districts-Local-Landmarks — The Church Cherokee homeowners' handbook states garages, carriage houses and accessory structures are important elements of a historic residential district, should get the same aesthetic care as the house when visible from the public right-of-way, and that **attached garages debuted in the 1940s and gained popularity in the 1950s** while earlier families kept a **single small bay with one door**. https://www.mariettaga.gov/DocumentCenter/View/605 — Downtown, a Certificate of Approval must be approved before a building permit will issue. https://www.mariettaga.gov/DocumentCenter/View/1479/Application-for-Certificate-of-Approval

3. **The climate and the soil are both documented, and both explain local failure modes.** NWS Atlanta/Peachtree City: north Georgia away from the mountains averages **50 to 55 inches of rain**, measurable precipitation on about **120 days**, and **thunder on 50 to 60 days** a year, with summers arriving as long spells of warm humid weather. https://www.weather.gov/ffc/clisumlst — The **Cecil** series mapped across Cobb's Piedmont uplands sits on divides, ridges and side slopes at **0 to 25 percent** slopes, with a Bt horizon of **red clay described as firm, sticky and plastic**, bedrock beyond 60 inches, and **medium surface runoff**. https://soilseries.sc.egov.usda.gov/OSD_Docs/C/CECIL.html — DASMA TDS 190 states springs must be kept dry because rust reduces the effective area of the spring wire and corrosion pits accelerate fatigue cracking. https://www.dasma.com/wp-content/uploads/pubs/TechDataSheets/CommercialResidential/TDS190.pdf

## Supporting sources also used in the copy

- Georgia state minimum codes: mandatory **2024 IRC with Georgia amendments** and **2023 NEC with Georgia amendments**. https://dca.georgia.gov/community-assistance/construction-codes/current-state-minimum-codes-construction
- Georgia Secretary of State: **Overhead Doors** is a traditional specialty; specialty contractors working in their specialty need no residential/general contractor license but must comply with all applicable codes and ordinances. https://sos.ga.gov/page/traditional-specialty-contractors-policy-statements
- Marietta stand-alone MEP inspections in occupied homes by video call, same day, requested at 770-794-5659 Option 8; homeowner-as-contractor per O.C.G.A. 43-41-17(h). https://www.mariettaga.gov/faq.aspx?TID=88
- 16 CFR Part 1211: applies to operators manufactured on or after **January 1, 1993**; reversal must initiate **within 2 seconds of contact**; red manual-release handle adjustable to **6 feet** above the floor, detaching under a maximum of **50 pounds**. https://www.govinfo.gov/content/pkg/CFR-2023-title16-vol2/pdf/CFR-2023-title16-vol2-part1211.pdf
- DASMA TDS 167 (checklist: photoeye beam no higher than 6 inches, 1½-inch object contact-reversal test, extension-spring containment cable, do not operate a door with a broken spring). https://www.dasma.com/wp-content/uploads/pubs/TechDataSheets/CommercialResidential/TDS167.pdf
- DASMA wood door guidance: inspect and maintain **every 12 to 18 months**, finish all six sides before installation, bottom section wicks the most moisture. https://www.dasma.com/how-to-inspect-and-maintain-wood-garage-doors/
- DASMA TDS 161: jamb-to-framing connection is as important as the door; anchor schedules cover **10 to 60 PSF** wind load. https://www.dasma.com/wp-content/uploads/pubs/TechDataSheets/CommercialResidential/TDS161.pdf

## Could not verify — written around, never invented

- Marietta median year housing built (Census API requires a key; data.census.gov needs JS). The copy uses the Church Cherokee handbook's documented garage-era narrative instead of a housing-age statistic.
- No numeric torsion spring cycle rating is published in DASMA TDS 190, so no cycle count is asserted.
- Cecil clay is **kaolinitic** (low-activity), so the copy frames the soil as a runoff, drainage and settling issue and makes no shrink-swell/expansive-clay claim.
