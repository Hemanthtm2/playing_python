#!/usr/bin/python

class Base():
      def __init__(self,item,exp,price):
          self.item=item
          self.exp=exp
          self.price=price

class Second(Base):
      def __init__(self,item,exp,price,manf):
          Base.__init__(self,item,exp,price)
          self.manf=manf


sec=Second('Candy','Sunday',20,'Today')

print(sec.item)
print(sec.exp)
print(sec.price)
print(sec.manf)
        
