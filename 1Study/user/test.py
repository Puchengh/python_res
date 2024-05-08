"""
用户发表文章
创建用户对象
发表文章 文章对象
"""
# User 对象
# from modules import User # 当前目录下面的modules下的User类
# # from user.modules import User
# from article.modules import Article
# user  = User('admin','123456')   # user就是通过导入User类创建的
#
# #发表文章 文章对象
# article  = Article('个人总结')
#
# user.public_article(article)

# from test import add   # 不能导入相同名不同 路径的包   这个代码就会报错
# add()

from study.test1 import add   # 这个代码正确执行
add()

max = '123456'