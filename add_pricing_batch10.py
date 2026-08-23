#!/usr/bin/env python3
"""Batch 10: add a fees/contingency pricing block to five dog bite sites."""
import json, pathlib, collections

SITES = pathlib.Path(__file__).parent / "sites"

GABAR = "https://www.gabar.org/handbook?rule=rule55"
FULTON = "https://www.fultonclerk.org/DocumentCenter/View/376/Superior-and-Magistrate-Court-Fee"
ATL = ("https://library.municode.com/ga/atlanta/codes/code_of_ordinances/177780"
       "?nodeId=PTIICOORENOR_CH18AN_ARTIIIDO_S18-62ADRACOREHECOFUCO")
NVRPC = "https://www.leg.state.nv.us/courtrules/rpc.html"
NRS7 = "https://www.leg.state.nv.us/nrs/nrs-007.html"
NRS18 = "https://www.leg.state.nv.us/nrs/nrs-018.html"
CLARKFEE = ("https://www.clarkcountycourts.us/res/clerk/civil-criminal-library/"
            "legal-forms/Filing-Fee-List.pdf")
CLARK10 = ("https://www.clarkcountynv.gov/adobe/assets/urn:aaid:aem:f1f58666-7941-"
           "4544-91ea-dd69326071b7/original/as/titles-1-and-10-final-combined-"
           "ordinance-jan2025.pdf")
CALRULE = ("https://www.calbar.ca.gov/legal-professionals/rules/rules-professional-"
           "conduct/current-rules-professional-conduct/chapter-1-lawyer-client-"
           "relationship")
BPC6146 = "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=6146.&lawCode=BPC"
BPC6147 = "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=6147.&lawCode=BPC"
BPC6148 = "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=6148.&lawCode=BPC"
LAFEE = ("https://lascpubstorage.blob.core.windows.net/cpw/LIBSVCExecutiveSupport-"
         "265-2024FeeSchedule010124.pdf")
LAMC15 = "https://codelibrary.amlegal.com/codes/los_angeles/latest/lamc/0-0-0-136628"
LAMC153 = "https://codelibrary.amlegal.com/codes/los_angeles/latest/lamc/0-0-0-136780"
SACFEE = "https://www.saccourt.ca.gov/fees/docs/fee-schedule.pdf"
SACLIC = "https://animalcare.saccounty.gov/Licensing/Documents/AnimalLicenseApp.pdf"
CRC7955 = "https://www.courts.ca.gov/cms/rules/index.cfm?title=seven&linkid=rule7_955"
NY603 = ("https://www.nycourts.gov/LegacyPDFS/rules/jointappellate/"
         "1st%20Dept.%20-%20603.25.pdf")
NY474A = "https://www.nysenate.gov/legislation/laws/JUD/474-A"
NY474 = "https://www.nysenate.gov/legislation/laws/JUD/474"
CPLR8018 = "https://www.nysenate.gov/legislation/laws/CVP/8018"
NYCDOG = "https://www.nyc.gov/site/doh/services/dog-licenses.page"

PRICING = {}

