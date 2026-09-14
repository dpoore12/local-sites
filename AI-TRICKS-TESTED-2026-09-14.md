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

## Standing instruction

Dan: "I am going to pump stuff to you and if it helps and needs things you
can do -- do it but always note it and store what you did in the repo."
This file is that log. Add to it, don't replace it, as more tips come in.
