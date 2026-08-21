# Writer Brief — read this before writing any site

You are writing one complete local service website. The structure is already
built and locked. Your job is the words and two config fields. Nothing else.

**This is a PHASE 1 site: home, about and contact only. No service pages.**
`site.json` already lists four services for later, but nothing renders or links
to them yet, and you must not write any `svc_*` block. Because there is no
service page to hand off to, the four symptom cards on the home page carry the
full explanation of each problem themselves.

## Read these first

1. `sites/garagedoorrepairnapervillepros.com/copy.md` — the reference site.
   Match its depth, tone and block structure exactly.
2. `sites/fortworthgaragedoorrepairpros.com/copy.md` — the second reference, same
   trade as the first. Read both and notice how they say completely different
   things about the same job. That is the bar.
3. Your own `sites/<domain>/copy.md` — the stub. Every block you must fill.
4. Your own `sites/<domain>/site.json` — read `service`, `city`, `state`,
   `counties`, `services`, and `_market.keyword`.

## Step 1 — Research three local facts

Find three things that are true about YOUR city and that change how this
specific service gets done there. Each needs a working source URL.

The three that worked for the reference sites:

- **Housing or infrastructure vintage.** When the building stock went up, with
  two or three named neighborhoods and their eras. Census Reporter and
  data.census.gov table B25035 give a median year built. This drives what
  equipment is actually installed in that city.
- **A local rule.** A city permit requirement, a municipal code, a county
  ordinance, a state statute. Search the city's own `.gov` site. For legal
  niches this is the state statute of limitations or a state-specific rule of
  liability, from the state legislature's own site.
- **A dated local event or condition.** A specific storm with a date from the
  National Weather Service office covering that city, a documented local
  hazard, a county-level statistic from an official source. It must be dated
  and specific, never a generality about the region.

Legal niches: substitute the housing fact for something equally concrete —
county court structure, local filing venue, a county-level crash or claim
statistic from the state DOT or the county clerk.

Also find **6 real neighborhoods** in that city, by name.

If you cannot source a claim, throw it out and find another. Never guess. A
guessed fact is the fastest way to lose the tenant this site is being built for.

## Step 2 — Write the copy

Fill every `TODO` in your `copy.md`.

- Home page blocks together render to **1,700–3,200 visible words**.
- `symptom_1` through `symptom_4` are **200–360 words each**. This is where the
  real substance goes. For depth and tone, read the `svc_*_body` blocks in the
  two reference sites and compress that quality into 200–360 words — those are
  phase-2 blocks you are NOT writing, but they set the bar.
- Nine short blocks head the page bands: `urgency_bullet`, `values_eyebrow`,
  `values_head`, `values_lede`, `factors_lede`, `problem_lede`, `problem_nudge`,
  `expect_head`, `emergency_note`. These used to be hardcoded in the template in
  garage-door language. Write them for YOUR service — a dog bite site must never
  say "your door". `emergency_note` is the footer safety line and must be true
  for your service; if there is no physical hazard, make it a plain practical
  note instead of inventing a danger.

Hard rules, all enforced by the build:

- **No block may share 15 consecutive words with any other site.** Not with the
  two reference sites, not with any other site in the batch. Write about your
  city's specifics and this stops being a constraint.
- **Sell the work, never a phone consultation.** A technician is dispatched, the
  price is quoted before work starts, the thing gets fixed. Never "call and
  describe the problem", never "talk it through with a technician", never
  anything that frames the value as a conversation.
- **Name no business, no licence number, no review count, no years in business,
  no dollar price.** No tenant is signed for this site, so none of it is true.
  For legal sites: no firm name, no attorney, no case result, no settlement
  figure, no "our lawyers", no win record.
- Write plainly. Short sentences. A homeowner or a person who just got hurt is
  reading this, not a marketer.

## Step 3 — Fill two fields in `site.json`

- `local_facts` — exactly 3 entries. Copy the object key names from the
  Naperville file exactly. Each carries the claim, why it matters for this
  service, and the source URL.
- `neighborhoods` — the 6 real names.

Change nothing else in `site.json`. Do not touch the phone number.

## Step 4 — Generate four photos

Four images into `sites/<domain>/assets/`: `hero.jpg` (1800px wide) and
`work-1.jpg`, `work-2.jpg`, `work-3.jpg` (900px wide). All four are used in
phase 1. Generate with:

    asi-generate-image '{"prompt":"...","filename":"x","aspect_ratio":"16:9","model":"gpt_image_2"}'

with `api_credentials=["llm-api:image"]`, one image per bash call. Then downscale
to JPEG with PIL, quality 80, progressive, and delete the PNGs.

Prompt rules: photorealistic documentary photography. Real work being done, real
equipment, real damage. Regionally correct architecture and light for your city.
**No text, no logos, no brand names, no company names anywhere in the image.**
Faces turned away or out of frame. The hero is a wide establishing shot; the
three work images are close on the actual job.

For legal niches, photograph the situation and the place, not a courtroom
stock cliché: the road type where these crashes happen, the local county
courthouse exterior, a documents-and-desk detail. No gavels, no scales of
justice, no stock lawyer portraits.

## Step 5 — Verify

    cd /home/user/workspace/local-sites && python3 template/build.py <your-domain>

Fix every ERROR until it passes. A `PLACEHOLDER` phone WARN is expected and
correct — leave it alone. If it reports shared word runs, rewrite the block it
names; do not delete the block.

Then run the full build to check yourself against every other site:

    python3 template/build.py

Report back: the three facts with URLs, the per-page word counts from the build
output, and confirmation your site passes.
