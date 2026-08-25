#!/usr/bin/env python3
"""Phase 2 copy edit for sandiegowrongfulterminationlaw.com."""
import io, json, re, pathlib

SITE = pathlib.Path("sites/sandiegowrongfulterminationlaw.com")
COPY = SITE / "copy.md"

REPLACE = {}
APPEND = {}

REPLACE["symptom_1_title"] = "I was fired and cannot tell whether the law was broken"

REPLACE["symptom_1"] = """A discharge can be cold, abrupt, and still lawful. What changes the answer is the reason behind it, and whether an unlawful reason can be shown from the record instead of a feeling. Write the sequence down today: last review, last complaint, last leave request, the words used in the meeting, and who was in the room. Then check the filing clock."""

REPLACE["symptom_2_title"] = "The discharge landed right after I reported something"

REPLACE["symptom_2"] = """Close timing is evidence, not proof. Fix the two dates that matter, the day the report went out and the day the adverse action arrived, then save the report itself and every reply to it. Labor Code 1102.5 reaches a disclosure made on reasonable cause even when reporting formed part of the job. Identify who knew before the decision."""

REPLACE["symptom_3_title"] = "The reason tracked a protected characteristic or a leave request"

REPLACE["symptom_3"] = """Discrimination cases are built on comparison and on the employer's own paperwork. Record who else did the same thing without consequence, when a disability, pregnancy, age, or national origin came up, and how the company answered an accommodation or leave request. Keep the request in writing. A request that was never answered is itself a problem worth naming."""

REPLACE["symptom_4_title"] = "A severance agreement or release has arrived with a short deadline"

REPLACE["symptom_4"] = """The deadline printed on the paper is rarely the only one that applies. California requires notice of the right to consult counsel and at least five business days for a separation agreement, and workers 40 and older get more time under federal law. Read what the release covers, what continues after signing, and what the money is buying."""

REPLACE["crosslink_head"] = "Facing a different workplace problem?"

APPEND["services_summary"] = """Four separate jobs hide behind one search for help with a San Diego firing. A wrongful termination claim asks whether the stated reason was one the law took away from the employer. A retaliation claim traces protected reporting to the adverse act that followed it. A discrimination claim names a category and produces a comparator. A severance review reads a release before a signature makes it permanent. Guessing wrong costs real money here, because the administrative intake, the right-to-sue letter, the federal charge window, and the deadline stamped on a release all run on separate calendars that do not wait for each other."""

# ---------------------------------------------------------------- service 1
APPEND["svc_wrongful_termination_lawyer_lede"] = """A discharge that felt arbitrary may be perfectly lawful. One delivered politely, with a tidy file behind it, may not be. The dividing line is the employer's real reason, plus two filing clocks that start the day your badge stops working."""

