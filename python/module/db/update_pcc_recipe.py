# !usr/bin/env python
# -*- coding:utf-8 _*-
# @author:lfy
# @file: update_pcc_recipe.py
# @time: 2020-02-13 下午12:33
# @description: Test
import cx_Oracle
import time
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

conn = cx_Oracle.connect('lchis/q1w2@192.168.1.142:1521/orcl')
cursor = conn.cursor()


def update_pcc_recipe():
    print("定时任务开始更新...")
    sql = "update FIN_OPB_ACCOUNT set CARD_NO = CARD_NO where CARD_NO='0034516972'"
    cursor.execute(sql)
    conn.commit()
    print('更新成功...,time={},sql={}.'.format(time.strftime('%H:%M:%S'), sql))


if __name__ == '__main__':
    update_pcc_recipe()
