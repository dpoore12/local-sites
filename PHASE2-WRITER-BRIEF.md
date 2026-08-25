# Phase 2 Writer Brief — add four service pages to one site

You are writing copy for exactly ONE site. Your domain is in your objective.

Work only in `/home/user/workspace/local-sites/`. You may edit ONLY these two files:
- `sites/<your-domain>/copy.md`
- `sites/<your-domain>/site.json` (one field only: `"phase": 1` → `"phase": 2`)

Never touch `template/`, `data/`, another site's folder, or any deploy script.

---

## What phase 2 is

Phase 1 sites are home + about + contact + pricing. The four "symptom" cards on the
home page carry full depth because there is nowhere to hand off to.

Phase 2 adds a `/services/` index plus four long service pages. The symptom cards
shrink to short teasers that link to the service page covering them in full.
The depth moves off the home page and onto the service pages.

---

## Your job, exactly

### 1. Shrink the four symptom blocks

`symptom_1` … `symptom_4` are currently 200–360 words each. Rewrite each to
**40–80 words**. Keep the same problem, same title. It becomes a teaser: name the
symptom, give the one useful immediate instruction, stop. The detail is not lost —
it moves onto the service page.

Do not change `symptom_N_title` unless the shrink makes it wrong.

Keep the same order. `site.json` has a `symptom_service` array mapping symptom 1–4
to the service slug each one links to. Read it. Your teaser must be about the thing
that service page covers.

### 2. Add three new blocks

- `## services_summary` — **95–115 words.** One paragraph naming all four jobs and
  saying plainly why confusing them costs the reader money or a second visit.
  Must be about YOUR city and YOUR trade.
- `## services_pick_head` — **6–10 words.** Heading above the four service links.
  Example shape: "Start with the failure you are actually seeing"
- `## crosslink_head` — **4–7 words.** Heading above the links at the bottom of a
  service page. Example shape: "Different problem than this one?"

### 3. Write the four service pages

`site.json` has a `services` array with four entries, each with `slug`, `name`, `h1`,
`keyword`. For each one, add two blocks. Convert the slug to the key by replacing
hyphens with underscores — slug `garage-door-spring-repair` → key
`garage_door_spring_repair`.

- `## svc_<key>_lede` — **30–45 words.** Sets up the page. Concrete, not a summary.
- `## svc_<key>_body` — **700–900 words** of markdown. Use `###` subheads. Six or
  seven sections is the right shape.

The whole rendered service page must land **900–1550 visible words**, and the
shared page furniture (nav, trust band, lead form, disclosure, footer) already
uses roughly 600 of that. So keep the authored body in the 700–900 band. The build
will tell you the exact number.

Subhead shape that works — adapt it, do not copy it:
- How you know that is what happened (the symptom, precisely)
- Which variant this city actually has, and why (housing stock, climate, local rule)
- What not to do yourself, and the specific hazard
- The thing a careless operator gets wrong (the second-visit trap)
- Local conditions that shorten the part's life
- What the visit actually looks like, step by step
- What it costs — the shape of the range and what moves it, never a number you charge

For legal sites the equivalent shape is: how you know you have this kind of claim /
what the state's deadline and rules actually are, with the statute / what to do in
the first week / the mistake that costs the case / what the other side does / what
happens after you make contact / how fees work under that state's rule.

### 4. Flip the phase

Change `"phase": 1` to `"phase": 2` in `sites/<your-domain>/site.json`.
Change nothing else in that file.

---

## The bar

Read `sites/fortworthgaragedoorrepairpros.com/copy.md` before you start. It is a
finished, passing phase 2 site. Study **how specific it is**: it names the median
year a housing unit was built, names neighborhoods and the decade each was
developed, gives the spring gap in inches, gives the cycle rating and what that is
in years at four openings a day.

**HARD WARNING.** Fort Worth is a STRUCTURE reference only. If you reuse its
phrasing you will fail the duplicate guard and waste the run. Never lift a
sentence, a subhead, or a distinctive turn of phrase from it. Same for any other
site you read. Write from your own research.

Specificity is the whole job. A page that could describe any city in America is a
page that fails. Use:
- `local_facts` in your `site.json` (each has a real source URL) — build on them
- `neighborhoods` in your `site.json` — name them and say something true about each
- Your own research: housing stock and typical build era, climate and what it does
  to the part, the actual city or state rule that applies, permit requirements

Search the web for real specifics. Do not invent a statute, a permit fee, a code
section, a climate figure, or a date. If you cannot verify it, write around it.

---

## Absolute prohibitions

No tenant is signed to any of these sites. Nothing may imply one is.

**Never write** — any of these fails the build:
years of experience · years in business · family owned · veteran owned ·
licensed and insured · fully licensed · 5-star / five-star · voted best ·
A+ rating · BBB accredited · award winning · trusted by · thousands of ·
satisfaction guaranteed · our customers say · read our reviews · since 19.. ·
since 20.. · no fee unless · no win no fee · free consultation · free case review ·
contingency fee · we recover · we have recovered · millions recovered ·
no upfront cost · you pay nothing

**Never name** a business, a person, a license number, a review count, or a year in
business.

**Never state a price you charge.** You may describe what a job costs in the market
in general shape ("a parts-and-labor repair with a fairly tight range"). You may
never write "we charge", "our price", "our rate", "call for a quote", "as low as",
"discount", "% off", or a first-person dollar figure. The pricing page is the only
page with numbers and you are not writing it.

**Sell the work, not a phone call.** What gets fixed, what happens, when someone
arrives. Never "call for a free consultation". The phone number is chrome; your
copy does not pitch the call.

**US spelling.** No British spellings.

**No em dashes are fine, but do not use the words** "map pack" or "SERP" anywhere.

---

## How you verify — do this, do not skip it

From `/home/user/workspace/local-sites/`:

```
python3 template/build.py --check-only <your-domain>
```

This runs every guard, including the duplicate check against all 82 other sites.
It prints `[PASS]` or a list of numbered failures with exact word counts.

**Iterate until you get `[PASS]`.** Common failures and the fix:
- `service <slug>: NNNN visible words, must be 900-1550` — lengthen or trim the body
- `symptom_N: NN words, must be 40-80` — you did not shrink it enough
- `copy.md shares N 15-word runs with <other-site>` — rewrite those runs. The
  message names the other site; the overlap is almost always a generic sentence
  about the trade. Make it specific to your city and it clears.
- `home NNNN words` outside 1300–2300 — if too low, your symptom teasers are too
  short; if too high, they are too long

Do not report done until the check prints `[PASS]` for your domain.

---

## Report back

- The `[PASS]` line and the per-page word counts the build printed
- The four service page slugs you wrote
- Every external fact you used, with the URL you verified it against
- Anything you could not verify and wrote around
