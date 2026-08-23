#!/usr/bin/env python3
"""
emails.py - write a ready-to-send intro email for every prospect.

One email per person in data/prospects.csv. Same offer everywhere; only the trade
words and the city change. Nothing here claims call volume, promises a number, or
sets a deadline - the offer is free leads with no obligation, and price is only
discussed after lead flow is proven.

The legal version is deliberately different. It never says client, case, referral
or recommend, never implies anyone was screened or matched, and offers a flat fee
only - never a share of anything. Those words are what turn a marketing payment
into a prohibited referral arrangement.

    python3 emails.py            # writes data/emails-home.csv, data/emails-legal.csv
"""
import csv, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROSPECTS = os.path.join(HERE, "data", "prospects.csv")
OUT = os.path.join(HERE, "data", "emails-home.csv")
OUT_LEGAL = os.path.join(HERE, "data", "emails-legal.csv")
PREVIEW = os.path.join(HERE, "PREVIEW-EMAILS.md")

# Fill these in before sending. The address and the opt-out line are legally
# required in every commercial email; the sending domain must NOT be the real
# operating domain.
SENDER = {
    "name": "Dan Poore",
    "company": "[COMPANY LEGAL NAME]",
    "address": "[STREET ADDRESS OR MAILBOX]",
}

# Per trade: what the caller is calling about, what to call the business, and the
# short noun used in the subject line. Written the way a customer would say it.
TRADES = {
    "Air Conditioner Repair": dict(
        trade="AC", biz="AC company", subject="AC calls",
        caller="homeowners whose AC has quit", work="AC work"),
    "Air Conditioning Installation": dict(
        trade="AC install", biz="AC company", subject="AC install calls",
        caller="homeowners looking to replace an AC unit", work="AC work"),
    "Furnace Repair": dict(
        trade="furnace", biz="heating company", subject="furnace calls",
        caller="homeowners with no heat", work="heating work"),
    "Emergency Plumbing": dict(
        trade="emergency plumbing", biz="plumbing company", subject="plumbing calls",
        caller="homeowners with a burst pipe or a backed-up drain",
        work="plumbing work"),
    "Leak Detection": dict(
        trade="leak detection", biz="plumbing company", subject="leak calls",
        caller="homeowners who think they have a hidden leak", work="plumbing work"),
    "Garage Door Repair": dict(
        trade="garage door", biz="garage door company", subject="garage door calls",
        caller="homeowners with a door stuck open or a broken spring",
        work="garage door work"),
    "Appliance Repair": dict(
        trade="appliance repair", biz="appliance repair company",
        subject="appliance repair calls",
        caller="homeowners with a dead fridge, washer or oven",
        work="appliance work"),
    "Foundation Repair": dict(
        trade="foundation", biz="foundation company", subject="foundation calls",
        caller="homeowners seeing cracks or a settling floor",
        work="foundation work"),
    "Mold Remediation": dict(
        trade="mold", biz="remediation company", subject="mold calls",
        caller="homeowners who just found mold", work="remediation work"),
    "Water Damage Restoration": dict(
        trade="water damage", biz="restoration company", subject="water damage calls",
        caller="homeowners dealing with a flood or a burst pipe",
        work="restoration work"),
    "Roof Inspection": dict(
        trade="roof inspection", biz="roofing company", subject="roof calls",
        caller="homeowners who want a roof looked at after a storm",
        work="roofing work"),
    "Tile Roof Repair": dict(
        trade="tile roof", biz="roofing company", subject="tile roof calls",
        caller="homeowners with cracked or slipped tiles", work="roofing work"),
    "Gutter Cleaning": dict(
        trade="gutter", biz="gutter company", subject="gutter calls",
        caller="homeowners with overflowing or clogged gutters",
        work="gutter work"),
    "Window Replacement": dict(
        trade="window replacement", biz="window company", subject="window calls",
        caller="homeowners pricing out new windows", work="window work"),
    "Bathroom Remodeling": dict(
        trade="bathroom remodel", biz="remodeling company", subject="bathroom remodel calls",
        caller="homeowners planning a bathroom remodel", work="remodeling work"),
    "Moving Services": dict(
        trade="moving", biz="moving company", subject="moving calls",
        caller="people who need a mover for a local move", work="moving work"),
}

