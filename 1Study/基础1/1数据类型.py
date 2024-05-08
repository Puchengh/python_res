#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/12/27 15:44
# @Author : puchen
# @File : 1数据类型.py

'''
数据类型
int
float
string
boolean
'''

money = 28
print(type(money))  # print 属于一个内置函数

money = 280

money = 28.9

print(type(money))

money = '15万'  # 字符串是单引号 双引号 三引号都行
print(type(money))

# 类型转换
# input('请输入用户名：')  # 阻塞型函数

# 字符串拼接
person = 'puchen'
address = '广东省宝安区'
print('我是:%s,我住在:%s' % (person, address))  #格式化输出%s %d %f

