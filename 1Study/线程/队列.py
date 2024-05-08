"""
队列：fist in first out
栈：fist in  last out  先进后出

"""

# from multiprocessing import Queue
#
# q = Queue(5)
# q.put('A')
# q.put('B')
# q.put('C')
# q.put('D')
# q.put('E')
#
# print(q.qsize())  # 获取队列的长度
#
# if not q.full():  # 判断队列已满  q.empty() 判断队列是不是空的
#     q.put('F', timeout=1) # 等待队列 put 如果队列满了则只能等待 除非有空的地方 则添加成功   queue.Full
# else:
#     print('队列已满!')
#
# print(q.get(timeout=2))
# print(q.get(timeout=2))
# print(q.get(timeout=2))
#
# q.put_nowait()
# q.get_nowait()
from time import sleep

"""
进程之间的通信
"""

from multiprocessing import Process, Queue


def download(q):
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']
    for image in images:
        print('正在下载:', image)
        sleep(0.5)
        q.put(image)


def getfile(q):
    while True:
        try:
            file = q.get(timeout=5)  # 只取了一次
            print('保存成功!'.format(file))
        except:
            print('全部保存完毕!')
            break


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))
    p1.start()
    p1.join()

    p2.start()
    p2.join()

    print('--------------')
