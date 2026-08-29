# UG — Directory signups

Aug 28, 2026. This replaces the vague "listings" ask with a specific, tested job.

## Why you and not the agent

I tried all eight of the main directories tonight with a cloud browser and completed
zero of them. Not one was blocked by missing business information. Every single block
was bot detection:

| Directory | What stopped the agent |
|---|---|
| Yellow Pages | Google reCAPTCHA image challenge, escalated 3 rounds, never cleared |
| Manta | Same escalating reCAPTCHA at account signup |
| Brownbook | Same, at the mandatory account-creation step |
| Yelp | Slider-style bot check at the final signup step |
| Cylex | Cloudflare blocked the datacenter IP outright — 403, no challenge offered |
| Bing Places | No business form exists until you sign in with Google/Facebook/Microsoft |
| Nextdoor | Dan's gmail already has a personal Nextdoor account, blocking business signup |
| Hotfrog | Email confirmed and logged in — then a reCAPTCHA on the Submit button |

A human clears each of these in about four minutes. That is the entire job.

## IMPORTANT — read this before you plan your time

My first assumption was that the captcha sits only at account creation, so one signup
would unlock unlimited listings. **Hotfrog disproved that.** We got the account created,
the email confirmed, logged in, and every field filled — and then hit a Google reCAPTCHA
image challenge sitting on the "Submit profile" button itself. Twenty-plus challenges,
never cleared. The widget itself eventually reported "This site is exceeding reCAPTCHA
Enterprise free quota," so at least part of that loop is Hotfrog's own misconfiguration.

So we do not yet know the answer to the question that decides everything:

**Is the captcha per-account, or per-listing-submission?**

- Per-account → you do 6 signups, the agent does the remaining 82 × 6 listings unattended.
- Per-submission → roughly 750 form submissions all need a human, and we have to cut the
  directory list down hard and pick maybe the top three only.

One directory at n=1 is not an answer. Please establish this deliberately and early:
create ONE account, submit TWO listings inside it, and tell us whether the second
submission showed a captcha. Do that before grinding through volume.

## What we need from you

**Create the accounts, and answer the per-listing captcha question above.**

Priority order — the first three carry most of the weight:

1. Yelp for Business — https://biz.yelp.com/
2. Yellow Pages — https://www.yellowpages.com/ (find "add your business")
3. Bing Places for Business — https://www.bingplaces.com/
4. Manta — https://www.manta.com/business-listings/add-your-company
5. Nextdoor Business — https://business.nextdoor.com/
6. Brownbook — https://www.brownbook.net/add-business
7. Angi, Thumbtack, Houzz — home services only, these want a license, park them for now
8. Cylex — skip, it blocks aggressively

Hotfrog's account is created and confirmed, but its listing is NOT submitted — it is
sitting on a broken captcha. Its captcha quota may reset, so it is worth one retry later.
Credentials below.

## First listing to enter in each account

Use this one. It is our test market.

- Business name: Danville Garage Door Repair Pros
- Street address: 965 Magnolia, STE 73-J
- City / State / ZIP: Larkspur, CA 94939
- Phone: (925) 230-5528
- Website: https://danvillegaragedoorrepairpros.com/
- Category: Garage Door Repair / Garage Door Services
- Description: Danville Garage Door Repair Pros connects Danville, CA homeowners with
  local garage door repair professionals. Call (925) 230-5528 to describe the problem
  and get a price before any work begins.

The other 82 are in `data/nap.csv` — business name, phone, website, city, service,
service area and a description already written for each one. Do not retype anything;
that file is the source.

## The address / service area thing — already solved

The address is in Larkspur but the business serves Danville. That is deliberate and
correct. Where the agent got far enough to test it, nothing rejected it.

- **Manta** handles it best: a "don't display my address publicly" checkbox plus a
  separate Service Areas field taking up to 20 areas. Put Larkspur in the address
  (hidden) and Danville in Service Areas.
- **Yelp** has a working "hide my full address" toggle — display drops to city/state/zip
  with the map blurred. No separate service-city field.
- **Brownbook** has neither. Single address/city only.

Where a service-area field exists, enter: Danville, Alamo, San Ramon, Blackhawk,
Diablo, Contra Costa County, California

## Categories

