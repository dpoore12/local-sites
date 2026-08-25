#!/usr/bin/env python3
"""
QC pass for the 83-site portfolio.

Reads the BUILT html in dist/ (what a visitor actually sees) and flags:
  mechanics  - double spaces, doubled words, spacing around punctuation,
               unbalanced brackets/quotes, leaked markdown, lowercase
               sentence starts, missing space after a period
  structure  - h1 count, heading level jumps, empty headings/paragraphs,
               subhead count on long pages, orphan headings (heading with
               no body under it), duplicate headings on one page
  flow       - runaway sentences, runaway paragraphs, repeated paragraph
               openers, a word used too many times on one page,
               single-sentence paragraph runs
  claims     - license/review/years-in-business claims, a price we charge
  spelling   - unknown words, with a project allowlist

Usage:
  python3 qc.py                 # all phase-2 sites
  python3 qc.py <domain> ...    # specific sites
  python3 qc.py --all-phases    # include phase-1 sites too
  python3 qc.py --csv out.csv   # write a flat findings file
"""
import sys, os, re, json, glob, csv, html as htmllib, collections

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")

# ---------------------------------------------------------------- allowlist
ALLOW = set("""
hvac ac dui uas hoa nap seo url urls faq faqs
condenser condensers evaporator evaporators refrigerant refrigerants
capacitor capacitors microfarad microfarads contactor contactors
plenum superheat subcooling thermostat thermostats btu btus seer
ductwork ducted rooftop crawlspace slab slabs caliche
underpinning underpinnings helical piering pier piers shim shims
grout grouted grouting subfloor subfloors backerboard drywall
flashing soffit soffits fascia eaves downspout downspouts gutter gutters
shingle shingles underlayment sheathing joist joists rafter rafters
lintel weatherstripping weatherstrip caulk caulking
torsion counterbalance jamb jambs mullion muntin sill sills
polybutylene pex cpvc abs galvanized cleanout cleanouts
hydrostatic exfiltration infiltration
karst limestone dolomite alluvial alluvium montmorillonite smectite
vertisol vertisols shrink swell escarpment
monsoon monsoonal microclimate microclimates
statute statutes statutory tolling tolled tolls prejudgment
comparative contributory joint several
subrogation uninsured underinsured um uim bi pd
deposition depositions discovery interrogatories subpoena subpoenas
adjuster adjusters lienholder liens lien
misdemeanor felony arraignment arraignments plea pleas
breathalyzer intoxilyzer implied
custodial noncustodial parenting
decedent decedents survivorship
premises quadriplegia paraplegia
homeowner homeowners renter renters landlord landlords
walkthrough walkthroughs punchlist
recode recodes retrofit retrofitted retrofits changeout changeouts
neighborhoods citywide countywide statewide nationwide
noaa usda usgs epa cpsc dasma nahb bls osha dhsmv fdot fdle ercot
jea derp cvb dca cpuc nist
rcw orc krs crs stat fla tex colo civ proc
llc inc co
""".split())

# ---------------------------------------------------------------- helpers
def strip_html(h):
    h = re.sub(r"(?is)<(script|style|svg|noscript)\b.*?</\1>", " ", h)
    h = re.sub(r"(?s)<!--.*?-->", " ", h)
    h = re.sub(r"(?i)<br\s*/?>", "\n", h)
    h = re.sub(r"(?i)</(p|li|h[1-6]|div|section|tr|td)>", "\n", h)
    h = re.sub(r"<[^>]+>", " ", h)
    h = htmllib.unescape(h)
    h = re.sub(r"[ \t\u00a0]+", " ", h)
    return "\n".join(l.strip() for l in h.split("\n"))

BLOCK = "h1|h2|h3|h4|h5|h6|p|li|td|th|dd|dt|figcaption|blockquote"
# Innermost blocks only. Requiring that no block tag opens inside the match
# stops a <li> wrapping an <h3> from being read as one merged block, while
# still letting that inner <h3> be found on its own.
BLOCK_RE = re.compile(
    r"(?is)<(%s)\b[^>]*>((?:(?!<(?:%s)\b).)*?)</\1>" % (BLOCK, BLOCK), re.S)

