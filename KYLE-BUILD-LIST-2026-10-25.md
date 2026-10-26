# The markets Kyle would build — step one finished (25 Oct 2026)

## What was done

Kyle's step one: pick a Kyle-type service in a town of about 100,000 people or fewer, then size
up the **top 3 Google results** in that town. Check their authority, links, content, pictures and
headings, and build only where they're weak ("do 10% better than them").

- **Markets:** the 191 clean markets from the 29 Aug screen (Kyle-type services in towns of
  37k–100k people with real searches; `kyle-screen.csv`).
- **Fresh Google page one for each, located in that town** (DataForSEO, 25 Oct): top 10 results
  plus the map listings. `kyle-screen/oct-top3/serp/`.
- **Authority and traffic** for every site in the top 5 (Ahrefs Domain Rating, the same idea as
  the "domain authority" Kyle checks): 415 sites. `oct-top3/dr.txt`.
- **Words, pictures and headings** on every top-3 page (298 of 302 read). `oct-top3/pages.json`.
- **Scored** with `oct_score.py`, all 191 rows in `oct-top3/kyle-verdicts.csv`.

How a spot is graded, in Kyle's terms:
- **Weak:** a small local site, the "Joe, Bill and Steve" he describes (Domain Rating 15 or
  under, under 2,000 visits a month).
- **Strong:** Yelp/Angi/BBB-type directories, national brands, government sites, or any site at
  Domain Rating 30+.

## Result

| Verdict | Markets | Meaning |
|---|---:|---|
| **BUILD** | **37** | 2 or 3 of the top 3 are small local sites — the easiest fights |
| BUILD, second wave | 65 | 1 of the top 3 is weak and 2+ of the top 5 are (spots 3–5 still get calls) |
| Maybe | 53 | only 1 weak spot in the top 5 |
| Skip | 36 | top 5 all held by directories, national brands or strong sites |

## The 37 Kyle would build first

Sorted by lead value (searches × cost per click). "DR" is Ahrefs Domain Rating out of 100; the
sites we'd be competing with mostly sit at 0–15. Directories (Yelp, Angi, BBB…) hold a spot but
aren't local competitors. Every domain shown was free on 25 Oct (checked with the .com registry).

