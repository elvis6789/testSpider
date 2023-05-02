from moviepy.editor import *
from skimage.filters import gaussian
import numpy as np

#竖版转横版，两边模糊处理

#image = np.random.rand(100, 100)  # 一个随机生成的示例图像
#result = gaussian(image.astype(float), sigma=30)


'''
# 输入 1.mp4 和 2.mp4，返回他们拼接的成品（带叠化效果）
def diehua(file_1, file_2):
    clip_1 = ImageClip(file_1).set_duration(3)
    clip_2 = ImageClip(file_2).set_duration(3)
    # 将这两个视频分成3部分，第一部分为纯 1.mp4 的部分，第二部分为 1.mp4 和 2.mp4 叠加的部分，第三部分为纯 2.mp4 的部分
    magic_time = 0.5  # 设置叠化转场时长
    duration_video1 = clip_1.duration  # 片段1时长
    duration_video2 = clip_2.duration  # 片段2时长

    part1 = clip_1.subclip(0, duration_video1 - magic_time)  # 片段1截取
    part3 = clip_2.subclip(magic_time, duration_video2)  # 片段2截取

    part2_1 = clip_1.subclip(duration_video1 - magic_time, duration_video1)  # 片段1的最后0.5秒
    part2_2 = clip_2.subclip(0, magic_time)  # 片段2的开始0.5秒

    # 将第二部分（1.mp4和2.mp4叠加的部分）分成10份，每份时长尽量保持一致，超过10份会明显卡顿一下，未探究原因
    part2_1_1 = part2_1.subclip(0, 0.05)
    part2_1_2 = part2_1.subclip(0.05, 0.1)
    part2_1_3 = part2_1.subclip(0.10, 0.15)
    part2_1_4 = part2_1.subclip(0.15, 0.2)
    part2_1_5 = part2_1.subclip(0.2, 0.25)
    part2_1_6 = part2_1.subclip(0.25, 0.3)
    part2_1_7 = part2_1.subclip(0.3, 0.35)
    part2_1_8 = part2_1.subclip(0.35, 0.4)
    part2_1_9 = part2_1.subclip(0.4, 0.45)
    part2_1_10 = part2_1.subclip(0.45, 0.5)

    part2_2_1 = part2_2.subclip(0, 0.05)
    part2_2_2 = part2_2.subclip(0.05, 0.1)
    part2_2_3 = part2_2.subclip(0.1, 0.15)
    part2_2_4 = part2_2.subclip(0.15, 0.2)
    part2_2_5 = part2_2.subclip(0.2, 0.25)
    part2_2_6 = part2_2.subclip(0.25, 0.3)
    part2_2_7 = part2_2.subclip(0.3, 0.35)
    part2_2_8 = part2_2.subclip(0.35, 0.4)
    part2_2_9 = part2_2.subclip(0.4, 0.45)
    part2_2_10 = part2_2.subclip(0.45, 0.5)

    # 将 part2_1 和 part2_2 叠加视频合成 part2，2个部分通过控制不同时间不同透明度完成叠化效果
    # 其中第二个参数处于上面一层，通过把前面的片段放在上面一层，再逐渐降低他的不透明度（就是让前面的片段慢慢变透明），来让下面一层的后面的片段慢慢浮现出来，产生片段叠加效果
    F_part2_1 = CompositeVideoClip([part2_2_1, part2_1_1.set_opacity(0.95)])
    F_part2_2 = CompositeVideoClip([part2_2_2, part2_1_2.set_opacity(0.85)])
    F_part2_3 = CompositeVideoClip([part2_2_3, part2_1_3.set_opacity(0.75)])
    F_part2_4 = CompositeVideoClip([part2_2_4, part2_1_4.set_opacity(0.65)])
    F_part2_5 = CompositeVideoClip([part2_2_5, part2_1_5.set_opacity(0.55)])
    F_part2_6 = CompositeVideoClip([part2_2_6, part2_1_6.set_opacity(0.45)])
    F_part2_7 = CompositeVideoClip([part2_2_7, part2_1_7.set_opacity(0.35)])
    F_part2_8 = CompositeVideoClip([part2_2_8, part2_1_8.set_opacity(0.25)])
    F_part2_9 = CompositeVideoClip([part2_2_9, part2_1_9.set_opacity(0.15)])
    F_part2_10 = CompositeVideoClip([part2_2_10, part2_1_10.set_opacity(0.05)])

    # 拼接视频片段
    video1 = concatenate_videoclips(
        [F_part2_1, F_part2_2, F_part2_3, F_part2_4, F_part2_5, F_part2_6, F_part2_7, F_part2_8, F_part2_9, F_part2_10])
    # 拼接视频片段
    video2 = concatenate_videoclips([part1, video1, part3], method="compose")
    #video2.write_videofile('8.mp4')

    #videoclip_nosound = concatenate_videoclips(video2, method="compose")
    video2.write_videofile("9.mp4", fps=30, remove_temp=True)

diehua('./img/243858.png', './img/243859.png')
'''

