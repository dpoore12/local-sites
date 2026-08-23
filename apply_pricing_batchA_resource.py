"""Re-source pricing rows for batch A (5 garage door sites) from published
company price pages. Every low/high comes from posted figures recorded in
pricing-research-*.md. Read 2026-08-23."""
import json
from pathlib import Path

SITES = Path(__file__).parent / "sites"
D = "read 2026-08-23"

def s(name, url):
    return {"name": name, "url": url}

# ---------------------------------------------------------------- sources
# DFW
COWTOWN = s(f"Cowtown Garage Doors, Fort Worth, posted spring price list, {D}",
            "https://www.cowtowndoors.com/page-14.html")
COWTOWN_TUNE = s(f"Cowtown Garage Doors, Fort Worth, posted tune-up page, {D}",
                 "https://www.cowtowndoors.com/page-17.html")
PANTHER_SPRING = s(f"Panther Garage Pros, Fort Worth, posted spring replacement page, {D}",
                   "https://panthergaragepros.com/services/garage-door-springs-replacement/")
PANTHER_LIST = s(f"Panther Garage Pros, Fort Worth, posted service cost list, {D}",
                 "https://panthergaragepros.com/garage-door-repair-service-costs-wedgwood-square/")
RESCUE = s(f"Garage Door Rescue, Dallas-Fort Worth, posted repair price list, {D}",
           "https://garagedoorrescuellc.com/garage-door-repair-cost-dfw/")
FASTMOBILE = s(f"Fast Mobile Garage Doors, Fort Worth and Garland, posted price list, {D}",
               "https://fastmobilegaragedoors.com/garage-door-repair-cost-dallas-tx.html")
VETERAN = s(f"Veteran Garage Door, Dallas-Fort Worth, posted installed spring prices, {D}",
            "https://veterangaragedoor.com/springs/")
DADS = s(f"Dad's Garage Doors, Dallas-Fort Worth, posted spring and tune-up prices, {D}",
         "https://dadsgaragedoors.com/")
# Frisco / Collin County
PROSPER_SPRING = s(f"Prosper Garage Door Repair, Frisco, posted spring repair page, {D}",
                   "https://prosperdoorrepair.com/garage-door-spring-repair/frisco")
PROSPER_OPENER = s(f"Prosper Garage Door Repair, Plano, posted opener price page, {D}",
                   "https://prosperdoorrepair.com/garage-door-opener-repair/plano")
PROSPER_DOOR = s(f"Prosper Garage Door Repair, Frisco, posted new door installation page, {D}",
                 "https://prosperdoorrepair.com/new-garage-door-installation/frisco")
METRO_PLANO = s(f"Metro Garage Door Repair, Plano, posted cost breakdown, {D}",
                "https://www.metrogaragedoor.net/garage-door-repair-cost-plano-tx-what-youll-actually-pay-and-why/")
# Garland
TRUESAFE_BLOG = s(f"TrueSafe Garage Door Repair, Garland, posted cost list, {D}",
                  "https://www.truesafegaragedoors.com/blog/how-much-does-garage-door-repair-cost-garland-tx")
TRUESAFE_SERV = s(f"TrueSafe Garage Door Repair, Garland, posted service prices, {D}",
                  "https://www.truesafegaragedoors.com/services")
SOS = s(f"SOS Garage Doors, Garland, posted spring repair price table, {D}",
        "https://www.sosgaragedoors.com/garland_springs.html")
GATEPRO = s(f"Garland Garage Door Repair Pro, Garland, posted repair prices, {D}",
            "https://www.gaterepairpro.com/garland/garage-door-repair-garland-tx/")
DALLASPRO = s(f"Dallas Garage Door Pro, Dallas and Garland area, posted price table, {D}",
              "https://dallasgaragedoorrepairpro.com/garage-door-repair-cost-dallas/")
MANDM = s(f"M&M Garage Door Services, Dallas, posted repair cost table, {D}",
          "https://mandmgaragedfw.com/blog/garage-door-repair-cost-dallas/")
# Chicago / DuPage
GDCENTER = s(f"Garage Door Center, Naperville, posted price list, {D}",
             "https://garagedoorcenterusa.com/service-area/garage-door-repair-services-naperville-il")
TRUSTED = s(f"Trusted Garage Door, Cook and DuPage counties, posted service prices, {D}",
            "https://www.trusted-garagedoor.com/services/")