| # | Service | Town | People | Searches/mo | $/click | Who holds the top 3 now | Map listings | Free domain |
|---|---|---|---:|---:|---:|---|---|---|
| 1 | septic tank pumping | North Miami, FL | 61k | 260 | $215.13 | caraballoexpress.com (DR 0.8) · Yelp · septictank.com (DR 13) | 187 reviews | northmiamiseptictankpumpingpros.com |
| 2 | septic tank pumping | Hesperia, CA | 92k | 110 | $101.86 | Yelp · aoseptic.com (DR 0.4) · usaseptic.com (DR 3.6) | 773 reviews | hesperiasepticpumping.com |
| 3 | air duct cleaning | Apex, NC | 42k | 720 | $15.39 | Bbb · airductcleaningapex.com (DR 0) · airductcleaningapex.com (DR 0) | 3,200 reviews | apexairductcleaningpros.com |
| 4 | air duct cleaning | Kissimmee, FL | 65k | 260 | $39.82 | Angi · abc-cleaninginc.com (DR 13) · central-florida-ducts-lighting.com (DR 1.6) | 289 reviews | kissimmeeairductcleaningpros.com |
| 5 | air duct cleaning | Sarasota, FL | 53k | 320 | $28.00 | badgerbobs.com (DR 14) · Yelp · suncoastducts.com (DR 1.3) | 408 reviews | sarasotaairductcleaningpros.com |
| 6 | dumpster rental | Ocala, FL | 57k | 1000 | $8.61 | thejunksharks.com (DR 14) · wm.com (national) · ocaladumpsterrentals.com (DR 6) | 346 reviews | ocaladumpsterrentalco.com |
| 7 | air duct cleaning | Schaumburg, IL | 74k | 260 | $32.10 | staronductcleaning.com (DR 0.7) · cleanairwerks.com (DR 0) · Yelp | 422 reviews | schaumburgairductcleaningpros.com |
| 8 | dumpster rental | Pensacola, FL | 52k | 880 | $9.27 | wm.com (national) · coastalcontainer.com (DR 0) · dumpsterwerks.com (DR 0.2) | weak (top has 2) | pensacoladumpsterrentalpros.com |
| 9 | air duct cleaning | Littleton, CO | 44k | 210 | $32.45 | indoorqualityair.us (DR 0) · Yelp · airductprosdenver.com (DR 0) | 1,300 reviews | littletonairductcleaningpros.com |
| 10 | air duct cleaning | Marietta, GA | 59k | 210 | $29.69 | Yelp · airductcleaningga.com (DR 0) · ductorcleanair.com (DR 0) | 230 reviews | mariettaairductcleaningpros.com |
| 11 | dumpster rental | Bentonville, AR | 40k | 480 | $11.81 | Angi · dumpsterrentalcrewbentonville.com (DR 0) · martinsstucco.com (DR 0.3) | weak (top has 2) | bentonvilledumpsterrentalpros.com |
| 12 | window tinting | Bradenton, FL | 51k | 480 | $11.75 | tintworxfl.com (DR 0) · Yelp · mjtint.com (DR 0) | 210 reviews | windowtintingbradenton.com |
| 13 | dryer vent cleaning | Ocala, FL | 57k | 140 | $37.80 | Thumbtack · airfreshexperts.com (DR 2.2) · budsairocala.com (DR 2.2) | none | dryerventcleaningocala.com |
| 14 | air duct cleaning | Wheaton, IL | 53k | 70 | $71.93 | djrcleaning.com (DR 7) · Bbb · saiairductclean.com (DR 3.2) | none | wheatonairductcleaningpros.com |
| 15 | dumpster rental | Wellington, FL | 60k | 170 | $28.41 | wellingtondumpsterrental.com (DR 5) · langleydumpsters.com (DR 7) · precisiondisposal.us (DR 25) | weak (top has 1) | wellingtondumpsterrentalpros.com |
| 16 | dumpster rental | Canton, OH | 72k | 590 | $7.81 | cantondumpster.rentals (DR 0) · kingdumpsters.com (DR 6) · Yelp | 540 reviews | cantondumpsterrentalpros.com |
| 17 | dumpster rental | Biloxi, MS | 44k | 390 | $11.67 | gulfwidewaste.com (DR 0.2) · rubleinvestments.com (DR 0) · Yelp | 176 reviews | biloxidumpsterrentalpros.com |
| 18 | air duct cleaning | Pflugerville, TX | 53k | 90 | $50.22 | Thumbtack · kandmsteamcleaning.com (DR 12) · supremeairaustin.com (DR 11) | 1,000 reviews | pflugervilleairductcleaningpros.com |
| 19 | dryer vent cleaning | Sarasota, FL | 53k | 210 | $21.36 | vent-solutions.com (DR 0.1) · badgerbobs.com (DR 14) · Yelp | 942 reviews | sarasotadryerventcleaningpros.com |
| 20 | pressure washing | Pensacola, FL | 52k | 590 | $7.44 | Yelp · advancedpressurewashingllc.com (DR 8) · calldudewash.com (DR 1.9) | 384 reviews | pensacolapressurewashingpros.com |
| 21 | dumpster rental | Hagerstown, MD | 40k | 480 | $8.87 | Yelp · blueboxrental.com (DR 6) · dumpsterrentalshagerstown.com (DR 11) | 129 reviews | hagerstowndumpsterrentalpros.com |
| 22 | air duct cleaning | Ogden, UT | 84k | 110 | $38.64 | dustabductors.com (DR 7) · clearairutah.com (DR 1.2) · Yelp | 846 reviews | ogdenairductcleaningpros.com |
| 23 | air duct cleaning | Bradenton, FL | 51k | 110 | $38.61 | express-bradenton.com (DR 0) · Yelp · cleansweepductsac.com (DR 8) | 759 reviews | bradentonairductcleaningpros.com |
| 24 | air duct cleaning | Franklin, TN | 68k | 110 | $37.64 | nashvillesairductcleaning.com (DR 1.4) · Yelp · thecleanairco.com (DR 13) | 209 reviews | franklinairductcleaningpros.com |
| 25 | chimney sweep | Santa Barbara, CA | 90k | 140 | $29.52 | Yelp · sbchimneysweeps.com (DR 0) · tubulargeorge.com (DR 4.9) | weak (top has 19) | chimneysweepsantabarbara.com |
| 26 | air duct cleaning | Appleton, WI | 73k | 170 | $22.57 | mrpowerclean.com (DR 5) · foxvalleycleanair.com (DR 0) · Yelp | 841 reviews | appletonairductcleaningpros.com |
| 27 | dryer vent cleaning | Marietta, GA | 59k | 170 | $20.56 | thehonestguysatl.com (DR 10) · Yelp · dryerventcleaningmariettaga.com (DR 0) | 580 reviews | dryerventcleaningmarietta.com |
| 28 | pressure washing | Hilton Head Island, SC | 39k | 90 | $27.36 | windowgenie.com (DR 55) · southerncleansc.com (DR 1.3) · suncosc.com (DR 5) | 165 reviews | pressurewashinghiltonheadisland.com |
| 29 | pressure washing | Palm Beach Gardens, FL | 50k | 90 | $25.81 | Angi · southflcleaningexperts.com (DR 0) · sunshinepressurewashing.com (DR 11) | 297 reviews | palmbeachgardenspressurewashingpros.com |
| 30 | dryer vent cleaning | Bradenton, FL | 51k | 110 | $19.40 | Yelp · dryerventcleaningofbradenton.com (DR 0.4) · ten8dryerventcleaning.com (DR 0.2) | 759 reviews | bradentondryerventcleaningpros.com |
| 31 | septic tank pumping | Asheville, NC | 87k | 70 | $30.08 | ableseptictankservice.com (DR 1) · Yelp · mountainwellandseptic.com (DR 1.8) | none | ashevillesepticpumping.com |
| 32 | window tinting | Boca Raton, FL | 89k | 210 | $9.68 | bocatintandaudio.com (DR 3) · Reddit · thetintteam.com (DR 2.6) | 464 reviews | bocaratonwindowtintingpros.com |
| 33 | chimney sweep | Bristol, CT | 60k | 70 | $27.78 | chimneysweepbristolct.com (DR 0) · gmthomeservices.com (DR 6) · Bbb | 105 reviews | bristolchimneysweeppros.com |
| 34 | chimney sweep | Manassas, VA | 41k | 90 | $20.45 | chimchimchureemasonry.com (DR 1.6) · helpmychimney.com (DR 0.7) · Yelp | 785 reviews | manassaschimneysweep.com |
| 35 | pressure washing | Sanford, FL | 56k | 110 | $15.92 | hobbieprofessionalservices.com (DR 0) · jimmysbincleaning.com (DR 0) · Nextdoor | 341 reviews | sanfordpressurewashingpros.com |
| 36 | epoxy garage floor | Sarasota, FL | 53k | 140 | $12.20 | Angi · garagefloorepoxy.org (DR 9) · rhinoepoxycoating.com (DR 0.7) | 126 reviews | sarasotaepoxygaragefloorpros.com |
| 37 | pressure washing | Boynton Beach, FL | 71k | 170 | $9.57 | Thumbtack · aceshighpressurecleaning.com (DR 0) · ivanspressurecleaning.com (DR 2.9) | 869 reviews | boyntonbeachpressurewashingpros.com |

