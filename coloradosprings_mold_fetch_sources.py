import json
import pplx_sdk
urls = [
  'https://leg.colorado.gov/bills/hb25-1202',
  'https://www.weather.gov/pub/climateCosDailyNormalsRecords',
  'https://coloradosprings.gov/system/files/2024-04/colorado_springs_2020-2024_conplan_amendment_3-comp.pdf',
  'https://coloradosprings.gov/system/files/2025-07/hna_co_springs_factsheet_2025_07_10a_lv.pdf',
  'https://www.epa.gov/mold/mold-cleanup-your-home'
]
result = pplx_sdk.content.fetch(urls, prompt='Extract the concrete facts relevant to Colorado Springs residential mold remediation: state licensing/registration status, climate annual precipitation, city housing construction age distribution, and EPA small-area versus professional remediation guidance. Include direct wording and figures only.')
out=[]
for r in result:
  out.append({
    'url':r.url, 'title':getattr(r,'title',None), 'error':getattr(r,'error',None), 'content':getattr(r,'content',None)
  })
path='/home/user/workspace/local-sites/coloradosprings_mold_sources_fetched.json'
with open(path,'w') as f: json.dump(out,f,indent=2)
print(path)
print(json.dumps(out,indent=2))
