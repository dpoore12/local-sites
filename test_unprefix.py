"""unprefix: Location must never leak /<host>/ to the client.

Regression for the Aug 24–Sep 7 outage. Pure string logic mirrored from
router/_worker.js so we can pin the fix without a Pages deploy in CI.
"""
from urllib.parse import urlparse, urlunparse


def unprefix(loc: str, host: str) -> str:
    if not loc:
        return loc
    needle = "/" + host
    if loc.startswith(needle + "/") or loc == needle:
        return loc[len(needle):] or "/"
    if "://" in loc[:8] or loc.startswith("//"):
        u = urlparse(loc)
        if u.path == needle or u.path.startswith(needle + "/"):
            path = u.path[len(needle):] or "/"
            return urlunparse((u.scheme, u.netloc, path, u.params, u.query, u.fragment))
        return loc
    return loc


fails = []


def check(label, cond, detail=""):
    print(("PASS  " if cond else "FAIL  ") + label + ("" if cond else f"   <- {detail}"))
    if not cond:
        fails.append(label)


HOST = "tampatileroofrepair.com"

check("relative leak stripped",
      unprefix(f"/{HOST}/services/", HOST) == "/services/")
check("exact host path -> /",
      unprefix(f"/{HOST}", HOST) == "/")
check("clean relative untouched",
      unprefix("/services/", HOST) == "/services/")
check("absolute leak stripped",
      unprefix(f"https://{HOST}/{HOST}/about/", HOST)
      == f"https://{HOST}/about/")
check("foreign host untouched",
      unprefix("https://evil.example/x", HOST) == "https://evil.example/x")
check("empty passthrough", unprefix("", HOST) == "")

print("\n" + (f"{len(fails)} FAILED: {fails}" if fails else "all green"))
raise SystemExit(1 if fails else 0)
