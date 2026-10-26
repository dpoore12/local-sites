"""Write FILING-SHEET-BATCH1-2026-10-25.md and kyle-screen/oct-top3/filing_sheet_batch1.csv: the fields to type into
the four directories that take a listing with no street address (NearSpotUSA, HVACServiceFast, RentADumpster.co,
BizHwy), for every Kyle batch 1 site each one fits. Nothing here submits anything.

ZIPs: Census 2020 ZCTA-to-place file (oct-top3/site_zips_census2020.json; a ZIP is kept if it covers 3%+ of the
town's land or 25%+ of the ZIP is inside the town), plus the USPS-name ZIPs for East Cobb and Cantonment, which
aren't Census places.

usage (from the repo root): python3 -I kyle-screen/filing_sheet.py
"""
import csv, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
census = json.load(open(os.path.join(HERE, 'oct-top3', 'site_zips_census2020.json')))

AREA = {  # towns named in each site's own "where we serve" copy, and the extra ZIPs Census places miss
 'bentonvilledumpsterrentalpros.com': (['Bentonville', 'Centerton', 'Bella Vista', 'Pea Ridge', 'Rogers'], [], []),
 'dryerventcleaningocala.com': (['Ocala', 'Silver Springs Shores', 'Marion Oaks', 'On Top of the World'], [], []),
 'mariettaairductcleaningpros.com': (['Marietta', 'Kennesaw', 'Smyrna', 'East Cobb'], ['30068'], []),
 'windowtintingbradenton.com': (['Bradenton', 'Palmetto', 'Ellenton', 'Holmes Beach', 'Lakewood Ranch'], [], ['34240']),
 'wellingtondumpsterrentalpros.com': (['Wellington'], [], []),
 'biloxidumpsterrentalpros.com': (['Biloxi'], [], []),
 'schaumburgairductcleaningpros.com': (['Schaumburg'], [], []),
 'northmiamiseptictankpumpingpros.com': (['North Miami'], [], []),
 'wheatonairductcleaningpros.com': (['Wheaton'], [], []),
 'pensacoladumpsterrentalpros.com': (['Pensacola', 'Warrington', 'Ferry Pass', 'Myrtle Grove', 'Cantonment', 'Perdido Key'], ['32533'], []),
}
DESC = {
 'bentonvilledumpsterrentalpros.com': "Roll-off dumpster rental for Bentonville and Benton County, AR: new-construction framing scrap, remodel tear-outs, garage and estate cleanouts, and concrete or dirt. Boxes sized to the job, with the tons, rental days and price stated before the drop. Serving Bentonville, Centerton, Bella Vista, Pea Ridge and Rogers.",
 'dryerventcleaningocala.com': "Dryer vent cleaning for Ocala and Marion County, FL: full-run cleaning from the dryer to the wall hood or roof cap, roof vent cleaning, bird nest removal and vent repair. The price for the whole run is stated before the dryer is moved. Serving Ocala, Silver Springs Shores, Marion Oaks and On Top of the World.",
 'mariettaairductcleaningpros.com': "Air duct cleaning for Marietta and Cobb County, GA: supply and return ducts, dryer vents, coil and air handler cleaning, and duct sealing. The whole system is in scope and the total is stated before work starts. Serving Marietta, Kennesaw, Smyrna and East Cobb.",
 'windowtintingbradenton.com': "Window tinting for Bradenton and Manatee County, FL: car tint at Florida-legal shades, ceramic film, and solar film for homes and businesses. Film and price named before the job. Serving Bradenton, Palmetto, Ellenton, Holmes Beach and Lakewood Ranch.",
 'wellingtondumpsterrentalpros.com': "Roll-off dumpster rental in Wellington, FL: home cleanouts, remodel and roofing debris, barn and farm cleanouts, and storm debris. Priced before delivery and placed where the HOA and the village allow. Serving all of Wellington, from Wellington Green to the farms off South Shore Boulevard.",
 'biloxidumpsterrentalpros.com': "Roll-off dumpster rental in Biloxi, MS: construction and renovation debris, roof tear-offs, concrete and heavy debris, and cleanouts. The box is matched to the debris, with the weight and rental days settled first. Serving Biloxi from Point Cadet and Edgewater north to Woolmarket.",
 'schaumburgairductcleaningpros.com': "Air duct cleaning for Schaumburg, IL: supply and return ducts, furnace and blower cleaning, dryer vents, and cleanup after a remodel. The whole system is in scope and the total is on paper first. Serving Schaumburg from Weathersfield and Lexington Village to the Woodfield area.",
 'northmiamiseptictankpumpingpros.com': "Septic tank pumping and service for North Miami, FL: routine pumping, emergency backups, drain field repair, and tank abandonment when sewer reaches the street, under Miami-Dade's septic rules. Priced before the hose goes in. Serving North Miami from Keystone Point and Sans Souci to Westside Sunkist Grove.",
 'wheatonairductcleaningpros.com': "Air duct cleaning for Wheaton, IL: every return and trunk line, furnace and blower cleaning, dust cleanup after a basement or remodel job, and dryer vents. Scope and price stated first. Serving Wheaton from the Northside to Danada and Arrowhead.",
 'pensacoladumpsterrentalpros.com': "Roll-off dumpster rental for Pensacola and Escambia County, FL: storm debris, roof tear-offs, construction and renovation, and home cleanouts. Tonnage, rental days and price named before the box is dropped. Serving Pensacola, Warrington, Ferry Pass, Myrtle Grove, Cantonment and Perdido Key.",
}
NEARSPOT = {'dumpster': 'Contractors & Builders', 'dryer': 'Cleaning Services', 'duct': 'HVAC & Heating',
            'tint': 'Auto Body & Paint', 'septic': 'Plumbers'}