APPEND["svc_wrongful_termination_lawyer_body"] = """### What separates a harsh discharge from an unlawful one

California starts at Labor Code 2922: an employment having no specified term "may be terminated at the will of either party on notice to the other," and a specified term means longer than one month ([Labor Code 2922](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=LAB&division=3.&title=&part=&chapter=2.&article=4.)). Fairness is not the test. The test is whether the reason falls inside a category the Legislature or the courts removed from an employer's discretion.

Four families of reason do that work. Discrimination on a protected ground. Punishment for protected reporting or for taking protected leave. Discharge for refusing to break the law. And an enforceable promise, written or implied, that limited the employer's freedom to end the job.

The refusal branch comes from Tameny v. Atlantic Richfield Co., where the state Supreme Court held that an employer's authority over a worker "does not include the right to demand that the employee commit a criminal act to further its interests," and that someone fired for saying no may sue in tort rather than only for breach of contract ([Tameny](https://law.justia.com/cases/california/supreme-court/3d/27/167.html)). Tort framing is why the case matters: it opened the door to damages a contract theory never reached.

### The two clocks that quietly decide the case

Most losses here are calendar losses, not merits losses. California's Civil Rights Department, renamed from the Department of Fair Employment and Housing effective July 1, 2022 under SB 189 ([CRD](https://calcivilrights.ca.gov/deptnamechange/)), handles the administrative stage that a state discrimination or retaliation suit has to pass through. Its instruction is blunt: in employment matters an intake form must reach the agency within three years of the date you were last harmed ([CRD complaint process](https://calcivilrights.ca.gov/complaintprocess/)). Government Code 12960(e)(5) sets the same three years, and 12960(b) provides that the later verified complaint relates back to the intake form ([Gov. Code 12960](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=12960.&lawCode=GOV)).

Clock two is shorter and less forgiving. A right-to-sue notice states that the action must be brought within one year from the date of that notice, under Government Code 12965(c)(1)(C). Where the agency has not sued within 150 days, it tells you the notice will issue on request; if nobody asks, it issues when the investigation ends and no later than a year after filing ([Gov. Code 12965](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=12965.&lawCode=GOV)). Asking for an immediate notice, which many people do to move faster, converts an unhurried three-year window into a hard twelve months.

### Where the federal calendar undercuts the state one

Federal claims obey their own arithmetic. The EEOC puts the baseline charge deadline at 180 calendar days, extended to 300 where a state agency enforces a law barring the same discrimination, which California plainly does ([EEOC](https://www.eeoc.gov/time-limits-filing-charge)). Once a federal notice of right to sue arrives, suit must follow within 90 days ([EEOC](https://www.eeoc.gov/filing-lawsuit)). Because the two agencies operate a work-sharing arrangement, and a charge lodged with one is treated as filed with the other, people assume the generous state window protects everything ([CRD employment](https://calcivilrights.ca.gov/employment/)). It does nothing for a Title VII claim that drifted past day 300.

### Your first week, ordered so the proof survives

Ask for the personnel file in writing before anything is filed. Labor Code 1198.5 gives an employer 30 calendar days from a written request, extendable to 35 by written agreement, and a former employee one request per year, with a $750 penalty for noncompliance. Subdivision (n) is the trap: the inspection right stops while a lawsuit relating to a personnel matter is pending in the trial court ([Labor Code 1198.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=1198.5)). File first and you may have shut your own document window.

Check the final check next. Discharge means all wages, accrued vacation included, are due immediately; someone who quits with 72 hours' notice is paid at quitting, and without notice within 72 hours ([DLSE](https://www.dir.ca.gov/dlse/faq_paydays.htm)). Late pay triggers the waiting time penalty of a daily rate for each day unpaid, capped at 30 calendar days including weekends, though a good faith dispute defeats it. The agency's own worked example takes $2,500 a month to a daily rate of $115.38 and a maximum of $3,461.54 ([DLSE](https://www.dir.ca.gov/dlse/FAQ_WaitingTimePenalty.htm)).

### What the employer's side is doing while you decide

Building a file backward. Expect a performance memo dated close to the discharge, a policy produced for the first time, coworker statements gathered by counsel, and an arbitration clause pulled from an onboarding packet nobody reread. None of that is unusual and none of it is fatal. It is why the sequence you write down in week one, with names and dates, carries more weight later than a summary written from memory a year on.

### Where a case like this is actually heard

For civil limited and unlimited filings, the court's own rule 1.2.2(E) folds the East and South divisions into Central at 330 West Broadway, Room 225 ([San Diego Superior Court](https://www.sdcourt.ca.gov/sdcourt/civil2/civilwheretofile)). Practical consequence: a Mira Mesa or Hillcrest job and a Chula Vista job land in the same downtown clerk's office, and the employer pays $435 to make its first appearance there.

### How the fee side works under California's rule

In a FEHA action the court may award the prevailing party fees, costs and expert witness fees, while a winning employer recovers only if the case was frivolous, unreasonable, or groundless. Labor Code 1102.5(j) similarly lets a court award fees to a successful whistleblower plaintiff. That asymmetry, not a percentage, is what makes this work economically possible for someone with no income."""

