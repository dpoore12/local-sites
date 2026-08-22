from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
root=Path('/home/user/workspace')
out=Path('/home/user/workspace/local-sites/sites/cincinnatipersonalinjurylawyerpros.com/assets')
out.mkdir(parents=True, exist_ok=True)
images=[
 ('cincinnatipersonalinjurylawyerpros-hero.png','hero.jpg',(1800,1200)),
 ('cincinnatipersonalinjurylawyerpros-work-1.png','work-1.jpg',(900,600)),
 ('cincinnatipersonalinjurylawyerpros-work-2.png','work-2.jpg',(900,600)),
 ('cincinnatipersonalinjurylawyerpros-work-3.png','work-3.jpg',(900,600)),
]
for src, dest, size in images:
    im=Image.open(root/src).convert('RGB')
    if src.endswith('work-1.png'):
        # Defocus generated handwriting and paperwork so no text is carried into the site asset.
        im.paste(im.crop((390,275,940,500)).filter(ImageFilter.GaussianBlur(13)), (390,275))
        im.paste(im.crop((360,475,1080,740)).filter(ImageFilter.GaussianBlur(15)), (360,475))
    im=ImageOps.fit(im,size,method=Image.Resampling.LANCZOS,centering=(0.5,0.5))
    im.save(out/dest,'JPEG',quality=80,progressive=True,optimize=True)
    print(dest, im.size)
