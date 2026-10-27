# Which trades and towns to build next (26 Oct 2026)

Dan's rule: only build where a job is $300+ and a lead is worth $50–90 or more to the owner.
This screen applies that rule with real numbers, then keeps only towns where Google page one is weak.

## How a lead's value was measured

The price an owner pays Google per ad click, in that town (Google Ads data via DataForSEO).
A phone call usually takes about 6–10 ad clicks, so **a call costs the owner roughly 6–10x the click price.**
That is the number our rent has to beat.

## What each trade is worth (middle click price across 707 towns of 37k–100k people)

| Trade | Click price | Call costs the owner about | Passes $50+? |
|---|---|---|---|
| Emergency plumber | $89 | $500+ | Yes |
| Drain cleaning | $46 | $280–460 | Yes |
| Garage door repair | $41 | $250–410 | Yes |
| Foundation repair | $40 | $240–400 | Yes |
| AC repair | $38 | $230–380 | Yes |
| Water damage restoration | $38 | $230–380 | Yes |
| Window replacement | $37 | $220–370 | Yes |
| Roof repair | $36 | $210–360 | Yes |
| Plumber | $32 | $190–320 | Yes |
| Septic pumping | $24 | $145–245 | Yes |
| Pest control | $23 | $135–225 | Yes |
| Mold removal | $22 | $130–220 | Yes |
| **Air duct cleaning** (3 of our sites) | $22 | $130–215 | Yes |
| **Dryer vent cleaning** (Ocala) | $21 | $125–210 | Yes |
| Electrician | $16 | $95–155 | Yes |
| Junk removal | $15 | $90–150 | Yes |
| Tree removal | $14 | $85–140 | Yes |
| **Dumpster rental** (4 of our sites) | $7.50 | $45–75 | Borderline |
| Towing | $6 | $35–60 | Borderline |
| **Window tinting** (Bradenton) | $4 | $25–40 | **No** |
| Mobile mechanic, dent repair | $4 | $25–40 | No |

Correction to what I told Dan earlier today: duct cleaning and dryer vent pay far more per lead than I guessed
(owners bid $21–22 a click; the cheap-coupon jobs upsell). Dumpsters are the borderline ones, and tint fails.
Full table for 64 trades: `kyle-screen/trades2/` (grid2.json + grid-scored.json).

## Where we can win

Screened: 23 high-value trades x 707 towns -> 2,978 town/trade pairs with 50+ searches and a $15+ click.
For each, Google page one located in that town. A top-3 spot counts as **weak** when it is a small local site
(not Yelp/Angi/Thumbtack, not a national brand) with under 1,000 Google visits a month **and** Ahrefs DR 15 or under.
Towns sharing a name with another top-1000 US city were dropped (their data mixes in the other city).

- 548 pairs had 2 of the top 3 weak by traffic; 393 after dropping same-name towns.
- The top 80 by ad dollars got an Ahrefs DR check: **65 pass** with 2 of the top 3 at DR 15 or under.

By trade, the clean weak markets were: garage door repair 84, plumber 63, pest control 51, electrician 46,
AC repair 38, roof repair 20, air duct cleaning 19, mold removal 14, window replacement 11, foundation repair 10,
tree removal 10, emergency plumber 7.

### The 65 (ranked by searches x click price)

Map-pack reviews = most reviews held by any business in the Google Maps box (how hard Maps is; organic is what we rank in).

