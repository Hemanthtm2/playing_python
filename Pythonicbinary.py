#!/usr/bin/python

n=39

remainders=[]

while n > 0:
      n,remainder=divmod(n,2)
      remainders.append(remainder)

remainders=remainders[::-1]

print(remainders)
