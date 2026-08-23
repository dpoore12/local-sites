# Batch 10 — pricing pages for five Dog Bite Lawyer sites (2026-08-23)

All five sites use `pricing.mode = "fees"` with `fee_kind = "contingency"`, 4 sourced
anchors and 6 fee rows each, plus `## pricing_lede` and `## pricing_body` in copy.md.
No page states what any firm charges.

## Build status

`python template/build.py <domain> --check-only` — all five [PASS], zero [ERROR]:

| Site | Pricing page visible words |
| --- | --- |
| atlantadogbitelawyerpros.com | 1535 |
| lasvegasdogbitelawyerpros.com | 1645 |
| losangelesdogbitelawyerpros.com | 1705 |
| newyorkdogbitelawyerpros.com | 1673 |
| sacramentodogbitelawyerpros.com | 1665 |

Full portfolio run `python template/build.py --check-only`: **80 PASS / 3 FAIL of 83**.
The three failures are **not** these five sites and not caused by them. They are
duplicate-phrase collisions among other sites that gained pricing blocks in a
concurrent batch: `sanjoseduilawyerpros.com` (shares runs with
`newportbeachduilawyerpros.com`), `victorvillecaraccidentlawyerpros.com` and
`westcovinacaraccidentlawyerpros.com` (share runs with `salinascaraccidentlawyer.com`
and `santabarbaracaraccidentlawyer.com`). An earlier run of this check showed five
collisions between `losangelesdogbitelawyerpros.com` and those car-accident sites over
quoted California rule text; the Los Angeles page was reworded to paraphrase and now
shares no 15-word run with any other site in the portfolio.

## Authority cited per state

**Georgia (Atlanta)** — Ga. R. Prof. Conduct 1.5(a) reasonableness standard with its
eight factors and no percentage cap; 1.5(c)(1) written contingency agreement with
percentages for settlement, trial and appeal and expense timing; 1.5(c)(2) written
closing statement; 1.5(d) prohibited contingencies. Fulton County Clerk of Superior
Court fee schedule ($215 general civil action, $8 per added party, $50 sheriff service,
$1 motion). Atlanta Code of Ordinances 18-61 ($3.00 annual permit, $10.00 family cap,
$7.50 impoundment plus $3.00 a day).

**Nevada (Las Vegas)** — Nev. R. Prof. Conduct 1.5(a) reasonableness with eight factors
and no cap; 1.5(c) written agreement signed by the client in boldface type at least as
large as the largest type used, with the loss-exposure and harassment warnings in
(c)(4)-(5). NRS 7.095 35 percent net ceiling, which applies only to a professional
negligence action against a health care provider. NRS 18.005 costs list including
$15,000 per expert for up to five experts. Eighth Judicial District Court Clerk filing
fee list ($270 complaint, $223 first appearance, $30 per added party, $200 summary
judgment motion). Clark County Code 10.08.135 ($800 breeder/show permit, $400 reduced
renewal, $100 reinspection). NRS 202.500 for the criminal exposure framing.

**California (Los Angeles)** — Cal. R. Prof. Conduct 1.5(a) unconscionable-or-illegal
standard and 1.5(b)'s thirteen factors; 1.5(c) prohibited contingencies. B&P 6147
(rate in writing, the non-negotiable-by-law notice, voidable at the plaintiff's option).
B&P 6146 25 percent / 33 percent health-care ceiling, expressly flagged as not reaching
a bite claim. Los Angeles Superior Court civil fee schedule ($435 first paper, $150
advance jury fee, $15 daily jury deposit, $0.34 mileage, $764 / $382 / $30 reporter per
diem, $1,000 complex designation per side with the $18,000 case cap). LAMC 53.15.3 and
53.15 ($91.50 and $16.50 processing fee, $8.50 and $3.50 annual tax, 25 percent late
fee, $25.00 field collection).

**California (Sacramento)** — same Rule 1.5(a) standard but built on factor (b)(3),
proportion of the fee to the value of the services. B&P 6147(a)(1),(a)(2),(a)(4),(b).
B&P 6148 $1,000 written-contract threshold, ten-day billing response, thirty-day repeat
requests, voidable at the client's option. Cal. R. Ct. 7.955 reasonable fee standard and
fourteen factors for a minor's recovery. Sacramento Superior Court fee schedule ($225 /
$370 / $435 tiers, $140 reclassification, $60 motion, $500 summary judgment, $20
continuance, $50 venue change, $1,000 complex). Sacramento County Animal Care license
fees ($50 / $15 annual, $10 senior rate, $25 late fee, $5 duplicate tag, $45 ranch or
competition dog, Galt and Isleton amounts).

Los Angeles and Sacramento share no figure and no statutory section other than Rule 1.5
and section 6147, which are handled with different subdivisions, different factors and
different prose. Los Angeles carries 6146, the LA court PDF and the LAMC amounts;
Sacramento carries 6148, Rule of Court 7.955, the limited-civil filing tiers and the
county license amounts.

**New York (Manhattan)** — 22 NYCRR 603.25(e), First Department. Because a dog bite
claim is a personal injury claim and not medical, dental or podiatric malpractice, the
department's published schedule governs: Schedule A at 50 percent of the first $1,000,
40 percent of the next $2,000, 35 percent of the next $22,000 and 25 percent above
$25,000; or Schedule B at not more than 33 1/3 percent where the initial contract so
provides, which forfeits the extraordinary-circumstances application preserved by
603.25(e)(4). 603.25(e)(3) net-or-gross election by the client, with no deduction for
hospital, medical, nursing, self-insurer or carrier liens. Anything above the schedule
is unconscionable absent a written court order under 603.25(e)(1). Judiciary Law 474-a's
30/25/20/15/10 malpractice scale is stated only to say it does **not** govern a bite
claim. Judiciary Law 474 puts a child's fee before the court. 22 NYCRR 1215.1 engagement
letter. CPLR 8018(a) $210 index number ($190 plus $5 plus $15). NYC Health dog license
$8.50 / $34 with the $2 per year late fine.

## Could not verify

- **Nevada dog license fee.** Clark County Code Title 10 as retrieved publishes permit
  and reinspection amounts but no plain per-dog license fee, so only the permit figures
  are cited.
- **Court HTML fee pages.** lacourt.ca.gov and saccourt.ca.gov HTML fee landing pages
  returned no readable figures to a script; each court's own posted PDF schedule was
  fetched and cited instead.
- **Judiciary Law 474-a subdivisions (3)-(5).** The 30/25/20/15/10 percentages were read
  verbatim on nysenate.gov, which is what the page cites. The net-computation and
  extraordinary-circumstances subdivisions were read on Justia; no figure on the page
  rests on that reading.
- **22 NYCRR 1215.2** dollar threshold for when an engagement letter is excused was not
  fetched, so no threshold figure appears on the page.
- **Sacramento County Code chapter 9.44** dangerous-animal provisions carry no dollar
  amount in the text retrieved, so no penalty figure is used.
- **Georgia sanction range.** Rule 1.5's maximum penalty is a public reprimand per the
  State Bar handbook; no monetary sanction figure exists to cite.

## Files

- `pricing-research-atlanta-dogbite.md`
- `pricing-research-lasvegas-dogbite.md`
- `pricing-research-losangeles-dogbite.md`
- `pricing-research-newyork-dogbite.md`
- `pricing-research-sacramento-dogbite.md`
- `add_pricing_batch10.py` (site.json pricing blocks, idempotent)
- `add_pricing_copy_batch10.py` (copy.md pricing_lede / pricing_body, idempotent)
