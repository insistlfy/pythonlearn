# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: numpy_demo.py
@time: 2021-04-15 上午10:34
@description: numpy_demo
            ① ： 矩阵（数组）
"""

import numpy as np

array = np.array([[1, 2],
                  [2, 3]])

array1 = np.arange(4).reshape((2, 2))

print(array)
print('array number of dim:', array.ndim)  # 维度
print('array shape:', array.shape)  # 形状
print('array size:', array.size)  # 大小
print('array1 number of dim:', array1.ndim)  # 维度
print('array1 shape:', array1.shape)  # 形状
print('array1 size:', array1.size)  # 大小
print('=================================================\n')

a = np.array([1, 2, 3], dtype=np.int64)
b = np.array([1, 2, 3], dtype=np.float64)
print(a)
print(b)
print('=================================================\n')

x = np.zeros((3, 4), dtype=int)
print(x)
y = np.ones((2, 2), dtype=float)
print(y)
m = np.linspace(1, 10, 6).reshape((2, 3))
print(m)
n = np.arange(4)
print(n)
print('=================================================\n')

aa = np.array([1, 2, 3])
bb = np.arange(3)
print(aa, bb)
print(aa + bb)
print(aa - bb)
print(aa ** 2)  # 平方
print(bb > 1)
print(bb == 1)
print('=================================================\n')

print(f'array : {array}')
print(f'array1 : {array1}')

c_dot = np.dot(array, array1)
# c_dot_2 = array.dot(array1)
# print(c_dot)
# print(c_dot_2)
print('=================================================\n')

print(np.sum(array))
# print(np.sum(array, aixs=0))
# print(np.sum(array, aixs=1))
print(np.max(array))
print(np.min(array))

# 最小值索引
print(np.argmin(array))
print(np.argmax(array))
print('=================================================\n')
# 平均值
print(np.mean(array))
print(np.average(array))
print(array.mean())
# 中位数
print(np.median(array))
print(np.cumsum(a))
print(np.nonzero(array))
print(array)  # 逐行排序

print(np.transpose(array))
print(array.T)

A = np.arange(3, 15).reshape((3, 4))
print(A)
print(A[2][2])
print(A[2, 2])
print(A[2, :])
print(A[:, 2])
print('=================================================\n')

for column in A:
    print(column)

for column in A.T:
    print(column)
print('=================================================\n')

print(A.flatten())
for item in A.flat:
    print(item)
