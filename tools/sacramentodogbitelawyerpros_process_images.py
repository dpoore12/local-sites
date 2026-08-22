from pathlib import Path
from PIL import Image

workspace = Path("/home/user/workspace")
assets = Path("/home/user/workspace/local-sites/sites/sacramentodogbitelawyerpros.com/assets")
images = {
    "hero": (workspace / "sacramentodogbitelawyerpros-hero.png", 1800),
    "work-1": (workspace / "sacramentodogbitelawyerpros-work-1.png", 900),
    "work-2": (workspace / "sacramentodogbitelawyerpros-work-2.png", 900),
    "work-3": (workspace / "sacramentodogbitelawyerpros-work-3.png", 900),
}

for name, (source, width) in images.items():
    with Image.open(source) as im:
        im = im.convert("RGB")
        height = round(im.height * width / im.width)
        im = im.resize((width, height), Image.Resampling.LANCZOS)
        destination = assets / f"{name}.jpg"
        im.save(destination, "JPEG", quality=80, progressive=True, optimize=True)
        print(f"{destination.name}: {im.width}x{im.height}")
    source.unlink()
