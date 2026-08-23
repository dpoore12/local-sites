# Phone numbers

One number per market, in that market's own area code. The number is how a call
gets attributed to a site, which is the entire basis for charging rent — two
sites sharing a number means you cannot tell a tenant what they are getting.

## Position, 2026-08-22

- **73 numbers bought** at Telnyx, $0.79 one-time and $0.79/month each.
  $57.67 spent, $57.67/month recurring. All verified active on the account.
- **10 markets use numbers Dan already owned**, confirmed unused elsewhere.
- 128 numbers now sit on the account: these 73 plus 55 that predate this.

## The 10 markets on pre-existing numbers

Dan confirmed on 2026-08-22 that these ten numbers, already on his account, are
not live in MarketCall, Ringba or any other campaign. Each one is now assigned
to the market whose area code it matches, so nothing extra had to be bought.

| Market | Number |
|---|---|
| Houston, TX — Motorcycle Accident Lawyer | `+17137154760` |
| McKinney, TX — Garage Door Repair | `+12149355494` |
| Allen, TX — Air Conditioner Repair | `+12147224321` |
| Dallas, TX — Wrongful Death Lawyer | `+12146170560` |
| Los Angeles, CA — Dog Bite Lawyer | `+12139531047` |
| Atlanta, GA — Dog Bite Lawyer | `+14046667615` |
| Phoenix, AZ — Leak Detection | `+16028940220` |
| Atlanta, GA — Emergency Plumbing | `+14043414588` |
| Los Angeles, CA — AC Installation | `+12137719221` |
| New York, NY — Dog Bite Lawyer | `+16469149310` |

**All 83 markets now have a real number and no two share one.** Zero
placeholders remain, so the build no longer blocks any site from publishing on
phone grounds.

## Area codes: what the audit found

Telnyx inventory skews toward **overlay** codes, and following it blindly would
have put the wrong-feeling number on a dozen sites. It offered 346 for Houston
over 713, 720 for Denver over 303, 331 for Naperville over 630, 737 for Austin
over 512, 669 for San Jose over 408, 980 for Charlotte over 704, 984 for Raleigh
over 919, 279 for Sacramento over 916, 945 for Dallas over 214.

Those are technically local and technically wrong. Every number bought here uses
the code a resident recognises, and the stored code had stock in every case.

One genuine data error was found and fixed: **Arlington, TX was stored primary
214**, a Dallas code. Arlington is Tarrant County — 817/682. It had been matched
to an existing 214 number on that basis. It now has its own 682 number.

Nine cities returned no carrier data at all because their numbers sit under a
neighbouring rate center rather than the city itself: Ann Arbor, Arvada,
Bellevue, Eden Prairie, Marietta, New York, Oceanside, Parker, West Covina. The
stored code was kept for those and the buy succeeded in each.

## What a bought number does not do

Nothing, yet. **None of the 73 is routed.** Each one rings nowhere until a
destination is set — the tenant's line once there is a tenant, and Dan's line
before that, since the hook is handing over live calls. That routing is the next
piece of work and it is not started.

## Refreshing this

    python3 phones.py       # re-read the account, rewrite this file

## Routing — built and tested 2026-08-22

All 83 numbers are now attached to their own handler on Telnyx. Every call is
answered, logged, and (once a market is sold) bridged to the contractor with a
whisper. Nothing is recorded except voicemail messages.

- Handlers live at https://call-desk-xi.vercel.app — see `call-desk/README.md`
- Turn a market live: `cd call-desk && python3 flip.py <domain> <phone>`
- Turn it back to voicemail: `python3 flip.py <domain> off`
- Call log: `python3 call_log.py` → `call-desk/log/calls.csv` (permanent, in this repo)
- Check everything: `python3 verify_wiring.py` and `verify_wiring.py --files-only`

Verified by real test calls: voicemail path records and logs; forwarding path
plays the whisper to the contractor, then bridges, preserving the caller's number.
