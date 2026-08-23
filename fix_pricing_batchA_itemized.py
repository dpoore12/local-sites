"""Batch A correction pass: total itemized posted prices before using them, and
drop sources that only post an adjacent job. Read 2026-08-23."""
import json
from pathlib import Path

SITES = Path(__file__).parent / "sites"
D = "read 2026-08-23"

def s(name, url):
    return {"name": name, "url": url}

RESCUE = s(f"Garage Door Rescue, Dallas-Fort Worth, posted repair price list, {D}",
           "https://garagedoorrescuellc.com/garage-door-repair-cost-dfw/")
DONTPANIC = s(f"Don't Panic Garage Door Repair, Cobb County, posted flat repair totals, {D}",
              "https://dontpanicdoor.com/")
LIBERTY = s(f"Liberty Garage Door Solutions, metro Atlanta, posted price table, {D}",
            "https://libertygaragedoorsolutionsatlanta.com/garage-door-repair-cost/")
HABPRO = s(f"Habpro Garage Doors, metro Atlanta, posted spring replacement prices, {D}",
           "https://www.habprogaragedoors.com/atlanta-ga/spring-replacement/")
ACWORTH_COST = s(f"Acworth Overhead Doors, Cobb County, posted service cost table, {D}",
                 "https://acworthoverheaddoors.com/acworth-ga-overhead-doors-service-costs")
GAGARAGE = s(f"Georgia Garage, Georgia, posted services and prices page, {D}",
             "https://georgiagaragellc.com/services/")

# (domain, row index) -> what changes
CHANGES = {
 "fortworthgaragedoorrepairpros.com": {
   1: {"high": 280},                       # Rescue posts track realignment to $280
 },
 "friscogaragedoorrepairexperts.com": {
   1: {"low": 200},                        # pair-specific posted lows are $200
   2: {"low": 100, "high": 650},           # Metro Plano: 2 x $150-250 per side + $75-150 bracket
 },
 "garagedoorrepairnapervillepros.com": {
   2: {"low": 120, "high": 550},           # John: cable $150-275 per side, both sides
 },
 "garlandgaragedoorrepairexperts.com": {
   0: {"low": 200, "high": 553},           # SOS itemized pair total: 67.50+185+2x150 insulated
   4: {"low": 100, "high": 775,
       "sources": "swap_gatepro_for_rescue"},
 },
 "mariettagaragedoorrepairpros.com": {
   0: {"low": 277, "high": 1099,
       "sources": [HABPRO, ACWORTH_COST, GAGARAGE]},
   3: {"job": "Opener gear or carriage replaced instead of the whole head",
       "low": 120, "high": 320, "basis": "flat",
       "note": "A gear kit or carriage swap keeps a sound head running; a dead board on a discontinued unit does not.",
       "sources": [DONTPANIC, LIBERTY]},
 },
}

for domain, rowmap in CHANGES.items():
    p = SITES / domain / "site.json"
    data = json.loads(p.read_text())
    rows = data["pricing"]["rows"]
    for idx, ch in rowmap.items():
        r = rows[idx]
        for k, v in ch.items():
            if k == "sources" and v == "swap_gatepro_for_rescue":
                r["sources"] = [x for x in r["sources"]
                                if "gaterepairpro" not in x["url"]] + [dict(RESCUE)]
            elif k == "sources":
                r["sources"] = [dict(x) for x in v]
            else:
                r[k] = v
        assert 0 < r["low"] < r["high"]
        assert 5 <= len(r["note"].split()) <= 30
        hosts = [x["url"].split("/")[2] for x in r["sources"]]
        assert len(set(hosts)) == len(hosts) == len(r["sources"])
        assert 2 <= len(r["sources"]) <= 4
        print(domain, idx, r["job"], r["low"], r["high"], len(r["sources"]))
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
