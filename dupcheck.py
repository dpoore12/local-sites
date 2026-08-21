import re, sys, json, pathlib
sys.path.insert(0, "template")
import importlib.util
spec = importlib.util.spec_from_file_location("b", "template/build.py")
b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)

def norm(t):
    return [w.lower() for w in re.sub(r"\s+"," ", re.sub(r"<[^>]+>"," ", t)).split()]

fw = pathlib.Path("sites/fortworthgaragedoorrepairpros.com/copy.md").read_text()
nap = pathlib.Path("sites/garagedoorrepairnapervillepros.com/copy.md").read_text()
fwb = b.parse_copy(pathlib.Path("sites/fortworthgaragedoorrepairpros.com/copy.md"))
napb = b.parse_copy(pathlib.Path("sites/garagedoorrepairnapervillepros.com/copy.md"))
N=15
def sh(words): return {" ".join(words[i:i+N]) for i in range(len(words)-N+1)}
napall = set()
for v in napb.values(): napall |= sh(norm(v))
bad=[]
for k,v in fwb.items():
    hits = sh(norm(v)) & napall
    if hits: bad.append((k, sorted(hits)[:5]))
for k,h in bad:
    print(k, h)
print("blocks with overlap:", len(bad))
