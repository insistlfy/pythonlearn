# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: pandas_demo02.py
@time: 2021-04-16 下午2:21
@description: pandas_demo02
            数据对比筛选
"""

import pandas as pd
import numpy as np

dates = pd.date_range('20210101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

if __name__ == '__main__':
    print(df)
    print('=======================================\n')

    print(df['A'])
    print(df.A)
    print('=======================================\n')

    print(df[0:3])
    print(df['2021-01-02':'2021-01-05'])
    print('=======================================\n')

    # select by label：loc
    print(df.loc['20210102'])
    print(df.loc[:, ['A', 'B']])  # 所有行，A,B两列
    print('=======================================\n')

    # select by position:iloc
    print(df.iloc[:, 1:3])
    print('=======================================\n')

    # mixed selection:ix
    # print(df.ix[:3, ['A', 'C']])
    # print('=======================================\n')

    # Boolean indexing
    print(df[df.A > 8])
    # print('=======================================\n')

    df.iloc[2, 2] = 1111
    print(df)
    df.loc['20210101', 'B'] = 2222
    print(df)

    df.A[df.A > 16] = 0
    print(df)
    df['F'] = np.nan
    print(df)
