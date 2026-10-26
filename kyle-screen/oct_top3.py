"""Step one, finished: size up the top 3 page-one sites in each of the 191 clean Kyle markets.

Kyle (Koerner ep. 296 / Doser interview) looks at the top three results for the search in that
city and checks their authority, backlinks, content, pictures and headings, then builds only
where they are weak. This pulls a fresh Google page one located in each city (DataForSEO,
desktop, top 10 + map pack) and saves it to oct-top3/serp/<n>.json. Resumable.

usage (from kyle-screen/):  python3 -I oct_top3.py serp
"""
import base64, json, os, sys, time, urllib.request, concurrent.futures as cf

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'oct-top3')
ENV = dict(l.strip().split('=', 1) for l in open(os.path.expanduser('~/.dataforseo.env')) if '=' in l)
AUTH = 'Basic ' + base64.b64encode(f"{ENV['DATAFORSEO_LOGIN']}:{ENV['DATAFORSEO_PASSWORD']}".encode()).decode()

DIRECTORIES = {
    'yelp.com', 'reddit.com', 'thumbtack.com', 'angi.com', 'homeadvisor.com', 'bbb.org', 'nextdoor.com',
    'facebook.com', 'mapquest.com', 'yellowpages.com', 'porch.com', 'houzz.com', 'tripadvisor.com',
    'indeed.com', 'craigslist.org', 'manta.com', 'birdeye.com', 'expertise.com', 'threebestrated.com',
    'superpages.com', 'chamberofcommerce.com', 'buildzoom.com', 'angieslist.com', 'trustpilot.com',
    'instagram.com', 'tiktok.com', 'youtube.com', 'pinterest.com', 'linkedin.com', 'x.com', 'twitter.com',
    'apple.com', 'google.com', 'dexknows.com', 'citysearch.com', 'local.com', 'yellowbook.com', 'opendi.us',
    'cylex.us.com', 'hotfrog.com', 'brownbook.net', 'wikipedia.org', 'carwise.com', 'repairpal.com',
    'openbay.com', 'fixr.com', 'homeguide.com', 'networx.com', 'modernize.com', 'hometownlocal.com',
    'homes.com', 'realtor.com', 'zillow.com', 'trulia.com', 'redfin.com', 'bark.com', 'quora.com',
    'alignable.com', 'loc8nearme.com', 'showmelocal.com', 'merchantcircle.com', 'n49.com', 'storeboard.com',
    'ezlocal.com', 'yahoo.com', 'bing.com', 'mapsus.net', 'cityseeker.com', 'allbiz.com', 'buzzfile.com',
    'bizapedia.com', 'dandb.com', 'zoominfo.com', 'thebluebook.com', 'procore.com', 'birdeye.com',
}
NATIONAL = {  # national brands / franchise lead sites: real competitors, but not "Joe, Bill and Steve"
    'budgetdumpster.com', 'dumpsters.com', 'hometowndumpsterrental.com', 'wm.com', 'republicservices.com',
    'waste-management.com', '1800gotjunk.com', 'junk-king.com', 'collegehunkshaulingjunk.com',
    'safelite.com', 'glass.com', 'ziebart.com', 'llumar.com', 'chimneysafety.org', 'csia.org', 'nadca.com',
    'servicemaster.com', 'servpro.com', 'mrrooter.com', 'rotorooter.com', 'stanleysteemer.com',
    'ductz.com', 'dryerventwizard.com', 'chimneyrx.com', 'aaa.com', 'honktowing.com', 'thedumpsterguyusa.com',
}


def site_kind(domain):
    base = domain
    if any(base == d or base.endswith('.' + d) for d in DIRECTORIES):
        return 'directory'
    if any(base == d or base.endswith('.' + d) for d in NATIONAL):
        return 'national'
    if base.endswith('.gov') or base.endswith('.edu'):
        return 'gov/edu'
    return 'site'


def post(path, body):
    req = urllib.request.Request('https://api.dataforseo.com' + path, data=json.dumps(body).encode(),
                                 headers={'Authorization': AUTH, 'Content-Type': 'application/json'})
    return json.loads(urllib.request.urlopen(req, timeout=120).read())


def markets():
    states = {c['state']: c['state_full'] for c in json.load(open(os.path.join(HERE, 'cities.json')))}
    rows = [r for r in json.load(open(os.path.join(HERE, 'kyle-screen.json'))) if r['name_conflict'] == 'clean']
    for r in rows:
        r['state_full'] = states[r['state']]
    return rows


