# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: update_pcc.py
@time: 2020-02-13 上午10:49
@description: 每天晚上九点定时更新最近一天的挂号的药品收费信息
"""

from threading import Timer
import cx_Oracle
import time

conn = cx_Oracle.connect('lchis/q1w2@192.168.1.142:1521/orcl')
cursor = conn.cursor()


def update_pcc_recipe():
    print("定时任务开始更新...")
    sql = "update FIN_OPB_ACCOUNT set CARD_NO = CARD_NO where CARD_NO='0034516972'"
    cursor.execute(sql)
    conn.commit()
    print('更新成功...,time={},sql={}.'.format(time.strftime('%H:%M:%S'), sql))
    Timer(5, update_pcc_recipe).start()


if __name__ == '__main__':
    timer = Timer(5, update_pcc_recipe)
    timer.start()
