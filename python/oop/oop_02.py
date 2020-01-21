# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: oop_02.py
@time: 2020-01-21 下午3:04
@description: oop_02
"""
'''Python中的继承和多态 ,请注意与Java语言的区别
      -- 开闭原则 : 即对扩展开放,对修改封闭
      -- 对于静态语言(Java)来说,在下面的例子中,如果需要Animal类型,则传入的对象必须是Animal类型或它的子类,否则,将无法调用run()方法;
      -- 对于Python这样的动态语言来说,则不一定需要传入Animal类型,我们只需要保证传入的对象有一个run()即可;
'''


class Animal:
    def run(self):
        print("Animal is running")


class Dog(Animal):
    def run(self):
        print("Dog is running")

    # 静态方法
    @staticmethod
    def bark():
        print("Dog can bark")


class Cat(Animal):
    def run(self):
        print("Cat is running")


class Timer:
    def run(self):
        print("starting...")


def run_twice(animal):
    animal.run()
    animal.run()


if __name__ == '__main__':
    dog = Dog()
    dog.run()
    '静态方法直接调用,无需创建实例'
    Dog.bark()

    cat = Cat()
    cat.run()
    print("\n=======================================")

    run_twice(Animal())
    run_twice(Dog())
    run_twice(Cat())

    '此处注意与Java语言的区别'
    run_twice(Timer())
