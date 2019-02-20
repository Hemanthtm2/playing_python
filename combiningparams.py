#!/usr/bin/python


def func(a,b,c=20,*arg,**kwarg):
    print('a,b,c',a,b,c)
    print('args',arg)
    print('kwarg',kwarg)

func(1,2,3,*(10,20,30),**{'A':30,'B':40})

func(1,2,3,10,20,30,A=30,B=40)
