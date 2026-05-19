from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator.tags import MemeTags
from meme_generator import add_meme
from meme_generator.utils import save_gif

img_dir = Path(__file__).parent / "images"

def nailoong_do(images: list[BuildImage], texts, args):
    frames: list[IMG] = []
    
    positions = [
        (194, 87), (193, 86), (198, 78), (201, 73), (201, 71),
        (196, 68), (186, 76), (178, 89), (172, 103), (163, 113),
        (162, 113), (175, 107), (184, 98), (194, 90), (199, 84),
        (203, 80), (203, 80), (199, 82), (194, 91), (187, 102),
        (177, 119), (164, 140), (152, 142), (161, 141), (174, 132),
        (189, 121), (203, 109), (210, 101), (208, 93), (204, 90),
        (203, 90), (191, 97), (181, 105), (171, 118), (156, 135),
        (153, 138), (167, 134), (180, 122), (196, 113), (205, 107),
        (211, 96), (207, 93), (205, 92), (200, 98), (191, 107),
        (185, 124), (175, 136), (157, 140), (157, 140), (171, 136),
        (186, 128), (197, 117)
    ]

    sizes = [(76, 76)] * 52

    for i in range(52):
        frame_num = (i % 52) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        user_head = images[0].resize(sizes[i]).convert("RGBA")
        user_head = user_head.rotate(-45, center=(user_head.width/2, user_head.height/2))
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        new_frame.paste(frame, (0, 0), alpha=True)
        frames.append(new_frame.image)

    return save_gif(frames, 0.02)

add_meme(
    "nailoong_do",
    nailoong_do,
    min_images=1,
    max_images=1,
    keywords=["奶龙撅"],
    date_created=datetime(2026, 5, 19),
    date_modified=datetime(2026, 5, 19),
)