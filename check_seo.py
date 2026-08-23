#!/usr/bin/env python3
"""Confirm every live site is open to Google and has a working sitemap.
Run with NO credential attached."""
import os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
DIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
doms = sorted(d for d in os.listdir(DIST) if "." in d and os.path.isdir(os.path.join(DIST, d)))

def one(d):
    bad = []
    home = subprocess.run(["curl","-s","-m","25",f"https://{d}/"],capture_output=True,text=True).stdout
    if 'content="index, follow"' not in home: bad.append("home is not open to Google")
    r = subprocess.run(["curl","-s","-m","25",f"https://{d}/robots.txt"],capture_output=True,text=True).stdout
    if "Allow: /" not in r: bad.append("robots.txt blocks")
    if f"https://{d}/sitemap.xml" not in r: bad.append("robots.txt missing sitemap line")
    sm = subprocess.run(["curl","-s","-m","25",f"https://{d}/sitemap.xml"],capture_output=True,text=True).stdout
    if "<urlset" not in sm: bad.append("no sitemap")
    elif f"<loc>https://{d}/</loc>" not in sm: bad.append("sitemap missing home page")
    return d, bad

fails = 0
with ThreadPoolExecutor(max_workers=8) as p:
    for d, bad in p.map(one, doms):
        if bad:
            fails += 1
            print(f"FAIL {d:<44}{'; '.join(bad)}")
print(f"\n{len(doms)-fails} of {len(doms)} open to Google with a working sitemap")
sys.exit(1 if fails else 0)
