'''
集合
set  底层是通过字典封装的  key不允许重复  是无序的
集合的表示：{元素,元素,元素,元素}
字典的表示: {key,value,key,value,key,value,key,value}
空集合的声名   set3 = set()

'''

import random

# set3 = set()
# set1 = {'zhangsan'}
# print(set1)
#
# #强转set  可以去重
# list1 = [1,2,3,4,5,6,3,4,6]
# print(set(list1))
# print(type(set3))
#

#添加元素
# set3.add('红楼梦')
# set3.add('盗墓笔记')   #返回值为None
# print(set3)

#append extend    ---> list
# add update      ---> set

# s = 'qwer'
# print(random.choice(s))


#移除元素
# set3.remove('红楼梦')   #如果找不到在这集合里面会报错
# print(set3)

# set3.discard('红楼梦2')  #如果在集合里面找不到 不会报错 也不会删除
# print(set3)


# del set3
# print(set3)   #只能用删除

# set3.clear()
# print(set3)
# set3.add('2')
# print(set3)

# set3.clear()
# set3.pop()  #随机删除一个元素,如果集合为空，则会抛出一个异常
# print(set3)


#集合：交集 intersection  并集 union  差集  difference
set2 = {1,2,3,4,5}
set3 = {4,5,6,7,8,9}

# result = set2.intersection(set3)  #交集
# print(result)
#
# result = set2.union(set3)  #并集
# print(result)
#
# result = set2.difference(set3)   #差集
# print(result)
#
#
# result = set3.difference(set2)   #差集
# print(result)

print(set3 | set2)   #并集
print(set3 & set2)   #交集
print(set3 - set2)   #差集
print(set3 ^ set2)   #除了交集之外的元素



print(globals())




















