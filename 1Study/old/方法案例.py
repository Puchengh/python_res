#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/2/27 18:47
# @Author : puchen
# @File : 方法案例.py

# 1.实例方法--方法内部需要访问实例属性
#     实例方法内部可以使用类名，访问类属性
# 2.类方法--方法内部之需要方法类属性
# 3.静态方法 -- 方法内部 不需要访问实例属性和类属性

class Game(object):
    # 类属性
    top_score = 0

    def __init__(self, player_name):
        # 定义属性
        # player_name 实例属性
        self.player_name = player_name
    #静态方法
    @staticmethod
    def show_help():
        print("帮助信息，让僵尸进入大门")

    #类方法
    @classmethod
    def show_top_score(cls):

        print("历史记录 %d" % cls.top_score)

    # 实例方法
    def stat_game(self):
        print("%s 开始游戏了。。。" % self.player_name)


# 1.查看游戏的帮助信息
Game.show_help()

# 2.查看历史最高分
Game.show_top_score()

# 4.创建游戏对象
game = Game("小明")
game.stat_game()
