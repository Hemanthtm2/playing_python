#!/usr/bin/python


def get_squares(n):
    return [x**2 for x in range(n)]


def get_squares_gen(n):
    for x in range(n):
        yield x**2
 

print(get_squares(10))

print(list(get_squares_gen(10)))
