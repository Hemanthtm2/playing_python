#!/usr/bin/python

class Price():
      def calc(self,vat,discount):
          return(self.amount*vat/100)


p1=Price()

p1.amount=100
print(p1.calc(12,20))
