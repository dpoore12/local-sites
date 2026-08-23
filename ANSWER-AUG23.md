# Two Questions, Answered

## 1. How do calls get to a local business fast?

Already built. One command, about ten seconds.

```
cd call-desk && python3 flip.py sacramentoacrepair.com +19165551234
```

From that second on, anyone calling the Sacramento site's number rings that
business's phone. The business hears a whisper first — "call from your
Sacramento air conditioner repair website" — so they know why it's ringing. The
caller's real number shows on their screen so they can call back. If nobody
answers in 25 seconds it drops to voicemail so no call is ever lost.

To take it back: `python3 flip.py sacramentoacrepair.com off`.

Right now all 83 numbers answer with a market-specific greeting and record a
voicemail. Nothing is recorded except voicemails people leave on purpose.

**The only thing missing is a phone number to point it at.** That's question 2.

## 2. How do we reach the businesses?

### The one thing every operator who has actually done this says

Don't pitch an empty site. Wait for the first real call, then push that call at
5-8 businesses in that city: *"I wait until I'm receiving calls before I start to
rent them... It's much easier to push a few calls/voicemails to a prospect and
tell them 'Hey, want more of these?'"*
([Warrior Forum](https://www.warriorforum.com/offline-marketing/811300-leasing-websites-instead-selling-web-design-not-related-rank-rent.html)).
The one operator with a real portfolio does the same and offers *"a few days of
free leads to get a feel for the relationship"*
([Side Hustle Nation](https://www.sidehustlenation.com/rank-and-rent/)).

So the trigger is a call, not a calendar date. A voicemail transcript in an
email is the whole pitch.

### The offer

Free for two weeks. One business in the city, never shared. Nothing to sign.
After that a flat monthly fee, same price whether they get 5 calls or 25.

That is the exact opposite of what they pay now, which is the whole reason it
works: Angi shares each lead with 3-8 contractors on a 12-month contract with a
30-35% cancellation penalty, at $35-$120 a lead depending on trade
([Lead Truffle](https://www.leadtruffle.co/blog/angi-leads-cost-pricing-contractors-2026/)).
Google's own local ads run $53 a lead blended, $57 for plumbing
([SearchLight, $6.72M of spend across 888 contractors](https://searchlightdigital.io/google-local-service-ads-cost-per-lead/)).
Injury attorneys pay $175-$425 a lead, and car-accident leads run $300-$1,500
([Rankings.io](https://rankings.io/blog/attorney-pay-per-lead/)).

Never explain how the site ranks. Sell "calls forwarded to your phone,
exclusive, flat fee." One operator quit this business specifically because he
kept trying to explain the model
([r/juststart](https://www.reddit.com/r/juststart/comments/12enb3i/rank_and_rent_what_do_you_know_about_it/)).

### The channels

Email first, one DM as the second touch. No cold texting ever — texting a
business owner's mobile without written consent is $500-$1,500 per violation per
person
([BCLP](https://www.bclplaw.com/en-US/events-insights-news/the-tcpas-new-opt-out-rules-take-effect-on-april-11-2025-what-does-this-mean-for-businesses.html)).

- Home services: email, then a Facebook page DM. Facebook is where these owners
  are — 32% of high-performing home-service businesses say it's their winning
  channel, from a survey of 1,050 US owners
  ([Jobber](https://www.getjobber.com/home-service-trends-report/)).
- Legal: email, then a LinkedIn note. Slow — a free LinkedIn account gets five
  personalized connection notes a month
  ([LinkedIn](https://www.linkedin.com/help/linkedin/answer/a550555)).

Four touches, 3-4 days apart, first email under 80 words. Small batches beat big
ones: under 50 recipients replies at 5.8% versus 2.1% at 1,000+
([Woodpecker](https://woodpecker.co/blog/cold-email-statistics/)).

Full copy for every email and DM is in `OUTREACH.md`.

## Who to email — the list

`data/prospects.csv`. Real owners, real verified work emails, pulled from Apollo
and sorted best-first per market.

| | |
|---|---|
| Owners with a verified email | 405 (still filling) |
| Right trade, no question | 338 |
| Markets with at least one | 67 of 83 |
| Markets with three or more | 58 |

Columns include `trade_match` — `CHECK` means Apollo's tags returned someone in
a neighboring trade (a roofer under an AC search), so read those before sending.
`found_by` says `city`, `metro`, or `state` — anything other than `city` may not
actually be local.

Rebuild or extend it with `python3 prospects.py search`, then `enrich`, then
`sheet`. Apollo rate-limits hard, so it runs slow on purpose and resumes where it
stopped.

### The 16 markets with nobody yet

Almost all garage door in small suburbs, plus a few others. Apollo simply does
not carry two-truck garage door shops in Eden Prairie or Overland Park. Those
need a different source — the local business listings themselves — which is a
separate job.

```
edenprairiegaragedoorrepairpros.com   overlandparkgaragedoorrepairpros.com
tucsonemergencyplumberpros.com        victorvillecaraccidentlawyerpros.com
virginiabeachcaraccidentlawyerpros.com  virginiabeachpersonalinjurylawyerpros.com
waterdamageaustinco.com               westcovinacaraccidentlawyerpros.com
fortworthgaragedoorrepairpros.com     garagedoorrepairnapervillepros.com
garlandgaragedoorrepairexperts.com    mariettagaragedoorrepairpros.com
mckinneygaragedoorrepairpros.com      mesquiteacrepairpros.com
parkergaragedoorrepairexperts.com     bocaratongaragedoorrepairpros.com
```

## Three things to do before the first email goes out

**1. Buy separate sending domains.** Three or four throwaway .coms, two or three
mailboxes each. Never send this from executivesearchsf.com — reputation is
judged at the domain level, so burning it stops mail reaching your own clients
([Hunter](https://hunter.io/cold-email-guide/dedicated-cold-email-domain/)).
Set SPF, DKIM and DMARC on each, warm them 2-4 weeks, then cap at 20-30 a day
per mailbox ([Google](https://support.google.com/a/answer/81126)).

**2. Get a mailing address.** Every cold email must carry a real postal address
and a working opt-out, honored within 10 business days. Missing either is up to
$53,088 per email
([FTC](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business)).
A PO box or a mailbox service is fine.

**3. Keep every subject line literally true.** 24 of the 83 sites are in
California, where a misleading subject line or From name in a commercial email
is $1,000 per email, up to $1,000,000 per incident
([Cal. B&P §17529.5](https://california.public.law/codes/business_and_professions_code_section_17529.5)).
"Your Plano garage door site" is fine. "Re: our conversation" is not. This is
the single largest money risk in the whole plan.

## One real problem: the five Florida legal sites

Florida says a website that hands prospective clients to lawyers must have
lawyers from at least four different firms on it. The Florida Supreme Court
wrote that rule for exactly this reason: to *"prevent an individual lawyer from
misleading the public by advertising in the guise of a qualifying provider but
funneling clients directly to a single firm"*
([Florida Supreme Court](https://caselaw.findlaw.com/court/fl-supreme-court/2319392.html),
[Florida Bar Advertising Handbook 2025](https://www-media.floridabar.org/uploads/2025/12/Handbook-2025-Approved-by-SCA-12-10-25.pdf)).

So a neutral-branded Florida legal site rented to one firm is a problem. Fix:
put the firm's own name, city and responsible-lawyer line on every page so the
site is plainly that firm's own advertising. Get a written Florida ethics opinion
before invoicing a Florida firm.

The five, from `data/nap.csv`:

```
fortlauderdaledomesticviolencelawyer.com
jacksonvillewrongfuldeathlawyerpros.com
orlandoduilawyerpros.com
tampacriminaldefenselawyerpros.com
tampafamilylawattorneypros.com
```

Everywhere else, flat rent to one named firm is fine as advertising, as long as
no site says "we recommend", "top-rated", or "we matched you", nobody screens a
caller's case, and the fee is never a percentage
([ABA Rule 7.2 comments](https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_7_2_advertising/comment_on_rule_7_2/)).

## What nobody publishes

No operator anywhere publishes a free-trial-to-paid conversion rate, and no
vendor publishes reply rates for contractors or small law firms specifically.
The closest real number is 0.72% reply for companies with 0-10 employees
([Belkins, 7.5M emails](https://belkins.io/blog/cold-email-response-rates)).
Nobody has documented signing a tenant purely by email either — the one operator
who tried DM-only never reported closing one
([r/juststart](https://www.reddit.com/r/juststart/comments/t12nlw/rank_rent_local_home_service_business_case_study/)).
Treat all of it as directional.
