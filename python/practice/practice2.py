# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: practice2.py
@time: 2021-04-14 上午9:49
@description:  函数参数 ： 必填，缺省，可变，关键字
               函数调用时，一个*代表对参数解包
               函数定义时，连个**代表关键字参数
"""
import random


# 必填
def _random(num, start, end):
    print('采用set集合存储不重复的随机数'.center(100, '-'))
    _set = set()
    while len(_set) < num:
        e = random.randint(start, end)
        _set.add(e)
        if len(_set) == num:
            break
    print(_set)


_random(10, 1, 100)


# 缺省
def info(name, age, sex, nation='中国'):
    print(f'name:{name},age:{age},sex:{sex},nation:{nation}')


info('Li', '18', 'M')


# 可变
def add(*num):
    print(num, type(num))
    _sum = 0
    for i in num:
        _sum += i
    return _sum


print(add(1, 2, 3))
# 可变参数的时序解包功能
_list = [1, 2, 3, 4]
_set = {1, 2, 3, 4}
print(add(*_list))  # 一个*代表对参数进行解包
print(add(*_set))


# 关键字参数
def showInfo(name, age, nation='中国', **other):
    print(other, type(other))
    print(f'name:{name},age:{age},nation:{nation},other:{other}')


showInfo('Li', '18', '中国', city='西安', phone='123456')
_dict = {'city': '中国', 'phone': '123456'}
showInfo('Li', '18', '中国', **_dict)  # 用两个**对关键字解包
