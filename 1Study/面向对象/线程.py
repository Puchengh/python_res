"""
锁

lock = threading.Lock()  拿到锁的对象
lock.acquire()  # 阻塞  全局解释器的锁
中间做动作
lock.release()  # 释放锁

只要不释放其他的线程 都无法进入运行状态  会降低速度

"""
#
# import threading
# import random
# import time
#
# lock = threading.Lock()
#
# list1 = [0] * 10
#
#
# def task1():
#     # 获取线程锁，如果已经上锁 则等待锁的释放
#     lock.acquire()  # 阻塞  全局解释器的锁
#     for i in range(len(list1)):
#         list1[i] = 1
#         print('放入{}'.format(i))
#         time.sleep(0.5)
#     lock.release()  # 释放锁
#
#
# def task2():
#     lock.acquire()
#     for i in range(len(list1)):
#         print('---->', i)
#         time.sleep(0.5)
#     lock.release()  # 释放锁
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=task1)
#     t2 = threading.Thread(target=task2)
#
#     t2.start()
#     t1.start()
#
#     t2.join()
#     t1.join()
#
#     print(list1)

"""
死锁
deadline 
避免死锁  尽管死锁很少发生 一旦发生就会造成应用的停止相应 程序不做任何事情
资源先后顺序出错

出现了该怎么解决：
1.重构代码 
2.在acquire() 加一个timeout参数
"""

from threading import Thread, Lock
import time

lockA = Lock()
lockB = Lock()


class MyThread(Thread):
    def run(self) -> None:
        if lockA.acquire():  # 如果获取到锁返回true
            print(self.name + "获取了A锁")
            time.sleep(0.1)
            if lockB.acquire():
                print(self.name + "获取了B锁,原来还有A锁")
                lockB.release()
            lockA.release()


class MyThread1(Thread):
    def run(self) -> None:
        if lockB.acquire():  # 如果获取到锁返回true
            print(self.name + "获取了B锁")   # 自定义锁名称
            time.sleep(0.1)
            if lockB.acquire(timeout=2):   # 阻塞
                print(self.name + "获取了A锁,原来还有B锁")
                lockA.release()
            lockB.release()


if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread1()

    t1.start()
    t2.start()


"""
线程 Thread
1.创建线程:
    Thread(target=cun, name='', args={}, kwargs={})
        t.start()---> 就绪状态
        
        run()
        join()
        
    自定义线程
     class MyThread(Thread):
        def __init__(self):
            pass
        def run(self):
            pass
     t = Thread()
     t.start
    
2.数据共享
    进程的共享数据和线程共享数据:
        进程是每个进程中都有一份
        线程是共同一个数据   数据安全性问题
        
        GIL  伪线程
        lock = Lock()
        lock.acquire()
        ...
        lock.release()
        
        ----死锁
        避免死锁  请求锁的时候添加 timeout= 参数
3.生产者和消费者：两个线程之间的通信
通过队列 queue

生产者：线程
消费者：线程
        
"""