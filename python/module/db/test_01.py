# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: test_01.py
@time: 2020-02-13 上午10:03
@description:  test
"""

import cx_Oracle

conn = cx_Oracle.connect('lchis/q1w2@192.168.1.142:1521/orcl')
cursor = conn.cursor()


def test():
    sql = "select * from FIN_OPB_ACCOUNT where CARD_NO='0034516972'"
    cursor.execute(sql)
    print("查询成功,sql={}".format(sql))

    sql1 = "update FIN_OPB_ACCOUNT set CARD_NO = CARD_NO where CARD_NO='0034516972'"
    cursor.execute(sql1)
    conn.commit()
    print("更新成功....")


if __name__ == '__main__':
    test()
