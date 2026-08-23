# Listings brief — UG

## What this is

We own 83 websites. Each one covers one service in one city — garage door repair
in Fort Worth, dog bite lawyers in San Diego, and so on. Each has its own domain,
its own phone number, and its own pages written for that city. They all went live
on 22 August 2026.

A site earns nothing until it shows up in Google, and Google mostly decides that
on two things: what is on the page, and who else on the web points at it. The
pages are done. This job is the second half.

## What you are doing

Getting each of the 83 sites listed on the free directories, and getting a
handful of genuinely local websites in each city to link to it.

Target is 10 to 30 links per site. Not 500. The businesses we are competing with
have a two-page website from 2012 and almost no links, so fifteen decent ones is
enough. Once a site ranks in a small local market it mostly stays there, which is
the only reason 83 of them is manageable.

## The files

Everything is in `local-sites/data/`:

| File | Use it for |
|---|---|
| `queue.csv` | **Your worklist.** Every site crossed with every listing it needs. Already sorted so the most valuable sites come first, and split into 11 batches of 8 sites. Work batch 1, then batch 2. |
| `nap.csv` | The exact business name, phone, city and description for each site. **Copy from here every single time.** |
| `link-prospects.csv` | Local link targets for the top 12 cities — community pages, chambers, local papers, bar associations. Every URL was opened and confirmed live. |

Update the `status` column in `queue.csv` as you go: `todo` → `done`, or
`blocked` with a short note saying why. Commit the file when you finish a batch
so we can both see progress.

## The one rule that matters most

**The business name, phone number and description must be byte-identical
everywhere they appear.** Not "close enough". Identical.

Google cross-references these listings against each other. Consistent details
read as a real business. Inconsistent details read as noise and the listings stop
helping. This is why `nap.csv` exists — never retype from memory, always copy and
paste from that file.

## Order of work, per site

Do all seven of these for one site before moving to the next. Bouncing between
sites is how details drift.

1. **Yelp** — `biz.yelp.com`. Claim or create. Real call volume in home services.
   Do not ask anyone for reviews.
2. **Nextdoor Business** — `business.nextdoor.com`. Genuinely local, and the
   neighborhoods we name on the page are the ones on Nextdoor.
3. **Apple Business Connect** — `businessconnect.apple.com`. Feeds Apple Maps and
   Siri. Almost nobody in these trades has bothered, so it is cheap distinction.
4. **Better Business Bureau** — `bbb.org`. Free listing only. Do not buy
   accreditation.
5. **Yellow Pages** — `yellowpages.com`. Free tier. Low value, two minutes.

Then, **home services sites only** (43 of the 83 — the `niche` column says which):

6. **Houzz** `houzz.com/pro`, then **Angi**, **Thumbtack**, **Porch**,
   **BuildZoom**, **Networx**. Houzz is the best of these. Expect Angi to start
   calling you; that is normal, ignore it.

Then, from `link-prospects.csv` for that city:

7. Work the rows marked free first. The best ones are community and HOA pages that
   openly invite businesses to be added — those are a form submission, not a
   negotiation. Examples already confirmed: Hidden Valley Tucson's recommended
   businesses page, Stonebridge Ranch in McKinney, RHENA Tucson's service
   provider directory.

About ten items per site. Roughly a day per batch of eight.

## Two things you cannot do without Dan

**Search Console and Bing.** These sit on Dan's Google account, so he does them,
not you. They are already in `queue.csv` as the first two rows of every site —
leave them alone and he will tick them off.

**The address.** Most listings want a street address and we do not have 83 of
them. Ask Dan for the one business address to use before you start batch 1.
Then:

- If a listing accepts a service area with a city and a phone and no street
  address, use that. Most on our list do.
- If it accepts our single real address, use that one, the same one, every time.
- If it demands a verified street address in that specific city, **skip it and
  mark the row `blocked — needs local address`.** Do not invent an address and do
  not rent a mailbox. That is the thing that gets every listing we own killed at
  once, not just the one.

## Things that will get us wiped out — never do these

- **Never create a Google Business Profile.** Not one. It needs a verified real
  address per city and 83 of those is the exact pattern Google suspends whole
  accounts over. We are deliberately giving up the map results and taking normal
  search positions instead. This is decided, not up for optimising.
- **Never link our 83 sites to each other.** One link between two of them turns an
  83-site portfolio into one detectable network. If a directory offers to link
  your other listings together, decline.
- **Never buy links.** No link packages, no guest post marketplaces, no Fiverr.
  If a site's pitch is that they will sell you a link, close the tab.
- **Never ask for a review** on any listing. We are not the ones doing the repair
  work. Fake or solicited reviews on a business that has not served the customer
  is the fastest way to lose a listing permanently.
- **Never create a lawyer profile** on Justia, Avvo, FindLaw or a bar directory.
  Those profiles describe a named, licensed attorney and we do not have one yet.
  All 240 of those rows are already marked `hold until a firm signs` — leave them
  exactly as they are.

## When something goes wrong

- **A listing wants a phone verification code.** The number is a real number that
  we control. Tell Dan which site and he can read the code off the call log.
- **A listing rejects us as a duplicate.** Someone already listed that name.
  Claim the existing one rather than making a second.
- **A listing wants money.** Chambers of commerce are the only paid thing worth
  buying and only on sites that already have a paying tenant. Everything else,
  take the free tier. If in doubt, mark it `blocked — wants payment` and ask.
- **A form asks how many employees or years in business.** Leave it blank if it
  lets you. Do not guess a number that becomes a claim.

## When to stop

Eight weeks per site, then stop. Do not keep adding links to a site that is
already ranking. The work is front-loaded on purpose so it ends.

## Background if you want it

- `LISTINGS.md` — the short version of this plan
- `PLAYBOOK-LINKS.md` — the full reasoning and where each number came from
- `HANDOFF-UG.md` — how the sites are built, hosted and wired to phones
