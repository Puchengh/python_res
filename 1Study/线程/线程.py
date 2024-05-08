"""
线程： 耗时操作 爬虫 io读取
线程（计算密集型）  伪线程 不是真正的线程

（共享数据）
共享数据会导致线程不安全

线程状态:
    线程是可以共享全局变量的
新建状态 -- start -- 就绪状态  排队  争夺cpu的执行权 --->  运行状态 sleep(n) 阻塞状态  完了之后会进入就绪状态  ---> 结束状态

线程同步
加锁 导致数据处理变慢（数据安全）  python底层只要用线程 默认就会加锁

GIL 全局解释器共享的锁

会有一个阈值 当阈值足够大 就会释放共享锁 导致线程不安全


"""

# 创建线程

import threading
from time import sleep


def download(n):
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']
    for image in images:
        print('正在下载:', image)
        sleep(n)
        print('下载{}成功'.format(image))


def listenMusic():
    musics = ['稻香', '土耳其冰激凌', '烤面筋', '烤馒头片']
    for music in musics:
        sleep(0.5)
        print('正在听：{}'.format(music))


# 线程对象
if __name__ == '__main__':
    t = threading.Thread(target=download, name='aa', args=(1,))
    t.start()

    t1 = threading.Thread(target=listenMusic, name='aa')
    t1.start()

    n = 1
    while True:
        print(n)
        sleep(1.5)
        n += 1
