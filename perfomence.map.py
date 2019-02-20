#!/usr/bin/python

from time import time

mx=2*10**6

t=time()

absloop=[]

for n in range(mx):
      absloop.append(abs(n))

print('for loop:{:.4f}s'.format(time()-t))


t=time()

abslist=[abs(n) for n in range(mx)]

print('List comprehension:{:.4f}s'.format(time()-t))

t=time()

absgen=list(abs(n) for n in range(mx))

print('generator expression:{:.4f}s'.format(time()-t))

t=time()

absmap=list(map(abs,range(mx)))

print('map function:{:.4f}s'.format(time()-t))
