"""Write COPYCAT-LINKS-BATCH1-2026-10-25.md from kyle-screen/oct-top3/copycat_links.csv.

Splits the FREE and NICHE links into: one core list every site should copy, trade lists, and
per-site extras. Directories for other trades (mold, water damage, janitorial) are dropped, and
free profile or post platforms are kept apart because they're the spammy end of "activity".

usage (from the repo root): python3 -I kyle-screen/copycat_report.py
"""
import csv, json, os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
rows = list(csv.DictReader(open(os.path.join(HERE, 'oct-top3', 'copycat_links.csv'))))
comp = json.load(open(os.path.join(HERE, 'oct-top3', 'copycat_competitors.json')))

OFF_TRADE = set('verifiedremediation.com waterdamagedispatch.com moldguide.com findmymoldguy.com restoration411.com '
                'americanrestorationregistry.com findmoldspecialists.com findkitchenhoodpros.com firerestorationnearme.net '
                'georgiainspectors.net moldcompaniesnearme.net hoardinghousecleanup.com wateresto.com findjanitor.com '
                'trustedhousecleaners.com'.split())
PLATFORM = set('about.me mypixieset.com yolasite.com vocal.media writeupcafe.com bresdel.com flokii.com articleted.com '
               'collcard.com buzzbii.com diowebhost.com ka-blogs.com dsiblogger.com weebly.com webflow.io web.app '
               'mystrikingly.com webselfsite.net boycat.co bsky.app deer.social hashnode.dev issuu.com company.site '
               'beamstart.com bebee.com crunchbase.com expatriates.com geebo.com video-bookmark.com'.split())
HVAC = set('hvacservice.io localac.net hvacservicefast.com localcleaning.net localcleaner.net homeservicebase.com '
           'licensedhvacnearme.com cleanerin.com reputablecleaners.com powerwashmaps.com chimscout.com'.split())
DUMPSTER = set('curbwaste.com dumpsterlocate.com dumpsterrentalguide.com dumpstercomparison.com dumpster.co rentadumpster.co '
               'wastebits.com wasterecyclingworkersweek.org needsdirt.com findtrashremoval.com'.split())
YP = {'yellowpages.com', 'dexknows.com', 'yp.com', 'superpages.com'}

good = [r for r in rows if r['bucket'] in ('FREE', 'NICHE') and r['source'] not in OFF_TRADE]
by_src = defaultdict(lambda: {'sites': set(), 'comps': set(), 'what': '', 'url': '', 'dr': 0.0})
site_url = {}
for r in good:
    s = 'yellowpages.com' if r['source'] in YP else r['source']
    k = (r['site'], s)
    if k not in site_url or float(r['dr'] or 0) > site_url[k][0]:
        site_url[k] = (float(r['dr'] or 0), r['url_from'])
    v = by_src[s]
    v['sites'].add(r['site']); v['comps'].add(r['competitor']); v['what'] = v['what'] or r['what']
    if float(r['dr'] or 0) >= v['dr']:
        v['dr'] = float(r['dr'] or 0); v['url'] = r['url_from']
by_src['yellowpages.com']['what'] = 'YP free listing (one listing also shows on dexknows.com and dk.yp.com)'
core = sorted([s for s, v in by_src.items() if len(v['sites']) >= 3 and s not in HVAC | DUMPSTER | PLATFORM],
              key=lambda s: (-len(by_src[s]['sites']), -by_src[s]['dr']))
hvac = sorted([s for s in by_src if s in HVAC], key=lambda s: -by_src[s]['dr'])
dump = sorted([s for s in by_src if s in DUMPSTER], key=lambda s: -by_src[s]['dr'])
shared = set(core) | set(hvac) | set(dump)
counts = defaultdict(lambda: defaultdict(int))
for r in rows:
    counts[r['site']][r['bucket']] += 1
off = defaultdict(int)
for r in rows:
    if r['bucket'] in ('FREE', 'NICHE') and r['source'] in OFF_TRADE:
        off[r['site']] += 1

L = []
L.append('# Kyle\'s copycat links for Kyle batch 1 (25 Oct 2026)\n')
L.append('Kyle\'s most-used link method: look up the backlinks of the sites already ranking and copy the free '
         'ones. For each of the 10 batch 1 sites this pulls the backlinks of the top 3 business sites on page one '
         'for its main search (directories like Yelp and Angi skipped as "competitors"), from Ahrefs, one link per '
         'linking site, live links only, Ahrefs\' own spam flag filtered out.\n')
L.append('- Data: `kyle-screen/oct-top3/copycat_raw/` (30 pulls), every link sorted in '
         '`kyle-screen/oct-top3/copycat_links.csv`. Scripts: `kyle-screen/copycat_sort.py`, `copycat_report.py`.')
L.append('- Cost: 7,294 Ahrefs units out of the 200,000 a month; 21,464 are left until it resets on 5 Nov. Nothing was signed up for.')
L.append('- Five competitors returned exactly 100 links, Ahrefs\' cap for this call. Links come sorted strongest first, '
         'so only the weakest tail of those five is missing.\n')
