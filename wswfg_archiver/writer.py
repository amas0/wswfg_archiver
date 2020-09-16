from pathlib import Path

from .download import Image


def save_image(img: Image, out_dir: Path):
    fname = f'{img.dat.isoformat()}.png'
    out_path = Path(out_dir) / fname
    with open(out_path, 'wb') as f:
        f.write(img.content)
