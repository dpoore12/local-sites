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

## Tip 6 (Gobig Systems reel #6): link from a clicking page to your money page

**The method as given:** Search Console -> Performance -> search results ->
pages, find a page that's already getting real clicks, open it, add a link
to your main service page. Google treats links like votes, so link from a
page it already likes to the page that makes money.

**Run for real, no new data needed** -- reused today's page-level GSC pull.
Only 3 of 585 measured pages across the whole network have gotten a single
real click in 28 days: `tampacriminaldefenselawyerpros.com/bond-hearings-
and-pretrial-release/` (5 clicks), `concordcaraccidentlawyerpros.com/rear-
end-collision-lawyer/` (1), `bellevuebathroomremodeling.com/walk-in-shower-
installation/` (1). Pulled the live outbound links on all three.

**Already done, verified live, nothing to add.** Every one of the three
already links to home, `/pricing/`, `/services/` and its sibling service
pages. That's `service.html`'s built-in "the other three jobs" cross-link
section plus the sitewide footer, doing exactly what this tip recommends,
automatically, on every page on every site -- not something that needed
fixing.

## Tip 7 (Gobig Systems reel #7): prune zero-click pages with no external links

**The method as given, in full (a first partial read of the reel nearly
produced a wrong call here):** Search Console -> Performance -> pages,
sort the last 16 months, find pages with zero clicks. Then check external
links -- any zero-click page that has real external links pointing to it,
keep. Only the ones with zero clicks *and* zero external links are
candidates to delete, redirected to a relevant page.

