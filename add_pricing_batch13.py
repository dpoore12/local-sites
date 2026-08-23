#!/usr/bin/env python3
"""Batch 13: pricing blocks for 2 contingency (motorcycle) + 3 criminal-shape family sites."""
import json, pathlib, collections

ROOT = pathlib.Path(__file__).parent
SITES = ROOT / "sites"

# --- sources ---------------------------------------------------------------
TX104 = "https://legalethicstexas.com/resources/rules/texas-disciplinary-rules-of-professional-conduct/fees/"
HCDC = "https://www.hcdistrictclerk.com/Common/Civil/pdf/Fee_Schedule_Civil_and_Family.pdf"
TX16003 = "https://law.justia.com/codes/texas/civil-practice-and-remedies-code/title-2/subtitle-b/chapter-16/subchapter-a/section-16-003/"
TX33001 = "https://law.justia.com/codes/texas/civil-practice-and-remedies-code/title-2/subtitle-c/chapter-33/subchapter-a/section-33-001/"
TX55004 = "https://codes.findlaw.com/tx/property-code/prop-sect-55-004/"
TX601072 = "https://law.justia.com/codes/texas/transportation-code/title-7/subtitle-d/chapter-601/subchapter-d/section-601-072/"

LAROPC = "https://www.ladb.org/Material/Publication/ROPC/ROPC.pdf"
LA34931 = "https://www.legis.la.gov/legis/Law.aspx?d=1386443"
LA2323 = "https://www.legis.la.gov/legis/law.aspx?d=109387"
ORLEANS = "https://www.orleanscivilclerk.com/memos/feeschedule2026-07-01.pdf"
LA1733 = "https://www.legis.la.gov/legis/Law.aspx?d=111291"
LA37218 = "https://codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-37-sect-218/"
LA94752 = "https://legis.la.gov/legis/Law.aspx?d=108040"

CORPC15 = "https://www.cobar.org/For-Members/Opinions-Rules-Statutes/Rules-of-Professional-Conduct/Rule-15-Fees"
COFEES = "https://www.coloradojudicial.gov/self-help/list-fees"
COODR = "https://www.coloradojudicial.gov/court-services/mediation-services-and-other-dispute-resolution-options/odr-policies-and-procedures"
CO1410119 = "https://law.justia.com/codes/colorado/title-14/dissolution-of-marriage-parental-responsibilities/article-10/section-14-10-119/"

FLBAR4 = "https://www-media.floridabar.org/uploads/2026/06/2026_12-JUNE-Chapter-4-RRTFB-1.pdf"
FL74130 = "https://www.flsenate.gov/Laws/Statutes/2025/741.30"
FL93808 = "https://www.flsenate.gov/Laws/Statutes/2025/938.08"
FL741281 = "https://www.flsenate.gov/Laws/Statutes/2025/741.281"
FL741283 = "https://www.flsenate.gov/Laws/Statutes/2025/741.283"
FL78403 = "https://www.flsenate.gov/Laws/Statutes/2025/784.03"
FL775082 = "https://www.flsenate.gov/Laws/Statutes/2025/775.082"
BROWARDDV = "https://www.browardclerk.org/Divisions/DomesticViolence"
BROWARDFEL = "https://www.browardclerk.org/Divisions/Felony"
HILLSFEES = "https://www.hillsclerk.com/about-us/fees-and-fines"
FL28241 = "https://www.flsenate.gov/Laws/Statutes/2025/28.241"
FL44108 = "https://www.flsenate.gov/Laws/Statutes/2025/44.108"
FL6116 = "https://www.flsenate.gov/Laws/Statutes/2025/61.16"
FL6121 = "https://www.flsenate.gov/Laws/Statutes/2025/61.21"

PRICING = {}

