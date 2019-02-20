#!/usr/bin/python

x=[1,2,3]

def func(x):
    x[1]=42
    x="Something else"

func(x)

print(x)
