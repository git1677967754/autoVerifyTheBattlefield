import numpy as np
import pyautogui
import time
import cv2


def is_img_exist(shot_img_path, img_path):
    """
    判断图片是否存在
    :param shot_img_path: 大图
    :param img_path: 小图
    :return: true or false
    """
    shot_img = cv2.imread(shot_img_path)
    img = cv2.imread(img_path)

    if shot_img is None or img is None:
        raise ValueError("无法读取图片，请检查路径是否正确")

    # 获取小图的模板匹配结果
    result = cv2.matchTemplate(shot_img, img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 设定匹配阈值，可以根据实际情况调整
    threshold = 0.8
    # 如果最大值大于阈值，则认为小图存在于大图中
    return max_val > threshold

def keyboard_click(key = 'e', sleep_time = 1):
    pyautogui.press(key)
    time.sleep(sleep_time)


def myclick(x, y, button='left'):
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click(button=button)