'''
列表推导式  []  集合推导式  {}
生成器  ()

还可以使用函数完成生成式

只要函数中出现了这个关键字  那么就是生成器
'''

# 得到生成器
# g = (x*3 for x in range(20))   #如果查出范围 取值的话会报错stopiteration 抛出异常
# print(type(g))  # <class 'generator'>   只有调用的时候才会产生数据  不会占用内存
# print(g)   # <generator object <genexpr> at 0x000001DFCD18B8B8>
#
# # 通过调用__next__()得到生成器的内容  系统自带的
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# 斐波那切数列
'''
1.定义一个函数 函数中要使用yeild 关键字
2.调用函数，接收调用的结果 就是一个生成器
'''
# def func():
#     n = 0
#     while True:
#         n+=1
#         yield n   # yeild其实就是相当于return + 暂停 不在继续执行了
#         # print(n)
# g = func()
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# g.close()   # 关闭流
# print(g.__next__()) #抛出异常 StopIteration


# def fib(length):
#     a, b = 0, 1
#     n = 0
#     while n < int(length):
#         # print(b)
#         yield b   #暂停必须是结果的数据
#         a, b = b, a+b
#         n+=1
#     return '没有更多的元素了!'   #return在得到StopIteration后的提示信息
#
# g = fib(8)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


'''
生成器方法:
    __next__() ：获取下一个元素
    send(var) 方法 :第一次调用 必须传一个空值
'''

# def gen():
#     i = 0
#     while i < 5:
#         temp = yield i   # return 0 + 暂停
#         print('temp:', temp)
#         for i in range(temp):
#             print('--------->', i)
#         i+=1
#     return '没有更多的元素了'
#
# g = gen()
# print(g.send(None))   # 第一次调用 必须传一个空值
# # n1 = g.send('呵呵')
# n1 = g.send(3)
# print('n1', n1)
# # n2 = g.send('哈哈')
# # print('n1', n2)


'''
生成器的应用
    进程 线程  协程
可以多个协程之间交替进行
'''


def task1(n):
    for i in range(n):
        print('正在搬第{}块砖'.format(i))
        yield


def task2(n):
    for i in range(n):
        print('正在听第{}首歌'.format(i))
        yield


g1 = task1(3)
g2 = task2(3)
#
# g1 = task1(5)
# g2 = task2(5)

while True:
    try:
        # g1.__next__()
        # g2.__next__()
        next(g1)
        next(g2)
    except:
        break

'''
生成器 generator
定义生成器的方式
    1.通过列表推导式
     g = (x+1 for x in range(6))
    2.函数+yeild
     def func():
        ....
        yeild
     g = func()
     
产生元素:
    g.__next__()  生成器自己的方法调用，如果元素产生完毕 再次调用就会产生异常
    g.send(value)  可以控制循环的产生
    g = func() ,next(g)
    
'''
