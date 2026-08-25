#!/usr/bin/env python3
"""Apply phase 2 blocks to tempeduilawyerpros.com copy.md."""
import json, re, pathlib

SITE = pathlib.Path("sites/tempeduilawyerpros.com")
copy_path = SITE / "copy.md"
text = copy_path.read_text()

REPL = {}

REPL["symptom_1_title"] = "It is a first arrest, and Arizona still starts at ten days"

REPL["symptom_1"] = """A first conviction under section 28-1381 begins at ten consecutive days in jail, and probation is off the table unless the whole term is served. The same subsection lets the judge suspend all but one of those days once court-ordered screening or treatment is finished. That trade, not a dismissal, is the shape of a minimum sentence. Start by finding the arraignment date printed on your paperwork."""

REPL["symptom_2_title"] = "A suspension order came with the arrest paperwork"

REPL["symptom_2"] = """That order is the motor vehicle division's, not the judge's. It takes effect on the thirtieth day after it was served, and a surrendered license buys a temporary permit good for the same span. A written or online hearing request has to reach the department inside those thirty days or the suspension becomes final without anyone reviewing it. Read the date on the notice today."""

REPL["symptom_3_title"] = "There is a breath or blood number and it looks final"

REPL["symptom_3"] = """A reading is admissible only once the state establishes five foundational facts: an approved device, a permitted operator, duplicate tests within 0.02 of each other or twenty minutes of observation, a completed operational checklist, and maintenance records showing the machine was working. Four of those live in paperwork somebody has to request. Ask while the calibration records around your test are still easy to isolate."""

REPL["symptom_4_title"] = "The charge may be aggravated DUI, which is a felony"

REPL["symptom_4"] = """Five circumstances lift a DUI out of city court: driving on a suspended, canceled, revoked or refused privilege, a third violation inside eighty-four months, a passenger under fifteen, driving while an interlock is required, or a wrong-way allegation. Felony cases arising here are filed by the county attorney and heard downtown, in months of prison rather than days of jail. Gather your driving record and every prior disposition."""

REPL["services_summary"] = """Four separate jobs hide behind one phrase in this city, and each keeps its own clock. A first misdemeanor answers to the city prosecutor and to an arraignment date printed on a citation. A suspension order answers to the motor vehicle division and expires quietly at thirty days. A breath or blood reading is a records problem assembled from operator permits and calibration logs. An aggravated count is a felony the county attorney files downtown. Treat the license notice as part of the criminal file and the deadline passes untouched. Treat a felony allegation as ordinary traffic court and the first real hearing arrives before anybody has read the driving record."""

REPL["services_pick_head"] = "Begin with the deadline sitting closest to you"

REPL["crosslink_head"] = "A different DUI problem?"

# ---------------------------------------------------------------- service 1
REPL["svc_first_offense_dui_defense_lede"] = """Ten consecutive days in jail is where a first Arizona conviction starts, and almost nobody walking out of booking near Mill Avenue has been told that. What the statute gives back, it gives back only for finishing screening."""

