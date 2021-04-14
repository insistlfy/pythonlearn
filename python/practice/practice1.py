# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: practice1.py
@time: 2021-04-14 上午9:12
@description: 使用list和set实现随机抽题
"""

import random

num = 10
print('采用list列表存储不重复的随机数'.center(100, '-'))
_list = []

while True:
    e = random.randint(1, 100)
    if e not in _list:
        _list.append(e)
        if len(_list) == num:
            break
print(_list)

print('采用set集合存储不重复的随机数'.center(100, '-'))
_set = set()
while len(_set) < num:
    e = random.randint(1, 100)
    _set.add(e)
    if len(_set) == num:
        break
print(_set)
