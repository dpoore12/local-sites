# Pricing research — orlandomovingcompanypros.com (Orlando, FL, moving)

All figures retrieved **2026-08-23** unless noted. Build status: **[PASS]**, pricing page 1,747 visible words.

## Anchors (government / BLS only)

| Anchor | Value | Source | URL |
| --- | --- | --- | --- |
| Florida mover registration, per year | $300 | Fla. Stat. 507.03(3)(a) | https://www.flsenate.gov/Laws/Statutes/2024/0507.03 |
| Civil penalty, operating unregistered; 1.5-inch truck lettering | up to $5,000 | Fla. Stat. 507.07 | https://www.flsenate.gov/Laws/Statutes/2024/507.07 |
| Median hourly wage, 53-7062 Laborers and freight/stock/material movers, Orlando-Kissimmee-Sanford (area 0036740) | $18.57 (emp 24,080) | BLS OEWS May 2025, release 2025A01 | https://www.bls.gov/oes/current/oes_36740.htm |

BLS series ID: **OEUM003674000000053706208** (area 0036740, occ 53-7062, datatype 08 = median hourly).
Retrieval method: `bls.gov/oes` and `api.bls.gov` both blocked; figure pulled from the OEWS flat-file release
`https://download.bls.gov/pub/time.series/oe/oe.data.0.Current` with a browser user agent (local copy `/home/user/workspace/oe_current.txt`).

Supporting statute detail used on the page: 507.03 requires the registration number on each estimate and contract;
507.07 requires the mover name and registration number on the driver's side of the truck in lettering ≥1.5 inches.
FDACS program page: https://www.fdacs.gov/Business-Services/Moving-Companies

Not usable: City of Orlando loading-zone / moving-truck tag fees are published only at an **http** URL, and no https
equivalent was found, so no city fee anchor appears on this page.

## Operator sources (posted figures)

| Company | URL | Posted figures |
| --- | --- | --- |
| Liberty Moves Orlando | https://www.libertymovesorlando.com/orlando-moving-cost | 2 movers + truck $130–180/hr; 3 + truck $170–230; 4 + truck $220–290; 5 + 2 trucks $300–400; truck, fuel, materials, mileage included. Totals: studio $400–700 (3–4 hrs), 3-BR $1,200–1,800 (6–8 hrs), 5+BR $2,500–5,000+ |
| We Like To Move It Movers | https://weliketomoveitmovers.com/ | 2 movers $134.99/hr, 3 $164.99, 4 $194.99, 5 $224.99, 6 $249.99; **3-hour minimum**; truck/fuel/tolls/materials included; customer pays return travel time to the shop; 3.5% card fee |
| Easy Moving Pros | https://easymovingpros.com/ | labor-only 2-man $90/hr, 2-hour minimum ($180); customer supplies truck |
| Happy Moving LLC | https://www.happymovingllc.com/ | 1 helper $75/hr, 2 $150/hr, 3 $225/hr, 4 $300/hr; 2-hour minimum; labor only |
| UniMovers Orlando | https://unimovers.com/movers/fl/orlando/ | 2 movers $120/hr, 3 $180, 4 $240; additional movers $60/hr each; labor only |
| Orlando Express Movers | https://orlandoexpressmovers.com/orlando-moving-cost/ | studio $350–550 (2 movers, 2–3 hrs, standard fuel charge included), 1-BR $500–750, 2-BR $750–1,100 (2–3 movers, 4–5 hrs), 3-BR $1,400–2,200 (3–4 movers, 5–8 hrs), 4+BR $2,200+; "local" = within ~30 miles |
| Toro Movers | https://toromovers.com/blog/how-much-does-a-local-move-cost-orlando | job averages: studio $340, 1-BR $460, 2-BR $725, 3-BR $1,625, 4-BR $1,860, 5+BR $2,850; crew bands $100–150 (2), $150–270 (3), $200–400 (4); states no per-mile or fuel surcharge |
| Cento Moving | https://centomoving.com/cost-to-hire-movers-in-orlando/ | 2 + truck $120–150/hr, 3 + truck $170–200, 4 + truck $210–260; studio/1-BR $600–1,100; 2–3 BR $1,100–2,000; 4BR+ $2,500+ |

## Rows as published, and how low/high were set

1. **Two movers and a truck, hourly — $120–180.** Low = Cento $120; high = Liberty $180. Also cites We Like To Move It $134.99 and Toro's $100–150 band.
2. **Three movers and a truck, hourly — $150–270.** Low and high both from Toro's 3-crew band $150–270; Liberty $170–230 and We Like To Move It $164.99 sit inside it.
3. **Two-person labor crew, no truck — $90–150.** Low = Easy Moving Pros $90; high = Happy Moving $150 (two helpers at $75 each); UniMovers $120 sits between.
4. **Posted minimum before a box moves — $180–405.** ITEMIZED TOTAL. Low = Easy Moving Pros $90/hr × 2-hour minimum = **$180**. High = We Like To Move It $134.99/hr × 3-hour minimum = **$404.97**, rounded down to $405 for a whole-dollar row. Happy Moving = $150 × 2 = $300 sits between.
5. **Studio or one-bedroom — $340–750.** Low = Toro studio average $340; high = Orlando Express 1-BR ceiling $750; Liberty studio $400–700 inside.
6. **Two-bedroom under 30 miles — $725–1,100.** Low = Toro 2-BR average $725; high = Orlando Express 2-BR ceiling $1,100. Cross-check by build-up: We Like To Move It 3 movers $164.99 × 5 hrs = $824.95, plus 0.5 hr posted return travel time ($82.50) = **$907.45**, plus the posted 3.5% card fee if paid by card = **$939.21** — inside the row.
7. **Three-bedroom local — $1,200–2,200.** Low = Liberty $1,200; high = Orlando Express $2,200; Toro average $1,625 inside.

## Rejected / not used

- Aggregators and national cost guides excluded per brief (angi, homeadvisor, thumbtack, homeguide, moving.com-style lead pages).
- Orlando Express Movers, Toro and Cento present their figures as market/typical ranges for Orlando rather than a company rate card; they are local operators publishing figures on their own domains, and are cited as such ("posted job averages", "posted hourly bands"). Liberty and We Like To Move It are the clearest own-rate sources.

## Notes / caveats

- Every row cites 3–4 distinct hostnames; hostname uniqueness verified programmatically.
- Card processing fees (3.5% at We Like To Move It) and return-travel-time billing are real Orlando structures and are described in the body rather than embedded in a row range.
- No city-level Orlando permit or loading-zone fee is cited because only an http source was found.
