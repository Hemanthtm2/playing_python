#!/usr/bin/python

day_num=int(input('Enter the day number\n'))

if 1<=day_num<=5:
   day='weekday'
   print(day)
elif day_num==6:
     day='Saturday'
     print(day)
elif day_num==0:
     day='Sunday'
     print(day)

else:
    day=''
    raise ValueError(str(day_num)+'is not a valid day number')
