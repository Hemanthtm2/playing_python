#!/usr/bin/python

def fibonocci(N):
    result=[0]
    next_n=1
    while next_n<=N:
          result.append(next_n)
          next_n=sum(result[-2:])
    return result

print(fibonocci(5))
