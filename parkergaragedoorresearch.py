import json
import pplx_sdk
queries = [
  "Parker Colorado growth Town official", "Parker Colorado garage door permit official", 
  "Parker Colorado HOA architectural review garage door", "Parker Colorado metropolitan district official",
  "Parker Colorado housing median year built Census"
]
rows=[]
for entry in pplx_sdk.search.web_many(queries, limit_per_query=10):
    row={"query": entry.spec.get("query"), "ok": entry.ok}
    if entry.ok:
        row["hits"]=[dict(h) for h in entry.result]
    else:
        row["error"]=str(entry.error)
    rows.append(row)
with open('/home/user/workspace/local-sites/parkergaragedoorresearch-search.json','w') as f:
    json.dump(rows,f,indent=2)
