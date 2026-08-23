#!/usr/bin/env python3
"""Put the 83 sites on Cloudflare Pages and point their domains at them.

One Pages project per domain. Each project gets the apex domain and www.
DNS lives in the same Cloudflare account, so attaching the custom domain is
all it takes -- Cloudflare writes the CNAME itself.

Usage:
    python3 deploy_sites.py                # everything not already done
    python3 deploy_sites.py --only x.com   # one site
    python3 deploy_sites.py --limit 10     # first ten that still need work
    python3 deploy_sites.py --status       # what is live, what is not
    python3 deploy_sites.py --jobs 4       # parallel uploads (default 4)

Needs the Cloudflare credential. Requires the token to have:
    Account | Cloudflare Pages | Edit
    Zone    | DNS              | Edit
"""

import argparse
import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
ACCOUNT = "a3bf1a13d93899d8408b9d1ea94df078"
API = "https://api.cloudflare.com/client/v4"
WRANGLER = "/home/user/node_modules/.bin/wrangler"
STATE = os.path.join(ROOT, "data", "hosting.json")


# ---------------------------------------------------------------- api helpers

def api(method, path, body=None, tries=4):
    """Cloudflare API through curl -- httpx does not see the credential proxy."""
    cmd = ["curl", "-s", "-X", method, f"{API}{path}"]
    if body is not None:
        cmd += ["-H", "Content-Type: application/json", "-d", json.dumps(body)]
    for attempt in range(tries):
        out = subprocess.run(cmd, capture_output=True, text=True).stdout
        if not out.strip():          # empty body means throttled, never zero
            time.sleep(1.5 * (attempt + 1))
            continue
        try:
            return json.loads(out)
        except json.JSONDecodeError:
            time.sleep(1.5 * (attempt + 1))
    return {"success": False, "errors": [{"message": "no response from Cloudflare"}]}


def err(resp):
    return "; ".join(e.get("message", "?") for e in (resp.get("errors") or [])) or "?"


def taken(resp):
    """True when the failure is just 'it already exists'."""
    text = err(resp).lower()
    return "already" in text or "exists" in text or "duplicate" in text


# ---------------------------------------------------------------- the sites

def sites():
    """[(domain, slug, dist_path)] for every built site."""
    out = []
    for domain in sorted(os.listdir(DIST)):
        path = os.path.join(DIST, domain)
        if not os.path.isdir(path) or "." not in domain:
            continue
        slug = domain.replace(".com", "").replace(".", "-")[:58]
        out.append((domain, slug, path))
    return out


def load_state():
    if os.path.exists(STATE):
        with open(STATE) as fh:
            return json.load(fh)
    return {}


def save_state(state):
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    with open(STATE, "w") as fh:
        json.dump(state, fh, indent=2, sort_keys=True)


# ---------------------------------------------------------------- the work

def ensure_project(slug):
    r = api("POST", f"/accounts/{ACCOUNT}/pages/projects",
            {"name": slug, "production_branch": "main"})
    if r.get("success") or taken(r):
        return True, ""
    return False, err(r)


def upload(slug, path):
    env = dict(os.environ,
               CLOUDFLARE_API_TOKEN=os.environ.get("CLOUDFLARE_API_TOKEN", "placeholder"),
               CLOUDFLARE_ACCOUNT_ID=ACCOUNT)
    p = subprocess.run(
        [WRANGLER, "pages", "deploy", path,
         f"--project-name={slug}", "--branch=main", "--commit-dirty=true"],
        capture_output=True, text=True, env=env, cwd="/tmp", timeout=300)
    blob = p.stdout + p.stderr
    if "Deployment complete" in blob or "Success" in blob:
        return True, ""
    return False, blob.strip().splitlines()[-1] if blob.strip() else "wrangler said nothing"


def attach(slug, name):
    r = api("POST", f"/accounts/{ACCOUNT}/pages/projects/{slug}/domains", {"name": name})
    if r.get("success") or taken(r):
        return True, ""
    return False, err(r)


def zone_id(domain, cache={}):
    if domain not in cache:
        r = api("GET", f"/zones?name={domain}")
        rows = r.get("result") or []
        cache[domain] = rows[0]["id"] if rows else None
    return cache[domain]


def ensure_dns(domain, slug):
    """Cloudflare normally writes these itself when the domain is attached.
    This fills in anything it missed."""
    zid = zone_id(domain)
    if not zid:
        return False, "no zone"
    have = {}
    r = api("GET", f"/zones/{zid}/dns_records?per_page=100")
    for rec in (r.get("result") or []):
        have[rec["name"]] = rec
    target = f"{slug}.pages.dev"
    problems = []
    for name in (domain, f"www.{domain}"):
        rec = have.get(name)
        if rec and rec["type"] == "CNAME" and target in rec["content"]:
            continue
        if rec:
            api("DELETE", f"/zones/{zid}/dns_records/{rec['id']}")
        w = api("POST", f"/zones/{zid}/dns_records",
                {"type": "CNAME", "name": name, "content": target,
                 "ttl": 1, "proxied": True})
        if not (w.get("success") or taken(w)):
            problems.append(f"{name}: {err(w)}")
    return (not problems), "; ".join(problems)


def do_site(domain, slug, path, state):
    step = "project"
    ok, why = ensure_project(slug)
    if ok:
        step = "upload"
        ok, why = upload(slug, path)
    if ok:
        step = "domain"
        ok, why = attach(slug, domain)
        if ok:
            ok, why = attach(slug, f"www.{domain}")
    if ok:
        step = "dns"
        ok, why = ensure_dns(domain, slug)
    state[domain] = {"slug": slug, "url": f"https://{slug}.pages.dev",
                     "live": bool(ok), "failed_at": None if ok else step,
                     "error": None if ok else why,
                     "when": time.strftime("%Y-%m-%d %H:%M")}
    print(f"{'ok  ' if ok else 'FAIL'} {domain:<42} {'' if ok else step + ': ' + why[:90]}",
          flush=True)
    return ok


def check_live(domain):
    p = subprocess.run(["curl", "-s", "-o", "/dev/null", "-m", "15",
                        "-w", "%{http_code}", f"https://{domain}/"],
                       capture_output=True, text=True)
    return p.stdout.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--redo", action="store_true", help="include ones already done")
    args = ap.parse_args()

    all_sites = sites()
    state = load_state()

    if args.status:
        live = [d for d, v in state.items() if v.get("live")]
        print(f"{len(all_sites)} sites built, {len(live)} deployed")
        for domain, _, _ in all_sites:
            v = state.get(domain, {})
            mark = "live" if v.get("live") else (v.get("failed_at") or "not started")
            print(f"  {domain:<42} {mark}")
        return 0

    todo = [s for s in all_sites
            if args.redo or not state.get(s[0], {}).get("live")]
    if args.only:
        todo = [s for s in all_sites if s[0] == args.only]
        if not todo:
            print(f"no site called {args.only}")
            return 1
    if args.limit:
        todo = todo[:args.limit]

    if not todo:
        print("everything is already deployed")
        return 0

    print(f"deploying {len(todo)} site(s), {args.jobs} at a time\n")
    lock_state = {}
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        results = list(pool.map(lambda s: do_site(s[0], s[1], s[2], lock_state), todo))
    state.update(lock_state)
    save_state(state)

    good = sum(1 for r in results if r)
    print(f"\n{good} of {len(todo)} done. state written to data/hosting.json")
    return 0 if good == len(todo) else 1


if __name__ == "__main__":
    sys.exit(main())
