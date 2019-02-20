#!/usr/bin/python 

from functools import wraps
from time import time


def measure(func):
    
    @wraps(func)
    def wrapper(*arg,**kwarg):
        time=()
        result=func(*arg,**kwarg)
        if result > 100:
           print('Value is too big',result)
           return result
    return wrapper

@measure
def cube(n):
    return n**3

print(cube(10))
