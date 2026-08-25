# coloradospringsfurnacerepair.com — phase 2 complete

## PASS line

```
[PASS] coloradospringsfurnacerepair.com -- home 1746 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           343 words  /about/
           654 words  /contact/
          1355 words  /furnace-blower-motor-repair/
          1315 words  /furnace-ignition-repair/
          1402 words  /furnace-repair/
          1294 words  /furnace-tune-up/
          1877 words  /
          1746 words  /pricing/
           597 words  /services/
exit=0
```

Command: `cd /home/user/workspace/local-sites && python3 template/build.py --check-only coloradospringsfurnacerepair.com`

## What changed

- `sites/coloradospringsfurnacerepair.com/copy.md` only, plus `"phase": 1` → `"phase": 2` in that site's `site.json`.
- Symptom teasers 1–4 shrunk to 61–63 authored words each (titles and order untouched).
- Added `services_summary` (107 words), `services_pick_head` (8), `crosslink_head` (5).
- Added four service pages using site.json slugs exactly: `furnace-repair` (lede 44 / body 879), `furnace-tune-up` (36 / 778), `furnace-ignition-repair` (42 / ~790), `furnace-blower-motor-repair` (40 / 830).
- `pricing_body` prose trimmed from 1815 → 1746 visible words. No dollar figure or fee removed: $50 / $75 / $40 permit fees, $50 / $100 / $200 re-inspections, $900 ENERGY STAR rebate, $99–$249 tune-up all still present.

## Differentiator

Altitude carries the site: 6,035 ft derating of gas input (two legitimate methods and the ~24% vs ~16% gap), orifice/pressure-switch changes, the manufacturer ban on derating via manifold pressure, combustion air in tight houses, depressurization plus radon fans in the same mechanical room, and Pikes Peak Regional Building Department as the permit authority for eight jurisdictions.

## 3 strongest verified local facts

1. Colorado Springs elevation **6,035 feet**, from the city's own budget profile — https://coloradosprings.gov/system/files/2024-03/2024fbudget-00-04-glanceprofile.pdf — combined with the fuel-gas rule that nameplate input applies only to 2,000 feet and must be reduced 4% per 1,000 feet above sea level, per AHJ, or per manufacturer instructions — https://up.codes/s/high-altitude
2. **PPRBD is the permit authority**, not a city building department: it serves Colorado Springs, unincorporated El Paso County, Fountain, Manitou Springs, Monument, Palmer Lake, Green Mountain Falls and Woodland Park (Teller County), lists furnaces as permit work, and limits homeowner permits to owner-occupied residences — https://www.pprbd.org/Information/HomeownerPermit ; its inspectors' top-5 mechanical mistakes include a mechanical room without combustion air and a missing CO alarm on any level with a bedroom — https://www.pprbd.org/File/Resources/Downloads/ResidentialHandout/Residential%20Mechanical%20Mistakes.pdf
3. **Manufacturer derate mechanics**: orifice size, not manifold pressure (2.15 mm → 2.05 mm, one orifice per 20,000 Btu/h, 50 in-lb) — https://docs.johnsoncontrols.com/ductedsystems/api/khub/documents/VunWlFwosRrP2twOx5drnA/content ; high-altitude pressure switch required on 90-plus furnaces above 5,000 ft — http://pts.myrheem.com/docstore/webdocs/ServiceDocs/histlib/pdfs/Accessories/RXGY/92-24096-06-04_RXGY-F18-F42_High_Alt_Kit.pdf ; unreduced input can cause premature heat exchanger failure from excessive temperature rise — https://hvacdirect.com/media/pdf/Goodman_HASFK_2_Manual.pdf

Supporting climate and safety facts used: NWS Pueblo normals (Jan mean 31.7 F, 32.5 in annual snowfall) https://www.weather.gov/pub/climateCosDailyNormalsRecords , record low −27 F on Dec 9, 1919 https://www.weather.gov/pub/climateCosDecemberExtremes , Chinook gusts 60 to near 100 mph near the foothills https://www.weather.gov/pub/winterpreparednessweekwind , 92 mph airport gust Dec 15, 2021 https://www.weather.gov/pub/ExtremeWindEvent_20211215 , CSU gas-odor and blue-flame/vent-cap guidance https://www.csu.org/safety/natural-gas and https://www.csu.org/safety/carbon-monoxide , combustion air 50 cu ft per 1,000 Btu/h and 0.35 cfm/1,000 Btu/h https://www.energy.gov/sites/prod/files/2013/12/f6/combustion_safety_codes.pdf , 3 ACH50 tightness and a single 300 cfm fan defeating natural draft https://basc.pnnl.gov/code-compliance/rooms-containing-fuel-burning-appliances-code-compliance-brief , EPA radon Zone 1 for El Paso County https://www.epa.gov/sites/default/files/2014-08/documents/colorado.pdf with about half of Colorado homes above 4 pCi/L https://cdphe.colorado.gov/hm/understanding-radon , PPRBD 130 mph Vult and Exposure C https://www.pprbd.org/File/ByAlias/DesignCriteria .

## Brief items I could not satisfy as written

- **Heating-degree-day data**: no HDD figure for Colorado Springs appears on any NWS/NOAA primary page I could fetch, so HDD is deliberately absent and the cold case is made with 1991–2020 normals and station records instead. (Denver's page uses HDD, so this also reduced collision risk.)
- **Winter outdoor design temperature**: PPRBD's Basic Design Information page publishes snow, wind and seismic criteria but no winter design temperature, so none is stated.
- Two sources were unavailable: `up.codes/s/combustion-air` (blocked by robots) and the EPA local-radon-zone lookup page (4xx). Worked around with DOE/PNNL code briefs and the EPA Colorado radon PDF.
- **site.json vs brief**: no disagreement found. site.json's city, county, phone, six neighborhoods, four slugs and local_facts were used as authority throughout.
