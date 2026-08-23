#!/usr/bin/env python3
"""Put the 83 sites on Cloudflare Pages and point their domains at them.

One Pages project per domain, apex + www on each, DNS written in the same
Cloudflare account.

It runs in phases because the sandbox credential proxy rewrites the auth header
on every api.cloudflare.com request. Asset upload needs a short-lived upload
pass instead, so that one phase has to run WITHOUT the Cloudflare credential
attached or the pass gets overwritten.

    python3 deploy_sites.py prep      # with the Cloudflare credential
    python3 deploy_sites.py upload    # with NO credential
    python3 deploy_sites.py publish   # with the Cloudflare credential
    python3 deploy_sites.py check     # with NO credential
    python3 deploy_sites.py status

Options: --only <domain>  --limit N  --jobs N  --redo

The token needs: Account > Cloudflare Pages > Edit, Zone > DNS > Edit,
Zone > Zone > Read.
"""

import argparse
import json
import os
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
ACCOUNT = "a3bf1a13d93899d8408b9d1ea94df078"
API = "https://api.cloudflare.com/client/v4"
WRANGLER = "/home/user/node_modules/.bin/wrangler"
STATE = os.path.join(ROOT, "data", "hosting.json")
MANIFESTS = os.path.join(ROOT, "data", "manifests")

_lock = threading.Lock()


# ---------------------------------------------------------------- api helpers

def api(method, path, body=None, form=None, tries=4):
    """Cloudflare API via curl -- python http clients do not see the proxy."""
    cmd = ["curl", "-s", "-X", method, f"{API}{path}"]
    if body is not None:
        cmd += ["-H", "Content-Type: application/json", "-d", json.dumps(body)]
    for k, v in (form or {}).items():
        cmd += ["--form-string", f"{k}={v}"]
    for attempt in range(tries):
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=180).stdout
        if not out.strip():        # empty body means throttled, never zero
            time.sleep(1.5 * (attempt + 1))
            continue
        try:
            return json.loads(out)
        except json.JSONDecodeError:
            time.sleep(1.5 * (attempt + 1))
    return {"success": False, "errors": [{"message": "no response from Cloudflare"}]}


def err(resp):
    return "; ".join(e.get("message", "?") for e in (resp.get("errors") or [])) or "?"


def fine(resp):
    """Success, or a failure that only means 'already there'."""
    if resp.get("success"):
        return True
    text = err(resp).lower()
    return "already" in text or "exists" in text or "duplicate" in text


# ---------------------------------------------------------------- state

def sites():
    out = []
    for domain in sorted(os.listdir(DIST)):
        path = os.path.join(DIST, domain)
        if not os.path.isdir(path) or "." not in domain:
            continue
        out.append((domain, domain.replace(".com", "").replace(".", "-")[:58], path))
    return out


def load():
    if os.path.exists(STATE):
        with open(STATE) as fh:
            return json.load(fh)
    return {}


def save(state):
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    with _lock:
        with open(STATE, "w") as fh:
            json.dump(state, fh, indent=2, sort_keys=True)


def note(state, domain, **kw):
    with _lock:
        state.setdefault(domain, {}).update(kw)


# ---------------------------------------------------------------- phase 1

def zone_of(domain):
    r = api("GET", f"/zones?name={domain}")
    rows = r.get("result") or []
    return rows[0]["id"] if rows else None


def prep(domain, slug, path, state):
    r = api("POST", f"/accounts/{ACCOUNT}/pages/projects",
            {"name": slug, "production_branch": "main"})
    if not fine(r):
        return False, f"project: {err(r)}"

    for name in (domain, f"www.{domain}"):
        r = api("POST", f"/accounts/{ACCOUNT}/pages/projects/{slug}/domains",
                {"name": name})
        if not fine(r):
            return False, f"attach {name}: {err(r)}"

    zid = state.get(domain, {}).get("zone") or zone_of(domain)
    if not zid:
        return False, "no Cloudflare zone for this domain"
    target = f"{slug}.pages.dev"
    have = {rec["name"]: rec for rec in
            (api("GET", f"/zones/{zid}/dns_records?per_page=100").get("result") or [])}
    for name in (domain, f"www.{domain}"):
        rec = have.get(name)
        if rec and rec["type"] == "CNAME" and target in rec["content"]:
            continue
        if rec:
            api("DELETE", f"/zones/{zid}/dns_records/{rec['id']}")
        w = api("POST", f"/zones/{zid}/dns_records",
                {"type": "CNAME", "name": name, "content": target,
                 "ttl": 1, "proxied": True})
        if not fine(w):
            return False, f"dns {name}: {err(w)}"

    r = api("GET", f"/accounts/{ACCOUNT}/pages/projects/{slug}/upload-token")
    jwt = (r.get("result") or {}).get("jwt")
    if not jwt:
        return False, f"upload pass: {err(r)}"

    note(state, domain, slug=slug, zone=zid, jwt=jwt,
         pages_url=f"https://{target}", prepped=True)
    return True, ""


