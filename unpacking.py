#!/usr/bin/python

def funcs(*arg):
    print(arg)

values=(1,2,3,4,0,-5,-100)

funcs(values)
funcs(*values)
