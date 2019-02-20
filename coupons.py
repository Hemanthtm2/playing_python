#!/usr/bin/python

customers=[dict(id=1,total=200,c_code='F20'),
           dict(id=2,total=150,c_code='P30'),
           dict(id=3,total=100,c_code='P50'),
           dict(id=4,total=110,c_code='F15'),
          ]

print(customers,'\n\n')

for customer in customers:
    code=customer['c_code']
    if code=='F20':
       customer['discount']=20.0
    elif code=='F15':
       customer['discount']=15.0
    elif code=='P30':
       customer['discount']=customer['total']*0.3
    elif code=='P50':
       customer['discount']=customer['total']*0.5
    else:
       customer['discount']=0.0

for customer in customers:
    print(customer['id'],customer['total'],customer['discount'])