LABEL_BLOCKS = set()

def visible_blocks(h):
    """(tag, text) for every innermost block element, in document order."""
    h2 = re.sub(r"(?is)<(script|style|svg|noscript|template)\b.*?</\1>", " ", h)
    h2 = re.sub(r"(?s)<!--.*?-->", " ", h2)
    out = []
    for m in BLOCK_RE.finditer(h2):
        # Inline tags carry no word boundary of their own. Replacing them with a
        # space turns "<a>cited page</a>." into "cited page ." and produces a
        # phantom space-before-punctuation on every sentence that ends in a
        # citation link, so drop them outright and only space out real breaks.
        inner = re.sub(r"(?is)</?(a|em|strong|b|i|u|span|code|abbr|sup|sub|small|cite|q|mark|time|var|kbd|samp)\b[^>]*>", "", m.group(2))
        txt = htmllib.unescape(re.sub(r"<[^>]+>", " ", inner))
        txt = re.sub(r"[ \t\u00a0]+", " ", txt).strip()
        tag = m.group(1).lower()
        if LINK_ONLY.match(m.group(2).strip()):
            LABEL_BLOCKS.add(txt)
        out.append((tag, txt))
    return out

# A block whose whole content is one link is a source label, not a sentence.
LINK_ONLY = re.compile(r"(?is)^\s*<a\b[^>]*>.*?</a>\s*$")
CITEY = re.compile(r"(?i)(?:read \d{4}-\d\d-\d\d|, read |^sources?:|^source\b|"
                   r"\b(?:\w+\.)+(?:com|org|gov|net|edu|us|ca)\b|^read about\b|"
                   r"^\s*\u00b7|\u00b7\s*$)")
def is_citation_ish(t):
    """Source lines, domain lists and 'Read about X' crosslinks are label text,
    not prose. They legitimately have no terminal punctuation."""
    return bool(CITEY.search(t)) or t.count("\u00b7") >= 1 or t in LABEL_BLOCKS

def sentences(t):
    t = re.sub(r"\b([A-Z])\.\s*", r"\1 ", t)          # initials
    t = re.sub(r"\b(No|Nos|Mr|Mrs|Ms|Dr|St|Ave|Rd|Inc|Co|Fla|Tex|Colo|Stat|Sec|Art|vs|v|approx|est|e\.g|i\.e|U\.S|D\.C)\.",
               r"\1<DOT>", t, flags=re.I)
    t = re.sub(r"(\d)\.(\d)", r"\1<DOT>\2", t)
    # A sentence that ends inside a quotation puts the period before the closing
    # mark, so the plain lookbehind misses the break and two sentences get
    # measured as one runaway.
    parts = re.split(r"(?<=[.!?])\s+(?=[\"'\u201c\u2018(]?[A-Z0-9])"
                     r"|(?<=[.!?][\"'\u201d\u2019])\s+(?=[\"'\u201c\u2018(]?[A-Z0-9])", t)
    return [p.replace("<DOT>", ".").strip() for p in parts if p.strip()]

WORD = re.compile(r"[A-Za-z][A-Za-z'\u2019-]*")
def words(t): return WORD.findall(t)

STOP = set("""a an the and or but if then than that this these those of to in on at by for with from as is are was were be been being
it its it's they them their there here he she his her you your we our us i me my not no nor so such can could would should will
what which who whom whose when where why how all any both each few more most other some only own same too very just about after
before during under over again once out up down off above below between into through do does did doing have has had having
one two three four five six seven eight nine ten first second next last also because while until unless whether though although""".split())