JOHNGD = s(f"John Garage Door Repair, Chicago area, posted price table, {D}",
           "https://johngaragedoorrepair.com/garage-door-repair-cost/")
ROYAL = s(f"Royal Garage Doors, Aurora, posted flat-rate spring prices, {D}",
          "https://royalgaragedoorrepairs.com/locations/garage-door-spring-repair-aurora/")
GDGUYS = s(f"Garage Door Guys, Naperville and DuPage County, posted spring price, {D}",
           "https://www.garagedoorguys.biz/garage-door-spring-repair")
INFANTINO = s(f"Infantino's Garage Door, Chicago area, posted starting prices, {D}",
              "https://infantinosgaragedoor.com/services/cost")
PREMIUMIL = s(f"Premium Garage Door Repair, Naperville, posted repair ranges, {D}",
              "https://premiumgarageil.com/garage-door-repair-naperville/")
# Atlanta / Cobb
ACWORTH_MAR = s(f"Acworth Overhead Doors, Marietta, posted repair cost page, {D}",
                "https://acworthoverheaddoors.com/garage-door-repair-marietta-ga")
ACWORTH_COST = s(f"Acworth Overhead Doors, Cobb County, posted service cost table, {D}",
                 "https://acworthoverheaddoors.com/acworth-ga-overhead-doors-service-costs")
HABPRO = s(f"Habpro Garage Doors, metro Atlanta, posted spring replacement prices, {D}",
           "https://www.habprogaragedoors.com/atlanta-ga/spring-replacement/")
LIBERTY = s(f"Liberty Garage Door Solutions, metro Atlanta, posted price table, {D}",
            "https://libertygaragedoorsolutionsatlanta.com/garage-door-repair-cost/")
GAGARAGE = s(f"Georgia Garage, Georgia, posted services and prices page, {D}",
             "https://georgiagaragellc.com/services/")
GOODGOLLY = s(f"Good Golly Garage Doors, Marietta, posted tune-up price, {D}",
              "https://goodgollygarage.com/garage-door-maintenance/garage-door-tune-up-in-atlanta-ga")
ATLFIX = s(f"Garage Door Atlanta, Atlanta area, posted cable replacement range, {D}",
           "https://atlantagaragedoorfix.com/garage-door-cable-replacement-atlanta-ga/")
GDATLGA = s(f"Garage Doors Atlanta GA, Atlanta area, posted repair cost list, {D}",
            "https://garagedoorsatlantaga.com/blog/how-much-does-it-cost-to-repair-a-garage-door-in-atlanta.html")