BIZHWY = {'dumpster': 'Energy and Environment', 'dryer': 'Real Estate and Construction', 'duct': 'Real Estate and Construction',
          'tint': 'Automotive', 'septic': 'Real Estate and Construction'}
HVACFAST = {'mariettaairductcleaningpros.com': 'Air Duct Cleaning, Ductwork Services, Indoor Air Quality',
            'schaumburgairductcleaningpros.com': 'Air Duct Cleaning, Furnace Services, Indoor Air Quality',
            'wheatonairductcleaningpros.com': 'Air Duct Cleaning, Furnace Services, Indoor Air Quality'}


def kind(d):
    return 'dumpster' if 'dumpster' in d else 'dryer' if 'dryervent' in d else 'duct' if 'airduct' in d else \
        'tint' if 'tint' in d else 'septic'


sites = []
for d, (towns, add, drop) in AREA.items():
    s = json.load(open(os.path.join(REPO, 'sites', d, 'site.json')))
    zips = set(add)
    for place, zs in census[d].items():
        for z, _ in (zs or []):
            zips.add(z)
    zips -= set(drop)
    disclosure = f"Independently operated advertising site, not itself a {s['entity_noun']}."
    sites.append({'domain': d, 'brand': s['brand'], 'phone': s['phone_display'], 'website': f'https://{d}/',
                  'state': s['state'], 'county': s['counties'][0], 'towns': towns, 'zips': sorted(zips),
                  'main_zip': sorted(zips)[0], 'kind': kind(d), 'service': s['service'],
                  'services': [x['name'] for x in s['services']],
                  'description': DESC[d] + ' ' + disclosure})
# the one ZIP NearSpotUSA asks for: the city's central ZIP
MAIN = {'bentonvilledumpsterrentalpros.com': '72712', 'dryerventcleaningocala.com': '34471', 'mariettaairductcleaningpros.com': '30060',
        'windowtintingbradenton.com': '34205', 'wellingtondumpsterrentalpros.com': '33414', 'biloxidumpsterrentalpros.com': '39530',
        'schaumburgairductcleaningpros.com': '60193', 'northmiamiseptictankpumpingpros.com': '33161', 'wheatonairductcleaningpros.com': '60187',
        'pensacoladumpsterrentalpros.com': '32502'}
