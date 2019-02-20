#!/usr/bin/python

students=[
         dict(id=0,credits=dict(math=9,physics=6,history=7)),
         dict(id=1,credits=dict(math=6,physics=7,latin=10)),
         dict(id=2,credits=dict(history=8,physics=9,chemistry=10)),
         dict(id=3,credits=dict(math=5,physics=5,geography=7)),
         ]

def decorated(student):
    return (sum(student['credits'].values()),student)

def undecorated(decorated_student):
    return decorated_student[1]


students=sorted(map(decorated,students),reverse=True)
students=list(map(undecorated,students))


print(students)
