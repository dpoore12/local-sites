#!/usr/bin/env python3
"""Print prose paragraphs (with index, opener, word count, sentence count)
for a page, so flow findings can be located in source copy."""
import sys, os, glob
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import qc

dom = sys.argv[1]
want = sys.argv[2] if len(sys.argv) > 2 else None
base = os.path.join(qc.DIST, dom)
for p in sorted(glob.glob(os.path.join(base, "**", "*.html"), recursive=True)):
    rel = os.path.relpath(p, base)
    page = "/" + os.path.dirname(rel) if os.path.dirname(rel) else "/"
    if want and page != want:
        continue
    raw = open(p, encoding="utf-8").read()
    blocks = qc.visible_blocks(raw)
    prose = [(t, x) for t, x in blocks if t == "p"]
    print("=" * 20, page)
    for i, (t, x) in enumerate(prose):
        w = qc.words(x)
        ss = qc.sentences(x)
        long_s = [len(qc.words(s)) for s in ss]
        print(f"[{i}] words={len(w)} sents={len(ss)} maxsent={max(long_s) if long_s else 0} opener={w[0].lower() if w else ''} cite={qc.is_citation_ish(x)}")
        print("   ", x[:400])
