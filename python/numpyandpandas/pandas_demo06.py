# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: pandas_demo06.py
@time: 2021-04-16 下午5:31
@description: pandas_demo06
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# plot data

# Series 线性
data = pd.Series(np.random.randn(1000), index=np.arange(1000))

# DataFrame
data1 = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list('ABCD'))

if __name__ == '__main__':
    print(data)
    data = data.cumsum()
    print(f'data={data}')
    data.plot()
    plt.show()
    print('==========================================\n')

    data1 = data1.cumsum()
    print(f'data1={data1}')
    data1.plot()
    plt.show()
    print('==========================================\n')

    ax = data1.plot.scatter(x='A', y='B', color='Blue', label='Class 1')
    data1.plot.scatter(x='A', y='C', color='Green', label='Class 2', ax=ax)
    plt.show()
