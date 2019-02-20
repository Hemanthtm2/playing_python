#!/usr/bin/python

from operator import mul
from functools import reduce
def factorial(n):
    result= reduce(mul,range(1,n+1),1)
    print(result)
    return result

print(factorial(5))
