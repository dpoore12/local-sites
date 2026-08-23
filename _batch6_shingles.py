import re, pathlib, sys, collections

SH = 15
root = pathlib.Path("/home/user/workspace/local-sites/sites")

def parse(md):
    c, key, buf = {}, None, []
    for line in md.splitlines():
        m = re.match(r"^##\s+(\w+)\s*$", line)
        if m:
            if key: c[key] = "\n".join(buf).strip()
            key, buf = m.group(1), []
        elif key is not None:
            buf.append(line)
    if key: c[key] = "\n".join(buf).strip()
    return c

def shingles(domain):
    c = parse((root / domain / "copy.md").read_text())
    authored = " ".join(str(v) for k, v in sorted(c.items()))
    low = re.findall(r"[a-z0-9']+", authored.lower())
    return {" ".join(low[i:i+SH]) for i in range(len(low)-SH+1)}

mine_doms = sys.argv[1:]
all_doms = sorted(d.name for d in root.iterdir() if (d / "copy.md").exists())
others = {d: shingles(d) for d in all_doms}
for d in mine_doms:
    m = others[d]
    print("="*20, d)
    for o in all_doms:
        if o == d: continue
        hits = m & others[o]
        if hits:
            print(f"-- vs {o} ({len(hits)})")
            for h in sorted(hits): print("   ", h)
