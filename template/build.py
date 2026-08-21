#!/usr/bin/env python3
"""Static builder for the local-sites network.

Two inputs per site and nothing else:

    sites/<domain>/site.json   facts only
    sites/<domain>/copy.md     every word a visitor reads

Nothing in template/ contains a sentence about a city, a service or a symptom.
If you find one, move it into copy.md -- that is the whole point of the guards
below. Run with --check-only to validate without writing.
"""
import json
import re
import sys
import shutil
import datetime
import urllib.parse
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
import markdown as md

ROOT = Path(__file__).resolve().parent.parent
TPL = ROOT / "template"
SITES = ROOT / "sites"
DIST = ROOT / "dist"
YEAR = datetime.date.today().year

# --- icons -------------------------------------------------------------------
def _svg(body, w=2):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{body}</svg>')

ICO = {
    "phone": _svg('<path d="M21.5 16.9v2.6a1.7 1.7 0 0 1-1.9 1.7 17 17 0 0 1-7.4-2.6 16.7 16.7 0 0 1-5.1-5.1A17 17 0 0 1 4.5 6a1.7 1.7 0 0 1 1.7-1.9h2.6a1.7 1.7 0 0 1 1.7 1.5c.1.9.3 1.7.6 2.5a1.7 1.7 0 0 1-.4 1.8l-1.1 1.1a13.7 13.7 0 0 0 5.1 5.1l1.1-1.1a1.7 1.7 0 0 1 1.8-.4c.8.3 1.6.5 2.5.6a1.7 1.7 0 0 1 1.4 1.7z"/>'),
    "pin": _svg('<path d="M12 21s7-5.7 7-11a7 7 0 1 0-14 0c0 5.3 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/>'),
    "check": _svg('<circle cx="12" cy="12" r="9.2"/><path d="M7.6 12.4l3 3 5.8-6.4"/>', 2.4),
    "bolt": _svg('<path d="M13.5 2L4 13.6h6.4L9.2 22 19 10.4h-6.3L13.5 2z"/>'),
    "clock": _svg('<circle cx="12" cy="12" r="9"/><path d="M12 7.2V12l3.2 2"/>'),
    "chat": _svg('<path d="M20.5 12.4c0 4-3.8 7.2-8.5 7.2a9.8 9.8 0 0 1-2.6-.35L4.5 21l1.3-3.7A6.9 6.9 0 0 1 3.5 12.4c0-4 3.8-7.2 8.5-7.2s8.5 3.2 8.5 7.2z"/>'),
    "search": _svg('<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.6-3.6"/>'),
    "house": _svg('<path d="M3.5 10.6L12 4l8.5 6.6"/><path d="M5.6 12.2V20h12.8v-7.8"/><path d="M10 20v-4.4h4V20"/>'),
    "cal": _svg('<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 9.8h17M8.2 3.2v3.4M15.8 3.2v3.4"/>'),
    "spring": _svg('<path d="M3 8h1.5M3 12h1.5M3 16h1.5"/><path d="M6 6c3 0 3 3 6 3s3-3 6-3M6 12c3 0 3 3 6 3s3-3 6-3"/><path d="M20.5 5v14"/>'),
    "wrench": _svg('<path d="M15.2 6.1a4.4 4.4 0 0 0 5.6 5.6l-8.4 8.4a2.3 2.3 0 0 1-3.2-3.2l8.4-8.4z"/><path d="M15.2 6.1L12.4 3.3"/>'),
    "warn": _svg('<path d="M10.3 3.9L1.9 18.2a1.9 1.9 0 0 0 1.7 2.9h16.8a1.9 1.9 0 0 0 1.7-2.9L13.7 3.9a1.9 1.9 0 0 0-3.4 0z"/><path d="M12 9.2v4.2M12 17.1h.01"/>'),
    "eye": _svg('<path d="M2.5 12S6 5.8 12 5.8 21.5 12 21.5 12 18 18.2 12 18.2 2.5 12 2.5 12z"/><circle cx="12" cy="12" r="2.8"/>'),
    "gear": _svg('<circle cx="12" cy="12" r="3"/><path d="M12 2.8v2.4M12 18.8v2.4M4.5 12H2.1M21.9 12h-2.4M6.7 6.7L5 5M19 19l-1.7-1.7M6.7 17.3L5 19M19 5l-1.7 1.7"/>'),
    "ruler": _svg('<path d="M4 18V9.5M10 18V4.5M16 18v-6M22 18H2"/>'),
    "shield": _svg('<path d="M12 3l7 3v5c0 4.4-2.9 8.4-7 9.6C7.9 19.4 5 15.4 5 11V6l7-3z"/><path d="M9.2 11.8l2 2 3.6-3.8"/>'),
}