**This is legitimate practice for a mature site, and it does not fire on
anything here -- for a specific, correct reason, not because the technique
is bad.** Only 3 of 585 measured pages have a click. Read naively ("delete
everything with zero clicks"), that's instructions to delete almost the
entire network -- which would be actively harmful, since these are
unranked pages sitting at position 60-90 for the authority reasons found
all day, not dead or low-quality content. Read correctly with the external-
links filter: the network currently has 0 citations actually submitted and
0-3 referring domains total per site, so essentially no deep page has a
real external link pointing at it either. The filter would still return
"delete nearly everything," which is the wrong output at this stage of the
network's life, not a green light.

**No pages deleted or redirected.** Queued the correct way -- re-run this
once real citations/links exist and a meaningful number of pages have had
real crawl/index time. At that point a page with genuinely zero clicks
*and* zero external links after a fair runway is a real pruning candidate.
Today, none of them have had that runway yet.

## Tip 8 (Gobig Systems reel #8): position 11-20 queries, beat whoever's #1

**The method as given:** Search Console -> Performance -> turn on average
position -> filter to position 11-20 -> sort by impressions -> open the
page -> compare it to whoever ranks #1 for that query -> add what's
missing (original data, stories, FAQs).

**Run for real using today's query pull, no new calls.** 49 (site, query)
rows sit at position 11-20 -- genuinely the closest band found all day.
Top ones: `oceansidepersonalinjurylawyerpros.com` / "injury lawyer" (pos
17.3, 28 impr), `jonesboropersonalinjurylawyerpros.com` / "injury lawyer"
(pos 18.0), `salinascaraccidentlawyer.com` / "car accident lawyer" (pos
19.9), `bellevuebathroomremodeling.com` / "bathroom remodeling" (pos 15.3).

**One catch that changes how to apply it: almost every one of these is a
generic, non-geo-qualified term, same pattern as the Jonesboro discovery
in tip 4.** Google is showing a small local page to searchers physically
near that city for a bare national query, not because the page is
genuinely competitive for it. Comparing against the literal #1 result for
"injury lawyer" nationally would mean comparing against a mega-firm or
Justia -- not a winnable content gap, just a mismatched comparison. The
tip's mechanism only works when the query itself is winnable, which for
these is really the geo-qualified version ("injury lawyer jonesboro ar"),
and that comparison is exactly the copycat method already run five times
today (tips 1 and this session's earlier work).

**Verdict: the targeting idea is genuinely good -- position 11-20 is the
right place to look for close wins, better than the 60-90 band most of
the network sits in.** But run it as: geo-qualify the query, then copycat
the real local competitor, not the broad-query #1. No new comparison run
this round since the method itself isn't new; logging the refinement.

## Tip 9 (Gobig Systems reel #9): claim Apple Maps, Bing, Yelp/BBB, Nextdoor/Facebook/Alignable, Angi/Houzz/Thumbtack

**The method as given:** a category-matched directory list -- Google/Apple
Maps/Bing for local customers, Yelp/BBB for reviews, Nextdoor/Facebook/
Alignable for word of mouth, Angi/Houzz/Thumbtack if a contractor.

Checked what was new here (Angi/Houzz/Thumbtack already covered in
`PLAYBOOK-LINKS.md`'s Tier 2; BBB already confirmed dead this session):

- **Apple Business Connect** -- real, but heavier than a simple form. The
  signup path routes through the full "Apple Business" suite (device
  management, email, storage tiers), not a lightweight Maps listing by
  itself. Didn't find a direct standalone place-listing flow to test the
  address requirement. Lower priority than the confirmed four until
  someone works through the full Apple Business enrollment.
- **Bing Places** -- confirmed free ("list it on Bing for FREE"), but the
  signup wall requires a Microsoft account sign-in before any form
  appears, so the address/service-area question couldn't be verified live
  today. Worth trying by hand.
- **Nextdoor** -- the business.nextdoor.com path is paid ads, not a free
  page. A guessed direct URL for the free Business Page redirected to an
  unrelated existing business's page rather than a signup flow. Not
  confirmed either way -- needs a person to find the actual free-page path
  from a logged-in Nextdoor account, which this session doesn't have.
- **Facebook Business Page, Alignable** -- not checked yet, ran out of
  turn before reaching these.

**Nothing new added to the confirmed-free list.** Everything here is
either already covered, needs deeper manual verification than today's
session reached, or (Apple) is a bigger lift than the four already
confirmed. No account created, no forms submitted.

## Tip 10 (Gobig Systems reel #10): industries ranked by SEO difficulty

Not a technique -- a tier list (roofing C, lawyers F "spend money to
win," remodeling B, plumbing D, decks S, HVAC D, landscaping B, window
tint S). Worth a sanity check against real data rather than a re-run:
lawyers are called F-tier/pay-to-play, but 49 of the 87 sites are legal
and `tampacriminaldefenselawyerpros.com` is the single best-performing
site in the whole network (position 15.7) at zero spend. A tested result
already on record outranks an anecdotal tier list -- consistent with the
shelf's own marketing-claims-register rule. No action taken.

## Tip 11 (Gobig Systems reel #11): check GA4 for AI-assistant referral traffic

**The method as given:** Google Analytics -> Reports -> Acquisition ->
Traffic Acquisition -> Default Channel Group -> look for an "AI Assistant"
row showing visits from ChatGPT, Gemini or Claude.

**Checked directly, not applicable -- cleanly.** Grepped `template/base.html`
and the live HTML of a real page for `gtag`, `googletagmanager`, any GA4
measurement ID. None exist anywhere in the network. There is no Google
Analytics property on any of the 87 sites, so there's no "AI Assistant"
channel to look at. Not a partial result -- there is nothing to check.

## Tip 12 (Gobig Systems reel #12): GBP search-terms -> Gemini posts

Pull the real search terms from your Google Business Profile's performance
report, connect the profile to Gemini, have it draft posts using those
exact terms. Same blocker as tip 3: no GBP exists on any of the 87 sites,
deliberately. Not applicable for the same documented reason. No new check
needed -- this is the same category as tip 3 and tip 9's Google/Apple/Bing
section, not a distinct technique.

## Tip 14 (Gobig Systems reel #14): find keyword cannibalization via GSC pages-per-query -- REAL FIX SHIPPED

**The method as given:** Search Console -> Performance -> Search Results ->
click a keyword you're trying to rank for -> click Pages. More than one
page showing means two pages are splitting the same keyword and Google
shows neither well. Pick the strongest page, link the weaker one to it.

**Run for real, cheaply** -- one query at a time (not the expensive
network-wide join estimated for tip 8), checked the top 15 highest-
impression queries via `dimensionFilterGroups` filtered per query. Two
real hits:

- `mesquiteacrepairpros.com`: `/about/` was getting MORE impressions (211)
  than the homepage (138) for "ac repair mesquite tx."
- `fresnowrongfuldeathlawyerpros.com`: `/contact/` was ranking BETTER
  (position 64.0) than the homepage (85.7) for the core money keyword
  "fresno wrongful death lawyer."

(A third apparent hit on jonesboropersonalinjurylawyerpros.com was just
an http:// vs https:// artifact in GSC's history, 2-3 impressions --
ignored, not real.)

**Root cause found and fixed, not just described.** Both About and
Contact page `<title>` tags were built in `template/build.py` as
`"About -- {service} in {city}, {state}"` / `"Contact -- {service} in
{city}, {state}"` -- the *exact* commercial phrase the homepage targets.
Verified live on both sites before touching anything (curl'd the actual
`<title>` tags). This is systemic, not a two-site problem: every one of
the 87 sites' About/Contact pages carries this same title pattern.

**Fix shipped:** both titles now use the site's own `brand` name (already
distinct per site, e.g. "Mesquite Air Conditioner Repair Pros") instead of
repeating the money phrase. Verified all 87 sites still build clean before
committing. `template/build.py` commit 299b1a1, pushed to master. This is
the first tip out of 14 that produced an actual source-code fix rather
than a confirmation or a "not applicable."

## Tip 15 (Gobig Systems reel #15): mine Reddit questions, answer them, link to the service page

**The method as given:** Google `<service> site:reddit.com`, find a real
question someone asked, answer it as a blog post with a quick-answer
summary up top, link that post to the matching service page.

**Genuinely new and ties directly to something already found dormant in
the codebase today, not yet executed.** `template/build.py` has a full
`question.html` template and a `questions` mechanism in `site.json`.
Checked all 87 site.json files directly rather than assuming: 86 have zero
questions. One, `coloradospringsfurnacerepair.com`, has 20 written and
ready (real examples: "How Long a Furnace Lasts," volume 6,600) -- but its
live sitemap only shows 9 URLs, so even that one site's questions were
never actually built and deployed. The mechanism is real, tested-ready on
one site, and live nowhere. This tip is exactly the sourcing method it was
built for.

**UPDATE, later 14 Sep: RUN FOR REAL on 6 sites, all pushed to master.**
Same discipline every time -- a real `site:reddit.com` search read for the
actual symptom/question patterns across multiple threads, a real Ahrefs
volume check to confirm demand exists, then a page written against that
site's own already-sourced local_facts, never generic. Each page was
written as a diagnostic router to the site's existing services rather than
a duplicate of any one (the lesson from tip 14's cannibalization bug).
`question.html` auto-links every question page to the site's top 3
services, so the "link to the service page" step the tip asks for is
built in. All verified inside the 700-1150 QUESTION_WORDS band with all 87
sites building clean before each commit.

| Site | Page | Ahrefs vol/mo | KD | Words |
|---|---|---|---|---|
| mesquiteacrepairpros.com | /ac-blowing-warm-air/ | 1,700 | 2 | 998 |
| annarborgaragedoorrepairpros.com | /garage-door-opener-not-working/ | 1,900 | 3 | 786 |
| fresnowrongfuldeathlawyerpros.com | /how-long-does-a-wrongful-death-lawsuit-take/ | 200 | 0 | 944 |
| kalamazootowingpros.com | /car-wont-start-in-cold-weather/ | 250 | 0 | 756 |
| orlandomovingcompanypros.com | /how-far-in-advance-to-book-movers/ | 100 | 10 | 930 |
| sanjoseemergencyplumberpros.com | /low-water-pressure-in-house/ | 5,100 | 0 | 970 |

Every keyword difficulty is 0-10 -- the low-competition band Kyle's
playbook targets -- and the San Jose one (5,100/mo, KD 0) is the largest
uncontested term found all day. This is the first tip out of 16 that
produced net-new pages, not just a fix or a confirmation.

**Still needs Dan: none of these are deployed.** They exist in source on
master and build clean, but the Cloudflare deploy pipeline
(`deploy_add_mac.py`) needs an API token this session does not have. The
mesquite, ann arbor and the 4 other sites' live HTML does not yet include
these pages until a deploy runs. Same gap applies to the og:image fix and
the About/Contact title fix from earlier today.

**Next candidates, same method, not yet done:** the other 81 sites.
`coloradospringsfurnacerepair.com` is the cheapest -- 20 questions already
written in its site.json, needing only a build and deploy, no writing.

## Tip 16 (Gobig Systems reel #16): Foursquare, "Yellow Pages" (already dead), Manta

Three directories claimed to send trust signals Google likes.

- **Foursquare** -- confirmed dead. Fully pivoted to a B2B "location
  intelligence" data-sales platform ("Speak to sales," "Try for free" is a
  developer/marketer trial). No consumer free-business-listing product
  exists on the site anymore.
- **Yellow Pages** -- already tested and confirmed dead this session
  (tip 9 / earlier). Not re-tested.
- **Manta** -- real business directory (20+ years, still operating), but
  `/claim` hit the same Cloudflare bot-check wall as ibegin.com and
  place123.net earlier today. Not confirmed either way in automated
  testing. Worth trying directly in a real browser.

## Standing instruction

Dan: "I am going to pump stuff to you and if it helps and needs things you
can do -- do it but always note it and store what you did in the repo."
This file is that log. Add to it, don't replace it, as more tips come in.
