#!/usr/bin/python

from time import time,sleep
from functools import wraps


def measure(func):
    @wraps(func)
    def wrapper(*arg,**kwarg):
        t=time()
        func(*arg,**kwarg)
        print(func.__name__,'took',time()-t)
    return wrapper

@measure
def f(sleep_time=0.5):
    """ I'm a cat I love to sleep"""
    sleep(sleep_time)

f()
print(f.__name__,':',f.__doc__)
