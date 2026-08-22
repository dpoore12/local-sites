# Handoff — UG

Everything you need to work on this repo without asking me anything first.
Read `README.md` for how the builder works. This file is the current state and
what is actually open.

---

## What this repo is

83 local service websites, one per city-and-trade market, each built from the
same locked template and each rented to one local contractor or law firm for a
flat monthly fee. The 83 markets were screened, scored and price-modelled before
any code was written. Modelled at full occupancy: **$71,400/month.**

The site is not the product; the ranked site is. Half the work is off-site and
lives in `PLAYBOOK-LINKS.md`.

---

## Repo layout

    template/            The locked design system. See LOCKED.md before touching it.
      build.py           Renderer + every guard. Run it from the repo root.
      base.html          Head, call bar, footer nav, mobile call bar
      index.html         The home page, 13 sections in a fixed order
      service.html       One service page, x4 per site
      inner.html         services hub / about / contact
      assets/theme.css   The whole design system
    niches/              28 niche structure packs. Defines the 4 service pages
                         per trade, the hero line, the 4 failure modes. No prose.
    sites/<domain>/
      site.json          City metadata, sourced local facts, market data
      copy.md            Every word on the site. Hand-written per city.
      assets/            hero.jpg + work-1..3.jpg for that city
    dist/<domain>/       Build output. Generated, do not edit.
    scaffold.py          Creates a new site directory from a screened market row
    data/markets.json    The 83 screened markets. Input to every script.
    data/registrar-snapshot.json  What Cloudflare says we own. Generated.
    cf_sync.py           Pulls the Cloudflare Registrar account into a snapshot
    domains.py           Rewrites the domain ledger from that snapshot
    DOMAINS.csv          The ledger. Edit phone / tenant / hosting here only.
    DOMAINS.md           Generated read-only view of the ledger. Never hand-edit.
    PLAYBOOK-LINKS.md    The off-site half: listings, links, the 8-week schedule

---

## Commands

    python3 template/build.py            build every site, run every guard
    python3 template/build.py --check    guards only, render nothing
    python3 scaffold.py                  create any missing site directories
    python3 scaffold.py --status         honest completion report for all 83
    python3 cf_sync.py                  refresh the registrar snapshot (needs token)
    python3 domains.py                  rewrite DOMAINS.csv + DOMAINS.md
    python3 domains.py --check          exit 1 if the ledger is stale (for CI)

`--status` is the one to trust. It counts filled copy blocks, sourced facts,
neighbourhoods and photos per site, and only calls a site buildable when all
four are actually present.

---

## The rules the build enforces

These are not style preferences. The build fails on all of them.

1. **No shared phrasing.** If any two sites share 15 consecutive words, the build
   fails. This is the single most important guard in the repo. 83 near-identical
   city sites is the exact pattern Google's doorway and scaled-content policies
   describe, and it would take the whole portfolio down at once rather than one
   site. Every block in every `copy.md` is written for its city.
2. **No absolute asset paths.** Everything is depth-relative via the `base`
   variable. This bit us once already: the pages loaded and the stylesheet
   404'd, so the deployed preview was raw unstyled HTML while local testing
   looked fine. `check_no_absolute_paths` now hard-fails on it.
3. **No unsourced local facts.** Every site needs 3 city-specific facts, each
   with a real source URL in `site.json`. Guessed facts are the fastest way to
   lose a tenant.
4. **No tenant claims before a tenant exists.** No business name, licence
   number, review count, years in business, or price appears anywhere until
   `tenant.status` is `active`. `LocalBusiness` schema is blocked until then too.
5. **Word ranges.** Home page 1,300–2,300 visible words. Each service page
   900–1,500. Symptom teasers on the home page 40–80 words.
6. **Phone numbers.** Every site ships with a reserved `555-01XX` number and
   WARNs on every build until a real Telnyx number in the correct local area
   code replaces it. Nothing dials a stranger while a site is a draft.

---

## Current state, honestly

- **Template: done and locked.** Tagged `template-v2`. Eight pages: home, four
  service pages, services hub, about, contact.
- **Naperville garage door: complete.** The reference site. Copy this one's depth.
- **32 sites written and passing.** 2,090 of 4,793 copy blocks done. Every one
  builds clean and no two share 15 consecutive words. Phase 1 only: home, about,
  contact. Service pages come in a second pass.
- **51 sites: scaffolded, no copy.** Directory, `site.json` with verified city
  metadata, and a `copy.md` worksheet listing every required block.
- **Off-site work: zero done.** Not one listing, not one link. This is 40% of
  ranking by Kyle's own weighting and it has not started.
- **Domains: all 83 registered.** Bought 2026-08-22 at Cloudflare, $10.46 each,
  all active, all auto-renew on, all expiring 2027-08-22. See `DOMAINS.md`.
- **Phone numbers: all 83 still placeholders.** Every site WARNs on build and
  none may be published until real numbers land. This is now the live blocker
  ahead of hosting.

