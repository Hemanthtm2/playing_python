#!/usr/bin/python

cubes=[k**3 for k in range(10)]

odd_cube1=list(filter(lambda k:k%2,cubes))

odd_cube2=(cube for cube in cubes if cube%2)
print(cubes)

print(odd_cube1)

print(list((odd_cube2)))
