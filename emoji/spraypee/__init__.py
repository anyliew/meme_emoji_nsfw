from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def spraypee(images: list[BuildImage], texts, args):
    user_head = images[0].resize((185, 185)).circle().convert("RGBA")

    frames: list[IMG] = []

    for i in range(30):
        frame_num = i + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")

        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, (425, 261), alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)

        frames.append(new_frame.image)

    return save_gif(frames, 0.04)

add_meme(
    "spraypee",
    spraypee,
    min_images=1,
    max_images=1,
    keywords=["滋你"],
    date_created=datetime(2026, 4, 17),
    date_modified=datetime(2026, 4, 17),
)