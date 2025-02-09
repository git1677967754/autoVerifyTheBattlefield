import time

import keyboard
import pyautogui

import unit

# 全局退出标志
exit_flag = False

def trigger():
    """
    触发程序
    :return:None
    """
    while True:
        if exit_flag:
            exit()
        pyautogui.screenshot().save('./jietu/screenshot1.png')
        if unit.is_img_exist('./jietu/screenshot1.png', './img/3.jpeg'):
            # 判断是否释放技能
            unit.keyboard_click()
        elif unit.is_img_exist('./jietu/screenshot1.png', './img/4.jpeg'):
            # 判断是否选择buff
            unit.myclick(959, 512)
            time.sleep(0.5)
            unit.myclick(960, 1000)
        elif unit.is_img_exist('./jietu/screenshot1.png', './img/5.jpeg'):
            # 判断是否选择到单体buff
            unit.myclick(294, 988)
            time.sleep(0.5)
            unit.myclick(1372, 762)
        elif unit.is_img_exist('./jietu/screenshot1.png', './img/6.jpeg'):
            # 一次验证战场结束
            unit.myclick(940, 960)
        elif unit.is_img_exist('./jietu/screenshot1.png', './img/7.jpeg'):
            # 拟境次数已耗尽,退出脚本
            # 可选，在运行结束后杀死游戏进程,'尘白禁区'的运行进程名默认为‘Game.exe’，请谨慎开启，存在误杀可能
            # unit.kill_process_by_name('Game.exe')
            exit()
        elif unit.is_img_exist('./jietu/screenshot1.png', './img/1.jpeg'):
            # 选择难度
            unit.myclick(1514, 513)
            time.sleep(0.2)
        elif unit.is_img_exist('./jietu/screenshot1.png', './img/2.jpeg'):
            # 选择角色
            unit.myclick(1752, 993)
            time.sleep(7)# 防止提前释放技能导致进入冷却


keyboard.on_press(unit.on_key)
try:
    unit.bring_to_front('尘白禁区')
except Exception as e:
    print(e)
    exit()
trigger()
