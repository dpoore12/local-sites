import re, pathlib, sys
d = pathlib.Path("/home/user/workspace/local-sites/sites")
def toks(t):
    return re.findall(r"[a-z0-9]+", t.lower())
mine = toks((d/"parkergaragedoorrepairexperts.com/copy.md").read_text())
mg = {}
for i in range(len(mine)-14):
    mg.setdefault(" ".join(mine[i:i+15]), i)
for f in sorted(d.glob("*/copy.md")):
    if "parkergarage" in str(f): continue
    o = toks(f.read_text())
    og = set(" ".join(o[i:i+15]) for i in range(len(o)-14))
    hits = sorted(mg.keys() & og, key=lambda g: mg[g])
    if hits:
        print("==", f.parent.name, len(hits))
        for h in hits: print("   ", h)
