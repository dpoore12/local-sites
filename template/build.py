#!/usr/bin/env python3
"""
LOCAL SITE NETWORK — build + guard

  python template/build.py                    # build every site in sites/
  python template/build.py <domain>           # build one
  python template/build.py --check-only       # run guards, write nothing

The template is identical across every site. Everything a visitor reads as
prose comes from that site's copy.md. The build FAILS rather than shipping a
page that is a name-swap of another page.
"""
import json, re, sys, html, datetime, pathlib, shutil, collections

ROOT   = pathlib.Path(__file__).resolve().parent.parent
TPL    = ROOT / "template"
SITES  = ROOT / "sites"
DIST   = ROOT / "dist"
YEAR   = datetime.date.today().year

from jinja2 import Environment, FileSystemLoader, select_autoescape
import markdown as md

# ---------------------------------------------------------------- guard config
REQUIRED_BLOCKS = [
    "meta_title", "meta_description", "hero_promise",
    "what_happens_when_you_call", "what_they_will_ask",
    "closing_cta", "services_summary", "about_summary",
]
MIN_WORDS = {
    "hero_promise": 35, "what_happens_when_you_call": 85,
    "what_they_will_ask": 75, "closing_cta": 25,
    "services_summary": 70, "about_summary": 70,
}
SYMPTOM_MIN, SYMPTOM_MAX = 105, 175   # words per symptom block
QA_MIN                   = 55         # words per answer
HOME_MIN, HOME_MAX       = 900, 1250  # visible body words on Home
MIN_SYMPTOMS, MIN_QAS    = 4, 3
MIN_LOCAL_FACTS          = 2
SHINGLE                  = 15         # no two sites may share N consecutive words
TOLLFREE                 = re.compile(r"\b(800|833|844|855|866|877|888)\b")

FABRICATED = [
    "years of experience", "licensed and insured", "family owned and operated",
    "5-star", "five star", "our customers say", "trusted by", "voted best",
    "a+ rating", "satisfaction guaranteed", "over 1,000 happy",
]

# ---------------------------------------------------------------- icons + logo
ICONS = {
"icon_phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21.5 16.9v2.6a1.7 1.7 0 0 1-1.9 1.7 17 17 0 0 1-7.4-2.6 16.7 16.7 0 0 1-5.1-5.1A17 17 0 0 1 4.5 6a1.7 1.7 0 0 1 1.7-1.9h2.6a1.7 1.7 0 0 1 1.7 1.5c.1.9.3 1.7.6 2.5a1.7 1.7 0 0 1-.4 1.8l-1.1 1.1a13.7 13.7 0 0 0 5.1 5.1l1.1-1.1a1.7 1.7 0 0 1 1.8-.4c.8.3 1.6.5 2.5.6a1.7 1.7 0 0 1 1.4 1.7z"/></svg>',
"icon_pin":   '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s7-5.7 7-11a7 7 0 1 0-14 0c0 5.3 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/></svg>',
"icon_bolt":  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 2 4.5 13.5H11l-1 8.5 8.5-11.5H12l1-8.5z"/></svg>',
"icon_check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6.5 9.5 17 4 11.5"/></svg>',
}
# Logo: garage silhouette with paneled door. Geometric, works at 24px.
LOGO = ('<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<path d="M3 28V13L16 4.5 29 13v15"/>'
        '<path d="M9 28V17.5h14V28"/><path d="M9 21.5h14M9 24.75h14"/></svg>')
FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
           '<rect width="32" height="32" rx="6" fill="#a8442a"/>'
           '<g fill="none" stroke="#fbf8f3" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">'
           '<path d="M5 27V13.5L16 6l11 7.5V27"/><path d="M10.5 27V17.5h11V27"/>'
           '<path d="M10.5 21h11M10.5 24h11"/></g></svg>')