# ---------------------------------------------------------------- checks
BANNED_CLAIM = [
 (r"\b(?:we|our team|our techs?|our crews?|our attorneys?|our lawyers?)\b[^.]{0,60}\b(?:licensed|certified|insured|bonded|accredited|award[- ]winning|top[- ]rated|best[- ]rated|five[- ]star|5[- ]star)\b", "claims a credential for us"),
 (r"\b(?:licensed and insured|fully licensed|state licensed|board certified|BBB accredited|A\+ rating)\b", "credential claim"),
 (r"\b(?:\d+\+?|over \d+|more than \d+)\s+years?\s+(?:of\s+)?(?:experience|in business|serving)\b", "years-in-business claim"),
 (r"\b(?:\d[\d,]*\+?\s+(?:five[- ]star|5[- ]star|customer|verified|google|online|happy[- ]customer)\s+(?:reviews?|ratings?)|rated \d(?:\.\d)? (?:stars?|out of))\b", "review/rating claim"),
 (r"\b(?:thousands|hundreds) of (?:satisfied )?(?:customers|clients|homeowners)\b", "volume claim"),
 (r"\bwe (?:charge|offer|bill)\b[^.]{0,40}\$\s?\d", "states a price we charge"),
 (r"\b(?:our|we) (?:price|rate|fee)s? (?:start|starts|begin|begins) at\b", "states a price we charge"),
 (r"\b(?:free estimate|no obligation quote|call now for a free)\b", "offer language"),
 (r"\b(?:we|our team|our crews?|our techs?)\s+(?:fully\s+)?guarantee\b", "we-guarantee claim"),
 (r"\b(?:satisfaction|results?|money[- ]back|lowest price|same[- ]day)\s+guarantee[ds]?\b", "guarantee claim"),
 (r"\bguaranteed\s+(?:results?|outcome|approval|savings|dismissal|settlement)\b", "guaranteed-outcome claim"),
 (r"\bour\s+(?:\w+\s+){0,2}(?:guarantee|warranty)\b", "our-guarantee claim"),
 (r"\bwe (?:have|are) (?:been )?(?:family[- ]owned|locally owned|serving)\b", "identity claim"),
]

LEAKED_MD = [
 (r"(?m)^\s{0,3}#{1,6}\s", "unrendered markdown heading"),
 (r"\*\*[^*\n]{2,80}\*\*", "unrendered bold"),
 (r"(?<![\w:])\[[^\]\n]{2,80}\]\([^)\n]{2,200}\)", "unrendered markdown link"),
 (r"(?m)^\s{0,3}[-*]\s{1,3}\S", "unrendered list bullet"),
 (r"\{\{|\}\}|\{%", "unrendered template tag"),
 (r"(?m)^\s*(?:None|nan|NaN|null|undefined)\s*$", "placeholder leaked"),
 (r"\bNone\b(?!\s+(?:of|in|is|are|was|were|apply|applies|applied|were|had|have|has|so|other|the|at|on|for|to|yet|but|and))", "bare 'None' leaked"),
 (r"\b(?:nan|undefined|TODO|TKTK|XXX|Lorem ipsum|PLACEHOLDER|FIXME)\b", "placeholder leaked"),
]

ALLOW |= {
 # trade and building vocabulary
 "upsell","upsells","wastewater","stormwater","repipe","repipes","repiping",
 "reinspection","reinspections","flashings","flashing","derated","derate",
 "reroofing","reroof","sideroom","headroom","rebar","respooled","respool",
 "runtime","accessorial","windborne","curbless","lineset","linesets",
 "woodgrain","repouring","repour","resized","rollout","screenshots",
 "multi","nonattainment","nonadversary","unvaccinated","backflow","backdraft",
 "downspout","downspouts","soffit","soffits","fascia","underlayment",
 "weatherhead","weatherization","ductwork","subfloor","subflooring",
 "waterproofing","dehumidification","condensate","evaporator","refrigerant",
 "thermostatic","hardscape","hardscaping","regrading","regrade","underpinning",
 "shoring","joist","joists","truss","trusses","parging","efflorescence",
 "sistering","kerf","mitered","caulked","recaulk","regrout","regrouting",
 "shutoff","cleanout","cleanouts","hydrojetting","jetting","descaling",
 "trenchless","sewerline","gasline","electrification","panelboard",
 # weather and geography
 "derecho","derechos","supercell","supercells","dryline","microburst",
 "microbursts","evapotranspiration","subsidence","karst","caliche",
 # legal and civic vocabulary
 "arraignment","subrogation","comparative","noneconomic","prejudgment",
 "postjudgment","tortfeasor","tortfeasors","decedent","decedents",
 "impleader","joinder","venued","recusal","remittitur","voir",
 "prescriptive","peremption","peremptory","adjudicative","dispositive",
 "unliquidated","liquidated","indemnitor","indemnitee","subrogee",
}

