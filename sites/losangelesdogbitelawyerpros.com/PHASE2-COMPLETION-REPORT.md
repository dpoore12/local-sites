# losangelesdogbitelawyerpros.com — Phase 2 complete

## Build
`cd /home/user/workspace/local-sites && python3 template/build.py --check-only losangelesdogbitelawyerpros.com`

```
[PASS] losangelesdogbitelawyerpros.com -- home 1744 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           448 words  /about/
          1436 words  /child-dog-bite-claim/
           572 words  /contact/
          1526 words  /dog-bite-injury-claim/
          1536 words  /dog-bite-insurance-claim/
          1909 words  /
          1537 words  /landlord-dog-bite-liability/
          1744 words  /pricing/
           597 words  /services/
exit=0
```

Zero 15-word runs shared with any of the other 82 sites (verified with an independent
15-gram scan across all `sites/*/copy.md`).

## Service slugs
- dog-bite-injury-claim
- child-dog-bite-claim
- landlord-dog-bite-liability
- dog-bite-insurance-claim

## Strongest verified local facts (differentiators vs. Sacramento / San Diego)
1. LA Animal Services dangerous-animal hearing: notice served at least 10 days ahead,
   Hearing Examiner appointed by the General Manager, recording/transcript taken,
   Department bears the burden by a preponderance, hearsay may supplement but cannot
   alone support a finding; remedies include enclosure design, keep-out locations on the
   property, and removal of dogs from the premises.
   https://www.laanimalservices.com/sites/default/files/documents/PERMITS/LAMC53.18.5.pdf
   and https://codelibrary.amlegal.com/codes/los_angeles/latest/lamc/0-0-0-137100
2. LAMC 53.06.2 six-foot leash / on-premises restraint, paired with Evidence Code 669
   negligence-per-se presumption.
   https://codelibrary.amlegal.com/codes/los_angeles/latest/lamc/0-0-0-136443
   https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=669.&lawCode=EVID
3. LA County Veterinary Public Health: 10-day minimum quarantine for biting dogs/cats,
   30 days for livestock, most quarantines served in the animal's own home; a bite report
   does not mean the animal was deemed dangerous.
   http://publichealth.lacounty.gov/vet/biteintro.htm
   http://publichealth.lacounty.gov/vet/rabiesmanual/quarantines.htm

Core statutes used exactly as written: Civil Code 3342 (incl. (b)-(d) police/military dog
exemption), CCP 335.1 two years, CCP 352(b) public-entity tolling exception,
Gov Code 911.2 / 945.6, Civil Code 1714, B&P 6147.

## Files changed
- `sites/losangelesdogbitelawyerpros.com/copy.md` (rewritten phase-2 blocks)
- `sites/losangelesdogbitelawyerpros.com/site.json` (`"phase": 1` → `2`, nothing else)

Helper artifacts left in place: `RESEARCH-NOTES.md`, `apply_copy.py`.
