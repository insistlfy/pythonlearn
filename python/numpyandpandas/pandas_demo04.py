# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: pandas_demo04.py
@time: 2021-04-16 下午3:20
@description: pandas_demo04
            -- ①：导入导出数据
            -- ②： DataFrame 合并
"""

import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])

df4 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df5 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'])
df6 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['b', 'c', 'd', 'e'])

if __name__ == '__main__':
    data = pd.read_csv('pandas.csv')
    print(data)
    print('=====================================\n')

    data.to_pickle('pandas.pickle')
    data1 = pd.read_pickle('pandas.pickle')
    print(data1)
    print('=====================================\n')

    print(df1)
    print(df2)
    print(df3)
    print('=====================================\n')

    # concatenating
    res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
    print(res)
    print('=====================================\n')
    print('=====================================\n')

    # join, ['inner','outer']

    outer = pd.concat([df4, df5], ignore_index=True)  # 默认为outer
    print(outer)
    print('=====================================\n')
    inner = pd.concat([df4, df5], join='inner', ignore_index=True)
    print(inner)
    print('=====================================\n')

    # append
    res1 = df4.append([df5, df6], ignore_index=True)
    print(res1)
    print('=====================================\n')

    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    print(s1)
    print(df4.append(s1, ignore_index=True))
