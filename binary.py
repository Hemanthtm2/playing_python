#!/usr/bin/python

n=int(input("Enter the number you want to get the binaryi\n"))

remainders=[]

while n > 0:
      remainder=n%2
      remainders.append(remainder)
      n=n//2
remainders=remainders[::-1]

print(remainders)