for s in sites:
    assert MAIN[s['domain']] in s['zips'], s['domain']
    s['main_zip'] = MAIN[s['domain']]

rows = []
for s in sites:
    base = {'site': s['domain'], 'business_name': s['brand'], 'phone': s['phone'], 'website': s['website'],
            'description': s['description']}
    rows.append({'directory': 'NearSpotUSA', **base, 'category': NEARSPOT[s['kind']], 'zip': s['main_zip'],
                 'service_area': '', 'other': 'Street address: leave blank. Business email: leave blank.'})
    rows.append({'directory': 'BizHwy', **base, 'category': BIZHWY[s['kind']] + ' (then the closest subcategory)',
                 'zip': s['main_zip'], 'service_area': f"{s['towns'][0]}, {s['state']}",
                 'other': 'If a street line is asked for, stop and note it: the claim it can be left blank rests on live listings, not the form.'})
    if s['domain'] in HVACFAST:
        rows.append({'directory': 'HVACServiceFast', **base, 'category': HVACFAST[s['domain']], 'zip': '',
                     'service_area': f"{s['state']}: " + ', '.join(s['towns']),
                     'other': 'Company name = business name. Leave Address, Google Maps link, Years of experience, License number and "I am insured" blank. No photos.'})
    if s['kind'] == 'dumpster':
        rows.append({'directory': 'RentADumpster.co', **base, 'category': 'Dumpster rental (roll-off)', 'zip': ' '.join(s['zips']),
                     'service_area': ', '.join(s['towns']),
                     'other': 'Yard location: the add step asks for one. If it insists on a street address, stop. Container sizes: leave blank. No photos.'})
