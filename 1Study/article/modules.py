class Article:
    def __init__(self, name):
        self.name = name

    def show(self):
        print('文章的名字是:{}'.format(self.name))


class Tag:
    def __init__(self, name):
        self.name = name