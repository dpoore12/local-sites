import re, collections
P="sites/kansascityemergencyplumber.com/copy.md"
src=open(P,encoding="utf-8").read()
parts=re.split(r"(?m)^## (\S+)\s*$",src)
blocks={parts[i]:parts[i+1].strip() for i in range(1,len(parts),2)}
keys=[k for k in blocks if k.startswith("svc_") or k.startswith("symptom_") or k in("services_summary","services_pick_head","crosslink_head","pricing_body","pricing_lede")]
for k in keys:
    t=blocks[k]
    for line in t.split("\n"):
        if line.startswith("###"):
            h=line.lstrip("# ").strip()
            if len(h)>89: print("LONG HEAD",k,len(h),h)
            if h.endswith(".") and h.count(".")==1: print("HEAD PERIOD",k,h)
    body=re.sub(r"(?m)^#+.*$","",t)
    for s in re.split(r"(?<=[.!?])\s+",body):
        n=len(s.split())
        if n>44: print("LONG SENT",k,n,s[:120])
    if re.search(r"(?<![\d])\.\d",body): print("BARE DEC",k)
    ws=re.findall(r"\b[a-zA-Z']+\b",body)
    for a,b in zip(ws,ws[1:]):
        if a.lower()==b.lower() and a.lower() not in("that","had"): print("DOUBLE",k,a,b)
    paras=[p for p in t.split("\n\n") if p.strip() and not p.startswith("#")]
    op=[p.split()[0].lower() for p in paras]
    for i in range(len(op)-2):
        if op[i]==op[i+1]==op[i+2]: print("OPENERS",k,op[i])
# word freq per service page
for k in keys:
    if not k.endswith("_body") or not k.startswith("svc_"): continue
    t=(blocks[k.replace("_body","_lede")]+" "+blocks[k]).lower()
    ws=re.findall(r"[a-z]+",t)
    c=collections.Counter(ws)
    tot=len(ws)
    print(k, tot, "kansas",c["kansas"],"city",c["city"],"missouri",c["missouri"],
          "pct city %.2f"%(100*c["city"]/tot))
# headings duplicated
allh=[]
for k in keys:
    hs=[l for l in blocks[k].split("\n") if l.startswith("###")]
    if len(set(hs))!=len(hs): print("DUP HEAD",k)
print("ok")
