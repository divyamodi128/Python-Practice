from threading import Thread, Lock
import time

funcLock = Lock()

def func(threadName, delay, repeat):
    print "Name :", threadName, "Started"
    funcLock.acquire()
    for _ in range(int(repeat)):
        time.sleep(int(delay))
        print threadName, ":", str(time.ctime(time.time()))
    print "Realsing the lock."
    funcLock.release()
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

if __name__ == '__main__':
    MultiThead()
    # normal_method()