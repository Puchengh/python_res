"""
继承
重写父类的方法, (函数方法同名)，先找调用的类，然后才会去找父类

特点：
    1.如果类中不定义__init__，调用父类 super class的__init__
    2.如果类继承父类也需要定义自己的__init__  就需要在当前类的__init__调用一下父类__init__
    3.如何调用父类的__init__：
        super().__init__(参数)
        supers(类名，对象).__init__(参数)
    4.如果父类有eat()  子类也定义了一个方法eat方法  默认搜索原则,先找当前类，再去找父类
        s.eat()
        override: 重写(覆盖)
        父类提供的方法不能满足子类的需求，就需要在子类中定义一个同名的方法 这种行为就是：重写

        super().方法名(参数) 先调用父类的方法
"""

class Person:
    def __init__(self, no, name, salary):
        self.no = no
        self.name = name
        self.salary = salary

    def __str__(self):
        msg = '工号是：{} ，姓名是：{} ，工资是{}'.format(self.no, self.name, self.salary)
        return msg

    def getSalary(self):
        return self.salary

class Worker(Person):
    def __init__(self, no, name, salary, hours, per_hour):
        super().__init__(no, name, salary)
        self.hours = hours
        self.per_hour = per_hour

    def getSalary(self):
        monery = self.hours * self.per_hour
        monery += self.salary
        return monery

class Saleman(Person):
    def __init__(self,no, name, salary, salemoney, percnet):
        super().__init__(no, name, salary)
        self.salemoney = salemoney
        self.percnet = percnet

    def getSalary(self):
        monery = self.salemoney * self.percnet
        monery += self.salary
        return monery

# 创建对象
worker = Worker('001', 'king', 2000, 160, 50)
month_worker = worker.getSalary()
print('worker的月薪是:', month_worker)
print(worker)

saleman = Saleman('002', 'lucy', 5000, 50000000, 0.003)
month_saleman = saleman.getSalary()
print('saleman的工资是：', month_saleman)   0.

print(saleman)