import json
import pplx_sdk
queries = [
    {"query": "Santa Clara Superior Court DUI arraignment Hall Justice", "domains": ["scscourt.org"]},
    {"query": "California DMV administrative per se DUI hearing 10 days", "domains": ["dmv.ca.gov"]},
    {"query": "Santa Clara County DUI crash statistics California OTS", "domains": ["ots.ca.gov"]},
    {"query": "Santa Clara County DUI arrest data official", "domains": ["ca.gov"]},
    {"query": "San Jose neighborhoods official city", "domains": ["sanjoseca.gov"]}
]
results = pplx_sdk.search.web_many(queries, limit_per_query=10)
rows=[]
for entry in results:
    row={"query": entry.spec, "ok": entry.ok}
    if entry.ok:
        row["hits"]=[dict(h) for h in entry.result]
    else:
        row["error"]=str(entry.error)
    rows.append(row)
with open('/home/user/workspace/local-sites/sanjose_dui_research_search.json','w') as f:
    json.dump(rows,f,indent=2)
print(json.dumps(rows,indent=2))
