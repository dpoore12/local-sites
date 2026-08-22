import json
import pplx_sdk
urls=[
'https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=911.2',
'https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=3602.',
'https://www.stancounty.com/newsfeed/?storyid=20190814-agriculture',
'https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/socioeconomic-forecasts/2022/stanislaus-2022-a11y.pdf',
'https://www.stanislaus.courts.ca.gov/location/city-towers-courthouse-civil',
'https://www.modestoneighborhoods.com/directory-category/neighborhoods/'
]
r=pplx_sdk.content.fetch(urls, cache_enabled=False, prompt='Extract the specific factual statements, dates, and locations relevant to a Modesto California personal injury information website. Preserve statutory wording where relevant.')
rows=[]
for x in r:
    rows.append({'url':x.url,'title':x.title,'error':x.error,'content':x.content})
open('/home/user/workspace/local-sites/research_modesto_pi_sources.json','w').write(json.dumps(rows,indent=2))
print(json.dumps(rows,indent=2))
