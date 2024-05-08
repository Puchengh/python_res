"""
在Python中 模块是代码组织的一种方式 把功能相近的函数或者类放到一个文件中，一个文件(.py)就是一个模块（module）
模块名称就是文件名去掉后缀 .py 这样做的好处是：
    提高代码的可重复用,可维护行。一个模块编写完毕后，可以很方便的在其他项目中导入
    解决了命名冲突，不同模块中相同的命名不会冲突

builtins  内置函数默认加载
math      数学库
random    生成随机数
time      时间
datetime  日期和时间
calender  日历
hashlib   加密算法
copy      拷贝
functools 常用的工具
os        操作系统接口
re        字符串正则匹配
sys       python自身的运行环境
multiprocessing  多进程
threading 多线程
json      编码和解码 json对象
loggin    记录日志,调试

1. 自定义模块
2. 系统模块
    # 导入模块
        1.import 模块名
            模块名.变量 模块名.函数  模块名.类
        2. from 模块名 import 变量 | 函数 | 类  可以省略包名调用
        3. from 模块名 import * 的方法去导入
            该模块中素有的内容
            但是如果像限制获取的内容 可以在模块中使用 __all__ = [使用*可以访问到的内容]
        4. 无论是import还是from的形式，加载所有的模块到函数中
            如果不希望对调用的语句，则需要使用到
            if __name__ == '__main__':
                print(__name__)  # __name__
                test()
            执行自身模块 __name__ 叫 __main__
            在其他模块中通过引入的方式调用的：  __name__ :就是他的模块名
"""



# import random
# import test
# list1 = [1, 2, 3, 4, 5, 6]
#
#
# # 使用模块中的函数  模块名.变量 模块名.函数  模块名.类
# # 导入模块
# print(test.add(*list1))




# from test import add
# from test import minus
# list1 = [1, 2, 3, 4, 5, 6]
# print(add(*list1))
# print(minus(1,2))