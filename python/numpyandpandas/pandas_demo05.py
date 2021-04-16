# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: pandas_demo05.py
@time: 2021-04-16 下午3:53
@description: pandas_demo05
            -- ①： merge  todo
"""

import pandas as pd

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

left1 = pd.DataFrame({'key1': ['K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K2'],
                      'A': ['A0', 'A1', 'A2'],
                      'B': ['B0', 'B1', 'B2']})

right1 = pd.DataFrame({'key1': ['K0', 'K1', 'K2'],
                       'key2': ['K0', 'K2', 'K3'],
                       'C': ['C0', 'C1', 'C2'],
                       'D': ['D0', 'D1', 'D2']})

if __name__ == '__main__':
    print(left)
    print(right)

    res = pd.merge(left, right, on='key')
    # print(res)
    print('=====================================\n')

    res1 = pd.merge(left1, right1, on=['key1', 'key2'])
    print(res1)
