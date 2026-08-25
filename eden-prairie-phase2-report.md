# Eden Prairie garage door pages — phase 2 conversion report

## Build result

```
[PASS] edenprairiegaragedoorrepairpros.com -- home 1747 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           375 words  /about/
           589 words  /contact/
          1488 words  /garage-door-opener-repair/
          1536 words  /garage-door-replacement/
          1471 words  /garage-door-spring-repair/
          1926 words  /
          1489 words  /off-track-garage-door-repair/
          1747 words  /pricing/
           608 words  /services/
```

`python3 template/build.py --check-only edenprairiegaragedoorrepairpros.com` exits 0.
`site.json` `"phase"` flipped 1 → 2 (nothing else changed).

Slugs used exactly as in site.json: `garage-door-spring-repair`, `garage-door-opener-repair`,
`off-track-garage-door-repair`, `garage-door-replacement`.

Differentiator: extreme cold as the spine — frozen bottom seal read as an obstruction by the
federal reversal rule, frosted photo-eyes, thickened grease loading the head, cold battery
capacity loss in keypads/remotes, frost depth and a racked jamb, and forcing an iced door as the
actual cause of bent panels and parted cables.

Collision guard: zero 15-word runs with any of the 82 sibling sites. The initial draft shared 39
runs with Ann Arbor (the other cold-climate garage door site) across the off-track and replacement
material; all of those passages were rewritten from scratch rather than reworded, and the federal
16 CFR 1211 content is built on different clauses than Ann Arbor's (the 1-to-4-unit/600-volt
definition, the 30-second lower-limit timeout, and the certification test parameters — 1-inch
object, 25 lbf, 50 cycles — instead of Ann Arbor's section-by-section citations).

## Three strongest verified local facts

1. **MSP January normals and sub-zero counts.** The 1991-2020 normals give a January daily max of
   23.6°F, daily min 8.8°F, monthly mean 16.2°F, 10.0 nights at or below 0°F and 22.7 days with a
   max at or below 32°F
   (https://files.dnr.state.mn.us/natural_resources/climate/twin_cities/msp_normals_means_extremes_page3.pdf).
   NWS Twin Cities puts the current winter average at 19 sub-zero lows, the record at 58 in
   1874-75, and the all-time low at −41°F on January 21, 1888
   (https://www.weather.gov/media/mpx/Climate/What%20Winter%20MSP.pdf).

2. **Frost depth is a code number, not a talking point.** Minnesota Rules 1303.1600 sets the
   minimum footing depth due to freezing at 5 feet in Zone I and 3-1/2 feet in Zone II, and
   Hennepin County is Zone II (https://www.revisor.mn.gov/rules/1303.1600/). The DNR frost-tube
   record near St. Paul shows a deepest reading of 35.2 in (2007-08), a median maximum near 20 in,
   frost in the ground from late November into the second week of April, and roughly 4 in of fluffy
   snow acting as insulation
   (https://www.dnr.state.mn.us/climate/journal/frost-depth-minnesota-winter-2025.html).

3. **A garage-door-only firm is a specialty contractor and needs no state license.** MN DLI
   requires the residential building contractor/remodeler license only when a contractor deals
   directly with a one-to-four-unit residential owner in *more than one* special skill; carpentry
   covers "doors, windows and skylights," and "specialty contractors who provide only one special
   skill are not required to have a state license (except residential roofers)," with a $15,000
   gross-receipts Certificate of Exemption
   (https://www.dli.mn.gov/business/residential-contractors/residential-contractor-licensing).
   Cities cannot require a local license of a state-licensed contractor
   (https://www.dli.mn.gov/business/residential-contractors/residential-contractor-faqs).

Full source list with every URL: `eden-prairie-phase2-research.md`.

## Things in the brief that were wrong or unverifiable

- **"Whether an attached Minnesota garage is required to be sealed or insulated under the state
  energy code."** No such requirement exists. Chapter 1322 treats a garage as unconditioned space
  (grouped with attics and ventilated crawl spaces for the R-8 duct requirement) and only demands
  full compliance when a nonconditioned space is *altered to become* conditioned
  (https://www.revisor.mn.gov/rules/1322/full). Written that way on the replacement page.
- **"Whether a garage door contractor needs the DLI license."** The brief implies yes; the verified
  answer is no for a single-special-skill firm. See fact 3.
- **Torsion spring steel metallurgy at low temperature, and "springs disproportionately break in
  the first hard freeze."** No primary source states either. Both are written as mechanism and
  trade pattern with no number attached: added system resistance from thickened grease, plus
  DASMA TDS 190 listing extreme cold among cycle-life-shortening climates and rust reducing the
  effective wire area (https://www.dasma.com/wp-content/uploads/pubs/TechDataSheets/CommercialResidential/TDS190.pdf).
- **Frost heave mechanism from MnDOT.** MnDOT pages cover spring-thaw load restrictions, not garage
  frost heave, so the frost section is grounded in DNR frost-tube depths and Rules 1303.1600.
- **Eden Prairie permit distinction.** The city FAQ does not enumerate garage doors. It states
  permits are required whenever the work is regulated by the state building code, including work on
  permanent weather-resistive surfaces, and names garages as permit work
  (https://www.edenprairiemn.gov/doing-business/building-inspections). The spring/opener-versus-
  replacement line is drawn from that language rather than from a garage-door-specific rule, and is
  worded to send the reader to 952-949-8342.
- **Neighborhood dating.** Only The Preserve has a primary-source date (1971 land purchase,
  association incorporated May 1972 — https://preserveassociation.com/history-of-the-preserve/).
  Bearpath, Olympic Hills, Bent Creek, Homeward Hills and Edenvale are named without decades.
- No site.json / brief contradiction on city, state, county or slugs.

## Notes

- Pricing did **not** overflow: it started at 1741 and finished at 1747, both under the 1750
  ceiling. No dollar figure or fee was removed anywhere. The replacement service page did overflow
  (1582 → 1536) and was trimmed by tightening prose only.
- Dollar amounts were deliberately kept off the service pages; the replacement page lists permit
  and state surcharge as line items to ask for, without amounts. Permit fee schedule figures live
  on the pricing page.
- The staging file `_ep_new_blocks.md` was removed after its contents were spliced into `copy.md`;
  nothing in it is lost — all of it is in the site's `copy.md`, in revised form.
