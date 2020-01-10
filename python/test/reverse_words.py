# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: reverse_words.py
@time: 2020-01-10 下午4:22
@description: 字符串翻转
"""


def reverse(_input):
    # 切割字符串
    inputWords = _input.split(' ')
    # 翻转字符串
    inputWords = inputWords[-1::-1]
    # 重组组合字符串
    output = ''.join(inputWords)
    return output


def reverse1(_input):
    inputWords = list(_input)[-1::-1]
    _output = ''.join(inputWords)
    return _output


if __name__ == '__main__':
    _input = 'I like python'
    rw = reverse(_input)
    print(rw)

    _input2 = 'python'
    rw2 = reverse1(_input2)
    print(rw2)
