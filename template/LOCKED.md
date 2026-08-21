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

Tagged in git as `template-v1`.
