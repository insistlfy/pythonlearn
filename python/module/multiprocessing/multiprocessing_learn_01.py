# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: multiprocessing_learn_01.py
@time: 2020-02-06 下午4:07
@description: ① GIL全局解释器锁（Global Interpreter Lock）: 计算机程序设计语言解释器用于同步线程的工具，使得在同一进程内任何时刻仅有一个线程在执行。
                    -- Python的线程是操作系统线程。在Linux上为pthread，在Windows上为Win thread，完全由操作系统调度线程的执行。
                       一个python解释器进程内有一条主线程，以及多条用户程序的执行线程。即使在多核CPU平台上，由于GIL的存在，所以禁止多线程的并行执行。
                    -- Python解释器进程内的多线程是合作多任务方式执行。
                       当一个线程遇到I/O任务时，将释放GIL。计算密集型（CPU-bound）的线程在执行大约100次解释器的计步（ticks）时，将释放GIL。
                       计步（ticks）可粗略看作Python虚拟机的指令。计步实际上与时间片长度无关。可以通过sys.setcheckinterval()设置计步长度。
                    -- 在单核CPU上，数百次的间隔检查才会导致一次线程切换。在多核CPU上，存在严重的线程颠簸（thrashing）。
                    -- Python 3.2开始使用新的GIL,可以创建独立的进程来实现并行化
               ②CPU密集型(CPU-bound) : 也叫计算密集型
               ③IO密集型(I/O bound) :
               ④Queue :
               ⑤Pool :
               ⑥创建多进程 :
                    -- 语法 : multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={})
                    -- 参数 :
                        - group：分组，实际上很少使用
                        - target：表示调用对象，你可以传入方法的名字
                        - name：别名，相当于给这个进程取一个名字
                        - args：表示被调用对象的位置参数元组，比如target是函数a，他有两个参数m，n，那么args就传入(m, n)即可
                        - kwargs：表示调用对象的字典
"""

import threading
import multiprocessing
import time

"""
初识,感受单线程,多线程,多进程的执行效率
"""


def func_01(start, stop):
    print("感受单线程,多线程,多进程的执行效率")

    _list = []

    """
    range():
        -- 作用 : 函数可创建一个整数列表
        -- 语法 : range(start, stop[, step])
        -- 参数说明 : 
                start : 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
                stop : 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
                step : 步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
    """
    for i in range(start, stop):
        _list.append(i)


if __name__ == '__main__':
    # 多线程添加
    thread_list = []
    start_time = time.time()
    t1 = threading.Thread(target=func_01, args=(1, 50000000))
    t2 = threading.Thread(target=func_01, args=(50000000, 100000001))
    thread_list.append(t1)
    thread_list.append(t2)
    # 启动线程
    t1.start()
    t2.start()
    for thread in thread_list:
        thread.join()  # 阻塞主线程
    end_time = time.time()
    print("多线程用时:{}秒".format(end_time - start_time))

    # 单线程添加
    start_time = time.time()
    func_01(1, 100000001)
    end_time = time.time()
    print("单线程用时:{}秒".format(end_time - start_time))

    # 多进程添加
    start_time = time.time()
    process_list = []
    p1 = multiprocessing.Process(target=func_01, args=(1, 50000000))
    p2 = multiprocessing.Process(target=func_01, args=(50000000, 100000001))
    process_list.append(p1)
    process_list.append(p2)
    p1.start()
    p2.start()
    for p in process_list:
        p.join()
    end_time = time.time()
    print("多进程用时:{}秒".format(end_time - start_time))
