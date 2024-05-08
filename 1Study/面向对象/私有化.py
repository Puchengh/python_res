'''
变量私有化
    封装: 1.私有化属性  2.定义共有set 和get 方法
    __属性： 将属性私有化，访问范围仅仅限于类中
    优点:
        1.颖仓属性不被外界随意修改
        2.也可以修稿  通过函数修改
        3.筛选复制的内容，可以加if判断
        4.如果像获取具体的某一个属性
            使用get函数
'''

# class Student:
#     __age = 18  # 类属性
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         self.__score = 59
#
#     # 定义共有set和get方法
#     # set是为了赋值
#     def setAge(self, age):
#         if age > 0 and age <= 120:
#             self.__age = age
#         else:
#             print('必须在0-120岁之间!')
#
#     def setName(self, name):
#         if len(name) == 6:
#             self.__name = name
#         else:
#             print('名字长度不是六位！')
#
#     # get是为了取值
#     def getAge(self):
#         return self.__age
#
#     #
#     def __str__(self):
#         return '姓名:' + self.__name + ',年龄:' + str(self.__age) + ',考试分数:' + str(self.__score)
#
#
# s = Student('张三', 10)
# #
# # s.setAge(56)
# # s.setName('admin1')
# # print(s)
#
# print(dir(Student))
# print(dir(s))
# print(s.getAge())
# # print(s._Student__age)  # 其实他就__age 只不过是系统在查询的时候改成了_Student__age
#
#
# print(__name__)


'''
开发中私有化的处理
'''

# class Student:
#     __age = 18  # 类属性
#
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     # def setAge(self, age):
#     #     if age > 0 and age <= 120:
#     #         self.__age = age
#     #     else:
#     #         print('必须在0-120岁之间!')
#     # def getAge(self):
#     #     return self.__age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if 0 < age <= 120:
#             self.__age = age
#         else:
#             print('必须在0-120岁之间!')
#
#     # 要定义property首先要定义get方法  然后再定义set方法
#
#     def __str__(self):
#         return '姓名:' + self.__name + ',年龄:' + str(self.__age)
#
#
# s = Student('cp', 20)
# s.name = 'xiaopeng'
# print(s.name)
#
# s.age = 15
# print(s.age)
# # s.setAge(50)
# # print(s.getAge())


import random


class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):
        ran_time = random.randint(1, 10)
        msg = '{}品牌的车在{}上以{}速度行驶了{}小时'.format(self.brand, road.name, self.speed, ran_time)
        print(msg)

    def __str__(self):
        return '{}品牌的车，速度是{}'.format(self.brand, self.speed)


r = Road('京藏高速', 12000)
c = Car('宝马', '15KM/1h')

r.name = '深陕高速'
print(c)
c.get_time(r)
print(c)

# is a 和has a的关系，继承和从属的关系
