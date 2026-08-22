import json
import pplx_sdk
queries = [
  {'query':'California Government Claims Act 911.2 six months', 'domains':['leginfo.legislature.ca.gov']},
  {'query':'California Labor Code 3602 exclusive remedy workers compensation', 'domains':['leginfo.legislature.ca.gov']},
  {'query':'Stanislaus County agriculture food processing employment official report'},
  {'query':'Stanislaus Superior Court civil division Modesto official'},
  {'query':'Modesto California neighborhoods official'}
]
results = pplx_sdk.search.web_many(queries, limit_per_query=8)
rows=[]
for entry in results:
    row={'query':entry.spec, 'ok':entry.ok}
    if entry.ok:
        row['hits']=[dict(h) for h in entry.result]
    else:
        row['error']=str(entry.error)
    rows.append(row)
open('/home/user/workspace/local-sites/research_modesto_pi_search.json','w').write(json.dumps(rows,indent=2))
print(json.dumps(rows,indent=2))
