import json
import pplx_sdk
queries = [
    'Ohio Revised Code 2305.10 personal injury two years',
    'Ohio Revised Code 2315.33 comparative fault 51 percent',
    'Ohio Revised Code 2315.18 noneconomic damages cap',
    'Hamilton County Ohio Court Common Pleas civil division personal injury',
    'Hamilton County Ohio municipal court civil division jurisdiction',
    'Cincinnati Ohio neighborhoods official city',
    'Ohio traffic crash facts Hamilton County 2024 official'
]
results = pplx_sdk.search.web_many(queries, limit_per_query=7)
out=[]
for q, env in zip(queries, results):
    rows=[]
    if env.ok:
        for h in env.result:
            rows.append(dict(h))
    out.append({'query':q,'results':rows})
path='/home/user/workspace/local-sites/research_cincinnati_pi_search.json'
with open(path,'w') as f: json.dump(out,f,indent=2)
print(path)
for item in out:
    print('\nQUERY',item['query'])
    for h in item['results'][:5]: print(h['title'],h['url'])
