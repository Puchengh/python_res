#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/12/27 16:25
# @Author : puchen
# @File : 2关系运算符.py
'''
关系运算符 结果 True  False

 < > <= >= == != is
'''

a = 10
b = 23
print(a > b)  # False
print(b > a)  # True

print(a == b)
print(a != b)

x = 'abc'
y = 'abcd'
print(x == y)
print(x < y)  #比较的时候比较的ascii码

# 1+2  = 3

c  = 10
print (a <= c)


'''
输入考试分数，判断成绩是够在100-80之间？
'''
score = float(input('输入分数：'))
print (80 <= score <= 100)  #可以连在一起
