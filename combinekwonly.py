#!/usr/bin/python

def kwonly(a,b=32,*arg,c,d=42,**kwarg):
    print(a,b)
    print(arg)
    print(c,d)
    print(kwarg)


kwonly(10,42,c=0,d=1,*(1,2,3),e=5,f=6)
