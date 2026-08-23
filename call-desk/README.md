# call-desk — what happens when one of the 83 numbers rings

Live at **https://call-desk-xi.vercel.app** (Vercel project `call-desk`, account `dpoore-6096`).

Every one of the 83 markets has its own phone number, and every number is now
attached to its own handler on Telnyx. Nothing is shared between markets, so a
call can always be traced back to exactly one site.

## The two states a market can be in

**Not sold yet (all 83 are here right now).** The call is answered, the caller
hears the market's own greeting, leaves a message, and hangs up. The message and
the caller's number land in the call log.

```xml
<Response>
  <Say>Thanks for calling Sacramento Air Conditioner Repair Pros. Leave your name,
       your number and the address, and we will call you right back.</Say>
  <Record maxLength="120" timeout="5" finishOnKey="#"/>
  <Say>Got it. We will call you right back.</Say>
  <Hangup/>
</Response>
```

**Sold.** The call rings the contractor for 25 seconds. Before he is connected he
hears "Call from your Sacramento air conditioner repair website". If he does not
pick up, the caller falls straight through to the same voicemail, so no call is
ever lost.

```xml
<Response>
  <Dial timeout="25"><Number url=".../w/sacramentoacrepair.com.xml">+1XXXXXXXXXX</Number></Dial>
  <Say>Thanks for calling ...</Say>
  <Record .../>
  <Hangup/>
</Response>
```

The customer's own number is passed through, so the contractor sees who is
calling and can call back directly. **No call is recorded** — only voicemail
messages, which need no notice in any state.

## Turning a market on or off

```
python3 flip.py sacramentoacrepair.com 916-555-1234   # calls now ring that shop
python3 flip.py sacramentoacrepair.com off            # back to taking messages
python3 flip.py --status                              # who is live right now
```

That is the whole thing: one command, about ten seconds, no phone number changes
and nothing to reconfigure on Telnyx. Needs `VERCEL_TOKEN` in the environment.

## The call log

```
python3 call_log.py            # pull the last 2 days and append to log/calls.csv
python3 call_log.py --since 2026-09-01
python3 call_log.py --report   # summary per market, no API calls
```

`log/calls.csv` is the permanent record and lives in this repo. One row per call:

| column | meaning |
| --- | --- |
| `when_pt` | date and time, Pacific |
| `domain` / `city` / `service` | which market the call came from |
| `caller` | the customer's number |
| `tracking_number` | the number on that site |
| `seconds_on_call` | how long the call lasted |
| `left_message` | yes / no |
| `message_seconds` | length of the voicemail |

Telnyx only keeps raw call events for a short window, so run `call_log.py` on a
schedule. Once it is in the CSV it is ours forever.

### The page

**https://call-desk-xi.vercel.app/calls-46b11d3e1d66ba86**

Totals at the top, a per-market table, then every call with a filter box. Long
random path, `noindex`, and the raw CSV is not published — but treat the link as
private, it has customers' phone numbers on it. Rebuild it with
`python3 build_log_page.py` (the path is stored in `log_slug.txt` so it never
changes).

### It updates itself

A scheduled task runs every day at 7:00am Pacific: pull the repo, pull new calls
from Telnyx, rebuild the page, deploy, commit and push. It reports back how many
calls came in and from which markets, or says nothing came in.

Test calls we place ourselves are skipped automatically — any call whose caller
is one of our own 83 numbers is ignored, so the log only ever holds real ones.

Voicemail audio is at `GET /v2/recordings` on Telnyx; each download link is
signed and expires 10 minutes after it is issued, so fetch it fresh when needed.

### One honest gap

A caller who hangs up during the greeting, before the beep, leaves no message and
so no voicemail row. The call itself is still counted from the Telnyx call
events, so the count is right — there is just nothing to listen to. Nothing can
be done about that short of recording every call, which we are not doing.

## Files

| file | what it is |
| --- | --- |
| `routes.json` | the only thing you edit: domain → forwarding number, or `null` for voicemail |
| `build_xml.py` | writes `v/*.xml` and `w/*.xml` from `routes.json` + the sites' `site.json` |
| `v/<domain>.xml` | what happens when that market's number rings |
| `w/<domain>.xml` | the whisper the contractor hears before being connected |
| `index.json` | flat list: domain, city, service, tracking number, current forward |
| `wiring.json` | domain → Telnyx app id and number id (written by `wire_numbers.py`) |
| `flip.py` | turn a market live or back to voicemail, and deploy |
| `call_log.py` | pull calls into `log/calls.csv` and print the summary |
| `wire_numbers.py` | one-time: create the Telnyx app per market and attach its number |
| `verify_wiring.py` | read the truth back off Telnyx and off the live site and check it |
| `t/test.xml` | a 90-second pause, used only for placing test calls |
| `build_log_page.py` | writes the log page from `log/calls.csv` |
| `log_slug.txt` | the random path the log page is published at |

## Verifying after any change

```
python3 verify_wiring.py               # with the Telnyx credential
python3 verify_wiring.py --files-only  # WITHOUT it (the Telnyx proxy blocks other hosts)
```

Both currently pass for all 83.

## How this was tested (2026-08-22)

Real calls placed through Telnyx to `+19168849420` (sacramentoacrepair.com):

1. **Voicemail path** — greeting played, `<Record>` ran, a 6-second recording
   appeared at `/v2/recordings` tagged to the Sacramento app with the caller's
   number, start and end times and duration.
2. **Forwarding path** — flipped Sacramento to a second number, placed a call:
   Telnyx dialled it, fetched the whisper document, played the whisper to the
   called party, then fired `call_bridged`. The caller heard ringback throughout,
   and the original caller ID was carried the whole way.

The whisper only works with the `url` attribute on `<Number>`. Putting it on
`<Dial>` is accepted but silently skipped — the call bridges with no whisper.

## Notes for UG

- Pure static hosting. No server, no database, no secrets in this project.
- One Telnyx TeXML application per market, named after the domain. Per-market
  apps are what make call events attributable to a single market.
- Telnyx rate limit is 5 requests/second and going over returns **empty
  responses, not 429s** — treat an empty body as "retry", never as zero.
- Use `curl`, not `httpx`: the sandbox proxy that injects the Telnyx credential
  is not picked up by `httpx`.
