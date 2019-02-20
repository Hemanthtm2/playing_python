#!/usr/bin/python


def outer():
    test=15
    def inner():
         nonlocal test
         test=10
         print('nonlocal scope',test)
    inner()
    print('printing from ouer scope',test)

test=15
outer()

print('global scope',test)

