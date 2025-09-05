from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def fleshlight_cleaning_liquid(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"{name}の❤️最爱"
    try:
        frame.draw_text(
            (13, 1039, 430, 1189),
            text,
            fill=(255, 255, 255),
            max_fontsize=100,
            min_fontsize=20,
            lines_align="center",
            font_families=["FZKaTong-M19S"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((920, 920))
        return frame.copy().paste(img, (290, 20), alpha=True, below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "fleshlight_cleaning_liquid",
    fleshlight_cleaning_liquid,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["清洗液"],
    date_created=datetime(2025, 3, 13),
    date_modified=datetime(2025, 9, 5),
)
