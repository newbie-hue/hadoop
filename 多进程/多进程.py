import os
from multiprocessing import Process,Pool

def run_proc(name):
    print("Run child process %s (%s)..." % (name , os.getpid()))


print("Parent process %s." % os.getpid())
p = Process(target = run_proc ,args = ("test",))
print("Child process will start.")
p.start()
p.join()
print("Child process end.")

























