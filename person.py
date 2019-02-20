#!/usr/bin/python 

class Person:
      def __init__(self,age):
         self.age=age


fab=Person(age=42)

print(fab.age)

print(id(fab))

fab.age=59

print(fab.age)

print(id(fab))
