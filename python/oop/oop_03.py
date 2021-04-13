# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: oop_03.py
@time: 2020-01-21 下午4:18
@description: oop_03
"""
'Python面向对象高级编程'


class Student:

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):

        self._birth = value


if __name__ == '__main__':
    s = Student()
    s.birth = '2020-08-08'
    print(s.birth)
