#!/usr/bin/env python3
"""Helper: dump visible prose blocks of a built page, using qc.py's parser."""
import sys, os, importlib.util
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("qcmod", os.path.join(ROOT, "qc.py"))
qc = importlib.util.module_from_spec(spec)
src = open(os.path.join(ROOT, "qc.py")).read().split("if __name__")[0]
qc.__dict__["__file__"] = os.path.join(ROOT, "qc.py")
exec(compile(src, "qc.py", "exec"), qc.__dict__)

dom = sys.argv[1]
page = sys.argv[2] if len(sys.argv) > 2 else "/"
path = os.path.join(ROOT, "dist", dom, page.strip("/"), "index.html")
raw = open(path).read()
blocks = qc.visible_blocks(raw)
pro = [x for t, x in blocks if t in ("p", "li")]
mode = sys.argv[3] if len(sys.argv) > 3 else "open"
if mode == "sent":
    for i, x in enumerate(pro):
        for s in qc.sentences(x):
            n = len(qc.words(s))
            if n > 44:
                print(i, n, "|", s[:400])
else:
    tot = len(qc.words(" ".join(pro)))
    print("total words", tot)
    for i, x in enumerate(pro):
        w = qc.words(x)
        print(i, len(w), "|", x[:110].replace("\n", " "))
