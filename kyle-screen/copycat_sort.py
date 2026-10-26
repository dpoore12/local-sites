"""Kyle's copycat method for Kyle batch 1: sort the top-3 competitors' backlinks into the ones
we can get free, and the rest.

Input: oct-top3/copycat_targets.json and oct-top3/copycat_raw/<competitor>.json (Ahrefs
all-backlinks, 1 per referring domain, live, spam already filtered out by Ahrefs).
Output: oct-top3/copycat_links.csv (every link, sorted) and a per-site summary on stdout.

Buckets:
  FREE       a directory, citation or review profile anyone can create or claim at no cost
  NICHE      a trade directory (tint shops, HVAC, restoration...) that lists businesses free,
             usually by claim or a submit form
  AUTO       a page generated automatically by an SEO tool, scraper or data broker; nothing to
             submit, it appears on its own once a site exists
  AVOID      link sellers, hacked WordPress pages, PBN networks and spam directories
  PAID       chamber or association membership, sponsorship, press release or guest post
  EARNED     editorial, podcast, news, award, supplier, web-designer or the competitor's own sites
  UNSORTED   not matched by any rule (reviewed by hand before the list is final)

usage (from kyle-screen/): python3 -I copycat_sort.py
"""
import csv, json, os, re
from collections import defaultdict
from urllib.parse import urlparse

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'oct-top3')

