#!/usr/bin/env python3
"""
prospects.py - find the local businesses to rent each of the 83 sites to.

One renter per site. Never a marketplace. This only finds candidates and their
emails so they can be emailed; it never calls anyone.

    python3 prospects.py search     # find candidates per market (no credits)
    python3 prospects.py enrich     # reveal work emails (costs lead credits)
    python3 prospects.py sheet      # write data/prospects.csv
    python3 prospects.py status     # coverage per market

State lives in data/prospects.json so every step is resumable. Apollo returns
empty or partial pages under load, so every step re-reads what it has and only
fills gaps - never assume a call that returned nothing means "none exist".
"""
import csv, json, os, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor

# Each Apollo call is its own subprocess, so markets can be worked in parallel.
# Keep this modest: too many at once and Apollo starts returning empty pages.
# Apollo's MCP endpoint rate-limits hard (HTTP 429) - two workers is the most it
# tolerates, and `call` below backs off for 30s whenever it sees a 429.
WORKERS = 2
_lock = threading.Lock()

HERE = os.path.dirname(os.path.abspath(__file__))
NAP = os.path.join(HERE, "data", "nap.csv")
STATE = os.path.join(HERE, "data", "prospects.json")
SHEET = os.path.join(HERE, "data", "prospects.csv")

# How many candidate businesses we want per market before we start emailing.
TARGET_PER_MARKET = 12

# ---------------------------------------------------------------- Apollo search
# Titles: the person who can say yes. Small shops - owner is usually reachable.
TITLES_HOME = ["owner", "president", "general manager", "operations manager",
               "co-owner", "founder", "vice president"]
TITLES_LEGAL = ["owner", "managing partner", "managing attorney", "partner",
                "founder", "principal attorney", "attorney"]

# service -> Apollo organization keyword tags. Loose on purpose; Apollo matches
# these against company tags and name, so a plumber may surface under hvac and
# that is fine - we filter on the company actually being local and small.
KEYWORDS = {
    "Air Conditioner Repair":       ["hvac", "air conditioning", "heating and cooling"],
    "Air Conditioning Installation":["hvac", "air conditioning", "heating and cooling"],
    "Furnace Repair":               ["hvac", "heating", "furnace"],
    "Emergency Plumbing":           ["plumbing", "plumber", "drain"],
    "Leak Detection":               ["plumbing", "leak detection", "water"],
    "Garage Door Repair":           ["garage door", "overhead door"],
    "Appliance Repair":             ["appliance repair", "appliance service"],
    "Foundation Repair":            ["foundation repair", "structural repair", "concrete"],
    "Mold Remediation":             ["mold remediation", "restoration", "environmental"],
    "Water Damage Restoration":     ["water damage", "restoration", "disaster restoration"],
    "Roof Inspection":              ["roofing", "roofer"],
    "Tile Roof Repair":             ["roofing", "roofer", "tile roofing"],
    "Gutter Cleaning":              ["gutters", "roofing", "exterior cleaning"],
    "Window Replacement":           ["windows", "window replacement", "remodeling"],
    "Bathroom Remodeling":          ["remodeling", "bathroom remodeling", "general contractor"],
    "Moving Services":              ["moving", "movers", "relocation"],

    "Car Accident Lawyer":          ["personal injury", "car accident", "law firm"],
    "Motorcycle Accident Lawyer":   ["personal injury", "motorcycle accident", "law firm"],
    "Truck Accident Lawyer":        ["personal injury", "truck accident", "law firm"],
    "Personal Injury Lawyer":       ["personal injury", "law firm", "injury"],
    "Dog Bite Lawyer":              ["personal injury", "law firm", "injury"],
    "Wrongful Death Lawyer":        ["personal injury", "wrongful death", "law firm"],
    "Criminal Defense Lawyer":      ["criminal defense", "criminal law", "law firm"],
    "DUI Lawyer":                   ["criminal defense", "dui", "law firm"],
    "Domestic Violence Lawyer":     ["criminal defense", "family law", "law firm"],
    "Divorce Lawyer":               ["family law", "divorce", "law firm"],
    "Family Law Attorney":          ["family law", "divorce", "law firm"],
    "Wrongful Termination Lawyer":  ["employment law", "labor and employment", "law firm"],
}


