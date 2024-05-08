# import turtle
# import random
#
# colors = ["red", "yellow", "green", "blue", "purple", "orange"]
#
# for i in range(10):
#     turtle.color(random.choice(colors)) # 随机选择颜色
#     turtle.circle(50)
#     turtle.right(36) # 向右旋转36度


import turtle

for i in range(5):
    turtle.circle(50 + i * 20) # 半径每次增加10
    turtle.penup() # 抬起画笔
    turtle.right(90) # 向右旋转90度
    turtle.forward(20) # 向前移动10个单位
    turtle.left(90) # 向左旋转90度
    turtle.pendown() # 落下画笔