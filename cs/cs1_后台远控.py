# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/31 18:02
@Auth ： wang
@File ：cs1_后台远控.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


# 结论一。mstsc网上后台远控方法全部无效（注册表，bat，python顶号等）
# 结论二。todesk在无显卡欺骗器时无法正常使用
# 结论三。显卡欺骗器与显示器毫无区别
# 结论四。mstsc在设计时为多用户考虑，todesk在设计时以显示器为基础
# 结论五。使用完整版todesk，安全设置关闭结束控制自动黑屏，即可后台使用pyautogui，相当于显示器亮屏状态
# 结论六。不同分辨率，不同缩放尺寸，均会影响pyautogui识别。因此在新设备部署须重新截图，最好使用相对坐标

#测试代码：
import time
import pyautogui

def judgment_element(element_img_path):
    print(f'判断{element_img_path}')
    try:
        element = pyautogui.locateOnScreen(element_img_path, confidence=0.9)
        center = pyautogui.center(element)
    except:
        center = None

    print(f'存在{bool(center)}')
    return center

while True:
    # 一秒检测一次，若因最小化或黑屏屏幕发生变化，会输出False。
    print(pyautogui.size())
    time.sleep(1)
    if judgment_element('cs.png'):
        print(1)