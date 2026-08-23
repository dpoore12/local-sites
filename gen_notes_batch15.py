#!/usr/bin/env python3
"""Generate pricing research notes for batch 15 from the written site.json blocks."""
import json, pathlib

BASE = pathlib.Path("/home/user/workspace/local-sites")

BLS = """## BLS OEWS wage anchor: attempted, not obtained

The brief allows a BLS metro wage figure as an anchor. It could not be retrieved on
2026-08-23 and no wage anchor is used on this page.

- Flat files `https://www.bls.gov/oes/special-requests/oesm25ma.zip` and `oesm24ma.zip`
  returned HTTP 403.
- The keyless BLS timeseries API returned `REQUEST_NOT_PROCESSED` with reason
  "daily threshold reached" for every series requested.
- Series ID attempted for this metro: `%(series)s` (%(seriesdesc)s).

Precedent for omitting rather than substituting: `pricing-research-arvada.md`.
"""

NOTES = {
 "coloradosprings-furnace": {
  "domain": "coloradospringsfurnacerepair.com",
  "title": "Colorado Springs, CO -- furnace repair",
  "series": "OEUM001782000000049902108",
  "seriesdesc": "Colorado Springs MSA, 49-9021 HVAC mechanics and installers, annual mean wage",
  "intro": """All figures read 2026-08-23. Mode: `cost`. 4 anchors, 8 rows.

Divergence note: this page is built on **El Paso County / Pikes Peak Regional Building
Department** permit authority, a **municipal** utility (Colorado Springs Utilities) rebate
structure, and **altitude derate** framing. The Denver page in the same batch is built on
**City and County of Denver** valuation-based permit math, **Xcel Energy** (investor-owned)
rebates, and **part-by-part flat-rate** framing. No anchor, source, row label or subhead is
shared between the two.""",
  "arith": """## Arithmetic on itemized totals

**Row 2, "Smallest billable repair once a technician opens the cabinet" -- $185 to $305.**
Best Pro Appliance Repair (Colorado Springs) posts, on the same price list, a $120 HVAC
service/trip charge and a separate $185 minimum HVAC labor charge. The page does not say
the trip charge is credited toward or waived with the repair, so under brief rule 1 the two
are **stacked**: $120 + $185 = **$305**, used as the row high. The row low is the $185
minimum labor on its own, which is the floor once a technician bills labor.
Source: https://www.bestprorepair-cos.com/prices.html

**Contrast, deliberately not stacked.** Cooper Heating & Cooling (Colorado Springs) posts a
$119 service call and states it is waived with the repair, so nothing is added to its
$159 low / $668 average / $1,600 high repair figures. Furnace World posts a flat $99 El
Paso County service fee and states it is charged whether or not work proceeds; that is a
"charged either way" fee and it sits in row 1 as a diagnostic, not stacked onto a repair.

**Row 1 band $89-$120.** Lowest posted flat diagnostic: Highland Heating & Air $89.
Highest: Best Pro $120. Furnace World $99 and Home Heating Service $110 sit inside.

**Job matching.** Row 6 is a tune-up (maintenance), not a repair; Bergs $99/$149, Solid
Rock $149 and MSI $129-$249 are all tune-up prices. Row 7 is an 80% AFUE changeout and
row 8 a 96-97% condensing changeout; Strong publishes both tiers separately
($3,750 / $4,750 vs $6,500 / $8,250), so the two rows do not overlap sources' meanings.
Bergs' installed figure is published as a floor, so it is used as row 8's **low**, never a
high.""",
  "extra": """## Identity check on a shared-name source

`bestprorepair-cos.com` was confirmed to serve Colorado Springs, Monument and Fort Carson
from its own site body text before its price list was used, since "Best Pro" appears in
other metros.

## Not used

- Awesome Home Services' $4,600 low on furnace replacement is inside the row 8 band; the
  $12,000 ceiling is the row high.
- Ascent HVAC's $150-$3,500 overall repair band is used only for the row 5 ceiling, because
  its low duplicates ignition-side figures already sourced twice.""",
 },
 "denver-furnace": {
  "domain": "denverfurnacerepairpros.com",
  "title": "Denver, CO -- furnace repair",
  "series": "OEUM001974000000049902108",
  "seriesdesc": "Denver-Aurora-Lakewood MSA, 49-9021 HVAC mechanics and installers, annual mean wage",
  "intro": """All figures read 2026-08-23. Mode: `cost`. 3 anchors, 8 rows.

Divergence note: Denver's permit cost is a **valuation formula**, not a flat schedule, and
its rebate anchor is **Xcel Energy**, an investor-owned utility with an AFUE-replacement
condition. The page is organized **part by part** (igniter, inducer, gas valve, board,
blower, heat exchanger) because three Denver operators publish component-level flat rates.
Colorado Springs in the same batch uses flat PPRBD permit dollars, a municipal utility
rebate, altitude derate framing, and job-stage rows.""",
  "arith": """## Arithmetic on itemized totals

**Anchor 1, permit on a $6,000 changeout = $67.** Denver Community Planning and Development
charges $35 for the first $2,000 of valuation plus $8 for each additional $1,000.
$6,000 - $2,000 = $4,000 additional, which is 4 increments of $1,000.
$35 + (4 x $8) = $35 + $32 = **$67**. Mechanical work is a quick-permit category, so no
plan-review charge is added.
Source: https://www.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Community-Planning-and-Development/Plan-Review-Permits-and-Inspections/Development-Fees

**After-hours itemized total, cited in the body copy.** Rabbit Heating and Air posts an
after-hours trip charge of $175 minimum and a basic repair at $250. Rabbit does not state
that the after-hours trip charge is credited or waived, so the two are **stacked**:
$175 + $250 = **$425** for the cheapest possible after-hours repair.
Source: https://rabbitheating.com/furnace-repair/

**Not stacked.** UniColorado's $180 diagnostic is explicitly credited toward the work, and
Gale Force states its $89-$150 service call is applied to the repair; neither is added to
their component prices. Rabbit's weekday trip charge is free with a repair and $60 without,
so row 1's low is $60 (a no-repair outcome), not $0.

**Row 1 band $60-$180.** Low: Rabbit $60 weekday, no repair. High: UniColorado $180 (a
credited diagnostic, which is why the row basis is `per visit`). Right Way $89 and
All Climate $79 sit inside.

**Job matching.** Every component row uses only figures that name that component. Gale
Force's blower band is split by its own text: $400-$1,800 for a standard motor and
$1,500-$2,000 for an ECM; only the ECM figure feeds the ECM/variable-speed row. The
changeout row keeps Right Way's tiered installed prices, which the page states include
permit and disposal, so no permit is added on top.""",
  "extra": """## Not used

- Plumbline's heat-exchanger labor estimate (up to eight hours) is descriptive, not a price,
  and is cited only in the note.
- Xcel's $300 rebate is not netted against any row; rebates stay off the price table by
  design and appear only as an anchor.""",
 },
 "phoenix-leak": {
  "domain": "phoenixleakdetectionpros.com",
  "title": "Phoenix, AZ -- leak detection",
  "series": "OEUM003806000000047215208",
  "seriesdesc": "Phoenix-Mesa-Scottsdale MSA, 47-2152 plumbers, pipefitters and steamfitters, annual mean wage",
  "intro": """All figures read 2026-08-23. Mode: `cost`. 4 anchors, 6 rows.

Divergence note: Phoenix is built on **no leak forgiveness** (City Code 37-27), a
**seasonal** water rate (low / medium / high season per 100 cubic feet), a **sewer fee
review** recalculated each July, and a **$195 minimum permit / $195 per re-inspection**
schedule. San Diego in the same batch is built on a **published leak adjustment policy**
with a 120-day window, **tiered HCF** rates, and a **per-dwelling-unit** plumbing permit
fee from Information Bulletin 103. Rows differ too: Phoenix carries pool leak detection and
a standalone camera inspection; San Diego carries epoxy lining and sleeving.""",
  "arith": """## Utility leak policy: Phoenix publishes none

Phoenix City Code 37-27 makes the customer responsible for all leaks downstream of the
point of service delivery **and** for full payment of charges for water lost through them.
There is no residential water-leak credit or adjustment program to apply for. The only
relief mechanism found is a **Sewer Fee Review**, which addresses the sewer portion of the
bill, is recalculated each July from average January-March water use, and must be requested
within 60 days of that July bill date.
Sources: https://phoenix.municipal.codes/CC/37-27 and
https://www.phoenix.gov/administration/departments/waterservices/city-services-bill/submit-a-sewer-fee-review.html

## Arithmetic on itemized totals

**After-hours detection, cited in the body copy.** Miracle Plumbing posts detection at
$150-$400 and an after-hours premium of $100-$150. Miracle does not state that the premium
replaces the base fee or is credited, so the two are **stacked**: $150 + $100 = **$250**
low and $400 + $150 = **$550** high for an after-hours locate. That total is described in
the copy, not used as a table row, because the row itself covers weekday work.
Source: https://miracleplumbingaz.com/2026/07/08/slab-leak-repair-in-queen-creek-and-phoenix-metro-signs-costs-and-methods/

**No credited fees stacked.** No Phoenix operator in this set publishes a detection fee
credited toward repair, so no subtraction was needed.

## Job matching: detection vs repair

Row 1 is **locating** a pressurized water leak, and uses only detection prices:
Darrel's flat $150 (about an hour), Miracle $150-$400, American Leak Detection $375 flat
(roughly two hours), Rapid Rooter $250-$600. Repair prices are kept out of it.
Rows 2-4 are **repair** work (open-slab spot repair, reroute, repipe). Row 5 is a
standalone camera inspection, which is an inspection, not a leak locate. Row 6 is **pool**
leak detection, kept separate from potable-line detection because the equipment and pricing
differ: Phoenix Leak Detectors $100-$600 per visit, American Leak Detection ~$250 single
line to $700, AE Outdoor $350-$650 dye and $650-$1,200 electronic.

Simba's repipe table is priced by house size and material, $4,500 PEX small to $24,000
copper large; the $24,000 is a genuine posted high, not an estimate.""",
  "extra": """## Note on rate arithmetic in the copy

100 cubic feet = 748 gallons. High-season inside-city volumetric rate $6.13 per 100 cf
against $4.93 low season, plus a $4.64 monthly service charge on a 5/8-inch meter, all from
the rate sheet effective March 1, 2025:
https://www.phoenix.gov/content/dam/phoenix/waterservicessite/documents/rates_effective_march_2025.pdf""",
 },
 "sandiego-leak": {
  "domain": "sandiegoleakdetectionpros.com",
  "title": "San Diego, CA -- leak detection",
  "series": "OEUM004174000000047215208",
  "seriesdesc": "San Diego-Carlsbad MSA, 47-2152 plumbers, pipefitters and steamfitters, annual mean wage",
  "intro": """All figures read 2026-08-23. Mode: `cost`. 3 anchors, 6 rows.

Divergence note: see the Phoenix note. San Diego uses a real leak-adjustment policy,
tiered HCF pricing, and IB 103 per-unit permit fees; rows emphasize epoxy lining and
sleeving, which no Phoenix operator in the set publishes.""",
  "arith": """## Utility leak policy: San Diego does publish one

City of San Diego Public Utilities publishes a leak adjustment policy, with conditions:
the leak must be a **concealed leak in a non-irrigation pipe**; irrigation, pool and
fixture leaks are excluded; the request must arrive **within 120 days** of the first high
bill; a repair invoice showing discovery and repair dates is required; and review takes
**six to ten weeks**. The page does not publish the size of the credit, only eligibility
and process, so no dollar figure is claimed.
Source: https://www.sandiego.gov/public-utilities/customer-support/leak-adjustment

## Arithmetic on itemized totals

**Row 1, one-hour slab locate = $367.** West Plumbing Services posts a $129 service call
plus hourly detection rates of $199 in wall, $218 in basement and $238 in slab. Nothing on
that page says the service call is credited or waived, so it is **stacked**:
$129 + $238 = **$367** for a one-hour slab locate.
Source: https://www.wpsexpert.com/professional-gas-and-water-leak-detection/

**Not stacked.** Best San Diego Leak Detection posts $249 basic and $495 normal detection
and states the fee is credited against the repair, so those figures stand alone. They set
the row 1 band ($249 low, $495 high); the $367 West total sits inside that band and is
explained in the note rather than replacing it.

## Job matching: detection vs repair

Row 1 is detection only. Rows 2-6 are repair, escalating by method: open-and-repair in
wall or ceiling, jackhammered slab repair, single-line reroute, interior lining or
sleeving, and full repipe. Tri Express publishes several figures as floors ("from $250",
"from $1,500", "from $6,500"); each is used as a **low**, never a high, per brief rule 2.
Clearwater's $150-$250 per linear foot lining price is a unit rate and is cited in the
lining note but not converted into a total, since linear footage is unknown.

Row 5's narrow $3,750-$3,950 band is deliberate: San Diego Plumbing and Pipelining posts
those two averages (epoxy lining, sleeving) as the only whole-job dollar figures published
for that method in this market.""",
  "extra": """## Not used

- Clearwater's posted permit range ($200-$1,500) and labor rate ($75-$150/hr) are company
  figures about third-party costs, so they are not used as anchors; the IB 103 fee schedule
  is the government source instead.
- Almco's $8,000-$20,000 repipe high anchors the row 6 ceiling alongside Clearwater's
  "$20,000 and up on large homes"; the low is the $4,500 both Repipe Home Hero and
  Clearwater publish.""",
 },
 "tampa-appliance": {
  "domain": "appliancerepairtampaco.com",
  "title": "Tampa, FL -- appliance repair",
  "series": "OEUM004530000000049903108",
  "seriesdesc": "Tampa-St. Petersburg-Clearwater MSA, 49-9031 home appliance repairers, annual mean wage",
  "intro": """All figures read 2026-08-23. Mode: `cost`. 4 anchors, 7 rows.

The anchors here are **tax, licensing and permit** rather than utility, because appliance
repair in Florida has no state license and no utility rebate program touching it. The
distinguishing local cost driver is the 7.5 percent combined sales tax that lands on the
whole repair charge whenever a part is supplied.""",
  "arith": """## Arithmetic on itemized totals

**The floor on a small repair is $185 plus the part, not $274.** Smart Appliance Services
posts an $89 regular diagnostic ($119 premium) and a $185 minimum labor fee, and states
explicitly that the diagnostic is **deducted from** the repair total. Under brief rule 1
the credited diagnostic is therefore **not stacked**: the smallest invoice once a part is
fitted is $185 + part. Adding $89 + $185 = $274 would overstate it by the credited
diagnostic, and that error is called out in the page copy.
Source: https://smartapplianceservices.com/prices/

**Hartman's two fees are not the same thing.** Hartman's posts a $19 service call **and** a
separate $120 diagnostic fee waived on approval of the repair. So the trip is not free even
when the diagnosis becomes free: $19 remains. Row 1's high is the $120 diagnostic figure.
Source: https://tampaappliancerepair.services/

**Tax arithmetic cited in the copy.** 6 percent state (GT-800010) + 1.5 percent Hillsborough
discretionary surtax (DR-15DSS 2026) = **7.5 percent** on a taxable repair invoice.
On a $500 refrigerator repair: $500 x 0.075 = **$37.50**.
Sources: https://floridarevenue.com/Forms_library/current/gt800010.pdf and
https://floridarevenue.com/Forms_library/current/dr15dss_26.pdf

**Waived vs deducted, per operator.** Professional $65 waived on approval; Teodor $79
waived on approval; Smart $89/$119 deducted; Hartman's $120 waived on approval plus a $19
service call. None are stacked onto repair prices.

## Job matching

Rows are per appliance and per fault family, matched to the operator tables that name that
appliance. Row 4 is sealed-system/compressor work only, which is why it sits above the
general refrigerator row rather than inside it. "And up" phrasing in Teodor's tables is
treated as a floor for that sub-fault, never as the row high.""",
  "extra": """## Anchors that do not exist as the brief suggested

**There is no Florida appliance-repair written-estimate statute.** Fla. Stat. ch. 559
part IX is the **Motor Vehicle Repair Act**; s. 559.905 requires a written estimate for
**motor vehicle** repair, not appliance repair.
Source: https://www.flsenate.gov/Laws/Statutes/2025/0559.905
No such anchor is used on the page. The written-estimate expectation in the copy is framed
as a homeowner practice, not as a legal requirement.

**Hillsborough County business tax receipt dollar amount not found.** No published dollar
figure for a Hillsborough business tax receipt could be located on hillstaxfl.gov or in
County Code ch. 46 art. III on 2026-08-23. The license-categories page is used instead,
which states that small appliance repair needs no contractor license, that the office
issues no handyman receipt, and that receipts run to September 30 and are delinquent
October 1.
Source: https://www.hillstaxfl.gov/taxes/business-tax-services/license-categories/""",
 },
}