LOGO_MARK = _svg('<path d="M3.4 10.7L12 4.2l8.6 6.5"/><path d="M5.7 12.3V20h12.6v-7.7"/><path d="M8.2 15h7.6M8.2 17.6h7.6"/>', 2.2)

FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
           '<rect width="32" height="32" rx="6" fill="#143d59"/>'
           '<g fill="none" stroke="#f5a524" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
           '<path d="M5 14L16 6l11 8"/><path d="M8 16v10h16V16"/><path d="M11 19h10M11 22.5h10"/></g></svg>')

# --- guard config ------------------------------------------------------------
HOME_WORDS = (1300, 2300)
SYMPTOM_WORDS = (40, 80)
QA_WORDS = 55
MIN_SYMPTOMS = 4
MIN_QAS = 3
MIN_FACTS = 2
SERVICE_WORDS = (900, 1500)  # each service page, whole rendered page including the shared bands
MIN_SERVICES = 4
SHINGLE = 15

# Claims nobody can verify from a page with no signed operator on it.
BANNED_PRE_TENANT = [
    "years of experience", "years in business", "family owned", "family-owned",
    "veteran owned", "veteran-owned", "licensed and insured", "licensed & insured",
    "fully licensed", "5-star", "five star", "five-star", "voted best",
    "a+ rating", "bbb accredited", "award winning", "award-winning",
    "trusted by", "thousands of", "satisfaction guaranteed", "our customers say",
    "read our reviews", "since 19", "since 20",
]

TENANT_FIELDS = ["business_name", "license_number", "years_in_business",
                 "reviews", "service_hours", "family_owned", "veteran_owned"]

TAG = re.compile(r"<[^>]+>")
WS = re.compile(r"\s+")


def visible_words(html):
    return WS.sub(" ", TAG.sub(" ", html)).strip().split()


def parse_copy(path):
    """copy.md is a flat list of `## key` blocks. Comments start with #."""
    blocks, key, buf = {}, None, []
    for line in path.read_text().splitlines():
        if line.startswith("## "):
            if key:
                blocks[key] = "\n".join(buf).strip()
            key, buf = line[3:].strip(), []
        elif line.startswith("#") and key is None:
            continue
        elif key:
            buf.append(line)
    if key:
        blocks[key] = "\n".join(buf).strip()
    return blocks


def domain_of(url):
    return urllib.parse.urlparse(url).netloc.replace("www.", "")


def is_draft(domain):
    """True when a site has not been written yet: copy blocks still TODO, or no
    sourced local facts. These are skipped rather than failed."""
    d = SITES / domain
    cm = (d / "copy.md")
    s = json.loads((d / "site.json").read_text())
    if not s.get("local_facts") or not s.get("neighborhoods"):
        return True
    return "\nTODO\n" in cm.read_text() if cm.exists() else True