## Things worth knowing

- **Other rank-and-renters are already in 11 of these 37 markets.** Their sites look like
  ours (for example airductcleaningapex.com holding #2 and #3 in Apex), at DR 0. Kyle's answer
  is the same either way: do 10% better.
- **The map listings are weak or missing in 7 of the 37.** In Pensacola, Bentonville
  and Wellington dumpster rental, the top map listing has 1–2 reviews, the mark of other
  operators' new listings. Where the map listings have hundreds of reviews (Apex, Littleton),
  they will take most of the clicks above the organic results.
- **The pages to beat are short.** The weak top-3 pages run from about 130 words (Boca Raton
  tinting) to about 3,000, with a handful of pictures. Our 9-page build already clears that.
- Searches a month and cost per click are from the 29 Aug pull. Page one, authority and pages
  are from 25 Oct.
- The second-wave 65 are in `kyle-verdicts.csv` with the same columns.

## The first 10 (picked 25 Oct, waiting for Dan's go)

Picked from the 37 by average rank on three things, equal weight: how easy the top 3 is,
how weak the map listings are, and lead value. Markets whose map listings are in the
strongest third of the 37 were left out (Apex, Littleton, Hesperia), because those
listings take the clicks above the organic results. All 10 domains rechecked free on 25 Oct.

| # | Market | Searches/mo | $/click | Top 3 now | Map listings | Domain |
|---|---|---:|---:|---|---|---|
| 1 | Dumpster rental, Bentonville AR | 480 | $11.81 | Angi · DR 0 · DR 0.3 | top listing has 2 reviews | bentonvilledumpsterrentalpros.com |
| 2 | Dryer vent cleaning, Ocala FL | 140 | $37.80 | Thumbtack · DR 2 · DR 2 | none | dryerventcleaningocala.com |
| 3 | Air duct cleaning, Marietta GA | 210 | $29.69 | Yelp · DR 0 · DR 0 | 230 reviews | mariettaairductcleaningpros.com |
| 4 | Window tinting, Bradenton FL | 480 | $11.75 | DR 0 · Yelp · DR 0 | 210 reviews | windowtintingbradenton.com |
| 5 | Dumpster rental, Wellington FL | 170 | $28.41 | DR 5 · DR 7 · DR 25 | top listing has 1 review | wellingtondumpsterrentalpros.com |
| 6 | Dumpster rental, Biloxi MS | 390 | $11.67 | DR 0.2 · DR 0 · Yelp | 176 reviews | biloxidumpsterrentalpros.com |
| 7 | Air duct cleaning, Schaumburg IL | 260 | $32.10 | DR 0.7 · DR 0 · Yelp | 422 reviews | schaumburgairductcleaningpros.com |
| 8 | Septic pumping, North Miami FL | 260 | $215.13 | DR 0.8 · Yelp · DR 13 | 187 reviews | northmiamiseptictankpumpingpros.com |
| 9 | Air duct cleaning, Wheaton IL | 70 | $71.93 | DR 7 · BBB · DR 3 | none | wheatonairductcleaningpros.com |
| 10 | Dumpster rental, Pensacola FL | 880 | $9.27 | WM · DR 0 · DR 0.2 | top listing has 2 reviews | pensacoladumpsterrentalpros.com |

Cost: 10 .com names at Cloudflare's at-cost price, ~$10.46 a year each = ~$105 for the year
(DOMAINS.md). Verisign raises the .com wholesale price on 1 Nov 2026, so names bought by
31 Oct bill at today's price for the first year. Building them also needs a tracking number
each (Telnyx, about $0.79 up front + $0.79 a month), and hosting is the existing Cloudflare
Pages project at no extra cost.

### Registered 25 Oct 2026 (Dan's go)

All 10 registered at Cloudflare Registrar through the Registrar API at $10.46 each,
**$104.60 total**. The live domain-check was run first, and every name was confirmed active in
the account listing afterwards. All expire 2027-10-25. **Auto-renew is off** (the API
default); turn it on before October 2027 or they lapse. The account now holds 99 of
Cloudflare's 100-domain cap, so any further batch needs a second Cloudflare account. Log:
`kyle-screen/oct-top3/registrations_2026-10-25.json`. Snapshot: `data/registrar-snapshot.json`.

### Built and live 25 Oct 2026

All 10 are live over HTTPS: phase 2, 9 pages each (home, 4 service pages, services, pricing,
about, contact), written by five parallel writers from sourced local facts, and passing the
house build check against all 97 sites. Each carries its own fresh Telnyx number, and calls go
to the call-desk voicemail. **Photos went live the same evening** on Dan's go: 40 stills (a
city hero plus one shot each for the first three services) from ElevenLabs gpt-image-2.5-sunburst,
8,462 credits (about $1.40). Prompts are in `kyle-screen/oct-top3/photo_prompts.json` and the
flow and generation ids in `photo_nodes.json`. Every one was checked for text, logos and faces
before it went up. Pensacola is on Pages project
`local-sites-2` (see HOSTING.md). Not yet done: Search Console properties and sitemaps,
copycat links, and directory citations.
