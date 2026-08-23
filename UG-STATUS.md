# Current state — 23 August 2026

Read this before anything else in the repo. It replaces every status claim in
`HANDOFF-UG.md`, which is now only architecture, rules and traps.

---

## The short version

All 83 sites are built, live, reachable, open to Google, in Search Console with
sitemaps submitted, and each has its own working phone number. The technical
build is finished.

Nothing earns a cent yet. Two things stand between here and revenue: getting the
sites found (your listings and links work) and getting the calls paid for (Dan's
side, plan below).

---

## What is done

| Thing | State |
|---|---|
| Template | Locked, tagged `template-v2`. Do not touch — see `template/LOCKED.md` |
| Copy | 83 sites written. Home, about, contact. Two also have a services hub |
| Domains | All 83 registered at Cloudflare, auto-renew on, expire 2027-08-22 |
| Phone numbers | All 83 live, each in its own market's area code, all routed |
| Call routing | Built and tested — voicemail plus a whisper announcing the site |
| Hosting | All 83 live, all returning 200 |
| Indexing | All 83 open to Google with a working sitemap and robots file |
| Search Console | All 83 registered and ownership-confirmed, sitemaps submitted |
| Listings and links | **Not started. This is your job.** |
| Tenants | **None. Zero revenue. Dan's side, plan below** |

---

## Hosting — read this, it changed

**One Cloudflare Pages project serves all 83 domains.** Not one project per
domain. Cloudflare caps projects per account and we hit the ceiling around 22, so
it was rebuilt around a single project with a small function that reads which
domain the visitor asked for and serves that site's folder.

- Project: `local-sites`, account `a3bf1a13d93899d8408b9d1ea94df078`
- Direct address: `https://local-sites-5d8.pages.dev` (note the `-5d8`, Cloudflare added it)
- The router: `router/functions/[[path]].js`
- DNS per domain: a `CNAME` on the plain domain pointing at that pages.dev address, proxied. No www records.

`deploy_sites.py` is dead. The pipeline is now, in this exact order:

    python3 template/build.py --live      # the --live flag is not optional
    python3 host_all.py stage             # no credential
    python3 host_all.py pass              # WITH the Cloudflare credential
    python3 host_all.py upload            # NO credential
    ./redeploy.sh                         # WITH the Cloudflare credential
    python3 host_all.py check             # NO credential
    python3 check_seo.py                  # NO credential

The credential on and off is not superstition. The sandbox's credential proxy
overwrites the authorisation header on every Cloudflare request, which destroys
the separate upload token wrangler needs. It also blocks every host that is not
Cloudflare, so any step that reads our own sites has to run without it.

Progress is kept in `data/hosting.json`, so every phase can be stopped and
re-run and only picks up what is unfinished.

Does consolidating hosting create a doorway-page problem? No. It is invisible to
visitors and to Google. Each domain keeps its own pages written for its own city,
its own phone number, and its own tenant. The shared box they are served from is
not something Google weighs.

---

## The `--live` flag — the mistake worth learning from

`template/build.py` has a `--live` flag that had never once been used. Without
it, every page carries a tag telling Google not to index it. All 83 sites went
live invisible to search. It was caught the same night and rebuilt.

**Always build with `--live` for anything that gets deployed.** `check_seo.py`
exists specifically to catch this and it now reports 83 of 83 clean. Run it
after every deploy.

---

## Search Console — what it is and is not

All 83 are registered as whole-domain properties with ownership confirmed and
sitemaps submitted. Details and scripts are in `SEARCH-CONSOLE.md`.

This did **not** make the sites live — they already were. What it gives us is
visibility: which pages Google has actually stored, which searches are starting
to surface them, and the ability to nudge a slow page.

Two API traps recorded there, both of which cost real time:

- **Google returns blank replies when called quickly.** Not errors — blanks. An
  early script read a blank as success and reported all 83 finished when 27 had
  landed. Every step now reads the result back before counting it. Same
  discipline as Telnyx and Cloudflare, which both do the same thing.
- **The ownership check needs a request body, not address parameters.** Passing
  the domain in the URL returns a success code and does nothing at all.

The access key used was a one-hour key and has expired. Nothing lasting was
granted. To pull numbers out of Search Console on a schedule, the connected
Search Console tool can already read performance and nudge pages without going
back to Google for another key.

---

## Your job: listings and links

Full brief in `BRIEF-LISTINGS-UG.md`. Method and reasoning in
`PLAYBOOK-LINKS.md`. Short version:

- Worklist is `data/queue.csv` — every site crossed with every listing it needs,
  sorted so the most valuable sites come first, split into 11 batches of 8.
- Copy business name, phone, city and description from `data/nap.csv` every
  single time. Byte-identical everywhere. Never retype from memory.
- `data/link-prospects.csv` has 120 local link targets across the top 12 cities.
  Every URL was opened and confirmed live.
- Batch 1 is $15,500/month of modelled value. Start there.

Update the `status` column as you go and commit at the end of each batch.

### Five things never to do

1. **Never create a Google Business Profile.** 83 addresses on one account gets
   the account suspended. This is a decision, not an oversight — and Google's own
   guidelines list lead generation companies as ineligible for a profile at all.
