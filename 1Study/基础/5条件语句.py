#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/12/27 21:06
# @Author : puchen
# @File : 5条件语句.py

'''
if else
if elif else

'''

resule  = input("请输入：")
if resule == 'Y':
    print('您的输入是正确的')
    print('Over')

print('-------------')

#随机数
import random

rand = random.randint(1,10)
guess = input('请输入你猜的数据:')

if rand == guess:
    print('恭喜你猜对了！')