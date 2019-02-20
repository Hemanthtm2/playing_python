#!/usr/bin/python

items=[0,None,0.0,7,True]

found=False

for item in items:
    print('Scanning items',item)
    if item:
       found=True
       break

if found:
   print("Atleast one item evalutes to True")
else:
   print("None of the items evalutes to True")
