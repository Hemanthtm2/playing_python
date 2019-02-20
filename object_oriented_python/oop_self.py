#!/usr/bin/python

class Price():
      def total(self,vat,discount):
          return(self.amount*vat)+discount/100


p1=Price()

p1.amount=10

print(p1.total(20,50))