ALLOW |= {
 "uninspected","remodelers","remodeler","frameless","templated","roofline",
 "rooflines","attaches","timelines","copetitioner","copetitioners","derating",
 "unconscionability","unconscionable","rulebook","parte","pipefitters",
 "pipefitter","workarounds","workaround","tankless","hubbed","daylighting",
 "subsoils","subsoil","reinstallation","subrogated","requestor","requestors",
 "jobsite","jobsites","worksite","worksites","presuit","litem","unspooled",
 "unspools","unspool","footpeg","footpegs","onsite","dewatering","dewaters",
 "dewater","phasedown","installable","oversizing","oversize","onboard",
 "arterials","arterial","retroreflective","pendleton","offutt","accessorials",
 "subcool","subcooling","nonrenew","nonrenewal","metadata","townhome",
 "townhomes","indigency","bayfront","upslope","repointed","repointing",
 "resecures","resecure","flushable","jetter","jetters","presidentially",
 "telematics","misdescribed","misdescribe",
}

ALLOW |= {"buildable","drainfield","drainfields","setpoint","setpoints",
 "assistive","misadjusted","misadjust","repost","reposts","rideshare",
 "rideshares","voicemail","voicemails"}

SUBJECT_STOP = {
 "california","texas","florida","colorado","georgia","arizona","nevada",
 "louisiana","alabama","tennessee","carolina","virginia","michigan","minnesota",
 "missouri","kansas","kentucky","arkansas","nebraska","washington","ohio",
 "pennsylvania","county","city","state","repair","service","services","lawyer",
 "attorney","claim","claims","injury","accident","garage","plumbing","plumber",
 "roof","roofing","bathroom","shower","furnace","foundation","gutter","gutters",
 "moving","movers","remodel","remodeling","window","windows","appliance",
 "install","installation","replacement","damage","water","court","insurance",
 "permit","fee","fees","cost","costs","price","prices","pricing","home","house",
 "system","systems","door","doors","spring","springs","opener","openers",
 "driver","vehicle","crash","collision","defense","charge","license","case",
 "cases","law","legal","rule","rules","code","local","area","market",
}

ALLOW |= {"prima","facie","nonfleet","setoff","setoffs","wantonness","wanton",
 "vult","psf","lbf","glazed","backwater","lateral","laterals","jetting",
 "prescriptive","delictual","interlock","spoliation","intestacy","subrogation",
 "underinsured","uninsured","noneconomic","arraigned","arraignment"}

# Real terms the dictionary lacks: trade jargon, legal Latin, soil science,
# municipal vocabulary and ordinary un-/non-/re- compounds. All verified by hand.
ALLOW |= set("""
admin antisubrogation apps arbitrations arborist arrestee auditable backfilled backfills batts
biocides borescope breakpoint buildout callout capitated centerline chargemaster checkboxes clearable
cnic cnrma comp contendere correlator counterflashing countertop damnum dataset decisionmaking
deemer delaminated dissolutions downslope driveaway durational encapsulant euthanized eyewall
factfinder farmworker farmworkers fatbergs fide flangeway flangeways flatwork gasketed gasketing
geolocation geotechnical glovebox hazmat inspectable intrafamily intraspinal ipsa knockovers
liberative licensure limine lookback lookup microamps microchipping montmorillonitic motorsports
nolle nonconditioned nonfiling nonmarital nonparties nonparty nonpecuniary novo offsite onboarding
overcollected paralic paralithic parentis paver payor picocuries pinholed plat ponding postmile
praecipe predeath preprinted prosequi ratemaking rebalance reframing relatch relatched relatching
releveling rematched remediate remediated remediator repiped repurposed requestable resize
retellings retiming ridgeline rodding rollup rulebooks rulemaking schwannoma screenshot searchable
servicemember servicemembers shipbreaking sightline sillcock sleeving slickensides smectitic snowmelt
snowpack sooted sportfishing stevedoring subgrade swallets teardown telemetered termiticide throughs
timestamp timestamps towaway toxigenic triaged unbilled unbonded uncited uncoached uncontroverted
uncooled unfloored unforwarded unlocated unlubricated unpermitted unphotographed unremedied
unrepaired unsalvageable waivable wasteline weatherseal whistleblower whistleblowing wildland xeriscape
""".split())

