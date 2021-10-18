# -*- coding: utf-8 -*-

import random , time,queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接受任务的队列
result_queue = queue.Queue()

#从BaseManager继承的QueueManger
class QueueManger(BaseManager):
    pass


def return_task_queue():
    global  task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


if __name__ == '__main__':

    # 把两个Queue注册到网络上，callable参数关联Queue对象

    QueueManger.register("get_task_queue", callable=return_task_queue)
    QueueManger.register("get_result_queue", callable=return_result_queue)

    # 绑定ip和端口号
    manager = QueueManger(address=("127.0.0.1", 5000), authkey=b"abc")

    # 启动manager
    manager.start()

    # 通过网络访问Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放一些任务
    for i in range(10):
        n = random.randint(0, 1000)
        print("Put task %d..." % n)
        task.put(n)

    # 从result队列读取结果：
    print("Try get results...")
    for i in range(10):
        r = result.get(timeout=10)
        print("Result:%s" % r)

    manager.shutdown()
    print("matser exit.")












