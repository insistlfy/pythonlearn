# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: sys_learn.py
@time: 2020-01-10 下午3:28
@description: sys_learn
"""

import sys

print('==============Python import mode ==============')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\npython路径为', sys.path)