# ---------------------------------------------------------------- row plans
PLANS = {
 "fortworthgaragedoorrepairpros.com": [
   ("Broken torsion spring, replaced as a matched pair", 200, 500, None, [COWTOWN, FASTMOBILE, RESCUE, VETERAN]),
   ("Door jumped the track, cables reset and drums retimed", 120, 275, None, [FASTMOBILE, PANTHER_LIST, RESCUE]),
   ("Rollers, hinges and bearings replaced across the door", 75, 220, None, [COWTOWN_TUNE, FASTMOBILE, RESCUE]),
   ("Opener head replaced, wall control and safety eyes included", 250, 800, None, [FASTMOBILE, RESCUE]),
   ("Track and strut straightened after a hail or wind hit", 100, 280, None, [PANTHER_LIST, RESCUE]),
   ("Two-car insulated steel door replaced, permit filed", 800, 3000, None, [FASTMOBILE, RESCUE]),
 ],
 "friscogaragedoorrepairexperts.com": [
   ("Tune-up visit that diagnoses a door which will not move", 75, 150,
    "Weeknight and weekend slots price at the top. Many companies apply the amount against the repair if work proceeds.",
    [FASTMOBILE, METRO_PLANO, RESCUE]),
   ("Torsion springs replaced in pairs on a builder-grade door", 150, 350, None, [PROSPER_SPRING, METRO_PLANO, FASTMOBILE]),
   ("Lift cables, drums and bottom brackets replaced", 100, 250, None, [METRO_PLANO, FASTMOBILE, RESCUE]),
   ("Opener gear kit or logic board rebuilt rather than replaced", 75, 250, None, [PROSPER_OPENER, METRO_PLANO, FASTMOBILE]),
   ("Wi-Fi capable belt drive opener installed", 250, 600, None, [PROSPER_OPENER, METRO_PLANO, FASTMOBILE]),
   ("One damaged section swapped on an existing door", 150, 700, None, [METRO_PLANO, FASTMOBILE, RESCUE]),
   ("Full double door replaced, insulated steel, permit filed", 800, 3000, None, [PROSPER_DOOR, METRO_PLANO, RESCUE]),
 ],
 "garagedoorrepairnapervillepros.com": [
   ("Torsion spring pair replaced on a sectional door", 225, 460, None, [GDGUYS, TRUSTED, JOHNGD, ROYAL]),
   ("Remotes, keypad and safety eyes reprogrammed or swapped out", 50, 200,
    "A dead keypad battery costs nothing to rule out; a sun-bleached sensor pair and fresh wiring do not.",
    [GDCENTER, JOHNGD, ROYAL]),
   ("Cables replaced and a door lifted back into its tracks", 120, 300, None, [GDCENTER, JOHNGD, ROYAL]),
   ("Rollers and hinges replaced across a two-car door", 95, 200, None, [TRUSTED, JOHNGD]),
   ("Opener replaced with a belt drive and battery backup", 400, 700, None, [GDCENTER, TRUSTED, JOHNGD, INFANTINO]),
   ("Bent track and struts corrected after a wind event", 120, 800, None, [GDCENTER, JOHNGD, PREMIUMIL]),
   ("Insulated double door replaced on a like-for-like opening", 800, 2500, None, [JOHNGD, TRUSTED, ROYAL]),
 ],
 "garlandgaragedoorrepairexperts.com": [
   ("Snapped torsion spring, both springs renewed", 200, 389, None, [TRUESAFE_BLOG, SOS, GATEPRO, DALLASPRO]),
   ("Frayed lift cable replaced and the drums retimed", 89, 489, None, [TRUESAFE_BLOG, DALLASPRO, MANDM]),
   ("Opener that lost power or memory brought back into service", 100, 489, None, [TRUESAFE_BLOG, DALLASPRO, RESCUE]),
   ("Opener head replaced, sensors and rail included", 200, 800, None, [TRUESAFE_BLOG, DALLASPRO, RESCUE]),
   ("Storm damage assessment with track and bracket repair", 125, 775, None, [DALLASPRO, MANDM, GATEPRO]),
   ("Single damaged section replaced on an older steel door", 150, 700, None, [DALLASPRO, RESCUE]),
   ("Two-car door replaced with insulated steel", 800, 3000, None, [DALLASPRO, RESCUE, FASTMOBILE]),
 ],
 "mariettagaragedoorrepairpros.com": [
   ("Torsion springs renewed in pairs", 100, 700, None, [HABPRO, LIBERTY, GDATLGA, ACWORTH_COST]),
   ("Door sticking or dragging, balance and hardware corrected", 49, 600, None, [GOODGOLLY, GAGARAGE, LIBERTY]),
   ("Cables and bottom brackets replaced after a door drops", 100, 300, None, [ATLFIX, LIBERTY, GDATLGA]),
   ("Rollers, hinges and end bearings refreshed", 99, 220, None, [LIBERTY, GAGARAGE]),
   ("Opener replaced, safety eyes and wall control included", 250, 1500, None, [LIBERTY, ACWORTH_COST]),
   ("Panels and track repaired after a vehicle or storm strike", 120, 1200,
    "A crumpled skin can be lived with; a shifted track and a cracked stile cannot, and matching Cobb-era panels adds time.",
    [ACWORTH_MAR, LIBERTY, GDATLGA]),
   ("Carriage style door replaced on a visible elevation", 700, 3000, None, [ACWORTH_MAR, LIBERTY]),
 ],
}

for domain, plan in PLANS.items():
    p = SITES / domain / "site.json"
    data = json.loads(p.read_text())
    old = {r["job"]: r for r in data["pricing"]["rows"]}
    old_list = data["pricing"]["rows"]
    rows = []
    for i, (job, lo, hi, note, srcs) in enumerate(plan):
        base = old.get(job)
        if note is None:
            if base is None:
                raise SystemExit(f"{domain}: no existing note for {job!r}")
            note = base["note"]
        basis = base["basis"] if base else old_list[i]["basis"]
        rows.append({"job": job, "low": lo, "high": hi, "basis": basis,
                     "note": note,
                     "sources": [dict(x) for x in srcs]})
    data["pricing"]["rows"] = rows
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print("updated", domain, len(rows), "rows")
