#!/usr/bin/env python3
"""Show the one-sentence-paragraph run (and openers) for a built page."""
import sys, importlib.util, os
ROOT = "/home/user/workspace/local-sites"
spec = importlib.util.spec_from_file_location("qc", os.path.join(ROOT, "qc.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

path = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else "onesent"
raw = open(os.path.join(ROOT, path)).read()
blocks = m.visible_blocks(raw)
prose = [(t, x) for t, x in blocks if t in ("p", "li") and len(x) > 40]
if mode == "onesent":
    run = 0
    for t, x in prose:
        if m.is_citation_ish(x):
            run = 0; print("--- citationish reset:", x[:60]); continue
        run = run + 1 if len(m.sentences(x)) == 1 else 0
        print(f"[{t} sents={len(m.sentences(x))} run={run}] {x[:200]}")
elif mode == "openers":
    for t, x in prose:
        print(f"[{m.words(x)[0].lower()}] {x[:140]}")
