# Pricing page brief

One new page per site at `/pricing/`. It is the single page on the site where
numbers are allowed. Read this whole file before writing anything.

## Why this page exists

Three of the highest-volume searches in every one of these markets are "how much
does X cost in [city]", "X cost", and "[practice area] fees". Nobody wins those
with a phone number. They get won by the page that actually answers, with the
source named. That page then becomes the thing an AI answer quotes, and the
quote carries the site with it.

It also does something the rest of the site cannot: it makes each of the 83
pages factually different from each other. A permit fee schedule is a different
number in every city. A metro wage is a different number in every metro. That
is real local uniqueness, not a city name swapped into a sentence.

## The one rule that keeps this safe

**The page says what a job costs in the market. It never says what the
advertiser charges.**

Everything follows from that. A market range with its source named is
information. A number attached to "we" is a quote, and there is no signed
operator on these sites yet to make one. The build blocks first-person pricing
language outright — `we charge`, `our price`, `our rate`, `call for a quote`,
`discount`, `as low as`, and the rest of `BANNED_PRICING` in `build.py`.

The sitewide footer disclosure normally says no price claim appears on the page.
On this page that sentence would be a lie, so the build swaps that one clause
automatically for the narrower true version: researched market ranges for the
city, sources named, not a quote and not an offer. You do not write that
sentence. If the swap fails to fire, the build fails.

## Two modes

| Site type | `mode` | What the table holds |
| --- | --- | --- |
| Home services | `cost` | Dollar ranges per job |
| Legal | `fees` | Amounts the law itself sets |

**Legal sites never publish dollar ranges for legal work.** A range for "what a
DUI lawyer costs" reads as a fee claim and fee advertising is what the bar rules
regulate hardest. The build rejects `mode: "cost"` on a legal site. Instead the
legal page explains how fees actually work in that state, using the state's own
rules and statutes as the source.

Legal splits again by `fee_kind`:

- `contingency` — injury work. Car accident, personal injury, dog bite,
  wrongful death, motorcycle, truck accident. The table holds the ceilings the
  state's bar rule puts on a fee taken out of a recovery.
- `criminal` — criminal defense, DUI, domestic violence, divorce, family law.
  **A fee taken out of the result is prohibited in these matters.** So there are
  no percentages. The table holds what the state sets: the court-appointed
  counsel application fee, the statutory maximum fines by offense level, the
  court costs, program and reinstatement fees.

Cite the correct subdivision. Do not copy a subdivision letter from this brief
or from another site without opening the rule yourself — numbering differs by
state and gets renumbered. Verified examples: California rule 1.5(c)(2) is the
criminal contingent-fee ban, (c)(1) is family law, and (d) is the true-retainer
/ "earned on receipt" provision — an earlier version of this brief wrongly said
(d). Colorado's domestic-relations ban is Colo. RPC 1.5(c)(4)(ii), with the
post-judgment-collection carve-out in Comment [6]; Colorado's (d) governs fee
division between lawyers in different firms and has nothing to do with
contingency — an earlier version of this brief wrongly said (d) here too.
Florida is Rule 4-1.5(f)(3)(A) for domestic relations and (f)(3)(B) for
criminal. Texas uses Rule 1.04, not 1.5. Arizona is ER 1.5(d)(2).

Note the pattern in those two corrections: both times the wrong answer was
"(d)". A subdivision that sounds right because it was right in another state is
the single most common error in this work. Open the rule.

Wrongful termination and other employment matters take **`contingency`**, not
`criminal`. A contingent fee is permitted and ordinary in employment work. Most
states set no percentage ceiling on it, so say that plainly and publish what the
law does require instead — the written-contract rule, the negotiability
disclosure, filing fees, and any statutory fee-shifting provision.

## Where a cost range comes from (home services)

**A dollar range with nothing published behind it does not go on a page.** The
first twenty home-service pages were built by reasoning a range from the metro
wage and a guess at parts. The numbers landed close to reality, which is exactly
why it was dangerous: they sat next to genuinely cited permit fees and looked
sourced. The build now rejects any cost row without sources.

Each row needs **2-4 sources**, each a **separate business**, each publishing a
real figure for that job:

- Companies that actually work in that metro and post prices on their own site.
  Plenty do: "torsion spring replacement $150-250", "service call $89",
  "tune-up from $75". These are the primary source for a market range.
- A manufacturer, distributor or utility page that publishes a part price,
  program cost or rebate.
- A government schedule for anything the government sets (permits, inspections,
  tap fees, disposal). These belong in `anchors` as well.

Rules:

- The published figures set the range. Take the low from the lowest credible
  posted figure and the high from the highest, so the row spans what the market
  actually shows rather than one company's number. Do not average them into a
  single point and do not narrow the range to look tidy.
