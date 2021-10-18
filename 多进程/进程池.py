import time,random

import os
from multiprocessing import Process,Pool


class Person():
    def __init__(self):
        self.count = 0

    def run(self):
        self.count+=1
        print(222)
        return self.count


def long_time_task():
    Person1 = Person()
    name = ""
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    print(111111111)
    print(Person1.run())
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(8):
        p.apply_async(long_time_task)
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

