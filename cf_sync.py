#!/usr/bin/env python3
"""Refresh the Cloudflare Registrar snapshot that `domains.py` treats as truth.

Writes ``data/registrar-snapshot.json`` -- every domain the account holds,
keyed by name, with the registrar's own created_at / expires_at / auto_renew /
locked / privacy_mode fields. That file is what proves a name is *ours* rather
than merely taken by somebody.

Auth: the request needs a Cloudflare API token with Registrar admin permission.
It is injected by the sandbox proxy, so nothing secret appears in this file or in
the shell. Run it as:

    bash(command="cd local-sites && python3 cf_sync.py",
         api_credentials=["custom-cred:api.cloudflare.com"])

Notes on the endpoint, learned the hard way on 2026-08-22:
  * `per_page` is capped at 50 and rejects anything larger.
  * Paging is **cursor**-based. A `page=N` parameter is silently ignored and you
    get page one back every time, which looks like 250 domains that are really
    the same 50 five times over.
  * `httpx` did not pick up the sandbox HTTPS proxy here; `curl` did. Hence the
    subprocess call rather than a Python HTTP client.
"""
import json
import pathlib
import subprocess
import sys
import urllib.parse

ACCOUNT_ID = "a3bf1a13d93899d8408b9d1ea94df078"
OUT = pathlib.Path(__file__).parent / "data" / "registrar-snapshot.json"
BASE = (f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}"
        "/registrar/registrations?per_page=50")
# Cloudflare caps a single account at 100 registrar domains, so five pages of
# fifty is already twice the ceiling -- a guard against looping forever, not a
# real limit we expect to reach.
MAX_PAGES = 5


def fetch():
    records, cursor = [], None
    for _ in range(MAX_PAGES):
        url = BASE + (f"&cursor={urllib.parse.quote(cursor)}" if cursor else "")
        proc = subprocess.run(["curl", "-s", "--max-time", "90", url],
                              capture_output=True, text=True)
        try:
            payload = json.loads(proc.stdout)
        except Exception:                                     # noqa: BLE001
            sys.exit(f"registrar returned non-JSON: {proc.stdout[:200]!r}")
        if not payload.get("success"):
            sys.exit(f"registrar error: {payload.get('errors')}")
        page = payload.get("result") or []
        records += page
        cursor = (payload.get("result_info") or {}).get("cursor")
        if not cursor or len(page) < 50:
            break
    return records


if __name__ == "__main__":
    records = fetch()
    by_name = {r["domain_name"]: r for r in records}
    OUT.write_text(json.dumps({k: by_name[k] for k in sorted(by_name)}, indent=1) + "\n")

    no_renew = [d for d, r in by_name.items() if not r.get("auto_renew")]
    inactive = [d for d, r in by_name.items() if r.get("status") != "active"]
    print(f"{len(by_name)} domains -> {OUT}")
    if no_renew:
        print(f"WARN auto-renew off on {len(no_renew)}: {', '.join(sorted(no_renew))}")
    if inactive:
        print(f"WARN not active: {', '.join(sorted(inactive))}")
    if len(by_name) > 90:
        print(f"WARN {len(by_name)} of the 100-domain account cap used — "
              "the next batch needs a second Cloudflare account")
