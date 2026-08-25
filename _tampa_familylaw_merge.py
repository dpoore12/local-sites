#!/usr/bin/env python3
"""Merge the new phase-2 blocks into tampafamilylawattorneypros.com/copy.md."""
import json, re, pathlib, sys

ROOT = pathlib.Path(__file__).parent
DOM = "tampafamilylawattorneypros.com"
SITE = ROOT / "sites" / DOM
NEW = ROOT / "_tampa_familylaw_blocks.md"


def parse(text):
    out, key, buf = {}, None, []
    for line in text.splitlines():
        m = re.match(r"^## ([a-z0-9_]+)\s*$", line)
        if m:
            if key:
                out[key] = "\n".join(buf).strip()
            key, buf = m.group(1), []
        elif key is not None:
            buf.append(line)
    if key:
        out[key] = "\n".join(buf).strip()
    return out


new = parse(NEW.read_text())
copy_path = SITE / "copy.md"
text = copy_path.read_text()

# 1. replace existing blocks in place
for k in ["symptom_1", "symptom_2", "symptom_3", "symptom_4"]:
    pat = re.compile(r"(^## %s\n)(.*?)(?=^## )" % k, re.S | re.M)
    if not pat.search(text):
        sys.exit("could not find block " + k)
    text = pat.sub(lambda m: m.group(1) + new[k] + "\n\n", text)

# 2. append the new blocks
tail_keys = ["services_pick_head", "services_summary", "crosslink_head"]
for key in ["child_custody_attorney", "child_support_attorney",
            "paternity_attorney", "spousal_support_attorney"]:
    tail_keys += [f"svc_{key}_lede", f"svc_{key}_body"]

add = []
for k in tail_keys:
    if k in text:
        sys.exit("block already present: " + k)
    add.append(f"## {k}\n{new[k]}\n")
text = text.rstrip("\n") + "\n\n" + "\n".join(add)
copy_path.write_text(text)

# 3. flip phase
sp = SITE / "site.json"
raw = sp.read_text()
raw2 = raw.replace('"phase": 1', '"phase": 2', 1)
if raw2 == raw:
    print("WARN: phase field not flipped (already 2?)")
sp.write_text(raw2)

# 4. report word counts
c = parse(copy_path.read_text())
for k in tail_keys + ["symptom_1", "symptom_2", "symptom_3", "symptom_4"]:
    print(f"{len(c[k].split()):5d}  {k}")
print("phase =", json.loads(sp.read_text())["phase"])
