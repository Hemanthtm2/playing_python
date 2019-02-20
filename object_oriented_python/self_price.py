#!/usr/bin/python

class Price():
      def final_value(self,vat,discount):
          return((self.netprice*vat)/100-discount)




p1=Price()

p1.netprice=55

print(p1.final_value(20,5))