# ---------------------------------------------------------------- service 2
APPEND["svc_retaliation_claim_lawyer_lede"] = """Retaliation claims are won on chronology. A report on Tuesday, a first written warning on Thursday, and a discharge three weeks later is a pattern the law has a specific answer for, including one that shifts the burden onto the employer."""

APPEND["svc_retaliation_claim_lawyer_body"] = """### Protected activity is a defined list, not a grievance

Labor Code 1102.5 covers a disclosure to a government or law enforcement agency, to a person with authority over the employee, or to another employee with authority to investigate. What it asks is that the worker had reasonable cause to believe the information showed a violation of a statute, or noncompliance with a local, state, or federal rule. The statute then adds the clause that decides many cases: the protection applies "regardless of whether disclosing the information is part of the employee's job duties" ([Labor Code 1102.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=1102.5)).

That clause was written for exactly the workers this county is full of. Quality and compliance staff at Kearny Mesa manufacturers, nurses and technicians at hospital campuses, lab auditors near La Jolla, and program staff on federally funded contracts all raise problems as part of the job description. An employer arguing that reporting was merely your assignment is arguing against the text.

### The sentence that flips the burden

Section 1102.6 is short and unusually valuable. Once an employee shows by a preponderance of the evidence that protected activity was a contributing factor in the action taken, the employer carries the burden of demonstrating by clear and convincing evidence that it would have acted the same way for legitimate, independent reasons ([Labor Code 1102.6](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=1102.6)). Contributing factor is a low bar. Clear and convincing is a high one, and it lands on the party that wrote the file.

Remedies follow the same logic. Section 1102.5(f)(1) allows a civil penalty of up to $10,000 per employee for each violation, payable to the person retaliated against, and subdivision (j) permits a fee award to a plaintiff who wins.

### The 90-day presumption after a pay complaint

Complaints about wages have their own provision. Under Labor Code 98.6, an employee discharged, demoted, suspended, or otherwise punished for conduct protected by the wage statutes is entitled to reinstatement and reimbursement for lost wages and work benefits. Subdivision (b)(1) adds a rebuttable presumption in the employee's favor when the prohibited action lands within 90 days of the protected activity, and subdivision (b)(3) authorizes a civil penalty of up to $10,000 per employee ([Labor Code 98.6](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=98.6)). So the gap between complaint and consequence is worth measuring in days.

### The local ordinance that creates its own protected complaint

This city runs a wage floor of its own. The Earned Sick Leave and Minimum Wage Ordinance, San Diego Municipal Code chapter 3, article 9, division 1, took effect July 11, 2016 and set the citywide rate at $17.75 an hour effective January 1, 2026, up from $17.25. Sick leave accrues at one hour for every 30 hours worked inside city boundaries, accrual may be capped at 80 hours, and an employer may instead award 40 hours at the start of a benefit year while limiting use to 40 hours ([City of San Diego](https://www.sandiego.gov/labor-and-wage/minimum-wage/earned-sick-leave)). Coverage reaches anyone performing at least two hours of work in a week within those boundaries ([official notice](https://www.sandiego.gov/sites/default/files/2025-01/mwo-notice-english.pdf)).

Two features matter for retaliation. The ordinance protects safe time for domestic violence, sexual assault, or stalking, and it prohibits retaliation, with enforcement available either in court or through the Labor Commissioner. A downtown restaurant worker punished for using accrued hours is not making a vague fairness argument; the complaint has a municipal code section behind it.

### First week: paper before argument

Stop litigating with human resources and start dating the record. Save the report or complaint in its original form, the reply, the calendar invitation for the meeting where things changed, and every message showing who was copied. Ask for the personnel file in writing under Labor Code 1198.5, which runs on that 30-day clock. Payroll records carry a tighter 21 calendar day deadline with the same $750 penalty attached ([DLSE](https://www.dir.ca.gov/dlse/faq_paydays.htm)). Leave confidential patient, client, research, and security material where it is.

### The mistake that lets a manager rewrite the story

Waiting. Every week that passes lets the employer add documentation, collect statements, and shape an explanation that reads as though it predated the report. Meanwhile deadlines quietly narrow: a FEHA retaliation theory needs the CRD intake within three years of the last harm, and a right-to-sue notice then leaves one year to file suit ([CRD](https://calcivilrights.ca.gov/complaintprocess/)).

### Agency routes, PAGA, and who pays the fees

Some retaliation claims travel through the Labor Commissioner rather than a civil rights agency, and some ride alongside a representative action. A claim under the Private Attorneys General Act begins with a notice submitted through the state's PAGA portal, which charges $75 for a new claim notice, and the court complaint must be filed with the agency within 10 days of the lawsuit ([DIR](https://www.dir.ca.gov/Private-Attorneys-General-Act/Private-Attorneys-General-Act.html)). Those civil penalties are shared with the state and are not a substitute for individual damages. On fees, a successful whistleblower plaintiff may recover them under 1102.5(j), and a minimum wage or overtime claim carries a one-way fee right in the employee's favor."""

