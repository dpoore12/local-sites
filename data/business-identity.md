# Business identity for listings and citations

Provided by Dan, Aug 28 2026.

## Primary address (in use)
965 Magnolia, STE 73-J
Larkspur, CA 94939

## Also available
- A Florida address (details not yet supplied)
- An Arizona address (details not yet supplied)

## Still missing
- Registered legal entity name. Listings are being tested under the site brand
  name from `data/nap.csv` (e.g. "Danville Garage Door Repair Pros").
- EIN (needed for 10DLC messaging registration, not for directory listings).

## Signup email used for the directory test
danpoore99@gmail.com

## Rules that still apply
- NEVER create a Google Business Profile.
- Legal-vertical directory profiles (Justia, Avvo, FindLaw, Lawyers.com, state bar)
  stay on hold until a firm signs. 240 rows in data/listings.csv are marked
  "hold until a firm signs" for this reason.

## Decision — Aug 29, 2026: paid directory syndication is on hold

**Dan: "Hold off until we have a signed tenant."**

The tool: eZlocal offers $39/mo (list $99) to sync one listing to 40+ directories — Google, Yellow Pages, Dexknows, Superpages, Bing, Apple, Yahoo, Waze, Manta. Seen at the final upsell step of the free eZlocal listing flow, Aug 29.

Why it's parked, not rejected:
- Priced per business, not per account. 83 x $39 = ~$3,200/mo, ~$39k/yr.
- It syncs to Google, which requires a Google Business Profile — a hard never-do.
- It would push the Larkspur address to 40+ sites at once. Aggregator data is hard to retract.

When to revisit: the first signed tenant. Push THEIR real business name, address and license number through it. $39/mo against $500-1,000/mo rent is trivial, and the listing is then true.

## Decision — Aug 29, 2026: no directory listings before a tenant signs

Triggered by a queued job to submit 82 FreeListingUSA listings using the Larkspur, CA address for businesses in Ann Arbor MI, Tampa FL, etc. That is false information published to a third party.

Extends Dan's existing rule ("never create a lawyer profile before a firm signs") to all directory listings.

What is still allowed:
- Listings where the directory has a service-area / hide-address option so no false address is published (eZlocal, Manta, Yelp all have one).
- Local link outreach — chambers, county sites, local news, community pages. Real site, nothing invented, no captchas. This is the 717-target list in data/link-targets-mined.csv.

Also open, from our own DISCLAIMERS.md: California makes it a misdemeanor to advertise construction work without holding the license in that classification, and "advertise" includes electronic transmission. The current first-person "we fix your garage door" copy on CA home-services sites has no license number and no operator behind it. Needs resolving separately from the listings question.
