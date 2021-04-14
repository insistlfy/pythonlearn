# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: oop_05.py
@time: 2021-04-14 下午2:53
@description: oop_05
            面向对象三大特征 ： 封装，继承，多态
            -- 封装：
            -- 继承： python支持多继承
            -- 多态： 重写（子类重写父类的方法），重载（Py重载是通过可变参数来体现的，而且更方便）
            -- 函数和方法的本质区别： 方法一定会有调用的主体（对象，类），而对象和类作为第一个参数自动传入
            -- Py中除了对象方法，还有类方法和静态方法

"""


class Animal(object):
    __total = 0  # 类成员（属于当前类，且只有一份）

    # '__'开头和结尾的方法为特殊方法，它会自动调用，主要完成创建对象属性赋值
    def __init__(self, name, sex, age):
        # public : 任何区域都能访问
        # protected : 当前类和Py模块和子类才能访问，'_'开头
        # private : 只有当前类能访问，'__'开头
        self.name = name
        self._sex = sex
        self.__age = age

    def show(self):  # 默认方法是public  --对象方法
        print(f'姓名为：{self.name}')

    @classmethod  # 修饰器，声明一个类方法
    def classShow(cls):  # 对于类方法，当前类作为第一个参数自动传入

        # 类方法不能操作对象成员
        print(f'total : {cls.__total}')


if __name__ == '__main__':
    animal = Animal('Animal', 'F', 2)
    animal.show()

    # 类方法可以通过类或者对象调用
    animal.classShow()
    Animal.classShow()
