from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
root=Path('/home/user/workspace')
out=Path('/home/user/workspace/local-sites/sites/cincinnatipersonalinjurylawyerpros.com/assets')
out.mkdir(parents=True, exist_ok=True)
images=[
 ('cincinnatipersonalinjurylawyerpros-hero.png','hero.jpg',(1800,1200)),
 ('cincinnatipersonalinjurylawyerpros-work-1-records.png','work-1.jpg',(900,600)),
 ('cincinnatipersonalinjurylawyerpros-work-2.png','work-2.jpg',(900,600)),
 ('cincinnatipersonalinjurylawyerpros-work-3.png','work-3.jpg',(900,600)),
]
for src, dest, size in images:
    im=Image.open(root/src).convert('RGB')
    im=ImageOps.fit(im,size,method=Image.Resampling.LANCZOS,centering=(0.5,0.5))
    im.save(out/dest,'JPEG',quality=80,progressive=True,optimize=True)
    print(dest, im.size)
