#!?usr/bin/python

def prime(n,remainders=[]):
    #remainders=[]
    while n > 0:
          remainder,n=divmod(n,2)
          remainders.append(remainder)
    remainders=remainders[::-1]
    return remainders


print(prime(39))
