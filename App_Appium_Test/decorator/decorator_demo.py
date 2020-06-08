import time



#装饰器:外部函数传入被装饰函数名称，内部函数返回装饰函数名
def outer(func): #传的参数是函数 func_1
    def inner(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)   #func = func_1
        end_time = time.time()
        print("运行的时间%0.2fs"%(end_time-start_time))
    return inner

#func_1_new = outer(func_1)

#func_1_new()
#计算一下代码执行的时间
@outer
def func_1(name):
    time.sleep(2)
    print("func_1%s"%name)

func_1("test")