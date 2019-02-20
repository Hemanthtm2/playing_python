#!/usr/bin/python


def get_sqr(n):
    for x in range(n):
        yield x**2


square=get_sqr(5)

print(square.__next__())
print(square.__next__())
print(square.__next__())
print(square.__next__())
print(square.__next__())

print(square.__next__())
