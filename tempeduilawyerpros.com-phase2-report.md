# Phase 2 report — tempeduilawyerpros.com (DUI Lawyer, Tempe, Maricopa County, AZ)

Sources fetched 2026-08-25 with `pplx_sdk.content.fetch`. Primary sources only: azleg.gov (Arizona
Revised Statutes), City of Tempe, Maricopa County, Arizona Governor's Office of Highway Safety,
Arizona Board of Regents policy manual.

## Build result

```
[PASS] tempeduilawyerpros.com -- home 1743 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           409 words  /about/
           590 words  /contact/
          1452 words  /dui-breath-test-defense/
          1468 words  /dui-license-suspension/
          1542 words  /felony-dui-defense/
          1542 words  /first-offense-dui-defense/
          1850 words  /
          1743 words  /pricing/
           577 words  /services/
```
exit 0. `"phase": 2` set; nothing else changed in site.json.

Service slugs written (from site.json, used exactly): `first-offense-dui-defense`,
`dui-license-suspension`, `dui-breath-test-defense`, `felony-dui-defense`.

## CORRECTION TO THE BRIEF

**The brief's "fifteen-day window to request a hearing" is wrong for Arizona. It is thirty days.**

- A.R.S. 28-1385 (admin per se): "The request for a hearing or summary review must be received by
  the department within thirty days after the date of the notice or the order of suspension becomes
  final." The order "is effective thirty days after the date it is served," and a surrendered valid
  license yields "a temporary driving permit that is valid for thirty days."
  https://www.azleg.gov/ars/28/01385.htm
- A.R.S. 28-1321 (implied consent) uses the same thirty-day figure: "if the person requests a
  hearing in writing or online and the request is received by the department within thirty days
  after the notice is sent." https://www.azleg.gov/ars/28/01321.htm

Fifteen days is the California figure (the sibling San Jose site). The page was written on thirty.

Second brief nuance corrected on the page: on the **extreme** tiers the suspended jail days are
**not** conditioned on screening. A.R.S. 28-1382(I) suspends all but nine days (0.15–0.199) or all
but fourteen days (0.20+) only "if the person equips any motor vehicle the person operates with a
certified ignition interlock device for a period of twelve months." The screening-conditioned
suspension ("all but one day") belongs to 28-1381(I). No disagreement found between site.json and
the brief; site.json's tier/jail numbers all verified.

## Three strongest verified local facts

1. **Tempe PD DUI totals fell by more than half in two years.** GOHS ten-year per-agency table:
   Tempe PD 1,333 (2022), 754 (2023), 646 (2024); ASU PD 26 (2022), 19 (2023), 55 (2024), 2025
   preliminary. https://gohs.az.gov/sites/default/files/2025-04/Copy%20of%2010%20Year%20DUI%20Statistics%20Statewide%20(Per%20Agency).xlsx%20-%20Sheet1_0.pdf
2. **A student or employee must be released from jail for school or work after the first 24 hours.**
   A.R.S. 28-1387(C): after twenty-four consecutive hours served on a 28-1381(I) sentence (48 hours
   on a 28-1381(K) or 28-1382(D)/(E) sentence), with court confirmation of employment or student
   status, the sentence must allow the person to continue work or schooling "for not more than
   twelve hours a day nor more than six days a week" absent good cause on the record.
   https://www.azleg.gov/ars/28/01387.htm
3. **Drug-recognition evaluations in Arizona jumped 32.5% in one year, and ASU Police in Tempe has
   its own evaluators.** GOHS 2024 DECP annual report: 1,875 enforcement evaluations in 2024 vs
   1,420 in 2023; 304 certified DREs and 78 instructors across 58 agencies; five named evaluators
   listed under "AZ STATE UNIV PD, TEMPE"; Tempe PD credited with 18 evaluations.
   https://gohs.az.gov/sites/default/files/2025-01/2024%20AZGOHS%20DECP%20Annual%20Report.pdf

## Everything else verified, by page

### /first-offense-dui-defense/
- A.R.S. 28-1381: https://www.azleg.gov/ars/28/01381.htm — "not less than ten consecutive days in
  jail," no probation/suspension "unless the entire sentence is served"; judge "may suspend all but
  one day" on completing court-ordered alcohol or other drug screening, education, evidence-based
  psychotherapy or treatment; order to show cause if the program is not completed and the person is
  not on probation; class 1 misdemeanor; impairment "to the slightest degree"; 0.08 within two
  hours; second within 84 months = not less than 90 days, 30 consecutive, and suspension of all but
  30 days.
- A.R.S. 28-1387(B): screening ordered from a DHS-approved facility, the US Department of Veterans
  Affairs, or a probation department; the person pays costs unless the court waives after
  considering ability to pay; facility reports completion. 28-1387(C): work/school release above.
  https://www.azleg.gov/ars/28/01387.htm
