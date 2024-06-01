# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
import time
import pyautogui

next1_path = 'next1.png'
next2_path = 'next2.jpg'
task_end_path = 'task_end.png'

test2_path = 'test2.png'
test3_path = 'test3.jpg'

traget3_path = 'traget3.jpg'

video2_path = 'video2.png'
video3_path = 'video3.jpg'

play_button = 'play_button.jpg'

cspng = 'cs.png'
def judgment_element(element_img_path):
    print(f'判断{element_img_path}')
    try:
        element = pyautogui.locateOnScreen(element_img_path, confidence=0.9)
        center = pyautogui.center(element)
    except:
        center = None

    print(f'存在{bool(center)}')
    return center


def click_element_position(element_img_path):
    print(f'点击{element_img_path}中心')

    element = pyautogui.locateOnScreen(element_img_path, confidence=0.9)


    center = pyautogui.center(element)
    pyautogui.click(center)


def watch_the_video():
    print('当前为视频页')
    time.sleep(5)
    while True:

        if judgment_element(task_end_path):
            break

        if judgment_element(play_button):
            click_element_position(play_button)
            print('播放视频')
            break

        time.sleep(5)


    while not judgment_element(task_end_path):
        print('等待播放完')
        time.sleep(20)

def next_section_video():
    # 翻页
    pyautogui.scroll(-2000)
    print('翻页中')
    time.sleep(2)
    pyautogui.scroll(-200)
    pyautogui.scroll(-2000)
    print('滚轮翻')
    time.sleep(2)
    pyautogui.click(1650,1250)
    print('点击固定点')

    if judgment_element(next1_path):
        click_element_position(next1_path)

    # 鼠标立即移到屏幕中央
    # pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
    time.sleep(2)
    print('翻页完成')


def next_section_test():
    # 翻页
    pyautogui.scroll(-2000)
    print('翻页中')
    time.sleep(2)
    pyautogui.scroll(-200)
    pyautogui.scroll(-2000)
    print('滚轮翻')
    time.sleep(2)
    pyautogui.click(1650,1250)
    print('点击固定点')

    if judgment_element(next2_path):
        time.sleep(2)
        click_element_position(next2_path)



    # 鼠标立即移到屏幕中央
    # pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
    time.sleep(2)
    print('翻页完成')

def next_section():
    # 翻页
    pyautogui.scroll(-2000)
    print('翻页中')
    time.sleep(2)
    pyautogui.scroll(-200)
    pyautogui.scroll(-2000)
    print('滚轮翻')
    time.sleep(2)

    time.sleep(4)

    if judgment_element(next1_path):
        click_element_position(next1_path)


    time.sleep(1)
    # 鼠标立即移到屏幕中央
    pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
    time.sleep(2)
    print('翻页完成')



while True:
    print('start')

    # 获取当前屏幕分辨率
    print(pyautogui.size())
    screenWidth, screenHeight = pyautogui.size()
    while True:
        print(pyautogui.size())
        time.sleep(1)
        if judgment_element(cspng):
            print(1)

        # if judgment_element(yellow_point) or judgment_element(green_point):
        #
        #
        # if 找到黄点or绿点：
        #     一直划
        #     if 看到视频：
        #         看视频
        #
        # else：
        #     一直划
        #
        # if 看到下一节：
        #     点击
        #     if 弹出未完成：
        #         点击下一节
    # if judgment_element(video2_path) or judgment_element(video3_path):
    #     time.sleep(30)
    #     watch_the_video()
    #     print('视频翻页，固定加选择1点击')
    #     next_section_video()
    #
    # if judgment_element(traget3_path):
    #     print('学习目标，选择点击')
    #     next_section()
    #
    #
    # if judgment_element(test2_path) or judgment_element(test3_path):
    #     print('习题翻页，固定加选择2点击')
    #     next_section_test()
    #
    #
    #
    # time.sleep(3)