PRICING["atlantadogbitelawyerpros.com"] = {
    "mode": "fees",
    "fee_kind": "contingency",
    "table_head": "What Georgia's fee rule fixes in a Fulton County dog bite claim, and what it leaves open",
    "col_a": "What it covers",
    "col_b": "What Georgia sets",
    "anchors": [
        {
            "label": "Filing a general civil action, Fulton County Superior Court",
            "value": "$215",
            "detail": "Paid to the Clerk when the complaint is docketed, with a further $8.00 for each party added beyond the first.",
            "source_name": "Fulton County Clerk of Superior Court fee schedule",
            "source_url": FULTON,
        },
        {
            "label": "Factors that decide whether a fee is reasonable",
            "value": "8",
            "detail": "Georgia measures a fee against eight listed factors, one of which is the fee customarily charged in the locality for similar work.",
            "source_name": "Ga. R. Prof. Conduct 1.5(a)",
            "source_url": GABAR,
        },
        {
            "label": "Annual Atlanta dog owner's permit",
            "value": "$3.00",
            "detail": "Charged per dog six months or older, capped at $10.00 for a household however many dogs it keeps.",
            "source_name": "Atlanta Code of Ordinances 18-61(a)(4)",
            "source_url": ATL,
        },
        {
            "label": "Sheriff service of the complaint",
            "value": "$50",
            "detail": "The Fulton schedule lists this for service by the Sheriff, with subpoena service billed separately at $10.00.",
            "source_name": "Fulton County Clerk of Superior Court fee schedule",
            "source_url": FULTON,
        },
    ],
    "fee_rows": [
        {
            "stage": "A fee taken out of a dog bite recovery",
            "share": "No percentage ceiling",
            "note": "Georgia fixes no cap. Rule 1.5(a) bars an unreasonable fee and lists eight factors, including the amount involved, the results obtained, and local custom.",
            "source_name": "Ga. R. Prof. Conduct 1.5(a)",
            "source_url": GABAR,
        },
        {
            "stage": "The contingency agreement itself",
            "share": "Writing required",
            "note": "Rule 1.5(c)(1) requires the writing to give the method of calculation, the percentages on settlement, trial and appeal, and whether expenses come off before or after the fee.",
            "source_name": "Ga. R. Prof. Conduct 1.5(c)(1)",
            "source_url": GABAR,
        },
        {
            "stage": "The statement owed when the matter ends",
            "share": "Written, itemized",
            "note": "Rule 1.5(c)(2) requires the outcome in writing plus the remittance, how it was figured, the attorney fee, and any share paid to an outside lawyer.",
            "source_name": "Ga. R. Prof. Conduct 1.5(c)(2)",
            "source_url": GABAR,
        },
        {
            "stage": "A fee riding on a divorce or a criminal charge",
            "share": "Barred outright",
            "note": "Rule 1.5(d) forbids a contingency in a domestic relations matter tied to the divorce, alimony or support, and forbids one for a criminal defendant.",
            "source_name": "Ga. R. Prof. Conduct 1.5(d)",
            "source_url": GABAR,
        },
        {
            "stage": "Opening the case at the Justice Center",
            "share": "$215 plus $8 a party",
            "note": "The Clerk's schedule adds $50.00 for Sheriff service, $10.00 for subpoena service and $1.00 per motion filed.",
            "source_name": "Fulton County Clerk of Superior Court fee schedule",
            "source_url": FULTON,
        },
        {
            "stage": "Getting an impounded dog back in Atlanta",
            "share": "$7.50 plus $3.00 a day",
            "note": "Sec. 18-61(a)(3) gives the owner seven days from the mailed notice and adds the unpaid permit fee and rabies cost where no current tag was worn.",
            "source_name": "Atlanta Code of Ordinances 18-61(a)(3)",
            "source_url": ATL,
        },
    ],
}

PRICING["lasvegasdogbitelawyerpros.com"] = {
    "mode": "fees",
    "fee_kind": "contingency",
    "table_head": "What Nevada sets on a fee taken from a recovery, and what Clark County charges to litigate",
    "col_a": "What it covers",
    "col_b": "What Nevada sets",
    "anchors": [
        {
            "label": "General civil complaint, Eighth Judicial District Court",
            "value": "$270",
            "detail": "The Clerk's list itemizes the statutory pieces that build this figure, and adds $30.00 for every plaintiff after the first.",
            "source_name": "Eighth Judicial District Court Clerk filing fee list",
            "source_url": CLARKFEE,
        },
        {
            "label": "Contingent fee ceiling against a health care provider",
            "value": "35%",
            "detail": "NRS 7.095 caps a professional negligence fee at 35 percent of the net recovery. An animal attack claim falls outside that statute.",
            "source_name": "NRS 7.095(1)",
            "source_url": NRS7,
        },
        {
            "label": "Expert witness fees taxable as costs",
            "value": "$15,000",
            "detail": "Per expert, for no more than five experts, unless the judge finds the testimony required a larger figure.",
            "source_name": "NRS 18.005(5)",
            "source_url": NRS18,
        },
        {
            "label": "Clark County breeder or show permit",
            "value": "$800",
            "detail": "Charged to start the permit and again each year, dropping to $400 where every animal shows once a year, with a $100 reinspection.",
            "source_name": "Clark County Code 10.08.135",
            "source_url": CLARK10,
        },
    ],
    "fee_rows": [
        {
            "stage": "A share of a dog bite recovery",
            "share": "No stated maximum",
            "note": "Nevada RPC 1.5(a) forbids an unreasonable fee and lists eight yardsticks, from the difficulty of the questions to what the locality customarily charges.",
            "source_name": "Nev. R. Prof. Conduct 1.5(a)",
            "source_url": NVRPC,
        },
        {
            "stage": "How the agreement has to look",
            "share": "Signed, in boldface",
            "note": "RPC 1.5(c) demands a written agreement signed by the client, with the required terms set in boldface at least as large as the largest type in the document.",
            "source_name": "Nev. R. Prof. Conduct 1.5(c)",
            "source_url": NVRPC,
        },
        {
            "stage": "Warnings the document must carry",
            "share": "Loss exposure spelled out",
            "note": "RPC 1.5(c)(3) through (5) require it to say who owes expenses whatever the result, that a loss can mean paying the other side's costs, and what a harassing suit risks.",
            "source_name": "Nev. R. Prof. Conduct 1.5(c)(4)",
            "source_url": NVRPC,
        },
        {
            "stage": "A claim over medical treatment of the wound",
            "share": "35% of the net recovery",
            "note": "NRS 7.095 reaches a professional negligence action against a health care provider, measured after costs of prosecuting the claim come out.",
            "source_name": "NRS 7.095",
            "source_url": NRS7,
        },
        {
            "stage": "Filing at the Regional Justice Center",
            "share": "$270, then $30 a plaintiff",
            "note": "A first appearance by the defense runs $223.00, a third party complaint $135.00, and a summary judgment motion $200.00 on the same list.",
            "source_name": "Eighth Judicial District Court Clerk filing fee list",
            "source_url": CLARKFEE,
        },
        {
            "stage": "Costs a losing side can be taxed",
            "share": "17 listed categories",
            "note": "NRS 18.005 runs from clerks' and reporters' fees to interpreters, process service, photocopies and deposition travel, with experts held to $15,000 each.",
            "source_name": "NRS 18.005",
            "source_url": NRS18,
        },
    ],
}

