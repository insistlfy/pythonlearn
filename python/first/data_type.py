# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: data_type.py
@time: 2020-01-10 下午3:36
@description: ①Python中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建
              ②在Python中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型
              ③Python3 中有六个标准的数据类型：
                Number（数字）
                    -- int
                    -- float
                    -- bool
                        -- 在Python2中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True;
                        -- 在Python3中,把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加)
                    -- complex（复数）)
                String（字符串）
                List（列表）
                Tuple（元组）
                Set（集合）
                Dictionary（字典）
              ④Python3 的六个标准数据类型中：
                不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
                可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
              注意 : string,list,tuple都属于sequence(序列).
"""

'''
基础数据和字符串
'''
counter = 100
miles = 1000.0
name = 'python'
a = b = c = 1
print('数字(int) : ', counter)
print('数字(float) : ', miles)
print('字符串(String) : ', name)
print('同时赋值 : ', a + b + c)
print('类型判断 : ', isinstance(counter, int))
print('类型判断 : ', isinstance(miles, float))
print('布尔类型(bool)与Number(数字)相加 : ', True + 1)
print('\n=========================================\n')

"""
List(列表)  ---有序
    定义 : 列表是写在方括号 [] 之间、用逗号分隔开的元素列表;
    用法 : 列表中元素的类型可以不相同,它支持数字,字符串甚至可以包含列表(所谓嵌套)
    截取语法 : 变量[头下标:尾下标] (索引值以 0 为开始值，-1 为从末尾的开始位置)
"""
_str = 'python'
_list = ["python", "PYTHON", 3000, 3000.0]
_list2 = [1, 2.0]
_list3 = ['1', '2']
_list4 = []
print('输出列表 : ', _list)
print('输出空列表 : ', _list4)
print('输出列表第一个元素 : ', _list[0])
print('输出列表第二个元素 : ', _list[1])
print('输出列表第三个元素 : ', _list[2])

print('列表截取 : ', _list[0:1])
print('列表拼接 : ', _list + _list2)
print('列表复制 : ', _list2 * 2)

print('字符串转换为列表：', list(_str))
print('列表转换为字符串：', ''.join(_list3))
_list.append(_list2)
print('列表遍历：')
for i in _list:
    print(i)
print('\n=========================================\n')

"""
Tuple (元组)
    定义 : 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开
    用法 : 元组中的元素类型也可以不相同
"""
_tuple = ('python', "PYTHON", 3000, 3000.0)
_tuple1 = ('python',)  # 一个元素，需要在元素后添加逗号
_tuple2 = 'hello', 'python'  # 可以不使用()
emptyTuple = ()  # 空元组

print('输出元组_tuple : ', _tuple)
print('输出元组_tuple2 : ', _tuple2)
print('输出空元组 : ', emptyTuple)
print('输出元组中第一个元素 : ', _tuple[0])
print('\n=========================================\n')

"""
Set (集合)
    定义 : 集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员
    用法 : 进行成员关系测试和删除重复元素,使用大括号 { } 或者 set() 函数创建集合,创建一个空集合必须用 set()
"""
_set = set()
_set1 = {'A', 'B', 'C', 'python', 'A'}
_set2 = {'A', 'E', 'F', 'PYTHON'}
_set3 = set(_set1)

print('输出空集合 : ', _set)
print('输出集合_set1 : ', _set1)
print('输出集合_set2 : ', _set2)
print('输出集合_set3 : ', _set3)
print('输出差集 : ', _set1 - _set2)
print('输出并集 : ', _set1 | _set2)
print('输出交集 : ', _set1 & _set2)
print('输出两个集合中不同时存在的元素 : ', _set1 ^ _set2)
print('\n=========================================\n')

"""
Dictionary (字典) --无序
    定义 : 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合
    用法 : 字典是无序的对象集合,典当中的元素是通过键来存取的;
          键(key)必须使用不可变类型;
          在同一个字典中，键(key)必须是唯一的;
"""
_dic = {}
_dic1 = {1: 'python', 'name': 'PYTHON'}
_dic2 = {1: '1', 2: '2'}
print('输出空字典 : ', _dic)
print('输出字典_dic1 : ', _dic1)
print('输出字典中键为1的值 : ', _dic1[1])
print('输出字典_dic1的所有键 : ', _dic1.keys())
print('输出字典_dic1的所有值 : ', _dic1.values())
print('输出字典中键为name的值 : ', _dic1['name'])
print('输出字典_dic2 : ', _dic2)
