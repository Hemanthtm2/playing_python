#!/usr/bin/python

class Triangle():

      def __init__(self,side1,side2):
          self.side1=side1
          self.side2=side2
      def area(self):
          return 3.14*self.side1*self.side2


t1=Triangle(12,14)

print(t1.area())
   


