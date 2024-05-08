'''
面向对象
对象  --> 具体的事物

涉及的名词: 类 对象 方法 属性
所有类名要求首字母大写 多个单词使用驼峰命名法
既有特征  又有动作 才是一个完整的类
'''

# 定义类
# class Phone:
#
#     # 类属性
#     brand = 'huawei'
#     price = 4999
#     type = '15'
#
#     #方法
#
#
# # 使用类创建对象
# # yp = Phone()  #yp 是对象名
# # print(yp.brand)
# # yp.brand = 'ipone'   # 对象属性 赋值操作只会作用到对象的内存空间里面
# # print(yp.brand)  # 在调用的时候 先找自己空间的  然后再去他的类属性中去找
# #
# # Phone.brand = 'android'  # 修改类的属性
# #
# # print(Phone.brand)
#
# phone = Phone()
# print(phone.brand)


'''
普通方法
类方法
魔术方法

'''

# class Phone():
#
#     brand = 'huawei'
#     price = 4999
#     type = '15'
#
#     # Phone类方法
#     def call(self):
#         print(self)
#         print('打电话....')
#         print('留言', self.note)
#         print('访问address_book')
#         for person in self.address_book:
#             print(person.items())
#
#
#
# phone = Phone()
# phone.note = '我是phone的note'
# phone.address_book = [{'123456789':'小李'},{'978654321':'小张'}]
# print(phone,'----1----')
# phone.call()
#
# phone1 =Phone()
# phone1.note = '我是phone1的note'
# phone1.address_book = [{'123456789':'小李'},{'978654321':'小张'}]
# print(phone1,'----2----')
# phone1.call()


# def func(names):
#     for name in names:
#         print(name)
#
#
# name_list = ['aa', 'bb', 'cc']
# func(name_list)


# class Phone():  # 公共的特征和动作
#     # 魔术方法 定义： __名字__()
#     def __init__(self):  # 初始化
#         print('----------init')
#         # 动态给self空间里面添加brand，price
#         self.brand = 'xiaomi'
#         self.price = 4999
#
#     def call(self):
#         print('-----call')
#         print('price', self.price)


# print(Phone.price)  # 类里面没有这个属性 会报错

# p = Phone()
# 1.有没有一块空间是不是Phone()
# 2.利用Phone类，向内存申请一块Phone一样的空间  0X78626nbac
# 3.去Phone中检查__init__()  如果没有 则执行将开辟内存给到对象p，地址才给到p。  如果有__init__() 则会进入init方法里面执行动作，才会执行将开辟内存给到对象p，地址才给到p。
# p.call()   #p.call()  p就是一块地址


'''
类方法
    特点: 
    1.定义需要依赖装饰器 @classmethod
    2.类方法中参数不是一个对象，而是类的地址
    3.类方法中只可以使用类属性
    
除了类方法， 类中方法的调用要通过self.test()  方法名

类方法的作用:
因为只能访问类属性和类方法，所以在对象创建之前，如果需要完成一些东西，则要把它放在类方法里面
'''

# class Dog:
#     nickname = '天使'
#
#     def __init__(self, nickname):
#         self.nickname = nickname
#
#     def run(self):  # 对象的方法
#         print('{}在院子里面跑'.format(self.nickname))
#
#     @classmethod  # 类方法
#     def test(cls):  # cls class 指的是类的地址
#         print(cls)
#         print(cls.nickname)
#
#
# d = Dog('大黄')
#
# d.run()
# d.test()


# class Person:
#     __age = 18
#
#     def show(self):
#         print('---', Person.age)
#     @classmethod
#     def test(cls):
#         cls.__age = 20
#         print('------类方法')
#
#     @classmethod
#     def show_age(cls):
#         print('修改后的年龄是',cls.__age)
#
#
# Person.test()
# Person.show_age()


'''
静态方法，很类似类方法
1.需要装饰器 @staticmethod
2.静态方法是无需传递参数的 cls self
3.也只能访问类的属性和方法，对象的是无法访问的
4.加载的时机同类方法  在类加在的时候就存在了

类方法和静态方法
不同
    1.装饰器不同
    2.类方法有参数 静态方法没有参数
相同 
    1.只能访问类的属性和方法，对象的是无法访问的
    2.都可以通过类名调用和访问
    3.都可以在创建对象之前使用，因为是不依赖与对象
    
普通方法和两者的区别
不同
    1.没有装饰器
    2.普通方法永远是要依赖对象，因为每个普通方法都有一个self
    3.只有创建了对象才能调用普通方法，否则无法调用
'''

# class Person:
#     __age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#
#     def show(self):
#         print('---', Person.age)
#     @classmethod
#     def test(cls):
#         cls.__age = 20
#         print('------类方法')
#
#     @classmethod
#     def show_age(cls):
#         print('修改后的年龄是',cls.__age)
#
#     @staticmethod
#     def test1():
#         print('------静态方法')
#         print(Person.__age)
#
#
# Person.test()
# Person.show_age()
# Person.test1()


# class Cat:
#     type = '猫'
#
#     # 通过__init__初始化的特征
#     def __init__(self, nickname, age, color):
#         self.nickname = nickname
#         self.age = age
#         self.color = color
#
#     # 动作和方法
#     def eat(self, food):
#         print('{}喜欢吃{}'.format(self.nickname, food))
#
#     def catch_mouse(self, color, weight):
#         print('{}, 抓了一直{}kg的，{}的大老鼠'.format(self.nickname, weight, color))
#
#     def sleep(self, hour):
#         if hour < 5:
#             print('怪怪！继续睡一会吧！')
#         else:
#             print('快点起床抓老鼠去！')
#
#     def show(self):
#         print('猫的详细信息:')
#         print(self.nickname, self.age, self.color)
#
#
# # 创建对象，在 内存中开了一个空间 绑定了一块地址
# cat1 = Cat('花花', 2, '灰色')
#
# # 通过对象调用方法
# cat1.catch_mouse('黑色', 2)
#
# cat1.sleep(8)
#
# cat1.eat('小金鱼')
#
# cat1.show()


'''
总结
多态 封装  继承
    封装 就是属性私有化，私有化属性，定义共有的get和set方法
    继承 就子类可以调用父类方法
    多态 
    
所有的类都是大类型  实例或者子类都属于小类型
'''


class Person:
    role = 'Pet'

    def __init__(self, name):
        self.name = name

    def feed_pet(self, pet):  # pet既可以接收cat 也可以接收dog  还可以接收tigger

        # isinstance(obj, 类) 判断obj是不是类的对象 或者判断onj是不是这个类子类的对象
        if isinstance(pet, Pet):  # 类型没有强定义  如果需要的话则要加判断
            print('可以养宠物！')
            print('{}喜欢养宠物:{},昵称是:{}'.format(self.name, pet.role, pet.nickname))
        else:
            print('不是宠物类型的!')


class Pet:
    role = '宠物'

    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def show(self):
        print('昵称{}年龄{}'.format(self.nickname, self.age))


class Cat(Pet):
    role = '猫'

    def catch_mouse(self):
        print('抓老鼠！')


class Dog(Pet):
    role = '狗'

    def watch_house(self):
        print('看家高手...')


class Tigger:
    def eat(self):
        print('可以吃人!')


# 创建对象
cat = Cat('花花', 1)

dog = Dog('大黄', 4)

person = Person('jiawei')

tigger = Tigger()

person.feed_pet(cat)
person.feed_pet(tigger)