FREE = {
    'bbb.org': 'BBB business profile (free listing; accreditation is the paid part)',
    'yellowpages.com': 'YP free listing (also feeds dexknows.com and dk.yp.com)',
    'dexknows.com': 'via the YP free listing', 'yp.com': 'via the YP free listing',
    'birdeye.com': 'Birdeye review profile (free claim)',
    'chamberofcommerce.com': 'ChamberofCommerce.com free listing (not a real chamber)',
    'citysquares.com': 'CitySquares free listing', 'ibegin.com': 'iBegin free listing',
    '2findlocal.com': '2FindLocal free listing', 'loc8nearme.com': 'Loc8NearMe (free claim)',
    'bestprosintown.com': 'Best Pros in Town (free claim)', 'mylocalservices.com': 'MyLocalServices free listing',
    'provenexpert.com': 'ProvenExpert free profile', 'askmap.net': 'AskMap free listing',
    'freelistingusa.com': 'FreeListingUSA free listing', 'bizlistusa.com': 'BizListUSA free listing',
    'businesslistus.com': 'BusinessListUS free listing', 'qdexx.com': 'Qdexx free listing',
    'yellow411.org': 'Yellow411 free profile', 'topseobrands.com': 'TopSEObrands free profile',
    'procore.com': 'Procore contractor network profile (free)', 'contractorsup.com': 'ContractorsUp free listing',
    'towncontractors.com': 'TownContractors listing', 'repairhit.com': 'RepairHit listing',
    'mytowninc.net': 'MyTownInc listing', 'diyorbuylocal.com': 'DIYorBuyLocal listing',
    'nearspotusa.com': 'NearSpotUSA listing', 'thebuildermarket.com': 'The Builder Market listing',
    'regionaldirectory.us': 'Regional Directory listing', 'ocalabusinessdirectory.com': 'Ocala Business Directory listing',
    'localverifiedpros.com': 'Local Verified Pros listing', 'vendorroster.com': 'VendorRoster listing',
    'allthehomeservices.online': 'All the Home Services listing', 'demandconvert.com': 'DemandConvert directory listing',
    'cylex.us.com': 'Cylex free listing', 'hotfrog.com': 'Hotfrog free listing', 'brownbook.net': 'Brownbook free listing',
    'manta.com': 'Manta free listing', 'merchantcircle.com': 'MerchantCircle free listing',
    'showmelocal.com': 'ShowMeLocal free listing', 'ezlocal.com': 'EZlocal free listing',
    'alignable.com': 'Alignable free profile', 'n49.com': 'n49 free listing', 'storeboard.com': 'Storeboard free listing',
    'tupalo.com': 'Tupalo free listing', 'expressupdate.com': 'Data Axle free listing',
    'foursquare.com': 'Foursquare free listing', 'mapquest.com': 'MapQuest (via Foursquare/Yext)',
    'yelp.com': 'Yelp free business page', 'facebook.com': 'Facebook page', 'nextdoor.com': 'Nextdoor business page',
    'thumbtack.com': 'Thumbtack free profile (pay per lead)', 'angi.com': 'Angi free profile',
    'houzz.com': 'Houzz free profile', 'porch.com': 'Porch free profile', 'buildzoom.com': 'BuildZoom profile',
    'superpages.com': 'via the YP free listing', 'local.com': 'Local.com listing', 'hub.biz': 'Hub.biz free listing',
    'elocal.com': 'eLocal free listing', 'bing.com': 'Bing Places', 'apple.com': 'Apple Business Connect',
    'video-bookmark.com': 'social bookmark (free account)', 'linkedin.com': 'LinkedIn company page',
    'instagram.com': 'Instagram profile', 'youtube.com': 'YouTube channel', 'pinterest.com': 'Pinterest profile',
    'x.com': 'X profile', 'twitter.com': 'X profile', 'tiktok.com': 'TikTok profile', 'reddit.com': 'Reddit (post or comment)',
    'quora.com': 'Quora answer', 'medium.com': 'Medium post', 'about.me': 'about.me profile', 'linktr.ee': 'Linktree profile',
    'gravatar.com': 'Gravatar profile', 'sites.google.com': 'Google Sites page', 'blogspot.com': 'Blogger post',
    'wordpress.com': 'WordPress.com blog', 'tumblr.com': 'Tumblr post', 'weebly.com': 'Weebly page',
}
NICHE = {
    'tintfinder.com': 'tint shop directory', 'tintbrokers.com': 'tint shop directory', 'tintingsource.com': 'tint shop directory',
    'tintlaws.net': 'tint installer list', 'findwindowtint.com': 'tint shop directory', 'carwrapshops.com': 'wrap and tint directory',
    'autonetworkhub.com': 'auto services directory', 'autorepairdirectories.com': 'auto repair directory',
    'hvacservice.io': 'HVAC directory (claim)', 'hvacservicefast.com': 'HVAC directory', 'licensedhvacnearme.com': 'HVAC directory',
    'localac.net': 'HVAC directory', 'localcleaning.net': 'cleaning directory', 'localcleaner.net': 'cleaning directory',
    'cleanerin.com': 'cleaning directory', 'reputablecleaners.com': 'cleaning directory', 'topsprinkler.com': 'home services directory',
    'verifiedremediation.com': 'restoration directory', 'waterdamagedispatch.com': 'restoration directory',
    'restoration411.com': 'restoration directory', 'americanrestorationregistry.com': 'restoration directory',
    'wateresto.com': 'restoration directory', 'findmoldspecialists.com': 'mold directory', 'findmymoldguy.com': 'mold directory',
    'moldguide.com': 'mold directory', 'moldcompaniesnearme.net': 'mold directory', 'firerestorationnearme.net': 'restoration directory',
    'hoardinghousecleanup.com': 'cleanup directory', 'homerepair.expert': 'home repair directory',
    'americasbesthomeservices.com': 'home services directory', 'georgiainspectors.net': 'inspector directory',
    'myfavoritebuilder.com': 'contractor directory', 'homeservicebase.com': 'home services directory',
}
AUTO = {
    'siteprice.org', 'sitelike.org', 'seolium.com', 'klazify.com', 'similars.net', 'websiterace.com', 'ycm.info',
    'alljobs.info', 'pagesearch.net', 'wallpapers.pro', 'tunca.org', 'getwebsiteworth.com', 'bestwebstats.com',
    'allwebsitesdirectory.com', 'linkspreader.com', 'coldlytics.com', 'cortera.com', 'appsruntheworld.com', 'poidata.io',
    'enigma.com', 'intently.co', 'dandb.com', 'us-info.com', 'us-customerservices.com', 'openingtimes.co',
    'transparencycertified.com', 'writeradar.com', 'whoreallyowns.org', 'unitedstatescompanies.org', 'revdex.com',
    'revaliew.com', 'orlandodirections.com', 'sarasotadirections.com', 'companieshousemanager.com', 'wogibtswas.de',
    'homeblue.com', 'mypodcastdata.com', 'linksnatcher.com', 'findinfo.in', 'theface.in', 'getonline.co.in',
    'tattooreg.com', 'planoptica.com', 'salondiscover.com', 'websitedesign.com.tr', 'statshow.com', 'hypestat.com',
    'siteindices.com', 'websiteoutlook.com', 'site-stats.org', 'sur.ly', 'sitesimilar.net', 'sitelinks.info',
}
HACKED = re.compile(r'(wordpress|woocommerce|elementor|template-kit|-theme/|/theme|plugin|addon|/shop/page/|/tag/|/product|'
                    r'/portal/|/outlet/|/vault/|/depot/|/emporium/|/warehouse/|/hub/|/library/|/catalog|/gallery/|/collection/|'
                    r'/store/|/bazaar/|/lab/|/factory/|/downloads/|/archive/|/directory-website-list|/domain-list|/all/\d+|'
                    r'/page-[0-9a-f]{20,}|attachment_id|/slide1|hello-world|sample-page|test-page|/donate|/header/)', re.I)
