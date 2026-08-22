from pathlib import Path
from PIL import Image
root = Path('/home/user/workspace')
out = root / 'local-sites' / 'sites' / 'denverdivorcelawyerpros.com' / 'assets'
out.mkdir(parents=True, exist_ok=True)
files = [
    ('denverdivorcelawyerpros-hero.png', 'hero.jpg', 1800),
    ('denverdivorcelawyerpros-work-1.png', 'work-1.jpg', 900),
    ('denverdivorcelawyerpros-work-2.png', 'work-2.jpg', 900),
    ('denverdivorcelawyerpros-work-3.png', 'work-3.jpg', 900),
]
for source, dest, width in files:
    with Image.open(root / source) as im:
        im = im.convert('RGB')
        height = round(im.height * width / im.width)
        im = im.resize((width, height), Image.Resampling.LANCZOS)
        im.save(out / dest, 'JPEG', quality=80, progressive=True, optimize=True)
        print(dest, im.size)
