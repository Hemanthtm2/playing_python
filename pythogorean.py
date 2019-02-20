#!/usr/bin/python

from math import sqrt

mx=10

legs=[(a,b,sqrt(a**2+b**2)) for a in range(1,mx) for b in range(a,mx)]


legs=list(filter(lambda triple:triple[2].is_integer(),legs))

print(legs)