PRICING["houstonmotorcycleaccidentlawyerpros.com"] = {
    "mode": "fees",
    "fee_kind": "contingency",
    "table_head": "What Texas fixes in a Harris County motorcycle claim, and what it leaves to the written agreement",
    "col_a": "Where the money goes",
    "col_b": "What Texas law fixes",
    "anchors": [
        {
            "label": "Percentage ceiling on an injury fee",
            "value": "None stated",
            "detail": "Rule 1.04 bars an illegal or unconscionable fee and lists eight factors for testing one. It prints no percentage for a negligence claim.",
            "source_name": "Tex. Disciplinary Rules Prof. Conduct 1.04(a)-(b)",
            "source_url": TX104,
        },
        {
            "label": "New civil suit, filed without service",
            "value": "$350",
            "detail": "Charged by the Harris County District Clerk to open a civil case. A citation is $8 more, and service through county civil process is $85.",
            "source_name": "Harris County District Clerk fee schedule",
            "source_url": HCDC,
        },
        {
            "label": "Deadline to file a personal injury suit",
            "value": "Two years",
            "detail": "Measured from the day the cause of action accrues, and from the date of death where the injury caused one. Physical evidence on a bike disappears far sooner.",
            "source_name": "Tex. Civ. Prac. & Rem. Code 16.003(a)",
            "source_url": TX16003,
        },
        {
            "label": "Ceiling on a hospital lien against the recovery",
            "value": "50 percent",
            "detail": "A hospital lien is capped at the lesser of first-100-day charges, half of all amounts recovered, or the amount the trier of fact specified less pro rata fees and expenses.",
            "source_name": "Tex. Prop. Code 55.004(b)",
            "source_url": TX55004,
        },
    ],
    "fee_rows": [
        {
            "stage": "The fee itself, in a crash claim",
            "share": "No statutory percentage",
            "note": "A fee is unconscionable only if a competent lawyer could not form a reasonable belief that it is reasonable, judged against the eight factors in paragraph (b).",
            "source_name": "Tex. Disciplinary Rules Prof. Conduct 1.04(a)-(b)",
            "source_url": TX104,
        },
        {
            "stage": "The written agreement",
            "share": "Required terms",
            "note": "Paragraph (d) requires writing, the method of determination, separate percentages for settlement, trial and appeal, which expenses are deducted, and whether they come out before or after the fee is figured.",
            "source_name": "Tex. Disciplinary Rules Prof. Conduct 1.04(d)",
            "source_url": TX104,
        },
        {
            "stage": "A referral or a second firm",
            "share": "Client consent in writing",
            "note": "A division of fees requires the client's written consent to the terms, the identity of every lawyer involved, whether fees are divided by services or responsibility, and each share.",
            "source_name": "Tex. Disciplinary Rules Prof. Conduct 1.04(f)(2)",
            "source_url": TX104,
        },
        {
            "stage": "Filing, citation and service in Harris County",
            "share": "$350 / $8 / $85",
            "note": "New civil suit, citation including one copy, and service by county civil process. Service by mail adds $15, clerk service by certified mail is $100, and the county jury fee is $10.",
            "source_name": "Harris County District Clerk fee schedule",
            "source_url": HCDC,
        },
        {
            "stage": "The rider's own share of fault",
            "share": "Bar above 50 percent",
            "note": "A claimant may not recover damages at all if his percentage of responsibility is greater than 50 percent. Below that line, damages are reduced by the share assigned.",
            "source_name": "Tex. Civ. Prac. & Rem. Code 33.001",
            "source_url": TX33001,
        },
        {
            "stage": "The at-fault driver's minimum coverage",
            "share": "$30,000 / $60,000 / $25,000",
            "note": "Texas financial responsibility limits per person, per collision for two or more people, and for property damage. A trauma admission can exceed the per-person figure on its own.",
            "source_name": "Tex. Transp. Code 601.072",
            "source_url": TX601072,
        },
    ],
}

