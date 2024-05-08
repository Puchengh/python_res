'''
递归函数
如果一个函数在内部不调用其他的函数 而是自己本身的话 这个函数就是递归函数
遵循：
1.要有结束条件
2.每次递归都要靠近结束条件
'''

# def test():
#     print('--------test----------')
#     a()
#
# def a():
#     print('-------aaaa-------')
#     a()

#1-10  打印数据
def test(i):
    if i == 10:
        print('10')
    else:
        print(i)
        i+=1
        test(i)

test(1)


#1-10  累计和
# sum=0
# def test1(i):
#     if i <= 10:
#         global sum
#         sum+=i
#         i+=1
#         test1(i)
#
#
# test1(1)
# print(sum)


def test1(i):
    if i == 5:
        return 5
    else:
        return i + test1(i + 1)
r = test1(1)
print(r)
#斐波那契数列