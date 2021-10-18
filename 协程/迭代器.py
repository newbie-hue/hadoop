import collections
from collections.abc import Iterator



a_list = [1,2,3,4,5]

print(isinstance(iter(a_list),Iterator))




#创建生成器的方法
L = (i*i for i in range(10))
def mygen(n):
    now = 0
    while now < n:
        yield now
        now += 1




def mygen(n):
    now = 0
    while now < n:
        print(11111111)
        yield now
        now += 1


gen = mygen(4)
# 通过交替执行，来说明这两种方法是等价的。
print(gen.send(None))
print(next(gen))
print(gen.send(None))
print(next(gen))