PRICING["neworleansmotorcycleaccidentlawyerpros.com"] = {
    "mode": "fees",
    "fee_kind": "contingency",
    "table_head": "What Louisiana law fixes in an Orleans Parish motorcycle claim, and what the signed agreement sets",
    "col_a": "Each piece of the recovery",
    "col_b": "What the rule, code article or clerk sets",
    "anchors": [
        {
            "label": "Percentage ceiling on a crash claim fee",
            "value": "None stated",
            "detail": "Rule 1.5 tests a fee for reasonableness against eight factors and permits a contingent fee in a civil matter. It publishes no percentage.",
            "source_name": "La. Rules of Prof. Conduct 1.5",
            "source_url": LAROPC,
        },
        {
            "label": "Prescriptive period for a delictual action",
            "value": "Two years",
            "detail": "Running from the day the injury or damage is sustained, under the period enacted by Acts 2024, No. 423, effective July 1, 2024.",
            "source_name": "La. Civ. Code art. 3493.1",
            "source_url": LA34931,
        },
        {
            "label": "Claimant fault that bars recovery outright",
            "value": "51 percent",
            "detail": "Recovery is barred where the injured person's share of fault is equal to or greater than fifty-one percent, under the amendment effective January 1, 2026.",
            "source_name": "La. Civ. Code art. 2323",
            "source_url": LA2323,
        },
        {
            "label": "Plaintiff's filing fee on an original petition",
            "value": "$514.50",
            "detail": "Orleans Parish Civil District Court, effective July 1, 2026: a $489.50 filing fee plus a $25 building fee. A request for trial by jury is $780 more.",
            "source_name": "Orleans Parish Clerk of Civil District Court fee schedule",
            "source_url": ORLEANS,
        },
    ],
    "fee_rows": [
        {
            "stage": "The fee on a motorcycle claim",
            "share": "Set by agreement, tested for reasonableness",
            "note": "Rule 1.5(a) forbids an unreasonable fee and lists the factors used to measure one. Nothing in the rule states a percentage a Louisiana lawyer must charge.",
            "source_name": "La. Rules of Prof. Conduct 1.5(a)",
            "source_url": LAROPC,
        },
        {
            "stage": "The contingent fee agreement",
            "share": "Signed writing, copy to client",
            "note": "Paragraph (c) requires a writing signed by the client with a copy handed over at signing, the percentages for settlement, trial and appeal, the expenses deducted, whether they come off before or after the fee, and a closing written statement.",
            "source_name": "La. Rules of Prof. Conduct 1.5(c)",
            "source_url": LAROPC,
        },
        {
            "stage": "The lawyer's claim on the recovery",
            "share": "First privilege",
            "note": "By written contract signed by the client, an attorney may acquire an interest in the subject matter that ranks as a first privilege superior to other privileges and security interests.",
            "source_name": "La. R.S. 37:218(A)",
            "source_url": LA37218,
        },
        {
            "stage": "Medical provider and hospital privileges",
            "share": "On the net amount payable",
            "note": "A provider privilege attaches to the net amount payable to the injured person out of any recovery, and the statute states that an attorney's privilege takes precedence over it.",
            "source_name": "La. R.S. 9:4752",
            "source_url": LA94752,
        },
        {
            "stage": "Opening the suit in Orleans Parish",
            "share": "$514.50 / $174 / $780",
            "note": "Original petition, an amending or supplemental petition, and a request for trial by jury. Naming more than five defendants adds $132 and a petition of intervention is $234.50.",
            "source_name": "Orleans Parish Clerk of Civil District Court fee schedule",
            "source_url": ORLEANS,
        },
        {
            "stage": "Cash deposit to hold a jury",
            "share": "$5,000",
            "note": "In a damages suit where an individual petitioner admits the cause of action exceeds $10,000 and is less than $50,000, the deposit is due within sixty days of the jury request or the jury is waived.",
            "source_name": "La. Code Civ. Proc. art. 1733(A)(2)(a)",
            "source_url": LA1733,
        },
    ],
}

