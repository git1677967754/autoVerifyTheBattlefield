import os
import time

import keyboard
import pyautogui

import unit


def trigger(number):
    """
    触发器
    :param number: 运行次数
    :return: None
    """
    start = 0
    while True:
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
            # 判断是否退出
            unit.myclick(940, 960)
            start += 1
            if start == number:
                exit()
        elif unit.is_img_exist('./jietu/screenshot1.png', './img/1.jpeg'):
            # 选择难度
            unit.myclick(1514, 513)
            time.sleep(0.2)
        elif unit.is_img_exist('./jietu/screenshot1.png', './img/2.jpeg'):
            # 选择角色
            unit.myclick(1752, 993)
            time.sleep(7)# 防止提前释放技能导致进入冷却


unit.bring_to_front('尘白禁区')
trigger(1)
