#!/usr/bin/python

class Square():
      side=8
      def area(self):
          return self.side**2

sq=Square()

print(sq.side)
print(sq.area())

print(Square.area(sq))