# ---------------------------------------------------------------- helpers
def parse_copy(path):
    """copy.md -> {block_key: text}. Blocks are '## key' then prose."""
    blocks, key, buf = {}, None, []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            if key: blocks[key] = "\n".join(buf).strip()
            key, buf = line[3:].strip(), []
        elif key is not None:
            buf.append(line)
    if key: blocks[key] = "\n".join(buf).strip()
    return {k: v for k, v in blocks.items() if v}

def words(t):
    return len(re.findall(r"[A-Za-z0-9'’\-]+", t or ""))

def norm(t):
    return re.findall(r"[a-z0-9']+", (t or "").lower())

def shingles(t, n=SHINGLE):
    w = norm(t)
    return {" ".join(w[i:i+n]) for i in range(max(0, len(w)-n+1))}

# ---------------------------------------------------------------- load one site
def load(dirpath):
    s = json.loads((dirpath / "site.json").read_text(encoding="utf-8"))
    c = parse_copy(dirpath / "copy.md")

    syms = []
    for i in range(1, 9):
        b, t = c.get(f"symptom_{i}"), c.get(f"symptom_{i}_title")
        if b and t: syms.append({"title": t, "body": b})
    qas = []
    for i in range(1, 9):
        q, a = c.get(f"qa_{i}_question"), c.get(f"qa_{i}_answer")
        if q and a: qas.append({"question": q, "answer": a})

    home_prose = " ".join([
        c.get("hero_promise", ""), c.get("what_happens_when_you_call", ""),
        c.get("what_they_will_ask", ""),
        *[x["body"] for x in syms], *[x["answer"] for x in qas],
        c.get("closing_cta", ""),
    ])
    return s, c, syms, qas, home_prose

# ---------------------------------------------------------------- guards
def guard(name, s, c, syms, qas, home_prose):
    err, warn = [], []

    for k in REQUIRED_BLOCKS:
        if k not in c: err.append(f"missing required block: {k}")
    for k, m in MIN_WORDS.items():
        if k in c and words(c[k]) < m:
            err.append(f"{k}: {words(c[k])} words, minimum {m}")

    if len(syms) < MIN_SYMPTOMS: err.append(f"{len(syms)} symptom blocks, minimum {MIN_SYMPTOMS}")
    if len(qas)  < MIN_QAS:      err.append(f"{len(qas)} local Q&As, minimum {MIN_QAS}")

    for i, x in enumerate(syms, 1):
        w = words(x["body"])
        if not (SYMPTOM_MIN <= w <= SYMPTOM_MAX):
            err.append(f"symptom_{i}: {w} words, needs {SYMPTOM_MIN}-{SYMPTOM_MAX}")
    for i, x in enumerate(qas, 1):
        if words(x["answer"]) < QA_MIN:
            err.append(f"qa_{i}_answer: {words(x['answer'])} words, minimum {QA_MIN}")

    hw = words(home_prose)
    if not (HOME_MIN <= hw <= HOME_MAX):
        err.append(f"Home body: {hw} visible words, needs {HOME_MIN}-{HOME_MAX}")

    # phone
    if TOLLFREE.search(s.get("phone_display", "")):
        err.append("toll-free number on a local site")
    ac = re.sub(r"\D", "", s.get("phone_display", ""))[:3]
    if ac not in s.get("area_codes", []):
        err.append(f"phone area code {ac} not in approved area codes {s.get('area_codes')}")
    if s.get("phone_status") == "PLACEHOLDER":
        warn.append("phone is a PLACEHOLDER — must be a live tracking number before DNS goes live")

    # local facts
    facts = s.get("local_facts", [])
    if len(facts) < MIN_LOCAL_FACTS:
        err.append(f"{len(facts)} local facts, minimum {MIN_LOCAL_FACTS}")
    for f in facts:
        if not f.get("sources"): err.append(f"local fact '{f.get('id')}' has no source URL")
        if not f.get("why_it_matters"): err.append(f"local fact '{f.get('id')}' has no practical relevance")
        if not f.get("verified"): err.append(f"local fact '{f.get('id')}' has no verification date")

    # pre-tenant honesty
    t = s.get("tenant", {})
    if t.get("status") == "none":
        for field in ("business_name", "license_number", "years_in_business", "reviews", "family_owned", "veteran_owned"):
            if t.get(field):
                err.append(f"pre-tenant site claims tenant.{field} — no tenant is signed")
        if s.get("schema", {}).get("local_business"):
            err.append("LocalBusiness schema enabled with no tenant")
        low = home_prose.lower()
        for phrase in FABRICATED:
            if phrase in low:
                err.append(f"unverifiable trust claim in copy: '{phrase}'")
    return err, warn

