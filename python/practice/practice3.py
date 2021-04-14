# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: practice3.py
@time: 2021-04-14 上午10:30
@description: practice3
变量作用域和Lambda表达式
        ① ： if，for，try中定义的变量，在外部可以访问
        ② ： 函数和类中定义的变量，就是局部的，外部不能访问
"""

for i in range(3):  # 0,1,2
    if i == 2:
        num = 100
    else:
        num = 50
    print(num)
print(num)

a = 10


def func1():
    print('func1 a=', a)


def func2():
    a = 5  # 就近原则
    print('func1 a=', a)


def func3():
    global a  # 但钱操作的是外部变量
    a += 20
    print('func1 a=', a)


func1()
func2()
func3()


def add(x, y):
    return x + y


# 等价上面的函数add
_add = lambda x, y: x + y

print(add(1, 2))
print(_add(1, 2))
