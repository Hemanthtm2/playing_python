#!/usr/bin/python


def funcs(a=[],b={}):
    print(a)
    print(b)
    print('#'*12)
    a.append(len(a))
    b[len(a)]=len(a)


funcs()
funcs()


funcs(a=[1,2,3,4],b={'a':10,'b':20})
funcs()
