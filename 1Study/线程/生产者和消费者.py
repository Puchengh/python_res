"""
生产者和消费者：两个线程之间的通信
通过队列 queue

python的queue模块中提供了同步的 线程安全的队列类 包括 FIFO(先入先出) 队列Queue
LIHO（后入先出）(栈)队列 lifeQueue  和优先级队列Priorityqueue 这些队列都实现了锁的原理
可以理解为原子操作 即要么不做 要么做完  能够在多线程中直接使用
可以使用队列来实现线程之间的同步。

线程睡醒之后也不一定能拿到执行权

"""




import threading
import queue
import random
import time

def pruduce(q) -> None:
     i =0
     while i < 10:
         num =random.randint(1,100)
         q.put("生产者产生数据{}".format(num))
         print("生产者产生数据{}".format(num))
         time.sleep(4)
         i += 1
     q.put(None)
     # 完成任务
     q.task_done()


def consumer(q)  -> None:
    while True:
        item = q.get()
        if item is None:
            break
        print("消费者获取到{}".format(item))
        time.sleep(3)
    q.task_done()


if __name__ == '__main__':
    q = queue.Queue(10)
    arr = []

    #创建生产者
    th = threading.Thread(target=pruduce, args=(q,))
    th.start()

    tc = threading.Thread(target=consumer, args=(q,))
    tc.start()

    th.join()
    tc.join()

    print('END')