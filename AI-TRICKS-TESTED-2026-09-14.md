# Two social-media SEO tips, actually run — 14 Sep 2026

Dan asked that any tip he sends gets a real test, not just filed away, with
what was done and found written here regardless of outcome.

## Tip 1 (Gobig Systems reel): competitor content-gap comparison

**The method as given:** Google your service+city, take the top 3 real
competitors, paste their pages and yours into AI, ask it to compare and find
what you're missing, then fill the gaps with real interviewed knowledge.

**Run for real** on `mesquiteacrepairpros.com` against the actual top-3
non-national-chain competitors for "ac repair mesquite tx": Mesquite Heating
and Air Conditioning Inc., Airtron, and Baker Brothers. Fetched and read all
four pages in full (not summaries).

**Result: no urgent gap found. If anything, our page is already ahead of
theirs on the dimension the shelf cares about most.**

- All three competitors lean on claims we structurally cannot make (a real
  license number, "since 1945," named staff, customer reviews with dates) --
  correctly excluded per `citation-packets/*.md`'s own rule. Not a gap, a
  deliberate compliance boundary.
- None of the three competitors cite a single external source anywhere on
  their pages. Our page cites Mesquite's 2026 Hazard Mitigation Plan, NWS
  DFW temperature data, ERCOT's 2024 peak load, and TDLR's contractor
  license lookup -- with links. That is the "fingerprinted content beats
  a templated twin" claim (register C-025/C-026) showing up as true on
  contact with a real competitor set, not just a theory.
- One soft, low-priority idea, not urgent: Baker Brothers separately covers
  duct cleaning, evaporator-coil cleaning, attic insulation, and thermostat
  repair as named topics. Our site covers 4 services (compressor, refrigerant
  leak, tune-up, general repair). Worth a look **only if** real local search
  volume supports a page for one of those -- not a blanket "add more pages,"
  since today's own cohort test found page count alone doesn't move clicks.

**Verdict: technique works as a sanity check, did not surface new work here.**
Worth re-running per-market as new competitors are checked, since the
"nothing missing" result could differ elsewhere.

## Tip 2 (Gobig Systems reel #2): GSC queries with no dedicated page

**The method as given:** Search Console -> Performance -> copy the sitemap
URL -> paste sitemap + Search Console query data into AI -> ask it to find
ranked keywords that have no page of their own.

**Run for real** across the whole network using the GSC pull already done
today (1,358 site/query rows, 28-day window) cross-referenced against every
site's actual service slugs, names and keywords from its own `site.json`.

**Result: 3 candidates out of 1,358 rows, and none of the 3 hold up.**

| Site | Query | Why it looked like a gap | Why it isn't one |
|---|---|---|---|
| tempeduilawyerpros.com | "camp verde dui attorney" | No page matches "Camp Verde" | Camp Verde is a different AZ town, not Tempe -- Google broad-matching us to it, not a page we're missing on this domain |
| newportbeachduilawyerpros.com | "newport beach california dui lawyers" | Matcher didn't check city name, only service keywords | False positive -- the homepage IS this exact page |
| sandiegodogbitelawyerpros.com | "dog attorney near me" | No page uses the word "attorney" | Synonym of "dog bite lawyer," already covered, just different wording |