def check_page(dom, page, raw):
    F = []
    def f(sev, kind, msg, ev=""):
        F.append(dict(domain=dom, page=page, severity=sev, kind=kind, message=msg, evidence=ev[:180]))

    blocks = visible_blocks(raw)
    # only prose blocks; skip nav/footer-ish short items
    prose = [(t, x) for t, x in blocks if t in ("p", "li") and len(x) > 40]
    heads = [(t, x) for t, x in blocks if t.startswith("h")]
    text = "\n".join(x for _, x in blocks)

    # ---- leaked markup / placeholders
    for pat, why in LEAKED_MD:
        for m in re.finditer(pat, text):
            f("HIGH", "markup", why, text[max(0, m.start()-50):m.end()+50]); break

    # ---- mechanics
    for _, x in prose:
        for m in re.finditer(r"\S{0,25}  +\S{0,25}", x):
            f("LOW", "mechanics", "double space", m.group(0)); break
    for _, x in prose:
        m = re.search(r"\b(\w{3,})\s+\1\b", x, re.I)
        if m and m.group(1).lower() not in ("that", "had", "so", "very", "no"):
            f("HIGH", "mechanics", "doubled word", m.group(0))
    for _, x in prose:
        m = re.search(r"[A-Za-z]{2,}\s+[,;:.!?]", x)
        if m: f("MED", "mechanics", "space before punctuation", m.group(0))
    for _, x in prose:
        m = re.search(r"[a-z]{2,}[.!?][A-Z][a-z]", x)
        if m: f("MED", "mechanics", "missing space after sentence end", m.group(0))
    for _, x in prose:
        if x.count("(") != x.count(")"):
            f("HIGH", "mechanics", "unbalanced parentheses", x[:120])
        if (x.count("\u201c") != x.count("\u201d")):
            f("MED", "mechanics", "unbalanced curly quotes", x[:120])
    for _, x in prose:
        if (re.match(r"^[a-z]", x) and not re.match(r"^(?:e\.g|i\.e)", x)
                and not re.match(r"^[a-z](?:[A-Z]|\d)", x)):   # iDesign, i30
            f("MED", "mechanics", "block starts lowercase", x[:100])
    for _, x in prose:
        if re.search(r"\bthe the\b|\bof of\b|\band and\b|\bto to\b|\ba a\b", x, re.I):
            f("HIGH", "mechanics", "duplicated function word", x[:120])
    for tag, x in prose:
        # List items are labels, not paragraphs -- the urgency bullets and the
        # service lists correctly run without a final period. Only flag an li
        # once it is long enough to really be prose.
        gate = 130 if tag == "li" else 80
        if (not re.search(r"[.!?:\u201d)]$", x) and len(x) > gate
                and not is_citation_ish(x)):
            f("LOW", "mechanics", "paragraph has no terminal punctuation", x[-90:])
    for _, x in prose:
        m = re.search(r"[a-z]{2,},[A-Za-z]{2,}", x)
        if m: f("HIGH", "mechanics", "missing space after comma", m.group(0))
    for _, x in prose:
        m = re.search(r"[a-z]{2,};[A-Za-z]{2,}", x)
        if m: f("MED", "mechanics", "missing space after semicolon", m.group(0))
    if re.search(r"['\u2019]s\s+['\u2019]s|\bits'\b|\byour welcome\b|\bcould of\b|\bshould of\b|\bwould of\b|\bthen\s+(?:the\s+)?other\b", text, re.I):
        f("HIGH", "grammar", "common grammar error", "")
    for _, x in prose:
        m = re.search(r"\b(\w+)\s+(?:is|are|was|were)\s+(?:is|are|was|were)\b", x)
        if m: f("HIGH", "grammar", "doubled verb", m.group(0))

    # ---- structure
    h1 = [x for t, x in heads if t == "h1"]
    if len(h1) != 1:
        f("HIGH", "structure", f"h1 count is {len(h1)}, expected 1", " | ".join(h1)[:150])
    lv = [int(t[1]) for t, _ in heads]
    for i in range(1, len(lv)):
        if lv[i] - lv[i-1] > 1:
            f("MED", "structure", f"heading jumps h{lv[i-1]} to h{lv[i]}", heads[i][1][:90])
    for t, x in heads:
        if not x.strip(): f("HIGH", "structure", f"empty {t}", "")
        if len(x) > 95: f("MED", "structure", f"{t} very long, likely to wrap badly ({len(x)} chars)", x[:110])
        if (re.search(r"[.]$", x) and len(sentences(x)) == 1
                and not re.search(r"(?:Inc|Co|No|St|U\.S)\.$", x)):
            f("LOW", "structure", f"{t} ends with a period", x[:90])
    dupe = [k for k, v in collections.Counter(x.lower() for _, x in heads if x).items() if v > 1]
    if dupe: f("MED", "structure", "duplicate heading text on one page", "; ".join(dupe)[:150])
    # Orphan heading: a heading immediately followed by a heading at the SAME or
    # HIGHER level. A section heading followed by lower-level card titles is a
    # normal card grid, not a defect.
    for i in range(len(blocks) - 1):
        a, b = blocks[i], blocks[i+1]
        if (a[0].startswith("h") and b[0].startswith("h")
                and int(b[0][1]) <= int(a[0][1])):
            f("MED", "structure", "heading with no body under it", a[1][:90])
    body_words = len(words(" ".join(x for _, x in prose)))
    subheads = sum(1 for t, _ in heads if t in ("h2", "h3"))
    if body_words > 900 and subheads < 3:
        f("MED", "structure", f"{body_words} words but only {subheads} subheads", "")

    # ---- flow
    for _, x in prose:
        for s in sentences(x):
            n = len(words(s))
            if n > 48: f("MED", "flow", f"runaway sentence ({n} words)", s[:160])
    for _, x in prose:
        n = len(words(x))
        if n > 170: f("MED", "flow", f"runaway paragraph ({n} words)", x[:120])
    openers = [words(x)[0].lower() for _, x in prose if words(x)]
    # Only consecutive repeats matter. A city name opening 5 of 30 paragraphs on
    # a page about that city is normal writing, not a defect.
    if len(openers) >= 3:
        for i in range(len(openers) - 2):
            if openers[i] == openers[i+1] == openers[i+2]:
                f("MED", "flow", f"3 paragraphs in a row open with '{openers[i]}'", "")
                break
    # Word overuse: exclude the page's own subject. A gutter page says "gutter".
    tot = len(words(" ".join(x for _, x in prose)))
    if tot > 400:
        subject = set()
        for src in (dom, page):
            subject |= {w.lower() for w in re.findall(r"[A-Za-z]+", src)}
        subject |= SUBJECT_STOP
        cnt = collections.Counter(w.lower() for w in words(" ".join(x for _, x in prose))
                                 if w.lower() not in STOP and len(w) > 4
                                 and w.lower() not in subject)
        for w, c in cnt.most_common(6):
            if c / tot > 0.022 and c >= 12:
                f("MED", "flow", f"'{w}' used {c}x in {tot} words ({c/tot:.1%})", "")
    # One-sentence runs: source/citation lines are labels, not prose rhythm.
    onesent = 0
    for _, x in prose:
        if is_citation_ish(x):
            onesent = 0
            continue
        onesent = onesent + 1 if len(sentences(x)) == 1 else 0
        if onesent >= 5:
            f("LOW", "flow", "5+ one-sentence paragraphs in a row", x[:100]); break

    # ---- claims (per block, so patterns never match across a block boundary)
    for _, x in blocks:
        lowb = x.lower()
        for pat, why in BANNED_CLAIM:
            m = re.search(pat, lowb)
            if m: f("HIGH", "claims", why, x[max(0, m.start()-60):m.end()+60])

    return F