- **Total an itemized price before you use it.** Some companies post a build-up
  rather than an all-in number: "$67.50 service call + $185 door service + $125
  per spring". For a two-spring row that is about $502, not $125. Add the parts,
  the labor and any dispatch or service-call charge the company says applies,
  multiply per-unit parts by the number the row describes, and use that total.
  Taking one line out of an itemized list understates the high end, which is the
  exact error that got caught on the first re-sourced batch.
- **Match the figure to the job in the row.** A single-spring price does not
  belong on a row about replacing a pair, an opener repair price does not belong
  on a row about a full opener replacement, and a part-only price does not belong
  on a row that includes labor. If a source only posts the adjacent job, either
  find a source for the actual job or change the row to describe what is posted.
- **Two sources on one row may not share a hostname.** One operator's price list
  is that operator's price, not the market.
- **Banned:** Angi, HomeAdvisor, Thumbtack, Fixr, Homewyse, Porch, Yelp, Forbes
  Home, Bob Vila, CostPatch, BuildX, Modernize, This Old House, Houzz, HomeGuide
  and every other national "cost guide". They are lead-generation pages with
  modelled numbers, they disagree with each other by up to 3x, and the build
  rejects their domains outright. Also avoid obvious doorway domains (a `.store`
  or `.online` with no real business behind it).
- Record every figure, its URL and the retrieval date in the research note. A
  posted price can change without notice; the note is what makes a stale link
  recoverable.
- Search pattern that works: `<trade> <city> price list`, `<trade> <city> cost`,
  `<trade> pricing <metro>`. Read the company's own pricing or service page.

Row shape:

```json
{"job": "Broken torsion spring, pair replaced", "low": 200, "high": 450,
 "basis": "flat per pair, parts and labor",
 "note": "High-cycle springs and a second door both push it up.",
 "sources": [
   {"name": "Company A, Dallas, posted price list, read 2026-08-23",
    "url": "https://example-a.com/prices"},
   {"name": "Company B, Plano, service pricing page, read 2026-08-23",
    "url": "https://example-b.com/pricing"}]}
```

The page renders these as small numbered references beside the range, with one
deduped numbered list under the table. So a reader can check any figure, and a
row citing three companies costs one line of visual noise instead of three.

## What goes in `site.json`

```json
"pricing": {
  "mode": "cost",
  "table_head": "What the four common jobs run in <City>",
  "anchors": [
    {
      "label": "Mechanical permit, AC changeout",
      "value": "$XXX",
      "detail": "One sentence on what triggers it and who pulls it.",
      "source_name": "City of <City> fee schedule",
      "source_url": "https://..."
    }
  ],
  "rows": [
    {
      "job": "The job, named the way a homeowner says it",
      "low": 145,
      "high": 420,
      "basis": "per visit | per unit | per linear foot | flat",
      "note": "5-30 words on what pushes it to the top of the range."
    }
  ]
}
```

Fees mode swaps `rows` for `fee_rows` and adds `fee_kind`:

```json
"pricing": {
  "mode": "fees",
  "fee_kind": "criminal",
  "table_head": "What <State> law sets, and what it does not",
  "col_a": "What it covers",
  "col_b": "What the law sets",
  "anchors": [ ... same shape ... ],
  "fee_rows": [
    {
      "stage": "Court-appointed counsel application",
      "share": "$50",
      "note": "Plain-English explanation.",
      "source_name": "Fla. Stat. 27.52",
      "source_url": "https://..."
    }
  ]
}
```

### Anchors are the load-bearing part

2 to 4 of them, and every one needs a real `https://` source that a person can
open and see the number on. The build checks the URL scheme and checks that at
least one `source_name` appears in visible page text. It cannot check that you
read the page — that is on you.

**Good anchors** (primary, exact, different in every city):

- The city or county building department **fee schedule** — the actual mechanical,
  plumbing, electrical or building permit fee for the job. Exact dollar amount,
  unique per jurisdiction, published by the government. This is the best anchor
  available and every home-services site should have one.
- **BLS Occupational Employment and Wage Statistics by metro area** — the median
  hourly wage for the trade in that specific metro. `bls.gov/oes/current/oes_<MSA>.htm`
  or the occupation page. Different in every metro, and it explains why a market
  is expensive without guessing.
- State or utility programme documents with published amounts — a rebate figure,
  a state code requirement that adds a testing step and a cost.
- For legal: the **state bar rule** itself, the **statute**, the **county clerk's
  published cost schedule**. Cite the rule number in the `source_name`.

**Not acceptable as anchors:** Angi, HomeAdvisor, Thumbtack, Fixr, Homewyse,
Porch, Yelp, Forbes Home, Bob Vila, any "average cost" content site. They are
aggregated national guesses recycled from each other. They may inform the range
you land on, but they are never the named source and never the anchor.

### Rows

