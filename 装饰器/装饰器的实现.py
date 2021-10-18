from functools import wraps



def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work before executing a_func()")

    return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")


print(a_function_requiring_decoration())





print("*/"*50)
'''
开始装饰器的蓝本---控制函数是否运行
'''
from functools import wraps

def decorator_name(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args,**kwargs)
    return decorated

@decorator_name
def func():
    return ("Function is runing")

can_run = True
print("can_run = True\t\t\t",func())

can_run = False
print("can_run = False\t\t\t",func())



'''
检查一个人是否被授权使用一个web的端点
被大量用于Flask 和Django web框架中
'''
from functools import wraps
import requests



def require_auth(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        auth = requests.agthorization
        if auth or not check_auth(auth.username,auth.password):
            pass
        return f(*args,**kwargs)
    return decorated


def check_auth():
    pass



'''
日志中的装饰器
'''

from functools import wraps
def logit(func):
    @wraps(func)
    def with_logging(*args,**kwargs):
        print(func.__name__+"was called")
        return func(*args,**kwargs)
    return with_logging




'''
带参数的装饰器
'''



from functools import wraps
import logging

def logit(logfile = "out.log"):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*arg,**kwargs):
            log_string = func.__name__ + "was called"
            print(log_string)
            with open(logfile,"a") as opened_file:
                opened_file.write(log_string + '\n')
            return func(*arg,**kwargs)
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1(a=3,b=4):
    print(a*b)

myfunc1(5,6)





'''
以类的形式重构logit装饰器
'''

print('以类的形式重构logit装饰器','*'*60)
from functools import wraps



class logit(object):
    def __init__(self,logfile = "out.log"):
        self.logfile = logfile

    def __call__(self, *args, **kwargs):
        @wraps(func)
        def wrapped_function(*args,**kwargs):
            log_string = func.__name__ + "was called"
            print(log_string)
            with open(self.logfile,"a") as opened_file:
                opened_file.write(log_string)
            self.notify()
            return func(*args,**kwargs)
        return wrapped_function
    def notify(self):
        pass


@logit()
def myfunc1():
    pass




class  email_logit(logit):
    def __init__(self,email = "admin@myproject.com",*args,**kwargs):
        self.email = email
        super(email_logit,self).__init__(*args,**kwargs)


    def notefy(self):
        pass


from functools import wraps


def log(*msg):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            for m in msg:
                if isinstance(m, str) and m != '':
                    print('print:' + m)
            print('do some decorating')
            return func(*args, **kw)

        return wrapper

    return decorator


@log('有msg参数')
def func1():
    print('func1 is called')


@log()
def func2():
    print('func2 is called')


func1()
func2()















