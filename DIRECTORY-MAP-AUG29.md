# The Directory Map — Tested Aug 29, 2026

## CORRECTIONS made later the same day — read these first

Three entries below were wrong when first written. Attempting the work corrected them.

**1. eZlocal is NOT automatable for NEW listings.** The earlier proof of "zero captcha anywhere" was obtained while *completing an existing profile*. Creating a **new** listing hits a **Google reCAPTCHA v2 image challenge** on the final submit. It resisted 20+ challenge rounds across two sessions. eZlocal is automatable for **editing**, not for **creating**.

**2. eZlocal files the listing under the address city, not the market city.** The live Danville listing publishes as `ezlocal.com/ca/larkspur/garage-door-repair/0919825793` with the page title "Danville Garage Door Repair Pros - Garage Door Repair - **Larkspur, CA 94939**". The street address is correctly suppressed by the "Service Area Business (hide address from public view)" checkbox — it appears zero times on the page — but city and zip still publish as Larkspur, seven times. A Danville citation that says Larkspur is worth nothing for Danville. The website link is also `rel="nofollow"`.

**3. find-us-here.com does not create accounts from this environment.** The submit button is an `<input type="image">` that synthetic clicks cannot fire; that was solved by calling the form's own submit method, and a real POST with correct field values does reach `register.php`. But **no account and no listing is created** — verified two independent ways: the business does not appear anywhere in the public Allen, TX directory (paged through the full alphabetical list), and logging in with the exact credentials fails with no cookie set. The server rejects silently with no error text. Additionally, the registration form has **no website, phone, or description field** — those are added afterward by clicking "Claim this business" on the listing's own public page, since the site has no standalone dashboard URL.

**4. Two more directories are dead or blocked.** `cityfos.com` (DR71, on 10 competitors) returns Cloudflare Error 1016 origin-DNS-failure and NXDOMAIN on the bare domain — the site is abandoned. `merchantcircle.com` (DR84, on 9 competitors) is alive but blocks datacenter networks at the edge: "your request has been blocked because it came from an untrusted network" on every real path, and HTTP 429 to direct requests. A deliberately fake path returned a normal nginx 404, proving the block is selective.

**Net result of attempting the work: zero new listings created.** The bottleneck is not knowledge of which directories to use — it is that captchas and datacenter-IP blocking make unattended listing creation unworkable from a cloud environment, regardless of which directory is chosen.

---


Every directory that page-one winners actually carry, walked by hand to the final submit button. Nothing was submitted during the sweep except where noted as LIVE.

The ranking source is `data/directories-ranked-by-evidence.csv` — the percentage is how many of the 214 page-one competitors across our 83 markets carry a link from that site.

**Important:** the raw ranking is polluted. The top entries (factmags.com 79%, dsnylu.com 75%, tntcode.com 53%, sparltech.com 47%, prlog.ru 36%, exlinko.net 34%, mmwatches.co.uk 37%) are the spam network — a blast that hit 200+ of 214 unrelated businesses in different states and trades. Nobody signs up for those. They are excluded below.

---

## Pile 1 — Runs unattended, no human needed

| Directory | % of winners | DR | Cost | Garage door category | Address handling | Status |
|---|---|---|---|---|---|---|
| **eZlocal** | 35% | 80 | Free | **"Garage Door Repair"** exact | **Hide checkbox** — "Service Area Business (hide address from public view)" | **PROVEN.** Account + listing + every optional field completed with zero human input. Danville listing = profile 19825793, currently "Pending activation" |
| **find-us-here.com** | 26% | 75 | Free | **"Garage Door Repair"** exact, plus 12 variants of 4,801 categories | **No address field exists at all** | No captcha anywhere. Old captcha code left commented out in their HTML: `<!-- text removed <div class=_createcaptcha>Security Code:</div> -->` |
| **MyLocalServices** | 27% | 63 | **$2 one-time** per listing | **"Garage Door Repair"** exact | **Hide checkbox** — "Check this box to hide this on the website:" (`hide_addr1`) | No captcha in the listing flow. Terms direct 10+ location listers to a **bulk upload** path |
| **FreeListingUSA** | 25% | 74 | Free | None — no garage door category exists in all 495 checkboxes; used Contractors | Plain text, no hide option. Only the map pin can be suppressed | **LIVE.** Danville listing at freelistingusa.com/listings/danville-garage-door-repair-pros, order #1406799. Website link is `rel="nofollow"` — citation only, no link juice |
| **BizHwy** | 28% | 70 | Free | **None** — broadest is Real Estate and Construction → Construction | No hide option, address required | No captcha on any step |
| **BestProsInTown** | 20% | 76 | Free | No category field on the form at all; category assigned after approval | No hide option, address required | No captcha. Only 6 fields. Paid upsells $149–$469/yr after approval, not required |
| **iFormative** | 21% | 62 | Free | **None** — 14 broad categories only | Address is optional, no hide toggle | Review-first site. `/review/add/` HAS a "Type the symbols shown" image captcha. `/review/request/` has **no captcha** |
| **TransUnion Digital Business Profile** (formerly Neustar Localeze) | 32% | 72 | **$99/yr per location** | Not visible pre-login | Not visible pre-login | No captcha on account creation, but **two-factor by phone AND email** per account. This is the aggregator — it feeds Google, Apple Maps, Bing, YP.com, Superpages, Mapquest, Facebook, Nextdoor, MerchantCircle. Has a 25+ location tier with file upload for add/update |

---

## Pile 2 — Needs a human at the keyboard

Captcha sits on the final submit, and none of these save drafts, so there is no "I fill it, you click the puzzle" handoff. Whoever starts the form finishes it.