# ---------------------------------------------------------------- service 3
APPEND["svc_workplace_discrimination_lawyer_lede"] = """Discrimination cases are not won by describing a hostile manager. They are won by naming a protected category, producing someone comparable who was treated better, and showing what the employer wrote down before it decided."""

APPEND["svc_workplace_discrimination_lawyer_body"] = """### Name the category, then find the comparison

The Fair Employment and Housing Act lists the grounds precisely. Government Code 12940(a) covers race, religious creed, color, national origin, ancestry, physical disability, mental disability, reproductive health decisionmaking, medical condition, genetic information, marital status, sex, gender, gender identity, gender expression, age, sexual orientation, and veteran or military status ([Gov. Code 12940](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=GOV&division=3.&title=2.&part=2.8.&chapter=6.&article=1.)).

Once the category is named, the useful evidence becomes comparative. Who else violated the same rule and kept their job. Which employee got the schedule that was refused to you. When a supervisor learned about the diagnosis, the pregnancy, or the religious observance, and what changed in the following pay period.

### Five employees is the number that decides coverage

Thresholds under this statute are low by national standards. California family and medical leave protections attach to any employer of five or more people, under Government Code 12945.2(b)(4)(A). Harassment prevention training obligations begin at five employees under 12950.1(a)(1), and the conviction history restrictions in 12952(a) use the same count. A twelve-person North Park practice or a small Hillcrest retailer is squarely inside the statute, which surprises both sides regularly.

### Disability: failing the interactive process is its own violation

Three separate provisions do three separate jobs. Section 12940(m)(1) makes it unlawful to fail to make reasonable accommodation for a known physical or mental disability, subject to an undue hardship defense defined in 12926(u). Section 12940(m)(2) bars retaliation against a person for requesting accommodation, "regardless of whether the request was granted." Section 12940(n) makes it unlawful to fail to engage in a "timely, good faith, interactive process" to determine effective accommodations.

Read those together and the practical rule is that silence is actionable. An employer that receives a doctor's note, never replies, and then terminates for attendance has a problem independent of whether the accommodation itself was owed. Keep the request, the note, and the dates of every meeting that followed.

### California leave and federal leave are not the same leave

Confusing the two statutes is a common and expensive error. State leave under 12945.2(a) requires more than 12 months of service, at least 1,250 hours in the previous 12 months, and provides up to 12 workweeks in a 12-month period, at an employer with five or more employees. Federal leave requires an employer with 50 or more employees for at least 20 workweeks, a worksite with 50 employees within 75 miles, 1,250 hours, and 12 months of employment ([U.S. Department of Labor](https://www.dol.gov/agencies/whd/fmla/faq)).

Pregnancy adds a third layer. Employers of five or more must provide up to four months of pregnancy disability leave, which the agency calculates as 17 1/3 weeks of the employee's normal schedule, and state family leave for bonding is counted separately from it ([CRD](https://calcivilrights.ca.gov/employment/)). So an employee who used four months of disability leave has not necessarily used any bonding leave at all, and a termination premised on the opposite assumption is worth examining closely.

### The intake form is the deadline, not the lawsuit

Before most FEHA suits, the state requires an administrative filing, and the agency says an intake form must arrive within three years of the date you were last harmed ([CRD complaint process](https://calcivilrights.ca.gov/complaintprocess/)). The verified complaint relates back to that intake under Government Code 12960(b). The agency generally has up to a year to investigate, and a right-to-sue notice then leaves one year to file in court under 12965(c)(1)(C).

Federal coverage runs on a 300-day charge window in this state, and the two agencies dual-file each other's charges under a work-sharing agreement ([CRD employment](https://calcivilrights.ca.gov/employment/)). Dual filing is convenient and misleading in equal measure, because it does not lengthen the federal window or excuse a missed 90-day deadline after a federal notice ([EEOC](https://www.eeoc.gov/filing-lawsuit)).

### Documents that decide these cases

Request the personnel file in writing early. The employer owes production within 30 calendar days, or 35 by written agreement, a former employee may make one request a year, and $750 attaches to a refusal, with the right suspended once a related lawsuit is pending ([Labor Code 1198.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=1198.5)). Add the handbook version in force at the time, the accommodation correspondence, schedules showing who covered which shift, and the names of anyone who heard the remark you remember.

### Fee shifting is the reason these cases get brought

Under Government Code 12965(c)(6) a court may award the prevailing party reasonable fees, costs and expert witness fees, and a prevailing employer may recover only where the action was frivolous, unreasonable, or groundless when brought or continued. That one-sided structure is deliberate. It lets a worker earning the city wage floor pursue a claim against an employer with a standing defense budget."""

