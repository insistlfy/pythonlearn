# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: multiprocessing_learn_03.py
@time: 2020-02-06 下午9:38
@description: Queue(进程通信)
                -- 特点 :
                    先进先出
                -- 常用方法 :
                    -- put() :
                        向队列中存放数据,如果队列已满将阻塞,直到队列释放空间;
                    -- get() :
                        返回队列的一条数据,如果队列为空将阻塞,直到队列有数据可用为止;
                    -- qsize() :
                        获取队列中数据的数据;
                    -- empty() :
                        判断队列是否为空;
                    -- full() :
                        判断队列是否已满;
                    -- get_nowait() :
                        取数据时不等待,如果队列为空直接抛出异常;
                    -- put_nowait() :
                        存数据时不等待,如果队列为空直接抛出异常;
                    -- close() :
                        关闭队列.
"""

import multiprocessing
import random
import time


def func1(queue):
    for i in range(1, 6):
        sec = random.randrange(1, 5)
        time.sleep(sec)
        # 向队列中添加数据
        queue.put(i)
        print("{} 第{}个数字加入队列".format(time.strftime("%H:%M:%S"), i))


def func2(queue):
    for i in range(1, 6):
        # 取出队列中的数据
        queue.get()
        print("{} 取出队列中第{}个数字".format(time.strftime("%H:%M:%S"), i))


if __name__ == '__main__':
    queue = multiprocessing.Queue(3)
    # 创建进程
    p1 = multiprocessing.Process(target=func1, args=(queue,))
    p2 = multiprocessing.Process(target=func2, args=(queue,))
    # 启动进程
    p1.start()
    p2.start()
