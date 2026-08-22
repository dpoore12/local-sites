from pathlib import Path
from PIL import Image

root = Path('/home/user/workspace')
out = Path('/home/user/workspace/local-sites/sites/bocaratongaragedoorrepairpros.com/assets')
out.mkdir(parents=True, exist_ok=True)
items = [
    ('bocaratongaragedoorrepairpros-hero.png', 'hero.jpg', 1800),
    ('bocaratongaragedoorrepairpros-work-1.png', 'work-1.jpg', 900),
    ('bocaratongaragedoorrepairpros-work-2.png', 'work-2.jpg', 900),
    ('bocaratongaragedoorrepairpros-work-3.png', 'work-3.jpg', 900),
]
for source, destination, width in items:
    with Image.open(root / source) as im:
        im = im.convert('RGB')
        height = round(im.height * width / im.width)
        im = im.resize((width, height), Image.Resampling.LANCZOS)
        im.save(out / destination, 'JPEG', quality=80, progressive=True, optimize=True)
        print(f'{destination}: {im.size[0]}x{im.size[1]}')