def spell_page(dom, page, raw, sp):
    F = []
    blocks = visible_blocks(raw)
    text = " ".join(x for t, x in blocks if t in ("p", "li", "h1", "h2", "h3"))
    text = re.sub(r"https?://\S+|\S+@\S+|\b[A-Z]{2,}\b|\b\d[\w.-]*\b", " ", text)
    text = re.sub(r"\b(?:[\w-]+\.)+(?:com|org|gov|net|edu|us|ca|io)\b", " ", text)
    text = text.replace("\u2019", "'")
    cand = set()
    for tok in WORD.findall(text):
        if any(c.isupper() for c in tok[1:]): continue    # CamelCase / acronyms
        if tok[0].isupper(): continue                     # proper nouns
        # split hyphenated compounds and drop possessive/plural apostrophes
        for w in re.split(r"[-\u2010-\u2015]", tok):
            lw = re.sub(r"'s?$", "", w.lower()).strip("'-")
            if len(lw) < 4 or lw in ALLOW or lw in STOP: continue
            cand.add(lw)
    for w in sorted(sp.unknown(cand)):
        F.append(dict(domain=dom, page=page, severity="MED", kind="spelling",
                      message=f"unknown word '{w}'", evidence=", ".join(list(sp.candidates(w) or [])[:3])))
    return F

