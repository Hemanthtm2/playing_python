#!/usr/bin/python


class Price():
      def final_price(self,vat,discount):
          return (self.net_price*(100+vat)/100)

p=Price()

p.net_price=10

print(Price.final_price(p,20,10))

print(p.final_price(30,10))