AVOID_PAT = re.compile(r'(seo|backlink|dofollow|link-?build|domain-?rating|guest-?post|link-?directory|dark-side-links|'
                       r'increase-your-domain|way2check|homefinance\.co\.in|backlinksbank|backlinkstree|backlinkon|tyres?\.pro|'
                       r'bisprofit|newsblogsports|masihnyata|trendyhealthtimes|toponlinegambling|mp3fresh|kyourc|japrime|'
                       r'hostingersite)', re.I)
EARNED = {
    'podimo.com': 'podcast episode', 'poddtoppen.se': 'podcast listing', 'rephonic.com': 'podcast listing',
    'epageflip.net': 'magazine feature', 'daveandjennymarrs.com': 'TV show feature', 'localwebdesign.com': 'web designer portfolio',
    'startupwebsolutions.com.au': 'web designer page', 'nationaldisasterrecovery.org': 'article mention',
    'gunungbelanda.com': 'blog post',
}

FREE.update({d: 'free business listing' for d in (
    'find-us-here.com fyple.com geebo.com golocalezservices.com gravitysplash.com localhomeservicepros.com localtips.net '
    'pegasusdirectory.com ringmybiz.com trueen.com unitedstatesbd.com uscity.net yplocal.com yplocal.us whatsyourhours.com '
    'palscity.com couponler.com locabee.com businessesup.com bizidex.com bizbangboom.com agreatertown.com bizhwy.com '
    'digitalbusinessdirectory.online dealerbaba.com ecohubmap.com beeynet.com jacksonvilledirect.info pompano.guide '
    'lakecharles.com linkcenter.com townplanner.com letsknowit.com viesearch.com excellentcontractor.com '
    'homeimprovementfirms.com renovationsup.com usacleaningcompany.com reputablebusinesses.com handsdown.pro handsdown.ai '
    'swivl.tech fixhubs.net fixurbix.com gigopro.com prosonrecord.com trustedhearth.com macraesbluebook.com trustburn.com '
    'stylevore.com uscity.net yellowpagesdirectory.com').split()})
FREE.update({d: 'free profile or post on a free platform (Kyle: "you just need some activity")' for d in (
    'crunchbase.com beamstart.com bebee.com issuu.com mystrikingly.com webflow.io web.app yolasite.com webselfsite.net '
    'company.site mypixieset.com hashnode.dev diowebhost.com dsiblogger.com ka-blogs.com vocal.media writeupcafe.com '
    'articleted.com bresdel.com collcard.com boycat.co flokii.com buzzbii.com expatriates.com bsky.app deer.social').split()})
NICHE.update({d: 'dumpster and waste directory' for d in (
    'dumpsterlocate.com dumpsterrentalguide.com dumpstercomparison.com dumpster.co rentadumpster.co curbwaste.com '
    'wastebits.com wasterecyclingworkersweek.org needsdirt.com findtrashremoval.com').split()})