# ---------------------------------------------------------------- main
def main():
    argv = sys.argv[1:]
    allp = "--all-phases" in argv
    csvout = None
    if "--csv" in argv:
        i = argv.index("--csv")
        csvout = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    args = [a for a in argv if not a.startswith("--")]

    doms = args or sorted(os.path.basename(os.path.dirname(p))
                          for p in glob.glob(os.path.join(ROOT, "sites", "*", "site.json")))
    if not args and not allp:
        keep = []
        for d in doms:
            try:
                if json.load(open(os.path.join(ROOT, "sites", d, "site.json"))).get("phase") == 2:
                    keep.append(d)
            except Exception: pass
        doms = keep

    try:
        from spellchecker import SpellChecker
        sp = SpellChecker(distance=1)
        sp.word_frequency.load_words(ALLOW)
    except Exception as e:
        print("spellcheck unavailable:", e); sp = None

    findings = []
    for d in doms:
        ddir = os.path.join(DIST, d)
        if not os.path.isdir(ddir):
            findings.append(dict(domain=d, page="-", severity="HIGH", kind="build",
                                 message="not built in dist/", evidence="")); continue
        for hp in sorted(glob.glob(os.path.join(ddir, "**", "*.html"), recursive=True)):
            page = "/" + os.path.relpath(hp, ddir).replace("index.html", "").rstrip("/")
            raw = open(hp, encoding="utf-8", errors="replace").read()
            findings += check_page(d, page or "/", raw)
            if sp: findings += spell_page(d, page or "/", raw, sp)

    order = {"HIGH": 0, "MED": 1, "LOW": 2}
    findings.sort(key=lambda r: (order[r["severity"]], r["domain"], r["page"]))

    bysev = collections.Counter(r["severity"] for r in findings)
    bykind = collections.Counter(r["kind"] for r in findings)
    print(f"QC over {len(doms)} sites -- {len(findings)} findings")
    print("  by severity:", dict(bysev))
    print("  by kind    :", dict(bykind))
    bad = collections.Counter(r["domain"] for r in findings if r["severity"] == "HIGH")
    if bad:
        print("\nsites with HIGH findings:")
        for d, c in bad.most_common(): print(f"   {c:3d}  {d}")
    print()
    for r in findings:
        if r["severity"] == "HIGH":
            print(f"[{r['severity']}] {r['domain']}{r['page']} {r['kind']}: {r['message']}")
            if r["evidence"]: print(f"        -> {r['evidence']}")

    if csvout:
        with open(csvout, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["domain","page","severity","kind","message","evidence"])
            w.writeheader(); w.writerows(findings)
        print(f"\nwrote {csvout}")
    return 1 if bysev.get("HIGH") else 0

if __name__ == "__main__":
    sys.exit(main())
