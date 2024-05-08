"""
文件夹 包
非py文件  包: py文件
一个包中可以存放多个模块
项目 > 包 > 模块 >  类|函数|变量

from 包 import 模块
from 包.模块 import 类|函数|变量
from 包.模块 import *

"""

# 使用包中的User类
# from article.modules import Article
#
# article = Article('张三')
# article.show()

# from article import modules
#
# article = modules.Article('张三')
# article.show()
#
# from user.modules import User
# user  = User('zhangsan','admin')
# user.login('zhangsan','admin')

# from user.modules import *
# print(version)  #包里面做了限制
# user  = User('zhangsan','admin')
# user.login('zhangsan','admin')


# 只要有模块的时候都会加载
# from user.modules import *
# from user.modules import version
# import user.modules
# import test

"""
__init__.py文件  只要导入包就会默认执行__init__里面的内容
默认加载到内存
要在flask里面会用到
使用:
1.当导入包的时候  把一些初始化的函数 变量 类定义在__init__.py中
2.此文件中函数 变量等的访问，只需要通过包名，函数...
3.可以结合__all__=['','']可以通过*访问到的模块
"""

# import user
# from user.modules import User
# user = User('张三')
# user.crete_app()
# user.printA()

"""
from 模块 import *  表示可以使用模块里面的所有内容，如果没有定义__all__所有的都可以访问到
        但是如果添加上了__all__  只能__all__=['','']列表中可以访问的
from 包 import * 表示包中内容 模块是不能访问的，就需要在__init__.py文件中定义
        __all__=['',''],可以通过*访问到的模块
"""
# from user import *
# user = modules.User('admin', '123')
# user.login('admin', '123')
#
# print(test.max)



'''
循环导入：大型的python项目中 需要很多的python文件 由于架构不当
可能会出现模块之间的相互导入,怎么解决这个问题呢？
解决办法:
    避免产生循环导入：
        1.重新架构
        2.可以在调用的时候把包放在调用的函数里面
'''