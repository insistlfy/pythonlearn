# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: data_type.py
@time: 2020-01-10 下午3:36
@description: ①Python中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建
              ②在Python中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型
              ③Python3 中有六个标准的数据类型：
                Number（数字）   --- (Python3 支持 int、float、bool、complex（复数）)
                String（字符串）
                List（列表）
                Tuple（元组）
                Set（集合）
                Dictionary（字典）
              ④Python3 的六个标准数据类型中：
                不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
                可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
"""

# 基础
counter = 100
miles = 1000.0
name = 'python'
a = b = c = 1
print(counter)
print(miles)
print(name)
print(a + b + c)
print('\n=========================================\n')

total = ['one', 'two', 'three']
print(total)
print(total[0])
print(total[1])
print(total[2])
for i in total:
    print(i)