PRICING["denverdivorcelawyerpros.com"] = {
    "mode": "fees",
    "fee_kind": "criminal",
    "table_head": "What Colorado forbids in a divorce fee, what it requires in writing, and what the court charges",
    "col_a": "The item",
    "col_b": "What the rule, statute or fee list sets",
    "anchors": [
        {
            "label": "Fee contingent on securing the divorce",
            "value": "Prohibited",
            "detail": "No contingent fee agreement may be made in a domestic relations matter where payment turns on securing a divorce or on the amount of maintenance, child support, or property settlement in lieu of those amounts.",
            "source_name": "Colo. RPC 1.5(c)(4)(ii)",
            "source_url": CORPC15,
        },
        {
            "label": "Petition for divorce, legal separation or annulment",
            "value": "$260",
            "detail": "Statutory filing fee published by the Colorado Judicial Branch under C.R.S. 13-32-101. A response is $146 and a petition for allocation of parental responsibilities is $252.",
            "source_name": "Colorado Judicial Branch list of fees",
            "source_url": COFEES,
        },
        {
            "label": "Court-connected mediation, each party",
            "value": "$75 per hour",
            "detail": "The Office of Dispute Resolution charges each party that rate for mediation, case preparation and preparing the memorandum of understanding, and a neutral may collect a two-hour advance deposit.",
            "source_name": "Colorado Judicial Branch ODR policies and procedures",
            "source_url": COODR,
        },
        {
            "label": "Order making one spouse pay the other's fees",
            "value": "Available",
            "detail": "After considering the financial resources of both parties, the court may order a party to pay a reasonable amount of the other party's fees and costs, including work done before filing or after judgment.",
            "source_name": "C.R.S. 14-10-119",
            "source_url": CO1410119,
        },
    ],
    "fee_rows": [
        {
            "stage": "A fee tied to the outcome",
            "share": "Prohibited, on two specific hooks",
            "note": "The bar reaches payment contingent on securing the divorce and payment sized by the maintenance, support or property figure. It is not a bar on every arrangement in a family case.",
            "source_name": "Colo. RPC 1.5(c)(4)(ii)",
            "source_url": CORPC15,
        },
        {
            "stage": "Collecting a past-due support balance",
            "share": "Contingent fee allowed",
            "note": "The comment to the rule states the prohibition does not preclude a contingent fee for recovering post-judgment balances due under support, maintenance or other financial orders.",
            "source_name": "Colo. RPC 1.5, comment [6]",
            "source_url": CORPC15,
        },
        {
            "stage": "How the terms are set",
            "share": "In writing, up front",
            "note": "Paragraph (b) requires the basis or rate of the fee, the expenses the client owes, and the scope of the representation communicated in writing before or within a reasonable time after starting, and changes in writing too.",
            "source_name": "Colo. RPC 1.5(b)",
            "source_url": CORPC15,
        },
        {
            "stage": "Money paid in advance",
            "share": "Client property until earned",
            "note": "Advances of unearned fees belong to the client and stay in trust until a benefit is conferred, and paragraph (g) prohibits nonrefundable fees and nonrefundable retainers.",
            "source_name": "Colo. RPC 1.5(f)-(g)",
            "source_url": CORPC15,
        },
        {
            "stage": "Court costs, start to finish",
            "share": "$260 / $146 / $105",
            "note": "Petition, response, and a motion to modify a decree or final order filed more than sixty days after it entered. Registering a foreign decree is $201.",
            "source_name": "Colorado Judicial Branch list of fees",
            "source_url": COFEES,
        },
        {
            "stage": "Mediation before a contested hearing",
            "share": "$75 per party, per hour",
            "note": "Billed by the Office of Dispute Resolution with a possible two-hour deposit, and up to two hours chargeable for a late cancellation or a no-show. Private mediators set their own rates.",
            "source_name": "Colorado Judicial Branch ODR policies and procedures",
            "source_url": COODR,
        },
    ],
}

