'''
全局变量和局部变量
global关键的添加
只有不可变的类型才需要加global
可变类型不需要添加global
可变类型:里面的内容发生了改变  但是地址没有发生改变 那么我们认为他就是可变类型
        类型:list dict set
不可变类型:当改变变量的值的时候  地址发生了改变，
    类型：int str float bool tuple

函数内部可以直接使用全局变量 但是不能直接修改全局变量
如果想修改全局变量  则必须使用关键字 global
'''

#小整数对象池子  默认存放的内存空间
# a = 100
# print(id(a))   #2297605197136
# a = 90
# print(id(a))   #2297605196816
#
# b = 'asdfas'
# print(id(b))   #2017597877936
# b = 'asdfa'
# print(id(b))   #2017597874672


# t1 = (1,2,3)
# print(id(t1))   #2048569336320
# t1 = (1,2,3,4)
# print(id(t1))   #2048568932880
#
#
# l1 = [1,2,3,4]
# print(id(l1))   #1887499969856
# l1.append(5)
# print(id(l1))   #1887499969856


# dict1 = {'1':'2'}
# print(id(dict1))  #1819234186880
# dict1['2'] = '3'
# print(id(dict1))  #1819234186880

islogin = False

def login(usename,passward):
    global islogin
    if usename == 'admin' and passward == '123':
        print('登录成功！')
        islogin = True
    else:
        print('用户名或者密码错误！')
        islogin = False


def borrow_books(bookName):
    # username = input('请输入用户名:')
    # password = input('请输入密码:')
    # if islogin(username,password):
    #     # print(f'成功借阅{bookName}')
    #     # print('成功借阅%s'%(bookName))
    #     print('成功借阅《{}》'.format(bookName))
    # else:
    #     print('还没有登录，不能借书！')
    if islogin:
        print(f'成功借阅{bookName}')
    else:
        print('用户还没有登录!')
        username = input('请输入用户名:')
        password = input('请输入密码:')
        login(username,password)

borrow_books('三国演义')
borrow_books('三国演义')