# ---------------------------------------------------------------- service 4
APPEND["svc_severance_agreement_review_lede"] = """Severance paperwork is a purchase offer, and what it is buying is your right to sue. The number on page one is easy to read. The clauses that decide whether the number is fair sit four pages later."""

APPEND["svc_severance_agreement_review_body"] = """### What the document is actually buying

A severance agreement trades money for a release. Everything else in it, confidentiality, non-disparagement, cooperation, return of property, references, and a no-rehire clause, adjusts the price of that trade. So the first question is never whether the amount sounds generous. It is what claims disappear when the signature lands, and what obligations you carry afterward.

Read the release definition itself with care. A broad release typically reaches wage claims, discrimination and retaliation claims, contract claims, and anything arising from the employment relationship. Carve-outs, where they exist, usually cover unemployment benefits, workers' compensation, vested retirement money, and the right to speak to a government agency.

### Five business days is a statute, not a favor

California puts a floor under the review period. Government Code 12964.5(b)(4) requires an employer offering a separation agreement to notify the employee of the right to consult an attorney and to provide a reasonable period of not less than five business days to do so. Signing sooner is allowed only where the decision is knowing and voluntary and was not induced by pressure, misrepresentation, or a threat to pull the offer ([Gov. Code 12964.5](https://law.justia.com/codes/california/code-gov/title-2/division-3/part-2-8/chapter-7/article-1/section-12964-5/)).

The same section limits what the paper may contain. Subdivision (b)(1)(A) makes it an unlawful employment practice to include a provision prohibiting disclosure of information about unlawful acts in the workplace. A confidentiality clause drafted to bury a harassment complaint is not merely aggressive; it collides with the statute.

### Workers 40 and older get two more clocks

Federal age discrimination law adds structure that many employers copy imperfectly. A waiver of age claims must give at least 21 days to consider the agreement, or at least 45 days where the waiver is requested as part of an exit incentive or termination program offered to a group. It must allow at least 7 days after signing to revoke, and it does not become effective until that revocation period expires ([29 U.S.C. 626(f)](https://www.law.cornell.edu/uscode/text/29/626)).

Group layoffs carry a disclosure obligation that rewards close reading. The employer must provide the job titles and ages of everyone eligible or selected for the program, plus the ages of those in the same classification or unit who were not selected. That table is sometimes the clearest evidence available about how a reduction in force actually chose people. If the waiver's validity is disputed, the burden of proving it was knowing and voluntary sits with the employer.

### The paragraph in capital letters

Somewhere near the release you will find a block quoting Civil Code 1542, which provides that a general release does not extend to claims the releasing party does not know or suspect to exist and that would have materially affected the settlement ([Civil Code 1542](https://law.justia.com/codes/california/code-civ/division-3/part-1/title-4/chapter-6/section-1542/)). The quoted text is followed by an express waiver of it. That waiver is the point of the paragraph: it sweeps in claims nobody has identified yet, including ones you might discover after the file is produced.

### The deadlines the agreement does not mention

An employer's response date has nothing to do with the state's administrative calendar. A discrimination or retaliation claim still requires an intake filing with the Civil Rights Department within three years of the last harm, and a right-to-sue notice starts a separate one-year window for suit ([CRD complaint process](https://calcivilrights.ca.gov/complaintprocess/)). Federal claims run on the 300-day charge deadline and, after a notice of right to sue, 90 days ([EEOC](https://www.eeoc.gov/time-limits-filing-charge)).

Two Labor Code deadlines belong on the same page of your notes. Final wages including accrued vacation are due immediately on discharge, with the waiting time penalty running up to 30 calendar days of pay when they are late ([DLSE](https://www.dir.ca.gov/dlse/FAQ_WaitingTimePenalty.htm)). And a written request for the personnel file obliges production within 30 calendar days, extendable to 35 by agreement, carrying a $750 penalty, with the inspection right suspended once a related suit is filed ([Labor Code 1198.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=1198.5)). Asking before signing is far easier than asking afterward.

### What the money is measured against

Severance is not owed by statute, so its value is judged against the claims being released. Where a departure follows a protected complaint, a leave request, or a wage dispute, the release is worth more to the employer than a routine restructuring release, and the analysis should reflect that. A separation from a defense contractor or hospital system may also involve clearance paperwork, an ethics file, restricted stock, commission plan terms, or a bonus that vested days after the last day of work.

### How this work is paid for

Review of a severance document is ordinarily hourly rather than contingent, because nothing is being recovered yet. California requires a written contract where the total expense to the client is reasonably foreseeable to exceed $1,000, so most engagements of this kind are documented in writing from the start. If the review turns up a viable claim, the fee structure can change, and FEHA's fee-shifting provision then becomes part of the calculation instead of a percentage cap that does not exist."""


def main():
    text = COPY.read_text()
    parts = re.split(r"(?m)^## (.+)$", text)
    head = parts[0]
    blocks = []
    for i in range(1, len(parts), 2):
        blocks.append([parts[i].strip(), parts[i + 1]])
    keys = {k for k, _ in blocks}
    for k, v in REPLACE.items():
        if k not in keys:
            raise SystemExit(f"missing block {k}")
        for b in blocks:
            if b[0] == k:
                b[1] = "\n" + v.strip() + "\n\n"
    for k, v in APPEND.items():
        if k in keys:
            for b in blocks:
                if b[0] == k:
                    b[1] = "\n" + v.strip() + "\n\n"
        else:
            blocks.append([k, "\n" + v.strip() + "\n\n"])
    out = head + "".join(f"## {k}\n{v}" for k, v in blocks)
    COPY.write_text(out)

    sj = SITE / "site.json"
    raw = sj.read_text()
    if '"phase": 1,' in raw:
        sj.write_text(raw.replace('"phase": 1,', '"phase": 2,', 1))
    assert json.loads(sj.read_text())["phase"] == 2
    print("done")


if __name__ == "__main__":
    main()