PRICING["fortlauderdaledomesticviolencelawyer.com"] = {
    "mode": "fees",
    "fee_kind": "criminal",
    "table_head": "What Florida forbids in a defense fee, and the amounts Broward County attaches to each track",
    "col_a": "The item",
    "col_b": "What the rule, statute or clerk sets",
    "anchors": [
        {
            "label": "Contingent fee for a criminal defendant",
            "value": "Prohibited",
            "detail": "A lawyer must not enter into an arrangement for, charge, or collect a contingent fee for representing a defendant in a criminal case. A battery charge under chapter 741 is a criminal case.",
            "source_name": "R. Regulating Fla. Bar 4-1.5(f)(3)(B)",
            "source_url": FLBAR4,
        },
        {
            "label": "Filing fee for a petition for protection",
            "value": "$0",
            "detail": "Assessment of a filing fee for a petition for protection against domestic violence is prohibited, and no bond is required for entry of an injunction.",
            "source_name": "Fla. Stat. 741.30(2)(a)",
            "source_url": FL74130,
        },
        {
            "label": "Surcharge on a domestic violence offense",
            "value": "$201",
            "detail": "The court shall impose it on a conviction, with $85 to the Domestic Violence Trust Fund. Payment is a condition of probation or other court-ordered supervision.",
            "source_name": "Fla. Stat. 938.08",
            "source_url": FL93808,
        },
        {
            "label": "Application for court-appointed counsel",
            "value": "$50",
            "detail": "Paid to the Broward County Clerk of Courts for each application filed, by cash, money order or online payment.",
            "source_name": "Broward County Clerk of Courts, felony division",
            "source_url": BROWARDFEL,
        },
    ],
    "fee_rows": [
        {
            "stage": "A defense fee measured by the result",
            "share": "Prohibited",
            "note": "Subparagraph (f)(3)(B) bars a contingent fee for a criminal defendant. The neighboring provision, (f)(3)(A), covers domestic relations matters and does not apply to a prosecution.",
            "source_name": "R. Regulating Fla. Bar 4-1.5(f)(3)(B)",
            "source_url": FLBAR4,
        },
        {
            "stage": "Filing the injunction petition",
            "share": "No fee, no bond",
            "note": "The statute prohibits a filing fee and reimburses the clerk $40 per petition, out of which the serving law enforcement agency receives a fee that may not exceed $20.",
            "source_name": "Fla. Stat. 741.30(2)(a)",
            "source_url": FL74130,
        },
        {
            "stage": "Probation and the intervention program",
            "share": "Minimum one year",
            "note": "On a finding of guilt, a withheld adjudication or a plea of nolo contendere to a crime of domestic violence, the court shall order at least a year of probation with a batterers' intervention program as a condition.",
            "source_name": "Fla. Stat. 741.281",
            "source_url": FL741281,
        },
        {
            "stage": "Statutory minimum jail on a finding of bodily harm",
            "share": "10 / 15 / 20 days",
            "note": "First, second and third or subsequent offense, rising to 15, 20 and 30 days where the offense occurred in the presence of a family or household member under sixteen.",
            "source_name": "Fla. Stat. 741.283(1)",
            "source_url": FL741283,
        },
        {
            "stage": "Maximum sentence on a first-degree misdemeanor",
            "share": "Up to one year",
            "note": "Battery is a first-degree misdemeanor unless a prior battery conviction makes it a third-degree felony, and a first-degree misdemeanor carries a definite term not exceeding one year.",
            "source_name": "Fla. Stat. 775.082(4)(a) and 784.03",
            "source_url": FL775082,
        },
        {
            "stage": "Sealing or expunging the record afterward",
            "share": "$75 plus $42",
            "note": "The Broward clerk lists the initial Florida Department of Law Enforcement charge and a statutory processing fee, with the instruction packet at sixty cents and copy and certification charges on top.",
            "source_name": "Broward County Clerk of Courts, felony division",
            "source_url": BROWARDFEL,
        },
    ],
}

