#!/usr/bin/python

def outer():
    test=1
    def inner():
        test=2
        print('Inner test',test)

    inner()
    print('outer test',test)

test=0
outer()
print('global test',test)
