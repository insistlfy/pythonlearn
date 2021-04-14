# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: oop_06.py
@time: 2021-04-14 下午3:20
@description: oop_06
            Py模块调用
            -- 语法1： import 模块路径名（不需要py结尾） as 别名
            -- 语法2： from 模块路径（不需要py结尾） import 对象名
            -- 语法3： 使用__init__.py
"""

import python.practice.practice1 as p1
from python.practice.practice4 import guess
import python.oop.oop_05 as oop5

print(p1.num)
a = oop5.Animal('Animal', 'F', 2)
a.show()
print(guess())
