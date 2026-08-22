# The template is LOCKED

Approved by Dan on 2026-08-21. The frozen files are:

    template/base.html
    template/index.html
    template/inner.html
    template/assets/theme.css

**These four files are identical on every site in the network and do not change per
site.** The design, the colors, the section order, the card shapes, the band
rhythm — all settled. Do not redesign, do not "improve", do not swap the palette
for a different niche.

## What DOES change per site

    sites/<domain>/site.json    the facts: city, phone, counties, neighborhoods, sourced local facts
    sites/<domain>/copy.md      every word of prose, hand-written for that city
    sites/<domain>/assets/      hero.jpg + work-1/2/3.jpg, generated for that city

The template renders those. That is the whole model: one frozen shell, unique
content inside it.

## The locked section order

     1. sticky call bar
     2. photo hero -- eyebrow, H1, gold accent line, lede, CTA, note, trust band
     3. four value cards            (white)
     4. stat strip                 (navy)
     5. three numbered steps
     6. three-photo work gallery   (navy)
     7. what the technician needs to know + answer box   (white)
     8. four service/factor cards  (tint)
     9. four problem cards + nudge + CTA                 (white)
    10. sourced local facts        (navy)
    11. FAQ accordion              (tint)
    12. closing CTA                (navy)
    13. footer + compliance + mobile call bar

## Changing a locked file

Only when it is a bug that affects every site (a rendering fault, a broken path,
an accessibility failure). Never for taste, and never for one site. If one site
needs something different, the answer is different copy, not different CSS.

Tagged in git as `template-v2`. v1 was the four-page version; v2 adds one page per
service, which is what Kyle means by "add service-specific pages".

## Page map — depends on the site's phase

`site.json` carries `"phase": 1` or `"phase": 2`. Phase 1 is what almost every
site in the portfolio is right now; phase 2 is the later expansion.

**Phase 1 — 3 pages.** The whole trade lives on the home page.

    /                              1,700-3,200 words  the money page, targets niche + city
    /about/  /contact/             short, /contact/ carries the what-to-have-ready block

The four failure cards are full sections of 200-360 words each, because there are
no service pages yet for them to hand off to.

**Phase 2 — 8 pages.** Adds the service pages.

    /                              1,300-2,300 words  the money page, targets niche + city
    /<service-1..4>/               900-1,500 words each, targets service + city
    /services/                     hub, links to all four
    /about/  /contact/             short, /contact/ carries the what-to-have-ready block

At phase 2 the failure cards shrink to 40-80 word teasers, each linking to the
service page that covers it. Every service page cross-links the other three, and
the footer lists all of them.

Only Naperville and Fort Worth are phase 2 today. All 83 site.json files already
carry full `services` definitions, so promoting a site is a pure writing job.
