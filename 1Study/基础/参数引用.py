'''
引用:
值是靠引用来传递的
我们可以用id()来判断两个变量是否为同一个值得引用 ，我们可以将id值理解为那块内存的地址标示。
'''

# a = 10
# b = a
# c = a
#
# print(id(a))
# print(id(b))
# print(id(c))
#
# import sys
#
# print(sys.getrefcount(a))  # 查找指针指向的个数
#
# list1 = [1, 2, 3, 4]
# list2 = list1  # 赋值的时候是把引用地址给了前面一个变量
# list3 = list1
# print(sys.getrefcount(list1))
#
# del list3
# print(sys.getrefcount(list2))
# print(list2)


'''
值是靠引用来传递的
函数的引用：
    最终还是看是否是可变类型和不可变类型
    如果是可变:里面发生改变，外部就能看到改变后的内容
    如果是不可变：里面发生发表，不会影响外部的内容
'''

# 不可变类型会导致引用指针发生改变
# import sys
# def test(n1):
#     n2 = 100
#     # n1和n2都属于局部变量
#     print(sys.getrefcount(n1))   # 14
#     for i in range(n1):
#         print('---->', i)
#     n1 += 1
#     print(sys.getrefcount(n1))   #10
#
# n = 9
# test(n)
#
# print(n)   #9


# 可变类型不会导致引用指针发生改变
list1 = [1, 2, 3]


def test1(l):
    if isinstance(l, list):
        for i in l:
            print('--->', i)
        l.insert(0, 8)
    else:
        print('不是列表类型的！')


test1(list1)
print(list1)
