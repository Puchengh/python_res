"""
开发模式:
单例模式 无论在创建对象的时候 创建的是同一个地址
"""


class Singleton:
    # 私有化示例  单例的地址就存在于__instance
    __instance = None
    name = 'Jack'

    # 重写父类的__new__方法,阻止__new__产生新的对象地址
    def __new__(cls):
        print('---new')
        if cls.__instance is None:
            # cls.__instance = super().__new__(cls)
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def show(self):
        print('--------->', Singleton.name)


s = Singleton()
s1 = Singleton()
# s2 = Singleton()

print(dir(Singleton))

print(s)
print(s1)

s.show()
s1.show()
