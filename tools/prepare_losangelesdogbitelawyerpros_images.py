from PIL import Image
from pathlib import Path
src = Path('/home/user/workspace')
dst = Path('/home/user/workspace/local-sites/sites/losangelesdogbitelawyerpros.com/assets')
dst.mkdir(parents=True, exist_ok=True)
items = [
    ('losangelesdogbitelawyerpros-hero.png', 'hero.jpg', 1800),
    ('losangelesdogbitelawyerpros-work-1.png', 'work-1.jpg', 900),
    ('losangelesdogbitelawyerpros-work-2.png', 'work-2.jpg', 900),
    ('losangelesdogbitelawyerpros-work-3.png', 'work-3.jpg', 900),
]
for original, out, width in items:
    with Image.open(src / original) as im:
        im = im.convert('RGB')
        h = round(im.height * width / im.width)
        im = im.resize((width, h), Image.Resampling.LANCZOS)
        im.save(dst / out, 'JPEG', quality=80, progressive=True, optimize=True)
        print(out, im.size)
