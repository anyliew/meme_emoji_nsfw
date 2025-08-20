from datetime import datetime
from pathlib import Path
import random

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_nsfw_verina_holdsign(images, texts: list[str], args):
    text = texts[0]
    
    # 定义每张图片的坐标和字体大小
    image_configs = [
        {
            "image": "0.png",
            "coords": (351, 612, 639, 918),
            "max_fontsize": 120,
            "min_fontsize": 30
        },
        {
            "image": "1.png",
            "coords": (124, 711, 404, 1021),
            "max_fontsize": 100,
            "min_fontsize": 25
        },
        {
            "image": "2.png",
            "coords": (216, 632, 528, 961),
            "max_fontsize": 110,
            "min_fontsize": 28
        },
        {
            "image": "3.png",
            "coords": (297, 490, 658, 841),
            "max_fontsize": 90,
            "min_fontsize": 20
        }
    ]
    
    # 获取index参数，如果没有提供则随机选择一张图片
    if args and hasattr(args, 'index'):
        img_index = getattr(args, 'index', 0)
        img_index = max(0, min(img_index, len(image_configs) - 1))
    else:
        # 随机选择一张图片
        img_index = random.randint(0, len(image_configs) - 1)
    
    config = image_configs[img_index]
    frame = BuildImage.open(img_dir / config["image"])
    
    try:
        frame.draw_text(
            config["coords"],
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=config["max_fontsize"],
            min_fontsize=config["min_fontsize"],
            lines_align="center",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_png()


add_meme(
    "kurogames_nsfw_verina_holdsign",
    kurogames_nsfw_verina_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["不可以色色"],
    keywords=["瑟瑟维里奈举牌"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 5, 17),
    date_modified=datetime(2025, 5, 17),
)