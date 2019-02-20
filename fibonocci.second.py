#!/usr/bin/python

def fibo(N):
    yield 0
    if N==0:
       return
    a=0
    b=1
    while b <=N:
          yield b
          a,b=b,a+b
          print(a)
          print(b)

print(list(fibo(5)))
       
