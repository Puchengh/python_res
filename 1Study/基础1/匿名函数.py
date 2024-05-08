'''
用lambda关键词能创建小型匿名函数 这中函数省略了def声明函数的标准步骤
lambda 参数列表 运算表达式
'''


# def test(a):
#     return a+1
# print(test(1))
#
#
# r = lambda a: a+1
# print(r)
# print(r(2))


'''
匿名函数的使用场景 作为参数来使用  只是为了简单和方便
'''

# def test():
#     print('----test------')
#
# def func(a,f):
#     print('a---->',a)
#     f()
#
# func(5,test)
# print('-'*97)
#
# def func1(a,f):   #类似r = lambda a: a+1
#     print('a---->',a)
#     r = f(a)
#     print(r)

# func1(8,lambda a:a ** 2)


'''
系统高阶函数
高阶函数：函数也是一种数据类型   function 可以把他当成一个变量来使用
        一个函数的参数是另一个函数  高阶函数
系统高阶函数:  stored函数  filter  map reduce
'''

# r = max(5,9)
# print(r)
#
# r = max([1234,1234,63456,345634,56])
# print(r)
#
# list1 = [('tom',9),('danney',3111),('rose',445)]
# print(max(list1,key=lambda x:x[1]))
# print(min(list1,key=lambda x:x[1]))
# #排序
# print(sorted(list1, key=lambda x:x[1], reverse=True))

#filter的匿名函数 要求返回值必须是bool类型的  只有bool结果为true才是符合过滤条件的
# list1 = [('tom',9),('danney',3111),('rose',445)]
# rr = filter(lambda x: x[1] > 555,list1)
# print(list(rr))


#通过匿名函数提取list1中符合的内容，并对内容进行加工
# list1 = [('tom',9),('danney',3111),('rose',445)]
# aa = map(lambda x:x[0].upper(),list1)
# print(list(aa))

#这个函数已经没有了 就是所有值相加
# r = reduce(lambda x, y :x+y,[1,2,3,4])
# print(r)

r = zip('asdfasdf','1234567489765456')
print(list(r))

