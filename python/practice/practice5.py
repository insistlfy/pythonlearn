# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: practice5.py
@time: 2021-04-14 上午11:26
@description: practice5
"""
from random import randint


def binaryQuery(lst, value):
    start = 0
    end = len(lst)

    while start < end:
        # 计算中间位置
        middle = (start + end) // 2

        if value == lst[middle]:
            return middle
        elif value < lst[middle]:
            end = middle - 1
        elif value > lst[middle]:
            start = middle + 1
    # 查找不到返回False
    return False


lst = [randint(1, 30) for i in range(20)]
# 给序列排序
lst.sort()
print(lst)
result = binaryQuery(lst, 30)
if result != False:
    print('index is ', result)
else:
    print('Not Exist')