NICHE.update({d: 'septic, plumbing and drain directory' for d in (
    'findasepticservice.com findmysepticguy.com findsepticpros.com septicandwell.com septicspot.com septicsystemservice.fyi '
    'septictrust.com septicalternative.com septic.fyi needseptic.com flinspectors.net plumberdirectories.com plumberfinderusa.com '
    'plumbersden.com locateplumbers.com searchaplumber.com greasetraplocator.com restaurantdisposal.com clearmylanddirectory.com '
    'doineedaplumber.org earthworkscout.com dashpages.io homesquad.us miamilocalservices.com imovingtoflorida.com '
    'inclusivebusinessalliance.org').split()})
NICHE.update({d: 'cleaning, HVAC and home services directory' for d in (
    'chimscout.com findjanitor.com trustedhousecleaners.com powerwashmaps.com buildingdupage.com re-building.com '
    'nationalhomeauthority.org findkitchenhoodpros.com placeprofile.net').split()})
PAID = {}
PAID.update({d: 'chamber, association or sponsor listing (membership costs money)' for d in (
    'chambermaster.com growthzoneapp.com memberzone.com gochambermaster.com swflinc.com ms-bia.org cdbia.com tbba.net '
    'pepmobile.org quadca.com mbaaa.org suncoastba.org paradeofhomesinfo.com suncoastfoodandwinefest.com kennethyoung.org '
    'mobilechamber.com eschamber.com eschamber.org manateechamber.com navarrechamber.com pensacolachamber.com '
    'charlottecountychamber.org myponline.com theconstructioncenter.org').split()})
PAID.update({d: 'press release distribution' for d in (
    'globenewswire.com ezpr.org universalpressrelease.com thecrimsonreport.com thenewsuniverse.com glamorousnews.com '
    'nynewscast.com sproutnews.com thefinancialmetrics.com thebusinessgazetteonline.com uknewshour.com diverhaven.com '
    'topcoreidea.com releasewire.com').split()})
PAID.update({d: 'guest post on a blog or magazine (normally sold)' for d in (
    'elevatedmagazines.com emagazine.com entrepreneursbreak.com gritdaily.com havokjournal.com hnmagazine.co.uk laprogressive.com '
    'leadgrowdevelop.com livepositively.com luxurylifestyle.com mirrorreview.com mynewsgh.com nerdbot.com offthemrkt.com '
    'onrec.com onyamagazine.com pctechmag.com seaislenews.com speedwaymedia.com techbullion.com thebossmagazine.com '
    'thepinnaclelist.com urbanmatter.com urbansplatter.com wordstreetjournal.com upscalelivingmag.com london-post.co.uk '
    'paisley.org.uk swindonlink.com businessingmag.com businessoutstanders.com alltopstartups.com artdaily.cc artdaily.com '
    'breakingac.com businesnewswire.com dgmnews.com backstageviral.com dutable.com inpeaks.com inspiringmeme.com '
    'momwithfive.com letstalkmommy.com nancy-rubin.com ericabuteau.com blogwithmom.com hudsonfarmhouse.com terristeffes.com '
    'thededicatedhouse.com thehouseshop.com stacyknows.com thealphaparent.com simplehomely.uk handymantips.org flexhouse.org '
    'fredeo.com lakelandcurrents.com monomousumi.com eyesicon.com cleansway.com build-review.com housesumo.com prereal.com '
    'easier.com modernmississauga.com mikegingerich.com pinoybisnes.com businessdiary.com.ph nifnex.com.au '
    'planabettermortgage.com.au estatefy.com thespottedcatmagazine.com futurology.life inven.ai decasacollections.com '
    'atoallinks.com blogs.bangboxonline.com enact.solar redfin.com convesio.cloud stsilaslutheran.org travelingappetites.com '
    'upgrowth-agency.com erriveonline.com robertwalkerstudio.com utilitiesformyhome.com hampersandhiccups.com '
    'septicsafeproducts.hashnode.dev maxmo.media spiny.com builderswebsource.com buildingadream.com mecindustries.com '
    'planetamagic.com texwaywastewater.com withbanner.com sv.theleader.info ortablu.org slgdesign.jp').split()})
