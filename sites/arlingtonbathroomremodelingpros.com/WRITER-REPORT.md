# Writer report — arlingtonbathroomremodelingpros.com

## Angle

A bathroom remodel is a planned construction project, not an emergency dispatch. The copy is built on Arlington’s permit and inspection sequence for bathroom, plumbing, and electrical work, plus the practical discovery risk in a mostly pre-1990 housing stock. It sells a site visit, a measured scope, a written price before construction, concealed-condition approval, and a realistic finish date.

## Three sourced local facts

1. **Bath remodel permit rule.** Arlington’s December 2024 DIY guide identifies kitchen and bath remodels as common home changes that require a permit, and recommends licensed professional contractors for plumbing and electrical work.  
   URL: https://www.arlingtontx.gov/News-Articles/2024/December/Do-I-Need-A-Permit-A-DIY-Guide

2. **Plumbing/electrical permitting and inspection timing.** Arlington’s permitting guide lists electrical and plumbing permits, directs applicants to ArlingtonPermits.com to apply and schedule inspections, and says inspection requests after 7 a.m. move to the next business day.  
   URL: https://www.arlingtontx.gov/files/assets/city/v/1/code-compliance/documents/get-involved-code-compliance/do-i-need-a-permit.pdf

3. **Older housing stock.** Arlington Economic Development Corporation’s July 2024 single-family housing profile reports a 1984 median year built and says more than 65% of the city’s housing stock predates 1990, using 2023 Tarrant Appraisal District data.  
   URL: https://arlingtontxedc.com/assets/main/singlefamilyhousingprofile_final.pdf

Neighborhood names were taken from the City’s Heart of Arlington Neighborhood Action Plan: https://www.arlingtontx.gov/files/assets/city/v/2/strategic-initiatives/documents/neighborhood-plans/heart-of-arlington-neighborhoods-plan.pdf

## Shared-template leak

The shared `template/index.html` hard-codes the steps-band heading **“Three steps, one phone call”** and the lead **“There is nothing to fill in and nothing to buy. The call is the whole process.”** This is wrong for a planned bathroom remodel: the call merely schedules the on-site measurement and scope review; it is not the entire process. `template/build.py` also hard-codes contact-page wording that says the number is “answered by a ... technician,” despite the pre-tenant status and no identified provider. The hard-coded “No forms / No obligation” stat strip is generic lead-generation copy rather than a remodeling-project message, although it is not an emergency-trade claim.

## Not sourced

No claim was made that Arlington homes generally contain cast iron drains or galvanized supply piping. The copy treats those as conditions to verify when access is opened, not as a citywide fact. No business, price, license, review count, or timeline guarantee was claimed.
