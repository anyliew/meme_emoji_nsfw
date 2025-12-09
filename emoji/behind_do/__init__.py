# 导入必要的库和模块
from datetime import datetime  # 用于处理日期时间
from pathlib import Path  # 用于处理文件路径

# 从meme_generator模块导入必要功能
from meme_generator import add_meme  # 用于注册表情包
from meme_generator.utils import save_gif  # 用于保存GIF动图

# 导入图像处理相关模块
from PIL.Image import Image as IMG  # PIL的Image类型别名
from pil_utils import BuildImage  # 图像构建工具

# 定义图像目录：获取当前文件所在目录的父级目录下的"images"文件夹路径
img_dir = Path(__file__).parent / "images"


# 定义核心的表情包生成函数
def behind_do(images: list[BuildImage], texts, args):
    """
    生成表情包的主函数
    
    参数:
    - images: 用户上传的图片列表，至少需要2张图片
    - texts: 文本参数（本函数未使用）
    - args: 其他参数（本函数未使用）
    
    返回值: 生成的GIF动图
    """
    
    # 定义三个帧中"自己"头像的位置坐标（左上角坐标）
    self_locs = [(72, 5), (72, 5), (71, 2), (70, 3), (66, 5), (66, 5), (66, 5), (61, 7), (61, 7), (69, 5)]
    
    # 定义三个帧中"对方"头像的位置坐标（左上角坐标）
    user_locs = [(174, 91), (174, 91), (173, 86), (171, 87), (170, 85), (170, 85), (167, 82), (170, 85), (170, 85), (172, 88)]
    
    # 处理第一张图片作为"自己"的头像
    self_head = (
        images[0]  # 取第一张图片
        .convert("RGBA")  # 转换为RGBA格式（支持透明度）
        .resize((110, 110), keep_ratio=True)  # 调整大小为122x122，保持宽高比
        .circle()  # 裁剪为圆形
        .rotate(15)  # 顺时针旋转15度
    )
    
    # 处理第二张图片作为"对方/用户"的头像
    user_head = (
        images[1]  # 取第二张图片
        .convert("RGBA")  # 转换为RGBA格式
        .resize((116, 116), keep_ratio=True)  # 调整大小为112x112，保持宽高比
        .circle()  # 裁剪为圆形
        .rotate(0)  # 顺时针旋转90度
    )
    
    # 初始化存储GIF帧的列表
    frames: list[IMG] = []
    
    # 循环处理3个背景帧（对应3张背景图片）
    for i in range(10):
        # 加载背景图片：从images目录加载0.png、1.png、2.png
        frame = BuildImage.open(img_dir / f"{i}.png")
        
        # 如果需要将头像置于背景下方，则需要修改粘贴顺序
        # 先粘贴要位于底层的头像（如果需要位于最底层）
        # 这里假设用户头像应该位于底层，自己的头像在上层
        
        # 首先粘贴用户头像作为底层
        frame.paste(user_head, user_locs[i], alpha=True, below=True)
        
        # 然后粘贴自己的头像在上层
        frame.paste(self_head, self_locs[i], alpha=True)
        
        # 将处理完的帧添加到列表中
        frames.append(frame.image)  # frame.image获取底层的PIL Image对象
    
    # 将所有帧保存为GIF并返回
    # 参数：帧列表，每帧持续时间0.07秒（即20帧/秒）
    return save_gif(frames, 0.07)


# 向表情包生成器注册这个表情包
add_meme(
    "behind_do",  # 表情包的调用命令/名称
    behind_do,  # 对应的处理函数
    min_images=2,  # 最少需要的图片数量
    max_images=2,  # 最多接受的图片数量（这里固定需要2张）
    keywords=["后撅"],  # 搜索关键词
    date_created=datetime(2025, 12, 6),  # 创建日期
    date_modified=datetime(2025, 12, 6),  # 修改日期
)