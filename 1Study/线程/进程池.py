"""
当需要创建的子进程不多的时候 可以直接利用 multiprocessing 中的Process动态生成多个进程
但是如果上百甚至上千个目标 手动的取创建进程的工作量比较巨大 此时就可以用到 multiprecessing 模块提供的Pool方法
初始化Pool时候 可以指定一个最大的进程池 当有新的请求提交到Pool中时 如果池子还没有满
那么就会创建一个新的进程用来执行该请求 但是如果池中的进程已经达到指定的最大值 那么该请求就会等待
知道池中有进程 才会创建新的进程来执行

1.阻塞式: （同步） 添加一个任务，如果一个任务不结束另外一个任务就进不来
2.非阻塞: （异步）全部添加到队列中, 立刻返回, 并没有等待其他的进程执行完毕，但是回调函数是等待任务完成之后才调用
    优点:
        1。尽可能使用机器的最大进程数量，不会因为同时启用过多进程而是的系统崩溃
        2. 实现进程的复用


pool = Pool(max)  创建进程池对象
pool.apply()  阻塞式
pool.applu_async()  非阻塞式的

pool.close()
pool.join()  让主进程让步，等待，等待子进程完成再执行
"""

# 创建线程池
from multiprocessing import Pool
import time
from random import random
import os


# # 非阻塞式
# def task(task_name):
#     print('开始做任务了!', task_name)
#     start = time.time()
#     # 使用sleep
#     time.sleep(random() * 2)
#     end = time.time()
#     # print('完成任务:{},用时{}!,进程id:{}!'.format(task_name,end-start,os.getpid()))
#     return '完成任务:{},用时{}!,进程id:{}!'.format(task_name, end - start, os.getpid())
#
#
# container = []
#
#
# def callback_func(n):
#     container.append(n)
#
#
# if __name__ == '__main__':
#     pool = Pool(5)
#     tasks = ['听音乐', '吃饭', '洗衣服', '打游戏', '散步', '看孩子', '做饭']
#     for task1 in tasks:
#         pool.apply_async(task, args=(task1,), callback=callback_func)  # 异步
#     pool.close()  # 添加任务结束
#     pool.join()  #
#
#     for i in container:
#         print(i)
#     print('over')


# 阻塞式
def task(task_name):
    print('开始做任务了!', task_name)
    start = time.time()
    # 使用sleep
    time.sleep(random() * 2)
    end = time.time()
    print('完成任务:{},用时{}!,进程id:{}!'.format(task_name, end - start, os.getpid()))
    # return '完成任务:{},用时{}!,进程id:{}!'.format(task_name, end - start, os.getpid())


container = []


def callback_func(n):
    container.append(n)


if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['听音乐', '吃饭', '洗衣服', '打游戏', '散步', '看孩子', '做饭']
    for task1 in tasks:
        pool.apply(task, args=(task1,))  # 同步
    pool.close()
    pool.join()
    print('over!!!!')
