# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/31 17:46
@Auth ： wang
@File ：main.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import time
import pyautogui
import random


def slipped_page():
    pyautogui.moveTo(1920 / 2, 1080 / 2)

    # 翻页
    pyautogui.scroll(-2000)
    print('翻页中')
    time.sleep(random.randint(0, 5))
    pyautogui.scroll(-200)
    pyautogui.scroll(-2000)
    print('滚轮翻')
    time.sleep(random.randint(0, 5))


def judgment_element(element_img_path, conf=0.7):
    print(f'判断{element_img_path}')
    try:
        element = pyautogui.locateOnScreen(element_img_path, confidence=conf)
        center = pyautogui.center(element)
    except:
        center = None

    print(f'存在{bool(center)}')
    return center


def click_element_position(element_img_path):
    print(f'点击{element_img_path}中心')

    element = pyautogui.locateOnScreen(element_img_path, confidence=0.7)

    center = pyautogui.center(element)
    pyautogui.click(center)
    time.sleep(random.randint(1, 7))


if __name__ == '__main__':
    time.sleep(4)
    while True:
        print('判断是否有知识点')

        if judgment_element('./element/yellow_point.png') or judgment_element('./element/green_point.png'):
            print('判断是否有视频')
            if judgment_element('./element/video.png'):
                pyautogui.click(739, 749)
                # click_element_position('./element/videoplay.png')  # 有视频则播放视频
                while True:
                    time.sleep(1)
                    if judgment_element('./element/green_point.png', conf = 0.9):  # 等待视频播放结束
                        # pyautogui.alert(text="视频播放结束", title="信息")  # 视频播放结束
                        break

            while True:
                slipped_page()  # 翻页直到找到下一节按钮
                if judgment_element('./element/next.png'):  # 下一节
                    click_element_position('./element/next.png')
                    if judgment_element('./element/next_section.png'):
                        click_element_position('./element/next_section.png')
                    break

        else:
            while True:
                slipped_page()  # 翻页直到找到下一节按钮
                if judgment_element('./element/next.png'):  # 下一节
                    click_element_position('./element/next.png')
                    if judgment_element('./element/next_section.png'):
                        click_element_position('./element/next_section.png')
                    break
        time.sleep(1)
