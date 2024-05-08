"""
1.单核CPU实现多任务原理: 操作系统轮流执行多个任务
2.多核cpu实现多任务原理: 真正的秉性执行多任务只能在多核cpu上实现  但是由于任务数据远远多于cpu的核心数量  所以 操作也会自动吧很多任务轮流调度到每个核心上执行

并发和并行：
并行(parallel)：指在同一时刻，有多条指令在多个处理器上同时执行。所以无论从微观还是从宏观来看，二者都是一起执行的。
并发(concurrency)：指在同一时刻只能有一条指令执行，但多个进程指令被快速的轮换执行，使得在宏观上具有多个进程同时执行的效果，但在微观上并不是同时执行的，只是把时间分成若干段，使多个进程快速交替的执行。

协程的底层是通过yeild通过交替进行的

进程
    优点:
        稳定性高 一个进程奔溃了 不糊影响其他进程
    缺点:
        创建进程开销巨大
        操作系统能同事运行进程数据有限

Process(target=函数名,name=进程的名字,args=(给函数传递的参数))
Process.start()  启动进程并且执行任务
Process.run()  只是执行了任务  但是没有启动进程
terminate()  终止
"""
import os
from multiprocessing import Process
from time import sleep

# # 创建进程
# def task1():
#     while True:
#         sleep(1)
#         print('这个是任务1。。。。。。。。。。。',os.getpid(),'-----',os.getppid())
#
#
# def task2():
#     while True:
#         sleep(2)
#         print('这个是任务2。。。。。。。。。。。',os.getpid(),'-----',os.getppid())
#
#
# if __name__ == '__main__':
#     print(os.getpid())
#     # 子进程
#     p1 = Process(target=task1,name='任务1')
#     # p1.run()   # 线程执行一次这个动作
#     p1.start()
#     print(p1.name)
#     p2 = Process(target=task2,name='任务2')
#     # p2.run()   # 线程执行一次这个动作
#     p2.start()
#     print(p2.name)
#     print('----------------------------')
#     print('****************************')


# # 创建进程
# def task1(tims_s,s):
#     while True:
#         sleep(tims_s)
#         print('这个是任务1。。。。。。。。。。。',os.getpid(),'-----',os.getppid(),s)
#
#
# def task2(tims_s,s):
#
#     while True:
#         sleep(tims_s)
#         print('这个是任务2。。。。。。。。。。。',os.getpid(),'*****',os.getppid(),s)
#
# number = 1
# if __name__ == '__main__':
#     print(os.getpid())
#     # 子进程
#     p1 = Process(target=task1,name='任务1',args=(1,'aa'))
#     # p1.run()   # 线程执行一次这个动作
#     p1.start()
#     print(p1.name)
#     p2 = Process(target=task2,name='任务2',args=(2,'bb'))
#     # p2.run()   # 线程执行一次这个动作
#     p2.start()
#     print(p2.name)
#
#     while True:
#         number += 1
#         sleep(0.1)
#         if number == 100:
#             p1.terminate()
#             p2.terminate()
#             break
#         else:
#             print(number)
#     print('----------------------------')
#     print('****************************')


# # 创建进程
# m = 1   # 不可变类型
# list1=[]   # 可变类型
#
# def task1(tims_s, s):
#     while True:
#         sleep(tims_s)
#         global m
#         m += 1
#         list1.append(str(m) + 'task1')
#         print('这个是任务1。。。。。。。。。。。', os.getpid(), '-----', os.getppid(), s, m, list1)
#
#
# def task2(tims_s, s):
#     while True:
#         sleep(tims_s)
#         global m
#         m += 1
#         list1.append(str(m) + 'task2')
#         print('这个是任务2。。。。。。。。。。。', os.getpid(), '*****', os.getppid(), s, m, list1)
#
#
# number = 1
# if __name__ == '__main__':
#     print(os.getpid())
#     # 子进程
#     p1 = Process(target=task1, name='任务1', args=(1, 'aa'))
#     p1.start()
#     p2 = Process(target=task2, name='任务2', args=(2, 'bb'))
#     p2.start()
#
#     print('----------------------------')
#     print('****************************')
#
#     while True:
#         sleep(1)
#         m += 1
#         print('-----', m)


""""
自定义进程
"""

from multiprocessing import Process


class MyProcess(Process):

    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name
    # 重写run方法
    def run(self):
        n = 1
        print('进程的名字:' + self.name)
        while True:
            print('{}----------自定义进程:{}'.format(n, self.name))
            n += 1


if __name__ == '__main__':
    p1 = MyProcess('小小')
    p1.start()
    p2 = MyProcess('大大')
    p2.start()
