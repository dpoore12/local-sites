import json, re, pathlib

base = pathlib.Path("/home/user/workspace/local-sites")
site = base / "sites/jacksonvillewrongfuldeathlawyerpros.com"
copy = site / "copy.md"
blocks_file = base / "_jax_wd_blocks.md"


def parse(text):
    parts = re.split(r"(?m)^## (\w+)\s*$", text)
    head = parts[0]
    out = []
    for i in range(1, len(parts), 2):
        out.append((parts[i], parts[i + 1].strip("\n")))
    return head, out


cur_head, cur = parse(copy.read_text())
_, new = parse(blocks_file.read_text())
newd = dict(new)

order_after_closing = ["services_summary"]
order_at_end = ["services_pick_head", "crosslink_head"]
for svc in ["fatal_car_accident_claim", "fatal_work_accident_claim",
            "medical_negligence_death_claim", "wrongful_death_damages_claim"]:
    order_at_end += [f"svc_{svc}_lede", f"svc_{svc}_body"]

result = []
for k, v in cur:
    if k in newd and k.startswith("symptom"):
        v = newd[k]
    result.append((k, v))
    if k == "closing_cta":
        for nk in order_after_closing:
            result.append((nk, newd[nk]))
    if k == "emergency_note":
        for nk in order_at_end:
            result.append((nk, newd[nk]))

text = cur_head.rstrip("\n") + "\n\n"
for k, v in result:
    text += f"## {k}\n\n{v}\n\n"
copy.write_text(text.rstrip("\n") + "\n")

sj = site / "site.json"
d = json.loads(sj.read_text())
d["phase"] = 2
sj.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
print("keys:", [k for k, _ in result])
