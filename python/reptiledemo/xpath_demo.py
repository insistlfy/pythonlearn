# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: xpath_demo.py
@time: 2021-04-14 下午4:47
@description: xpath_demo
"""

from lxml import etree

wb_data = """

"""

html = etree.HTML(wb_data)
print(etree.tostring(html), type(html))