# Apollo matches organization_locations against the company's HQ city, so a
# suburb returns almost nothing even when the metro is full of shops. For those
# markets we widen to the metro, then the state, and record which pass found
# each person so a non-local company can be spotted before anyone is emailed.
METRO = {
    "Ann Arbor": "Detroit, Michigan", "Bellevue": "Omaha, Nebraska",
    "Boca Raton": "Fort Lauderdale, Florida", "Carrollton": "Dallas, Texas",
    "Garland": "Dallas, Texas", "Mesquite": "Dallas, Texas",
    "McKinney": "Dallas, Texas", "Plano": "Dallas, Texas",
    "Fort Worth": "Dallas, Texas", "Naperville": "Chicago, Illinois",
    "Marietta": "Atlanta, Georgia", "Parker": "Denver, Colorado",
    "Danville": "Oakland, California", "Eden Prairie": "Minneapolis, Minnesota",
    "Overland Park": "Kansas City, Missouri", "Victorville": "Riverside, California",
    "Virginia Beach": "Norfolk, Virginia", "West Covina": "Los Angeles, California",
    "Oceanside": "San Diego, California", "Arvada": "Denver, Colorado",
    "Sandy Springs": "Atlanta, Georgia", "Chandler": "Phoenix, Arizona",
    "Gilbert": "Phoenix, Arizona", "Tempe": "Phoenix, Arizona",
    "Scottsdale": "Phoenix, Arizona", "Henderson": "Las Vegas, Nevada",
    "Katy": "Houston, Texas", "Pearland": "Houston, Texas",
    "Sugar Land": "Houston, Texas", "Round Rock": "Austin, Texas",
    "Cary": "Raleigh, North Carolina", "Clearwater": "Tampa, Florida",
    "Aurora": "Denver, Colorado", "Roseville": "Sacramento, California",
    "Elk Grove": "Sacramento, California", "Fremont": "San Jose, California",
    "Sunnyvale": "San Jose, California", "Santa Clara": "San Jose, California",
    "Chula Vista": "San Diego, California", "Escondido": "San Diego, California",
}

STATE_NAME = {
    "AL": "Alabama", "AR": "Arkansas", "AZ": "Arizona", "CA": "California",
    "CO": "Colorado", "FL": "Florida", "GA": "Georgia", "IL": "Illinois",
    "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "MI": "Michigan",
    "MN": "Minnesota", "MO": "Missouri", "NC": "North Carolina",
    "NE": "Nebraska", "NV": "Nevada", "NY": "New York", "OH": "Ohio",
    "PA": "Pennsylvania", "TX": "Texas", "VA": "Virginia", "WA": "Washington",
}


def call(tool, args, tries=4):
    """One Apollo call. Empty or error result is a retry, never a zero."""
    payload = {"source_id": "apollo", "tool_name": tool, "arguments": args}
    for n in range(tries):
        try:
            p = subprocess.run(["external-tool", "call", json.dumps(payload)],
                               capture_output=True, text=True, timeout=180)
            if p.returncode == 0 and p.stdout.strip():
                return json.loads(p.stdout)
            err = (p.stderr or p.stdout or "")[:200]
        except Exception as e:
            err = str(e)[:200]
        # A 429 means Apollo wants us to stop, not that there is no data.
        time.sleep(30.0 if "RATE_LIMITED" in err or "429" in err else 2.0 * (n + 1))
    print(f"    ! failed after {tries}: {err}")
    return None


def markets():
    rows = list(csv.DictReader(open(NAP)))
    out = []
    for r in rows:
        out.append({
            "domain": r["domain"],
            "niche": r["niche"],
            "service": r["service"],
            "city": r["city"],
            "state": r["state"],
        })
    return out


def load():
    if os.path.exists(STATE):
        return json.load(open(STATE))
    return {}


def save(st):
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    with _lock:
        tmp = STATE + ".tmp"
        json.dump(st, open(tmp, "w"), indent=1)
        os.replace(tmp, STATE)


