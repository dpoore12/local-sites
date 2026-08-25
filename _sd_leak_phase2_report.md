# sandiegoleakdetectionpros.com — Phase 2 conversion report

## Build result

```
[PASS] sandiegoleakdetectionpros.com -- home 1731 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           379 words  /about/
           607 words  /contact/
          1963 words  /
          1361 words  /pool-leak-detection/
          1731 words  /pricing/
           578 words  /services/
          1491 words  /slab-leak-detection/
          1462 words  /underground-leak-detection/
          1547 words  /water-leak-detection/
```
exit 0. `site.json` `"phase": 2`. Pricing page came in at 1731, under the 1750 ceiling, so no dollar figure or fee was removed — all 24 remain ($249, $495, $129, $199, $218, $238, $367, $8.51, $9.50, $11.89, $35.53, $264.25, $87.68, $264.25, $52.39, $200, $1,500, $500, $2,000, $3,750, $3,950, $150, $250, plus the CSLB $1,000/$1,000/$500 thresholds).

Zero 15-word shingle collisions with any of the eight named siblings. Three initial Phoenix collisions (underground lede opener, "chip an exploratory hole", "belongs on the list too") were rewritten.

## Three strongest verified local facts

1. **The 120-day leak-credit clock, and what it excludes.** A City credit is considered only for a concealed leak in a non-irrigation pipe; irrigation, pool and leaking-fixture losses are excluded by name, the request must reach Public Utilities within 120 days of the first high bill, and it must be supported by a repair invoice carrying the date the leak was discovered and the date repairs were made — [City of San Diego leak adjustment policy](https://www.sandiego.gov/public-utilities/customer-support/leak-adjustment).
2. **A leaked unit of water is billed twice, into a tier that just rose 14.7 percent.** Single-family volumetric rates effective Jan 1, 2026 are $8.51 / $9.50 / $11.89 per HCF over a $35.53 base ([water billing rates](https://www.sandiego.gov/public-utilities/customer-support/water-billing-rates)), the single-family sewer charge is computed from 95 percent of metered water at $5.92/HCF capped at 20 HCF ([sewer billing rates](https://www.sandiego.gov/public-utilities/customer-support/sewer-billing-rates)), and Council approved a 14.7 percent water and 6 percent wastewater increase on Oct 28, 2025 with up to 14.5 percent more for Jan 2027 and a court-forced unitary volumetric rate under *Patz v. City of San Diego* ([rate increases](https://www.sandiego.gov/public-utilities/customer-support/water-and-sewer-rates-increases)).
3. **The City's own geologic work names utility leakage as a cause of slab heave.** Very old paralic deposits capping the mesas form expansive, highly plastic residual clay whose expansion can cause unacceptable settlement or heave of concrete slabs supported on grade, and the listed moisture-change causes include precipitation, landscape irrigation, roof drainage, perched groundwater, drought and utility leakage ([University Community desktop geotechnical and geologic hazard evaluation](https://www.sandiego.gov/sites/default/files/2024-03/app-e_desktop-geotechnical-and-geologic-hazard-evaluation-university-community-plan-update-april-2020.pdf)). Paired with the City's submittal rule that a foundation plan must show the tendon layout for a post-tension slab ([project submittal requirements §2](https://www.sandiego.gov/sites/default/files/dsdpsm_sec_02.pdf)).

Also verified and used: the 30-minute meter-dial test and its suspect list ([leaks page](https://www.sandiego.gov/public-utilities/customer-support/leaks)); the ownership boundary — owner maintains the system from the meter onward, and on the property side the City keeps up only the gasket and washer ([meter/pressure page](https://www.sandiego.gov/public-utilities/customer-support/meter-water-pressure-plumbing-system), [water emergency procedures](https://www.sandiego.gov/sites/default/files/legacy/water/pdf/operations/emergency.pdf)); claims handling for main breaks and backups ([Council Policy 400-10](https://docs.sandiego.gov/councilpolicies/cpd_400-10.pdf)); permit fees $264.25 / $87.68 ([Information Bulletin 103](https://www.sandiego.gov/development-services/forms-publications/information-bulletins/103)); CSLB $1,000 license threshold, 10%/$1,000 down-payment cap, and C-36 scope ([CSLB consumer guide](https://www.cslb.ca.gov/Resources/GuidesAndPublications/WYSKbro_ENG0525_ADA.pdf), [C-36 classification](https://www.cslb.ca.gov/about_us/library/licensing_classifications/Licensing_Classifications_Detail.aspx?Class=C36)); July ETo 5.7 in ([county WELO manual appendix A](https://www.sandiegocounty.gov/content/dam/sdc/pds/docs/Landscape/WELDManual-Appendix-A.pdf)); ~85% of rain Nov–Mar, ~2% Jun–Aug ([NWS TM-275](https://www.weather.gov/media/wrh/online_publications/TMs/TM-275.pdf)).

## Things in the brief or site.json I found to be wrong

- **"six to ten weeks" for the leak-adjustment review is not a City figure.** The City page says eight to ten weeks in its instructions and six to eight weeks in its own FAQ on the same page. The phase-1 pricing anchor's "six to ten weeks" matches neither, so I changed the pricing copy to the City's instruction figure (eight to ten weeks) and disclosed both figures on the water page.
- **AMI leak alerts could not be verified as a present-day feature.** The adopted FY26 capital program (project S17008, ~280,000 meters, $126.5M, 2017–2031) says implementation of the deployment plan is *anticipated to begin in fiscal 2027*, after a pilot of ~11,000 connections in FY2013–2015 ([FY26 adopted budget, Public Utilities](https://www.sandiego.gov/sites/default/files/2025-08/fy26ab_v3pud.pdf)); a 2020 audit found only ~16,000 meters (6%) read remotely ([AMI implementation audit](https://www.sandiego.gov/sites/default/files/20-002_ami_implementation.pdf)). I wrote the page to say most accounts still get periodic reads rather than claiming leak alerts exist.
- **The CSLB threshold is $1,000, not $500.** $500 survives only as the written-contract threshold for home improvement, which is a different rule; I used both correctly.
- **The City contradicts itself on the size of an HCF**: 748.05 gallons (rates page), 748.5 (meter page), 748 (sewer page). I wrote "roughly 748 gallons."
- No conflict arose between site.json and the brief on city, state, service slugs, neighborhoods or the three local facts — site.json's slugs and fact set were used exactly as given.
