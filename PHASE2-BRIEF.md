# Phase 2 Brief — Adding Service Pages To A Live Site

You are upgrading ONE existing site from phase 1 (home + about + contact) to
phase 2 (home + about + contact + services hub + 4 service pages).

Everything except the copy already exists. `site.json` already has the four
service definitions, the local facts, the neighbourhoods, the live phone number
and the images. **Do not add, rename or reorder the services.** Your job is
writing prose into `sites/<domain>/copy.md` and nothing else.

Working directory: `/home/user/workspace/local-sites`

---

## Read these first, in this order

1. `sites/<your-domain>/site.json` — the four service slugs, the local facts
   (each with a source URL), the neighbourhoods, the city and state.
2. `sites/<your-domain>/copy.md` — the existing phase-1 copy. You are editing
   this file in place.
3. `sites/fortworthgaragedoorrepairpros.com/copy.md` — **the reference build.**
   This is the standard. Read the whole thing. Match its depth, its specificity
   and its tone. Do not match its words.
4. `sites/fortworthgaragedoorrepairpros.com/site.json` if you want to see how a
   finished phase-2 site.json relates to its copy.

---

## What to change in copy.md

### 1. Update the RULES block at the top

Replace the phase-1 rules block with the phase-2 version, copied from the Fort
Worth reference (home page 1,300-2,300 words; each service page 900-1,500;
symptom blocks 40-80 word teasers).

### 2. Shrink the four `symptom_N` blocks to 40-80 words each

They are currently 200-360 words because in phase 1 the card was the only
coverage of that problem. Now each card is a teaser that hands off to the
service page covering it in full. Keep the specific local detail that makes the
teaser worth reading; move the depth into the service page. **40-80 words is a
hard build guard — count them.**

### 3. Add `## services_summary`

A few paragraphs introducing the four jobs and, most importantly, why they get
confused with each other. This renders on the services hub page. Put it directly
after `## closing_cta`, before `## about_summary`, matching the reference.

### 4. Add two blocks per service: `svc_<slug>_lede` and `svc_<slug>_body`

Take the slug verbatim from `site.json`, replacing every hyphen with an
underscore. Example: slug `garage-door-spring-repair` becomes
`## svc_garage_door_spring_repair_lede` and
`## svc_garage_door_spring_repair_body`.

- **lede** — two or three sentences. The hook. What this repair actually is and
  why it matters here specifically.
- **body** — the page. Use `###` subheads. Each rendered service page must land
  **900-1,500 visible words**, and the body is almost all of that, so aim for
  roughly 1,000-1,300 words of body. Six to eight `###` sections is the shape
  that works.

Put all eight service blocks at the end of the file, after the `factor_4` block,
in the same order the services appear in `site.json`.

---

## What the writing has to do

**Be about this city, concretely.** The reference page names Wedgwood, Arlington
Heights and Walsh, cites the census median build year, and explains what North
Texas heat does to a lubricated bearing. Yours must do the equivalent for your
city, using the `local_facts` already researched in your `site.json` plus your
own additional research. Housing stock and build era, climate and what it does
to the equipment, local permit rules, local road or geography facts, the actual
neighbourhoods.

**Research anything you assert.** If you state a permit rule, a statute, a
climate figure, a build year or a code requirement, verify it against a real
source first and keep the URL. For legal sites this matters most: filing
deadlines, comparative fault rules, insurance minimums and dog-bite liability
standards vary by state and change. Never state one from memory. If you cannot
verify a fact, leave it out — the page is better shorter than wrong.

**Teach, do not sell.** Explain how a person can tell what went wrong, what
varies about the job in this city and why, what the visit actually looks like
step by step, what is dangerous to attempt, and how pricing is structured.
Someone should be able to diagnose their own problem from the page.

**On price:** explain what drives the range and say a firm figure comes before
work starts. Never state a dollar amount.

---

## Hard rules the build enforces — it fails if you break any

- **No 15 consecutive words may match any other site in the portfolio.** 83
  sites cover overlapping trades. Never reuse a sentence, and never lift phrasing
  from the Fort Worth reference.
- **Never name a business, a licence number, a review count, a price, or a
  number of years in business.** No operator has signed. None of it is true yet.
- **Never promise a phone consultation, a free quote or a free estimate.** Sell
  the repair: what gets fixed, what it costs, when someone arrives.
- Banned outright: "years of experience", "years in business", "family owned",
  "veteran owned", "licensed and insured", "fully licensed", "5-star",
  "five star", "voted best".
- **Legal sites only:** never "client", "case", "referral", "we recommend",
  "top-rated", "we matched you", or anything implying a caller was screened,
  evaluated or matched to a firm. Write "inquiry" and "the person calling". Never
  characterise anyone's situation as a claim with merit. Do not create an
  attorney profile or name a responsible attorney — no firm has signed.

---

## Verify before you finish

```bash
cd /home/user/workspace/local-sites
python template/build.py <your-domain>
```

Fix every error and re-run until it builds clean. The guards check word counts
per block, the 15-word duplicate shingle across all 83 sites, the banned
phrases, and that all four service pages exist. A clean build is the definition
of done.

Then set `"phase": 2` in `sites/<your-domain>/site.json` and build once more.
(If you set phase 2 before the copy is written the build will fail — that is
expected, so write first.)

Do not deploy, do not touch git, do not edit any other site's files, and do not
edit anything in `template/`.

---

## Report back

- The domain, and whether `python template/build.py <domain>` exits clean.
- Word count of each of the four service pages.
- Every fact you researched, with the source URL, so it can be spot-checked.
- Anything you deliberately left out because you could not verify it.
