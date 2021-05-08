# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: sklearn01.py
@time: 2021-04-22 上午10:09
@description: sklearn01
            -- 数据的获取
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets


iris = datasets.load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
print(df)
df.plot()
plt.show()
