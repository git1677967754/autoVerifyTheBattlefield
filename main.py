import pygetwindow
import unit
import time
import pyautogui


def trigger():
    while True:
        pyautogui.screenshot().save('./jietu/screenshot1.png')
        if unit.is_img_exist('./jietu/screenshot1.png', './img/3.jpeg'):
            unit.keyboard_click()
        elif unit.is_img_exist('./jietu/screenshot1.png', './img/4.jpeg'):
            unit.myclick(959, 512)
            time.sleep(0.5)
            unit.myclick(960, 1000)
            time.sleep(0.3)
            pyautogui.screenshot().save('./jietu/screenshot2.png')
            if unit.is_img_exist('./jietu/screenshot2.png', './img/5.jpeg'):
                unit.myclick(294, 988)
                time.sleep(1)
                unit.myclick(1372, 762)
        elif unit.is_img_exist('./jietu/screenshot1.png', './img/6.jpeg'):
            unit.myclick(940, 960)
            time.sleep(1.5)
        elif unit.is_img_exist('./jietu/screenshot1.png', './img/1.jpeg'):
            unit.myclick(1514, 513)
            time.sleep(0.2)
        elif unit.is_img_exist('./jietu/screenshot1.png', './img/2.jpeg'):
            unit.myclick(1752, 993)
            time.sleep(7)



def bring_to_front(window_title):
    """
    将指定程序调至焦点
    :param window_title: 程序的标题
    """
    # 获取指定程序窗口
    window = pygetwindow.getWindowsWithTitle(window_title)
    # 将窗口调至焦点
    window[0].activate()


try:
    bring_to_front('尘白禁区')
except:
    pass

for i in range(99):
    trigger()