#!/usr/bin/python

def fib(N):
    a,b=0,1
    while a <=N:
          yield a
          a,b=b,a+b


print(list(fib(10)))
