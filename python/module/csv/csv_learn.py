# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: csv_learn.py
@time: 2020-02-05 下午5:15
@description: csv_learn
"""

import csv


class CsvUtil:
    """
    以列表形式读取
    """

    @staticmethod
    def read_csv(file):
        print("start read csv...")
        with open(file, 'r') as fp:
            reader = csv.reader(fp)  # reader 迭代器
            next(reader)  # 是否需要输出标题
            for x in reader:
                first = x[0]
                second = x[1]
                third = x[2]
                print({"first": first, "second": second, "third": third})

    """
    已元组的形式读取
    """

    @staticmethod
    def read_csv_pro():
        print("start read csv...")

    @staticmethod
    def write_csv():
        print("start write csv...")

    @staticmethod
    def write_csv_pro():
        print("start write csv...")


if __name__ == '__main__':
    CsvUtil.read_csv("./csv/read_01.csv")
