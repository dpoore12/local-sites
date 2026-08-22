from pathlib import Path
from PIL import Image

root = Path("/home/user/workspace")
site_assets = root / "local-sites" / "sites" / "friscogaragedoorrepairexperts.com" / "assets"
site_assets.mkdir(parents=True, exist_ok=True)

jobs = [
    ("friscogaragedoorrepairexperts-hero.png", "hero.jpg", 1800),
    ("friscogaragedoorrepairexperts-work-1.png", "work-1.jpg", 900),
    ("friscogaragedoorrepairexperts-work-2.png", "work-2.jpg", 900),
    ("friscogaragedoorrepairexperts-work-3.png", "work-3.jpg", 900),
]

for src_name, dest_name, width in jobs:
    with Image.open(root / src_name) as image:
        image = image.convert("RGB")
        height = round(image.height * width / image.width)
        image = image.resize((width, height), Image.Resampling.LANCZOS)
        image.save(site_assets / dest_name, "JPEG", quality=80, progressive=True, optimize=True)
        print(f"{dest_name}: {image.width}x{image.height}")
