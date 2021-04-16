# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: numpy_demo02.py
@time: 2021-04-15 下午5:35
@description: numpy_demo02
"""

import numpy as np

a = np.array([1, 1, 1])
b = np.array([2, 2, 2])

A = np.arange(12).reshape((3, 4))

B = np.arange(4)

if __name__ == '__main__':
    print(np.vstack((a, b)))  # 上下合并
    print(np.hstack((a, b)))  # 左右合并
    print(a[np.newaxis, :].shape)

    print(np.concatenate((a, b)))
    print(np.concatenate((a, b), axis=0))
    print('==========================================\n')

    # 分割
    print(f'A={A}')
    print(np.split(A, 2, axis=1))
    print(np.split(A, 3, axis=0))

    print(np.array_split(A, 3, axis=1))

    print(np.vsplit(A, 3))
    print(np.hsplit(A, 2))
    print('==========================================\n')

    # 赋值
    print(f'B={B}')

    C = B
    D = B
    E = C
    print(f'C={C}')
    print(f'D={D}')
    print(f'E={E}')
    print(C is B)
    B[0] = 11
    print(f'C={C}')
    print(f'D={D}')
    print(f'E={E}')

    # deep copy
    M = B.copy()
    print(f'M={M}')
    B[0] = 12
    print(f'B={B}')
    print(f'M={M}')
