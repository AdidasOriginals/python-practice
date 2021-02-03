#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/25 11:20 
# @Author : Edison
# @Version：V 0.1
# @File : test-033.py
# @desc :进程和线程
print('Python中的多进程'.center(50, '-'))
from random import randint
from time import time, sleep


def download_task(filename):
    print(f'开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    download_task('Python从入门到住院')
    download_task('Java')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


# main()
print('Process类创建进程对象'.center(50, '-'))
from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task2(filename):
    print(f'启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


# 由于Windows系统没有fork()调用，因此要实现跨平台的多进程编程，可以使用multiprocessing模块的Process类来创建子进程
# 通过Process类创建了进程对象，通过target参数我们传入一个函数来表示进程启动后要执行的代码，后面的args是一个元组，它代表了传递给函数的参数
def main1():
    start = time()
    p1 = Process(target=download_task2, args=('Python从入门到住院.pdf',))
    # start方法用来启动进程
    p1.start()
    p2 = Process(target=download_task2, args=('Java',))
    p2.start()
    # join方法表示等待进程执行结束
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


# if __name__ == '__main__':
#     main1()

# 启动两个进程，一个输出Ping，一个输出Pong，两个进程输出的Ping和Pong加起来一共10个
# 最后的结果是Ping和Pong各输出了10个（或者ping 10个）
print('实现两个进程间的通信'.center(50, '-'))
from multiprocessing import Process
from time import sleep

counter = 0


def sub_task(string):
    global counter
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.01)


def main2():
    Process(target=sub_task, args=('Ping',)).start()
    Process(target=sub_task, args=('Pong',)).start()


# if __name__ == '__main__':
#     main2()

# 多进程消息队列
from multiprocessing import Process, Queue


def sub_task2(name, queue):
    counter = 0
    while counter < 5:
        queue.put(name)
        counter += 1


def main3():
    q = Queue(10)
    Process(target=sub_task2, args=('Ping', q)).start()
    Process(target=sub_task2, args=('Pong', q)).start()
    sleep(2)
    # 判断队列是否为满
    print(q.full())
    # 判断队列是否为空
    print(q.qsize())
    #  获取队列中消息个数
    print(q.empty())
    for _ in range(q.qsize()):
        # 从队列取出消息
        print(q.get())


# if __name__ == '__main__':
#     main3()

print('Python中的多线程'.center(50, '-'))
from random import randint
from threading import Thread
from time import time, sleep


def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main4():
    start = time()
    t1 = Thread(target=download, args=('Python从入门到住院.pdf',))
    t1.start()
    t2 = Thread(target=download, args=('Java.mp4',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))


# if __name__ == '__main__':
#     main4()
print('Python中的多线程2'.center(50, '-'))
from random import randint
from threading import Thread
from time import time, sleep


class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))


def main5():
    start = time()
    # 将多个下载任务放到多个线程中执行
    # 通过自定义的线程类创建线程对象 线程启动后会回调执行run方法
    t1 = DownloadTask('Python从入门到住院.pdf')
    t1.start()
    t2 = DownloadTask('Java.mp4')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


# if __name__ == '__main__':
#     main5()
print('Python中的多线程3-临界资源'.center(50, '-'))
from time import sleep
from threading import Thread


class Account(object):
    def __init__(self):
        self._balance = 0

    def deposit(self, money):
        # 计算存款后的余额
        new_balance = self._balance + money
        # 模拟受理存款业务需要0.01秒的时间
        sleep(0.01)
        # 修改账户余额
        self._balance = new_balance

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


# 100个线程分别向账户中转入1元钱，结果居然远远小于100元
# 是因为我们没有对银行账户这个“临界资源”加以保护，多个线程同时向账户中存钱时，会一起执行到new_balance = self._balance + money这行代码，
# 多个线程得到的账户余额都是初始状态下的0，所以都是0上面做了+1的操作，因此得到了错误的结果
def main6():
    account = Account()
    threads = []
    # 创建100个存款的线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


# if __name__ == '__main__':
#     main6()
print('Python中的多线程4-加锁'.center(50, '-'))
from time import sleep
from threading import Thread, Lock


class Account2(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        self._lock.acquire()
        try:
            # 先获取锁才能执行后续的代码
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread2(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main7():
    account = Account2()
    threads = []
    for _ in range(100):
        t = AddMoneyThread2(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
        print('账户余额为: ￥%d元' % account.balance)


# if __name__ == '__main__':
#     main7()
print('将耗时间的任务放到线程中以获得更好的用户体验'.center(50, '-'))
import time
import tkinter
import tkinter.messagebox


def download():
    # 模拟下载任务需要花费10秒钟时间
    time.sleep(10)
    tkinter.messagebox.showinfo('提示', '下载完成！')


def show_about():
    tkinter.messagebox.showinfo('关于', '作者：吴彦祖')


def main8():
    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)
    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')
    tkinter.mainloop()


# if __name__ == '__main__':
#     main8()
# 使用多线程将耗时间的任务放到一个独立的线程中执行，这样就不会因为执行耗时间的任务而阻塞了主线程
import time
import tkinter
import tkinter.messagebox
from threading import Thread


def main9():
    class DownloadTaskHandler(Thread):
        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('提示', '下载完成！')
            # 启用下载按钮
            button1.config(state=tkinter.NORMAL)

    def download():
        # 禁用下载按钮
        button1.config(state=tkinter.DISABLED)
        # 通过daemon参数将线程设置为守护线程(主程序退出就不再保留执行)
        # 在线程中处理耗时间的下载任务
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于', '作者：吴彦祖')

    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', 1)
    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')
    tkinter.mainloop()


# if __name__ == '__main__':
#     main9()
print('使用多进程对复杂任务进行“分而治之“'.center(50, '-'))
from time import time


# 耗时间
# 5000000050000000
# Execution time:16.180s
def main10():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('Execution time:%.3fs' % (end - start))


# if __name__ == '__main__':
#     main10()
from multiprocessing import Process, Queue
from random import randint
from time import time


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


# 5000000050000000
# Execution time:2.410898447036743s
def main11():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end - start), 's', sep='')


if __name__ == '__main__':
    main11()
