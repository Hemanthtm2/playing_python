#!/usr/bin/python

class Rectangle():
      def __init__(self,sideA,sideB):
                   self.sideA=sideA
                   self.sideB=sideB
      def area(self):
          return self.sideA*self.sideB


r1=Rectangle(10,20)

print(r1.area())
