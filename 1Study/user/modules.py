__all__ = ['User']

version = '1.1'

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if username == self.username and password == self.password:
            print('登录成功')
        else:
            print('登录失败')
    def public_article(self, article):
        print(self.username,'发表了文章：',article.name)
if __name__ == '__main__':
    print('----user----')