
'''
javascript  Python  面向对象编程  一切皆对象
函数为闭包函数，可以将函数名赋值给变量
'''
def hi(name = "yasoob"):
    return "hi" + name

print(hi())
#output:"hi yasoob"

#我们甚至可以将一个函数赋值为一个变量，比如

greet = hi



'''
在函数中定义函数
'''

def hi(name = "yasoob"):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
hi()


'''
从函数中返回函数
这样就可以把函数中定义的函数返回出来
'''

print("*"*20)
def hi(name = "yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome

a = hi()
print(a())

print('*'*50)

"""
将函数名作为一个参数传给另一个参数
"""

def  hi():
    return "hi yasoob!"

def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())

doSomethingBeforeHi(hi)



print('开始第一个装饰器')
'''
开始第一个装饰器
'''
def a_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before executing a_fun()")

        a_func()

        print("I am doing some boring work agter executing a_fun()")

    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")
a_new_decorator(a_function_requiring_decoration)()




print('使用@定义的装饰器')
'''
使用@定义的装饰器,但是这里进行更改了注释的文档
需要用functools.wraps来修改注释文档
'''

@a_new_decorator
def a_function_requore_decoration():
    """ Hey you! Decorate me!!!"""
    print("I am the function which needs some decoration to remove my foul smell")

print(a_new_decorator(a_function_requore_decoration)())




























