# 导入必要的模块
from datetime import datetime
from pathlib import Path

from PIL.Image import Image as IMG  # 导入PIL的Image类并重命名为IMG
from pil_utils import BuildImage  # 导入用于构建和操作图像的BuildImage类

from meme_generator import add_meme  # 导入添加meme模板的函数
from meme_generator.utils import save_gif  # 导入保存GIF的函数

# 获取当前文件所在目录的路径，并拼接images子目录路径
img_dir = Path(__file__).parent / "images"

def big_eagle_cute_girl(images: list[BuildImage], texts, args):

    user_head = images[0].resize((70, 70)).convert("RGBA") #.circle()
    
    # 初始化帧列表，用于存储每一帧图像
    frames: list[IMG] = []

    positions = [
        (193, 20), (187, 20), (182, 20), (182, 20), (182, 20), # 1-5
        (186, 17), (195, 35), (215, 68), (227, 65), (227, 40), # 6-10
        (219, 41), (223, 48), (229, 44), (227, 33), (211, 28), # 11-15
        (200, 28), (185, 26), (176, 20), (167, 22), (160, 24), # 16-20
        (160, 31), (162, 28), (161, 28), (154, 30), (154, 30), # 21-25
        (155, 30), (155, 30), (154, 23), (157, 23), (152, 22), # 26-30
        (148, 28), (136, 28), (123, 19), (116, 38), (116, 40), # 31-35
        (116, 40), (103, 44), (102, 46), (100, 48), (99, 43), # 36-40
        (99, 33), (98, 35), (111, 39), (116, 27), (103, 19), # 41-45
        (98, 33), (101, 30), (113, 29), (122, 29), (135, 43), # 46-50
        (143, 45), # 51
    ]

    # 处理所有帧
    for i in range(51):
        frame_num = (i % 51) + 1
        frame = BuildImage.open(img_dir / f"{frame_num}.png").convert("RGBA")
        
        # 创建一个新的图像，首先粘贴用户头像作为背景
        new_frame = BuildImage.new("RGBA", frame.size)
        new_frame.paste(user_head, positions[i], alpha=True)
        
        # 然后将原始帧内容粘贴到上面
        new_frame.paste(frame, (0, 0), alpha=True)
        
        frames.append(new_frame.image)

    # 将所有帧保存为GIF，帧间隔为0.14秒
    return save_gif(frames, 0.14)

add_meme(
    "big_eagle_cute_girl",  # 模板的唯一标识符
    big_eagle_cute_girl,  # 处理函数
    min_images=1,  # 需要的最小图片数量
    max_images=1,  # 需要的最大图片数量
    keywords=["大屌萌妹","大吊萌妹","大雕萌妹"],  # 搜索关键词
    date_created=datetime(2025, 9, 9),  # 创建日期
    date_modified=datetime(2025, 9, 9),  # 修改日期
)