PRICING["losangelesdogbitelawyerpros.com"] = {
    "mode": "fees",
    "fee_kind": "contingency",
    "table_head": "What California's fee rules set on a dog bite claim, and what the Los Angeles courthouse charges",
    "col_a": "What it covers",
    "col_b": "What the rule or schedule sets",
    "anchors": [
        {
            "label": "First paper, unlimited civil case",
            "value": "$435",
            "detail": "The court's own schedule sets this for a complaint where more than $35,000 is at issue, and the same figure for each responding party.",
            "source_name": "Los Angeles Superior Court civil fee schedule",
            "source_url": LAFEE,
        },
        {
            "label": "Factors in the unconscionability test",
            "value": "13",
            "detail": "California asks whether a fee is unconscionable rather than merely unreasonable, and lists thirteen things that answer the question.",
            "source_name": "Cal. R. Prof. Conduct 1.5(b)",
            "source_url": CALRULE,
        },
        {
            "label": "Advance jury fee, nonrefundable",
            "value": "$150",
            "detail": "Posted under Code of Civil Procedure section 631(b) to keep a jury, with later daily deposits of $15.00 plus juror mileage.",
            "source_name": "Los Angeles Superior Court civil fee schedule",
            "source_url": LAFEE,
        },
        {
            "label": "City of Los Angeles dog license fee",
            "value": "$91.50",
            "detail": "Charged for processing an unaltered dog's license, against $16.50 where a veterinarian certifies the dog cannot breed.",
            "source_name": "L.A. Municipal Code 53.15.3",
            "source_url": LAMC153,
        },
    ],
    "fee_rows": [
        {
            "stage": "A share of a dog bite recovery",
            "share": "No fixed percentage",
            "note": "Rule 1.5(a) bars an unconscionable or illegal fee, and Rule 1.5(b) weighs thirteen factors, among them the fee against the value of the work done.",
            "source_name": "Cal. R. Prof. Conduct 1.5",
            "source_url": CALRULE,
        },
        {
            "stage": "What the contract has to admit",
            "share": "The rate is negotiable",
            "note": "Section 6147(a) requires the agreed rate in writing plus a statement that the fee is not set by law, and 6147(b) makes a defective contract voidable.",
            "source_name": "Cal. Bus. & Prof. Code 6147",
            "source_url": BPC6147,
        },
        {
            "stage": "A claim against a health care provider",
            "share": "25% before filing, 33% after",
            "note": "Section 6146 is the only California percentage ceiling in injury work. It governs professional negligence claims, not a claim against a dog's owner.",
            "source_name": "Cal. Bus. & Prof. Code 6146",
            "source_url": BPC6146,
        },
        {
            "stage": "Opening the file downtown",
            "share": "$435",
            "note": "Government Code section 70611 sets the first paper fee for an unlimited civil case, and the Los Angeles schedule prints it alongside every other courtroom charge.",
            "source_name": "Los Angeles Superior Court civil fee schedule",
            "source_url": LAFEE,
        },
        {
            "stage": "Trial deposits, jury and reporter",
            "share": "$150 jury, $764 a day reporter",
            "note": "The reporter per diem falls to $382 for a session under four hours and $30 for an hour or less, under Government Code section 68086.",
            "source_name": "Los Angeles Superior Court civil fee schedule",
            "source_url": LAFEE,
        },
        {
            "stage": "A case designated complex",
            "share": "$1,000 a side, $18,000 cap",
            "note": "Government Code section 70616 charges one fee for all plaintiffs and another for each defendant, stopping at $18,000 for the whole case.",
            "source_name": "Los Angeles Superior Court civil fee schedule",
            "source_url": LAFEE,
        },
    ],
}