with open(os.path.join(HERE, 'oct-top3', 'filing_sheet_batch1.csv'), 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader(); w.writerows(rows)

L = ['# Filing sheet: Kyle batch 1, the four no-address directories (25 Oct 2026)\n',
     'Everything needed to file the 10 batch 1 sites on the only four free directories that take a listing without a '
     'street address (see `COPYCAT-LINKS-BATCH1-2026-10-25.md`). **Nothing has been submitted.** The same data as one '
     'row per directory and site: `kyle-screen/oct-top3/filing_sheet_batch1.csv`.\n',
     '| Directory | Add page | Sites | Account |', '|---|---|---|---|',
     '| NearSpotUSA | https://nearspotusa.com/add-business | all 10 | none |',
     '| BizHwy | https://www.bizhwy.com/addlisting.php | all 10 | yes (email and password) |',
     '| HVACServiceFast | https://hvacservicefast.com/register-as-pro?new=1 | Marietta, Schaumburg, Wheaton | none (captcha) |',
     '| RentADumpster.co | https://rentadumpster.co/for-haulers/ | Bentonville, Wellington, Biloxi, Pensacola | yes (email and password) |',
     '\n**27 listings in all** (10 + 10 + 3 + 4). Ocala is left off HVACServiceFast: its service boxes have no dryer-vent option, '
     'and ticking an HVAC box would misdescribe the site.\n',
     '## Read before filing\n',
     '- **What the listings say.** Every description ends with the same line the sites carry on every page: independently '
     'operated advertising, not itself a contractor or hauler. The sites make no license, insurance, years or review '
     'claims, so the listings don\'t either. Leave every such field blank.',
     '- **Two of these are for working providers.** HVACServiceFast is a "register as a pro" form, and RentADumpster.co '
     'tells homeowners "We are not in the middle" and lists haulers by yard. Filing an advertising site there is a '
     'mismatch with what they\'re for. NearSpotUSA and BizHwy are general directories with no such premise. Whether to '
     'file the first two before a renter signs is Dan\'s call.',
     '- **No photos.** The site photos are AI-made stand-ins. Don\'t upload them as "photos of your work".',
     '- **Contact details** (not shown publicly; used to verify): use one inbox for all 27, for example a desk address. '
     'NearSpotUSA and HVACServiceFast also want a first and last name: the person filing.',
     '- **Phone checks.** RentADumpster.co goes live once the number is confirmed. The numbers ring the call-desk '
     'voicemail, so a code read out by an automated call is in the Telnyx recording.',
     '- **Hours:** none of the sites state hours. Leave them as "not specified".\n',
     '## Directory by directory\n',
     '**NearSpotUSA** (all 10): Business name, Category, ZIP (one), Phone, Website, Description. Leave Street address and '
     'Business email blank. Untick the marketing-email box.\n',
     '**BizHwy** (all 10): Business name, Category, State, then the next step. Pick the closest subcategory there '
     '(for example Waste Management, Duct Cleaning, Window Tinting, Septic). If it requires a street line, stop and '
     'note it.\n',
     '**HVACServiceFast** (3): First and last name, Company name, Website, Email, Phone; tick the services below; Service '
     'Area: pick the state, then tick each town; About your business: the description. Leave Address, Google Maps link, '
     'Years of experience, License number, "I am insured", logo and photos empty.\n',
     '**RentADumpster.co** (4): make the account, search for the business name (it won\'t be there), choose "Add it": '
     'company name, phone, yard location (stop if it insists on a street address), then the service ZIPs below.\n',
     '## Site by site\n']
for s in sites:
    L.append(f"### {s['brand']}\n")
    L.append('| Field | Value |')
    L.append('|---|---|')
    L.append(f"| Business name | {s['brand']} |")
    L.append(f"| Phone | {s['phone']} |")
    L.append(f"| Website | {s['website']} |")
    L.append(f"| Towns served | {', '.join(s['towns'])} ({s['county']} County, {s['state']}) |")
    L.append(f"| ZIP for NearSpotUSA and BizHwy | {s['main_zip']} |")
    if s['kind'] == 'dumpster':
        L.append(f"| Service ZIPs for RentADumpster.co ({len(s['zips'])}) | {' '.join(s['zips'])} |")
    else:
        L.append(f"| All service ZIPs ({len(s['zips'])}) | {' '.join(s['zips'])} |")
    L.append(f"| NearSpotUSA category | {NEARSPOT[s['kind']]} |")
    L.append(f"| BizHwy category | {BIZHWY[s['kind']]}, then the closest subcategory |")
    if s['domain'] in HVACFAST:
        L.append(f"| HVACServiceFast services | {HVACFAST[s['domain']]} |")
        L.append(f"| HVACServiceFast service area | {s['state']}: {', '.join(t for t in s['towns'] if t != 'East Cobb')} |")
    L.append(f"| Description ({len(s['description'])} characters) | {s['description']} |")
    L.append('')
L.append('## Where the ZIPs come from\n')
L.append('The towns are the ones each site names in its own "where we serve" copy. ZIPs are from the Census Bureau\'s '
         '2020 ZIP-to-town relationship file: a ZIP is listed if it covers at least 3% of the town\'s land or a '
         'quarter of the ZIP lies inside the town, which drops P.O.-box-only ZIPs and keeps the edges. Added by '
         'mailing name, because Census doesn\'t treat them as places: 30068 (East Cobb) and 32533 (Cantonment). '
         'Perdido Key falls in 32507. Dropped: 34240, the Sarasota County side of Lakewood Ranch, since the Bradenton '
         'site serves Manatee County. Data: `kyle-screen/oct-top3/site_zips_census2020.json`.\n')
open(os.path.join(REPO, 'FILING-SHEET-BATCH1-2026-10-25.md'), 'w').write('\n'.join(L) + '\n')
print(len(rows), 'rows;', ', '.join(f"{s['brand']} {len(s['zips'])} ZIPs" for s in sites))