- Yelp has an exact match: Home Services > Garage Door Services. Best taxonomy of the eight.
- Brownbook has no garage door category. Closest is "Home and Garden Equipment Repair
  and Maintenance".
- Hotfrog has no garage door category either. Closest real matches in its typeahead are
  "Doors & Door Systems" (what we selected) and "Doors", with "Home Improvement" as a
  broader fallback. Hotfrog also has a "Hide address?" checkbox.

## Nothing here requires paperwork

Across all eight, not one form asked for a business license, EIN, tax ID, employee
count, years in business, or proof of insurance. Angi/Thumbtack/Houzz do want a
license, which is why they are parked.

## The one thing to check on every listing

**Does the finished public listing render the website as a real clickable hyperlink, or
as plain unlinked text, or is it hidden behind a paid upgrade?**

Note the answer for each directory. A listing that does not link is worth nothing to us
and we should stop doing that one. This is the single most important data point you can
bring back.

## Hard rules

- **Never create a Google Business Profile.** Not for any site, not ever. This is the
  thing that gets portfolios suspended.
- **Do not touch the 40 legal sites.** No Justia, Avvo, FindLaw, Lawyers.com or state
  bar profiles until an actual firm signs as a tenant. 240 rows in `data/listings.csv`
  are already marked "hold until a firm signs".
- **Do not pay for anything.** If a directory demands payment to publish, note the price
  and move on.
- **Do not link the 83 sites to each other.**
- **Never ask anyone for a review.**
- If a directory demands an SMS or voice verification code, stop on that one and note it.
  The 83 numbers ring to voicemail and there is no code to read.

## Credentials

- Hotfrog: admin.hotfrog.com — danpoore99@gmail.com / LandlordSEO2026! (created and
  email-confirmed Aug 28)
- For the rest, Dan is setting up a dedicated listings email tomorrow. Use that once it
  exists rather than his personal gmail. Ask him for it before you start on Yelp.
- Nextdoor specifically will NOT work on danpoore99@gmail.com — that address already has
  a personal Nextdoor account. It needs the new address.

## What to report back

Per directory: account created yes/no, listing live or pending review, the public listing
URL, whether the website link is clickable / plain text / paywalled, whether adding a
SECOND listing inside the same account triggered a fresh captcha, and anything demanded
that we could not supply.

That second-listing question is the one that decides whether the agent can finish the
remaining 82 unattended or whether all 83 need a human. Please test it deliberately.

---

## Aug 29 test round 2 — the captcha map is now clear

| Directory | Captcha? | Where | Result |
|---|---|---|---|
| FreeListingUSA | NONE anywhere | — | **SUBMITTED, LIVE.** Order #1406799 · https://www.freelistingusa.com/listings/danville-garage-door-repair-pros · account `danvillegdrpros` · email still unverified and it went live anyway · website link is `rel="nofollow"` · no garage door category, used Contractors · street address shows as text (only the map pin can be hidden) |
| CitySquares | NONE anywhere | — | Account created, blocked ONLY by email confirmation link. Fully automatable once confirmed. Submission form is behind login at citysquares.com/users/sign_up |
| eZlocal | YES | final Continue, after all fields filled | Form URL prefills by query string: `https://dash.ezlocal.com/newlisting/add/?ph=<phone>&bn=<name>`. Has a "Service Area Business (hide address from public view)" checkbox. Real "Garage Door Repair" category exists. |
| GoLocal247 | YES | final Submit, after all fields filled | Form at https://www.golocal247.com/claim/business/free · no login step, form creates the account · no hide-address option · only broad categories (used Home Improvement) |
| Hotfrog | YES | Submit profile | **No draft persistence** — verified by logout/login, all fields wipe. There is no Save Draft button. Nothing can be pre-filled for a human to finish. |

### The answer to the per-account vs per-submission question
Still unanswered — no listing has cleared a captcha yet. But it now matters less: the captcha is on the **final submit** on every site that has one, not on account creation. That means pre-filling and handing off is impossible on those sites, because nothing persists (proven on Hotfrog).

### Real conclusion
Sort directories into two piles: **no-captcha (fully automatable, zero human time)** and **captcha-on-submit (a human must be at the keyboard for the whole form)**. FreeListingUSA and CitySquares are in pile one so far.