'''
====转场效果====
下滑转场-下滑过程屏幕黑，效果一般
clips1 = ImageClip(photo_path).set_duration(3)
slided_clips = [CompositeVideoClip([clip.fx( transfx.slide_out, 1, 'bottom')]) for clip in clips_list]
----------------------------
淡出转场
from moviepy.editor import *
from moviepy.video import fx

# 添加淡出效果
clip = clip.fx(fx.fadeout, fade_out_duration)

# 添加淡入效果
clip = clip.fx(fx.fadein, fade_in_duration)
-------------------
from moviepy.editor import *
from moviepy.video.compositing.transitions import slide_in

# 添加从左滑入的转场效果
transition = slide_in(clip2, clip1, transition_duration, 'left')
-------------------
渐变遮罩转场-暂不实现
from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects

# 创建一个遮罩
mask = ImageClip("mask_image.png", ismask=True)

# 将遮罩应用于片段
transition = clips_array([[clip1.with_mask(mask), clip2]])
-------------------
上下滑动转场-效果一般
from moviepy.editor import *
from moviepy.video.compositing.transitions import slide_in

# 添加从上滑入的转场效果
transition = slide_in(clip2, clip1, transition_duration, 'top')
-------------------
缩放转场
from moviepy.editor import *
from moviepy.video.fx.resize import resize

# 将 clip2 缩放为 0
clip2_start = clip2.fx(resize, 0.0)

# 在转场期间，将 clip2 从 0 缩放至 1
clip2_transition = clip2_start.fx(resize, 1.0, t=transition_duration)

# 将转场后的 clip2 与原始 clip2 进行连接
clip2 = concatenate_videoclips([clip2_transition, clip2])

# 连接 clip1 和 clip2
final_clip = concatenate_videoclips([clip1, clip2])
--------------------
交叉溶解转场
from moviepy.editor import *

# 设置转场持续时间
transition_duration = 1

# 创建一个遮罩，从黑色到白色的水平渐变
mask = ImageClip("mask_horizontal_gradient.png", ismask=True).resize(clip1.size)

# 使用遮罩在转场期间逐渐显示 clip2
clip2_transition = clip2.set_mask(mask.fx(vfx.fadein, transition_duration))

# 将转场后的 clip2 与原始 clip2 进行连接
clip2 = concatenate_videoclips([clip2_transition, clip2])

# 连接 clip1 和 clip2
final_clip = concatenate_videoclips([clip1, clip2])
--------------------
旋转转场
from moviepy.editor import *

# 为 clip2 创建旋转转场
clip2_rotated = clip2.fx(vfx.rotate, lambda t: -90 * t / transition_duration, preserve_origin=True)

# 将旋转的 clip2 与原始 clip2 拼接
clip2 = concatenate_videoclips([clip2_rotated.subclip(0, transition_duration), clip2])

# 连接 clip1 和 clip2
final_clip = concatenate_videoclips([clip1, clip2])
旋转转场2
from moviepy.editor import *

# 为 clip1 创建旋转转场
clip1_rotate = clip1.fx(vfx.rotate, lambda t: 360 * t / transition_duration, expand=False)

# 为 clip2 创建旋转转场
clip2_rotate = clip2.fx(vfx.rotate, lambda t: 360 * (1 - t / transition_duration), expand=False)

# 连接旋转转场后的片段
final_clip = concatenate_videoclips([clip1_rotate, clip2_rotate])

--------------------
垂直翻转转场
from moviepy.editor import *

# 为 clip2 创建垂直翻转转场
clip2_flipped = clip2.fx(vfx.mirror_y, duration=transition_duration)

# 将翻转的 clip2 与原始 clip2 拼接
clip2 = concatenate_videoclips([clip2_flipped.subclip(0, transition_duration), clip2])

# 连接 clip1 和 clip2
final_clip = concatenate_videoclips([clip1, clip2])
---------------------
模糊过渡转场
from moviepy.editor import *
from moviepy.video.fx.blur import blur

# 创建一个函数，根据给定的时间和转场持续时间计算模糊程度
def blur_amount(t, duration):
    return min(1, max(0, abs(t - duration / 2) * 2))

# 在转场期间逐渐模糊 clip1
clip1_blurred = clip1.fx(blur, lambda t: blur_amount(t - (clip1.duration - transition_duration), transition_duration))

# 在转场期间逐渐解除 clip2 的模糊
clip2_blurred = clip2.fx(blur, lambda t: blur_amount(transition_duration - t, transition_duration))

# 连接模糊过渡后的片段
final_clip = concatenate_videoclips([clip1_blurred, clip2_blurred])
------------------------
水平翻转转场
from moviepy.editor import *

# 为 clip2 创建水平翻转转场
clip2_flipped = clip2.fx(vfx.mirror_x, duration=transition_duration)

# 将翻转的 clip2 与原始 clip2 拼接
clip2 = concatenate_videoclips([clip2_flipped.subclip(0, transition_duration), clip2])

# 连接 clip1 和 clip2
final_clip = concatenate_videoclips([clip1, clip2])
-------------------------
颜色渐变转场
from moviepy.editor import *
from moviepy.video.fx.lum_contrast import lum_contrast

# 创建一个函数，根据给定的时间和转场持续时间计算对比度
def contrast_amount(t, duration):
    return min(1, max(0, abs(t - duration / 2) * 2))

# 在转场期间逐渐增加 clip1 的对比度
clip1_high_contrast = clip1.fx(lum_contrast, lambda t: contrast_amount(t - (clip1.duration - transition_duration), transition_duration), contrast=2)

# 在转场期间逐渐降低 clip2 的对比度
clip2_low_contrast = clip2.fx(lum_contrast, lambda t: contrast_amount(transition_duration - t, transition_duration), contrast=0.5)

# 连接对比度渐变后的片段
final_clip = concatenate_videoclips([clip1_high_contrast, clip2_low_contrast])
--------------------------
随机马赛克转场
from moviepy.editor import *
from moviepy.video.fx.pixelate import pixelate

# 为 clip1 和 clip2 添加随机马赛克效果
clip1_pixelated = clip1.fx(pixelate, size=(100, 100), p_size=(20, 20), xy=random.sample(range(0, 100), 2))
clip2_pixelated = clip2.fx(pixelate, size=(100, 100), p_size=(20, 20), xy=random.sample(range(0, 100), 2))

# 按顺序连接马赛克过渡后的片段
final_clip = concatenate_videoclips([clip1_pixelated, clip2_pixelated])
------------------------
边缘变亮转场
from moviepy.editor import *

# 创建一个纯白色的图像剪辑
white_clip = ColorClip(size=clip1.size, color=(255, 255, 255), duration=transition_duration)

# 为 clip1 创建边缘变亮转场
clip1_transition = CompositeVideoClip([clip1, white_clip.set_start(clip1.duration - transition_duration).set_opacity(lambda t: t / transition_duration)])

# 为 clip2 创建边缘变亮转场
clip2_transition = CompositeVideoClip([clip2, white_clip.set_start(0).set_opacity(lambda t: 1 - t / transition_duration)])

# 连接转场后的片段
final_clip = concatenate_videoclips([clip1_transition, clip2_transition])
----------------------
手绘效果转场
from moviepy.editor import *
from moviepy.video.fx.painting import painting

# 在转场期间为 clip1 和 clip2 添加手绘效果
clip1_painting = clip1.fx(painting, black=0.5).subclip(clip1.duration - transition_duration, clip1.duration)
clip2_painting = clip2.fx(painting, black=0.5).subclip(0, transition_duration)

# 连接手绘效果过渡后的片段
final_clip = concatenate_videoclips([clip1, clip1_painting, clip2_painting, clip2])
------------------------
逐像素过渡转场
from moviepy.editor import *

# 创建一个遮罩图像，每个像素的透明度随机改变
mask_array = np.random.rand(*clip1.size[::-1], 1) * 255
mask_image = ImageClip(mask_array, ismask=True)

# 使用遮罩逐像素过渡 clip1 和 clip2
transition_clip = CompositeVideoClip([clip1.set_mask(mask_image), clip2.set_mask(mask_image.invert())])

# 连接逐像素过渡后的片段
final_clip = concatenate_videoclips([clip1, transition_clip, clip2])
---------------------------
图像缩放转场
from moviepy.editor import *

# 为 clip1 创建缩放转场
clip1_resized = clip1.fx(vfx.resize, lambda t: 1 + 0.5 * (1 - t / transition_duration), origin="center")

# 为 clip2 创建缩放转场
clip2_resized = clip2.fx(vfx.resize, lambda t: 0.5 + 0.5 * t / transition_duration, origin="center")

# 连接缩放转场后的片段
final_clip = concatenate_videoclips([clip1_resized, clip2_resized])
---------------------------
图像滑动转场
from moviepy.editor import *

# 为 clip1 创建滑动转场
clip1_slide = clip1.fx(vfx.slide_out, lambda t: 'bottom' if t < transition_duration / 2 else 'top', transition_duration / 2)

# 为 clip2 创建滑动转场
clip2_slide = clip2.fx(vfx.slide_in, lambda t: 'top' if t < transition_duration / 2 else 'bottom', transition_duration / 2)

# 连接滑动转场后的片段
final_clip = concatenate_videoclips([clip1_slide, clip2_slide])


# 为 clip1 创建速度变化转场
#clip1_speed = clip1.fx(vfx.speedx, lambda t: 1 + t / transition_duration)
# 为 clip2 创建速度变化转场
#clip2_speed = clip2.fx(vfx.speedx, lambda t: 2 - t / transition_duration)
# 连接速度变化转场后的片段
#final_clip = concatenate_videoclips([clip1_speed, clip2_speed])


#声音渐入渐出
# 为 clip1 创建淡出音频效果
clip1_audio_fadeout = clip1.fx(vfx.audio_fadeout, transition_duration)
# 为 clip2 创建淡入音频效果
clip2_audio_fadein = clip2.fx(vfx.audio_fadein, transition_duration)
# 连接淡入淡出音频效果后的片段
final_clip = concatenate_videoclips([clip1_audio_fadeout, clip2_audio_fadein])
噪声过渡转场：
from moviepy.editor import *
from moviepy.video.fx.blink import blink
# 在转场期间为 clip1 和 clip2 添加闪烁噪声效果
clip1_blink = clip1.fx(blink, 10, 0.05).subclip(clip1.duration - transition_duration, clip1.duration)
clip2_blink = clip2.fx(blink, 10, 0.05).subclip(0, transition_duration)
# 连接噪声过渡后的片段
final_clip = concatenate_videoclips([clip1, clip1_blink, clip2_blink, clip2])
'''



 
def blur(image):
    """ Returns a blurred (radius=2 pixels) version of the image """
    return gaussian(image.astype(float), sigma=30)

# 读取待转换的视频
clip1 = VideoFileClip("9.mp4")

# 将视频放大并加蒙版遮罩
tempClip2 = VideoFileClip("9.mp4",audio=False,has_mask="True").resize(4)
clip2 = tempClip2.fl_image( blur )

# 将小的视频叠在大视频的居中位置
temp = CompositeVideoClip([clip2, clip1.set_pos("center")])

# 对叠好的视频进行剪切
final = temp.crop(x1=0, x2=clip2.w, y1=(clip2.h - clip1.h) / 2, y2=clip1.h + (clip2.h - clip1.h) / 2)

# 输出编辑完成的视频
final.resize(height=clip1.h).write_videofile("test.avi", codec="libx264")

