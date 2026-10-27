"""Page one (desktop, located in the town, top 10 + map pack) for every high-value trade/town pair:
Google Ads CPC >= $15 and 50+ searches a month. Reuses oct_top3's directory/national lists.
Saves trades2/serp/<n>.json. Resumable. Research only."""
import json, os, sys, concurrent.futures as cf
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import oct_top3 as o
o.NATIONAL |= {'mrrooter.com', 'rotorooter.com', 'benjaminfranklinplumbing.com', 'mrelectric.com', 'mistersparky.com',
               'onehourheatandair.com', 'aireserv.com', 'terminix.com', 'orkin.com', 'truly-nolen.com', 'aptive.com',
               'rentokil.com', 'overheaddoor.com', 'precisiondoor.net', 'garagedoorsandmore.com', 'renewalbyandersen.com',
               'windownation.com', 'pella.com', 'andersenwindows.com', 'champion.com', 'championwindow.com', 'leaffilter.com',
               'gutterhelmet.com', 'servpro.com', 'puroclean.com', 'paulDavis.com', 'pauldavis.com', '911restoration.com',
               'rainbowrestores.com', 'belfor.com', 'ramjack.com', 'olshanfoundation.com', 'groundworks.com', 'thrasher.com',
               'basementsystems.com', 'mrhandyman.com', 'homedepot.com', 'lowes.com', 'searshomeservices.com', 'lennox.com',
               'carrier.com', 'trane.com', 'davey.com', 'bartlett.com', 'monstertreeservice.com', 'mosquitojoe.com',
               '1800gotjunk.com', 'popalock.com', 'mrappliance.com', 'roofle.com', 'modernize.com', 'angi.com'}
OUT = os.path.join(HERE, 'serp')
os.makedirs(OUT, exist_ok=True)
T = ['emergency plumber', 'drain cleaning', 'garage door repair', 'foundation repair', 'ac repair', 'basement waterproofing',
     'water damage restoration', 'window replacement', 'roof repair', 'siding repair', 'plumber', 'gutter installation',
     'furnace repair', 'septic tank pumping', 'pest control', 'mold removal', 'air duct cleaning', 'roofing contractor',
     'termite treatment', 'water heater installation', 'tree removal', 'junk removal', 'electrician']
g = json.load(open(os.path.join(HERE, '..', 'grid-scored.json'))) + json.load(open(os.path.join(HERE, 'grid2.json')))
ms = sorted([dict(x, query=x['q'], lead_value=round((x['vol'] or 0) * (x['cpc'] or 0)))
             for x in g if x['niche'] in T and (x.get('vol') or 0) >= 50 and (x.get('cpc') or 0) >= 15],
            key=lambda x: x['q'])
o.OUT = HERE
bad = 0
with cf.ThreadPoolExecutor(max_workers=6) as ex:
    for i, s in ex.map(lambda a: o.fetch_serp(*a), enumerate(ms)):
        if not s.startswith(('ok', 'cached')):
            bad += 1; print(i, ms[i]['query'], s, flush=True)
json.dump(ms, open(os.path.join(HERE, 'markets2.json'), 'w'))
print(len(ms), 'markets; problems:', bad)