Run `python3 scaffold.py --status` for the live numbers rather than trusting
this paragraph, and `python3 domains.py` before trusting the ledger.

---

## What each site actually needs to go live

| Step | What | Who |
|---|---|---|
| 1 | ~8,500 words of city-specific copy across 62 blocks | writing pass |
| 2 | 3 sourced local facts + 6 neighbourhoods in `site.json` | writing pass |
| 3 | 4 photos in `assets/` | image generation |
| 4 | Domain registered — **done for all 83** | Dan |
| 5 | Real Telnyx number in the local area code | Dan |
| 6 | Build passes with zero errors | build |
| 7 | Deploy, then the 8-week schedule in `PLAYBOOK-LINKS.md` | UG |

Steps 1–3 are the bottleneck. 81 sites × 62 blocks is about 5,000 blocks of
original writing, and it cannot be shortcut by templating without tripping guard
1 and taking the portfolio with it.

---

## Domains and hosting

All 83 names are registered at **Cloudflare Registrar** on Dan's account
(`Danpoore99@gmail.com`, account `a3bf1a13d93899d8408b9d1ea94df078`). Bought
2026-08-22 via the Registrar API, $10.46 each, ~$868 for the set. Every one is
active with auto-renew on and expires 2027-08-22.

`DOMAINS.csv` is the ledger and the only file to hand-edit — and only the
`phone`, `tenant` and `hosting` columns. Everything else is regenerated:

    python3 cf_sync.py     # registrar -> data/registrar-snapshot.json
    python3 domains.py     # snapshot  -> DOMAINS.csv + DOMAINS.md

Run both after any registrar change and commit the result. `domains.py --check`
fails if the ledger drifted, so it belongs in CI.

### Things that will bite you

- **One Cloudflare account caps at 100 registrar domains.** We are at 83. The
  next 17 fit; batch two of the portfolio needs a second account.
- **The Registrar API pages by cursor, not by page number.** A `page=2`
  parameter is silently ignored and returns page one again. `cf_sync.py` already
  handles this; do not "simplify" it back.
- **`per_page` is capped at 50.** Anything larger is rejected outright.
- **`httpx` does not pick up the sandbox HTTPS proxy** for this host, so the
  token never gets injected and every call fails to connect. `curl` works.
- **A registration can return `success: true` with `state: "failed"`.** One of
  the 83 did exactly that and looked bought when it was not. Trust the account
  listing, not the create response.
- **Registrations are non-refundable.** Never register from a script without
  checking the name first and getting Dan's sign-off on the total.

### Hosting, not yet started

Nothing is deployed. Cloudflare Pages free tier allows 100 projects per account
and 500 builds/month, which covers 83 sites, and the domains are already on the
same account so DNS is one step. When a site goes live, record where in the
`hosting` column and re-run `domains.py`.

No site may be published while its `phone` column reads `PLACEHOLDER`. That is
all 83 right now.

---

## Where to start, UG

Highest value first, and none of this is blocked on Dan:

1. **Read `PLAYBOOK-LINKS.md` and start Tier 1 on Naperville.** Search Console,
   Bing, and the free listings. It is the only site with finished content, so it
   is the only one that can start earning position. Note the section on why
   Google Business Profile is deliberately excluded — that is a decision, not an
   oversight.
2. **Sanity-check the 28 niche packs in `niches/`.** Each defines the four
   service pages for a trade. If the four sub-jobs for a trade are wrong, every
   site in that trade inherits the mistake. Cheapest possible time to catch it.
3. **Build the Tier 3 prospect list for Naperville** — 10 to 15 local sites that
   might link. The method is in the playbook.
4. Do not start on template changes. It is locked for a reason and the reason is
   documented in `template/LOCKED.md`.

Questions to Dan, not to me.

## Phone numbers

73 Telnyx local numbers were bought 2026-08-22, one per market, each in that
market's own area code. $57.67 one-time, $57.67/month. All verified active
against the account rather than trusted from the order response.

**None of them is routed.** A bought number rings nowhere. Setting destinations
is separate work and it is not started.

Ten more markets use numbers Dan already owned; he confirmed they are not live
in MarketCall, Ringba or anywhere else. **All 83 markets now have a real,
unique number.** See PHONES.md.

Hard rule, unchanged: **no site publishes while its phone_status reads
PLACEHOLDER.** The build prints a warning for each one. `python3 phones.py`
re-reads the carrier and reports any drift between the sites and the account.

Two API traps worth knowing before you touch Telnyx:

- Square brackets in the URL **must be percent-encoded** (`page%5Bsize%5D=50`).
  A raw `[` returns an empty body, not an error.
- The rate limit is 5 requests/second and exceeding it returns **silent empty
  pages, not 429s**. An empty result means retry, never zero. This produced a
  completely false "23 area codes are out of stock" reading before it was caught.
