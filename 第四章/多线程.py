# 线程，进程
# 进程是资源单位，每个进程中只要要有一个线程
# 线程是执行单位

# 启动每一个程序默认都有一个主线程

from threading import Thread # 线程类

def func():
    for i in range(1000):
        print("func", i)

if __name__ == '__main__':
    t = Thread(target = func)
    t.start()  # 启动线程 -> 多线程
    for i in range(1000):
        print("子线程", i)


class MyThread(Thread):
    def run(self):  # 固定的 -> 线程启动后要执行的方法
        for i in range(1000):
            print("子线程", i)

if __name__ == '__main__':
    t = MyThread()
    # t.run() # 方法的调用 -> 单线程？？？
    t.start() # 启动线程 -> 多线程
    pass 