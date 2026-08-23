# local-sites

Rank-and-rent network. One domain per niche + city. Each site is rented to **one**
local operator for a **flat monthly subscription**. This is not a per-call marketplace
and it is not connected to any call-routing product.

**Start with `UG-STATUS.md`** for the current state of all 83 sites. As of
23 August 2026 they are built, live, indexed and in Search Console.

> **Open question, added 23 August 2026.** This repo states above that it is not a
> per-call marketplace, and the pages carry no routing disclaimers because each
> site is rented to one named operator. The researched tenant plan in
> `TENANTS.md` ranks selling the calls into pay-per-call networks first, because
> Dan does not do phone selling. If that route is taken, calls do get distributed
> and the disclaimer position changes. **Do not deploy any copy change on this
> basis, and do not connect any site to a call network, until Dan has ruled on
> it.** Flagged rather than quietly resolved.

**This is a separate repository from `lead-router` on purpose.** Different product,
different deploy target, different content rules, and — critically — different legal
posture. `lead-router` pages carry routing disclaimers because calls get distributed.
Sites here are rented to a single named operator, so those disclaimers would be
false. Nothing should ever be copied between the two repos.

---

## The one rule

**The template is identical on every site. Everything a visitor reads as prose is not.**

Two inputs per site:

| File | Holds | Who writes it |
|---|---|---|
| `sites/<domain>/site.json` | facts only — domain, phone, city, counties, neighborhoods, sourced local facts, tenant status | operator |
| `sites/<domain>/copy.md` | every block of prose on the page | a human writer, per city |

Nothing in `template/` contains a sentence about a city, a service, or a symptom.
If you find one, that is a bug — move it into `copy.md`.

---

## Build

```bash
pip install jinja2 markdown
python template/build.py                    # build all sites into dist/
python template/build.py <domain>           # build one
python template/build.py --check-only       # run guards, write nothing
python template/build.py --live             # emit index,follow instead of noindex
```

Output is plain static HTML + one CSS file. No JS, no build step, no framework.
Deploy `dist/<domain>/` to anything.

`--live` is deliberately opt-in. Default output is `noindex` so a half-finished
site can never be indexed by accident.

---

## The guards (build fails, it does not warn)

The point of these is that 80 near-identical city pages is the exact pattern
Google names under [doorway abuse](https://developers.google.com/search/docs/essentials/spam-policies).
The build refuses to produce that.

| Guard | Threshold |
|---|---|
| Home body word count | 900–1,250 visible words |
| Symptom blocks | ≥ 4, each 105–175 words |
| Local Q&As | ≥ 3, each ≥ 55 words |
| Sourced local facts | ≥ 2, each needs a source URL, a stated practical relevance, and a verification date |
| **Cross-site duplication** | **no two sites may share a run of 15 consecutive words** |
| Phone | area code must be in that site's approved list; toll-free numbers rejected |
| Pre-tenant honesty | with no tenant signed, any license number, review count, years-in-business, family/veteran-owned claim, or `LocalBusiness` schema is a hard failure |
| Trust-claim blocklist | "licensed and insured", "5-star", "voted best", "A+ rating", etc. cannot appear until a tenant is verified |

The cross-site duplication check runs across the whole `sites/` directory on every
build. It is the guard that keeps the network alive.

---

## Tenant states

**`tenant.status: "none"`** — no operator signed yet. Page renders real local
troubleshooting content and a tracking number. No provider is named, no reviews,
no license, no `LocalBusiness` markup, and the footer says plainly that the site
is operated independently and is not itself a contractor. This is honest and it
still ranks.

**`tenant.status: "active"`** — fill in `business_name`, `license_number`,
`years_in_business`, `service_hours`, and only the trust claims the operator has
actually given you in writing. Set `schema.local_business: true`. Everything in
the tenant block must be verifiable, because it becomes structured data.

---

## Adding a site

1. `mkdir sites/<domain>` and copy `site.json` + `copy.md` from an existing site.
2. Replace **every** value in `site.json`. Research two real local facts and record
   their source URLs — this is the part that cannot be automated.
3. Rewrite **every** block in `copy.md` from scratch. Do not edit the previous
   city's prose; the 15-word duplication guard will catch it and the build will fail.
4. `python template/build.py --check-only` until it passes.
5. Point DNS only after the placeholder phone number has been swapped for a live
   tracking number in the correct area code.

Realistic effort: **90 minutes minimum per site**, and roughly 170–210 hours for a
network of 80+ once research, fact checking, and cross-portfolio duplicate review
are counted. Do not attempt this as one bulk generation run.

---

## Layout

```
template/
  build.py            build + all guards
  base.html           shell: header, footer, mobile call bar
  index.html          home page
  inner.html          services / about / contact
  assets/theme.css    entire design system, identical everywhere
sites/
  <domain>/site.json  facts
  <domain>/copy.md    prose
dist/                 build output, gitignored
```