PRICING["tampafamilylawattorneypros.com"] = {
    "mode": "fees",
    "fee_kind": "criminal",
    "table_head": "What Florida forbids in a family law fee, and what Hillsborough County charges at each step",
    "col_a": "The item",
    "col_b": "What the rule, statute or clerk sets",
    "anchors": [
        {
            "label": "Fee tied to securing a divorce or to the amount",
            "value": "Prohibited",
            "detail": "No fee in a domestic relations matter may be contingent on the securing of a divorce or on the amount of alimony or support, or property settlement in lieu of those.",
            "source_name": "R. Regulating Fla. Bar 4-1.5(f)(3)(A)",
            "source_url": FLBAR4,
        },
        {
            "label": "Dissolution of marriage filing fee",
            "value": "$408",
            "detail": "Charged by the Hillsborough County Clerk of Circuit Court. A counter petition is $295, and any other family law action not separately listed is $300.",
            "source_name": "Hillsborough County Clerk fees and fines",
            "source_url": HILLSFEES,
        },
        {
            "label": "Court-ordered family mediation, per person per session",
            "value": "$120 or $60",
            "detail": "The higher rate applies where combined income is above $50,000 and below $100,000, the lower where combined income is under $50,000. No fee is assessed against an indigent party.",
            "source_name": "Fla. Stat. 44.108(2)",
            "source_url": FL44108,
        },
        {
            "label": "Order requiring one party to pay the other's fees",
            "value": "Available",
            "detail": "After considering the financial resources of both parties, the court may order a reasonable amount for attorney's fees, suit money and costs, including enforcement, modification and appeals.",
            "source_name": "Fla. Stat. 61.16(1)",
            "source_url": FL6116,
        },
    ],
    "fee_rows": [
        {
            "stage": "A fee riding on the outcome",
            "share": "Prohibited on two hooks",
            "note": "The rule reaches payment contingent on the divorce being secured and payment sized by the alimony, support or property figure. The comment treats a later bonus based on results as the same prohibited arrangement.",
            "source_name": "R. Regulating Fla. Bar 4-1.5(f)(3)(A)",
            "source_url": FLBAR4,
        },
        {
            "stage": "Recovering a post-judgment support balance",
            "share": "Contingent fee allowed",
            "note": "The rule states that the provision does not preclude a contingent fee contract for recovering post-judgment balances due under support, alimony or other financial orders.",
            "source_name": "R. Regulating Fla. Bar 4-1.5(f)(3)",
            "source_url": FLBAR4,
        },
        {
            "stage": "Statutory ceiling on a chapter 61 filing fee",
            "share": "Up to $295",
            "note": "Lower than the $395 figure for general circuit civil actions, with additional statutory charges layered on top of it by the clerk.",
            "source_name": "Fla. Stat. 28.241(1)(a)1.b.",
            "source_url": FL28241,
        },
        {
            "stage": "Opening the case in Hillsborough County",
            "share": "$408 / $295 / $10",
            "note": "Dissolution of marriage, counter petition, and issuing a summons. Filing and issuing a subpoena is $7 and signing and sealing one is $2.",
            "source_name": "Hillsborough County Clerk fees and fines",
            "source_url": HILLSFEES,
        },
        {
            "stage": "Coming back after the judgment",
            "share": "$50 / $188",
            "note": "Reopening a closed family file, and a writ of garnishment used to reach wages or an account when an ordered payment is not made.",
            "source_name": "Hillsborough County Clerk fees and fines",
            "source_url": HILLSFEES,
        },
        {
            "stage": "Parent education course with minor children",
            "share": "Minimum four hours",
            "note": "Every party to a dissolution involving minor children must complete an approved course before final judgment, the petitioner within forty-five days of filing and other parties within forty-five days of service.",
            "source_name": "Fla. Stat. 61.21",
            "source_url": FL6121,
        },
    ],
}

COPY = {
    "houstonmotorcycleaccidentlawyerpros.com": "pricing-copy-houston-motorcycle.md",
    "neworleansmotorcycleaccidentlawyerpros.com": "pricing-copy-neworleans-motorcycle.md",
    "denverdivorcelawyerpros.com": "pricing-copy-denver-divorce.md",
    "fortlauderdaledomesticviolencelawyer.com": "pricing-copy-fortlauderdale-dv.md",
    "tampafamilylawattorneypros.com": "pricing-copy-tampa-familylaw.md",
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
        print("pricing block:", domain)

    for domain, fname in COPY.items():
        cp = SITES / domain / "copy.md"
        body = cp.read_text()
        # strip any previous pricing sections
        lines = body.split("\n")
        keep, skipping = [], False
        for ln in lines:
            if ln.startswith("## "):
                skipping = ln.strip() in ("## pricing_lede", "## pricing_body")
            if not skipping:
                keep.append(ln)
        body = "\n".join(keep).rstrip() + "\n\n"
        add = (ROOT / fname).read_text().strip() + "\n"
        cp.write_text(body + add)
        print("copy sections:", domain)


if __name__ == "__main__":
    main()
