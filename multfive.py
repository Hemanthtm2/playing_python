#!/usr/bin/python


def mult_five(n):
    return list(filter(lambda k: not k%5,range(n)))

print(mult_five(100))