4 to 8 for cost mode. Name the jobs the way a homeowner says them, not the way
a trade catalogue does. Ranges must be whole dollars, low strictly under high,
and wide enough to be honest — a $10 spread is a fake precision. The `note`
column is where the page earns its keep: say what actually pushes a job to the
top of its range in that city. Old housing stock, a roof you cannot walk,
attic access, a permit inspection wait, a specific local code requirement.

3 to 6 for fees mode, and every single row needs its rule or statute URL. No
exceptions — an unsourced fee number on a legal site is the one thing on this
whole portfolio that could actually cause a problem.

## What goes in `copy.md`

Two new sections:

```
## pricing_lede
One or two sentences. Goes in the hero under the H1. Say plainly what the page
tells them.

## pricing_body
Markdown. This is the bulk of the page. Use ### subheads.
```

Body runs long enough that the whole page lands **900 to 1650 visible words**
including the table and the standing page furniture. Target roughly 700-900
words of authored body.

What the body should cover, in whatever order reads best:

- Why the range is a range. The two or three variables that actually decide it.
- The local reason this market prices the way it does. Housing age, climate load,
  permit process, distance, labour supply. Tie it to the anchor numbers.
- What a fair quote looks like and what it should itemise, so the reader can
  tell a real quote from a bad one.
- The trap. The upsell that gets pushed in this trade, or the fee structure
  that surprises people. Say it straight.
- What is not included in the number people find online.

For legal, the body covers how the fee arrangement is actually structured, what
comes out of a recovery before the client sees it, what costs are separate from
fees, what the written agreement has to say, and what the state's rule requires.

Write it the way somebody who has done the work would explain it to a neighbour.
No hedging, no "it depends" without saying what it depends on.

## Hard rules

1. Never a first-person price. Not `we charge`, not `our rates`, not implied.
2. No discount, coupon, beat-any-price or urgency language. Guarded in code.
3. No `Offer` or `PriceSpecification` schema on this page, ever. That markup
   means a seller is making an offer at a price. Nobody here is selling.
4. Every anchor and every legal fee row carries an `https://` source that
   states the number. If you cannot find the number on a primary source, drop
   the row rather than soften it.
5. Aggregator sites are never the named source.
6. The 15-word shingle guard applies. The pricing page cannot share 15
   consecutive words with any other site in the portfolio. Same-trade markets
   are where this bites — write the local reasoning genuinely local.
7. The pre-tenant ban still applies, minus `contingency fee`, which the fees
   page may use when describing what a state rule permits.

## Build and check

```
python template/build.py <domain>      # one site
python template/build.py --check-only  # all 83, no write
```

Guards that will stop you: `PRICING_WORDS (900, 1650)`, `PRICING_ROWS (4, 8)`,
`PRICING_FEE_ROWS (3, 6)`, `PRICING_ANCHORS (2, 4)`, `BANNED_PRICING`,
note length 5-30 words, `low < high`, https on every source, disclosure swap
must fire, at least one anchor source name visible on the page.

A site with no `pricing` block in `site.json` builds exactly as it did before.
The page is opt-in per site.

## Retrieval notes (added after the two proof sites)

**BLS blocks automated access.** `https://www.bls.gov/oes/current/oes_XXXXX.htm`
returns 403 to any script and to headless Chromium. Do not conclude the figure
is missing. Get the number from the BLS public data API instead:

    https://api.bls.gov/publicAPI/v2/timeseries/data/OEUM<area><industry><occ><datatype>

Sacramento HVAC example: series `OEUM004090000000049902108` = area 0040900,
occupation 49-9021, datatype 08 (median hourly wage). Datatype 04 is annual
mean, 13 is annual median. Record the exact series ID in the research note, and
cite the human-readable OEWS metro page as `source_url` — a reader can open it
even though a script cannot.

Same rule for Google, Cloudflare and Telnyx endpoints: an empty body is a block,
not a zero. Retry or find another route to the same figure.

**California EDD is not a substitute.** `labormarketinfo.edd.ca.gov` is
disallowed by robots and covers California only.

## Two things the build now enforces that it did not before

**American spelling.** `BRITISH_SPELLINGS` in `build.py` is a whole-word regex
checked against every rendered page of every site. It caught `licence` in the
footer disclosure on all 40 legal sites, plus `labour`, `defence`, `travelling`,
`neighbourhoods`, `authorises`, `itemises`, `realise`, `recognising`, `labelled`
and `tyre` across 15 sites. Write American English. `license`, `labor`,
`defense`, `traveling`, `neighborhood`, `authorizes`, `mold`, `tire`, `story`.

**The table stacks into cards on a phone.** Below 640px each row becomes its own
gold-topped card with the column names as small labels, so the "what moves it"
column is never scrolled out of sight. Nothing to do per site — but keep row
notes inside the 5-30 word limit, because on a phone that note is body copy
rather than a table cell.
