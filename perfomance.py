#!/usr/bin/python

from time import time

mx=3500

#for loop

t=time()
dmloop=[]

for a in range(1,mx):
    for b in range(a,mx):
        dmloop.append(divmod(a,b))

print('for loop:{:.4f}s'.format(time()-t))

#List comprehension

t=time()
dmlist=[divmod(a,b) for a in range(1,mx) for b in range(a,mx)]

print('List comprehension:{:.4f}s'.format(time()-t))


#Generator expression
t=time()
dmgen=list((divmod(a,b) for a in range(1,mx) for b in range(a,mx)))

print('Generator expression:{:.4f}s'.format(time()-t))

print(dmloop==dmlist==dmgen,len(dmloop))
