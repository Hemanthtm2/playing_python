#!/usr/bin/python

from functools import wraps


def max_value(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*arg,**kwarg):
            result=func(*arg,**kwarg)
            if result>threshold:
               print('Result is too big',result)
            return result
        return wrapper
        return decorator

def cube(n):
    return n**3

               
@max_value(75)
print(cube(5))