PRICING["sacramentodogbitelawyerpros.com"] = {
    "mode": "fees",
    "fee_kind": "contingency",
    "table_head": "What California's fee statutes require, and the tiers Sacramento Superior Court prints",
    "col_a": "What it covers",
    "col_b": "What the rule or schedule sets",
    "anchors": [
        {
            "label": "First paper where the claim stays under $10,000",
            "value": "$225",
            "detail": "The schedule the court posts steps up to $370 above $10,000 and $435 once more than $35,000 is at issue.",
            "source_name": "Sacramento Superior Court civil fee schedule",
            "source_url": SACFEE,
        },
        {
            "label": "Motion for summary judgment",
            "value": "$500",
            "detail": "Government Code section 70617(d) prices this one motion at $500 while an ordinary motion needing a hearing costs $60.",
            "source_name": "Sacramento Superior Court civil fee schedule",
            "source_url": SACFEE,
        },
        {
            "label": "Threshold that forces a written fee contract",
            "value": "$1,000",
            "detail": "Where hourly or flat-rate work is reasonably expected to cost the client more than this, section 6148 requires the contract in writing.",
            "source_name": "Cal. Bus. & Prof. Code 6148(a)",
            "source_url": BPC6148,
        },
        {
            "label": "Annual county license, unaltered dog",
            "value": "$50",
            "detail": "Sacramento County Animal Care charges this a year in the unincorporated county, against $15 for an altered animal.",
            "source_name": "Sacramento County Animal Care license fees",
            "source_url": SACLIC,
        },
    ],
    "fee_rows": [
        {
            "stage": "The cut taken from a dog bite recovery",
            "share": "Unconscionability standard",
            "note": "Rule 1.5(a) prohibits an unconscionable or illegal fee. Factor (b)(3) asks how the fee compares with the value of the services actually performed.",
            "source_name": "Cal. R. Prof. Conduct 1.5(a)",
            "source_url": CALRULE,
        },
        {
            "stage": "Contents of a contingency contract",
            "share": "Rate, costs, negotiability",
            "note": "Section 6147(a) requires the rate, how disbursements affect the fee and the recovery, and the plain statement that the rate is negotiable, not fixed by law.",
            "source_name": "Cal. Bus. & Prof. Code 6147(a)",
            "source_url": BPC6147,
        },
        {
            "stage": "A recovery belonging to a child",
            "share": "The judge sets it",
            "note": "Rule 7.955 makes a court apply a reasonable fee standard, weighing fourteen factors including risk of loss, costs advanced and delay in payment.",
            "source_name": "Cal. R. Ct. 7.955",
            "source_url": CRC7955,
        },
        {
            "stage": "Hourly or flat-rate work above $1,000",
            "share": "Writing, or voidable",
            "note": "Section 6148 requires the basis of compensation and the nature of the services in writing, and a bill within ten days of a client's request.",
            "source_name": "Cal. Bus. & Prof. Code 6148",
            "source_url": BPC6148,
        },
        {
            "stage": "Filing tier by amount at issue",
            "share": "$225, $370 or $435",
            "note": "Reclassifying a limited case as unlimited costs $140 more, a continuance $20, and a change of venue $50 on the schedule the court publishes.",
            "source_name": "Sacramento Superior Court civil fee schedule",
            "source_url": SACFEE,
        },
        {
            "stage": "Licensing the dog in Sacramento County",
            "share": "$50 or $15, plus $25 late",
            "note": "County Code 8.24.030 requires the license; Animal Care charges $50 a year unaltered, $15 altered, $45 for a qualifying ranch or competition dog.",
            "source_name": "Sacramento County Animal Care license fees",
            "source_url": SACLIC,
        },
    ],
}

