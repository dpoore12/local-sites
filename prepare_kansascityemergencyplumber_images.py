from pathlib import Path
from PIL import Image

src = Path('/home/user/workspace')
dst = Path('/home/user/workspace/local-sites/sites/kansascityemergencyplumber.com/assets')
dst.mkdir(parents=True, exist_ok=True)
items = [
    ('kansascityemergencyplumber-hero.png', 'hero.jpg', 1800),
    ('kansascityemergencyplumber-work-1.png', 'work-1.jpg', 900),
    ('kansascityemergencyplumber-work-2.png', 'work-2.jpg', 900),
    ('kansascityemergencyplumber-work-3.png', 'work-3.jpg', 900),
]
for input_name, output_name, width in items:
    with Image.open(src / input_name) as im:
        im = im.convert('RGB')
        height = round(im.height * width / im.width)
        im.resize((width, height), Image.Resampling.LANCZOS).save(
            dst / output_name, 'JPEG', quality=80, progressive=True, optimize=True
        )
    (src / input_name).unlink()
    print(f'{output_name}: {width}x{height}')
