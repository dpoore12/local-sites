import re, pathlib, collections
p = pathlib.Path('sites/virginiabeachpersonalinjurylawyerpros.com/copy.md')
txt = p.read_text()
blocks = re.split(r'^## ', txt, flags=re.M)[1:]
for b in blocks:
    name, body = b.split('\n', 1)
    name = name.strip()
    lines = [l for l in body.split('\n')]
    prev_head = False
    heads = []
    paras = [l.strip() for l in lines if l.strip()]
    openers = []
    onesent = 0
    for l in paras:
        if l.startswith('#'):
            h = l.lstrip('#').strip()
            heads.append(h)
            if len(h) > 89: print(f'{name}: LONG HEADING {len(h)}: {h}')
            sents = re.split(r'(?<=[.!?]) +', h)
            if len(sents) == 1 and h.endswith('.'): print(f'{name}: HEADING PERIOD: {h}')
            if prev_head: print(f'{name}: BACK-TO-BACK HEADING: {h}')
            prev_head = True
            openers = []
            onesent = 0
            continue
        prev_head = False
        for s in re.split(r'(?<=[.!?]) +', l):
            n = len(s.split())
            if n > 44: print(f'{name}: LONG SENTENCE {n}: {s[:120]}')
        w = l.split()[0].lower().strip('",')
        openers.append(w)
        if len(openers) >= 3 and openers[-1] == openers[-2] == openers[-3]:
            print(f'{name}: 3 SAME OPENERS "{w}"')
        ns = len(re.split(r'(?<=[.!?]) +', l))
        onesent = onesent + 1 if ns == 1 else 0
        if onesent >= 5: print(f'{name}: 5+ ONE-SENTENCE PARAS near: {l[:80]}')
    dup = [h for h, c in collections.Counter(heads).items() if c > 1]
    if dup: print(f'{name}: REPEAT HEADING {dup}')
# bare decimals, doubled words
for m in re.finditer(r'(?<![\d.])\.\d', txt): print('BARE DECIMAL:', txt[m.start()-40:m.start()+10])
for m in re.finditer(r'\b(\w+)\s+\1\b', txt, re.I): print('DOUBLED:', m.group(0))
# city/state density per page-ish (whole doc rough)
words = re.findall(r"[A-Za-z']+", txt)
print('total words', len(words))
for term in ('Virginia', 'Beach'):
    print(term, round(100*sum(1 for w in words if w == term)/len(words), 2), '%')