# Per practice area: what the caller is asking about. Never a characterization of
# their situation as a case or a claim, and never anything that sounds like the
# site evaluated them.
LEGAL = {
    "Car Accident Lawyer": dict(
        area="car accident", subject="car accident inquiries",
        caller="people who were just in a car wreck"),
    "Motorcycle Accident Lawyer": dict(
        area="motorcycle accident", subject="motorcycle accident inquiries",
        caller="people who were just in a motorcycle wreck"),
    "Truck Accident Lawyer": dict(
        area="truck accident", subject="truck accident inquiries",
        caller="people who were just hit by a commercial truck"),
    "Personal Injury Lawyer": dict(
        area="personal injury", subject="injury inquiries",
        caller="people who were just injured and are looking for a lawyer"),
    "Dog Bite Lawyer": dict(
        area="dog bite", subject="dog bite inquiries",
        caller="people who were just bitten by a dog"),
    "Wrongful Death Lawyer": dict(
        area="wrongful death", subject="wrongful death inquiries",
        caller="families who just lost someone and are looking for a lawyer"),
    "Criminal Defense Lawyer": dict(
        area="criminal defense", subject="criminal defense inquiries",
        caller="people who were just arrested or charged"),
    "DUI Lawyer": dict(
        area="DUI", subject="DUI inquiries",
        caller="people who were just arrested for DUI"),
    "Domestic Violence Lawyer": dict(
        area="domestic violence", subject="domestic violence inquiries",
        caller="people facing a domestic violence charge or order"),
    "Divorce Lawyer": dict(
        area="divorce", subject="divorce inquiries",
        caller="people looking for a divorce attorney"),
    "Family Law Attorney": dict(
        area="family law", subject="family law inquiries",
        caller="people looking for a family law attorney"),
    "Wrongful Termination Lawyer": dict(
        area="wrongful termination", subject="employment inquiries",
        caller="people who were just fired and are looking for a lawyer"),
}

BODY = """{first} -

I own {domain} and the phone number on it. I build local {trade} sites and get
them ranking in Google. This one brings in {caller} in {city}.

I don't do {work}, so the calls need to go somewhere.

The offer: I point the number at your line and the calls come straight to you.
Free. No contract, no fee, nothing to sign. Take the ones you want, ignore the
rest. Say the word and I'll turn it off.

Be clear on who's carrying the risk, because it isn't you. I paid for the
domain, the site and the number, and I'm the one spending the money and the
months getting it to rank - that's my system and my cost. If this market never
produces, I ate it and you're out nothing. Your total exposure is answering a
phone that rings.

One {biz} per city. Yours alone, not a lead list going out to five shops.

On price, so there's no surprise later: I won't bring up money on a hunch.
There's a bar I have to hit first - steady, repeatable call volume, enough weeks
in a row that I know what a market this size actually produces. Until I hit that
bar there is nothing to talk about. When I do, I'll come to you first with a
month-to-month number, and by then you'll have months of your own calls to judge
it against. You can say no and nothing changes about what you already got.

All I need is a reputable {biz} that answers the phone. Want me to send them
your way?

{sender}
{company}
{address}
Reply "stop" and I won't email you again."""


LEGAL_BODY = """{first} -

I own {domain} and the phone number on it. I build local {area} sites and get
them ranking in Google. This one brings in {caller} in {city}.

First, what I am not: I'm not a referral service. I don't screen anyone, I don't
ask about anyone's situation, I don't evaluate anything, and I never tell a
caller which firm to use. Nobody is matched or recommended to you. The phone
simply rings on your end and you decide what to do with it.

The offer: I point the number at your intake line and the inquiries come
straight to you. Free. No contract, no fee, nothing to sign, and never a
percentage of anything - not now, not ever. Take the ones you want, ignore the
rest. Say the word and I'll turn it off.

Be clear on who's carrying the risk, because it isn't you. I paid for the
domain, the site and the number, and I'm the one spending the money and the
months getting it to rank - that's my system and my cost. If this market never
produces, I ate it and you're out nothing.

One firm per city. Yours alone.

On price, so there's no surprise later: I won't bring up money on a hunch.
There's a bar I have to hit first - steady, repeatable volume, enough weeks in a
row that I know what a market this size actually produces. Until then there is
nothing to talk about. When I get there I'll come to you first and offer you the
site month-to-month at a flat monthly rate - your firm's name and contact
information on it, plainly your own advertising, with a responsible attorney
named on every page. A flat fee for advertising, never a share of a fee. By then
you'll have months of your own numbers to judge it against, and you can say no
without losing anything you already got.

Want the inquiries pointed at your intake line?

{sender}
{company}
{address}
Reply "stop" and I won't email you again."""


