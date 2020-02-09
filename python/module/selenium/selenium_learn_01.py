# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: selenium_learn_01.py
@time: 2020-02-07 下午8:41
@description: 初识(请安装对应浏览器的驱动)
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # 按照什么方式查找
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
from selenium.webdriver.support import expected_conditions as EC  # 异常
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素

# 声明驱动对象
chrome_driver = "/home/lfy/HDD/Project/mine/pythonlearn/python/module/selenium/chromedriver"
browser = webdriver.Chrome(executable_path=chrome_driver)


def func_01():
    # 发送get请求
    browser.get("https://www.baidu.com/")
    browser.get("https://www.taobao.com/")
    browser.get("https://www.python.org/")
    browser.back()
    time.sleep(1)
    browser.forward()


def func_02():
    try:
        # 发送get请求
        browser.get("https://www.baidu.com/")
        # 找到目标
        _input = browser.find_element_by_id("kw")
        # 输入'python'关键字
        _input.send_keys("python")
        # 回车
        _input.send_keys(Keys.ENTER)
        # 等待数据加载
        _wait = WebDriverWait(browser, 10)
        # 加载
        _wait.until(EC.presence_of_element_located((By.ID, 'content_left')))

        # 输出搜索的路径
        # print(browser.page_source)
        print(browser.current_url)
        print(browser.get_cookies())

    finally:
        # 关闭谷歌浏览器
        # browser.close()
        print("")


if __name__ == '__main__':
    # func_01()
    func_02()
