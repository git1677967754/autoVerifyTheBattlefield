import pyautogui
import time
import cv2
import pygetwindow
import psutil

def is_img_exist(shot_img_path, img_path, threshold = 0.8):
    """
    判断图片是否存在
    :param threshold:
    :param shot_img_path: 大图
    :param img_path: 小图
    :return: true or false
    """
    shot_img = cv2.imread(shot_img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    if shot_img is None or img is None:
        raise ValueError("无法读取图片，请检查路径是否正确")

    # 获取小图的模板匹配结果
    result = cv2.matchTemplate(shot_img, img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 如果最大值大于阈值，则认为小图存在于大图中
    return max_val > threshold

def keyboard_click(key = 'e', sleep_time = 1):
    """
    模拟键盘点击，附带延迟
    :param key:
    :param sleep_time:
    :return:
    """
    pyautogui.press(key)
    time.sleep(sleep_time)


def myclick(x, y, button='left', duration = 0.5):
    """
    模拟鼠标点击，先移动再点击，防止因未渲染而点击失败
    :param duration:
    :param x:
    :param y:
    :param button: 鼠标按键，默认左键
    :return: None
    """
    pyautogui.moveTo(x, y, duration)
    pyautogui.click(button=button)

def bring_to_front(window_title):
    """
    将指定程序调至焦点
    :param window_title: 程序的标题
    """
    # 获取指定程序窗口
    window = pygetwindow.getWindowsWithTitle(window_title)
    # 将窗口调至焦点
    window[0].activate()


def kill_process_by_name(process_name):
    """
    根据进程名结束进程
    :param process_name: 进程名
    :return: None
    """
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            print(f'kill {process_name}')
            proc.kill()

