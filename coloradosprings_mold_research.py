import json
import pplx_sdk

queries = [
    {"query": "Colorado mold remediation license state", "domains": ["co.gov"]},
    {"query": "Colorado Springs climate average humidity precipitation", "domains": ["weather.gov"]},
    {"query": "Colorado Springs home median year built", "domains": ["censusreporter.org", "census.gov"]},
    {"query": "Colorado Springs neighborhoods official", "domains": ["coloradosprings.gov"]},
    {"query": "Colorado Springs snowmelt flooding April", "domains": ["coloradosprings.gov", "weather.gov", "elpasoco.com"]}
]
results = pplx_sdk.search.web_many(queries, limit_per_query=8, concurrency=5)
out = []
for envelope in results:
    entry = {"spec": envelope.spec, "ok": envelope.ok}
    if envelope.ok:
        entry["hits"] = [dict(h) for h in envelope.result]
    else:
        entry["error"] = str(envelope.error)
    out.append(entry)
path = "/home/user/workspace/local-sites/coloradosprings_mold_research_search.json"
with open(path, "w") as f:
    json.dump(out, f, indent=2)
print(path)
print(json.dumps(out, indent=2))
