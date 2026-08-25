#!/usr/bin/env python3
"""Show paragraph openers / one-sentence runs for a built page, using qc.py's own parsing."""
import sys, os, glob
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import qc

dom, page = sys.argv[1], sys.argv[2]
path = os.path.join(qc.DIST, dom, page.strip("/"), "index.html") if page.strip("/") else os.path.join(qc.DIST, dom, "index.html")
html = open(path, encoding="utf-8").read()
blocks = qc.visible_blocks(html)
prose = [(t, x) for t, x in blocks if t == "p" and x and not qc.is_citation_ish(x)]
for i, (t, x) in enumerate(prose):
    ns = len(qc.sentences(x))
    print(f"[{i}] sent={ns} words={len(qc.words(x))} :: {x[:110]}")

ops = [qc.words(x)[0].lower() for _, x in prose if qc.words(x)]
for i in range(len(ops)-2):
    if ops[i]==ops[i+1]==ops[i+2]:
        print("RUN at", i, ops[i])
