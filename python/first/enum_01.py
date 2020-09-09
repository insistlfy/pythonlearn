# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: enum_01.py
@time: 2020-09-09 下午5:32
@description: 枚举的简单使用
"""

from enum import Enum, unique


@unique  # @unique装饰器可以帮助我们检查保证没有重复值
class WeekDay(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wen = 3
    Thu = 4
    Fri = 5
    Sat = 6


if __name__ == '__main__':
    print(WeekDay)
    print(WeekDay.Sun.name)
    print(WeekDay.Sun.value)

    Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)

    print("=====================================\n")
    for name, member in WeekDay.__members__.items():
        print(name, '=>', member, ',', member.value)