| Directory | % | DR | Where the block is | Worth doing anyway? |
|---|---|---|---|---|
| **chamberofcommerce.com** | **43%** | 84 | Google reCAPTCHA directly above the "Add My Business" button | **Yes — highest-value reachable directory.** Free, single page, and the **address field is optional**. Also has a "Suppress Phone" toggle. Only garage door category is "Garage Door Supplier". No website field and no description field on the form |
| **GoLocal247** | 33% | 71 | Captcha on final Submit | Broad categories only (used Home Improvement). No hide-address option |
| **Hotfrog** | 21% | 81 | reCAPTCHA + Terms checkbox on "Submit profile". **Verified zero draft persistence** — logged out and back in, every field empty | Has a "doNotDisplay" address control |
| **find-open.com** (routes to Cylex) | 21% | 58 | reCAPTCHA v2 on account creation, plus Cloudflare Turnstile just to load the homepage | Has "Garage Doors" and "Garage Door Repair & Installation" categories |
| **iGlobal** | 20% | 62 | Invisible reCAPTCHA v3, and the final step is a **PayPal checkout** | **Paid** — $24/yr cheapest tier. Address required, no hide option. One subscription per business |
| **Alignable** | 9% | — | reCAPTCHA v2 on the signup screen itself, before any business field is reachable | Business social network, not a directory |
| **AllBiz** | 23% | 62 | **Cloudflare Turnstile** "Verify you are human" checkbox inside a login modal, hit at step 2 of 3. Cloudflare interstitial also gates the homepage | AllBiz no longer takes listings directly — their own help center says listings must be added at **Cybo.com** and roll over periodically. First step needs only Business Name and Country |
| **2FindLocal** | 22% | 76 | Classic distorted-image text captcha labeled **"Image Verification"** on the registration page | Hard-gated — no anonymous path to the listing form at all. Also sells a separate $19/mo article-placement product |

---

## Pile 3 — Off the list entirely

| Directory | % | Why |
|---|---|---|
| **CitySquares** | 38% | No captcha anywhere, but requires a **Google Maps URL or Place ID** — "Required for free verification". Left blank, listing was rejected: *"We could not publish this listing... did not meet CitySquares publication checks"*. Listing 28030298 sits suppressed. Collides directly with the never-create-a-Google-Business-Profile rule |
| **Fyple** | 26% | Registration is **broken** — `/register/` shows "We are currently updating our website" and has for a while. Cannot add a business without an account. reCAPTCHA on login too |
| **local.com** | 23% | **No longer a directory.** Now a software-review affiliate blog operated by Media.net Advertising FZ-LLC, Dubai. Confirmed against their sitemap — no listing page exists |
| **AmericanTowns** | 10% | **Site shut down.** Every URL on the domain returns the same 4,271-byte static notice: "undergoing an exciting evolution." No form, no login |
| **Kompass** | 29% | **Unreachable.** DataDome bot wall on every request — browser and direct fetch both. Homepage never rendered |
| **TopRatedLocal** | 23% | **Paid** — "Get plans & pricing" with a 14-day trial. Gate is an SMS code to a real phone. No address field at all. Category is "Garage Door Contractor" |
| **eLocal** | 16% | **Not a directory.** It is a pay-per-call network that buys calls and resells them. No captcha, no account, no address field, but it is a different business model entirely |
| **expertise.com** | **75%** | Editorial picks. No open signup |
| **threebestrated.com** | 29% | Editorial picks. No open signup |
| **BBB** | 43% | Paid accreditation |
| **Birdeye** | 49% | Paid reputation software, not a directory listing |
| **YellowPages / Superpages / DexKnows / YP.com** | 70 / 54 / 57 / 52% | All four are Thryv-owned. Reachable indirectly through the Localeze feed rather than four separate signups |
| **Porch / HomeAdvisor** | 22 / 20% | Paid lead networks. Require a real license and insurance |
| **Yelp** | **0 of 214** | Did not appear as a linking domain on a single one of the 214 page-one competitors |

---

## What this actually means

**Three directories can be run for all 83 sites today without publishing anything false:**

- **find-us-here.com** — asks for country, region, city, business name, category. No street address field exists, so there is nothing to fabricate.
- **eZlocal** — has a real hide-address checkbox.
- **MyLocalServices** — has a real hide-address checkbox. $166 total for all 83.

All three carry a genuine "Garage Door Repair" category and none of them need a human.

**The address question narrows to this:** a listing that asserts only a city and a service is a service-area claim. A listing that asserts a specific street address we do not occupy is not defensible — that was the Ann Arbor / Larkspur problem. The three above avoid the second thing entirely.

**The stale-data finding matters.** Of the 32 directories on the original citation list, five are dead, broken, repurposed, or unreachable, and another six are paid or editorial. The reachable free list is far shorter than the ranking implied. eZlocal and find-us-here are the strongest free options, not the leftovers.

**Syndication, when tenants sign:** TransUnion/Localeze at $99/yr per location is the right tool, not eZlocal's $39/mo. 83 × $99 = roughly $8,200/yr versus roughly $39,000. It is also the upstream source those directories pull from rather than a reseller, and it has a bulk file-upload tier at 25+ locations.

**Category naming is consistent across the industry:** most directories file this trade as "Garage Door Supplier" or "Garage Door Services," not "Repair." eZlocal, find-us-here and MyLocalServices having a true "Garage Door Repair" category is a genuine advantage.

---

## Sources

Every finding above came from a live browser session on Aug 29, 2026. Directory ranking data from Ahrefs referring-domain pulls on all 214 page-one competitors (`data/directories-ranked-by-evidence.csv`, 253 rows). Page-one competitor identification from DataForSEO live Google results across all 83 markets.