| # | Trade | Town | People | Searches/mo | Map-pack reviews | Weak top-3 sites (Ahrefs DR) |
|---|---|---|---|---|---|---|
| 1 | plumber | Fort Myers, FL | 68,190 | 1600 | 859 | theplumbersplumber.com DR7.0, dolphinplumbingdrain.com DR9.0 |
| 2 | plumber | Sugar Land, TX | 83,860 | 1300 | 1700 | texasplmbgroup.com DR0.4, plumbingofsugarland.com DR0.1 |
| 3 | plumber | Kenosha, WI | 99,889 | 1300 | 475 | craneplumbingservices.com DR1.4, christheplumberwi.com DR0.6 |
| 4 | plumber | New Braunfels, TX | 63,279 | 1300 | 251 | connallyplumbing.com DR1.9, plungerprostx.com DR2.5 |
| 5 | garage door repair | Eden Prairie, MN | 62,603 | 880 | 538 | edenprairiegarageedoorsrepair.com DR0.0, garage-door-repair-edenprairie-mn.com DR0.0 |
| 6 | plumber | Bend, OR | 81,236 | 1000 | 3700 | pearlplumbingbend.com DR0.9, bestplumbersinbend.com DR1.0 |
| 7 | garage door repair | Annapolis, MD | 38,722 | 720 | 1200 | annapolisgaragedoorsinc.com DR1.1, garagedoorannapolis.com DR11.0 |
| 8 | plumber | Castle Rock, CO | 53,063 | 880 | 514 | tpscolorado.com DR0.6, castlerockplumbers.co DR0.0 |
| 9 | plumber | Bellingham, WA | 82,631 | 880 | 899 | lyndensheetmetal.com DR14.0, bpheating.com DR0.0 |
| 10 | plumber | Gulfport, MS | 71,012 | 880 | 223 | plumbinggulfportms.com DR3.6, southernsewerservices.com DR0.0 |
| 11 | plumber | Livonia, MI | 95,208 | 720 | 99 | livoniaplumbers.com DR0.2, allstardraincleaningmi.com DR0.0 |
| 12 | plumber | Lawton, OK | 97,151 | 720 | 2300 | solidplumbing.com DR11.0, plumbinglawton.com DR4.1 |
| 13 | pest control | Santa Barbara, CA | 90,412 | 880 | 91 | santabarbarapestcontrol.com DR0.9, jhonnyspestcontrol.com DR1.0 |
| 14 | garage door repair | Franklin, TN | 68,886 | 480 | 145 | watkinsgaragedoorservice.com DR0.2, garagedoorrepair-franklintn.com DR0.0 |
| 15 | plumber | Galveston, TX | 48,733 | 590 | 567 | listerplumbinginc.com DR0.1, doddsplumbingservice.com DR0.0 |
| 16 | plumber | Enid, OK | 50,725 | 590 | 328 | prestigeplumbingok.com DR0.0, dieterleplumbing.com DR0.1 |
| 17 | garage door repair | Palatine, IL | 69,350 | 390 | 141 | garagedoorrepairpalatine.com DR1.1, doorservicespalatine.com DR0.0 |
| 18 | air duct cleaning | Apex, NC | 42,214 | 720 | 3200 | airductcleaningapex.com DR0.0, airductcleaningapex.com DR0.0 |
| 19 | plumber | Watsonville, CA | 52,477 | 480 | 183 | watsonvilleplumbingco.com DR0.0, saplumbinginc.com DR0.0 |
| 20 | plumber | Wheeling, IL | 38,015 | 480 | 1100 | 24-7plumbing4u.com DR0.8, localtrustedplumber.com DR0.0 |
| 21 | plumber | Battle Creek, MI | 51,848 | 480 | 1000 | wilbursplumbing.com DR0.0, crooksplumbing.com DR9.0 |
| 22 | ac repair | Lake Elsinore, CA | 57,525 | 390 | 661 | rkmair.com DR11.0, airconditioningrepairlakeelsinoreca.com DR0.1 |
| 23 | garage door repair | League City, TX | 90,983 | 320 | 446 | garagedoorfamily.com DR2.0, garagedoorsrepair-thewoodlands.com DR0.1 |
| 24 | plumber | Lake Forest, CA | 79,312 | 390 | 3400 | largeplumbing.com DR1.5, ocplumbingandrestoration.com DR0.2 |
| 25 | plumber | Johns Creek, GA | 82,788 | 390 | 16 | johnscreek-plumbing.com DR0.7, johnscreekplumbingco.com DR0.0 |
| 26 | plumber | Port Orange, FL | 57,203 | 390 | 336 | integrityplumbingandmore.com DR2.0, billshaferplumbing.com DR1.5 |
| 27 | plumber | Wheaton, IL | 53,648 | 390 | 923 | keeleysplumbing.com DR12.0, toptierplumbers.com DR0.8 |
| 28 | plumber | Novato, CA | 54,194 | 390 | 2000 | baswellplumbing.com DR7.0, theplumbingpros.net DR0.0 |
| 29 | plumber | Lodi, CA | 63,338 | 390 | 225 | philpaulplumbing.com DR9.0, rooterproplumbing.com DR6.0 |
| 30 | plumber | Newton, MA | 87,971 | 390 | 679 | sdhplumbingandheating.com DR10.0, pannhomeservices.com DR12.0 |
| 31 | ac repair | Avondale, AZ | 78,822 | 320 | 1600 | fixitfrankie.com DR5.0, aztrademasters.com DR1.4 |
| 32 | ac repair | Lake Havasu City, AZ | 52,844 | 320 | 569 | theweathermanac.com DR0.3, affordableaclhc.com DR0.6 |
| 33 | pest control | Taylor, MI | 61,817 | 480 | 945 | taylorpestcontrolco.com DR0.0, taylorpestcontrolco.com DR0.0 |
| 34 | garage door repair | Delray Beach, FL | 64,072 | 260 | 1100 | summitgaragedoor.com DR2.5, garagedoorrepair-delraybeach.com DR0.0 |
| 35 | garage door repair | Canton, OH | 72,535 | 260 | - | timkengaragedoors.com DR0.0, atlantaentrysystems.com DR1.2 |
| 36 | foundation repair | New Braunfels, TX | 63,279 | 260 | 71 | newbraunfelsfoundationrepairexperts.com DR10.0, newbraunfelsfoundationrepairexperts.com DR10.0 |
| 37 | plumber | Mission Viejo, CA | 96,346 | 320 | 137 | ocplumbingandrestoration.com DR0.2, thedoneriteplumber.com DR6.0 |
| 38 | plumber | Fort Pierce, FL | 43,074 | 320 | 350 | fitzpatrickplumbingfl.com DR0.0, reelplumbing.com DR8.0 |
| 39 | plumber | Upland, CA | 75,413 | 320 | 1800 | plumberuplandca.com DR0.3, highspeedplumbing.com DR13.0 |
| 40 | plumber | Glenview, IL | 45,417 | 320 | 882 | glenviewplumbingco.com DR0.0, plumberarlingtonheights.com DR9.0 |
| 41 | pest control | Yakima, WA | 93,257 | 390 | 3600 | jerryspestservice.com DR11.0, valleypest.net DR0.0 |
| 42 | garage door repair | Bedford, TX | 48,592 | 210 | 422 | garagedoorrepair-bedford.com DR0.0, trustygaragerepair.com DR11.0 |
| 43 | garage door repair | Farmington, NM | 45,426 | 210 | 388 | overheaddoorfourcorners.com DR9.0, devilbissgaragedoors.com DR0.4 |
| 44 | garage door repair | Mission Viejo, CA | 96,346 | 210 | 1100 | wolfgaragedoorservices.com DR0.0, 3rrrgaragedoors.com DR0.1 |
| 45 | garage door repair | Redondo Beach, CA | 67,815 | 210 | 33 | doorrepairredondobeach.com DR0.0, la-garagedoor.com DR0.1 |
| 46 | plumber | Caldwell, ID | 48,957 | 260 | 1700 | acecaldwellemergencyplumber.com DR0.0, safeguardplumbingcompany.com DR0.0 |
| 47 | plumber | Bonita Springs, FL | 47,547 | 260 | 1300 | paulsteinplumbing.com DR0.2, nobelplumbing.com DR0.0 |
| 48 | plumber | Citrus Heights, CA | 85,285 | 260 | 535 | boydplumb.com DR3.5, dependablerooter.com DR8.0 |
| 49 | plumber | Montclair, CA | 38,027 | 260 | 1800 | luckyduckplumbing.com DR4.8, a2z-plumbing.com DR0.5, renownedplumbers.com DR2.2 |
| 50 | plumber | Davis, CA | 66,205 | 260 | 53 | reliablerooterpro.com DR1.3, americanplumbingt.com DR0.2 |
| 51 | plumber | DeSoto, TX | 51,483 | 260 | 1100 | republic-ac.com DR7.0, republic-ac.com DR7.0 |
| 52 | plumber | Beavercreek, OH | 45,712 | 260 | 1800 | premierplumbingservicesohio.com DR9.0, watkem.com DR12.0 |
| 53 | ac repair | Grapevine, TX | 50,195 | 210 | 2500 | coldfactor.com DR12.0, greentechdfw.com DR1.4 |
| 54 | ac repair | Jupiter, FL | 58,298 | 210 | 2100 | reynoldsac.com DR0.5, ebens.com DR9.0 |
| 55 | emergency plumber | Weston, FL | 68,388 | 90 | 77 | westonplumbingco.com DR0.0, westonemergencyplumbingsfl.com DR0.0 |
| 56 | roof repair | Oak Lawn, IL | 57,073 | 210 | 77 | arcroofs.com DR0.0, vulcanconstruction.com DR3.9 |
| 57 | electrician | York, PA | 43,935 | 480 | 149 | markleelectric.com DR4.8, lefeverelectric.com DR8.0 |
| 58 | electrician | Santa Cruz, CA | 62,864 | 480 | 161 | allegrielectric.com DR2.7, johnhopeelectric.com DR3.1 |
| 59 | pest control | York, PA | 43,935 | 320 | 3600 | yorkexterminating.com DR0.2, kirchnerspest.com DR10.0 |
| 60 | pest control | Wilson, NC | 49,628 | 320 | 2100 | mosquitoxperts.com DR2.0, thepestdr.com DR0.0 |
| 61 | garage door repair | Tinley Park, IL | 57,282 | 170 | 302 | gcgaragedoors.com DR2.2, firstamericangaragedoors.com DR1.2 |
| 62 | garage door repair | Camarillo, CA | 66,086 | 170 | 1200 | thegaragedoordoc.com DR0.9, unitedgaragedoorrepair.org DR0.0 |
| 63 | garage door repair | Oak Park, IL | 52,066 | 170 | 834 | garagedoorrepair-oak-park.com DR0.1, garagedoorinstallandrepair.com DR0.0 |
| 64 | garage door repair | Oak Lawn, IL | 57,073 | 170 | 107 | smithgaragedoorsolutions.com DR0.3, a1oaklawngaragedoor.com DR0.0 |
| 65 | garage door repair | Rock Hill, SC | 69,103 | 170 | 549 | rockhillgaragedoorrepair.org DR0.0, dev.24hrgaragedoorservice.com DR2.9 |

