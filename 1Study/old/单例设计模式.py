#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/2/27 19:02
# @Author : puchen
# @File : 单例设计模式.py

# 音乐播放对象
# 单例设计模式  让类创建的对象  在系统中只有一个实例
#             每一次执行类名返回的对象 内存地址是相同的
# 使用类名创建对象是  python的解释其首先会调用__new__方法为对象分配空间
#  __new__是一个有object基类提供的内置的静态方法 主要作用有两个 1)在内存中为对象分配空间  2)返回对象的引用


class MusicPlayer(object):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否是空对象
        if cls.instance is None:
            # 2.调用父类的方法 为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3.返回类属性保存的对象引用
        return cls.instance

    # pass

    def __init__(self):
        # 1.判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return
        # 2.如果没有执行过  在执行初始化动作
        print("初始化播放器")

        # 3.修改类属性的标记
        MusicPlayer.init_flag = True



# 创建多个对象

player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
