# Kyle's copycat links for Kyle batch 1 (25 Oct 2026)

Kyle's most-used link method: look up the backlinks of the sites already ranking and copy the free ones. For each of the 10 batch 1 sites this pulls the backlinks of the top 3 business sites on page one for its main search (directories like Yelp and Angi skipped as "competitors"), from Ahrefs, one link per linking site, live links only, Ahrefs' own spam flag filtered out.

- Data: `kyle-screen/oct-top3/copycat_raw/` (30 pulls), every link sorted in `kyle-screen/oct-top3/copycat_links.csv`. Scripts: `kyle-screen/copycat_sort.py`, `copycat_report.py`.
- Cost: 7,294 Ahrefs units out of the 200,000 a month; 21,464 are left until it resets on 5 Nov. Nothing was signed up for.
- Five competitors returned exactly 100 links, Ahrefs' cap for this call. Links come sorted strongest first, so only the weakest tail of those five is missing.

## What the 30 competitors' links actually are

| Site | Free listings | Trade directories | Paid (chambers, PR, guest posts) | Auto-made pages | Spam or hacked | Editorial |
|---|---:|---:|---:|---:|---:|---:|
| bentonvilledumpsterrentalpros.com | 17 | 0 | 0 | 20 | 114 | 5 |
| dryerventcleaningocala.com | 12 | 8 | 0 | 31 | 28 | 1 |
| mariettaairductcleaningpros.com | 13 | 22 | 0 | 25 | 23 | 3 |
| windowtintingbradenton.com | 15 | 12 | 0 | 23 | 24 | 0 |
| wellingtondumpsterrentalpros.com | 57 | 3 | 16 | 18 | 18 | 6 |
| biloxidumpsterrentalpros.com | 23 | 4 | 17 | 33 | 45 | 6 |
| schaumburgairductcleaningpros.com | 18 | 13 | 3 | 33 | 34 | 3 |
| northmiamiseptictankpumpingpros.com | 21 | 38 | 29 | 36 | 43 | 6 |
| wheatonairductcleaningpros.com | 56 | 19 | 49 | 42 | 44 | 6 |
| pensacoladumpsterrentalpros.com | 38 | 17 | 31 | 48 | 35 | 7 |

The plain reading: these competitors have almost no real links. What they do have is a stack of directory listings, and that stack is what we copy. **No blog-comment links turned up for any of the 30**, so the "blog comments" half of Kyle's copycat method has nothing to copy in these markets.

"Auto-made pages" are SEO-tool and data-broker pages (siteprice, sitelike, Crunchbase-style scrapers) that appear on their own once a site exists. "Spam or hacked" are link sellers and hacked WordPress pages. Both are left alone. The paid ones need money (chamber dues, press releases, sold guest posts) and are outside this list.

## Before anyone files: the address problem

Most of these directories ask for a street address, and several check it by phone, postcard or a matching Google listing. A rank-and-rent site has no office. Some accept a service-area business with the address hidden, some don't. Listing a made-up address breaks most directories' terms and is the same problem as a fake Business Profile. Whether to list with a real address (a client's, a virtual office), list only where the address can be hidden, or skip is Dan's call. The "free" label below means the listing costs nothing, not that it needs no address.

## Which directories we can file without a street address (checked 25 Oct)

All 46 directories in the core, duct and dumpster lists were checked by reading their public add-a-business,
claim, help and terms pages, without signing up or submitting anything. Four helpers used web fetch and search;
YellowPages, CitySquares, Best Pros in Town, BizListUSA and TechDirectory were then opened by hand. Raw notes,
with the page each answer came from: `kyle-screen/oct-top3/address_check_0.json` to `_3.json`.

**The short answer: 4 free directories take us with no street address, 6 more do for a small fee, 8 need a
street address, 15 can't be joined directly (10 of them copy Google Maps, so a Google Business Profile is the
only way on), and 13 couldn't be checked without signing up.**

### File now: free, no street address needed (4)

| Directory | List | How it works | Check before it goes live |
|---|---|---|---|
| nearspotusa.com | core (6 markets) | Free, no account. Only a ZIP is required; street address is optional. https://nearspotusa.com/add-business | Manual review; contact email used to confirm |
| hvacservicefast.com | duct | Free, no account. Address optional; you pick the cities you serve. https://hvacservicefast.com/register-as-pro?new=1 | Captcha (the person filing ticks it), then manual review |
| rentadumpster.co | dumpster | Free to list or claim. Matches customers by the ZIP codes you serve; sample listings show no street. https://rentadumpster.co/for-haulers/ | Goes live once they confirm the phone number |
| bizhwy.com | core (3) | Free basic listing. Live listings read "Serving, Athens AL" with no street, so a city-only listing works in practice. https://www.bizhwy.com/addlisting.php | Email link (from a 2013 guide; the live form only shows its first step) |

