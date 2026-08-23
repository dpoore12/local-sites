import re, sys, pathlib, itertools, collections
ROOT = pathlib.Path(__file__).resolve().parent
SITES = ROOT / "sites"
DOMS = ["salinascaraccidentlawyer.com","santabarbaracaraccidentlawyer.com",
        "victorvillecaraccidentlawyerpros.com","westcovinacaraccidentlawyerpros.com",
        "virginiabeachcaraccidentlawyerpros.com"]

def norm(t):
    t = re.sub(r"[^a-z0-9\s]", " ", t.lower())
    return t.split()

def shingles(dom):
    txt = (SITES/dom/"copy.md").read_text()
    w = norm(txt)
    return {" ".join(w[i:i+15]): i for i in range(len(w)-14)}

S = {d: shingles(d) for d in DOMS}
for a, b in itertools.combinations(DOMS, 2):
    common = set(S[a]) & set(S[b])
    if common:
        print(f"=== {a} <-> {b}: {len(common)}")
        for c in sorted(common):
            print("   ", c)
