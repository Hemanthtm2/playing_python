#!/usr/bin/python

def funcs(a,b,c=10,*arg,**kwarg):
    print(a,b,c)
    print(arg)
    print(kwarg)

funcs(10,20,30,*(1,2,3,4),**{'y':'a','z':'b'})
