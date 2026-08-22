import json
import pplx_sdk
urls = [
 'https://codes.ohio.gov/ohio-revised-code/section-2305.10',
 'https://codes.ohio.gov/ohio-revised-code/section-2315.33',
 'https://codes.ohio.gov/ohio-revised-code/section-2315.18',
 'https://www.courtclerk.org/civil-division/',
 'https://hamiltoncountycourts.org/index.php/common-pleas/',
 'https://dam.assets.ohio.gov/image/upload/otso.ohio.gov/DataSheets/Hamilton.pdf'
]
prompt = '''Extract the exact current provisions or official facts relevant to a Cincinnati Ohio personal injury website. For statutes, give section, operative rules and all important exceptions/thresholds. For the Hamilton County court sources, explain official court/clerk functions and civil case filing path. For the crash report, give stated year and total crash/injury/fatal counts. Quote closely and do not add legal conclusions.'''
res=pplx_sdk.content.fetch(urls,prompt=prompt,cache_enabled=False)
out=[]
for r in res:
 out.append({'url':r.url,'title':r.title,'error':r.error,'content':r.content})
open('/home/user/workspace/local-sites/research_cincinnati_pi_fetched.json','w').write(json.dumps(out,indent=2))
for r in out:
 print('\n###',r['url'],'\n',r['content'][:6000] if r['content'] else r['error'])