## What this means, plainly

**What we know**
- Plumbing is the standout: the most searches, $190–320 a call to the owner, and 40+ small towns where the top 3
  organic spots are held by tiny sites (DR 0–12). Every town has many plumbers, so there are many possible renters.
- Garage door repair pays even more per call, but page one is full of other rank-and-renters' keyword domains,
  and the trade is known for fake Google Maps listings. Winnable, more of a fight to keep.
- Pest control, AC repair and roof repair are solid second tier.
- Of our current 10: the 3 duct sites and Ocala dryer vent are fine on lead value; the 4 dumpster sites are borderline
  ($45–75 a call); Bradenton tint is below the line.

**If it were my business**
1. Next batch = **plumbers in the top 10–15 towns above** (Fort Myers, Sugar Land, Kenosha, New Braunfels,
   Castle Rock, Gulfport, Livonia, Galveston, Enid, Watsonville, Port Orange, Johns Creek...).
   Avoid towns where Maps leaders have 2,000+ reviews if there is a choice (Bend, Lawton, Lake Forest).
2. Add garage door repair in 3–5 towns as a test (Eden Prairie, Franklin TN, Palatine).
3. Keep the 10 live sites; sell the duct, septic and dumpster ones first; stop adding pages to Bradenton tint.
4. Every new build still needs your yes: about $10.50 a domain, and the Cloudflare account is at 99/100 domains,
   so a second account is needed first.

Research cost: about $7 of DataForSEO and 310 Ahrefs units. Nothing bought, nobody contacted.
