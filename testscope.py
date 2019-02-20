#!/usr/bin/python 


def scopetest():
    m=10
    print(m,'Printing from the local scope')


m=15
print(m,'printing from the global scope')


scopetest()
