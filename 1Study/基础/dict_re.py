'''
字典定义
'''

# list1=[]
# list1.append('价格')

# dict1 = {'name': 'puchen', 'age': 28, 1: ('1', 2), 'score': 99}
# print(dict1)


# dict1['list'] = list1
# print(dict1)
# print(dict1.get(1))
# print(dict1[1])


# clear() 清空数据
# pop(key) 取消这个键值对
# r = dict1.pop(2)  # 找不到这个key也会报错
# print(r)
# print(dict1)


# popitem()  从后往前删除 返回值是（key，value）
# r = dict1.popitem()
# print(r)
# print(dict1)

# del dict1   # 直接删除这个元组的定义
# print(dict1)
# del dict1['name']   # 找不到这个key也会报错
# print(dict1)


# books = [
#          {'书名': '钢铁是怎样练成的', '价格': 28.5, '作者': '列夫托尔斯泰', '出版社': '中国人名出版社'},
#          {'书名': '复活', '价格': 28.5, '作者': '雨果', '出版社': '中国人名出版社'}
#         ]
# books1 = books
# # 书名 价格 作者 出版社
# for book in books:
#     book.pop('出版社')
# print(books)
# print(books1)
#
# print(id(books))
# print(id(books1))

# for i in range(len(books)):
#     books[i].pop('出版社')
#
# print(books)

book = {'书名': '《复活》', '价格': 28.5, '作者': '雨果', '出版社': '中国人名出版社'}
# print(book.get('作者', '《钢铁是怎样练成的》'))  # 可以给一个默认值，根据key获取value的值  如果get(key)里面的key不存在则会返回 None
# print(book['1'])   如果找不到用报错Error，默认值
# print(len(book))

# list1 = [1, 4, 7, 8, 9]
# for i in list1:
#     print(i)


'''
如果使用for in 直接遍历字典，取出的是字典的key
book.values() 这样可以获取到value
print(tuple(book.values()))
print(list(book.values()))

print(tuple(book.keys()))
print(list(book.key()))
'''

# for i in book:    #普通的循环
#     print(book.get(i))

# for i in book.values():   # 加强for循环
#     print(i)

# print(tuple(book.values()))
# print(list(book.values()))
#
# print(tuple(book.keys()))
# print(list(book.keys()))

# for i in book.items():
#     print(i)
# print(book.items())


'''
非常使用的一种方式   book.items()把key value变成了元组
'''
# print()
# for k,s in book.items():
#     print(k,end=' ')
#     print(s)
# print(book)


# book.setdefault('厚度','1.1mm')
# book.setdefault('厚度','1.2mm')   #只能新增  不能修改
# print(book)

# book1 = {'1111':'1111', '作者':'111'}
#
# book.update(book1)   #更新相加
# print(book)

# print(book.fromkeys(['q','b'],10))  #构建一个新的字典 结果是 {'q': 10, 'b': 10}



