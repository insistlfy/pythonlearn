# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: oop_04.py
@time: 2020-09-09 下午3:25
@description: oop_04
"""
'__slots__ 用tuple定义允许绑定的属性名称'


class Fruit:
    __slots__ = ("num", "price")  # 用tuple定义允许绑定的属性名称

    @staticmethod
    def show():
        print('Fruit show...')


class Apple(Fruit):
    # __slots__ = ("tot_cost",)

    def print(self):
        print("Apple is delicious...")


if __name__ == '__main__':
    fruit = Fruit()
    fruit.num = "1"
    fruit.price = "1.0"
    print(fruit.num)
    print(fruit.price)

    apple = Apple()
    apple.color = "RED"
    print(apple.color)
    apple.print()
