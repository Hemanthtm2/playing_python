#!/usr/bin/python

class Point():
      x=10
      y=12

p=Point()

print(p.x)
print(p.y)

p.x=20
p.y=40
print(p.x)
print(p.y)
print(Point.x)
print(Point.y)



del p.x
del p.y

print(p.x)
print(p.y)


p.z=25

print(p.z)

print(Point.z)
