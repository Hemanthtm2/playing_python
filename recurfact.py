#!/usr/bin/python

def fact(n):
    if n in (0,1):
       return 1
    return fact(n-1)*n

print(fact(5))
