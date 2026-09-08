# The Art of SEO (4th ed.) — what applies to this network

Read 7 Sep 2026 against our measured position. Sections read in full: duplicate
content (pp. 289–298), content uniqueness and depth (pp. 286–288), local search
(pp. 599–616), plus topic mapping across all 775 pages for link building,
keyword research and technical SEO.

Sorted into what changes the plan, what confirms it, and what to discard.

---

## 1. What changes the plan

### 1.1 The map pack is a ceiling we cannot pass

> "If you see a map pack for any search phrases that matter to your business,
> that's proof that Google ascribes local intent to that search query."

Tested on `garage door repair fort worth`, searched from Fort Worth:

    POSITION 1-3    local_pack   Supreme (4.9/224) · Express (5.0/255) · Action (4.9/412)
    POSITION 4      organic      first non-map result
    POSITION 5      People Also Ask
    POSITION 6      Yelp

The top three slots are Google Business Profiles. They need a verified physical
address and they carry hundreds of reviews. **We cannot enter that block.** Our
absolute ceiling on a local commercial term is organic #1, which renders as the
fourth thing on the page, under a map.

Local results rank on relevance, prominence **and proximity**. Proximity is not a
content problem and cannot be written around.

This does not kill the model. It prices it: on local commercial terms we are
competing for the scraps under the map, and every such market has that same
ceiling. It is the strongest argument yet that the tenant is the product, not an
afterthought — a signed operator brings the profile we cannot have.

### 1.2 Google is told, in print, not to fall for city-swapped pages

> "Unique text content, different from other pages on the site in more than just
> the replacement of key verbs and nouns (yes, this means all those webmasters who
> build the same page and just change the city and state names, thinking this makes
> the content 'unique,' are mistaken)."

That is the town-page strategy described exactly, and it is the failure mode if we
scale it by template. The three Fort Worth pages written on 7 Sep (Keller, Haltom
City, Benbrook) are safe because each is built on different verifiable facts — a
1990s subdivision boom, a 1950s postwar tripling, a lake and a storm track. That
standard is now a requirement, not a preference. A town page that could have its
town name swapped is a page that should not ship.

### 1.3 Duplicate content wastes crawl budget — which may be our 26%

> "A search engine bot comes to a site with a crawl budget... Each time it crawls a
> page that is a duplicate, you have let the bot waste some of its crawl budget.
> That means fewer of your 'good' pages will get crawled. This can result in fewer
> of your pages being included in the search engine's index."

We measured 26% index coverage and blamed the router redirect bug. This is a second
candidate cause that is entirely consistent with what we see: 83 sites on one
template, near-identical structure, Google spending its budget confirming
duplication instead of indexing new pages. The 28 September re-measure now has two
hypotheses to separate, not one.

### 1.4 Helpful Content risk is sitewide, not per page

> "Sites that engage in publishing significant volumes of content solely to rank in
> search results can see drops in their search traffic sitewide, not just to the
> pages that are seen as search engine-focused."

The 2,859-page expansion plan is not a page-level bet. If it reads as
volume-for-ranking, the downside lands on the whole site including the pages that
already work. This raises the cost of being wrong and supports building one site
deep and watching it, rather than 83 at once.

### 1.5 Our duplicate guard is looser than the engines'

> "Search engines look at relatively small phrase segments (e.g., five to six words)
> for the presence of the same segments on other pages on the web."

`template/build.py` sets `SHINGLE = 15`. We only fail a build when two sites share
a fifteen-word run. Google is described as working at five to six. Dropping to 15
was reasonable to avoid false positives on common phrasing, but it means our guard
passes content Google may still read as duplicated. Worth testing at 8–10 to see
what it catches; not worth going to 6, which would fail on ordinary English.

### 1.6 Zero structured data on all 1,291 pages

No `application/ld+json` on any page, including the homepage — `build.py` passes
`schema_json=None` everywhere and the homepage's schema object is falsy in
practice. Breadcrumb markup is the honest win here and it is small.

Be careful what we add: `LocalBusiness` markup requires an address we do not have,
and asserting one in structured data is the same misrepresentation problem the
directory categories raise. Google also cut FAQ and HowTo rich results back to
authoritative sites in 2023, so the CTR upside the book describes is smaller in
2026 than when it was written. This is a real gap, not a large one.

### 1.7 Google strips our chrome before judging thinness

> "Google and Bing factor out the common page elements, such as navigation, before
> evaluating whether a page is a duplicate... Note, however, that these pages risk
> being considered thin content."

Our location pages render at ~770 words, of which ~366 is shared chrome. Google
judges the ~400 authored words. That is above the 30–50 word floor the book gives
but not by the margin the rendered number suggests. The authored body is the real
page.

---

## 2. What it confirms

- **Topic clusters / hub and spoke.** Already built: `/services/` links down to all
  20 spokes, every spoke links up to hub and homepage, siblings capped at 3. The
  cap is correct — Ippei's "no footer link blocks" says the same.
- **Search intent and SERP format matching.** Explains the Tampa result directly:
  our informational pages win, our commercial pages lose, because the SERP for each
  rewards a different thing.
- **Weakness testing before writing.** The book's manual sanity check is the screen
  that found the furnace questions — ranking pages carrying 2 referring domains
  against our 3.
- **Content themes.** Off-topic content weakens the whole site. Furnace questions on
  a furnace repair site are on-theme; this is not blog-for-the-sake-of-it.

## 3. What to discard

- **Backlink outreach to competitors' link sources.** We pulled those profiles.
  They are scraper junk and bar-licensed attorney directories. Nobody to email.
- **Copyright/DMCA enforcement, syndication canonicals, affiliate guidance.** Not
  our situation.
- **Geogrid tools (Local Falcon, BrightLocal grid scans), GBP performance
  dashboards, fake-competitor audits.** All require a Google Business Profile.
  Revisit the day a tenant signs; useless before then.
- **Rich snippet chasing beyond breadcrumbs**, for the 2023 deprecations above.

---

## 4. Actions this produces

1. Make the weakness test a required gate in `PHASE2-WRITER-BRIEF.md`: check the
   top 10 and the referring-domain count of ranking pages before any page is
   written.
2. Add the city-swap rule to the writer brief in the book's own words.
3. Test `SHINGLE` at 8 and 10 against the current corpus; see what fails.
4. Add BreadcrumbList markup. Do not add LocalBusiness.
5. Treat the 28 Sep re-measure as separating two hypotheses — redirect damage
   versus duplicate-driven crawl waste — not confirming one.
6. Keep expansion on one site until it is measured. Sitewide risk changes the
   arithmetic of being wrong.
