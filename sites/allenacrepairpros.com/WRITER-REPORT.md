# Writer Report — allenacrepairpros.com

## Result

- **Assigned-site build:** PASS — `python3 template/build.py allenacrepairpros.com`
- **Home page:** 2,591 visible words
- **About page:** 306 visible words
- **Contact page:** 516 visible words
- **Assets:** `hero.jpg` at 1800×1200 and three 900×600 progressive JPEG work photos.

## Angle used

North Texas summer load is the organizing idea: a cooling problem becomes especially disruptive during sustained heat, so the copy stays focused on on-site diagnosis, airflow/electrical/drainage checks, and a defined repair price before work starts. The local layer is Allen's newer housing stock and the City of Allen contractor/permit process. I did not use California energy-code or Central Valley heat language.

## Three sourced local facts

1. **Housing vintage:** A Census-data housing profile lists Allen’s median year built as **2002**. It supports treating much of the market as post-1990/post-2000 housing, while still requiring an on-site check of each system’s actual installation and replacement history.  
   URL: https://www.point2homes.com/US/Neighborhood/TX/Allen-Demographics.html

2. **Local contractor process:** The City of Allen says **all contractors must register annually**; the city registration form expressly lists **HVAC/Mechanical** as a contractor classification. This is why the site distinguishes ordinary repair from a full equipment change that may need the local process addressed.  
   URLs: https://www.cityofallen.org/1939/Contractor-and-Commercial-Services  
   https://cms3.revize.com/revize/allentx/Images/Documents/Departments/Community%20Development/Building%20and%20Permitting/Contractor%20and%20Commercial%20Services/Registration/Contractor%20Registration%20Form.pdf

3. **Documented heat event:** National Weather Service Dallas/Fort Worth data records **55 days at or above 100°F in 2023**, including **21 consecutive 100-degree days from July 24 through August 13**. That supports the site’s emphasis on addressing reduced cooling rather than masking it during a prolonged hot spell.  
   URLs: https://www.weather.gov/fwd/danncon10  
   https://www.weather.gov/fwd/d100data

## Template finding

No garage-door wording leaked into this site. The shared `template/index.html` does contain hard-coded process wording that does not fit the brief’s requirement to sell dispatched, on-site work rather than a phone interaction:

> “Three steps, one phone call”
>
> “There is nothing to fill in and nothing to buy. The call is the whole process.”

That wording is not trade-specific, but it is misleading for AC repair because the actual diagnostic and repair happen at the home. It is locked shared-template text and has not been edited.

## Anything not sourced

No unsupported local claim was retained. The permit-related copy deliberately does **not** say that every AC repair requires a permit; the city sources establish annual contractor registration, the HVAC/mechanical classification, and the city process. The housing-vintage fact uses a live Census-data housing profile rather than a Census API endpoint because the current public API response required a key.

## Full-build status

The final full `python3 template/build.py` run cross-checked this site successfully but exited non-zero because of unrelated sites shared in the repository at the time of the run:

- `charlotteguttercleaningpros.com`: `symptom_3` and `symptom_4` exceed the 360-word maximum.
- `overlandparkgaragedoorrepairpros.com`: an unverifiable “thousands of” claim and three duplicate 15-word runs with the Boca Raton garage-door site.

The full command output is saved at `/home/user/workspace/allenacrepairpros-full-build.log`.