def build_legal(row):
    t = LEGAL.get(row["service"])
    if not t:
        return None
    subject = f"{row['city']} {t['subject']} - no cost"
    body = LEGAL_BODY.format(
        first=row["first_name"] or "Hello",
        domain=row["domain"],
        area=t["area"],
        caller=t["caller"],
        city=row["city"],
        sender=SENDER["name"],
        company=SENDER["company"],
        address=SENDER["address"],
    )
    return subject, body


def build(row):
    t = TRADES.get(row["service"])
    if not t:
        return None
    subject = f"{row['city']} {t['subject']} - free, no strings"
    body = BODY.format(
        first=row["first_name"] or "Hi",
        domain=row["domain"],
        trade=t["trade"],
        caller=t["caller"],
        city=row["city"],
        work=t["work"],
        biz=t["biz"],
        sender=SENDER["name"],
        company=SENDER["company"],
        address=SENDER["address"],
    )
    return subject, body


def collect(rows, builder):
    out, skipped = [], 0
    for r in rows:
        built = builder(r)
        if not built:
            skipped += 1
            continue
        subject, body = built
        out.append({
            "domain": r["domain"], "city": r["city"], "state": r["state"],
            "service": r["service"], "company": r["company"],
            "first_name": r["first_name"], "last_name": r["last_name"],
            "email": r["email"], "trade_match": r["trade_match"],
            "subject": subject, "body": body, "status": "not sent",
        })
    # Best candidates first so whoever sends works top down and can stop at 6.
    out.sort(key=lambda r: (r["domain"], r["trade_match"] != "yes"))
    return out, skipped


def examples(rows):
    """One filled-in email per service, so the wording can be read before sending."""
    seen, blocks = set(), []
    for r in rows:
        if r["service"] in seen:
            continue
        seen.add(r["service"])
        blocks.append(
            f"## {r['service']} - {r['city']}, {r['state']}\n\n"
            f"To: {r['first_name']} {r['last_name']}, {r['company']} "
            f"<{r['email']}>\n\n"
            f"**Subject:** {r['subject']}\n\n```\n{r['body']}\n```\n")
    return blocks


def main():
    allrows = list(csv.DictReader(open(PROSPECTS)))
    home, hskip = collect([r for r in allrows if r["niche"] != "legal"], build)
    legal, lskip = collect([r for r in allrows if r["niche"] == "legal"], build_legal)

    for path, rows, skip, label in ((OUT, home, hskip, "home services"),
                                    (OUT_LEGAL, legal, lskip, "legal")):
        if not rows:
            print(f"no {label} rows")
            continue
        with open(path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        print(f"wrote {path}: {len(rows)} {label} emails across "
              f"{len({r['domain'] for r in rows})} markets"
              + (f" ({skip} rows had no template)" if skip else ""))

    with open(PREVIEW, "w") as f:
        f.write("# Intro Emails - One Real Example Per Service\n\n"
                "Generated from `data/emails-home.csv` and "
                "`data/emails-legal.csv`. Every email below is addressed to a "
                "real owner or partner with a verified work email. Same offer "
                "everywhere; only the trade words and the city change.\n\n"
                "Before sending: fill in the company name and street address in "
                "`emails.py`, and send from a separate domain, never the "
                "operating one.\n\n"
                "## Home Services\n\n" + "\n---\n\n".join(examples(home))
                + "\n---\n\n## Legal\n\nThe legal version never says client, "
                "case, referral or recommend, never implies anyone was screened "
                "or matched, and offers a flat monthly fee only - never a share "
                "of a fee.\n\n" + "\n---\n\n".join(examples(legal)))
    print(f"wrote {PREVIEW}")


if __name__ == "__main__":
    main()
