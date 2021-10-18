def generator_1():
    total = 0
    while True:
        x = yield
        print("加",x)
        if not x:
            return total
        total += x

def generator_2():
    while True:
        total = yield from generator_1()
        print("加和总数是：",total)

def main():
    # g1 = generator_1()
    # g1.send(None)
    # print("g1中填入1~~",g1.send(1))
    # print("g1中填入2~~",g1.send(2))
    # print("g1中填入3~~",g1.send(3))
    # print("最终出结果！！",g1.send(None))
    g2 = generator_2()
    g2.send(None)
    g2.send(2)
    g2.send(3)
    g2.send(None)

main()


print("==========  yield  ===========")

# 字符串
astr='ABC'
# 列表
alist=[1,2,3]
# 字典
adict={"name":"wangbm","age":18}
# 生成器
agen=(i for i in range(4,8))

def gen(*args, **kw):
    for item in args:
        for i in item:
            yield i

new_list=gen(astr, alist, adict,agen)
print(list(new_list))
# ['A', 'B', 'C', 1, 2, 3, 'name', 'age', 4, 5, 6, 7]

print("==========  yield from  ===========")

# 字符串
astr='ABC'
# 列表
alist=[1,2,3]
# 字典
adict={"name":"wangbm","age":18}
# 生成器
agen=(i for i in range(4,8))

def gen(*args, **kw):
    for item in args:
        yield from item

new_list=gen(astr, alist, adict, agen)
print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))
# print(list(new_list))
# ['A', 'B', 'C', 1, 2, 3, 'name', 'age', 4, 5, 6, 7]


print("============  生成器的嵌套  =================")
'''
1、调用方:调用委派生成器的客户端代码
2、委托生成器：包含yield from 表达式的生成器函数
3、子生成器：yield from 后面加的生成器函数
'''

def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average


print(dir(list))



print("=================  =      ==============================")
# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        count += 1
        total += new_num
        average = total/count

# 委托生成器
def proxy_gen():
    while True:
        yield from average_gen()

# 调用方
def main():
    calc_average = proxy_gen()
    print(next(calc_average))  #打印  0
    print(calc_average.send(10))  # 打印：10.0
    print(calc_average.send(20))  # 打印：15.0
    print(calc_average.send(30))  # 打印：20.0


main()


print('======================================================')





# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        if new_num is None:
            break
        count += 1
        total += new_num
        average = total/count

    # 每一次return，都意味着当前协程结束。
    return total,count,average

# 委托生成器
def proxy_gen():
    while True:
        # 只有子生成器要结束（return）了，yield from左边的变量才会被赋值，后面的代码才会执行。
        total, count, average = yield from average_gen()
        print("计算完毕！！\n总共传入 {} 个数值， 总和：{}，平均数：{}".format(count, total, average))

# 调用方
def main():
    calc_average = proxy_gen()
    next(calc_average)            # 预激协程
    print(calc_average.send(10))  # 打印：10.0
    print(calc_average.send(20))  # 打印：15.0
    print(calc_average.send(30))  # 打印：20.0
    calc_average.send(None)      # 结束协程
    # 如果此处再调用calc_average.send(10)，由于上一协程已经结束，将重开一协程


main()



