- A.R.S. 28-3319(D)(1)(a), (F), (H), (E): interlock twelve months after a 28-1381 conviction; the
  period begins when screening/education/treatment is complete and the person is otherwise eligible
  to reinstate; deferment of the remainder starting six months after installation for a 28-1381(I)
  sentence with a sixteen-hour alcohol education program, a maintained device, no two attempts to
  start at 0.08 or more, and no injury/property-damage crash at the time of the offense; deferment
  permanent unless a new DUI arrest occurs; monthly screening substituted for a documented medical
  condition. https://www.azleg.gov/ars/28/03319.htm
- Tempe city prosecutor: criminal division prosecutes misdemeanors occurring in Tempe including DUI;
  felonies occurring in Tempe prosecuted by the Maricopa County Attorney's Office.
  https://www.tempe.gov/government/city-attorney-s-office/prosecutor-s-office
- Tempe Municipal Court criminal/criminal-traffic page: arraignment date comes from the citation, a
  court summons, or the release order; three pleas; no witnesses or testimony at arraignment; the
  arraignment judge will not dismiss; diversion information given at arraignment; "In no instance
  will sentences exceed the maximum levels of $2,500 fine plus surcharges and/or 6 months in jail
  and/or 5 years probation."
  https://www.tempe.gov/government/city-court/criminal-and-criminal-traffic
- A.R.S. 13-905: set-aside on fulfilling conditions and discharge; no filing fee; excluded
  categories are a dangerous offense, a registration offense, a sexual-motivation finding, and a
  felony with a victim under fifteen — **DUI is not excluded**; penalties lifted "except those
  imposed by" ADOT under the listed licensing sections; a set-aside conviction may still be used as
  a prior and pleaded in later prosecutions; DPS annotates and "may not redact or remove any part of
  the person's record." https://www.azleg.gov/ars/13/00905.htm
- A.R.S. 13-911: sealing waiting periods — 3 years class 1 misdemeanor, 2 years class 2/3
  misdemeanor, 5 years class 4/5/6 felony, 10 years class 2/3 felony; all fines, fees and
  restitution must be paid; sealed records may still be "used to enhance the sentence pursuant to
  sections 28-1381 and 28-1382" and must be disclosed for a job "involving the commercial or private
  operation of a motor vehicle." https://www.azleg.gov/ars/13/00911.htm

### /dui-license-suspension/
- A.R.S. 28-1385: order effective thirty days after service; thirty-day temporary permit; not less
  than ninety consecutive days on a 0.08 result; 28-1385(I) thirty consecutive days suspended plus
  at least sixty additional restricted days under 28-144 where there was no death or serious
  physical injury, no 28-1381/1382/1383 conviction within 84 months of the commission date, and
  proof of completed screening (department may impose 90 days if screening is skipped); five-issue
  hearing scope; 28-1385(J)/(K) special ignition interlock restricted license issued in lieu of
  suspension, and once issued "the person waives any right to an administrative hearing."
  https://www.azleg.gov/ars/28/01385.htm
- A.R.S. 28-1321: refusal suspension twelve months, two years for a second or subsequent refusal
  within 84 months; failure to expressly agree or to complete the test "is deemed a refusal";
  reinstatement only on completing screening; four-issue refusal hearing scope; timely request stays
  the suspension but the surrendered license is not returned; 28-1321(P) interlock restricted
  license after screening, not available on a second refusal within 84 months.
  https://www.azleg.gov/ars/28/01321.htm
- Felony exposure for driving while suspended: A.R.S. 28-1383(A)(1).
  https://www.azleg.gov/ars/28/01383.htm
- MVD fees and SR-22: https://azdot.gov/mvd/services/dui-suspension/suspension-revocation (figures
  quoted only on the pricing page, which was already sourced).

### /dui-breath-test-defense/
- A.R.S. 28-1323(A)(1)–(5) and (B), (C), (D): approved quantitative device; permitted operator;
  duplicate tests within 0.02 or twenty minutes' observation; approved operational checklist; proper
  operating condition, with periodic maintenance records as prima facie evidence and calibration
  checks "with a standard alcohol concentration solution bracketing each person's duplicate breath
  test" named as one qualifying record; "The records are public records"; compliance with (A) is the
  only requirement for admission; inability to obtain manufacturer's schematics and software does
  not affect admissibility. https://www.azleg.gov/ars/28/01323.htm
- A.R.S. 28-1388(A), (C), (D), (E): who may draw blood and that the drawer's qualifications and
  method "are not foundational prerequisites"; reasonable opportunity to arrange an independent
  test, and failure to obtain one does not exclude the state's result; refusal evidence admissible
  as an issue of fact; a portion of a sample taken for any reason must be provided to an officer on
  request where there is probable cause. https://www.azleg.gov/ars/28/01388.htm
- A.R.S. 28-1382: 0.15–0.199 and 0.20+ tiers; thirty and forty-five consecutive days; all but nine
  or all but fourteen suspendable only with twelve months of interlock.
  https://www.azleg.gov/ars/28/01382.htm
