# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: oop_01.py
@time: 2020-01-15 下午5:45
@description: oop_01
"""
'"__"双下划线开头的变量是私有变量'


class Student:

    def __init__(self, name, sex):
        self.__name = name
        self.sex = sex

    def go_to_school(self):
        print(self.__name.title() + " go to school...")

    def leave_school(self):
        print(self.__name.title() + " leave school...")

    @staticmethod
    def info_test(name, sex, weight):
        print("My name is " + name + ",sex is " + sex + ",weight is " + weight + ".")

    # 获取属性
    def get_name(self):
        return self.__name

    # 获取属性
    def set_name(self, name):
        self.__name = name


if __name__ == '__main__':
    student = Student("Curry", "M")
    student.go_to_school()
    student.leave_school()

    student.set_name("James")
    print(student.get_name())
    print(student.sex)

    Student.info_test("James", "M", "150")