REPL["svc_first_offense_dui_defense_body"] = """### Ten days is the floor the statute prints

A.R.S. 28-1381(I)(1) sentences a first conviction to "not less than ten consecutive days in jail," and the same paragraph withholds probation and suspension of sentence "unless the entire sentence is served." The relief appears further down. At sentencing the judge may suspend all but one day if the person completes a court-ordered alcohol or other drug screening, education, evidence-based psychotherapy or treatment program. If that program is never finished and the person was not placed on probation, the court must issue an order to show cause on why the remaining jail term should not be served. One day served with nine held back is the realistic minimum, and it is conditional the whole way.

### A number under 0.08 settles nothing by itself

The same section reaches driving while under the influence to the slightest degree. It separately reaches an alcohol concentration of 0.08 or more within two hours of driving, where the alcohol came from drinking before or during the drive. There is also a route for a listed drug or its metabolite in the body. A complaint can carry more than one of those counts at once, each resting on different proof, and a conviction on any of them is a class 1 misdemeanor. Reading the cited paragraph numbers on the charging document is the first useful hour of work.

### Screening is ordered by law, and the cost lands on you

Under 28-1387(B) the judge shall order a convicted person to complete screening at a facility approved by the Department of Health Services, the United States Department of Veterans Affairs, or a probation department. If the judge decides more is needed, education or treatment follows under court supervision. The person pays those costs unless the court waives some or all of them after weighing ability to pay, and the facility reports back on whether the program was completed. This is also the gate on everything else, because the interlock period does not begin until the screening, education or treatment requirements are finished.

### Twelve hours a day for a student or a worker

A provision most people never hear about sits in 28-1387(C). Once someone sentenced under 28-1381(I) has served twenty-four consecutive hours, and the court has confirmation that the person is employed or is a student, the sentence must allow that employment or schooling to continue. The limit is twelve hours a day and six days a week, unless the court finds good cause otherwise and puts the finding on the record. Remaining hours are served in custody. For an undergraduate at the university mid-semester, that paragraph decides whether the term survives the sentence. Sentences under the second-offense and extreme statutes require forty-eight consecutive hours first.

### The city path, from citation to plea

The city prosecutor's criminal division handles misdemeanors occurring in Tempe, including DUI complaints, while felony matters go to the Maricopa County Attorney's Office. Your arraignment date comes from the officer's citation, a summons issued by the court, or the release order handed over at the jail. Three pleas are available there, no testimony is taken, and the judge at arraignment will not dismiss anything. The municipal court's own criminal page fixes its outer limit: "In no instance will sentences exceed the maximum levels of $2,500 fine plus surcharges and/or 6 months in jail and/or 5 years probation." Diversion alternatives exist for some offenses, and eligibility information is given at arraignment.

### Twelve months of interlock, with one route to less

Section 28-3319(D)(1)(a) requires a certified ignition interlock device for twelve months after a 28-1381 conviction, and subsection (F) starts that clock when screening, education or treatment is complete and the driver is otherwise eligible to reinstate. Subsection (H) then allows the department to defer the remainder, beginning six months after installation, for a driver sentenced under 28-1381(I) who finished an alcohol education program of at least sixteen hours, kept a functioning device on every vehicle driven, did not twice attempt to start a vehicle at 0.08 or more during the restriction, and was in no injury or property-damage crash at the time of the offense. The deferment is permanent unless a new DUI arrest lands during it. A documented medical condition substitutes monthly alcohol and drug screening for the device.

### Set aside is real; expunged is the wrong word

A.R.S. 13-905 lets a person apply after fulfilling the conditions of probation or sentence and being discharged, with no filing fee, and DUI is not among the excluded categories. The order dismisses the charge and releases the person from penalties, except those the transportation department imposes under the licensing sections it names. A conviction set aside can still be alleged as an element, used as a prior, and pleaded in a later prosecution, and the Department of Public Safety must annotate the criminal history without removing any of it. Sealing under 13-911 is a separate petition, available three years after a class 1 misdemeanor sentence is completed and all money is paid.

### The fee cannot be tied to the result

Arizona's ethical rule bars a lawyer from arranging, charging or collecting a contingent fee to defend a criminal case, so nothing about a defense fee here can be built on the verdict. The rule also requires the scope of the work and the basis of the fee to be put in writing. What moves a fee is scope: whether a test result is contested, whether records are subpoenaed, and whether the matter is tried."""

# ---------------------------------------------------------------- service 2
REPL["svc_dui_license_suspension_lede"] = """The order handed over with your other paperwork did not come from a judge. It comes from the motor vehicle division, it takes hold on the thirtieth day, and the request that stops it has to arrive before then."""

