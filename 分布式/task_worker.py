import time,sys,queue
from multiprocessing.managers import BaseManager

#创建类似的QueManager
class QueueManager(BaseManager):
    pass

QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")

#连接到服务器，也就是运行task_master.py的机器：
server_addr = "127.0.0.1"
print("Connect to server %s..." % server_addr)
#端口号和验证码要保持一致
m = QueueManager(address=(server_addr,5000),authkey=b"abc")
#从网络连接
m.connect()

#获取Queue的对象
task = m.get_task_queue()
result = m.get_result_queue()

#从task对列取任务，并把结果写入result队列：
for i in range(10):
    try:
        n = task.get(timeout = 1)
        print("run task %d *%d..."% (n,n))
        r = "%d * %d = %d" %(n,n,n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print("task queue is empty.")
print("worker exit.")


































