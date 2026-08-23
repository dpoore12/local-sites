import json
import pplx_sdk

queries = [
    "Colorado mold remediation licensing requirements",
    "Colorado DORA mold remediation license",
    "Colorado mold remediation regulation state license",
    "Colorado Springs mould housing median year built 2024",
    "El Paso County Colorado housing median year structure built",
    "Colorado Springs water damage mold public health"
]
results = pplx_sdk.search.web_many(queries, limit_per_query=10, concurrency=5)
out = []
for env in results:
    item = {"spec": env.spec, "ok": env.ok}
    if env.ok:
        item["hits"] = [dict(h) for h in env.result]
    else:
        item["error"] = str(env.error)
    out.append(item)
path = "/home/user/workspace/local-sites/coloradosprings_mold_research_round2.json"
with open(path, "w") as f:
    json.dump(out, f, indent=2)
print(path)
print(json.dumps(out, indent=2))