2. **Never link the 83 sites to each other.** A visible network of same-template
   sites pointing at each other is the single clearest pattern Google penalises.
3. **Never buy links.**
4. **Never ask for a review.** We are not the business being reviewed.
5. **Never create a lawyer or firm profile before a firm actually signs.** 240
   rows in the queue are already held back for this reason.

### One thing you need from Dan before batch 1

**One business address.** Some listings demand a verified street address in that
city. Where they do and we cannot supply one, mark the row
`blocked — needs local address`. Never invent an address.

---

## Tenants — how the sites get paid for

This was the open strategic question and it now has an answer. Full evidence in
`TENANTS.md`. Relevant to you because it changes what the sites are for.

Dan does not do phone selling, which rules out how this model is usually run.
Six routes were researched and ranked. The winner:

**Sell the calls into pay-per-call networks, routed through a bid auction.**
No persuasion involved at all. Published per-call prices exist in all six of our
niches. Live in days, no minimum call volume to get in. It pays proportionally
across 83 sites at wildly different traffic levels, which single flat-fee tenants
cannot do while most sites are still ramping.

Then, in order: hand tenant-side selling to a rank-and-rent broker (they will
not take sites without existing call flow, so this comes later); free-leads-first
delivered in writing, not email; brokered flat-fee deals direct with firms. Cold
email alone runs about one meeting per 6,000 sends and cannot fill 83 tenancies.
Selling the sites now is the trap — pre-revenue local sites fetch around $8k
against 20 to 60 times monthly once revenue is documented.

What this means for your work: the call has to be attributable to exactly one
site, every time. Call routing already guarantees that — one handler per market.
Do not do anything in the listings work that shares a phone number between two
sites.

---

## Where to start, today

1. `BRIEF-LISTINGS-UG.md`, then batch 1 of `data/queue.csv`. Highest value and
   nothing blocks it except the one address question.
2. Ask Dan for that address before you hit the first listing that needs it.
3. Sanity-check the 28 niche packs in `niches/`. Each defines the four service
   pages for a trade. A wrong sub-job propagates to every site in that trade, and
   now is the cheapest moment to catch it.
4. If you want a bonus job: a daily task that runs `python3 call-desk/call_log.py`
   and commits the log would make call tracking hands-off. Do not set it up until
   calls are actually arriving — Dan explicitly does not want it running yet.

Do not start on template changes. It is locked and the reason is in
`template/LOCKED.md`.

Questions to Dan.

---

## Every script, current

| Script | Does | Credential |
|---|---|---|
| `template/build.py --live` | Renders all 83 for real deployment | none |
| `template/build.py --check` | Guards only, renders nothing | none |
| `scaffold.py --status` | Honest per-site completion report | none |
| `host_all.py` | Hosting phases: reset, stage, pass, upload, publish, domains, check | mixed, see above |
| `redeploy.sh` | Builds the router bundle and creates the deployment | Cloudflare |
| `check_seo.py` | Confirms all 83 are open to Google with a working sitemap | none |
| `gsc.py` | Search Console: ownership values, DNS records, first claim pass | Google, Cloudflare |
| `gsc_fix.py` | The reliable Search Console claimer, reads the list back as truth | Google |
| `gsc_sitemaps.py` | Confirms every sitemap is genuinely submitted | Google |
| `gsc_audit.py check` | Lists what is present and missing in Search Console | Google |
| `build_listings.py` | Generates the details sheet and the raw work queue | none |
| `build_queue.py` | Orders the queue by site value into 11 batches | none |
| `cf_sync.py` / `domains.py` | Refresh the registrar snapshot, rewrite the ledger | Cloudflare |
| `phones.py` | Re-reads the carrier, reports drift against the sites | Telnyx |

---

## Traps, all of them, in one place

Every one of these cost hours. They share a shape: **an empty reply is not a
zero, it is a retry.**

- **Google** returns blank bodies when called quickly. Read every result back.
- **Google's ownership check** needs a JSON body, not URL parameters.
- **Cloudflare** returns empty bodies when throttled. Never read that as nothing.
- **Cloudflare's Pages project list** rejects `per_page` and `page` — call it bare.
- **Cloudflare** will not delete a Pages project until its custom domains go first.
- **Cloudflare** does not create DNS automatically when you attach a domain.
- **Cloudflare Registrar** pages by cursor; `page=2` silently returns page one.
- **Cloudflare Registrar** can return success with a failed state. Trust the
  account listing, not the create response.
- **Telnyx** returns silent empty pages instead of rate-limit errors. This
  produced a completely false "23 area codes out of stock" reading.
- **Telnyx** needs square brackets percent-encoded (`page%5Bsize%5D=50`).
- **Telnyx whisper** works only via `url` on `<Number>`, never on `<Dial>`.
- **wrangler 4 needs Node 22**; the sandbox has 20, so we use wrangler 3.
- **`httpx` ignores the sandbox proxy** for some hosts, so tokens never get
  attached and calls just fail. Use `curl`.
- **Backgrounded processes lose the credential proxy.** Run credentialed work in
  the foreground.
- **Sandbox commands time out around ten minutes.** Wrap long loops so they can
  resume.
- **`data/dataforseo` keyword difficulty numbers are wrong.** Do not use them.
