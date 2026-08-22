import json
import pplx_sdk
urls = [
  'https://www.dmv.ca.gov/portal/driver-education-and-safety/dmv-safety-guidelines-actions/driving-under-the-influence/',
  'https://santaclara.courts.ca.gov/divisions/criminal-division/criminal-case-records',
  'https://www.ots.ca.gov/rankings/santa-clara-county-2023/',
  'https://www.scscourt.org/general_info/contact/courthouses/hoj.shtml',
  'https://data.sanjoseca.gov/dataset/neighborhoods'
]
prompt = '''Extract the exact factual statements relevant to a San Jose DUI legal information site. For DMV: administrative per se, hearing deadline, and relation to criminal court. For the court: criminal venue/address and cities handled. For OTS: 2023 Santa Clara County crash totals and alcohol-involved figures. For neighborhood source: what it establishes about official neighborhood boundaries. Do not add outside facts.'''
results=pplx_sdk.content.fetch(urls,prompt=prompt,cache_enabled=False)
rows=[]
for r in results:
    rows.append({'url':r.url,'title':r.title,'content':r.content,'error':r.error})
with open('/home/user/workspace/local-sites/sanjose_dui_research_sources.json','w') as f:
    json.dump(rows,f,indent=2)
print(json.dumps(rows,indent=2))
