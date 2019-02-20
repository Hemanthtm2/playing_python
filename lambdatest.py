#!/usr/bin/python

def get_mult_five(n):
    return list(filter(lambda k: not k%5,range(n)))


print(get_mult_five(200))