def build(domain, live=False, check_only=False, corpus=None):
    sdir = SITES / domain
    s = json.loads((sdir / "site.json").read_text())
    c = parse_copy(sdir / "copy.md")
    errs, warns = [], []

    def need(key, minw=0):
        if key not in c or not c[key].strip():
            errs.append(f"copy.md missing block: {key}")
            return ""
        n = len(c[key].split())
        if minw and n < minw:
            errs.append(f"{key}: {n} words, needs {minw}+")
        return c[key]

    for k in ["meta_title", "meta_description", "hero_promise",
              "what_happens_when_you_call", "what_they_will_ask",
              "expect_intro_1", "expect_intro_2", "closing_cta",
              "services_summary", "about_summary"]:
        need(k)

    # --- symptoms (problem cards) --------------------------------------------
    symptoms = []
    sy_icons = [ICO["bolt"], ICO["eye"], ICO["warn"], ICO["wrench"]]
    i = 1
    while f"symptom_{i}" in c:
        body = c[f"symptom_{i}"]
        n = len(body.split())
        if not (SYMPTOM_WORDS[0] <= n <= SYMPTOM_WORDS[1]):
            errs.append(f"symptom_{i}: {n} words, must be {SYMPTOM_WORDS[0]}-{SYMPTOM_WORDS[1]}")
        # Each home-page teaser hands off to the service page that covers it in
        # full. symptom_service maps them in order.
        target = s.get("symptom_service", [])
        slug = target[i - 1] if i - 1 < len(target) else ""
        if not slug:
            errs.append(f"symptom_{i} has no service page in site.json symptom_service")
        link = next((o for o in s.get("services", []) if o["slug"] == slug), None)
        symptoms.append({"title": need(f"symptom_{i}_title"), "body": body,
                         "slug": slug,
                         "link_text": f"Read about {link['name'].lower()}" if link else "",
                         "icon": sy_icons[(i - 1) % len(sy_icons)]})
        i += 1
    if len(symptoms) < MIN_SYMPTOMS:
        errs.append(f"{len(symptoms)} symptom blocks, needs {MIN_SYMPTOMS}+")

    # --- local Q&As -----------------------------------------------------------
    faqs, i = [], 1
    while f"qa_{i}_question" in c:
        a = need(f"qa_{i}_answer", QA_WORDS)
        faqs.append({"q": c[f"qa_{i}_question"], "a": a})
        i += 1
    if len(faqs) < MIN_QAS:
        errs.append(f"{len(faqs)} local Q&As, needs {MIN_QAS}+")

    # --- repeating card groups ------------------------------------------------
    def group(prefix, icons, minn):
        out, i = [], 1
        while f"{prefix}_{i}" in c:
            out.append({"title": need(f"{prefix}_{i}_title"), "body": c[f"{prefix}_{i}"],
                        "icon": icons[(i - 1) % len(icons)]})
            i += 1
        if len(out) < minn:
            errs.append(f"{len(out)} {prefix} blocks, needs {minn}+")
        return out

    values = group("value", [ICO["chat"], ICO["pin"], ICO["bolt"], ICO["clock"]], 4)
    steps = group("step", [ICO["phone"], ICO["search"], ICO["cal"]], 3)
    factors = group("factor", [ICO["wrench"], ICO["ruler"], ICO["shield"], ICO["warn"]], 4)

    expects, i = [], 1
    ex_icons = [ICO["house"], ICO["search"], ICO["cal"], ICO["warn"]]
    while f"expect_{i}" in c:
        expects.append({"label": need(f"expect_{i}_label"), "body": c[f"expect_{i}"],
                        "icon": ex_icons[(i - 1) % len(ex_icons)]})
        i += 1
    if len(expects) < 4:
        errs.append(f"{len(expects)} expect items, needs 4+")

    # --- sourced local facts --------------------------------------------------
    facts = s.get("local_facts", [])
    if len(facts) < MIN_FACTS:
        errs.append(f"{len(facts)} local facts, needs {MIN_FACTS}+")
    for f in facts:
        for k in ("claim", "why_it_matters", "sources", "verified"):
            if not f.get(k):
                errs.append(f"local_fact {f.get('id','?')}: missing {k}")
        for u in f.get("sources", []):
            if not u.startswith("http"):
                errs.append(f"local_fact {f.get('id','?')}: bad source URL {u}")

    # --- phone ---------------------------------------------------------------
    disp = s.get("phone_display", "")
    ac = re.sub(r"\D", "", disp)[:3]
    if ac in {"800", "833", "844", "855", "866", "877", "888"}:
        errs.append(f"toll-free number {disp} -- local sites need a local area code")
    elif ac not in s.get("area_codes", []):
        errs.append(f"area code {ac} not in approved list {s.get('area_codes')}")
    if s.get("phone_status") == "PLACEHOLDER":
        warns.append(f"phone {disp} is a PLACEHOLDER -- swap for a live number before DNS")

    # --- tenant honesty ------------------------------------------------------
    t = s.get("tenant", {})
    pre = t.get("status") != "active"
    if pre:
        for fld in TENANT_FIELDS:
            if t.get(fld):
                errs.append(f"tenant.{fld} is set but tenant.status is not active")
        if s.get("schema", {}).get("local_business"):
            errs.append("LocalBusiness schema requested with no signed tenant")

    # --- render --------------------------------------------------------------
    env = Environment(loader=FileSystemLoader(str(TPL)), autoescape=select_autoescape(["html"]))
    env.filters["domain_of"] = domain_of

    hero_note = ("Upfront pricing · No obligation · Local "
                 f"{s['counties'][0]} County technician")
    disclosure = (
        f"This site is operated independently and is not itself a licensed contractor. "
        f"Calls are answered by a local {s['service_inline']} technician serving {s['city']}. "
        f"No pricing, licensing, insurance or review claims are made on this page, because no "
        f"specific provider is named on it yet. Verify license and insurance directly with any "
        f"provider before work begins."
    ) if pre else (
        f"{t.get('business_name')} &mdash; {s['service']} in {s['city']}, {s['state']}. "
        f"License {t.get('license_number')}. Verify license and insurance before work begins."
    )

    fact_titles = {
        f["id"]: f.get("title") or f["id"].replace("_", " ").title()
        for f in facts
    }

    work = [
        {"src": "assets/work-1.jpg", "caption": "Torsion spring replacement"},
        {"src": "assets/work-2.jpg", "caption": "Sectional door installation"},
        {"src": "assets/work-3.jpg", "caption": "Opener and rail repair"},
    ]

    ctx = dict(
        s=s, c=c, year=YEAR,
        robots="index, follow" if live else "noindex, nofollow",
        logo_mark=LOGO_MARK, hero_note=hero_note, disclosure=disclosure,
        values=values, steps=steps, factors=factors, expects=expects,
        symptoms=symptoms, faqs=faqs, work=work, fact_titles=fact_titles,
        facts_verified=max((f.get("verified", "") for f in facts), default=""),
        neighborhood_count=len(s.get("neighborhoods", [])),
        ico=ICO,
        **{f"ico_{k}": v for k, v in ICO.items()},
    )

    schema = None
    if s.get("schema", {}).get("faq_page") and faqs:
        schema = {"@context": "https://schema.org", "@type": "FAQPage",
                  "mainEntity": [{"@type": "Question", "name": q["q"],
                                  "acceptedAnswer": {"@type": "Answer", "text": q["a"]}}
                                 for q in faqs]}

    services = s.get("services", [])
    if len(services) < MIN_SERVICES:
        errs.append(f"{len(services)} service pages, needs {MIN_SERVICES}+")

    pages = {}
    pages["index.html"] = env.get_template("index.html").render(
        meta_title=c.get("meta_title", ""), meta_description=c.get("meta_description", ""),
        canonical_path="/", base="", schema_json=json.dumps(schema) if schema else None, **ctx)

    inner = env.get_template("inner.html")
    pages["services/index.html"] = inner.render(
        meta_title=f"{s['service']} Services in {s['city']}, {s['state']}",
        meta_description=f"The four {s['service_inline']} jobs that get confused with each other in {s['city']}.",
        canonical_path="/services/", base="../", schema_json=None,
        page_h1=f"{s['service']} Services", page_kicker=f"{s['city']}, {s['state']}",
        page_lede=c.get("services_summary", "").split(". ")[0] + ".",
        page_body=md.markdown(c.get("services_summary", "")),
        page_links=services, page_cards=factors, page_cards_eyebrow="What changes the job",
        page_cards_head=f"What affects {s['service_inline']} in {s['city']}", **ctx)

    pages["about/index.html"] = inner.render(
        meta_title=f"About &mdash; {s['service']} in {s['city']}, {s['state']}",
        meta_description=f"Why this page covers {s['city']} only.",
        canonical_path="/about/", base="../", schema_json=None,
        page_h1="About This Page", page_kicker=f"{s['city']} only",
        page_lede=f"One city, one trade, written for {s['city']}.",
        page_body=md.markdown(c.get("about_summary", "")),
        page_cards=None, **ctx)

    contact_body = (
        f"<p>Call <a href=\"tel:{s['phone_tel']}\">{s['phone_display']}</a> and describe what the "
        f"door is doing. There is no form on this page on purpose &mdash; a garage door problem is "
        f"faster to describe out loud than to type.</p>"
        f"<p>Coverage is {s['city']} and the surrounding {' and '.join(s['counties'])} County "
        f"communities, including {', '.join(s.get('neighborhoods', [])[:-1])} and "
        f"{s.get('neighborhoods', [''])[-1]}.</p>"
        f"<p><strong>If a spring has snapped or the door is off its track:</strong> unplug the "
        f"opener, do not try to lift the door, and say so when you call.</p>"
    )
    pages["contact/index.html"] = inner.render(
        meta_title=f"Contact &mdash; {s['service']} in {s['city']}, {s['state']}",
        meta_description=f"Call a {s['city']} {s['service_inline']} technician.",
        canonical_path="/contact/", base="../", schema_json=None,
        page_h1="Contact", page_kicker=s["phone_display"],
        page_lede="One number, and the four things worth having ready when you call.",
        page_body=contact_body, page_cards=None, page_expects=expects, **ctx)

    for key in ("hero_accent", "trust_third"):
        if not s.get(key):
            errs.append(f"site.json is missing {key!r} -- it appears in the H1 or the trust band")

    # --- service pages -------------------------------------------------------
    svc_tpl = env.get_template("service.html")
    for o in services:
        key = o["slug"].replace("-", "_")
        lede = c.get(f"svc_{key}_lede", "")
        body = c.get(f"svc_{key}_body", "")
        if not lede or not body:
            errs.append(f"service {o['slug']}: missing svc_{key}_lede or svc_{key}_body in copy.md")
            continue
        html = svc_tpl.render(
            meta_title=f"{o['h1']} in {s['city']}, {s['state']}",
            meta_description=lede.split(". ")[0][:155] + ".",
            canonical_path=f"/{o['slug']}/", base="../", schema_json=None,
            svc=o, svc_lede=lede, svc_body=md.markdown(body), **ctx)
        wc = len(visible_words(html))
        if not (SERVICE_WORDS[0] <= wc <= SERVICE_WORDS[1]):
            errs.append(f"service {o['slug']}: {wc} visible words, must be "
                        f"{SERVICE_WORDS[0]}-{SERVICE_WORDS[1]}")
        pages[f"{o['slug']}/index.html"] = html

    # --- post-render guards ---------------------------------------------------
    for page_name, page_html in pages.items():
        check_no_absolute_paths(page_html, page_name, errs)
    check_no_absolute_paths((TPL / "assets" / "theme.css").read_text(), "theme.css", errs)

    home_words = visible_words(pages["index.html"])
    n = len(home_words)
    if not (HOME_WORDS[0] <= n <= HOME_WORDS[1]):
        errs.append(f"home page {n} visible words, must be {HOME_WORDS[0]}-{HOME_WORDS[1]}")

    if pre:
        low = " ".join(home_words).lower()
        for phrase in BANNED_PRE_TENANT:
            if phrase in low:
                errs.append(f"unverifiable pre-tenant claim on page: '{phrase}'")

    # cross-site duplicate prose: no two sites may share SHINGLE consecutive words
    if corpus is not None:
        authored = " ".join(str(v) for k, v in sorted(c.items()))
        low = re.findall(r"[a-z0-9']+", authored.lower())
        mine = {" ".join(low[i:i + SHINGLE]) for i in range(len(low) - SHINGLE + 1)}
        for other, theirs in corpus.items():
            hits = mine & theirs
            if hits:
                errs.append(f"copy.md shares {len(hits)} {SHINGLE}-word runs with {other}, "
                            f"e.g. \"{sorted(hits)[0][:90]}...\"")
        corpus[domain] = mine

    # --- report / write ------------------------------------------------------
    label = f"{domain} -- home {n} words, {len(symptoms)} symptoms, {len(faqs)} local Q&As, {len(facts)} sourced facts"
    for w in warns:
        print(f"  [WARN] {w}")
    if errs:
        print(f"[FAIL] {label}")
        for e in errs:
            print(f"  [ERROR] {e}")
        return False
    print(f"[PASS] {label}")
    for name in sorted(pages):
        print(f"         {len(visible_words(pages[name])):5d} words  /{name.replace('index.html', '')}")

    if not check_only:
        out = DIST / domain
        if out.exists():
            shutil.rmtree(out)
        (out / "assets").mkdir(parents=True)
        for rel, html in pages.items():
            p = out / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(html)
        shutil.copy(TPL / "assets" / "theme.css", out / "assets" / "theme.css")
        (out / "assets" / "favicon.svg").write_text(FAVICON)
        for img in (sdir / "assets").glob("*"):
            shutil.copy(img, out / "assets" / img.name)
    return True


