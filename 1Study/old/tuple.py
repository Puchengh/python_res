#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/2/10 22:09
# @Author : puchen
# @File : tuple.py

# 元组一旦定义完成是不能完成修改的

info_tuple = ("zhangsan", 2, 3, 1.75)

print(info_tuple[2])
print(type(info_tuple))


sigle_tuple = "zhangsan"
print(type(sigle_tuple))
sigle_tuple1 = ("zhangsan",)
print(type(sigle_tuple1))


for name in "text":
    print(name)


sign_list = [21, 12, 123, 123, 12, 3, 123]
print(tuple(sign_list))


print(id('hello'))