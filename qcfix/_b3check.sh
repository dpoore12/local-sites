#!/bin/bash
# usage: _b3check.sh <domain>
cd /home/user/workspace/local-sites || exit 1
D="$1"
echo "=== check-only ==="
timeout 300 python3 template/build.py --check-only "$D" 2>&1 | tail -20
echo "=== build ==="
timeout 300 python3 template/build.py "$D" 2>&1 | tail -3
echo "=== qc ==="
timeout 300 python3 qc.py "$D" --csv /tmp/qc_$D.csv 2>&1 | tail -20
python3 - "$D" <<'PY'
import csv,sys
d=sys.argv[1]
rows=list(csv.DictReader(open(f"/tmp/qc_{d}.csv")))
for r in rows:
    if r["kind"] in ("flow",) or r["severity"]=="HIGH":
        print(f'{r["severity"]:4} {r["page"]:45} {r["kind"]}: {r["message"]}')
        if r["evidence"]: print("      ->", r["evidence"][:150])
PY
