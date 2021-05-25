#coding:utf-8
from threading import Thread
from time import sleep
 
def asyn(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target = f, args = args, kwargs = kwargs)
        thr.start()
    return wrapper
 
@asyn
def A():
    sleep(5)
    print("a function")
 
def B():
    print("b function")
 
A()
B()