def _work_market(m, have, label):
    """Find candidates for one market. Returns the merged candidate list."""
    kw = KEYWORDS.get(m["service"])
    if not kw:
        print(f"{label} {m['domain']}: NO KEYWORD MAP for {m['service']!r}")
        return have
    titles = TITLES_LEGAL if m["niche"] == "legal" else TITLES_HOME
    loc = f"{m['city']}, {m['state']}"
    found = {p["id"]: p for p in have}
    # Widen only as far as needed: exact city, then the metro, then the state.
    places = [(loc, "city")]
    if METRO.get(m["city"]):
        places.append((METRO[m["city"]], "metro"))
    if STATE_NAME.get(m["state"]):
        places.append((STATE_NAME[m["state"]], "state"))
    for place, how in places:
        if len(found) >= TARGET_PER_MARKET:
            break
        # Verified emails first, then loosen if the market is still thin.
        for statuses in (["verified"], ["verified", "likely to engage"], None):
            if len(found) >= TARGET_PER_MARKET:
                break
            args = {
                "person_titles": titles,
                "q_organization_keyword_tags": kw,
                "organization_locations": [place],
                "organization_num_employees_ranges": ["1,10", "11,50"],
                "per_page": 25,
                "_rationale": "Finding local business owners to offer a website rental to",
                "_conversation_ref": "lr83outreach",
            }
            if statuses:
                args["contact_email_status"] = statuses
            res = call("apollo_mixed_people_api_search", args)
            if not res:
                continue
            for p in res.get("people", []):
                org = (p.get("organization") or {}).get("name") or ""
                if not org or p["id"] in found:
                    continue
                found[p["id"]] = {
                    "id": p["id"],
                    "first_name": p.get("first_name") or "",
                    "title": p.get("title") or "",
                    "org": org,
                    "has_email": bool(p.get("has_email")),
                    "found_by": how,
                    "found_in": place,
                }
    out = list(found.values())[:TARGET_PER_MARKET * 2]
    print(f"{label} {m['domain']}: {len(out)} candidates")
    return out


def cmd_search():
    # State is saved after every market, so a run that is cut short loses nothing.
    st = load()
    ms = [m for m in markets()
          if len(st.get(m["domain"], {}).get("people", [])) < TARGET_PER_MARKET]
    print(f"{len(ms)} markets still short of {TARGET_PER_MARKET} candidates")

    def job(idx_m):
        i, m = idx_m
        have = st.get(m["domain"], {}).get("people", [])
        people = _work_market(m, have, f"[{i}/{len(ms)}]")
        st[m["domain"]] = {**m, "people": people}
        save(st)

    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        list(ex.map(job, enumerate(ms, 1)))
    cmd_status()


def cmd_status():
    st = load()
    ms = markets()
    thin, ok, none = [], 0, []
    for m in ms:
        n = len(st.get(m["domain"], {}).get("people", []))
        if n == 0:
            none.append(m["domain"])
        elif n < 5:
            thin.append((m["domain"], n))
        else:
            ok += 1
    print(f"\n{ok} markets with 5+ candidates, {len(thin)} thin, {len(none)} empty, "
          f"{len(ms)} total")
    if thin:
        print("thin: " + ", ".join(f"{d}({n})" for d, n in thin))
    if none:
        print("empty: " + ", ".join(none))
    tot = sum(len(v.get("people", [])) for v in st.values())
    withmail = sum(1 for v in st.values() for p in v.get("people", []) if p.get("email"))
    print(f"{tot} candidates found, {withmail} with a revealed email")


def cmd_enrich():
    """Reveal work emails. Costs one lead credit per person revealed."""
    # Only reveal as many per market as we actually intend to email. One credit
    # per reveal, and a market only needs one tenant plus a few backups.
    per_market = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    st = load()
    batches = []
    for d, v in st.items():
        people = v.get("people", [])
        already = sum(1 for p in people if p.get("email"))
        want = max(0, per_market - already)
        queue = [p for p in people if not p.get("email") and p.get("has_email")][:want]
        for i in range(0, len(queue), 10):
            batches.append((d, queue[i:i + 10]))
    total = sum(len(b) for _, b in batches)
    print(f"{total} people to reveal across {len({d for d, _ in batches})} markets")

    counter = {"n": 0}

    def job(batch):
        d, people = batch
        res = call("apollo_people_bulk_match", {
            "details": [{"id": p["id"]} for p in people],
            "_rationale": "Revealing work emails so local owners can be emailed an offer",
            "_conversation_ref": "lr83outreach",
        })
        if not res:
            return
        for p, mt in zip(people, res.get("matches") or []):
            if not isinstance(mt, dict) or not mt.get("email"):
                continue
            p["email"] = mt["email"]
            p["last_name"] = mt.get("last_name") or ""
            p["org_site"] = ((mt.get("organization") or {}).get("website_url") or "")
        save(st)
        counter["n"] += len(people)
        print(f"  {counter['n']}/{total}")

    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        list(ex.map(job, batches))
    cmd_status()