REPL["svc_dui_license_suspension_body"] = """### The document that is not from the court

Under A.R.S. 28-1385, an officer serves an order of suspension that "is effective thirty days after the date it is served." If a valid license is surrendered on the spot, the officer issues a temporary driving permit good for thirty days, which is why the loss of driving privileges often feels like it happens a month after the arrest. On a test result of 0.08 or more, the department shall suspend the license or the right to apply for not less than ninety consecutive days. Reinstatement afterward depends on completing department-ordered screening.

### Thirty days, counted from the date on the notice

The request for a hearing or a summary review must reach the department within thirty days after the date of the notice, or the order of suspension becomes final. A summary review may be asked for any time before the effective date instead of a hearing. A timely hearing request stays the suspension until the hearing happens, though a surrendered license is not handed back; the department may issue temporary permits that run no later than its final decision. If the department decides at the hearing to suspend, that suspension starts thirty days after written notice. Nothing here is automatic, and nobody sends a reminder.

### Refusing the test is a longer, separate suspension

Section 28-1321 handles refusal. A driver must be told that the license or permit will be suspended or denied for twelve months, or for two years on a second or subsequent refusal within eighty-four months, unless the driver expressly agrees to the test and completes it successfully. Failing to expressly agree, or failing to complete the test, is deemed a refusal. Reinstatement after the period runs is conditioned on completing alcohol or other drug screening. A refusal hearing is narrow: reasonable grounds, whether an arrest occurred, whether there was a refusal, and whether the person was informed of the consequences.

### The thirty-and-sixty split many drivers qualify for

Section 28-1385(I) softens the ninety days for a defined group. The department shall suspend for at least thirty consecutive days and then restrict privileges for at least sixty additional consecutive days, if three things hold true. Nobody was killed or seriously injured in the conduct that produced the case. There is no conviction under 28-1381, 28-1382 or 28-1383 within eighty-four months of the commission date, with commission dates controlling that count. And the driver gives the department satisfactory evidence of completing ordered screening. Skip the screening and the department may impose the full ninety days instead.

### What the hearing is actually deciding

Five issues define the scope on a test-result suspension: whether the officer had reasonable grounds to believe the person was driving or in actual physical control while under the influence, whether the person was arrested for one of the listed offenses, whether a test showed 0.08 or more, or 0.04 in a commercial vehicle or a vehicle for hire, or a listed drug without a valid prescription, whether the testing method used was valid and reliable, and whether the results were accurately evaluated. Two of those five are about the test itself. That is the part of a license case worth building.

### The interlock license trades the hearing away

In place of the suspension, on request, the department shall issue a special ignition interlock restricted driver license to a person who meets the same three conditions listed above. There is a price that is not money. Once that license is issued, the person waives any right to an administrative hearing contesting the action against the license under either 28-1385 or 28-1321. A driver suspended for a first refusal may also apply after completing ordered screening, must keep a functioning device for the rest of the suspension period, and cannot use that route on a second refusal inside eighty-four months.

### Losing the car here is not a small inconvenience

Households in The Lakes and around Kiwanis Park sit well away from the light rail line that runs through the campus core, and a sixty-day driving restriction reshapes commuting, custody exchanges and shift work all at once. The temptation to drive anyway is the expensive part: a DUI committed while a privilege is suspended, canceled, revoked or refused is charged as aggravated DUI, a felony, under 28-1383(A)(1). Reinstatement is also its own transaction with the department rather than the court, carrying its own fees plus proof of future financial responsibility on an SR-22 form, which the insurer prices separately.

### How fees work on the license side

Because the criminal charge and the administrative suspension travel together, a written fee agreement should say plainly which of the two it covers. Arizona's professional conduct rule flatly prohibits a contingent fee for defending a criminal case, and it requires the basis or rate of any fee to be communicated in writing. Administrative work is billed on scope as well: the request, the record, the witnesses, and whether an interlock license ends the fight early."""

# ---------------------------------------------------------------- service 3
REPL["svc_dui_breath_test_defense_lede"] = """A printed reading arrives looking like the end of the argument. Arizona treats it as admissible only after five foundational facts are established, and four of them live in documents somebody has to go request."""