### No street address, but it costs money (6), needs your yes

| Directory | List | Price | How it works |
|---|---|---|---|
| contractorsup.com | core (4) | $19.95 once | They build the listing from our website, so it carries no street address |
| reputablebusinesses.com | core (3) | $19.95 once | Same company and setup as ContractorsUp |
| cleanerin.com | duct | $19.95 once | Built from the website; listings show city and ZIP only |
| reputablecleaners.com | duct | $19.95 once | Sister site of Cleanerin |
| mylocalservices.com | core (4) | $2 once | Form has an address step; whether it can be left blank is unclear. Many listings arrive through Yext |
| powerwashmaps.com | duct | not stated | Street address optional; manual review in 1 to 3 days. Mostly a pressure-washing directory |

Total if all six: about $82 once.

### Needs a street address (8)

- **bbb.org** (core, 7 markets): the get-listed form requires a street address, and BBB may phone to confirm the business is real. Some live profiles show only a city, so BBB hides addresses in some cases, but no policy was found.
- **bestprosintown.com** (core, 7): "Business Address *" is required (one free-text box; whether a city alone passes review is unknown).
- **procore.com** (core, 3): street address required, no P.O. box, and a manual check that the business is real.
- **myfavoritebuilder.com** (core, 3): $45 and asks for a street address.
- **allthehomeservices.online** (core, 3): asks for an address plus proof of ownership. UK-run.
- **ibegin.com** (core, 3): listings show full addresses, and a privacy site tells home-based owners to use a P.O. box there. Verifies with an automated phone call and code.
- **wastebits.com** (dumpster): address required, and it **no longer accepts dumpster rental or junk removal businesses at all**.
- **wasterecyclingworkersweek.org** (dumpster): paid featured listing only, address required.

### Can't be joined directly (15)

These build their listings from Google Business Profiles, Yelp or data vendors and have no add form, so the
only way onto them is a Google Business Profile, or (for YP) a sales call:

