'''
列表的增删改查
1.添加元素  append 追加 类似排队
'''

# list1 = []
# list2 = ['面包']
# list1.append('火腿')
# list1.append('酸奶')
# list1.append('')
# print(list1)
#
# print(list1 + list2)
# print(list2 + list1)
#
# list1.extend(list2)
# print(list1)


# container = []   # 保存多件商品
# flag= True
# while flag:
#     name = input('商品名称：')
#     price = input('商品价格: ')
#     number = input('商品数量： ')
#     goods = [name, price, number]
#     #将商品添加到container
#     container.append(goods)
#
#     #添加商品
#     answer  = input('是否继续添加?(按q或者Q退出)')
#     if answer.lower() == 'q':
#         flag = False
# #遍历container
# for goods in container:   #列表里面套了一层列表
#     print('名称:{}\t价格:{}\t数量:{}'.format(goods[0],float(goods[1]),int(goods[2])))
import random

'''
删除 列表里面的内容
 pop 把下标对应的元素删除 下表不能超过范围,可以不用添加任何参数， 表示删除从后往前删除一个元素
 remove  根据元素名称进行删除，删除不存在的元素会导致报错 list.remove(x): x not in list，从左往右删除第一个元素

list = ['火腿','酸奶','牛奶','酸奶']
# list.pop()   #把下标对应的元素删除 下表不能超过范围

if '酸奶' in list:
    list.remove('酸奶')
print(list)

上面的方法不能删除所有酸奶
'''
# print(list.count('酸奶'))

# list = ['火腿','酸奶','牛奶','酸奶','酸奶']    #删除元素下标不会变  12345...   因此可能会出现遗漏删除
# list1 = list[::1]
# print(list1)
# for i in list[::1]:
#     if i == '酸奶':
#         list.remove(i)
# print(list)


# list = ['火腿','酸奶','牛奶','酸奶','酸奶']
#
# while '酸奶' in list:
#     list.remove('酸奶')
# print(list)

# n=0
# while n<len(list):
#     if list[n] == '酸奶':
#         list.remove(list[n])
#     else:
#         n += 1
# print(list)



# list = ['火腿','酸奶','牛奶','酸奶']
# print(list.reverse())


'''
修改,插队 不是完整的修改
'''
# list1=[1,2,3,4,5]
# list1.insert(0,8)   #[8, 1, 2, 3, 4, 5]
# print(list1)
#
# list1.reverse()    #反转 把所有元素翻转放入list中
# print(list1)
#
#
# list1[2] = 10
# print(list1)
#
# print(list1.index(10))   #返回的是下标的位置
#
#
# for i in range(0,1):
#     print(i)


# x = 'runoob'
# for i in range(len(x)) :
#     print(x[i])
#
# for i in range(12):
#     if i == 12:
#         break
#
# print(i)


'''
clear  清空列表的元素
'''
# list1=[1,2,3,4,5]
# list1.clear()
# print(list1)
# print(list)
# print(list1.count(5))  #和instr差不多
#
# if 1 not in list1:
#     print('元素在文件里面！')

# list1.pop(list1[1])
# del list1[1]
#
# print(list1)


'''
list存放机制

del list   #删除之后没有文件list这个列表了
list.clear()  #clear指的是清空list列表里面的内容

'''

#
# list1 = [1,2,3,4,5]
#
# list2 = list1    #内存地址指向list2  所以你变了里面的内容  所以list1的也会变
# list2.append(88)    #只有list会出现这种情况，string不会出现
#
#
# print(list1)
# print(list2)
# 结果
# [1, 2, 3, 4, 5, 88]
# [1, 2, 3, 4, 5, 88]

# del list2
# print(list1)
# #删除的是对象引用的指针


# print(id(list1))
# print(id(list2))

# a='qwerq'
# b=a
# a+='2'
# print(a)
# print(b)
# # 结果
# # qwerq2
# # qwerq


'''
sort   默认是升序的   通过reserve来控制是否升序  是 False  降序 True
reverse  单纯的反转  reverse
'''

# import random
# list1 = []
# print(id(list1))
# for i in  range(8):
#     # print(i)
#     ran = random.randint(1,20)
#     list1.append(ran)
#     # print(ran)
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)
#
#
# list1.reverse()
# print(list1)
# print(id(list1))




 