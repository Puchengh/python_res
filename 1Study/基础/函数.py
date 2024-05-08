# 封装重复的内容
import random


# 生成验证码 函数部分
def generate_code(n):
    code = 'qwertyuiopasdfghjklzxcvbnm123456789'
    code_result = ''
    for i in range(n):
        code_chart = random.choice(code)
        code_result += code_chart
    print(code_result)


# 加函数才能表名你需要调用这个函数  如果不加括号则能获取函数的内存块的地址
# print(generate_code)
# print(generate_code)
# generate_code(5)

'''
参数
    1 无参数
def 函数名()
    pass
    2 有参数
def 函数名(参数1，参数2)
    pass
    
默认值参数：在定义函数的时候  有一个或者多个参数赋值。 调用的时候默认可以给也可以不用给参数
定义函数的时候，默认的参数必须要位于普通参数之后
设置默认值参数的时候可以使用关键字参数赋值  boorow_book('2', 2, school = '北科')

'''


def get_sum(a, b, isremember=False):
    print('函数中:', a, b)
    if isinstance(a, int) and isinstance(b, int):
        s = a + b
        print(s)
    else:
        print('类型不一致')


# get_sum(2, 3)


library = ['mysql', 'python', 'java']

# 形参
# def add_book(bookname):
#     library.append(bookname)
#     print('图书添加成功!')
#
#
# def show_baook(books):
#     for book in books:
#         print(book)
#
#
# # 列表传的是地址
# add_book('english')
# show_baook(library)


list1 = [23, 45, 56, 89]

# def get_list(list2):
#     # new_list = []
#     # for e in list1:
#     #     if e > 50:
#     #         new_list.append(e)
#     # print(new_list)
#
#     new_list = [e for e in list1 if e >= 50]
#     print(new_list)
#
#
# get_list(list1)


# def remove_from_list(list2):
#     # for e in list2:
#     #     if e <= 50:
#     #         list1.remove(e)
#     # print(list2)
#
#     n = 0
#     while n < len(list2):
#         if list2[n] < 50:
#             list2.remove(list2[n])
#         else:
#             n += 1
#
#     print(list2)
#
#
# remove_from_list(list1)
# print(list1)
'''
可变参数   *args  **kwargs
拆包和装包 

拆包和装包在函数过程中
形参*args 对应的是装包的过程
调用参数*args 对应的是拆包的过程 里面是列表|元组|set的类型
'''

# def get_sum1(*args):
#     print(args)
#
#
# get_sum1(1, 2, 23, 4)  # 打出来的就是一个元组 函数存放是一个元组
#
# a, b, *c = 12, 3, 4, 5, 67, 4   #装包
# print(a)
# print(b)
# print(c)   # 这里打出来是一个列表 变量里面是一个列表


'''
**kwargs接受的是一个字典 
所以函数在调用的时候必须要使用关键字参数餐可以转换成key value的形式

'''

# def get_sum1(**kwargs):
#     print(kwargs)  # 字典
#     for k, v in kwargs.items():
#         print(k, v)
#
#
# # get_sum1(bookname='西游记', author = '吴承恩')
# book = {'bookname': '西游记', 'author': '吴承恩'}
# get_sum1(**book)


'''
可变参数
*args **kwargs
argments

'''

# def show_book(*args, **kwargs):
#     print(args)  # () 元组
#     print(kwargs)  # {} 字典
#
#
# book = {'bookname': '西游记', 'author': '吴承恩'}
# # show_book('龙少', '小芳', **book)
# student = ['龙少', '小芳']
# show_book(*student, **book)


'''
函数的返回值
def 函数名(参数)：
    pass
    return XXXXXXXXX
    
:return后面的值可以是多个值，也可能是一个值
如果是多个值，其实返回的是一个元组，可以经过拆包赋值给每个变量
'''


# def get_sum(*args):
#     total = 0
#     for i in args:
#         total += 1
#     return total, args
#
#
# print(get_sum(1, 2, 3, 4))  # 返回值  (4, (1, 2, 3, 4))


#冒泡排序
# def get_maxadmin(numbers):
#     for i in range(0,len(numbers) - 1):
#         for j in range(0,len(numbers) - 1 - i):
#             if numbers[j] > numbers[j+1]:
#                 numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#     print(numbers)
#
#
# list1 = [23, 42345, 12, 35, 7, 8453, 546]
# get_maxadmin(list1)


def get_maxadmin(numbers):
    for i in range(0,len(numbers) - 1):
        for j in range(0,len(numbers) - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    min  = numbers[0]
    max = numbers[-1]
    return min,max


list1 = [23, 42345, 12, 35, 7, 8453, 546]
d = get_maxadmin(list1)
a,b = get_maxadmin(list1)

print(d)
print(a,b)


# for i in range(2):
#
#     print(i)
#
# print('-'*20)
# for i in range(0,2):
#     print(i)

# list1  = list(range(2))
# list2  = list(range(0,2))
#
# for i in list1:
#     print(list1[i])
#
#
# for i in list2:
#     print(list1[i])
# print(list1)
# print(list2)