def fetch_serp(i, m):
    f = os.path.join(OUT, 'serp', f'{i}.json')
    if os.path.exists(f):
        return i, 'cached'
    body = [{'keyword': m['query'], 'location_name': f"{m['city']},{m['state_full']},United States",
             'language_code': 'en', 'device': 'desktop', 'depth': 10}]
    for attempt in range(4):
        try:
            t = post('/v3/serp/google/organic/live/advanced', body)['tasks'][0]
            if t.get('status_code') != 20000:
                if attempt == 3:
                    return i, f"ERR {t.get('status_code')} {t.get('status_message')}"
                time.sleep(3 + attempt * 3)
                continue
            items = t['result'][0].get('items') or []
            organic, pack = [], []
            for x in items:
                if x.get('type') == 'organic':
                    d = (x.get('domain') or '').lower().removeprefix('www.')
                    organic.append({'pos': x.get('rank_group'), 'domain': d, 'url': x.get('url'),
                                    'title': x.get('title'), 'kind': site_kind(d)})
                elif x.get('type') == 'local_pack':
                    pack.append({'title': x.get('title'), 'domain': (x.get('domain') or '').lower().removeprefix('www.'),
                                 'rating': (x.get('rating') or {}).get('value'),
                                 'reviews': (x.get('rating') or {}).get('votes_count')})
            json.dump({**m, 'organic': organic, 'map_pack': pack, 'fetched': time.strftime('%Y-%m-%d')},
                      open(f, 'w'), indent=1)
            return i, f'ok {len(organic)} organic, {len(pack)} in map pack'
        except Exception as e:
            if attempt == 3:
                return i, f'FAIL {type(e).__name__}'
            time.sleep(3 + attempt * 3)


def fetch_pages(urls):
    """Content, pictures and headings of each top-3 page (Kyle's other checks). 20 per request."""
    f = os.path.join(OUT, 'pages.json')
    done = json.load(open(f)) if os.path.exists(f) else {}
    todo = [u for u in urls if u not in done]
    def run(chunk):
        body = [{'url': u, 'enable_javascript': False} for u in chunk]
        out = {}
        try:
            for t in post('/v3/on_page/instant_pages', body).get('tasks') or []:
                u = (t.get('data') or {}).get('url')
                item = ((t.get('result') or [{}])[0].get('items') or [None])[0] if t.get('result') else None
                if not u:
                    continue
                if not item:
                    out[u] = {'error': t.get('status_message')}
                    continue
                meta = item.get('meta') or {}
                h = meta.get('htags') or {}
                out[u] = {'status': item.get('status_code'),
                          'words': (meta.get('content') or {}).get('plain_text_word_count'),
                          'images': meta.get('images_count'),
                          'h1': len(h.get('h1') or []), 'h2': len(h.get('h2') or []), 'h3': len(h.get('h3') or []),
                          'title': meta.get('title')}
        except Exception as e:
            for u in chunk:
                out[u] = {'error': type(e).__name__}
        return out
    chunks = [todo[i:i + 20] for i in range(0, len(todo), 20)]
    with cf.ThreadPoolExecutor(max_workers=4) as ex:
        for out in ex.map(run, chunks):
            done.update(out)
            json.dump(done, open(f, 'w'), indent=0)
    return done


if __name__ == '__main__':
    os.makedirs(os.path.join(OUT, 'serp'), exist_ok=True)
    ms = markets()
    print(len(ms), 'clean markets')
    if sys.argv[1:] == ['pages']:
        urls = []
        for i in range(len(ms)):
            d = json.load(open(os.path.join(OUT, 'serp', f'{i}.json')))
            urls += [o['url'] for o in sorted(d['organic'], key=lambda o: o['pos'] or 99)[:3]
                     if o['kind'] in ('site', 'national')]
        urls = sorted(set(urls))
        got = fetch_pages(urls)
        print(len(urls), 'top-3 pages;', sum(1 for u in urls if 'words' in got.get(u, {})), 'read')
    if sys.argv[1:] == ['serp']:
        bad = 0
        with cf.ThreadPoolExecutor(max_workers=4) as ex:
            for i, s in ex.map(lambda a: fetch_serp(*a), enumerate(ms)):
                if not s.startswith(('ok', 'cached')):
                    bad += 1
                    print(i, ms[i]['query'], s, flush=True)
        print('done; problems:', bad)
