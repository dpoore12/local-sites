# Audit — 30 August 2026

Independent re-verification of `SEO Landlord — The Complete Bible` against the
repository. Method: every number below was recomputed from a named file in this
repo, or produced by running the build. Nothing is quoted from the Bible without
being re-derived. Where I could not verify a claim, I say so rather than
resolving it.

Four findings. The first one changes strategy.

---

## 1. The "40 soft markets" finding does not survive. There is no soft bucket.

**Bible, Section 9:** *"40 of our 83 markets have page-one operators with 0–2
referring domains on the ranking page, while 12 markets have operators with
151–582."* It concludes *"roughly half our markets have genuinely soft page-one
incumbents."* That conclusion is load-bearing — it is the basis for triaging the
portfolio and for the belief that links are optional in half of it.

**What the data actually holds** (`data/competitor-links.json`, 282 rows):

| | |
|---|---|
| Rows carrying a `refdomains` value | **111** |
| Rows where the key is absent entirely | **171** |
| Competitors with `refdomains` ≤ 2 | **0** |
| Competitors with `refdomains` = 0 | **0** |
| Median `refdomains` among the 111 measured | **488** |

**Not one competitor in the entire measured set has 2 or fewer referring
domains.** The minimum is well above it. A market cannot have a page-one
operator at 0–2 refdomains, because no such operator exists in the data.

Joining page-one local competitors per market (`data/serp-aug29.json`, top 10,
directories and aggregators excluded):

- 40 of 83 markets have link data on at least one page-one local competitor.
- Of those 40, **all 40** have a median page-one competitor at ≥ 150 refdomains.
  Median across markets: **630**.
- The remaining **43 markets have no link measurement at all** on any page-one
  local.

The reproduction: if the 171 absent values are read as `0`, **78 of 83 markets**
score "≤ 2 median." That is the failure mode. The published 40/12 split is a
missing-data artifact of the same family as correction 12.3, which the Bible
already caught once in `competitor-depth.json`. It was not caught here.

**Is missing data evidence of a weak site?** No — and this is the part that
matters, because "Ahrefs has no data on them so they must be tiny" is the
tempting reading. Comparing the 111 measured against the 171 unmeasured, from
`data/competitor-depth.json`:

| | measured (111) | unmeasured (171) |
|---|---|---|
| Median sitemap pages | 157 | **260** |
| Median ranking-page words | 1,434 | 1,372 |
| Median organic position | 3 | 3 |
| Median domain rating (where known) | 13.0 | **21.5** (n=14) |

The unmeasured competitors have **larger** sites, the same ranking positions,
and where a rating exists at all it is **higher**. They are not the weak ones.

**There is also no page-level link data anywhere in this repository.** The Bible
describes "referring domains pointing at the specific pages currently ranking."
`competitor-links.json` and `competitor-full.json` are both keyed on
`comp_domain` and carry only domain-level `dr` / `refdomains` / `backlinks`. The
per-page measurement the claim rests on has no source file, and the strings
"0–2" and "151–582" appear in no markdown in this repo — that analysis was done
in-session and never written down, which is how it went unchecked.

**Update, later the same day.** Live Ahrefs SERP data (`serp-overview`, which
returns `url_rating` and page-level `refdomains` per result) shows the Bible's
underlying instinct was right even though the repo file could not support it.
Ranking pages routinely carry 0–4 referring domains of their own — Precision
Door's `/reviews/city/eden-prairie` at position 3 with 0, A1 Garage's
`/eden-prairie-mn/` at 10 with 0, `dfwaffordablegaragedoor.com` at 8 with 2.
Page-level URL Rating across page one runs 4–7 almost everywhere.

The reconciliation the Bible proposed is the correct one: domain-level authority
and page-level links are different measurements and both are true. A competitor
ranking with its *homepage* brings 200–700 referring domains; one ranking with a
deep city page brings almost none and holds position on domain age alone.

So: this section stands as a correction to the *sourcing* (the claim could not be
reproduced from any committed file, and the 40/12 split is not what the data
says), not as a refutation of the strategic read. Links are still the portfolio's
largest measured gap.

---

## 2. The pre-tenant gate ran on 2 page types out of 9. Now it runs on all of them.

`BANNED_PRE_TENANT` was checked against the home page and the pricing page only.
Every site renders 9 pages. Service, services-hub, about and contact pages —
**six of the nine** — were never scanned. Any banned claim on a service page
passed the build.

Fixed in `template/build.py`: the claim gate now runs on every rendered page,
with the pricing page keeping its own `PRICING_EXEMPT` handling.

## 3. The matcher was substring-based and produced false positives on real copy.

`if phrase in low` with no word boundaries. Live examples from current copy:

| Copy | Fired on | Actually |
|---|---|---|
| "a tub reacting to **toilet use**" | `let us` | plumbing content |
| "in the National Register **since 19**72" | `since 19` | a historic district |
| "hundreds of **thousands of** dollars" | `thousands of` | marital property value |
| "§6146 caps a **contingency fee**" | `contingency fee` | explaining the statute |

Raw scan of the 83 `copy.md` files produced **18 hits, zero of them real**. Left
as-is, extending coverage to all pages would have failed the build on 17 sites
for statute explanations that are the best content we have.

Fixed three ways: phrases now match on word boundaries; `since 19` / `since 20`
and `thousands of` moved to `BANNED_CONTEXTUAL`, which only fires when the
sentence is actually claiming (a first-person or establishment marker beside a
date, a people-noun after a volume); `contingency fee` behaviour unchanged on the
pricing page.

