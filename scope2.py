#!/usr/bin/python 

def enclosing_func():
    m=17
    
    def local():

        print(m,'printing from local scope')


    local()

m=5
print(m,'printing from the global scope')

enclosing_func()

