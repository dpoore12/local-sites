# UG — read this, then start

Everything below is now in the repo. Pushed to `master`.

## Start here

`UG-STATUS.md` — the current state of all 83 sites, every script, every trap in
one place. It replaces the status sections in `HANDOFF-UG.md`, which I stripped
out because they were stale enough to send you down wrong paths. `HANDOFF-UG.md`
is still correct on architecture, rules and traps.

## What changed since you last looked

**All 83 sites are live.** Hosting got rebuilt around a single Cloudflare Pages
project with a router function, because Cloudflare caps projects per account and
we hit it around 22. `deploy_sites.py` is dead. The new pipeline is in
`UG-STATUS.md` and the credential-on / credential-off sequence in it is not
optional — the sandbox proxy overwrites the auth header on Cloudflare calls and
blocks every non-Cloudflare host.

**All 83 were accidentally invisible to Google.** `build.py` has a `--live` flag
that had never been used, so every page shipped with a do-not-index tag. Caught
and fixed the same night. Always build with `--live`. `check_seo.py` exists to
catch it and reports 83 of 83 clean.

**All 83 are now in Search Console** with ownership confirmed and sitemaps
submitted, zero errors. So the "submit to Search Console" step at the top of the
old playbook is done — skip it. See `SEARCH-CONSOLE.md`.

**The tenant question is answered.** See below.

## Your job

`BRIEF-LISTINGS-UG.md` (I appended an update at the bottom), then batch 1 of
`data/queue.csv`. Batch 1 is $15,500/month of modelled value.

Copy business details from `data/nap.csv` every single time, byte-identical.
`data/link-prospects.csv` has 120 local targets, every URL opened and confirmed.

**One thing I need from Dan and so do you: a single business address.** Some
listings demand a verified street address in that city. Where we cannot supply
one, mark the row `blocked — needs local address`. Never invent one.

## Tenants — the answer, and why it touches your work

Dan will not do phone selling, which rules out how this model is normally run.
Six routes were researched. Ranked first: sell the calls into pay-per-call
networks through a bid auction. No persuasion, published prices in all six of our
niches, live in days, pays proportionally across 83 sites at very different
traffic levels. Full evidence and the other five routes in `TENANTS.md`.

Two consequences for you:

1. **Every call must be attributable to exactly one site.** Routing already
   guarantees it, one handler per market. Never share a number between two sites
   in a listing, and never substitute a number — always copy from `nap.csv`.
2. **Never create a Google Business Profile.** This was already rule one because
   83 addresses on one account gets suspended. It is now firmer: Google's
   guidelines list lead generation companies as ineligible for a profile at all
   and allow them to revoke one. It is the portfolio's largest correlated risk.

## One thing I did not resolve, deliberately

`README.md` says this is not a per-call marketplace, and the pages carry no
routing disclaimers because each site is rented to one named operator. The
ranked tenant plan involves distributing calls, which changes that position. I
flagged it at the top of `README.md` rather than quietly rewriting it.

**Do not change any copy on this basis and do not connect any site to a call
network until Dan rules on it.**

## The pattern behind almost every bug so far

An empty reply is not a zero. It is a retry.

Google, Cloudflare and Telnyx all return blank bodies rather than errors when
called quickly. An early Search Console script read blanks as success and
reported 83 finished when 27 had landed. The same thing produced a false "23 area
codes out of stock" reading on Telnyx. Every script now reads its result back
before counting it. Keep that discipline in anything you add.

Full list of traps at the bottom of `UG-STATUS.md`.

Questions to Dan.
