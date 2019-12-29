import threading
import time


# 创建一个线程子类
class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        moyu_time(self.name, self.counter, 10)
        print("退出线程：" + self.name)


def moyu_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print(
            "%s 开始摸鱼 %s" %
            (threadName, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        counter -= 1


thread1 = MyThread(1, "niki", 1)
thread2 = MyThread(2, "粉红女郎", 2)

# initialize threads
thread1.start()
thread2.start()

# hang the main thread till the subprocess is done
thread1.join()
thread2.join()

print("退出主线程")
