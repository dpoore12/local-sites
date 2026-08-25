#!/usr/bin/env python3
"""List sentences >= LIMIT words in a site's copy.md and site.json."""
import sys, re, json, os

dom = sys.argv[1]
LIMIT = int(sys.argv[2]) if len(sys.argv) > 2 else 45
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sites", dom)

def sents(text):
    # crude split on sentence end
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(\"'\u201c])", text)
    return parts

def wc(s):
    return len(re.findall(r"\S+", s))

p = os.path.join(base, "copy.md")
if os.path.exists(p):
    for i, line in enumerate(open(p), 1):
        line = line.rstrip("\n")
        if not line.strip():
            continue
        for s in sents(line):
            if wc(s) >= LIMIT:
                print(f"copy.md:{i} ({wc(s)}w) {s}\n")

p = os.path.join(base, "site.json")
d = json.load(open(p))
def walk(o, path=""):
    if isinstance(o, dict):
        for k, v in o.items():
            walk(v, f"{path}.{k}")
    elif isinstance(o, list):
        for j, v in enumerate(o):
            walk(v, f"{path}[{j}]")
    elif isinstance(o, str):
        for s in sents(o):
            if wc(s) >= LIMIT:
                print(f"site.json {path} ({wc(s)}w) {s}\n")
walk(d)
