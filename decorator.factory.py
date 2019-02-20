#!/usr/bin/python

from functools import wraps
def max_result(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*arg,**kwarg):
            result=func(*arg,**kwarg)
            if result >threshold:
               print('Value is too big')
            return result
        return wrapper
    return decorator


@max_result(75)
def cube(n):
    return n**3

print(cube(5))
