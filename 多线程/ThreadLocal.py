import threading



#创建全局的ThreadLocal对象
local_student = threading.local()


def process_student():
    #获取当前
    std = local_student.student
    print("Hello ,%s (in %s)" % (std,threading.current_thread().name))

def process_thread(name):
    local_student.student = name
    process_student()

t1 = threading.Thread(target = process_thread ,args=("Alice",),name = "thread-A")
t2 = threading.Thread(target = process_thread ,args=("Bob",),name = "thread-B")
t1.start()
t2.start()
t1.join()
t2.join()