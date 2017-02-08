from threading import Thread
import time


def func(threadName, delay, repeat):
    print "Name :", threadName, "Started"
    for _ in range(int(repeat)):
        time.sleep(int(delay))
        print threadName, ":", str(time.ctime(time.time()))
    print "Name :", threadName, "Ended"

def MultiThead():
    print "Begin Multithreading\n"
    tup1 = ("Thread1", 2, 5)
    tup2 = ("Thread2", 3, 5)
    t1 = Thread(target=func, args=tup1)
    t2 = Thread(target=func, args=tup2)
    t1.start()
    t2.start()
    print "\nEnd Multithreading"

def normal_method():
    print "Normal Function Calling"
    tup1 = ["Thread1", 2, 5]
    func(*tup1)
    func("Thread2", 3, 5)
    print "-------The End-------"

if __name__ == '__main__':
    # MultiThead()
    normal_method()