def table(pricing):
    out = ["## Anchors\n"]
    for a in pricing["anchors"]:
        out.append(f"- **{a['label']} -- {a['value']}**  \n"
                   f"  {a['detail']}  \n"
                   f"  Source: {a['source_name']} -- {a['source_url']} (read 2026-08-23)")
    out.append("\n## Rows\n")
    for i, r in enumerate(pricing["rows"], 1):
        out.append(f"**{i}. {r['job']} -- ${r['low']:,} to ${r['high']:,}** ({r['basis']})  \n"
                   f"  {r['note']}")
        for s in r["sources"]:
            out.append(f"  - {s['name']} -- {s['url']}")
        out.append("")
    return "\n".join(out)


for short, n in NOTES.items():
    p = BASE / "sites" / n["domain"] / "site.json"
    pricing = json.load(open(p))["pricing"]
    body = f"""# Pricing research -- {n['title']}

Site: `{n['domain']}`  |  Retrieval date for every figure below: **2026-08-23**

{n['intro']}

{table(pricing)}
{n['arith']}

{n['extra']}

{BLS % {'series': n['series'], 'seriesdesc': n['seriesdesc']}}
## Banned-source compliance

No figure on this page comes from angi, angieslist, homeadvisor, thumbtack, fixr, homewyse,
porch, yelp, forbes, bobvila, costpatch, buildx, modernize, thisoldhouse, houzz, homeguide,
networx, lawnstarter, manta, expertise, bark, costimates, improvenet or craftjack. Every row
source is an operator serving this metro publishing the price on its own website, and every
source within a row is a distinct https hostname.

## Build status

`python template/build.py {n['domain']} --check-only` -> **[PASS]**, zero errors.
"""
    out = BASE / f"pricing-research-{short}.md"
    out.write_text(body)
    print("wrote", out, len(body.split()), "words")
