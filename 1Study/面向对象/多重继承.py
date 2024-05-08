"""
python支持多继承

如果继承了多个类 每个父类中都有相同的方法，那么可以通过这个方法来查找顺序
    print(inspect.getmro(类名))  # 告诉是类中要搜索的顺序
    print(类名.__mro__)  # 也可以使用这个魔术方法

经典类:
    从左到右 深度优先
新式类:  新式类的意思就是在每个类后面继承object (object):
    广度优先

"""


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print('----eat不带参数')
#
#     def eat(self, food):   # 第二个会把eat覆盖掉，没有重载的概念，只有重写的概念
#         print('----eat', food)
#
#
# p = Person('jack')
# p.eat('狮子头')

class Base:
    def test(self):
        print('------base-------')


# python支持多继承
class A(Base):
    def test(self):
        print('--------AAAAAA')


class B(Base):
    def test1(self):
        print('-------BBBBBB')


class C(A, B, Base):
    def test2(self):
        print('----------CCCCCCC')


c = C()
c.test1()

import inspect

print(inspect.getmro(C))  # 告诉是类中要搜索的顺序
print(C.__mro__)  # 也可以使用这个魔术方法
