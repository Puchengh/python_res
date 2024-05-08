class Money:
    count = 3


# print(Money.__name__)
# xxx = Money
# print(xxx.__name__)
#
# print(id(xxx))
# print(id(Money))
one = Money()
# print(one)



# 对象访问流程 会覆盖
one.age = 18
one.age = 21

one.pets = ['dog', 'cat']
one.pets.append('小黄')  # 增加值和修改值

del one.pets  # 删除属性
print(one.__dict__)

# 不同的对象不能相互访问属性

# 类增加一个属性
print(one.count)
print(one.__class__)
print(Money.__dict__)

