#!/usr/bin/python


def is_mult_five(n):
    return not n%5

def get_mult_five(n):
    return list(filter(is_mult_five,range(n)))


print(get_mult_five(100))
