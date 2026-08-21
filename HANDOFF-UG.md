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
    PLAYBOOK-LINKS.md    The off-site half: listings, links, the 8-week schedule

---

## Commands

    python3 template/build.py            build every site, run every guard
    python3 template/build.py --check    guards only, render nothing
    python3 scaffold.py                  create any missing site directories
    python3 scaffold.py --status         honest completion report for all 83

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
- **Fort Worth garage door: in progress.** Site two, and the first real test of
  the duplicate-phrasing guard since it is the same trade as Naperville.
- **81 sites: scaffolded, no copy.** Directory, `site.json` with verified city
  metadata, and a `copy.md` worksheet listing every required block.
- **Off-site work: zero done.** Not one listing, not one link. This is 40% of
  ranking by Kyle's own weighting and it has not started.
- **Domains: none bought yet.**

Run `python3 scaffold.py --status` for the live numbers rather than trusting
this paragraph.

---

## What each site actually needs to go live

| Step | What | Who |
|---|---|---|
| 1 | ~8,500 words of city-specific copy across 62 blocks | writing pass |
| 2 | 3 sourced local facts + 6 neighbourhoods in `site.json` | writing pass |
| 3 | 4 photos in `assets/` | image generation |
| 4 | Domain registered (Cloudflare, ~$10.44 flat — not GoDaddy, they renew at $22.99) | Dan |
| 5 | Real Telnyx number in the local area code | Dan |
| 6 | Build passes with zero errors | build |
| 7 | Deploy, then the 8-week schedule in `PLAYBOOK-LINKS.md` | UG |

Steps 1–3 are the bottleneck. 81 sites × 62 blocks is about 5,000 blocks of
original writing, and it cannot be shortcut by templating without tripping guard
1 and taking the portfolio with it.

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