**Verdict: no real missed-page opportunities exist in the current top
queries.** Consistent with everything else found today (internal linking
already solid, page count doesn't move clicks) -- the site structure isn't
the constraint. Re-run this monthly as query mix shifts; a real gap would
show up as a genuinely new topic with real impressions and zero page match,
which none of these three are.

## Tip 3 (Gobig Systems reel #3): GBP primary category vs. competitors

**The method as given:** Open your Google Business Profile, check your
primary and secondary categories. Install the "GMB Spy" Chrome extension,
search your service on Google Maps, check what category the top-ranking
competitors use as primary. If theirs differs from yours, fix it -- called
"a huge factor." Add any secondary categories you're missing too.

**Not runnable today -- correctly, not a gap.** None of the 87 sites have a
Google Business Profile at all. That's the deliberate decision already on
record in `PLAYBOOK-LINKS.md`: registering fake addresses across dozens of
cities to create GBP listings is the exact pattern Google's guidelines are
written to catch and suspend. There is no profile to open, so there's
nothing this technique can check right now.

**Queued, not dropped.** The playbook already has the right home for this:
once a tenant signs, calls route into *their* existing, real GBP rather
than a new one. At that point this is a real, correct move -- check their
primary category against the top local-pack competitors', fix a mismatch,
fill in secondary categories. Re-read this section the day the first
tenant signs.

## Tip 4 (Gobig Systems reel #4): find high-impression low-click pages, rewrite the title

**The method as given:** Search Console -> Performance -> export -> paste
into AI -> find pages with lots of impressions but few clicks -> have AI
rewrite the title to match the search better -> more clicks, possibly
better rank.

**Run for real.** Pulled page-level GSC data (585 pages, 28-day window)
across the network. Filtered first the naive way (>=30 impressions, <1%
CTR): 122 pages, but almost all of them sit at position 60-90, where 0%
CTR is just what position explains on its own -- a title rewrite there is
rearranging deck chairs. Refiltered to the only cases where a title could
plausibly matter: position <=30 with real impressions. 20 pages qualified,
two on page 1 (position ~5) with zero clicks -- looked like exactly what
the tip describes.

**Checked the actual queries behind those two instead of touching a title
blind, and neither held up:**

- `sandiegowrongfulterminationlaw.com/severance-agreement-review/` looked
  like 102 impressions at position 5. The real per-query breakdown: 8
  impressions total, all one obscure legal-citation search ("12964.5"
  "five business days"). Not a real audience -- nothing to fix.
- `jonesboropersonalinjurylawyerpros.com/` looked like 937 impressions at
  position 29.6 -- a real candidate. Broken into actual queries: it's
  getting real volume on generic, non-geo-qualified terms ("car accident
  lawyer near me" 139 impr, "car accident lawyer" 88 impr, "injury lawyer"
  23 impr) at position 30-34, not 29.6. Google is geo-matching a Jonesboro
  site to people physically near Jonesboro searching bare national terms
  -- a genuinely useful discovery on its own -- but the true position
  for that real volume is still page 3-4. A title rewrite doesn't move a
  page-3 result to where anyone clicks.

**No titles changed. Verdict: the tip's premise (page 1 position, fixable
by title) didn't survive contact with the real per-query data on either
candidate found today.** Worth re-running once any page has a real,
query-verified position in the top 10 with genuinely low CTR -- that
case would be worth a title rewrite. Neither candidate today was that.

**The bigger finding, independent of the tip: GSC's page-level "position"
is a blended average across every query that page matched, and it can be
badly misleading** -- a page can show an attractive aggregate position
while the queries carrying its real volume sit 20+ positions deeper.
Any future GSC read (including earlier ones today) should check per-query
data before trusting a page's headline position number.

## Tip 5 (Gobig Systems reel #5): AI-interview yourself for original numbers

**The method as given:** Copy a page's content, paste into AI, have it
interview you for original info -- specific numbers especially: years in
business, homeowners served, jobs completed.

**Not runnable today, same reason as tip 3.** This requires a real business
owner with real operating history to interview. None of the 87 sites have
one yet -- they're pre-tenant shells. Fabricating "since 2015" or "4,000+
jobs completed" would be false advertising, and it's the exact thing
`citation-packets/*.md` already forbids in writing: *"Do not claim a
licence, a year founded, staff, or years in business."*

**Already doing the substitute, and it's a stronger version.** The sites
already carry specific, real numbers -- just sourced from government/public
data (city hazard plans, NWS, ERCOT, TDLR license lookups, with links)
instead of self-reported business history. Tip 1's test today showed that
already beats real competitors, none of whom cite any source at all.
Self-reported "years in business" is optional-trust; a cited government
number isn't.

**Queued for real.** The day a tenant signs, they have actual years in
business, actual jobs completed, actual customers served -- that's exactly
when to run this interview technique for real, adding their real numbers
on top of the sourced local facts already there.

## Standing instruction

Dan: "I am going to pump stuff to you and if it helps and needs things you
can do -- do it but always note it and store what you did in the repo."
This file is that log. Add to it, don't replace it, as more tips come in.
