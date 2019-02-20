#!/usr/bin/python

class Person():
      def __init__(self,age):
                   self._age=age

      @property
      def age(self):
          return  self._age

      @age.setter
      def age(self,age):
          if 18 <=age <=99:
             self._age=age
          else:
             raise ValueError('Age must be with in [18,99]')

person=Person(39)

print(person.age)
