// One Pages project serves every site. The hostname picks the folder.
//
// THIS IS THE LIVE ROUTER. host_all.py stage copies it to .stage/_worker.js,
// and Cloudflare Pages gives _worker.js precedence over any functions/
// directory -- which is why router/functions/ was deleted on 2026-08-23 after
// an edit there deployed successfully and changed nothing.
//
// Two dynamic routes sit in front of the static assets:
//   POST /lead                 the lead form on every page of every site
//   GET  /leads-<LEAD_SLUG>    the lead desk, every lead across all 83 sites
// Everything else is a static file lookup, unchanged.

const LEAD_SLUG = "9f3c1a77b25e4d80";

// ---------------------------------------------------------------- validation
const DIGITS = /\D+/g;

function clean(v, max) {
  return String(v == null ? "" : v).replace(/\s+/g, " ").trim().slice(0, max);
}

function validate(f) {
  const out = {
    site: clean(f.get("site"), 120).toLowerCase(),
    page: clean(f.get("page"), 120),
    name: clean(f.get("name"), 80),
    problem: clean(f.get("problem"), 1200),
    zip: clean(f.get("zip"), 10),
    email: clean(f.get("email"), 120),
    best_time: clean(f.get("when"), 40) || "Right away",
  };

  // Honeypot. A real visitor never sees this field, so anything in it is a bot.
  if (clean(f.get("company_url"), 200)) return { spam: true };

  // A human takes longer than two and a half seconds to fill six boxes. The
  // stamp is set by script, so a missing stamp is not held against anyone.
  const t = parseInt(f.get("t") || "0", 10);
  if (t && Date.now() - t < 2500) return { spam: true };

  if (!/^[a-z0-9.-]+\.[a-z]{2,}$/.test(out.site)) return { error: "Missing site." };
  if (out.name.length < 2) return { error: "Please enter your name." };
  if (out.problem.length < 3) return { error: "Please say what you need help with." };

  let d = String(f.get("phone") || "").replace(DIGITS, "");
  if (d.length === 11 && d[0] === "1") d = d.slice(1);
  if (d.length !== 10 || /^(\d)\1{9}$/.test(d)) {
    return { error: "Please enter a 10-digit phone number." };
  }
  out.phone = "+1" + d;

  if (out.zip && !/^\d{5}$/.test(out.zip)) out.zip = "";
  if (out.email && !/^[^@\s]+@[^@\s.]+\.[^@\s]{2,}$/.test(out.email)) out.email = "";

  return { lead: out };
}

// --------------------------------------------------------------- pitch filter
// Agency bots fill the form to pitch web work. They pass the honeypot, the
// timer and the address limit because they drive a real browser from a fresh
// address every time. The only reliable tell is what they type: they talk
// about the site owner's own website. A customer talks about their problem.
const PITCH_PHRASES = [
  "seo", "backlink", "rank higher", "ranking on google", "search rankings",
  "online presence", "online visibility", "digital marketing", "web design",
  "website design", "web development", "booking page", "book online",
  "online booking", "appointment form", "booking form", "intake form",
  "social media", "social profiles", "linkedin page", "facebook page",
  "add testimonials", "google business profile", "lead generation service",
  "i can help add", "i can help you", "i can draft", "i can add", "i can write",
  "i would like to discuss", "i'd love to discuss", "love to discuss",
  "happy to write it up", "send it across", "reply if you would like",
  "reply and i will", "want the details", "no charge", "costs you nothing",
  "free audit", "backend analysis", "i visited your", "i came across your",
  "i was going through your", "went through your", "grow your online",
  "we help business", "our team would be happy", "quick phone call",
  "preferred time availability", "hey team", "dear owner", "dear team",
  "not appearing on google", "several important", "potential clients may",
  "potential clients might", "customers may leave", "visitors may leave",
];
const OWNER_TALK = [
  "your website", "your site", "your page", "your web page", "your homepage",
  "your business online", "your online",
];