def cross_site_duplicates(corpus):
    """corpus: {domain: home_prose}. Returns list of (a, b, count, sample)."""
    idx, hits = collections.defaultdict(set), []
    for dom, prose in corpus.items():
        for sh in shingles(prose):
            idx[sh].add(dom)
    pairs = collections.Counter()
    samples = {}
    for sh, doms in idx.items():
        if len(doms) > 1:
            for a in doms:
                for b in doms:
                    if a < b:
                        pairs[(a, b)] += 1
                        samples.setdefault((a, b), sh)
    for (a, b), n in pairs.items():
        hits.append((a, b, n, samples[(a, b)]))
    return hits

# ---------------------------------------------------------------- render
def render(dirpath, s, c, syms, qas, live=False):
    env = Environment(loader=FileSystemLoader(str(TPL)),
                      autoescape=select_autoescape(["html"]), trim_blocks=True, lstrip_blocks=True)
    ctx = dict(s=s, c=c, symptoms=syms, qas=qas, year=YEAR, live=live,
               logo_svg=LOGO, **{k: v for k, v in ICONS.items()})
    for k in ("logo_svg", *ICONS):
        from markupsafe import Markup
        ctx[k] = Markup(ctx[k])

    out = DIST / s["domain"]
    if out.exists(): shutil.rmtree(out)
    (out / "assets").mkdir(parents=True, exist_ok=True)
    shutil.copy2(TPL / "assets" / "theme.css", out / "assets" / "theme.css")
    (out / "assets" / "favicon.svg").write_text(FAVICON, encoding="utf-8")

    # deduped, human-readable source list
    seen, source_list = set(), []
    for f in s.get("local_facts", []):
        for u in f["sources"]:
            if u in seen: continue
            seen.add(u)
            host = re.sub(r"^https?://(www\.)?", "", u).split("/")[0]
            tail = u.rstrip("/").rsplit("/", 1)[-1]
            label = host if (not tail or tail == host or len(tail) > 34) else f"{host} — {tail.replace('-', ' ').replace('.pdf','')[:34]}"
            source_list.append({"url": u, "label": label})
    ctx["source_list"] = source_list

    faq_schema = json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q["question"],
                        "acceptedAnswer": {"@type": "Answer", "text": q["answer"]}} for q in qas]
    }, ensure_ascii=False)

    # HOME
    (out / "index.html").write_text(env.get_template("index.html").render(
        **ctx, page_title=c["meta_title"], page_description=c["meta_description"],
        page_path="/", schema_blocks=[faq_schema] if s.get("schema", {}).get("faq_page") else []
    ), encoding="utf-8")

    # SERVICES
    svc_body = md.markdown(
        f"## What the four jobs actually are\n\n{c['services_summary']}\n\n"
        + "\n\n".join(f"### {x['title']}\n\n{x['body']}" for x in syms)
    )
    _write(env, out / "services" / "index.html", ctx,
           f"{s['service']} Services in {s['city']}, {s['state']}",
           f"{s['service']} services in {s['city']}, {s['state']}: spring replacement, opener repair, track and roller work, panel and full door replacement.",
           "/services/", f"{s['service']} Services in {s['city']}", svc_body)

    # ABOUT — carries the sourced local facts, which exist on no other site
    fact_md = "\n\n".join(
        f"### {f['claim']}\n\n{f['why_it_matters']}\n\n"
        + "Source: " + ", ".join(
            f"[{re.sub(r'^https?://(www.)?', '', u).split('/')[0]}]({u})" for u in f["sources"])
        + f"  \nVerified {f['verified']}."
        for f in s.get("local_facts", []))
    _write(env, out / "about" / "index.html", ctx,
           f"About This {s['city']} {s['service']} Page",
           f"Why this page is {s['city']}-only, and the local details that change how {s['service_inline']} gets handled here.",
           "/about/", f"About this {s['city']} page",
           md.markdown(f"## Why this page exists\n\n{c['about_summary']}\n\n## {s['city']} details that change the job\n\n") + md.markdown(fact_md))

    # CONTACT
    contact_md = md.markdown(
        f"## Call {s['phone_display']}\n\n"
        f"One number. No form, no phone menu, no callback queue. Describe what the door is doing and you will get "
        f"routed to a {s['service_inline']} technician working in {s['city']} and the surrounding "
        f"{' and '.join(s['counties'])} County areas.\n\n"
        f"## Say these four things\n\n"
        f"- Whether the door is one solid slab or horizontal sections\n"
        f"- Where the springs are: above the opening, or along the ceiling\n"
        f"- Roughly when the house was built\n"
        f"- Whether the door is open, closed, or stuck part way\n\n"
        f"## Areas covered\n\n" + ", ".join(s["neighborhoods"]) + f", and the rest of {s['city']}.\n\n"
        f"## Not a {s['service_inline']} call\n\n"
        f"Gas smell, live electrical wiring, or a structure that looks like it is failing: call 911 or your utility. "
        f"Not this number.")
    _write(env, out / "contact" / "index.html", ctx,
           f"Contact — {s['service']} in {s['city']}, {s['state']}",
           f"Call {s['phone_display']} for {s['service_inline']} in {s['city']}, {s['state']}. What to have ready before you call.",
           "/contact/", f"Contact a {s['city']} technician", contact_md)
    return out

