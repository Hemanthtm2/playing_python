#!/usr/bin/python



def get_squares_gen(n):
    for x in range(n):
        yield x**2


square=get_squares_gen(10)


print(square)

print(next(square))
print(next(square))
print(next(square))
print(next(square))
print(next(square))
print(next(square))
print(next(square))
print(next(square))
print(next(square))
