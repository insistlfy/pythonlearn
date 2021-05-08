# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: sklearn02.py
@time: 2021-04-22 下午6:29
@description: sklearn02
            -- 数据预处理
"""
import pandas as pd
import matplotlib as plt
from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import svm

iris = datasets.load_iris()
scaler = preprocessing.MinMaxScaler()  # MinMaxScaler将样本特征值线性缩放到0，1之间
scaler.fit(iris.data)  # 先fit
data = scaler.transform(iris.data)  # 在transform
target = iris.target
print(data)
print("=======================================")

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=1 / 3)

print(len(X_train))
print(len(X_test))
print("=======================================")

clf = svm.SVC(kernel='linear', C=1, probability=True)
clf.fit(X_train, y_train)  # 用训练集数据训练模型
print(clf.predict(X_test))
print("=======================================")

# 查看参数
print(clf.get_params())
print("=======================================")

# 概率值
print(clf.predict_proba(X_test))
print("=======================================")

# 评分（对于不同的模型有不同的评分算法，有score方法内部所定义）
print(clf.score(X_test, y_test))
