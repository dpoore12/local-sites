from PIL import Image
from pathlib import Path
root=Path('/home/user/workspace')
items=[
 ('annarborgaragedoorrepairpros-hero.png','hero.jpg',1800),
 ('annarborgaragedoorrepairpros-work-1.png','work-1.jpg',900),
 ('annarborgaragedoorrepairpros-work-2.png','work-2.jpg',900),
 ('annarborgaragedoorrepairpros-work-3.png','work-3.jpg',900),
]
outdir=Path('/home/user/workspace/local-sites/sites/annarborgaragedoorrepairpros.com/assets')
for src, dest, width in items:
 p=root/src
 im=Image.open(p).convert('RGB')
 height=round(im.height*width/im.width)
 im=im.resize((width,height),Image.Resampling.LANCZOS)
 out=outdir/dest
 im.save(out,'JPEG',quality=80,progressive=True,optimize=True)
 print(f'{out.name}: {im.width}x{im.height}, {out.stat().st_size} bytes')
 p.unlink()