REPL["svc_dui_breath_test_defense_body"] = """### Five things established before a reading counts

A.R.S. 28-1323(A) lists them. The test used a quantitative breath testing device approved by the Department of Health Services or the Department of Public Safety. The operator held a valid permit to run that device. Duplicate tests were administered with results within 0.02 alcohol concentration of each other, or an operator watched the person for twenty minutes immediately before the test. The operator followed an approved operational checklist. And the device was in proper operating condition. Subsection (B) then states that compliance with that list is the only requirement for admission, which cuts both ways.

### The duplicate rule and the twenty minutes

Two of those requirements are alternatives to each other, and that is where the paperwork gets interesting. Either the pair of readings agrees within 0.02, or an operator observed the subject for a full twenty minutes beforehand. The observation period exists because material in the mouth can affect a breath sample, so the honest question is not whether the officer wrote a time down but whether the sequence in the report and the video supports it. Operator testimony is what establishes that the checklist was followed, which makes the checklist and the timeline worth reading side by side.

### Calibration records bracket your test, and they are public

Records of periodic maintenance showing the device was working are admissible as prima facie evidence that it was working when you blew. The statute names one qualifying type: calibration checks run with a standard alcohol concentration solution bracketing the duplicate breath tests. It then says outright that those records are public records, and section 28-1327 records are admissible as well. Requesting them early is ordinary practice, not an accusation. One limit deserves stating plainly: not being able to obtain the manufacturer's schematics and software does not affect admissibility under subsection (C).

### The two-hour clause and the lines that follow it

The alcohol-count statutes measure concentration within two hours of driving or being in actual physical control, from alcohol consumed before or while driving. Section 28-1382 then draws two lines. From 0.15 to below 0.20 a first conviction carries not less than thirty consecutive days in jail. At 0.20 or more it is not less than forty-five consecutive days. The judge may suspend all but nine days in the lower band, or all but fourteen in the upper one, only if the person equips every vehicle driven with a certified ignition interlock device for twelve months. The device requirement itself runs twelve months in the lower band and eighteen months at 0.20 or above.

### Blood leaves a different trail than breath

If blood was drawn under 28-1321, only a physician, a registered nurse or another qualified person may take it, and the statute says the drawer's qualifications and the method used are not foundational prerequisites for admitting the result. A separate provision matters after a crash: when a sample is taken from someone for any reason and an officer has probable cause on a 28-1381 violation, a portion sufficient for analysis must be provided on request. You also have a right to a reasonable opportunity to arrange an independent test by a physician, nurse or other qualified person of your own choosing, though failing to get one does not exclude the state's result.

### Drug allegations run through evaluators, not only instruments

Where the claim is drugs rather than alcohol, the record often includes a drug recognition evaluation. The state's highway safety office counted 1,875 enforcement evaluations in 2024 against 1,420 in 2023, a 32.5 percent increase, with 304 certified evaluators and 78 instructors spread across 58 agencies. Its roster lists five named evaluators at the university police department in this city and credits the city police department with 18 evaluations. If the arrest involved one, there is a structured form behind the conclusion, and refusal itself is admissible as a question of fact for the trier of fact.

### Write down what only you can still remember

The record you can protect is the timeline. Note when the last drink was finished, what and when you ate, every prescription and over-the-counter medication, dental work, reflux, injuries, and how long you sat in the patrol car before anyone produced a mouthpiece. Add the roadside conditions: traffic noise on Apache Boulevard, a slanted shoulder off Rural Road, temperature, footwear, lighting. Field instructions given quickly at night are hard to reconstruct months later from memory, and video does not always capture what standing on that surface was like.

### What a records-heavy case does to a fee

The state's ethical rules do not permit a defense fee in a criminal matter to depend on the outcome, and the basis for the fee has to be set out in writing. Contesting a reading is the part that adds hours, because it means gathering maintenance and calibration records, operator permits, checklists and video, and often paying an independent analyst. That is scope, and scope is what a written agreement should describe."""

# ---------------------------------------------------------------- service 4
REPL["svc_felony_dui_defense_lede"] = """Aggravated DUI is measured in months of prison rather than days of jail, and it leaves the city courthouse entirely. Five circumstances trigger it, and three of them have nothing to do with how much anybody drank."""