# Apollo's keyword tags are loose, so an AC search can return a roofer. These
# words are checked against the company name and website so an obvious mismatch
# is visible in the sheet instead of being emailed the wrong offer.
TRADE_WORDS = {
    "Air Conditioner Repair": ["air", "hvac", "heat", "cool", "ac ", "climate", "comfort"],
    "Air Conditioning Installation": ["air", "hvac", "heat", "cool", "climate", "comfort"],
    "Furnace Repair": ["furnace", "heat", "hvac", "air", "comfort"],
    "Emergency Plumbing": ["plumb", "drain", "rooter", "sewer", "pipe"],
    "Leak Detection": ["plumb", "leak", "water", "pipe", "drain"],
    "Garage Door Repair": ["garage", "door", "overhead"],
    "Appliance Repair": ["appliance", "repair"],
    "Foundation Repair": ["foundation", "concrete", "structur", "pier", "level"],
    "Mold Remediation": ["mold", "restor", "remediat", "environ", "abate"],
    "Water Damage Restoration": ["restor", "water", "damage", "dry", "servpro", "flood"],
    "Roof Inspection": ["roof"],
    "Tile Roof Repair": ["roof", "tile"],
    "Gutter Cleaning": ["gutter", "roof", "exterior", "clean"],
    "Window Replacement": ["window", "glass", "remodel", "exterior"],
    "Bathroom Remodeling": ["remodel", "bath", "kitchen", "renovat", "construct", "design"],
    "Moving Services": ["moving", "movers", "relocat", "van lines", "transfer"],
}
LEGAL_WORDS = ["law", "legal", "attorney", "llp", "pllc", " pc", "p.c.", "counsel",
               "firm", "justice", "injur", "advocate", "esq"]


def trade_match(service, niche, company, site):
    hay = f" {company.lower()} {site.lower()} "
    words = LEGAL_WORDS if niche == "legal" else TRADE_WORDS.get(service, [])
    return "yes" if any(w in hay for w in words) else "CHECK"


def cmd_sheet():
    st = load()
    rows = []
    for d, v in sorted(st.items()):
        for p in v.get("people", []):
            if not p.get("email"):
                continue
            rows.append({
                "domain": d,
                "niche": v.get("niche", ""),
                "service": v.get("service", ""),
                "city": v.get("city", ""),
                "state": v.get("state", ""),
                "first_name": p.get("first_name", ""),
                "last_name": p.get("last_name", ""),
                "title": p.get("title", ""),
                "company": p.get("org", ""),
                "email": p["email"],
                "company_site": p.get("org_site", ""),
                "trade_match": trade_match(v.get("service", ""), v.get("niche", ""),
                                           p.get("org", ""), p.get("org_site", "")),
                "found_by": p.get("found_by", "city"),
                "found_in": p.get("found_in", f"{v.get('city','')}, {v.get('state','')}"),
                "status": "not contacted",
            })
    # Best candidates first within each market: right trade, and actually local.
    rank = {"city": 0, "metro": 1, "state": 2}
    rows.sort(key=lambda r: (r["domain"], r["trade_match"] != "yes",
                             rank.get(r["found_by"], 3)))
    os.makedirs(os.path.dirname(SHEET), exist_ok=True)
    with open(SHEET, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else
                           ["domain", "email"])
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {SHEET}: {len(rows)} rows, "
          f"{len({r['domain'] for r in rows})} markets covered")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    {"search": cmd_search, "enrich": cmd_enrich, "sheet": cmd_sheet,
     "status": cmd_status}[cmd]()