function pitchScore(lead) {
  const t = (lead.problem || "").toLowerCase();
  const hits = [];

  for (const p of PITCH_PHRASES) if (t.includes(p)) { hits.push(p); if (hits.length > 3) break; }
  let score = hits.length;

  for (const p of OWNER_TALK) if (t.includes(p)) { hits.push(p); score += 1; break; }

  // The bot greets the domain it is pitching. No customer types that.
  const host = (lead.site || "").toLowerCase().replace(/^www\./, "");
  if (host && t.includes(host)) { score += 2; hits.push("names the domain"); }

  if (/https?:\/\/|www\.|\.com\b/.test(t) && t.length > 150) { score += 1; hits.push("link in a long message"); }

  // A person with a burst pipe writes a line, not four paragraphs.
  if (t.length > 320) { score += 1; hits.push("very long"); }


  // "Hello Sacramento AC Repair," -- greeting the business by its own brand
  // name. A customer says "hi" or nothing at all, never the company name.
  const greet = (lead.problem || "").match(/^\s*(?:hello|hi|hey|dear|greetings)\s+([^,.!?\n]{3,60}),/i);
  if (greet && /^(?:[A-Z][\w&.'-]*\s+){1,}[A-Z][\w&.'-]*$/.test(greet[1].trim())) {
    score += 2; hits.push("greets the business by name");
  }

  return { score, why: hits.slice(0, 5).join(", ") };
}

// ------------------------------------------------------------------ handlers
async function postLead(request, env) {
  const wantsJson = (request.headers.get("Accept") || "").includes("application/json");
  const reply = (status, body) =>
    wantsJson
      ? new Response(JSON.stringify(body), {
          status,
          headers: { "Content-Type": "application/json", "Cache-Control": "no-store" },
        })
      : new Response(confirmPage(body), {
          status,
          headers: { "Content-Type": "text/html; charset=utf-8", "Cache-Control": "no-store" },
        });

  let form;
  try {
    form = await request.formData();
  } catch (_) {
    return reply(400, { ok: false, error: "Could not read the form." });
  }

  const v = validate(form);
  // A bot is told the same thing a person is told. Telling it that it failed
  // only helps it try again with the trap field empty.
  if (v.spam) return reply(200, { ok: true });
  if (v.error) return reply(422, { ok: false, error: v.error });

  const lead = v.lead;
  const ip = request.headers.get("CF-Connecting-IP") || "";
  const now = new Date().toISOString();

  // Agency pitches are filed, not dropped, so the call can be audited and a
  // wrong call can be reversed. The sender is told the same thing a customer
  // is told, which keeps it from retrying with softer wording.
  const p = pitchScore(lead);
  const isPitch = p.score >= 2 ? 1 : 0;

  if (!env.LEADS) return reply(500, { ok: false, error: "Lead store not configured." });

  // Rate limit by address: six in ten minutes is far more than any real
  // household needs and cheap to check.
  try {
    const since = new Date(Date.now() - 600000).toISOString();
    const r = await env.LEADS.prepare(
      "SELECT COUNT(*) AS n FROM leads WHERE ip = ? AND created_at > ?"
    ).bind(ip, since).first();
    if (r && r.n >= 6) return reply(429, { ok: false, error: "Too many requests." });
  } catch (_) { /* never block a real lead on the rate check failing */ }

  try {
    await env.LEADS.prepare(
      `INSERT INTO leads
         (created_at, site, page, name, phone, problem, zip, email, best_time, ip, ua, country, spam, spam_reason)
       VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)`
    ).bind(
      now, lead.site, lead.page, lead.name, lead.phone, lead.problem,
      lead.zip, lead.email, lead.best_time, ip,
      clean(request.headers.get("User-Agent"), 300),
      (request.cf && request.cf.country) || "",
      isPitch, isPitch ? clean(p.why, 200) : ""
    ).run();
  } catch (e) {
    return reply(500, { ok: false, error: "Could not save that." });
  }

  return reply(200, { ok: true });
}

function esc(s) {
  return String(s == null ? "" : s).replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

function confirmPage(body) {
  const ok = body.ok;
  return `<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>${ok ? "Request received" : "Not sent"}</title>
<style>body{margin:0;min-height:100vh;display:grid;place-items:center;padding:2rem;
background:#0b2233;color:#fff;font:16px/1.6 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
.b{background:#fff;color:#12212f;max-width:30rem;padding:2rem;border-radius:14px;border-top:4px solid #f5a524}
h1{margin:0 0 .6rem;font-size:1.4rem;color:#143d59}p{margin:0 0 .5rem;color:#45566a}
a{color:#143d59;font-weight:700}</style></head><body><div class="b">
<h1>${ok ? "Got it." : "That did not go through."}</h1>
<p>${ok ? "Expect a call at the time you picked."
        : esc(body.error || "Please try again.")}</p>
<p><a href="/">Back to the site</a></p></div></body></html>`;
}

async function leadDesk(request, env) {
  if (!env.LEADS) return new Response("Lead store not configured.", { status: 500 });
  const url = new URL(request.url);
  const site = (url.searchParams.get("site") || "").toLowerCase();
  const limit = Math.min(parseInt(url.searchParams.get("limit") || "300", 10) || 300, 1000);
  // The desk shows real people. Agency pitches are kept but parked behind
  // ?pitches=1 so the filter's calls can be checked and reversed.
  const showPitches = url.searchParams.get("pitches") === "1";
  const flag = showPitches ? 1 : 0;

  let rows = [], counts = [], pitchTotal = 0;
  try {
    const q = site
      ? env.LEADS.prepare(
          "SELECT * FROM leads WHERE site = ? AND COALESCE(spam,0) = ? ORDER BY id DESC LIMIT ?").bind(site, flag, limit)
      : env.LEADS.prepare(
          "SELECT * FROM leads WHERE COALESCE(spam,0) = ? ORDER BY id DESC LIMIT ?").bind(flag, limit);
    rows = (await q.all()).results || [];
    counts = (await env.LEADS.prepare(
      "SELECT site, COUNT(*) AS n, MAX(created_at) AS last FROM leads WHERE COALESCE(spam,0) = ? GROUP BY site ORDER BY n DESC"
    ).bind(flag).all()).results || [];
    const pt = await env.LEADS.prepare(
      "SELECT COUNT(*) AS n FROM leads WHERE COALESCE(spam,0) = 1").first();
    pitchTotal = (pt && pt.n) || 0;
  } catch (e) {
    return new Response("Query failed: " + e.message, { status: 500 });
  }

  if ((url.searchParams.get("format") || "") === "csv") {
    const cols = ["id", "created_at", "site", "name", "phone", "best_time", "zip", "email", "problem", "page", "country"];
    const q = (v) => '"' + String(v == null ? "" : v).replace(/"/g, '""') + '"';
    const csv = [cols.join(",")].concat(rows.map((r) => cols.map((c) => q(r[c])).join(","))).join("\n");
    return new Response(csv, {
      headers: {
        "Content-Type": "text/csv; charset=utf-8",
        "Content-Disposition": 'attachment; filename="leads.csv"',
        "Cache-Control": "no-store",
      },
    });
  }

  const tel = (p) => `<a href="tel:${esc(p)}">${esc(
    /^\+1\d{10}$/.test(p) ? `(${p.slice(2, 5)}) ${p.slice(5, 8)}-${p.slice(8)}` : p)}</a>`;

  const html = `<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>Lead desk</title>
<style>
:root{--ink:#12212f;--brand:#143d59;--deep:#0b2233;--cta:#f5a524;--line:#e2dfd6;--muted:#6b7a89}
*{box-sizing:border-box}body{margin:0;font:15px/1.55 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;
color:var(--ink);background:#f7f6f2}
header{background:var(--deep);color:#fff;padding:1.1rem 1.4rem;display:flex;flex-wrap:wrap;
gap:1rem;align-items:baseline;justify-content:space-between}
header h1{margin:0;font-size:1.15rem;letter-spacing:-.01em}
header .n{color:var(--cta);font-weight:800}
header a{color:var(--cta);font-weight:700;text-decoration:none;font-size:.9rem}
main{padding:1.4rem;max-width:1400px;margin:0 auto}
table{width:100%;border-collapse:collapse;background:#fff;border:1px solid var(--line);border-radius:10px;overflow:hidden}
th{background:#eaf0f5;color:var(--brand);text-align:left;font-size:.7rem;letter-spacing:.08em;
text-transform:uppercase;padding:.6rem .7rem;white-space:nowrap}
td{padding:.7rem;border-top:1px solid #edeae2;vertical-align:top;font-size:.92rem}
td.p{min-width:17rem}tr:hover td{background:#fcfcfa}
a{color:var(--brand)}.when{display:inline-block;background:#eaf0f5;color:var(--brand);
font-weight:700;font-size:.78rem;padding:.15rem .5rem;border-radius:99px;white-space:nowrap}
.site{font-size:.82rem;color:var(--muted);overflow-wrap:anywhere;min-width:10rem;max-width:14rem}
.why{font-size:.78rem;color:var(--muted);overflow-wrap:anywhere;min-width:9rem;max-width:12rem}
.ts{color:var(--muted);font-size:.8rem;white-space:nowrap}
.tally{display:flex;flex-wrap:wrap;gap:.4rem;margin:0 0 1.2rem}
.tally a{background:#fff;border:1px solid var(--line);border-radius:99px;padding:.28rem .7rem;
font-size:.82rem;text-decoration:none;font-weight:600}
.empty{background:#fff;border:1px solid var(--line);border-radius:10px;padding:2.4rem;text-align:center;color:var(--muted)}
</style></head><body>
<header><h1>${showPitches ? "Filtered as sales pitches" : "Lead desk"} &mdash; <span class="n">${rows.length}</span> ${site ? esc(site) : "across all sites"}</h1>
<div>${site ? `<a href="?${showPitches ? "pitches=1" : ""}">All sites</a> &nbsp; ` : ""}${
  showPitches
    ? `<a href="?${site ? "site=" + encodeURIComponent(site) : ""}">Back to real leads</a>`
    : `<a href="?${site ? "site=" + encodeURIComponent(site) + "&" : ""}pitches=1">Sales pitches (${pitchTotal})</a>`
} &nbsp; <a href="?${site ? "site=" + encodeURIComponent(site) + "&" : ""}${showPitches ? "pitches=1&" : ""}format=csv">Download CSV</a></div></header>
<main>
${counts.length ? `<div class="tally">${counts.map((c) =>
  `<a href="?site=${encodeURIComponent(c.site)}">${esc(c.site)} <strong>${c.n}</strong></a>`).join("")}</div>` : ""}
${rows.length === 0
  ? `<div class="empty">${showPitches ? "Nothing filtered." : "No form leads yet."}</div>`
  : `<table><thead><tr><th>When</th><th>Site</th><th>Name</th><th>Phone</th>
<th>Call at</th><th>ZIP</th><th>What they said</th><th>Email</th>${showPitches ? "<th>Why filtered</th>" : ""}</tr></thead><tbody>
${rows.map((r) => `<tr>
<td class="ts">${esc((r.created_at || "").replace("T", " ").slice(0, 16))}</td>
<td class="site">${esc(r.site)}</td>
<td><strong>${esc(r.name)}</strong></td>
<td>${tel(r.phone)}</td>
<td><span class="when">${esc(r.best_time)}</span></td>
<td>${esc(r.zip)}</td>
<td class="p">${esc(r.problem)}</td>
<td>${r.email ? `<a href="mailto:${esc(r.email)}">${esc(r.email)}</a>` : ""}</td>
${showPitches ? `<td class="why">${esc(r.spam_reason)}</td>` : ""}
</tr>`).join("")}
</tbody></table>`}
</main></body></html>`;

  return new Response(html, {
    headers: { "Content-Type": "text/html; charset=utf-8", "Cache-Control": "no-store" },
  });
}

// -------------------------------------------------------------------- router
export default { fetch: onRequest };

async function onRequest(request, env) {
  const url = new URL(request.url);
  const host = url.hostname.toLowerCase().replace(/^www\./, "");
  const path = url.pathname.replace(/\/+$/, "") || "/";

  if (path === "/lead") {
    if (request.method === "POST") return postLead(request, env);
    return new Response("", { status: 405, headers: { Allow: "POST" } });
  }
  if (path === "/leads-" + LEAD_SLUG) return leadDesk(request, env);

  if (host.endsWith(".pages.dev") || host === "localhost") {
    return env.ASSETS.fetch(request);
  }

  const at = (p) => {
    const u = new URL(request.url);
    u.pathname = "/" + host + p;
    return env.ASSETS.fetch(new Request(u.toString(), request));
  };

  let res = await at(url.pathname);
  if (res.status === 404 && !url.pathname.endsWith("/")) {
    const retry = await at(url.pathname + "/");
    if (retry.status !== 404) return retry;
  }
  if (res.status === 404) {
    const home = await at("/");
    if (home.status === 200) {
      return new Response(home.body, { status: 404, headers: home.headers });
    }
  }
  return res;
}
