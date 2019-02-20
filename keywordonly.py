#!/usr/bin/python

def kwo(*a,b):
    print(a,b)


kwo(1,2,3,b=10)


#kwo(2,3)

def kwo2(a,b=42,*,c):
        print(a,b,c)


kwo2(10,b=7,c=15)
