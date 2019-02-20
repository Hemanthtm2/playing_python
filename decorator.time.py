#!/usr/bin/python

from time import time,sleep

def f(sleep_time=0.3):
    sleep(sleep_time)

def measure(func):
    def wrapper(*arg,**kwarg):
        t=time()
        func(*arg,**kwarg)
        print(func.__name__,'took',time()-t)
    return wrapper

f=measure(f)

f(0.2)
    
