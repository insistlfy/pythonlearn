# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: pandas_demo01.py
@time: 2021-04-16 下午12:15
@description: pandas_demo01
"""

import pandas as pd
import numpy as np

s = pd.Series([1, 2, 5, np.nan, 44, 1])

dates = pd.date_range('20210101', periods=6)

df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
df1 = pd.DataFrame(np.arange(24).reshape(6, 4))

if __name__ == '__main__':
    print(s)
    print(dates)
    print('==================================\n')

    print(df)
    print(df1)

    print(df1.dtypes)
    print(df1.index)
    print(df1.columns)
    print(df1.values)
    print(df1.describe())
    print(df1.T)
    print('==================================\n')

    print(df1.sort_index(axis=1, ascending=False))
    print(df1.sort_index(axis=0, ascending=False))
    print('==================================\n')

    print(df1.sort_values(by=1))