def _write(env, path, ctx, title, desc, page_path, h1, body):
    path.parent.mkdir(parents=True, exist_ok=True)
    from markupsafe import Markup
    path.write_text(env.get_template("inner.html").render(
        **ctx, page_title=title, page_description=desc, page_path=page_path,
        h1=h1, body=Markup(body), schema_blocks=[]), encoding="utf-8")

# ---------------------------------------------------------------- main
def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check_only = "--check-only" in sys.argv
    live = "--live" in sys.argv
    dirs = [SITES / a for a in args] if args else sorted(d for d in SITES.iterdir() if d.is_dir())

    corpus, loaded, failed = {}, [], 0
    for d in dirs:
        s, c, syms, qas, prose = load(d)
        err, warn = guard(d.name, s, c, syms, qas, prose)
        corpus[s["domain"]] = prose
        loaded.append((d, s, c, syms, qas, prose))
        tag = "FAIL" if err else "PASS"
        print(f"\n[{tag}] {s['domain']}  —  Home body {words(prose)} words, "
              f"{len(syms)} symptoms, {len(qas)} local Q&As, {len(s.get('local_facts',[]))} sourced facts")
        for e in err:  print(f"   ERROR  {e}")
        for w in warn: print(f"   WARN   {w}")
        if err: failed += 1

    dups = cross_site_duplicates(corpus)
    if dups:
        print("\n[FAIL] shared phrasing across sites:")
        for a, b, n, sample in dups:
            print(f"   {a} <-> {b}: {n} shared {SHINGLE}-word runs, e.g. \"{sample}\"")
        failed += 1
    elif len(corpus) > 1:
        print(f"\n[PASS] no shared {SHINGLE}-word run across {len(corpus)} sites")

    if failed:
        print(f"\n{failed} failure(s). Nothing built."); sys.exit(1)
    if check_only:
        print("\nAll guards passed. --check-only, nothing written."); return

    for d, s, c, syms, qas, _ in loaded:
        out = render(d, s, c, syms, qas, live=live)
        print(f"built  {out.relative_to(ROOT)}  (robots: {'index' if live else 'noindex'})")

if __name__ == "__main__":
    main()
