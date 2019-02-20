#!/usr/bin/python

def funcs(**kwarg):
    print(kwarg)


funcs(a=1,b=2)

funcs(**{'a':1,'b':2})

funcs(**dict(a=1,b=2))
