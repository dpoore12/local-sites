import re, json, io
p="sites/fortlauderdaledomesticviolencelawyer.com/copy.md"
src=open(p).read()
new=open("_ftl_dv_blocks_tmp.md").read() if False else open("_ftl_dv_phase2_blocks.md").read()

def parse(text):
    blocks={}; order=[]
    cur=None; buf=[]
    for line in text.split("\n"):
        m=re.match(r"^## ([a-z0-9_]+)\s*$", line)
        if m:
            if cur: blocks[cur]="\n".join(buf).strip()
            cur=m.group(1); order.append(cur); buf=[]
        elif cur is not None:
            buf.append(line)
    if cur: blocks[cur]="\n".join(buf).strip()
    return blocks, order

nb, norder = parse(new)
# replace existing symptom bodies
for k in ["symptom_1","symptom_2","symptom_3","symptom_4"]:
    pat = re.compile(r"(## %s\n\n)(.*?)(\n## )" % k, re.S)
    assert pat.search(src), k
    src = pat.sub(lambda m: m.group(1)+nb[k]+m.group(3), src, count=1)

# append new blocks before pricing_lede
add=[k for k in norder if not k.startswith("symptom_")]
chunk="".join("## %s\n\n%s\n\n" % (k, nb[k]) for k in add)
i=src.index("## pricing_lede")
src=src[:i]+chunk+src[i:]
open(p,"w").write(src)
sj="sites/fortlauderdaledomesticviolencelawyer.com/site.json"
s=open(sj).read().replace('"phase": 1,', '"phase": 2,',1)
open(sj,"w").write(s)
print("done", add)