REPL["svc_felony_dui_defense_body"] = """### Five circumstances, two felony classes

A.R.S. 28-1383(A) lists them. Committing a DUI while a driver license or privilege is suspended, canceled, revoked or refused, or restricted because of an earlier alcohol case. A third or subsequent violation within eighty-four months, or a violation by someone with prior convictions under the DUI sections. A violation with a person under fifteen years of age in the vehicle. A violation while the court or the department requires a certified ignition interlock device. And a violation committed while driving the wrong way on a highway, defined as movement opposing the legal flow of traffic, which excludes a median crossing and a crash that merely ends up facing backward. Subsection (O) makes the first, second, fourth and fifth a class 4 felony and the child-passenger paragraph a class 6 felony.

### Prison time before any release is possible

Subsection (D) removes eligibility for probation, pardon, commutation, suspension of sentence or release on any other basis until four months have been served in prison, for a suspended-privilege count, a wrong-way count, or a repeat count with two qualifying priors inside eighty-four months. Subsection (E) raises that to eight months where three or more priors are found. A child-passenger count carries at least the minimum incarceration the underlying 28-1381 or 28-1382 conviction would require. If someone on probation fails to comply, the court can order incarceration as a probation term, capped at four months at a time and a year total in the first group and eight months and two years in the second. In counties running an aggravated DUI jail program, that mandatory time may be served in county jail instead, without release or work privileges the person would not otherwise have.

### Priors get proved from paper, and the dates decide

Section 28-1387(A) requires the court to allow an allegation of a prior conviction or another pending DUI charge filed twenty or more days before trial, and permits a later filing if the state gives the defense a copy of the information it obtained. Any conviction may enhance another regardless of the order in which the offenses happened inside the eighty-four month window. A juvenile delinquency adjudication counts as a conviction for this purpose. So the first document to pull is a certified disposition for every prior case, because commission dates, not sentencing dates, run the count.

### Which building the case lands in

The city prosecutor's office handles misdemeanors arising here and states that felonies occurring in Tempe are prosecuted by the Maricopa County Attorney's Office. The county process starts with an initial appearance, where charges are read, counsel is appointed if needed, release conditions or a bond are set, and the next date is given. From there the case either goes to a preliminary hearing before a court commissioner, where the state presents evidence of probable cause, or to a grand jury; an indictment removes the preliminary hearing and sends the matter straight to arraignment in Superior Court, where a not guilty plea is entered. An initial pretrial conference follows, and sentencing after a plea is typically set about a month out.

### The license and the device afterward

On receiving the conviction report the department revokes the driving privilege and may not issue a new license within one year of the conviction date. Where intoxicating liquor was involved, a certified ignition interlock device is required, and section 28-3319 sets twenty-four months for the class 4 felony paragraphs and for a child-passenger count resting on the extreme statute. That period begins only once screening, education or treatment is finished and the person is otherwise eligible to reinstate. A conviction also triggers an approved traffic survival school course and screening at an approved facility.

### If the person charged is a university student

Board of Regents policy states that students may be accountable both to criminal authorities and to the university for the same conduct, and that university action may proceed before, during or after the court case. Off-campus conduct may be subject to educational intervention or discipline, and the prohibited conduct list reaches violations of laws governing alcohol as well as off-campus conduct a reasonable person would believe presents a risk to the safety of the community. Available sanctions run from a warning and conduct probation to an administrative hold that blocks registration, transcripts or graduation, to suspension and expulsion, which bar attendance at any Regents university. Anyone here on a visa needs immigration advice from counsel who practices it, because that exposure is not resolved in the criminal courtroom.

### What the record looks like years later

Sealing under A.R.S. 13-911 becomes available five years after a class 4, 5 or 6 felony sentence is completed and all fines, fees and restitution are paid. Even then, sealed case records may be used to enhance a later sentence under the DUI statutes and must be disclosed when applying for work involving the commercial or private operation of a motor vehicle. Setting a judgment aside under 13-905 dismisses the charge and lifts penalties, but expressly leaves the transportation department's licensing consequences in place.

### How a felony defense fee is structured

State rules forbid a contingent fee for representing a defendant in a criminal case, so no part of this work can be priced against the outcome, and the basis or rate has to be communicated in writing. Felony exposure moves a fee through hours rather than percentages: certified priors, grand jury or preliminary hearing coverage, laboratory and interlock records, mitigation before a mandatory prison term, and trial preparation if it goes that far."""

# apply
def replace_block(text, key, body):
    pat = re.compile(r"(^## " + re.escape(key) + r"\n\n)(.*?)(?=\n## )", re.S | re.M)
    if not pat.search(text):
        raise SystemExit("block not found: " + key)
    return pat.sub(lambda m: m.group(1) + body.strip() + "\n", text, count=1)

order_new = ["services_summary", "services_pick_head", "crosslink_head",
             "svc_first_offense_dui_defense_lede", "svc_first_offense_dui_defense_body",
             "svc_dui_license_suspension_lede", "svc_dui_license_suspension_body",
             "svc_dui_breath_test_defense_lede", "svc_dui_breath_test_defense_body",
             "svc_felony_dui_defense_lede", "svc_felony_dui_defense_body"]

for k, v in REPL.items():
    if k in order_new:
        continue
    text = replace_block(text, k, v)

# insert new blocks before ## pricing_lede
new_chunk = "".join("## %s\n\n%s\n\n" % (k, REPL[k].strip()) for k in order_new)
text = text.replace("## pricing_lede\n", new_chunk + "## pricing_lede\n", 1)

copy_path.write_text(text)

sj = json.loads((SITE / "site.json").read_text())
sj["phase"] = 2
(SITE / "site.json").write_text(json.dumps(sj, indent=2, ensure_ascii=False) + "\n")
print("done")
