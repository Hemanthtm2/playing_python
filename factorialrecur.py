#!/usr/bin/python

def factorial(n):
    if n in (0,1):
       return 1
    return factorial (n-1) * n

print(factorial(10))
