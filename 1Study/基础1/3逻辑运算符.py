#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/12/27 16:37
# @Author : puchen
# @File : 3逻辑运算符.py

'''
逻辑运算符
and or not
and :与  并且   只要一侧为假  结果为假
or :或 或者 只要一侧为真 true  结果则为真
not: 非
'''

a = 1
b = 3

print(a and b)  #如果两个都是非0的数字  结果则去and后面的值  场景  username  = '123' and password  =  'admin'

c = 0
print(c and 0)  #and 两边只要一边为0 结果即为0

print (a>b and a < b)
print (a==c and a < b)

print('*'*40)

print(a or b)  #如果两个都是非0的数字  结果则去or前面的值

print (a>b or a < b)
print (a==c or a < b) #场景  1 账号密码  or 2 手机号码  验证码

flag  = True
print(not flag)

print(not (a>c))
