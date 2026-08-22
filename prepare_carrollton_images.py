from pathlib import Path
from PIL import Image
root=Path('/home/user/workspace')
out=Path('/home/user/workspace/local-sites/sites/carrolltongaragedoorrepairexperts.com/assets')
items=[
 ('carrolltongaragedoorrepairexperts-hero.png','hero.jpg',1800),
 ('carrolltongaragedoorrepairexperts-work-1.png','work-1.jpg',900),
 ('carrolltongaragedoorrepairexperts-work-2.png','work-2.jpg',900),
 ('carrolltongaragedoorrepairexperts-work-3.png','work-3.jpg',900),
]
out.mkdir(parents=True,exist_ok=True)
for src,name,width in items:
    im=Image.open(root/src).convert('RGB')
    h=round(im.height*width/im.width)
    im.resize((width,h),Image.Resampling.LANCZOS).save(out/name,'JPEG',quality=80,progressive=True,optimize=True)
    print(name, width, h)
