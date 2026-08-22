## From research-notes-2026-08-22.md

# Harrisburg local research notes

1. Pennsylvania Insurance Department — Automobile Insurance Guide, page 3:
   limited tort preserves out-of-pocket medical and other expenses but limits
   certain damages unless an exception applies; full tort preserves unrestricted
   rights to sue a negligent party.
   https://www.pa.gov/content/dam/copapwp-pagov/en/insurance/documents/documents/auto_guide.pdf

2. Dauphin County Court of Common Pleas / civil administration:
   the Court of Common Pleas is at the Dauphin County Courthouse, 101 Market
   Street, Harrisburg; civil matters are submitted by the Prothonotary's Office
   to Civil, Family and Orphans' Court Administration for review and assignment.
   https://www.dauphincounty.gov/government/court-departments/court-of-common-pleas-judges
   https://www.dauphincounty.gov/government/court-departments/court-administration/civil-family-orphans-court-administration

3. PennDOT Crash Statistics workbook:
   sheet `Dauphin(22)`, Dauphin County Crash Statistics, lists 2,914 total
   crashes for 2024.
   https://www.pa.gov/content/dam/copapwp-pagov/en/penndot/documents/travelinpa/safety/documents/crash_statistics.xlsx

Neighborhoods used: Allison Hill, South Allison Hill, Midtown, Uptown, Shipoke,
Academy Manor. City material supports Allison Hill / South Allison Hill,
Shipoke, Midtown, Uptown, and Academy Manor references.


## From validation-2026-08-22.md

# Validation notes

## Individual build

Command:

```text
python3 template/build.py harrisburgcaraccidentlawyerpros.com
```

Result: PASS, zero errors.

```text
[PASS] harrisburgcaraccidentlawyerpros.com -- home 2785 words, 4 symptoms,
3 local Q&As, 3 sourced facts
336 words  /about/
539 words  /contact/
2785 words  /
```

## Full build

The full batch build was run after the individual validation. This Harrisburg
site passed in that batch-wide word-run check. The overall command exited
non-zero because several other writers' sites had independent incomplete-block
or shared-word-run errors; no error was attributed to
`harrisburgcaraccidentlawyerpros.com`.
