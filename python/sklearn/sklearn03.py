# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: sklearn03.py
@time: 2021-04-29 下午4:58
@description: sklearn03
"""

from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import svm

# 网格搜索法 （超参数）
from sklearn.model_selection import GridSearchCV

# k折交叉验证
from sklearn.model_selection import cross_val_score

# 分类模型评分报告
from sklearn.metrics import classification_report

iris = datasets.load_iris()
scaler = preprocessing.MinMaxScaler()
scaler.fit(iris.data)
data = scaler.transform(iris.data)
target = iris.target
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=1 / 3)

clf = svm.SVC(kernel='linear', C=1, probability=True)
clf.fit(X_train, y_train)

print(classification_report(target, clf.predict(data), target_names=iris.target_names))
print("=============================================")

scores = cross_val_score(clf, data, target, cv=5)  # 5折交叉验证
print(scores)
print("=============================================")

# 平均得分和95%置信区间
print("Accuracy:%0.2f(+/-0.2f)" % scores.mean(), scores.std() * 2)
print("=============================================")

# 估计器
svc = svm.SVC()

# 超参数空间
param_grid = [{'C': [0.1, 1, 10, 100, 1000], 'kernel': ['linear']},
              {'C': [0.1, 1, 10, 100, 1000], 'gamma': [0.001, 0.01], 'kernel': ['rbf']}]

# 打分函数
scoring = 'accuracy'

# 指定采样方法
clf = GridSearchCV(svc, param_grid, scoring=scoring, cv=10)
clf.fit(data, target)
