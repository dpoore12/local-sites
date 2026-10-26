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
