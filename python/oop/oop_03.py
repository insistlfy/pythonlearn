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
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


if __name__ == '__main__':
    s = Student()
    s.score = 60
    print(s.score)