# ---------------------------------------------------------------- phase 2

def upload(domain, slug, path, state):
    jwt = state.get(domain, {}).get("jwt")
    if not jwt:
        return False, "not prepped yet"
    os.makedirs(MANIFESTS, exist_ok=True)
    out = os.path.join(MANIFESTS, f"{domain}.json")
    env = dict(os.environ, CLOUDFLARE_API_TOKEN="placeholder",
               CLOUDFLARE_ACCOUNT_ID=ACCOUNT, CF_PAGES_UPLOAD_JWT=jwt)
    p = subprocess.run([WRANGLER, "pages", "project", "upload", path,
                        f"--output-manifest-path={out}"],
                       capture_output=True, text=True, env=env,
                       cwd="/tmp", timeout=600)
    if not os.path.exists(out):
        blob = (p.stdout + p.stderr).strip().splitlines()
        return False, blob[-1][:120] if blob else "wrangler said nothing"
    note(state, domain, uploaded=True)
    return True, ""


# ---------------------------------------------------------------- phase 3

def publish(domain, slug, path, state):
    out = os.path.join(MANIFESTS, f"{domain}.json")
    if not os.path.exists(out):
        return False, "nothing uploaded yet"
    with open(out) as fh:
        manifest = fh.read()
    r = api("POST", f"/accounts/{ACCOUNT}/pages/projects/{slug}/deployments",
            form={"manifest": manifest, "branch": "main"})
    if not r.get("success"):
        return False, f"deploy: {err(r)}"
    note(state, domain, published=True, jwt=None,
         deployment=(r.get("result") or {}).get("url"),
         when=time.strftime("%Y-%m-%d %H:%M"))
    return True, ""


# ---------------------------------------------------------------- phase 4

def check(domain, slug, path, state):
    codes = {}
    for url in (f"https://{domain}/", f"https://www.{domain}/"):
        p = subprocess.run(["curl", "-s", "-o", "/dev/null", "-m", "25",
                            "-w", "%{http_code}", url], capture_output=True, text=True)
        codes[url] = p.stdout.strip()
    ok = codes.get(f"https://{domain}/") == "200"
    note(state, domain, live=ok, codes=codes)
    return ok, "" if ok else " ".join(f"{u.split('//')[1]}={c}" for u, c in codes.items())


# ---------------------------------------------------------------- driver

PHASES = {"prep": (prep, "prepped"), "upload": (upload, "uploaded"),
          "publish": (publish, "published"), "check": (check, "live")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("phase", choices=list(PHASES) + ["status"])
    ap.add_argument("--only")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--redo", action="store_true")
    args = ap.parse_args()

    all_sites = sites()
    state = load()

    if args.phase == "status":
        cols = ["prepped", "uploaded", "published", "live"]
        counts = {c: sum(1 for v in state.values() if v.get(c)) for c in cols}
        print(f"{len(all_sites)} sites built")
        for c in cols:
            print(f"  {c:<10} {counts[c]}")
        bad = [(d, v.get("error")) for d, v in sorted(state.items())
               if v.get("error") and not v.get("live")]
        if bad:
            print("\nstill wrong:")
            for d, e in bad:
                print(f"  {d:<42} {e}")
        return 0

    fn, flag = PHASES[args.phase]
    todo = [s for s in all_sites if args.redo or not state.get(s[0], {}).get(flag)]
    if args.only:
        todo = [s for s in all_sites if s[0] == args.only]
    if args.limit:
        todo = todo[:args.limit]
    if not todo:
        print(f"nothing left to {args.phase}")
        return 0

    print(f"{args.phase}: {len(todo)} site(s), {args.jobs} at a time\n")

    def run(s):
        domain, slug, path = s
        try:
            ok, why = fn(domain, slug, path, state)
        except Exception as exc:                      # noqa: BLE001
            ok, why = False, f"{type(exc).__name__}: {exc}"[:120]
        note(state, domain, error=None if ok else why)
        print(f"{'ok  ' if ok else 'FAIL'} {domain:<42}{'' if ok else why[:100]}",
              flush=True)
        return ok

    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        results = list(pool.map(run, todo))
    save(state)

    good = sum(1 for r in results if r)
    print(f"\n{good} of {len(todo)} {args.phase} ok")
    return 0 if good == len(todo) else 1


if __name__ == "__main__":
    sys.exit(main())
