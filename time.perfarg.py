#!/usr/bin/python

from time import time,sleep

def f(sleep_time=0.4):
    sleep(sleep_time)


def measure(func,*arg,**kwarg):
    t=time()
    func(*arg,**kwarg)
    print(func.__name__ ,'took:',time()-t)

measure(f)

measure(f,sleep_time=0.5)