## 4. The first-person voice rule is now gated (12.13), and the violation it names does not exist.

Added `BANNED_VOICE` — the law-firm voice (`we defend`, `our attorneys`,
`we represent`, …) and the trade voice (`we fix`, `we repair`, `our technicians`,
…). Correction 12.13 flagged this as writer convention only, so a new writer
could violate it and the build would pass. It is now a gate.

The Bible names one live violation: *"list of repairs we handle"* on
`overlandparkgaragedoorrepairpros.com`. **It is not there.** `grep` across that
site's source returns nothing for `we handle`, `we fix`, or `repairs we`.

**The build passes 83 of 83 with all of the above active.** Zero pre-tenant
claims, zero voice violations, portfolio-wide, on every page. Writer discipline
held completely — the gap was that nothing was checking it.

---

## Open — could not verify from here

**The repository builds 747 pages, not 1,291.** All 83 `site.json` files carry
`phase: 2` with exactly 4 services, which renders 9 pages each: 83 × 9 = **747**.
The Bible reports *"1,291 total pages live. 49 sites at 9 pages, 34 sites
expanded to 25 pages."* Nothing in this repo produces a 25-page site.
`expansion-queue.json` and the `EXPANSION-SPEC-*.md` files that the Bible lists
as key files are **not committed** — consistent with its own note that several
working files live at the sandbox workspace root rather than under `local-sites/`.

I could not reach the live sites to settle it; they are outside this
environment's network allowlist.

**This needs checking before the next deploy, by someone who can load a live
sitemap.** If the deployed network really carries 1,291 pages, then running the
documented pipeline (`build.py --live` → `host_all.py` → `redeploy.sh`) from this
repository would republish 747 and silently remove 544 pages. If the live sites
carry 9 pages each, the Bible's page count is wrong and the expansion never
shipped. Either answer matters; the dangerous case is assuming the first is
false.

Related: `template/LOCKED.md` still says *"Only Naperville and Fort Worth are
phase 2 today."* All 83 are phase 2. That file is stale.

---

## Changed in this branch

- `template/build.py` — `phrase_hits()` word-boundary matcher; `BANNED_CONTEXTUAL`;
  `BANNED_VOICE`; claim gate extended to all rendered pages.
- `call-desk/check_atlanta.py` — settles whether a post-launch call left a
  voicemail or hung up on the greeting.
- `AUDIT-AUG30-CLAUDE.md` — this file.

No copy, no `site.json`, no template file, no deployed site was touched.
`python3 template/build.py --check-only` → 83 PASS, 0 FAIL.

---

## Addendum — the Atlanta call signal does not hold up (30 Aug, later)

A Telnyx pull found 23 connected calls since launch, five of which survived a
junk filter, and read three of them — all local Georgia numbers into
`atlantaemergencyplumberpros.com` — as the first market reaching page one.

**It is not.** Checked against Ahrefs live SERP data for `emergency plumbing
atlanta`, positions 1 through 11: Reliable Air, All Good, Yelp, Mr Plumber,
Emergency Plumbers LLC, Roto-Rooter, High Priority Plumbing, Thumbtack.
`atlantaemergencyplumberpros.com` does not appear. That is consistent with
Search Console reporting zero clicks across all 83 properties. Organic search
cannot be the source of those calls.

The likelier source is in the same report: **that number is recycled and took 79
calls before launch**, including 30-attempt auto-dialer bursts on 14, 20 and 21
August. Local Georgia numbers dialling a recycled Atlanta line is that pattern
continuing, not a new one.

The duration is the tell. All three calls ran 16–17 seconds against a greeting
that consumes 8–10 of them. Each caller heard the greeting and rang off without
leaving a message. A burst pipe leaves a message; a wrong number hangs up.

The other two "possible" calls are not local either — 332 is Manhattan calling
Ann Arbor, 818 is the San Fernando Valley calling Danville, a 925 town.

**Confirmed by the recordings themselves.** All seven recordings in the Telnyx
account were pulled and resolved to markets and callers:

| When | Market | Caller | Message |
|---|---|---|---|
| Aug 29 | Ann Arbor Garage Door | +1 332-330-0159 | 9.0s |
| Aug 27 | Atlanta Emergency Plumbing | +1 470-256-4708 | **1.3s** |
| Aug 26 | New Orleans Motorcycle Lawyer | +1 833-935-2504 | 17.8s |
| Aug 24 | Atlanta Emergency Plumbing | +1 943-200-5014 | **1.5s** |
| Aug 23 | Houston Motorcycle Lawyer | one of our own numbers | 71.2s |
| Aug 23 | Houston Motorcycle Lawyer | one of our own numbers | 71.1s |
| Aug 23 | Sacramento AC Repair | one of our own numbers | 6.2s |

Three are our own launch-night test calls. The longest real message is a
toll-free 833 robocall into New Orleans. The two Atlanta voicemails are 1.3 and
1.5 seconds — the beep and a hang-up, not a message.

**Read: zero confirmed leads, which is the correct result for day nine of a site
with no links and no rankings.** Absence of signal is not a negative signal.

Two actions follow:

1. `call-desk/check_atlanta.py` re-runs this check on demand. Needs
   `TELNYX_API_KEY` and network, so it runs on a real machine, not in the
   sandbox. A daily automated watch now covers it as well.
2. **Swap the Atlanta tracking number.** While that line carries a previous
   owner's traffic, no call on that market is attributable, and a call log shown
   to a prospective tenant will contain other people's wrong numbers.
