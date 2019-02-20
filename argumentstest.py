#!/usr/bin/python
#positional arguments

def pos(a,b,c):
    print(a,b,c)

#keyword arguments

def kw(a,b,c=10):
       print(a,b,c) 

#variable positional arguments

def varpo(*n):
    print(n)


#variable keyword arguments

def varkw(**a):
    print(a)


#keyword only arguments


def kwo(*a,c):
    print(a,c)


pos(1,2,3)

kw(12,20,30)

varpo(1,2,3)

varkw(a=1,b=2)

kwo(1,2,3,c=10)




