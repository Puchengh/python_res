import random

ran = random.random()  # 0~1之间的随机小数
print(ran)

ran = random.randrange(1,10,2)  # 产生的范围，步长  2 只能产生基数
#其实就是range(i, j)
print(ran)

ran = random.randint(1,2)  # 左右都包含[] 闭区间
print(ran)

list1 = ['a','s','d','f']
ran = random.choice(list1)  # 随机选择列表的内容
print(ran)


pai = ['A','K','Q','J']
random.shuffle(pai)   # 随机打乱顺序
print(pai)


# 验证码
def func():
    code = ''
    for i in range(4):
        ran1 = str(random.randint(0,9))
        ran2 = chr(random.randint(65,90))
        ran3 = chr(random.randint(97,122))
        print([ran1, ran2, ran3])
        ran = random.choice([ran1, ran2, ran3])
        code += ran
    return code

print(func())
