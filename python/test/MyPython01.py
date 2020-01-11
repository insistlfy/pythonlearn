# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: MyPython01.py
@time: 2020-01-10 下午6:00
@description: MyPython01
"""

import os
import cx_Oracle

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

his_conn = cx_Oracle.connect('lchis/q1w2@192.168.1.142:1521/orcl')
his_cursor = his_conn.cursor()

lis_conn = cx_Oracle.connect('lchis/q1w2@192.168.1.142:1521/orcl')
lis_cursor = lis_conn.cursor()

pacs_conn = cx_Oracle.connect('lchis/q1w2@192.168.1.142:1521/orcl')
pacs_cursor = pacs_conn.cursor()


def get_his_middle_table_count():
    rec_sql = "select count(*) from jdyyy.REC_SYNC_TABLE2"
    base_sql = "select count(*) from jdyyy.BASIC_SYNC_TABLE2"
    busi_sql = "select count(*) from jdyyy.BUSI_SYNC_TABLE2"
    pha_sql = "select count(*) from jdyyy.PHA_SYNC_TABLE2"
    appoint_sql = "select count(*) from jdyyy.APPOINT_SYNC_TABLE2"
    inhositem_sql = "select count(*) from JDYYY.INITEM_SYNC_TABLE2"
    inhosmed_sql = "select count(*) from JDYYY.INMED_SYNC_TABLE2"
    inhosorder_sql = "select count(*) from jdyyy.INIPM_SYNC_TABLE2"

    his_cursor.execute(rec_sql)
    rec_cnt = his_cursor.fetchall()
    print('rec-middle-table-num: ' + str(rec_cnt[0][0]))

    his_cursor.execute(base_sql)
    base_cnt = his_cursor.fetchall()
    print('base-middle-table-num: ' + str(base_cnt[0][0]))

    his_cursor.execute(busi_sql)
    busi_cnt = his_cursor.fetchall()
    print('busi-middle-table-num: ' + str(busi_cnt[0][0]))

    his_cursor.execute(pha_sql)
    pha_cnt = his_cursor.fetchall()
    print('pha-middle-table-num: ' + str(pha_cnt[0][0]))

    his_cursor.execute(appoint_sql)
    pha_cnt = his_cursor.fetchall()
    print('appoint-middle-table-num: ' + str(pha_cnt[0][0]))

    his_cursor.execute(inhositem_sql)
    pha_cnt = his_cursor.fetchall()
    print('inhositem-middle-table-num: ' + str(pha_cnt[0][0]))

    his_cursor.execute(inhosmed_sql)
    pha_cnt = his_cursor.fetchall()
    print('inhosmed-middle-table-num: ' + str(pha_cnt[0][0]))

    his_cursor.execute(inhosorder_sql)
    pha_cnt = his_cursor.fetchall()
    print('inhosorder-middle-table-num: ' + str(pha_cnt[0][0]))


def get_lis_middle_table_count():
    lis_sql = "select count(*) from LIS.LIS_SYNC_TABLE2"
    lis_cursor.execute(lis_sql)
    cnt = lis_cursor.fetchall()
    print('lis-middle-table-num: ' + str(cnt[0][0]))


def get_pacs_middle_table_count():
    pacs_sql = "select count(*) from PACS.PACS_SYNC_TABLE2"
    pacs_cursor.execute(pacs_sql)
    cnt = pacs_cursor.fetchall()
    print('pacs-middle-table-num: ' + str(cnt[0][0]))


if __name__ == '__main__':
    get_his_middle_table_count()
    get_lis_middle_table_count()
    get_pacs_middle_table_count()
