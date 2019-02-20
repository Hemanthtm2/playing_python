#!/usr/bin/python

def outer():
    test=2
    def inner():
        #test=3
        print('Inner function testing',test)
    inner()
    print('Outer function testing',test)

outer()
test=5
print('Global testingi',test)
