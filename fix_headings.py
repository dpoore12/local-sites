#!/usr/bin/env python3
"""Shorten over-long headings and drop trailing periods on headings.

Every replacement is a hand-written rewrite, not a truncation, so the heading
still reads as a sentence fragment a human wrote.
"""
import pathlib, sys

# domain -> (old table_head, new table_head)
TABLE_HEAD = {
 "austinwrongfuldeathlawyerpros.com": (
   "What Texas Rule 1.04 and chapter 71 govern in a Travis County death case, and what no Texas rule limits",
   "What Texas fixes in a Travis County death case, and what it does not"),
 "cincinnatipersonalinjurylawyerpros.com": (
   "What Ohio law settles in a Hamilton County injury claim, and what stays inside the signed agreement",
   "What Ohio settles, and what stays inside the signed agreement"),
 "concordpersonalinjurylawyer.com": (
   "The figures North Carolina publishes for a Cabarrus County injury claim, and the one it leaves blank",
   "The figures North Carolina publishes, and the one it leaves blank"),
 "dallaswrongfuldeathlawyerpros.com": (
   "What the Texas fee rule requires of a Dallas County death case, and what the two clerks charge to run one",
   "What the Texas fee rule requires, and what the two clerks charge"),
 "fresnowrongfuldeathlawyerpros.com": (
   "What California law settles about fees in a Fresno County death case, and what it leaves to the contract",
   "What California settles about fees, and what the contract sets"),
 "houstonmotorcycleaccidentlawyerpros.com": (
   "What Texas fixes in a Harris County motorcycle claim, and what it leaves to the written agreement",
   "What Texas fixes, and what the written agreement sets"),
 "jacksonvillewrongfuldeathlawyerpros.com": (
   "The sliding fee schedule Florida actually publishes for a Duval County death claim, tier by tier",
   "The sliding fee schedule Florida publishes, tier by tier"),
 "jonesboropersonalinjurylawyerpros.com": (
   "Published Arkansas figures behind a Craighead County injury claim, and the blank where a fee cap would be",
   "Published Arkansas figures, and the blank where a fee cap would be"),
 "longbeachpersonalinjurylawyerpros.com": (
   "What the contract has to say in a Long Beach injury claim, and what the Los Angeles courthouse collects",
   "What the contract has to say, and what the courthouse collects"),
 "losangelesdogbitelawyerpros.com": (
   "What California's fee rules set on a dog bite claim, and what the Los Angeles courthouse charges",
   "What California's fee rules set, and what the courthouse charges"),
 "modestopersonalinjurylawyerpros.com": (
   None,
   "The fee standard, the caps on other case types, and Stanislaus County filing costs"),
 "neworleansmotorcycleaccidentlawyerpros.com": (
   "What Louisiana law fixes in an Orleans Parish motorcycle claim, and what the signed agreement sets",
   "What Louisiana fixes, and what the signed agreement sets"),
 "newportbeachduilawyerpros.com": (
   "What California law and Orange County set in a Newport Beach DUI case, and what no lawyer may charge",
   "What California and Orange County set, and what no lawyer may charge"),
 "salinascaraccidentlawyer.com": (
   "What California fixes in a Monterey County injury claim, and what it leaves to the written contract",
   "What California fixes, and what the written contract sets"),
 "sandiegodogbitelawyerpros.com": (
   "What California pins down in a San Diego dog bite claim, and what it deliberately leaves to negotiation",
   "What California pins down, and what it leaves to negotiation"),
 "sandiegowrongfulterminationlaw.com": (
   "What California fixes in a San Diego wrongful termination fee, and who can be made to pay whose fees",
   "What California fixes about fees, and who can be made to pay them"),
 "tempeduilawyerpros.com": (
   "What Arizona statutes, Tempe Municipal Court and the MVD set on a Tempe DUI, and the fee no lawyer may take",
   "What the statutes, the Tempe court and the MVD each set on a DUI"),
}

# domain -> list of (old, new) for site.json service accents
ACCENTS = {
 "neworleansmotorcycleaccidentlawyerpros.com": [
   ("Fault, Visibility and Intersection Evidence", "Fault and Intersection Evidence"),
   ("Coverage Questions and Claim Options", "Coverage and Claim Options"),
 ],
}

# domain -> list of (old, new) for copy.md headings that end in a period
COPY_HEADS = {
 "denverfurnacerepairpros.com": [
   ("Choose the furnace problem that best matches what the equipment is doing.",
    "Choose the furnace problem that best matches what the equipment is doing"),
 ],
 "sacramentodogbitelawyerpros.com": [
   ("The dog owner and the building owner are not automatically the same claim.",
    "The dog owner and the building owner are not automatically the same claim"),
   ("Build the record before it becomes harder to retrieve.",
    "Build the record before it becomes harder to retrieve"),
 ],
}

changed, missed = [], []

for dom, (old, new) in TABLE_HEAD.items():
    p = pathlib.Path("sites") / dom / "site.json"
    t = p.read_text()
    if old is None:  # modesto: match on its unique opening instead
        import re
        m = re.search(r'"table_head": "([^"]+)"', t)
        old = m.group(1)
    if f'"table_head": "{old}"' not in t:
        missed.append((dom, "table_head", old[:50])); continue
    p.write_text(t.replace(f'"table_head": "{old}"', f'"table_head": "{new}"'))
    changed.append((dom, "table_head", len(new)))

for dom, pairs in ACCENTS.items():
    p = pathlib.Path("sites") / dom / "site.json"
    t = p.read_text()
    for old, new in pairs:
        if f'"{old}"' not in t:
            missed.append((dom, "accent", old)); continue
        t = t.replace(f'"{old}"', f'"{new}"')
        changed.append((dom, "accent", len(new)))
    p.write_text(t)

for dom, pairs in COPY_HEADS.items():
    p = pathlib.Path("sites") / dom / "copy.md"
    t = p.read_text()
    for old, new in pairs:
        if old not in t:
            missed.append((dom, "copy head", old[:50])); continue
        t = t.replace(old, new)
        changed.append((dom, "copy head", len(new)))
    p.write_text(t)

print(f"{len(changed)} headings rewritten")
for c in changed: print("  ", c)
if missed:
    print(f"\n{len(missed)} NOT FOUND:")
    for m in missed: print("  ", m)
    sys.exit(1)