EARNED.update({d: 'news, encyclopedia, award or the competitor\'s own network' for d in (
    'wikipedia.org grokipedia.com explained.today recyclingtoday.com wastetodaymagazine.com siliconvalleyjournals.com '
    'abc3340.com qualitybusinessawards.com expertise.com threebestrated.com kredodesign.com adrianagency.com '
    'ecosouthservices.net bcleanllc.com dandhdumpsterrental.com ontimedumpsters.com onthemarkhvac.com '
    'indoorairductcleaning.com easycleanseptic.com septic911.com worryfreeservices.ca slicemiami.com eastphoenixau.com '
    'greencrescenttrail.org protocloudtechnologies.com thewebhelp.com photograph.expertphotography.com amcsgroup.com '
    'cgmimm.com bly.com').split()})
AUTO.update(set((
    'datanyze.com leadiq.com owler.com theorg.com acquirezy.com bubba.ai heybubba.ai vektortms.com dealmate.ai mustat.com '
    'urlm.co scam-detector.com willro.com example3.com que.com spotsnow.io us-business.info uahot.com snn.gr hiringcafe.com '
    'dailyremote.com mapcarta.com uswasteindex.com supplymatchms.com dlmpropertygroup.com phonebooks.com bizratings.com '
    'pensacoladirections.com trustfeed.com getlisteduae.com 101apartmentforrent.com 2getmarried.com alexanderformayor2026.com '
    'chi.vibary.net countyadvisoryboard.com').split()))

FREE.update({'techdirectory.io': 'TechDirectory free listing', 'whowhere.io': 'WhoWhere contractor listing',
             'broxer.com': 'Broxer free company profile'})
AUTO.update({'domainsystemsusa.com', 'diib.com', 'eurekster.com', 'gruntose.com', 'sabns.com'})


def root(host):
    host = host.lower().removeprefix('www.')
    for table in (FREE, NICHE, PAID, EARNED):
        for d in table:
            if host == d or host.endswith('.' + d):
                return d
    for d in AUTO:
        if host == d or host.endswith('.' + d):
            return d
    return host


def sort_link(url):
    host = urlparse(url).netloc.lower()
    r = root(host)
    if re.search(r'(#comment|replytocom=|/comment-page-|guestbook)', url, re.I):
        return 'FREE', 'blog comment', r
    if r in AUTO:
        return 'AUTO', '', r
    if AVOID_PAT.search(url):
        return 'AVOID', '', r
    if r in FREE:
        return 'FREE', FREE[r], r
    if r in NICHE:
        return 'NICHE', NICHE[r], r
    if r in PAID:
        return 'PAID', PAID[r], r
    if r in EARNED:
        return 'EARNED', EARNED[r], r
    if HACKED.search(urlparse(url).path):
        return 'AVOID', 'hacked or junk page', r
    return 'AVOID', 'unrelated site (hacked page or spam), checked by hand 25 Oct', r


if __name__ == '__main__':
    targets = json.load(open(os.path.join(HERE, 'copycat_targets.json')))
    rows = []
    for t in targets:
        f = os.path.join(HERE, t['file'])
        data = json.load(open(f)) if os.path.exists(f) else {'error': 'missing'}
        for b in data.get('backlinks', []):
            bucket, note, r = sort_link(b['url_from'])
            rows.append({'site': t['site'], 'competitor': t['competitor'], 'bucket': bucket, 'source': r,
                         'what': note, 'dr': b.get('domain_rating_source'), 'url_from': b['url_from']})
    with open(os.path.join(HERE, 'copycat_links.csv'), 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    by = defaultdict(lambda: defaultdict(int))
    for r in rows:
        by[r['site']][r['bucket']] += 1
    for s, c in by.items():
        print(f"{s:40s} " + '  '.join(f'{k} {c[k]}' for k in ('FREE', 'NICHE', 'PAID', 'AUTO', 'AVOID', 'EARNED', 'UNSORTED')))
    print('UNSORTED sources:')
    for src in sorted({(r['source'], r['url_from']) for r in rows if r['bucket'] == 'UNSORTED'}):
        print('  ', src[0], '|', src[1][:110])
