# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: pandas_demo03.py
@time: 2021-04-16 下午3:11
@description: pandas_demo03
            处理丢失数据
"""

import pandas as pd
import numpy as np

dates = pd.date_range('20210101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

if __name__ == '__main__':
    df.iloc[0, 1] = np.nan
    df.iloc[1, 2] = np.nan

    print(df)
    print('=================================\n')

    print(df.dropna(axis=1, how='any'))
    print(df.dropna(axis=0, how='all'))
    print('=================================\n')

    print(df.isnull())
    print(np.any(df.isnull()) == True)
