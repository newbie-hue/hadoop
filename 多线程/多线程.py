import time
from threading import Thread,current_thread


def loop():
    print("thread %s is running..." % current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print("thread %s >>> %s" % (current_thread().name,n))
        time.sleep(1)
    print("thread %s ended." % current_thread().name)

print("thread %s id running..." % current_thread().name)
t = Thread(target=loop,name="loopThread")
t.start()
t.join()
print("thread %s ended." % current_thread().name)