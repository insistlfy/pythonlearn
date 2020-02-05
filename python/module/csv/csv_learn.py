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
    以返回列表的形式读取
    """

    @staticmethod
    def read_csv(file):
        print("start read csv by List...")
        with open(file, 'r') as fp:
            reader = csv.reader(fp)  # reader 迭代器
            next(reader)  # 是否需要输出标题
            for x in reader:
                first = x[0]
                second = x[1]
                third = x[2]
                print({"first": first, "second": second, "third": third})

    """
    已字典的形式读取 (推荐)
    """

    @staticmethod
    def read_csv_pro(file):
        print("start read csv by Dictionary...")
        with open(file, 'r') as fp:
            reader = csv.DictReader(fp)  # 使用DictReader创建的reader是一个字典对象，遍历后，不包含第一行数据
            for x in reader:
                value = {"title_1": x["title_1"], "title_2": x["title_2"]}
                print(value)

    """
    以元组的方式写入
    """

    @staticmethod
    def write_csv(_file, _header, _contents):
        print("start write csv by Tuple...")

        with open(_file, "w", encoding="utf-8", newline="") as fp:
            writer = csv.writer(fp)
            writer.writerow(_header)
            writer.writerows(_contents)
            print("write success...")

    """
    以字典的形式写入（推荐使用）
    """

    @staticmethod
    def write_csv_pro(_file, _header, _contents):
        print("start write csv by Dictionary...")

        with open(_file, "w", encoding="utf-8", newline="") as fp:
            writer = csv.DictWriter(fp, _header)  # 使用csv.DictWriter()方法，需传入两个个参数，第一个为对象，第二个为文件的title
            writer.writeheader()
            writer.writerows(_contents)
            print("write success...")


if __name__ == '__main__':
    # CsvUtil.read_csv("./csv/read_01.csv")
    # CsvUtil.read_csv_pro("./csv/read_01.csv")

    header = ["A", "B", "C", "D"]
    contents_01 = [
        (1, 1, 1, 1),
        (2, 2, 2, 2)
    ]
    contents_02 = [
        {"A": "a", "B": "b", "C": "c", "D": "d"},
        {"A": "1", "B": "2", "C": "3", "D": "4"}
    ]

    # CsvUtil.write_csv("./csv/read_02.csv", header, contents_01)
    CsvUtil.write_csv_pro("./csv/read_02.csv", header, contents_02)
