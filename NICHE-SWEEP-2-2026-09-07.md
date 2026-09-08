# Niche sweep 2 — beyond towing (2026-09-07)

Question Dan asked: does it have to be towing / Kyle's list, or is anything else winnable?

Method: DataForSEO keyword_overview (volume + avg referring domains of ranking pages) across
12 base cities, then the 57-city 100–300k list for the two services that popped; Ahrefs
keywords-explorer-overview for KD, volume and SERP features; then live SERP pulls and
DataForSEO bulk_referring_domains on the sites actually ranking. Gate: volume ≥140 (DFS) and
ranking-page refdoms ≤15 on DFS, then confirm with Ahrefs KD ≤15, then eyeball the SERP.

Lesson carried from Pueblo: DFS avg_backlinks_info is stale/optimistic. The number that
matters is the refdom count of the actual sites on page one.

## What passed and what did not

| Service | Cities checked | Pass DFS gate | Verdict |
|---|---|---|---|
| Mobile mechanic | 59 | 38 | **Best Kyle-style niche found.** SERPs are Facebook groups, Reddit, Wix, Craigslist, one-page sites. Ahrefs KD 0–13 in 20+ cities. |
| Dumpster rental | 61 | 37 | Big volume (Richmond 880/800, Chattanooga 1300/700) and Ahrefs KD 0–9, but organic is crowded with nationals (WM, Republic, Budget Dumpster, Junk King, redbox+). Exact-match local sites do rank (cedarrapidsdumpsterrentals.com #7 with 33 refdoms, brownsvilledumpsterrentals.com holds the pack with 8). |
| Junk removal | 12 | 10 | Fort Wayne 300/KD5 ($6 CPC), Cedar Rapids 200/KD0, Asheville 200/KD8 ($7 CPC). Ranking sites 37–71 refdoms. 1-800-GOT-JUNK and College Hunks own the pack. |
| Appliance repair | 12 | 11 | Kalamazoo 200/KD4, Evansville 150/KD5. Mr. Appliance franchise holds the pack; organic is tiny sites + Facebook. Lower ticket than the others. |
| Handyman | 12 | 10 | Spokane 250/KD0 — but WA requires a contractor registration for handyman work; licensing exposure. Park it. |
| Tree removal | 12 | 2 | Ahrefs KD 16–50. No. |
| Gutter cleaning | 12 | 5 | Volume 110 median. Thin. |
| Mobile detailing | 12 | 4 | Refdoms 9–13, volume decent (Richmond 1300). Non-emergency, price-shopped. Maybe later. |
| Basement waterproofing, chimney, emergency electrician, snow plowing, well pump, wildlife, sprinkler, septic, junk car, mobile tire, pressure washing | 12 each | 0–1 | No. |

## Mobile mechanic — the ranking-site link bar (what it actually takes)

| City | DFS vol | Ahrefs vol / KD | Pack? | Organic page-one sites and their refdoms |
|---|---|---|---|---|
| Savannah GA | 320 | 150 / 2 | yes | aztecsmobilemechanic 15, mobilemechanicssavannahga 29, whittons 47, a Wix site, a Facebook page |
| Wilmington NC | 260 | 100 / 0 | yes | wilmingtonmobileautomotiverepair 14, prestononwheels 7, mobiletechilm 62, Facebook group #1 |
| Des Moines IA | 170 | 150 / 13 | yes | desmoinesmobilemechanics 21 (#1), mosautoshop 52, Facebook page #2 |
| Columbus GA | 320 | 200 / 0 | yes | columbusmobilemechanics 48, Yelp #1, Reddit, Facebook, wrench.com |
| Rochester NY | 210 | 100 / 0 | yes | Facebook page #1, mobileautorepairrochester 64, a Square site, Craigslist |
| Reno NV | 480 | 150 / 0 | yes | renonvmobilemechanic 164 (94 main), carrepairreno 41, renosmobilemechanic 40 |
| Tallahassee FL | 480 | 200 / 0 | yes | Facebook page #1, tallysmobilemechanic 22, tallahasseemobilemechanic 56, tallahasseeflmobilemechanic 70 |
| Asheville NC | 390 | 50 / 0 | **no pack** (knowledge panel only) | ashevillemobilemechanic 57 (#1), Facebook, Reddit, codys 21, a Google Sites page |
| Spokane WA | 390 | 150 / 44 | yes | spokanemobilemechanics 61, unitedmobilemechanic 13, syphers 19, megs 49 |
| Columbia SC | 590 | 250 / 40 | yes | columbiamobilemechanic 51, mobilemechaniccolumbiasc 54, onsitemobiletech 35 |

Read: 7–30 referring domains puts a real 25-page site on page one in Savannah, Wilmington,
Des Moines, and probably Rochester and Tallahassee (where a Facebook page is #1 organic).
That is the same bar as towing in Kalamazoo/Evansville, with 2–3× the volume and a more
open SERP (no national chains except wrench.com / Instant Car Fix, which sit at #9–12).

Why the tenant will pay: a mobile mechanic has no shop, no address to run ads from, and
lives off Facebook groups. A ranked site that rings is the whole business. Ahrefs CPC
$1.20–$1.80; DFS $3–$7.

## Dumpster rental — worth one test, not a program

Richmond VA (880 DFS / 800 Ahrefs, KD 8, CPC $8) and Toledo (1,000 / 300, KD 1) are the
two where a local exact-match site could take #2–#4 under WM. Ranking local sites carry
40–75 refdoms, so the bar is higher than mobile mechanic. Brownsville TX (320 / 400, KD 0)
is the softest: the pack leader has 8 refdoms, organic #3 is a .click domain with 28.

## Recommendation

1. Keep the two towing tests (Kalamazoo, Evansville) — they are already researched.
2. Add two mobile-mechanic tests: **Savannah GA** and **Wilmington NC** (lowest link bar,
   volume 100–320, pack present but organic is Facebook + sub-30-refdom sites).
   Domains available: savannahmobilemechanicpros.com, desmoinesmobilemechanicpros.com,
   rochestermobilemechanicpros.com, tallahasseemobilemechanicpros.com,
   ashevillemobilemechanicpros.com, columbusgamobilemechanic.com.
   Taken: wilmingtonmobilemechanicpros.com (use wilmingtonmobilemechanicexperts.com or
   ilmmobilemechanic.com — not yet checked).
3. One dumpster test only if the first four rank: Brownsville TX
   (brownsvilledumpsterpros.com available) or Richmond VA (richmonddumpsterrentalpros.com available).
4. Do not touch handyman (licensing), tree removal (KD), or anything informational.

Data files: scratchpad niche-sweep/services_wide.json (259 keywords), towing60_merged.json.
