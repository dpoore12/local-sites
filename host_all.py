#!/usr/bin/env python3
"""Host all 83 sites on ONE Cloudflare Pages project.

Cloudflare caps how many Pages projects an account can have, so one project per
domain does not scale. Instead: a single project holds every site's files in its
own folder, and a tiny worker in front picks the folder from the hostname.

    sacramentoacrepair.com/about/  ->  /sacramentoacrepair.com/about/index.html

Phases, because the sandbox credential proxy rewrites the auth header on every
api.cloudflare.com call and asset upload needs its own short-lived pass:

    python3 host_all.py reset     # with the Cloudflare credential  (one time)
    python3 host_all.py stage     # no credential
    python3 host_all.py upload    # NO credential  (uses the upload pass)
    python3 host_all.py publish   # with the Cloudflare credential
    python3 host_all.py domains   # with the Cloudflare credential
    python3 host_all.py check     # no credential
"""

import json
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
STAGE = os.path.join(ROOT, ".stage")
ACCOUNT = "a3bf1a13d93899d8408b9d1ea94df078"
API = "https://api.cloudflare.com/client/v4"
WRANGLER = "/home/user/node_modules/.bin/wrangler"
PROJECT = "local-sites"
STATE = os.path.join(ROOT, "data", "hosting.json")
MANIFEST = os.path.join(ROOT, "data", "manifest.json")

WORKER = """// One project, many sites. The hostname picks the folder.
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    let host = url.hostname.toLowerCase().replace(/^www\\./, "");

    // browsing the project directly: serve as-is
    if (host.endsWith(".pages.dev") || host === "localhost") {
      return env.ASSETS.fetch(request);
    }

    const target = new URL(request.url);
    target.pathname = "/" + host + url.pathname;
    let res = await env.ASSETS.fetch(new Request(target.toString(), request));

    // /foo -> /foo/
    if (res.status === 404 && !url.pathname.endsWith("/")) {
      const alt = new URL(target.toString());
      alt.pathname = alt.pathname + "/";
      const retry = await env.ASSETS.fetch(new Request(alt.toString(), request));
      if (retry.status !== 404) return retry;
    }

    // anything else on that site falls back to its own home page
    if (res.status === 404) {
      const home = new URL(target.toString());
      home.pathname = "/" + host + "/";
      const fallback = await env.ASSETS.fetch(new Request(home.toString(), request));
      if (fallback.status === 200) {
        return new Response(fallback.body, {status: 404, headers: fallback.headers});
      }
    }
    return res;
  }
};
"""


def api(method, path, body=None, form=None, tries=5):
    cmd = ["curl", "-s", "-X", method, f"{API}{path}"]
    if body is not None:
        cmd += ["-H", "Content-Type: application/json", "-d", json.dumps(body)]
    for k, v in (form or {}).items():
        cmd += ["--form-string", f"{k}={v}"]
    for attempt in range(tries):
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=300).stdout
        if not out.strip():
            time.sleep(1.5 * (attempt + 1))
            continue
        try:
            return json.loads(out)
        except json.JSONDecodeError:
            time.sleep(1.5 * (attempt + 1))
    return {"success": False, "errors": [{"message": "no response from Cloudflare"}]}


def err(r):
    return "; ".join(e.get("message", "?") for e in (r.get("errors") or [])) or "?"


def fine(r):
    if r.get("success"):
        return True
    t = err(r).lower()
    return "already" in t or "exists" in t or "duplicate" in t


def domains():
    return sorted(d for d in os.listdir(DIST)
                  if os.path.isdir(os.path.join(DIST, d)) and "." in d)


def load():
    return json.load(open(STATE)) if os.path.exists(STATE) else {}


def save(s):
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    json.dump(s, open(STATE, "w"), indent=2, sort_keys=True)


# ---------------------------------------------------------------- phases

def reset():
    """Clear out the per-domain projects and leave one project standing."""
    keep = PROJECT
    existing = []
    for page in range(1, 20):
        r = api("GET", f"/accounts/{ACCOUNT}/pages/projects?page={page}")
        rows = r.get("result") or []
        existing += [p["name"] for p in rows]
        if not rows:
            break
        time.sleep(0.3)
    print(f"{len(existing)} project(s) on the account")
    for name in existing:
        if name == keep:
            continue
        # a project cannot be deleted while it still holds custom domains
        d = api("GET", f"/accounts/{ACCOUNT}/pages/projects/{name}/domains")
        for dom in (d.get("result") or []):
            api("DELETE",
                f"/accounts/{ACCOUNT}/pages/projects/{name}/domains/{dom['name']}")
            time.sleep(0.2)
        r = api("DELETE", f"/accounts/{ACCOUNT}/pages/projects/{name}")
        print(f"  {'removed' if fine(r) else 'KEPT (' + err(r) + ')'} {name}")
        time.sleep(0.3)
    if keep not in existing:
        r = api("POST", f"/accounts/{ACCOUNT}/pages/projects",
                {"name": keep, "production_branch": "main"})
        print(f"created {keep}: {r.get('success') or err(r)}")
    return 0


