#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/2/10 21:24
# @Author : puchen
# @File : list.py
import keyword

'''
list数组是 first in  last out
'''


def testeee():
    print("isnert into table dwb_hj_help")


testeee()

name_list = ['张三', '李四']
print(name_list[1])
print(name_list.index("李四"))
name_list[1] = "王五"
print(name_list.index("王五"))
name_list.append("王小六")
print(name_list)
print(len(name_list))

temp_list = ["test", "text"]
temp_list.extend(temp_list)
print(temp_list)
temp_list.extend(name_list)
print(temp_list)
name_list.extend(temp_list)
print(name_list)

temp_list1 = ["test", "text", 111, 1212321]
temp_list1.pop()
temp_list1.pop(2)
print(temp_list1)

temp_list2 = ["test", "text", 111, 1212321]
temp_list2.remove(111)
print(temp_list2)

temp_list3 = ["test", "text", 111, 1212321]
temp_list3.clear()
print(temp_list3)

temp_list4 = ["test", "text", 111, 1212321]
# del 关键字本质上是用来将一个变量存内存中删除的
del temp_list4[1]
print(temp_list4)

temp_list5 = [33, 22, 111, 1212321]
temp_list5.sort()
print(temp_list5)


# 列表的循环遍历
# 在python中为了提高列表的遍历效率，专门提供的迭代iteration遍历
temp_list5.sort(reverse=True)
print(temp_list5)

temp_list6 = [33, 22, 111, 1212321]
temp_list6.reverse()
print(temp_list6)

temp_list6 = [33, 22, 111, 1212321]
print(temp_list6.count(22))

print(keyword.kwlist)

print(len(keyword.kwlist))
for name in keyword.kwlist:
    print("我的名字叫做 %s" % name)
