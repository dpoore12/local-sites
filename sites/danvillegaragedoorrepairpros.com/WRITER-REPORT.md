## From WRITER-FINDINGS.md

# Danville Garage Door Repair Pros — writer findings

Completed 2026-08-22.

## Sourced local facts

1. **Hillside access:** Town planning materials say nearly 50 percent of Danville lies on hillsides, including Las Trampas Ridge and the hills paralleling Sycamore Valley. This informed the copy’s discussion of steep driveways, access, safe vehicle placement, and securing a disabled door.
   - https://www.danville.ca.gov/DocumentCenter/View/10792/Appendix-B---Constraints

2. **Wildfire/ember exposure:** The Town identifies its undeveloped, grassland, and oak-woodland edges as Very High Fire Hazard Severity Zone areas. CAL FIRE says gaps and missing gasketing around garage doors can provide ember entry paths. This informed the weather-seal inspection angle without implying that every repair is a code project.
   - https://www.danville.ca.gov/DocumentCenter/View/10792/Appendix-B---Constraints
   - https://www.fire.ca.gov/home-hardening

3. **Exterior design review:** Danville’s Design Review Board evaluates site design and architecture under Town standards; its official submittal requirements identify exterior doors, materials, and colors. This informed the distinction between a repair and an address-specific larger exterior project.
   - https://www.danville.ca.gov/276/Design-Review-Board
   - https://www.danville.ca.gov/DocumentCenter/View/1724/Design-Review-Board-Requirements

## Neighborhoods used

Greenbrook; Sycamore; Danville South; Diablo Highlands; Tassajara Ranch; Shadow Creek.

## Photo assets

- `assets/hero.jpg` — 1800×1200, progressive JPEG, quality 80
- `assets/work-1.jpg` — 900×600, progressive JPEG, quality 80
- `assets/work-2.jpg` — 900×600, progressive JPEG, quality 80
- `assets/work-3.jpg` — 900×600, progressive JPEG, quality 80

## Validation

Targeted command:

```text
python3 template/build.py danvillegaragedoorrepairpros.com
[PASS] danvillegaragedoorrepairpros.com -- home 2845 words, 4 symptoms, 3 local Q&As, 3 sourced facts
           324 words  /about/
           539 words  /contact/
          2845 words  /
```

The required full build was also run. It reports `[PASS]` for `danvillegaragedoorrepairpros.com`; the command exits nonzero because unrelated concurrent drafts (Dallas window replacement, Eden Prairie garage doors, Fort Worth garage doors, Harrisburg car accident lawyer, and Oxnard car accident lawyer) have their own incomplete/shared-copy errors.
