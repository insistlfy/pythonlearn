# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: practice4.py
@time: 2021-04-14 上午10:53
@description: practice4
              实现猜数小游戏
"""

import random


def guess(maxValue=10, maxTimes=3):
    # 随机生成一个数据
    value = random.randint(1, maxValue)
    print(f'value={value}')

    for i in range(maxTimes):
        try:
            num = int(input('请输入一个数字'))
        except:
            # 发生异常执行此语句块
            print('必须输入数字...')
            break
        else:
            # 没有异常执行此语句块
            if num == value:
                print('恭喜您，猜对了...')
                break
            elif num < value:
                print('输入的数字太小了，请重新输入')
            else:
                print('输入的数字太大了，请重新输入')
    else:
        # for正常结束，才会进入else
        print(f'对不起，一共有{maxTimes}次机会，已使用完了，正确答案是{value}')


if __name__ == '__main__':
    guess(10, 3)
