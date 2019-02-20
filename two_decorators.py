#!/usr/bin/python

from time import time,sleep
from functools import wraps

def measure(func):
    @wraps(func)
    def wrapper(*arg,**kwarg):
        t=time()
        result=func(*arg,**kwarg)
        print(func.__name__,'took',time()-t)
        return result
    return wrapper

def max_value(func):
    @wraps(func)
    def wrapper(*arg,**kwarg):
        t=time()
        result=func(*arg,**kwarg)
        if result > 100:
           print('Result is too big ({0}).Max allowed is 100.'.format(result))
        return result
    return wrapper

@measure
@max_value

def cube(n):
    return n**3


print(cube(2))
print(cube(5))
    
