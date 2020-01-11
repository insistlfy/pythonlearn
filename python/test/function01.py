# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: function01.py
@time: 2020-01-11 下午12:18
@description: function01
"""


def hello():
    print("Hello Python")


def world(self):
    print(self)


def format_name(first_name, middle_name, last_name):
    _full_name = first_name + ' ' + middle_name + ' ' + last_name
    return _full_name.title()


def format_name_pro(first_name, last_name, middle_name=''):
    if middle_name:
        _full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        _full_name = first_name + ' ' + last_name
    return _full_name.title()


def city_country(city, country):
    return city + ',' + country


def make_album(star, album):
    return {star: album}


hello()
world("Hello World...")

print(format_name('john', 'lee', 'hooker'))
print(format_name_pro('bryant', 'kobe'))
print(format_name_pro('john', 'lee', 'hooker'))
print(city_country('西安', '中国'))

print(make_album('周杰伦', '说散就散'))
