# Writer Report — tucsonemergencyplumberpros.com

## Build status

PASS — `python3 template/build.py tucsonemergencyplumberpros.com` passed, and the full `python3 template/build.py` run passed the cross-site 15-word duplication check.

- Home: 2,492 visible words
- About: 374 visible words
- Contact: 513 visible words
- Four required phase-1 JPEGs: present (`hero.jpg` at 1800px wide; three `work-*.jpg` files at 900px wide)

The expected placeholder-phone warning remains unchanged.

## Three sourced local facts

1. **Older housing and desert ground.** The University of Arizona MAP Dashboard says the largest share of Tucson homes was built from 1970 to 1979. University of Arizona Cooperative Extension describes caliche as a calcium-carbonate-cemented desert-soil layer that can form at or below the surface.
   - https://mapazdashboard.arizona.edu/housing-age
   - https://extension.arizona.edu/publication/managing-caliche-home-yard

2. **Permit threshold for a bigger repair.** The City of Tucson distinguishes minor accessible leak/stopper work from a repair that replaces or reroutes pipes, valves, or fixtures; the latter requires a permit, particularly when the work is in walls, below floors, or behind access panels.
   - https://www.tucsonaz.gov/Departments/Planning-Development-Services/Permits/Tucson-Permit-Exemptions

3. **Documented flooding history.** Pima County records six presidential-declared flood disasters in the Tucson area between July 1977 and July 1993: October 1977, March 1978, December 1978, October 1983, July 1990, and January 1993.
   - https://www.pima.gov/1618/Historical-Flood-Events

## Angle used

Led with **caliche, slab-on-grade access and the possibility of under-slab water paths** rather than hard-water maintenance. The copy treats a wet location as evidence to investigate, not the promised pipe location. It also makes the City permit threshold part of how a quick accessible emergency repair differs from a pipe reroute or under-floor/in-wall replacement. Six named Tucson neighborhoods are Armory Park, Barrio Viejo, Sam Hughes, Menlo Park, El Presidio, and Rita Ranch.

## Shared-template finding

The template still contains a trade-neutral but operationally misleading hardcoded band: **“Three steps, one phone call”** and **“The call is the whole process.”** For emergency plumbing, the work is necessarily an on-site inspection and repair, so that phrase can imply the phone call itself is the product. It cannot be corrected from this site’s `copy.md` because it is in `template/index.html`. The hardcoded “No forms / No obligation” stat strip is also generic chrome rather than service-specific copy, but it does not leak another trade’s wording.

## Anything not sourced

I did not state a Tucson-wide percentage of slab-on-grade homes or make a claim about pipe material by neighborhood because I did not obtain a source strong enough to support either. The site uses caliche as a documented local ground condition and describes the repair consequences conditionally, after on-site inspection.
