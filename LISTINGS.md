# Links and listings — the work pack

The sites are live and open to Google. This is the other half: getting other
websites to point at them. Target is 10 to 30 links per site, weighted local.

## What is in `data/`

| File | What it is |
|---|---|
| `nap.csv` | One row per site — the exact business name, phone, city and description to type into every listing. Copy from here every time so all 83 read identically wherever they appear. |
| `listings.csv` | The work queue. 1,079 rows: every site crossed with every listing it belongs on, with a status column. |
| `link-prospects.csv` | Local link targets found per city — community pages, chambers, local news, bar associations. |

## The queue, by the numbers

- 83 sites — 43 home services, 40 legal
- 839 rows ready to work now, about 10 per site
- 240 rows held: legal directory profiles describe a named attorney, so they
  cannot be filled in honestly until a firm signs that site

## Order of work, per site

1. Search Console and Bing — how we see whether Google picked the site up
2. The free listings: Yelp, Yellow Pages, BBB, Nextdoor, Apple Business Connect
3. Home-service sites only: Houzz, Angi, Thumbtack, Porch, BuildZoom, Networx
4. Local targets from `link-prospects.csv` — community pages, chambers, local news
5. Stop at eight weeks

## Two things that will bite

**No street address.** Most listings want one. We are running these as
service-area listings with a city and a phone and no street address, which most
of the list accepts. The ones that insist on a verified street address get
skipped rather than faked.

**No Google Business Profile.** Deliberate. It needs a real address per city and
83 mail drops in 83 cities is the exact pattern Google suspends accounts over.
We take organic positions four to seven with the call bar pinned to the top
instead. When a site gets a paying tenant, calls forward into the tenant's own
existing verified profile — cleaner, legitimate, free.

## Never

- Buying links, link packages, guest-post marketplaces
- Linking the 83 sites to each other — that turns a portfolio into one
  detectable network overnight
- Asking for reviews on any listing where we are not the one doing the work

Full reasoning and sources: `PLAYBOOK-LINKS.md`.
