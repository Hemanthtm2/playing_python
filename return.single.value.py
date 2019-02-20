#!/usr/bin/python

def factorial(n):
    if n in (0,1):
       return 1
    result=n
    for k in range(2,n):
        result*=k
        print(result)
    return result

print(factorial(5))
