'''
函数里面变量加在的过程顺序  内层函数 -->  外层函数 --> 全局变量里面的变量  -->  系统里面的默认变量
嵌套:
闭包:  闭包 = 函数块+引用环境
    1.嵌套函数
    2.内部函数引用了外部函数的变量
    3.返回值是内部函数

闭包本身没有任何意义，只有在装饰器用的时候才有意义
'''


# 函数的嵌套
# def outer():
#     a = 100
#
#     # print('我是外部函数!')
#     # def inner():
#     #     b = 200
#     #     print('我是内部函数!')
#     # # result = locals()   # locals() 用来查看函数中所有局部变量的，以字段的形式来返回
#     # # print(result)   # {'a': 100, 'inner': <function outer.<locals>.inner at 0x00000169AB07ABF8>}
#     # print(a)
#     # inner()
#     def inner():
#         b = 200
#         # b += a    #内部函数可以使用外部函数的变量
#         nonlocal a  # 如果想修改外部函数的变量，需要在内部函数中添加 nonlocal
#         a += b  # 不能修改外部函数的变量
#         print('内部函数')
#     print(a)
#     inner()
#     print(a)
#
#
# outer()


def outer(n):
    a = 10

    def inner():
        b = a + n
        print('内部函数:', b)

    return inner


r = outer(5)
print(r)   # <function outer.<locals>.inner at 0x000002F5DF0BABF8>
r()  # 可以在外侧调用内部函数
