'''
魔术方法

__init__: 初始化魔术方法
触发时机： 初始化对象时触发(不是实例化触发  当时和实例化在一个操作中)

__new__： 实例化的魔术方法
触发时机： 在实例化对象的时候触发

__call__:对象调用方法
触发时机： 将对象当成函数使用的时候 会默认调用此函数中的内容

__del__: delete 的缩写 析构魔术方法
触发时机  当对象没有用(没有任何变量引用)的时候被触发
del 删除的是对地址的引用
当一块空间没有了任何引用,默认执行del ref = 0


__str__ :
出发时机：打印对象名  自动触发去调用__str__里面的内容
注意: return 定义要在__str__里面添加return return后面内容就是打印对象看到的内容


魔术方法:
重点
__init__(构造方法，创建完空间之后调用的第一个方法)  __str__

了解
__new__  开辟空间
__del__  没有指针引用的时候会调用
__call__ 把对象当成函数调用的时候需要重写
'''

# class Person():
#     def __init__(self, name):
#         print('----->init', self)
#         self.name = name
#
#     # def __init__(self):
#     #     print('----->init', self)
#
#     def __new__(cls, *args, **kwargs):  #向内存中申请空间  --地址
#         print('----->new', cls)
#         # return super(Person, cls).__new__(cls)
#         return object.__new__(cls)
#
#     def __call__(self, name):  # 对象本身调用自己当成函数来调用
#         print('------>call')
#         print(name)
#
# # p = Person()
# p = Person('jack')
# # print(p)
#
# # 如果需要把实例当成函数就需要重写call的魔术方法
# p('hello')
# # print(p.name)


# import sys
#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def __del__(self):
#         print('删除的是', self.name)
#
#
# p = Person('Jack')
#
# p1 = p
# p2 = p
# p1.name = 'Tom'
#
# print(p1.name)
# print(p2.name)
#
# print(sys.getrefcount(p))
#
# # del p2  # 只是删除了p2对p的引用
#
# del p2
#
# p1.name = 'jack'
# del p1
#
# print(sys.getrefcount(p))
#
# # 对象赋值
#
# n = 5
# n1 = n


# 在代码最末尾的时候，python解释器 回收在本次执行过程中使用到的空间
# python底层自带垃圾回收机机制  --> 内存




'''
单纯打印对象名称，出来的是一个地址
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '姓名:'+self.name+',年龄是'+str(self.age)

p = Person('Tom', 8)
print(p)