- **yellowpages.com** (core, all 10 markets): "Can't find your business" goes to a Thryv sales form ("Connect with a Business Advisor"); submitting it opts you into their marketing texts. Its free listings are otherwise fed by the big data aggregators.
- **birdeye.com**, **hvacservice.io**, **chimscout.com**: built from Google Business Profile data.
- **localac.net**, **localcleaning.net**, **localcleaner.net**: one network built from Google data; new businesses only through a contact form.
- **dumpstercomparison.com**, **needsdirt.com**, **findtrashremoval.com**, **dumpsterrentalguide.com**: built from Google; dumpsterrentalguide's "List your business" links are dead.
- **dumpster.co** (a lead-gen site that routes calls to its own number) and **curbwaste.com** (a hauler-software company's own list): no way in.
- Also not usable: **homeservicebase.com** is a paid data tool, not a directory; **licensedhvacnearme.com** only lists holders of a Florida A/C contractor license.

### Couldn't tell (13)

The form sits behind sign-up (which we didn't do) or the site blocks automated checks:
citysquares.com (free; third-party guides say an address is required), provenexpert.com, freelistingusa.com,
bizidex.com, qdexx.com, thebuildermarket.com, techdirectory.io (free plan shows a website link but no phone
number), bizlistusa.com and businesslistus.com (one site, behind an "I am human" check), localhomeservicepros.com,
whatsyourhours.com, prosonrecord.com and dumpsterlocate.com (blocked). Whoever files can see the form on
sign-up and skip any that insist on a street address.

### What this means

- The copycat list is much shorter without an address: 4 free directories, 6 cheap ones, and up to 13 that
  might work once someone signs up. Kyle's competitors got most of their listings because they have real
  addresses and Google Business Profiles that these sites copy.
- **A Google Business Profile is the only way onto 10 of the 46**, and it also feeds YellowPages and Birdeye. That's the
  same Maps question as before, and it needs a real address or a real operator.
- Several check by phone (rentadumpster.co, iBegin, YellowPages). Our numbers go to voicemail, so a code read
  out by an automated call would land in the voicemail recording, which we can play back from Telnyx.

## Core list: copy these for all 10 sites (25)

Each of these lists competitors in 3 or more of the 10 markets.

| # | Directory | What it is | Markets where competitors use it | Example competitor listing |
|---:|---|---|---:|---|
| 1 | yellowpages.com | YP free listing (one listing also shows on dexknows.com and dk.yp.com) | 10 | https://www.yellowpages.com/mobile-al/environmental-ecological-consultants |
| 2 | bbb.org | BBB business profile (free listing; accreditation is the paid part) | 7 | https://www.bbb.org/us/al/mobile/profile/waste-management/ecosouth-services-of-mobile-llc-0463-1000031704 |
| 3 | bestprosintown.com | Best Pros in Town (free claim) | 7 | https://www.bestprosintown.com/fl/pensacola/coastal-container-/ |
| 4 | birdeye.com | Birdeye review profile (free claim) | 6 | https://reviews.birdeye.com/sai-air-duct-169754944353794 |
| 5 | nearspotusa.com | NearSpotUSA listing | 6 | https://nearspotusa.com/business/emerald-coast-utilities-authority-pensacola |
| 6 | provenexpert.com | ProvenExpert free profile | 5 | https://www.provenexpert.com/en-us/ecosouth-services/ |
| 7 | freelistingusa.com | FreeListingUSA free listing | 5 | https://www.freelistingusa.com/listings/ecosouth-services |
| 8 | citysquares.com | CitySquares free listing | 5 | https://citysquares.com/b/sai-air-duct-24700009 |
| 9 | bizidex.com | free business listing | 4 | https://bizidex.com/en/ecosouth-services-waste-management-598137 |
| 10 | mylocalservices.com | MyLocalServices free listing | 4 | https://www.mylocalservices.com/Coastal+Container-Pensacola-Florida-24590331.html |
| 11 | bizlistusa.com | BizListUSA free listing | 4 | http://mobile.bizlistusa.com/business/5428958.htm |
| 12 | businesslistus.com | BusinessListUS free listing | 4 | http://mobilecounty.businesslistus.com/business/5428958.htm |
| 13 | localhomeservicepros.com | free business listing | 4 | http://www.localhomeservicepros.com/mobile-al-36693/home-improvement/ecosouth-services |
| 14 | contractorsup.com | ContractorsUp free listing | 4 | https://www.contractorsup.com/22954/done-just-right |
| 15 | procore.com | Procore contractor network profile (free) | 3 | https://network.procore.com/p/alpha-dumpsters-usa-llc-sarasota |
| 16 | ibegin.com | iBegin free listing | 3 | https://www.ibegin.com/directory/us/florida/pensacola/coastal-container-408-ditmar-street/ |
| 17 | bizhwy.com | free business listing | 3 | https://alabama.bizhwy.com/businesses.php?c=324 |
| 18 | techdirectory.io | TechDirectory free listing | 3 | https://www.techdirectory.io/united-states/glenview/home-services/sai-air-duct |
| 19 | whatsyourhours.com | free business listing | 3 | https://www.whatsyourhours.com/united-states/mobile/business-services/ecosouth-services |
| 20 | qdexx.com | Qdexx free listing | 3 | https://www.qdexx.com/US/AL/Mobile/Business%20Services/US-AL-Mobile-Business-Services-EcoSouth-Services-EcoSouth-Services/ |
| 21 | thebuildermarket.com | The Builder Market listing | 3 | https://thebuildermarket.com/us/il/roselle/cleaning-maid-services/ |
| 22 | myfavoritebuilder.com | contractor directory | 3 | https://www.myfavoritebuilder.com/water-damage-restoration/listing_1a47765b0ac515629a1216274c52d1a3.shtml |
| 23 | allthehomeservices.online | All the Home Services listing | 3 | https://allthehomeservices.online/directory/listings/sai-air-duct-glenview-60025-3597-us-f9e4000b/ |
| 24 | reputablebusinesses.com | free business listing | 3 | https://www.reputablebusinesses.com/3841/coastal-container |
| 25 | prosonrecord.com | free business listing | 3 | https://www.prosonrecord.com/pro/sai-air-duct-glenview-il |

## Trade lists

**Air duct and dryer vent** (Ocala, Marietta, Schaumburg, Wheaton), 11: hvacservice.io (HVAC directory (claim)), homeservicebase.com (home services directory), hvacservicefast.com (HVAC directory), localcleaning.net (cleaning directory), localac.net (HVAC directory), localcleaner.net (cleaning directory), cleanerin.com (cleaning directory), reputablecleaners.com (cleaning directory), powerwashmaps.com (cleaning, HVAC and home services directory), licensedhvacnearme.com (HVAC directory), chimscout.com (cleaning, HVAC and home services directory)

**Dumpster rental** (Bentonville, Wellington, Biloxi, Pensacola), 10: curbwaste.com (dumpster and waste directory), wastebits.com (dumpster and waste directory), wasterecyclingworkersweek.org (dumpster and waste directory), dumpster.co (dumpster and waste directory), findtrashremoval.com (dumpster and waste directory), dumpsterrentalguide.com (dumpster and waste directory), dumpstercomparison.com (dumpster and waste directory), needsdirt.com (dumpster and waste directory), rentadumpster.co (dumpster and waste directory), dumpsterlocate.com (dumpster and waste directory)

## Per site: extra free listings only that market's competitors have

"Free profiles and posts" are free accounts on blog and profile platforms (Weebly, Strikingly, Vocal, Crunchbase…). Kyle would count them as "activity". Google's spam policy names low-quality directory, bookmark and mass-made pages as link spam, so they're listed apart and are the last thing to do, if at all.

### bentonvilledumpsterrentalpros.com

Search: "dumpster rental bentonville". Competitors copied: dumpsterrentalcrewbentonville.com, martinsstucco.com, gravitydumpsterrentals.com.

Copy: the core list, the dumpster list, and these 6 directories:

- **askmap.net** (AskMap free listing, DR 73): http://www.askmap.net/location/7828362/united-states/gravity-dumpster-rental-bentonville
- **yellow411.org** (Yellow411 free profile, DR 20): https://www.yellow411.org/profile/12c24ac
- **repairhit.com** (RepairHit listing, DR 16): https://repairhit.com/biz/martins-plastering-stucco-corp
- **towncontractors.com** (TownContractors listing, DR 8): https://www.towncontractors.com/martins-plastering-stucco-fayetteville-72701-carpenters
- **mytowninc.net** (MyTownInc listing, DR 0): https://mytowninc.net/martins-plastering-stucco-corp/
- **diyorbuylocal.com** (DIYorBuyLocal listing, DR 0): https://diyorbuylocal.com/local-pros/siding-contractors/springdale-ar

Free profiles and posts (1): video-bookmark.com

### dryerventcleaningocala.com

Search: "dryer vent cleaning ocala". Competitors copied: airfreshexperts.com, budsairocala.com, ocaladrymaster.com.

Copy: the core list, the air duct list, and these 3 directories:

- **loc8nearme.com** (Loc8NearMe (free claim), DR 78): https://www.loc8nearme.com/florida/ocala/air-fresh-dryer-vent-and-duct-cleaning-inc/7683919/
- **ocalabusinessdirectory.com** (Ocala Business Directory listing, DR 8): https://ocalabusinessdirectory.com/business/air-fresh-dryer-vent-and-duct-cleaning-inc/
- **topsprinkler.com** (home services directory, DR 4): https://topsprinkler.com/florida/ocala/bud-s-heating-and-air-llc-ocala-fl

### mariettaairductcleaningpros.com

Search: "air duct cleaning marietta". Competitors copied: airductcleaningga.com, ductorcleanair.com, advantaclean.com.

Copy: the core list, the air duct list, and these 6 directories:

- **chamberofcommerce.com** (ChamberofCommerce.com free listing (not a real chamber), DR 84): https://www.chamberofcommerce.com/business-directory/georgia/marietta/water-damage-restoration-service/1334397049-advantaclean-of-marietta
- **2findlocal.com** (2FindLocal free listing, DR 76): https://www.2findlocal.com/b/12302064/advantaclean-of-marietta-marietta-ga
- **demandconvert.com** (DemandConvert directory listing, DR 29): https://demandconvert.com/directory/ga/marietta/restoration/biz/advantaclean-of-marietta/
- **vendorroster.com** (VendorRoster listing, DR 0.7): https://vendorroster.com/best/best-hvac-atlanta
- **americasbesthomeservices.com** (home services directory, DR 0): https://americasbesthomeservices.com/georgia/roswell/damage-restoration/
- **homerepair.expert** (home repair directory, DR 0): https://homerepair.expert/providers/4241b88a-1e88-4909-ab91-e8b747357792

Left out: 13 mold, water-damage or janitorial directories from competitors' other trades.

### windowtintingbradenton.com

Search: "window tinting bradenton". Competitors copied: tintworxfl.com, mjtint.com, dmwintint.com.

Copy: the core list, no trade list, and these 10 directories:

- **regionaldirectory.us** (Regional Directory listing, DR 46): https://home-improvement.regionaldirectory.us/florida.htm
- **tintfinder.com** (tint shop directory, DR 29): https://tintfinder.com/places/florida/bradenton/tint-worx-of-florida/
- **tintbrokers.com** (tint shop directory, DR 10): https://tintbrokers.com/tint-shops/fl/bradenton/tint-worx-of-florida/8876
- **tintingsource.com** (tint shop directory, DR 9): https://www.tintingsource.com/florida/bradenton/tint-worx-of-florida-bradenton
- **autorepairdirectories.com** (auto repair directory, DR 1): https://autorepairdirectories.com/florida/bradenton
- **autonetworkhub.com** (auto services directory, DR 0): https://autonetworkhub.com/businesses/tint-worx-of-florida/
- **tintlaws.net** (tint installer list, DR 0): https://tintlaws.net/car-window-tint-installers-in-bradenton-fl/
- **findwindowtint.com** (tint shop directory, DR 0): https://findwindowtint.com/fl/bradenton
- **carwrapshops.com** (wrap and tint directory, DR 0): https://carwrapshops.com/shop/tint-worx-of-florida-bradenton-fl
- **localverifiedpros.com** (Local Verified Pros listing, DR 0): https://localverifiedpros.com/pros/tint-worx-of-florida-bradenton-22i0

### wellingtondumpsterrentalpros.com

Search: "dumpster rental wellington". Competitors copied: wellingtondumpsterrental.com, langleydumpsters.com, precisiondisposal.us.

Copy: the core list, the dumpster list, and these 23 directories:

- **loc8nearme.com** (Loc8NearMe (free claim), DR 78): https://www.loc8nearme.com/florida/fort-myers/precision-disposal-and-dumpster-rental-of-swfl/10059562/
- **2findlocal.com** (2FindLocal free listing, DR 76): https://www.2findlocal.com/b/14955452/precision-disposal-middleborough-middleborough-ma
- **find-us-here.com** (free business listing, DR 76): https://www.find-us-here.com/businesses/Precision-Disposal-Dumpster-Rental-of-SWFL-Fort-Myers-Florida-USA/33752700/
- **askmap.net** (AskMap free listing, DR 73): http://www.askmap.net/location/7823564/united-states/precision-disposal-middleborough
- **viesearch.com** (free business listing, DR 72): https://viesearch.com/1vkrr/plan
- **trueen.com** (free business listing, DR 71): https://www.trueen.com/business/listing/precision-disposal/794721
- **yplocal.com** (free business listing, DR 69): https://www.yplocal.com/united-states/north-fort-myers/business-professional-services/precision-disposal-dumpster-rental-of-swfl
- **unitedstatesbd.com** (free business listing, DR 64): https://www.unitedstatesbd.com/pro/precisiondisposaldu/precision-disposal-dumpster-rental-naples-bonita-springs
- **fyple.com** (free business listing, DR 63): https://www.fyple.com/company/fort-myers-dumpsters-by-precision-disposal-ihkszao/
- **stylevore.com** (free business listing, DR 62): https://review.stylevore.com/precision-disposal-and-dumpster-rental-of-melbourne/
- **townplanner.com** (free business listing, DR 62): https://www.townplanner.com/directory/214732/
- **dealerbaba.com** (free business listing, DR 60): https://www.dealerbaba.com/suppliers/business-services/fort-lauderdale-dumpsters-by-precision-disposal.html
- **couponler.com** (free business listing, DR 59): https://support.couponler.com/business/pages/precision-disposal
- **agreatertown.com** (free business listing, DR 59): https://agreatertown.com/melbourne-fl/precision-disposal-dumpster-rental-melbourne-0001633053931
- **bizbangboom.com** (free business listing, DR 56): https://www.bizbangboom.com/sandwich-ma/business-services/cape-cod-dumpster-rental-by-precision-disposal
- **palscity.com** (free business listing, DR 54): https://www.palscity.com/precision11
- **letsknowit.com** (free business listing, DR 52): http://www.letsknowit.com/cape-cod-dumpster-rental
- **gravitysplash.com** (free business listing, DR 51): https://www.gravitysplash.com/b/precision-disposal-5/
- **golocalezservices.com** (free business listing, DR 50): http://www.golocalezservices.com/middleborough/home-garden/precision-disposal-middleborough
- **ringmybiz.com** (free business listing, DR 48): https://www.ringmybiz.com/business/fort-myers-dumpsters-by-precision-disposal
- **digitalbusinessdirectory.online** (free business listing, DR 45): http://www.digitalbusinessdirectory.online/united-states/north-fort-myers/precision-disposal-dumpster-rental-of-swfl
- **localtips.net** (free business listing, DR 43): https://www.localtips.net/place/cleaning/precision-disposal-and-dumpster-rental/6a5b336cbe9e49006fe1cab2
- **pegasusdirectory.com** (free business listing, DR 41): https://pegasusdirectory.com/listing/cape-cod-dumpsters-by-precision-disposal/

Free profiles and posts (16): about.me, mypixieset.com, yolasite.com, vocal.media, writeupcafe.com, video-bookmark.com, bresdel.com, expatriates.com, flokii.com, articleted.com, buzzbii.com, diowebhost.com, geebo.com, collcard.com, ka-blogs.com, dsiblogger.com

### biloxidumpsterrentalpros.com

Search: "dumpster rental biloxi". Competitors copied: gulfwidewaste.com, rubleinvestments.com, alphadumpsters.com.

Copy: the core list, the dumpster list, and these 7 directories:

- **manta.com** (Manta free listing, DR 86): https://www.manta.com/c/m1x4q8k/alpha-dumpsters
- **chamberofcommerce.com** (ChamberofCommerce.com free listing (not a real chamber), DR 84): https://www.chamberofcommerce.com/business-directory/florida/daytona-beach/garbage-dump-service/2034060251-alpha-dumpsters
- **trueen.com** (free business listing, DR 71): https://trueen.com/blog/rental/190/your-guide-to-a-clutterfree-commercial-renovation
- **uscity.net** (free business listing, DR 71): https://uscity.net/listing/alpha_dumpsters-11637522
- **jacksonvilledirect.info** (free business listing, DR 25): https://jacksonvilledirect.info/listings/alpha-dumpsters/
- **lakecharles.com** (free business listing, DR 21): https://lakecharles.com/business/alpha-dumpsters
- **pompano.guide** (free business listing, DR 9): https://pompano.guide/item/alpha-dumpsters/

Free profiles and posts (1): beamstart.com

### schaumburgairductcleaningpros.com

Search: "air duct cleaning schaumburg". Competitors copied: staronductcleaning.com, cleanairwerks.com, 180066ducts.com.

Copy: the core list, the air duct list, and these 2 directories:

- **gigopro.com** (free business listing, DR 31): https://gigopro.com/illinois/westchester/hvac/indoor-air-duct-cleaning-westchester/
- **fixhubs.net** (free business listing, DR 0): https://fixhubs.net/pro/staron-duct-cleaning

Free profiles and posts (1): company.site

### northmiamiseptictankpumpingpros.com

Search: "septic tank pumping north miami". Competitors copied: caraballoexpress.com, septictank.com, abetteraimseptic.com.

Copy: the core list, no trade list, and these 31 directories:

- **swivl.tech** (free business listing, DR 34): https://swivl.tech/pro/fl-a-better-aim-septic-inc
- **septicandwell.com** (septic, plumbing and drain directory, DR 30): https://septicandwell.com/listings/caraballo-express-pump-outs-corp
- **demandconvert.com** (DemandConvert directory listing, DR 29): https://demandconvert.com/directory/fl/hialeah/septic-system-service/biz/caraballo-express-pump-outs-corp-2/
- **greasetraplocator.com** (septic, plumbing and drain directory, DR 23): https://greasetraplocator.com/places/caraballo-express-septic-grease-trap-drainfield-services/
- **miamilocalservices.com** (septic, plumbing and drain directory, DR 8): https://miamilocalservices.com/business/caraballo-express-septic-tank-grease-trap-pump-outs-hydrojet-atu-drain-fields-storm-drains-septic-system-service-in-hialeah/
- **dashpages.io** (septic, plumbing and drain directory, DR 5): https://dashpages.io/florida/hialeah/plumbers/caraballo-express
- **plumbersden.com** (septic, plumbing and drain directory, DR 4.8): https://plumbersden.com/plumber-directory/US/hialeah-florida/
- **homesquad.us** (septic, plumbing and drain directory, DR 4): https://homesquad.us/plumbing-services/hialeah/caraballo-express-septic-grease-trap-drainfield-services/
- **locateplumbers.com** (septic, plumbing and drain directory, DR 3.3): https://www.locateplumbers.com/listing/caraballo-express-septic-plumbing/
- **findmysepticguy.com** (septic, plumbing and drain directory, DR 2): https://findmysepticguy.com/fl/miami-dade-county/
- **imovingtoflorida.com** (septic, plumbing and drain directory, DR 1.5): https://imovingtoflorida.com/business/all-star-pump-outs-septic-tanks-grease-traps-storm-drains-lift-stations-hialeah/
- **plumberdirectories.com** (septic, plumbing and drain directory, DR 1): https://plumberdirectories.com/florida/hialeah
- **searchaplumber.com** (septic, plumbing and drain directory, DR 0.7): https://searchaplumber.com/hydro-jetting/fl/north-miami-beach-fl
- **needseptic.com** (septic, plumbing and drain directory, DR 0.5): https://needseptic.com/services/septic-inspection/miami--fl
- **septic.fyi** (septic, plumbing and drain directory, DR 0.5): https://septic.fyi/florida/broward-county/pembroke-pines
- **clearmylanddirectory.com** (septic, plumbing and drain directory, DR 0.5): https://clearmylanddirectory.com/contractors/caraballo-express-septic-grease-trap-drainfield-services-hialeah
- **restaurantdisposal.com** (septic, plumbing and drain directory, DR 0.1): https://restaurantdisposal.com/grease-trap-cleaning/fl/miami-beach-fl
- **doineedaplumber.org** (septic, plumbing and drain directory, DR 0.1): https://www.doineedaplumber.org/directory/caraballo-express-septic-grease-trap-drainfield-services-hialeah
- **homerepair.expert** (home repair directory, DR 0): https://homerepair.expert/providers/fb0a35b3-de50-4c55-bd1d-a9e847b0e9ea
- **septictrust.com** (septic, plumbing and drain directory, DR 0): https://septictrust.com/listing/caraballo-express-miami/
- **fixurbix.com** (free business listing, DR 0): https://fixurbix.com/services/caraballo-express-hialeah
- **septicspot.com** (septic, plumbing and drain directory, DR 0): https://septicspot.com/provider/caraballo-express-septic-grease-trap-drainfield-services-miami-fl
- **plumberfinderusa.com** (septic, plumbing and drain directory, DR 0): https://www.plumberfinderusa.com/business/caraballo-express-septic-grease-trap-drainfield-services-hialeah/
- **whowhere.io** (WhoWhere contractor listing, DR 0): https://whowhere.io/contractors/caraballo-express-septic-grease-trap-drainfield-services-miami
- **findsepticpros.com** (septic, plumbing and drain directory, DR 0): https://findsepticpros.com/provider/caraballo-express
- **septicsystemservice.fyi** (septic, plumbing and drain directory, DR 0): https://septicsystemservice.fyi/pros/caraballo-express-septic-tank-grease-trap-pump-outs-5797/
- **inclusivebusinessalliance.org** (septic, plumbing and drain directory, DR 0): https://inclusivebusinessalliance.org/business/caraballo-express-septic-grease-pump-outs-trenchless-sewer-line-repair-pipe-lining/
- **flinspectors.net** (septic, plumbing and drain directory, DR 0): https://flinspectors.net/fl/miami/septic-tank-pumping/
- **earthworkscout.com** (septic, plumbing and drain directory, DR 0): https://earthworkscout.com/fl/hialeah/caraballo-express-septic-grease-trap-and-drainfield-services-hialeah/
- **septicalternative.com** (septic, plumbing and drain directory, DR 0): https://septicalternative.com/florida/hialeah/caraballo-express-septic-tank-grease-trap-pump-outs-hialeah-fl
- **findasepticservice.com** (septic, plumbing and drain directory, DR 0): https://findasepticservice.com/listing/aim-septic-service-cutler-bay/

Free profiles and posts (3): bsky.app, hashnode.dev, deer.social

Left out: 2 mold, water-damage or janitorial directories from competitors' other trades.

### wheatonairductcleaningpros.com

Search: "air duct cleaning wheaton". Competitors copied: djrcleaning.com, saiairductclean.com, airductcleaningwheaton.com.

Copy: the core list, the air duct list, and these 20 directories:

- **find-us-here.com** (free business listing, DR 76): https://www.find-us-here.com/businesses/Sai-Air-Duct-Cleaning-Glenview-Illinois-USA/33879110/
- **yplocal.com** (free business listing, DR 69): https://www.yplocal.com/united-states/glenview/home-garden/sai-air-duct
- **fyple.com** (free business listing, DR 63): https://www.fyple.com/company/sai-air-duct-cleaning-ibca1fy/
- **digitalbusinessdirectory.online** (free business listing, DR 45): http://www.digitalbusinessdirectory.online/united-states/glenview/sai-air-duct
- **usacleaningcompany.com** (free business listing, DR 27): https://www.usacleaningcompany.com/5904/djr-cleaning
- **yplocal.us** (free business listing, DR 20): https://yplocal.us/business/sai-air-duct/
- **renovationsup.com** (free business listing, DR 19): https://www.renovationsup.com/85688/djr-cleaning
- **re-building.com** (cleaning, HVAC and home services directory, DR 18): https://re-building.com/location/done-just-right-inc/
- **linkcenter.com** (free business listing, DR 12): https://www.linkcenter.com/business/cleaning/198.php
- **homeimprovementfirms.com** (free business listing, DR 12): https://www.homeimprovementfirms.com/8441/djr-cleaning
- **excellentcontractor.com** (free business listing, DR 9): https://www.excellentcontractor.com/41835/djr-cleaning
- **trustedhearth.com** (free business listing, DR 6): https://www.trustedhearth.com/illinois/glenview/sai-air-duct/
- **buildingdupage.com** (cleaning, HVAC and home services directory, DR 5): https://buildingdupage.com/company/done-just-right-inc
- **placeprofile.net** (cleaning, HVAC and home services directory, DR 2.2): https://placeprofile.net/v/done-just-right-inc-roselle-us
- **nationalhomeauthority.org** (cleaning, HVAC and home services directory, DR 1.5): https://nationalhomeauthority.org/done-just-right/
- **handsdown.pro** (free business listing, DR 1.2): https://development.handsdown.pro/professional/djr-cleaning
- **handsdown.ai** (free business listing, DR 0.9): https://www.handsdown.ai/professional/djr-cleaning
- **diyorbuylocal.com** (DIYorBuyLocal listing, DR 0): https://diyorbuylocal.com/local-pros/hvac-contractors/elgin-il
- **fixhubs.net** (free business listing, DR 0): https://fixhubs.net/pro/done-just-right
- **beeynet.com** (free business listing, DR 0): https://beeynet.com/business/done-just-right-inc/

Free profiles and posts (7): weebly.com, webflow.io, web.app, mystrikingly.com, webselfsite.net, buzzbii.com, boycat.co

Left out: 4 mold, water-damage or janitorial directories from competitors' other trades.

### pensacoladumpsterrentalpros.com

Search: "dumpster rental pensacola". Competitors copied: coastalcontainer.com, dumpsterwerks.com, ecosouthservices.com.

Copy: the core list, the dumpster list, and these 12 directories:

- **trustburn.com** (free business listing, DR 76): https://trustburn.com/about/coastalcontainer-com
- **townplanner.com** (free business listing, DR 62): https://www.townplanner.com/directory/266755/
- **ecohubmap.com** (free business listing, DR 62): https://www.ecohubmap.com/company/business/ecosouth-services/l0qr3v33
- **dealerbaba.com** (free business listing, DR 60): https://www.dealerbaba.com/suppliers/business-services/ecosouth-services.html
- **macraesbluebook.com** (free business listing, DR 59): https://www.macraesbluebook.com/search/company.cfm?company=649692
- **letsknowit.com** (free business listing, DR 52): https://www.letsknowit.com/ecosouth100982
- **gravitysplash.com** (free business listing, DR 51): https://www.gravitysplash.com/b/ecosouth-services/
- **businessesup.com** (free business listing, DR 31): https://www.businessesup.com/538033/coastal-container
- **broxer.com** (Broxer free company profile, DR 26): https://broxer.com/c/ecosouth-services
- **renovationsup.com** (free business listing, DR 19): https://www.renovationsup.com/142708/coastal-container
- **excellentcontractor.com** (free business listing, DR 9): https://www.excellentcontractor.com/65708/southern-disposal
- **locabee.com** (free business listing, DR 7): https://locabee.com/pensacola/service%20provider/coastal%20container-2281562

Free profiles and posts (4): issuu.com, crunchbase.com, bebee.com, video-bookmark.com

Left out: 3 mold, water-damage or janitorial directories from competitors' other trades.

