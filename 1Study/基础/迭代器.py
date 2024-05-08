"""
可迭代的对象:
    1.生成器
    2.集合 列表 元组 字典 字符串
如何判断一个对象是否是可迭代的
    isinstance()

迭代器：
    迭代是访问集合元素的一种方式  迭代器是一个可以记住遍历的位置的对象
    特点:迭代器对象从合计的第一个元素开始访问，直到所有的元素别访问完结束
    迭代器只能往前  不会后退

    定义:可以被next()函数调用并不断返回下一个值的对象成为迭代器 Iterable

    可迭代是不是迭代器?

    1.生成器是可迭代的  也是迭代器
    2.list是可迭代的 当不是迭代器

可以通过iter 把集合 列表 元组 字典 字符串 转换为Iterable 迭代器，生成器本身就是一个迭代器

"""
from collections import Iterable

list1 = [1, 2, 3, 4, 5]
# g = isinstance(list1, Iterable)   #DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated, and in 3.8 it will stop working
# print(g)  #结果是True

# print(next(list1))  #list 不是迭代器

# print(next(iter(list1)))    #DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated, and in 3.8 it will stop working