- Interlock length by tier: twelve months for 28-1382(A)(1), eighteen months for 28-1382(A)(2),
  twenty-four months for a repeat 0.20+ or for 28-1383(A)(1),(2),(4),(5) and (A)(3)(b).
  https://www.azleg.gov/ars/28/03319.htm
- DRE figures: GOHS 2024 DECP annual report (URL above).

### /felony-dui-defense/
- A.R.S. 28-1383: five aggravating routes (suspended/canceled/revoked/refused or restricted
  privilege; third or subsequent violation within 84 months; passenger under fifteen; violation
  while interlock is required; wrong-way driving, with the statutory definition excluding a median
  crossing or a crash ending facing backward); subsection (O) — paragraphs 1, 2, 4, 5 are a class 4
  felony, paragraph 3 is a class 6 felony; subsection (D) four months in prison before any release
  eligibility, (E) eight months with three or more priors; child-passenger counts carry at least the
  28-1381 or 28-1382 minimum; probation incarceration caps of four months/one year and eight
  months/two years; county aggravated DUI jail program alternative; revocation with no new license
  within one year; traffic survival school; screening from an approved facility; (J) $250 assessment,
  fine not less than $750, and $1,500 + $1,500 assessments.
  https://www.azleg.gov/ars/28/01383.htm
- A.R.S. 28-1387(A): allegation of a prior conviction or another pending DUI charge allowed if filed
  twenty or more days before trial, later filing permitted if the state provides its information;
  enhancement irrespective of the order of offenses within the 84-month window; a juvenile
  delinquency adjudication counts as a conviction. https://www.azleg.gov/ars/28/01387.htm
- Maricopa County criminal process: initial appearance (charges, appointed counsel, next date,
  release conditions or bond); preliminary hearing before a court commissioner on probable cause;
  an indictment removes the preliminary hearing and goes to arraignment in Superior Court where a
  not guilty plea is entered; initial pretrial conference; sentencing about one month after a plea.
  https://www.maricopa.gov/5610/Criminal-Process
- ABOR Policy 5-308: students "may be accountable to both civil and criminal authorities and to the
  university"; university action may proceed "before, during, or after other proceedings";
  "off-campus conduct may also be subject to educational interventions or discipline"; F.15 covers
  violations of laws governing alcohol; F.17 covers off-campus conduct a reasonable person would
  believe presents a risk to health, safety or security; sanctions include expulsion (ineligible to
  attend ASU, NAU or U of A), suspension, probation, and an administrative hold that "may preclude
  the student from registering, from receiving transcripts, or from graduating."
  https://public.powerdms.com/ABOR/documents/1491970

### Fee rule (all four pages, paraphrased differently on each)
- Ariz. R. Sup. Ct. 42, ER 1.5(d)(2): no contingent fee for representing a defendant in a criminal
  case; ER 1.5(b): scope and basis or rate of the fee in writing.
  https://tools.dev.azbar.org/RulesofProfessionalConduct/ViewRule.aspx?id=25 (pricing page citation,
  carried over from the earlier pricing research; the service pages describe the rule without a
  duplicate URL).

## Could not verify, written around

- **Any ASU-specific disciplinary process or sanction for a DUI arrest.** ASU's own code page
  (https://eoss.asu.edu/dos/srr/codeofconduct) points to the ABOR policy and states no alcohol or
  off-campus specifics, so the page cites the Regents policy language only.
- **Immigration or visa consequences for an international student.** No primary federal or ASU
  source with usable language was located, so the felony page says only that immigration exposure is
  not resolved in the criminal courtroom and that counsel practicing immigration law is needed. No
  outcome, statute or percentage is claimed.
- **Named GOHS holiday task force periods.** The FFY 2024 Project Directors Manual does list them
  (Halloween October 28–31 2023, St. Patrick's Day March 16–17 2024, Cinco de Mayo May 3–5 2024,
  Memorial Day May 24–27 2024, Independence Day July 4–6 2024, Labor Day August 30–September 2 2024,
  and five separate December windows), and the GOHS mandate that overtime-grant agencies join the
  statewide impaired driving task force, but the dates are fiscal-year specific and would read as
  stale, so the pages use the DRE enforcement figures and the per-agency arrest counts instead.
  https://gohs.az.gov/sites/default/files/2024-06/2024%20Project%20Directors%20Manual_0.pdf
- **Tempe Municipal Court and Maricopa County jail per-diem, screening program prices, interlock
  monthly cost.** Vendor- and county-set, no primary schedule found; no figure published.
- **Whether Maricopa County operates an aggravated DUI jail program** under 28-1383(N). The page
  describes the statutory option as available "in counties running" such a program rather than
  asserting one exists here.

## Note on the symptom mapping

`site.json` `symptoms` and `symptom_service` map symptom 2 to `dui-license-suspension`, but the
phase 1 copy had symptom 2 written about the extreme/super extreme tiers. Symptom 2 and its title
were rewritten to the license-suspension notice so the teaser matches the page it links to; the
0.15/0.20 tier material now lives in depth on the breath test page. site.json was treated as the
authority throughout.
