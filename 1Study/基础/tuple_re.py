"""
列表可以删除，增加，但是元组的元素的不能修改（增 删 改）
元组使用小括号
元组的定义
tuple 元组
list 列表

"""
# tuple1 = ()
# tuple1 = ('2',)  # 如果元组里面有一个元素，需要加个逗号 才能表名它是一个元组 （1,）  如果不加就是基础数据类型
# print(tuple1)  # 结果是  2

tuple1 = (1, 2, 3, 4, 5, 2, 2, 2, 2, 2,)
# print(tuple1)

"""
元组下标和名称
"""
# print(tuple1.count(2))
# print(tuple1[0])

# print(tuple1[::-1])

#index(key)
# print(tuple1.index(2))

#包含start不包含stop
# print(tuple1.index(2,3,6))  # 3指的是下标位置  2指的是里面的位置   print(tuple1.index(2,3,3))会报错  ValueError: tuple.index(x): x not in tuple  ，元素找不到就会报错

# print(len(tuple1))  # in not in 这些都属于系统的东西
#
# if 2 in tuple1:
#     print('在tuple里面。')
# else:
#     print('不在tuple里面。')
#
# for i in tuple1:
#     print(i)

print(list(tuple1))  # 元组转列表
print(tuple(list(tuple1)))  #元组转列表

