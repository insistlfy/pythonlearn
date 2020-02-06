# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: multiprocessing_learn_02.py
@time: 2020-02-06 下午8:53
@description: 通过继承的方式
"""

import multiprocessing
import time


class MyProcessing(multiprocessing.Process):

    def __init__(self, _start, _stop):
        super(MyProcessing, self).__init__()
        self._start = _start
        self._stop = _stop

    # 复写父类的run方法
    def run(self) -> None:
        _list = []
        for i in range(self._start, self._stop):
            _list.append(i)


if __name__ == '__main__':
    start_time = time.time()
    process_list = []
    p1 = MyProcessing(1, 50000000)
    p2 = MyProcessing(50000000, 100000001)
    process_list.append(p1)
    process_list.append(p2)
    p1.start()
    p2.start()
    for p in process_list:
        p.join()
    end_time = time.time()
    print("多进程用时:{}秒".format(end_time - start_time))
