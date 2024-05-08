"""
#is a base class
继承
 Student Employee Doctor  ---> 都属于人类
 相同的代码  -- 代码冗余  可读性不高
 将相同代码提取  继承 Person

class Student(Person):
"""


# class Person:
#     # def __init__(self, name, age):
#     #     print('------->person的init')
#     #     self.name = name
#     #     self.age = age
#
#     def __init__(self, name):
#         print('------->person的init')
#         self.name = name
#         self.age = 18
#
#     def eat(self):
#         print(self.name + '正在吃饭...')
#
#     def run(self):
#         print(self.name + '正在跑步...')
#
#
# class Student(Person):
#     def __init__(self, name):
#         print('------->student的init')
#
#         # 调用父类的__init__方法  super() 表示父类对象
#         super().__init__(name)
#
#
# class Employee(Person):
#     pass
#
#
# class Doctor(Person):
#     pass
#
#
# # s = Student('张三', 25)
# # e = Employee('李四', 21)
# # d = Doctor('王五', 24)
#
# # s.run()
# # e.run()
# # d.run()
# # s.eat()
# # e.eat()
# # d.eat()
#
# # if __name__ == '__main__':
# #     s.run()
# #     e.run()
# #     d.run()
# #     s.eat()
# #     e.eat()
# #     d.eat()
#
# s = Student('jack')
# s.run()



class Person:
    def __init__(self, name, age):
        print('------->person的init')
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃饭...')

    def run(self):
        print(self.name + '正在跑步...')


class Student(Person):
    def __init__(self, name, age, glazz):
        print('------->student的init')
        super().__init__(name, age)
        self.glazz = glazz


class Employee(Person):
    pass


class Doctor(Person):
    pass