PRICING["newyorkdogbitelawyerpros.com"] = {
    "mode": "fees",
    "fee_kind": "contingency",
    "table_head": "The fee schedule the First Department applies to a New York County injury claim",
    "col_a": "What it covers",
    "col_b": "What the schedule sets",
    "anchors": [
        {
            "label": "Flat ceiling under Schedule B",
            "value": "33 1/3%",
            "detail": "Available only where the original retainer chose it, and choosing it gives up any later application for extra compensation.",
            "source_name": "22 NYCRR 603.25(e)(2)",
            "source_url": NY603,
        },
        {
            "label": "Top step of the graduated Schedule A",
            "value": "50%",
            "detail": "Applies to the first $1,000 recovered only, then the schedule falls to 40, 35 and finally 25 percent above $25,000.",
            "source_name": "22 NYCRR 603.25(e)(2)",
            "source_url": NY603,
        },
        {
            "label": "Index number from the County Clerk",
            "value": "$210",
            "detail": "CPLR 8018 sets $190 payable in advance plus $5 for records management and $15 for the cultural education account.",
            "source_name": "CPLR 8018(a)",
            "source_url": CPLR8018,
        },
        {
            "label": "City license, unaltered dog over four months",
            "value": "$34",
            "detail": "A spayed or neutered dog is $8.50 a year, and a lapsed license carries a $2 fine for each year it went unrenewed.",
            "source_name": "NYC Health dog license fees",
            "source_url": NYCDOG,
        },
    ],
    "fee_rows": [
        {
            "stage": "Schedule A, the graduated option",
            "share": "50 / 40 / 35 / 25 percent",
            "note": "Fifty percent of the first $1,000, forty of the next $2,000, thirty-five of the next $22,000, then twenty-five percent of everything past $25,000.",
            "source_name": "22 NYCRR 603.25(e)(2)",
            "source_url": NY603,
        },
        {
            "stage": "Schedule B, the flat option",
            "share": "Not above 33 1/3 percent",
            "note": "The rule allows it only if the initial contract says so, and then shuts off the extraordinary circumstances application that Schedule A keeps open.",
            "source_name": "22 NYCRR 603.25(e)(2)",
            "source_url": NY603,
        },
        {
            "stage": "Whether the percentage runs on net or gross",
            "share": "The client picks",
            "note": "Under 603.25(e)(3) the retainer must describe both methods and show the choice, and hospital and treatment liens are never deducted first.",
            "source_name": "22 NYCRR 603.25(e)(3)",
            "source_url": NY603,
        },
        {
            "stage": "Anything above the schedule",
            "share": "Unconscionable without an order",
            "note": "603.25(e)(1) treats an excess fee as the exaction of unreasonable and unconscionable compensation unless a judge authorizes it in a written order.",
            "source_name": "22 NYCRR 603.25(e)(1)",
            "source_url": NY603,
        },
        {
            "stage": "Malpractice sliding scale",
            "share": "30 / 25 / 20 / 15 / 10 percent",
            "note": "Judiciary Law 474-a governs medical, dental and podiatric malpractice only. A bite claim against an owner is expressly outside it.",
            "source_name": "Judiciary Law 474-a(2)",
            "source_url": NY474A,
        },
        {
            "stage": "A claim belonging to a child",
            "share": "Court fixes the amount",
            "note": "Judiciary Law 474 voids a percentage agreement with an infant's guardian unless the court, on notice, summarily values the services and orders the fee.",
            "source_name": "Judiciary Law 474",
            "source_url": NY474,
        },
    ],
}


def main():
    for domain, block in PRICING.items():
        p = SITES / domain / "site.json"
        raw = p.read_text()
        data = json.loads(raw, object_pairs_hook=collections.OrderedDict)
        data.pop("pricing", None)
        out = collections.OrderedDict()
        for k, v in data.items():
            out[k] = v
            if k == "schema":
                out["pricing"] = block
        assert "pricing" in out, domain
        text = json.dumps(out, indent=1, ensure_ascii=False)
        if raw.endswith("\n"):
            text += "\n"
        p.write_text(text)
        print("wrote pricing block:", domain)


if __name__ == "__main__":
    main()