def check_no_absolute_paths(html: str, page: str, problems: list) -> None:
    """Root-relative asset and nav paths work on the live domain but break the
    moment the site is served from a subfolder, which is exactly what every
    preview does. A page that 404s its own stylesheet looks like raw HTML, so
    this is a hard failure rather than a warning."""
    for pat in ('href="/assets/', "href='/assets/", 'src="/assets/', "src='/assets/",
                'url("/assets/', "url('/assets/", 'href="/services/', 'href="/about/',
                'href="/contact/'):
        if pat in html:
            problems.append(f"{page}: absolute path {pat!r} -- must be relative to the page")
    # href="/" as a home link is the same bug in a shorter form.
    if 'href="/"' in html:
        problems.append(f"{page}: absolute home link href=\"/\" -- use the relative base")


def main():
    args = [a for a in sys.argv[1:]]
    live = "--live" in args
    check = "--check-only" in args
    targets = [a for a in args if not a.startswith("--")]
    if not targets:
        targets = sorted(p.name for p in SITES.iterdir() if (p / "site.json").exists())
    corpus, ok, drafts = {}, True, []
    for d in targets:
        if is_draft(d):
            drafts.append(d)
            continue
        ok = build(d, live=live, check_only=check, corpus=corpus) and ok
    if drafts:
        print(f"\n{len(drafts)} site(s) skipped as unwritten drafts "
              f"(no copy, no sourced facts). `python3 scaffold.py --status` "
              f"lists what each one still needs.")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
