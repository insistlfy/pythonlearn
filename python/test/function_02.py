# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: function_02.py
@time: 2020-01-15 下午4:22
@description: function_02
"""


def print_models(unPrinted_designs, finished_models):
    while unPrinted_designs:
        current_design = unPrinted_designs.pop()
        print("Printing model: " + current_design)
        finished_models.append(current_design)


def show_completed_models(finished_models):
    print("\nThe following models have been printed ; ")
    for completed_model in finished_models:
        print(completed_model)


if __name__ == '__main__':
    unprinted_designs = ['111', '222', '333']
    completed_models = []

    print_models(unprinted_designs, completed_models)
    show_completed_models(completed_models)
