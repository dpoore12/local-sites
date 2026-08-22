from pathlib import Path
changes = {
 'sites/charlotteguttercleaningpros.com/copy.md': [
  (' A basic screen can be lifted by wind or clogged where the roof valley dumps directly into it.', ''),
  ('and leave the structure far enough from the foundation that it does not turn one corner of the house into the rain garden.', 'and drain away from the foundation.')
 ],
 'sites/overlandparkgaragedoorrepairpros.com/copy.md': [
  ('thousands of wind-and-unwind cycles', 'many wind-and-unwind cycles'),
  ('A door that comes down and immediately returns upward is usually reacting to its safety system, not deciding on its own that it needs a new motor.', 'When a closing door returns straight to open, its safety circuit is responding to an obstacle signal or mechanical drag, not automatically calling for an opener replacement.')
 ]
}
for name, replacements in changes.items():
 p=Path(name); t=p.read_text()
 for old,new in replacements:
  if old not in t: raise SystemExit(f'missing expected text in {name}: {old[:80]}')
  t=t.replace(old,new,1)
 p.write_text(t)
 print('updated', name)
