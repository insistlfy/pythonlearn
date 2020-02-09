# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: selenium_learn_02.py
@time: 2020-02-09 下午3:46
@description: 模拟浏览器登录
"""
import time
from selenium import webdriver

# 声明驱动对象
chrome_driver = "/home/lfy/HDD/Project/mine/pythonlearn/python/module/selenium/chromedriver"
browser = webdriver.Chrome(executable_path=chrome_driver)
# 设置窗口全屏
browser.maximize_window()


def auto_alimail():
    # 发送get请求
    browser.get("http://mail.swifthealth.cn/alimail/auth/login")
    # 表单赋值
    browser.find_element_by_id("username").click().send_keys('****')
    browser.find_element_by_id('password').click().send_keys('****')
    # 点击提交按钮
    button = browser.find_element_by_id("login_submit_btn")
    button.click()


# #定位到登录按钮，并点击
def auto_baidu():
    browser.get('https://www.baidu.com/')
    time.sleep(1)
    login = browser.find_element_by_id('u1').find_element_by_class_name('lb')
    login.click()
    time.sleep(1)
    username = browser.find_elements_by_css_selector('p.tang-pass-footerBarULogin')[0]
    username.click()
    time.sleep(1)
    browser.find_element_by_name('userName').send_keys('****')
    time.sleep(1)
    browser.find_element_by_name('password').send_keys('****')
    time.sleep(1)
    password = browser.find_element_by_id('passport-login-pop-api').find_element_by_class_name('pass-button')
    password.click()
    # time.sleep(3)
    # sendcode = browser.find_element_by_id('TANGRAM__36__content_send_mobile').find_element_by_class_name(
    #     'forceverify-button ')
    # sendcode.click()  # 定位到发送验证码的元素，并点击
    print("=====>Auto Login baidu Successfully")


if __name__ == '__main__':
    # auto_baidu()
    auto_alimail()