L.append('## What the 30 competitors\' links actually are\n')
L.append('| Site | Free listings | Trade directories | Paid (chambers, PR, guest posts) | Auto-made pages | Spam or hacked | Editorial |')
L.append('|---|---:|---:|---:|---:|---:|---:|')
for s in comp:
    c = counts[s]
    L.append(f"| {s} | {c['FREE']} | {c['NICHE']} | {c['PAID']} | {c['AUTO']} | {c['AVOID']} | {c['EARNED']} |")
L.append('\nThe plain reading: these competitors have almost no real links. What they do have is a stack of '
         'directory listings, and that stack is what we copy. **No blog-comment links turned up for any of the '
         '30**, so the "blog comments" half of Kyle\'s copycat method has nothing to copy in these markets.\n')
L.append('"Auto-made pages" are SEO-tool and data-broker pages (siteprice, sitelike, Crunchbase-style scrapers) that '
         'appear on their own once a site exists. "Spam or hacked" are link sellers and hacked WordPress pages. '
         'Both are left alone. The paid ones need money (chamber dues, press releases, sold guest posts) and are '
         'outside this list.\n')
L.append('## Before anyone files: the address problem\n')
L.append('Most of these directories ask for a street address, and several check it by phone, postcard or a matching '
         'Google listing. A rank-and-rent site has no office. Some accept a service-area business with the address hidden, '
         'some don\'t. Listing a made-up address breaks most directories\' terms and is the same problem as a fake '
         'Business Profile. Whether to list with a real address (a client\'s, a virtual office), list only where the '
         'address can be hidden, or skip is Dan\'s call. The "free" label below means the listing costs nothing, '
         'not that it needs no address.\n')
L.append(f'## Core list: copy these for all 10 sites ({len(core)})\n')
L.append('Each of these lists competitors in 3 or more of the 10 markets.\n')
L.append('| # | Directory | What it is | Markets where competitors use it | Example competitor listing |')
L.append('|---:|---|---|---:|---|')
for i, s in enumerate(core, 1):
    v = by_src[s]
    L.append(f"| {i} | {s} | {v['what']} | {len(v['sites'])} | {v['url']} |")
L.append(f'\n## Trade lists\n')
L.append(f'**Air duct and dryer vent** (Ocala, Marietta, Schaumburg, Wheaton), {len(hvac)}: ' +
         ', '.join(f"{s} ({by_src[s]['what']})" for s in hvac) + '\n')
L.append(f'**Dumpster rental** (Bentonville, Wellington, Biloxi, Pensacola), {len(dump)}: ' +
         ', '.join(f"{s} ({by_src[s]['what']})" for s in dump) + '\n')
L.append('## Per site: extra free listings only that market\'s competitors have\n')
L.append('"Free profiles and posts" are free accounts on blog and profile platforms (Weebly, Strikingly, Vocal, '
         'Crunchbase…). Kyle would count them as "activity". Google\'s spam policy names low-quality directory, '
         'bookmark and mass-made pages as link spam, so they\'re listed apart and are the last thing to do, if at all.\n')
for s, info in comp.items():
    extra = sorted([k for k, v in by_src.items() if s in v['sites'] and k not in shared], key=lambda k: -by_src[k]['dr'])
    dirs = [k for k in extra if k not in PLATFORM]
    plats = [k for k in extra if k in PLATFORM]
    cs = ', '.join(c['domain'] for c in info['competitors'])
    L.append(f"### {s}\n")
    L.append(f"Search: \"{info['query']}\". Competitors copied: {cs}.\n")
    trade = 'the air duct list' if s in ('dryerventcleaningocala.com', 'mariettaairductcleaningpros.com', 'schaumburgairductcleaningpros.com', 'wheatonairductcleaningpros.com') \
        else 'the dumpster list' if 'dumpster' in s else 'no trade list'
    L.append(f"Copy: the core list, {trade}, and these {len(dirs)} directories:\n")
    if dirs:
        for k in dirs:
            v = by_src[k]
            dr, url = site_url[(s, k)]
            L.append(f"- **{k}** ({v['what']}, DR {dr:g}): {url}")
    else:
        L.append('- none beyond the core list')
    if plats:
        L.append(f"\nFree profiles and posts ({len(plats)}): " + ', '.join(plats))
    if off[s]:
        L.append(f"\nLeft out: {off[s]} mold, water-damage or janitorial directories from competitors' other trades.")
    L.append('')
addr = os.path.join(HERE, 'oct-top3', 'address_check_summary.md')
if os.path.exists(addr):
    i = next(n for n, line in enumerate(L) if line.startswith('## Core list'))
    L[i:i] = [open(addr).read()]
open(os.path.join(REPO, 'COPYCAT-LINKS-BATCH1-2026-10-25.md'), 'w').write('\n'.join(L) + '\n')
print('core', len(core), '| hvac', len(hvac), '| dumpster', len(dump))
for s in comp:
    extra = [k for k, v in by_src.items() if s in v['sites'] and k not in shared]
    print(f"{s:40s} extras {len([k for k in extra if k not in PLATFORM])} directories + {len([k for k in extra if k in PLATFORM])} platforms")
