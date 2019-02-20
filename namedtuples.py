#!/usr/bin/python

from collections import namedtuple

Vision=namedtuple('Vision',['left','right'])

vision=Vision(9.9,8.8)

print(vision.right)
print(vision.left)


Vision=namedtuple('Vision',['left','combined','right'])

vision=Vision(9.9,7.5,8.8)

print(vision.combined)
