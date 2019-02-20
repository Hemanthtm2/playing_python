#!/usr/bin/python

class Point():
      x=5
      y=3

p=Point()

print(Point.x)
print(Point.y)

print(p.x)
print(p.y)

p.z=10

print(p.z)


p.x=15

print(p.x)

print(Point.x)

del p.x

print(p.x)

print(Point.z)
