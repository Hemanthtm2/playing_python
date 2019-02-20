#!/usr/bin/python

class Rectangle():
      def __init__(self,sideA,sideB):
                   self.sideA=sideA
                   self.sideB=sideB
      def area(self):
          return self.sideA**2+self.sideB**2

r1=Rectangle(10,20)

print(r1.area())
