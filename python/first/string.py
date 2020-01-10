# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: string.py
@time: 2020-01-10 下午3:02
@description: 字符串练习
"""

# test String
_01 = '你好'
_02 = "你好"
_03 = '''你好'''
_04 = """
你好
世界
"""
print(_01)
print(len(_01))
print(_02)
print(len(_02))
print(_03)
print(len(_03))
print(_04)
print(len(_04))

'''
字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
'''
_str = "python"
print(_str)  # 输出字符串
print(_str[0])  # 输出字符串第一个字符
print(_str[0:-1])  # 输出第一个到倒数第二个所有的字符
print(_str[0:5:2])  # 截取从第一个开始至第六个字符,步长为2
print(_str[0:])  # 输出从第一个开始后的所有字符(包括第一个)
print(_str * 2)  # 输出字符串两次(用*运算符重复)
print('hello ' + _str + '!')  # 连接字符串(用+连接字符串)

print('------------------------------------------')

print('hello python \n!')
