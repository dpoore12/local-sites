# Search Console — All 83 Sites In

Date: 23 August 2026

## Where things stand

| Item | Count |
|---|---|
| Sites confirmed as ours in Search Console | 83 of 83 |
| Ownership records written into DNS | 83 of 83 |
| Sitemaps handed to Google | 83 of 83 |
| Sitemaps Google accepted with zero errors | verified on a 10-site spot check, 3 pages each |

Each site is registered as a whole-domain property, which covers the plain
address, the www address, and every page under both.

## What this actually does

It does not make the sites live. They were already live and open to Google
before any of this. What it does give us:

- Google now accepts a direct list of every page on every site instead of
  waiting to stumble across them.
- We can see, per site, which pages Google has actually stored and which
  searches are starting to show them.
- We can nudge individual pages when they are slow to appear.

## How it was done

Adding 83 properties by hand through the Search Console screens would have
taken hours. Instead it ran through Google's own interface for this, using a
one-hour access key Dan generated and handed over through the secure form. The
key expired on its own; nothing lasting was granted.

Three steps per site:

1. Ask Google for the private value that proves we own the domain.
2. Write that value into the domain's DNS at Cloudflare.
3. Tell Google to check, then register the site and hand it the sitemap.

## Scripts

| File | Does |
|---|---|
| `gsc.py tokens` | Collects the ownership value for each domain |
| `gsc.py dns` | Writes those values into DNS at Cloudflare |
| `gsc.py verify` | First pass at claiming and submitting |
| `gsc_fix.py` | The reliable claimer — reads the property list back as truth |
| `gsc_sitemaps.py` | Confirms every sitemap is genuinely submitted, resubmits gaps |
| `gsc_audit.py check` | Lists what is present and what is missing |

State lives in `data/gsc.json` and `data/gsc_sitemaps_done.json`, so every
script can be stopped and re-run and only picks up unfinished work.

## Two things that cost time, recorded so they do not repeat

**Google's replies come back empty when called quickly.** Running several
domains at once, or even in fast succession, returns a blank body rather than an
error. An early version of the script read a blank body as success and reported
83 finished when only 27 had landed. Every step now reads the result back before
counting it, and the same discipline already applies to the Cloudflare work.

**The ownership check needs a request body, not address parameters.** Passing the
domain as `site.type` and `site.identifier` in the address returns a success code
without doing anything. It has to go in the body as
`{"site": {"type": "INET_DOMAIN", "identifier": "<domain>"}}`.

## What to watch over the next few weeks

Nothing here produces rankings. The sites went live yesterday. Realistically:

- Days: Google stores the pages. Watch the page count per site climb from 0 to 3.
- Weeks: the sites start appearing for their own name and long, specific searches.
- Months: movement on the searches that actually carry money.

The listings and links work is what moves that timeline, not Search Console.

## Not done

To pull the numbers back out of Search Console on a schedule, we need a lasting
connection rather than a one-hour key. The connected Search Console tool can
already read how each site is doing and can nudge individual pages, so a weekly
report is possible without going back to Google for another key.
