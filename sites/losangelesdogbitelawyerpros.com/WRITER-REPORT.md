# Writer Report — losangelesdogbitelawyerpros.com

**Status:** PASS

- Individual build: `python3 template/build.py losangelesdogbitelawyerpros.com` — passed.
- Full cross-site build: `python3 template/build.py` — passed with no duplicate-copy error for this site.
- Home-page visible word count: **2,684**.
- About-page visible word count: 422.
- Contact-page visible word count: 545.
- Expected warning retained: placeholder 213 phone number.

## Angle used

This site is built around the Los Angeles split between City restraint rules and County public-health / dangerous-dog processes. The copy explains that a rabies/bite report, a separate dangerous-animal report, and a civil injury claim have different functions. It deliberately avoids the landlord-liability angle assigned to Sacramento and the quarantine-centered angle assigned to San Diego.

## Three sourced local facts

1. **City restraint rule.** Los Angeles Municipal Code section 53.06.2 requires a dog that is off the keeper’s premises to be controlled by a competent person and restrained by a substantial leash or chain no longer than six feet, subject to its dog exercise/training-area exception. This is used as location-specific context for City incidents, not as an automatic liability conclusion. Source: [Los Angeles Municipal Code §53.06.2](https://codelibrary.amlegal.com/codes/los_angeles/latest/lamc/0-0-0-136443).
2. **County dangerous-dog process.** Los Angeles County Animal Care and Control states that its Dangerous Dog Investigations Unit investigates reported bites and attacks; an officer may prepare a petition for an administrative hearing officer, who can impose restrictions or conditions and, in some cases, order euthanasia. This supports the distinction between public-safety enforcement and a civil claim. Source: [LA County Animal Care & Control — Protecting People](https://animalcare.lacounty.gov/protecting-people/).
3. **Documented County bite volume.** A 2016 Public Health Reports study of Los Angeles County Department of Public Health surveillance data recorded 23,103 reported dog bites from 2009–2011, representing 88% of 26,169 reported animal-to-human bites. Its scope excluded Pasadena, Long Beach, and Vernon because those cities had separate health departments and rabies-control protocols. This supports the emphasis on exact jurisdiction and reporting agency. Source: [Public Health Reports study](https://pmc.ncbi.nlm.nih.gov/articles/PMC5230840/).

## Shared-template issues / wording leaks

The generic template still includes legal-site problems that copy blocks cannot correct:

- `template/build.py` creates the contact page statement **“One number, answered by a Los Angeles attorney”** even though the site is pre-tenant, names no attorney, and cannot substantiate who answers. It also says **“A case review is arranged on the call.”** This conflicts with the site’s no-named-provider posture and with the brief’s instruction not to sell a phone conversation.
- `template/index.html` hardcodes **“Three steps, one phone call”** and **“The call is the whole process.”** Those are not trade-specific and frame the page’s value as a call rather than the evidence and legal work described in the copy.
- `template/index.html` hardcodes the generic **“No forms / No obligation”** stat band and “The work itself” caption boilerplate. It is not another trade’s wording, but it bypasses the copy-only requirement and is not tailored to a legal information/referral site.

No other cross-trade wording leak was found in the rendered Los Angeles pages.

## Items not sourced

No claim was made about a present-day, dog-only County annual total because the current County performance measure found is for **animal bites**, not dog bites. The dated dog-only volume above is explicitly identified as 2009–2011 and is not presented as a current annual count.
