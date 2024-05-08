# if 5>3:
#     pass
# else:
#     pass

'''
列表推导式：最终得到的是一个列表
格式 [ i for i in 可迭代的]
格式 [ i for i in  if 条件]
格式 [ i if 条件 else 结果 for i in 迭代器]

'''

# list1 = []
# for i in range(1,21):
#     list1.append(i)
# print(list1)

# list1 = [i for i in range(1,21)]
# print(list1)
#
# list2 = [i+2 for i in range(10)]
# print(list2)


#将1-100之间所有的偶数存放在列表里面
# list1 = [i for i in range(0,101,2)]
# list1 = [i for i in range(0,101) if i%2==0]
# print(list1)

# list1 = ['62','hello','100','lucy']
# # list2 = [i for i in list1 if i.isalpha()]
# list2 = [i.title() if i.isalpha() and i.startswith('h') else i.upper() for i in list1 ]
#
# print(list2)

# list3 = []
# for i in range(1,10):
#     for y in range(1,10):
#         list3.append((i,y))
#
#
# list5 = [(i,y) for i in range(1,10) for y in range(1,10)  ]
# print(list3)
# print

a = [x for x in range(1,101)]
b = [a[i:i+3] for i in range(0,len(a),3)]
print(b)