def stage():
    """Copy every site into one folder tree and drop the worker in front."""
    if os.path.exists(STAGE):
        shutil.rmtree(STAGE)
    os.makedirs(STAGE)
    n = 0
    for d in domains():
        shutil.copytree(os.path.join(DIST, d), os.path.join(STAGE, d))
        n += 1
    open(os.path.join(STAGE, "_worker.js"), "w").write(WORKER)
    files = sum(len(f) for _, _, f in os.walk(STAGE))
    size = subprocess.run(["du", "-sh", STAGE], capture_output=True, text=True).stdout.split()[0]
    print(f"staged {n} sites, {files} files, {size}")
    return 0


def upload():
    state = load()
    jwt = state.get("jwt")
    if not jwt:
        print("no upload pass -- run `publish` once first to fetch one")
        return 1
    env = dict(os.environ, CLOUDFLARE_API_TOKEN="placeholder",
               CLOUDFLARE_ACCOUNT_ID=ACCOUNT, CF_PAGES_UPLOAD_JWT=jwt)
    os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)
    p = subprocess.run([WRANGLER, "pages", "project", "upload", STAGE,
                        f"--output-manifest-path={MANIFEST}"],
                       env=env, cwd="/tmp", timeout=3000)
    if not os.path.exists(MANIFEST):
        print("upload failed")
        return 1
    print(f"manifest written: {len(json.load(open(MANIFEST)))} files")
    return 0


def pass_only():
    """Fetch an upload pass and stop."""
    r = api("GET", f"/accounts/{ACCOUNT}/pages/projects/{PROJECT}/upload-token")
    jwt = (r.get("result") or {}).get("jwt")
    if not jwt:
        print("could not get an upload pass:", err(r))
        return 1
    s = load()
    s["jwt"] = jwt
    save(s)
    print("upload pass saved")
    return 0


def publish():
    if not os.path.exists(MANIFEST):
        print("nothing uploaded yet")
        return 1
    manifest = open(MANIFEST).read()
    r = api("POST", f"/accounts/{ACCOUNT}/pages/projects/{PROJECT}/deployments",
            form={"manifest": manifest, "branch": "main"})
    if not r.get("success"):
        print("deploy failed:", err(r))
        return 1
    res = r.get("result") or {}
    s = load()
    s["deployment"] = res.get("url")
    s["when"] = time.strftime("%Y-%m-%d %H:%M")
    save(s)
    print("deployed:", res.get("url"))
    return 0


def project_host():
    """Cloudflare may add a suffix to the project name, so ask for the real one."""
    r = api("GET", f"/accounts/{ACCOUNT}/pages/projects/{PROJECT}")
    sub = (r.get("result") or {}).get("subdomain")
    return sub or f"{PROJECT}.pages.dev"


def hook_up():
    """Attach every domain to the project and point its DNS at it."""
    s = load()
    target = project_host()
    s["pages_host"] = target
    print(f"pointing everything at {target}")
    done = s.setdefault("sites", {})

    def one(d):
        r = api("POST", f"/accounts/{ACCOUNT}/pages/projects/{PROJECT}/domains",
                {"name": d})
        if not fine(r):
            return d, f"attach: {err(r)}"
        z = api("GET", f"/zones?name={d}")
        rows = z.get("result") or []
        if not rows:
            return d, "no zone"
        zid = rows[0]["id"]
        have = {rec["name"]: rec for rec in
                (api("GET", f"/zones/{zid}/dns_records?per_page=100").get("result") or [])}
        for name in (d, f"www.{d}"):
            rec = have.get(name)
            if name != d:
                # www is not attached to the project; drop any stale record
                if rec:
                    api("DELETE", f"/zones/{zid}/dns_records/{rec['id']}")
                continue
            if rec and rec["type"] == "CNAME" and rec["content"] == target:
                continue
            if rec:
                api("DELETE", f"/zones/{zid}/dns_records/{rec['id']}")
            w = api("POST", f"/zones/{zid}/dns_records",
                    {"type": "CNAME", "name": name, "content": target,
                     "ttl": 1, "proxied": True})
            if not fine(w):
                return d, f"dns: {err(w)}"
        return d, None

    todo = [d for d in domains() if not done.get(d)]
    print(f"hooking up {len(todo)} domain(s)")
    with ThreadPoolExecutor(max_workers=3) as pool:
        for d, why in pool.map(one, todo):
            done[d] = (why is None)
            print(f"{'ok  ' if why is None else 'FAIL'} {d:<44}{why or ''}")
    save(s)
    bad = [d for d, v in done.items() if not v]
    print(f"\n{len(done) - len(bad)} of {len(done)} hooked up")
    return 1 if bad else 0


def check():
    s = load()
    codes = {}

    def one(d):
        p = subprocess.run(["curl", "-s", "-o", "/dev/null", "-m", "25",
                            "-w", "%{http_code}", f"https://{d}/"],
                           capture_output=True, text=True)
        return d, p.stdout.strip()

    with ThreadPoolExecutor(max_workers=8) as pool:
        for d, code in pool.map(one, domains()):
            codes[d] = code
    live = [d for d, c in codes.items() if c == "200"]
    print(f"{len(live)} of {len(codes)} answering 200")
    for d, c in sorted(codes.items()):
        if c != "200":
            print(f"  {d:<44}{c}")
    s["codes"] = codes
    s["live_count"] = len(live)
    save(s)
    return 0 if len(live) == len(codes) else 1


PHASES = {"reset": reset, "stage": stage, "pass": pass_only, "upload": upload,
          "publish": publish, "domains": hook_up, "check": check}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in PHASES:
        print(__doc__)
        sys.exit(1)
    sys.exit(PHASES[sys.argv[1]]())
