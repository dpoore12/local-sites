import json, io, sys
from pathlib import Path
sys.path.insert(0,'.')
from pricing_batch1_data import PRICING

for domain, d in PRICING.items():
    p = Path('sites')/domain/'site.json'
    s = json.loads(p.read_text())
    s['pricing'] = d['pricing']
    p.write_text(json.dumps(s, indent=1, ensure_ascii=False) + "\n")
    cp = Path('sites')/domain/'copy.md'
    txt = cp.read_text().rstrip('\n')
    add = Path(d['copy']).read_text().strip('\n')
    # strip any previous pricing sections
    if '## pricing_lede' in txt:
        txt = txt.split('## pricing_lede')[0].rstrip('\n')
    cp.write_text(txt + "\n\n" + add + "\n")
    print('updated', domain)
