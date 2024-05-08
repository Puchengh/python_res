'''
语法异常都可以发现
真正的异常:在程序运行的时候报出来的异常  XXXError,导致程序不能正常运行下去
'''

# while True:
#     pass

# number = 1010
# def func():
#     global number
#     number += 1


# def chu(a, b):
#     return a / b
#
#
# chu(1, 0)   # ZeroDivisionError: division by zero
# print('------>')

# 异常处理
'''
try:
    pass  #可能出现异常的代码
except:
    pass #如果有异常会去执行的代码
finally:
    pass #无论是否存在异常都会执行的代码
    
情况1
    except 异常类型1:
        pass
    except 异常类型2:
        pass
所有的类型都是exception 都是继承与object
如果是多个exception，异常类型需要注意，最大的exception要放到最后

如果代码里面里面有return  但是有finally  也会继续执行下去，除了finally里面  其他的遇到了return  后面的代码后不会执行
finally不管怎么都后执行
'''

# def func():
#     sum1 = None
#     try:
#         n1 = int(input('输入第一个数字:'))
#         n2 = int(input('输入第二个数字:'))
#         # 加法
#         # per= input('请输入运算符号(+ - * /):')
#         sum1 = n1 + n2
#         print('sum是{}'.format(sum1))
#     except Exception as err:
#         print('报错了！', err)
#
#     # 报异常则才会执行这里
#     else:
#         pass
#     # 不管有没有异常 最后都会执行这里
#     finally:
#         print('你还是很有天赋的哦！')
#         # stream.close() 流的关闭也可以放在这个里面
#         print(sum1)
#
#
# func()

'''
抛出异常 raise 相当于java中的throw  抛出异常
注册 用户名必须是6位
'''


def register():
    username = input('输入用户名:')
    if len(username) < 6:
        raise Exception('用户名长度必须是六位以上!')
    else:   # 没有异常则会进入
        print('输入的用户名：', username)


try:
    register()
    # return 如果在这里返回  则不会进入到else里面
except Exception as err:
    print(err)
    print('注册失败!')
else:
    print('注册成功!')
