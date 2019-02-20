#!/usr/bin/python

customers=[dict(id=1,total=200,c_code='F20'),
           dict(id=2,total=150,c_code='P30'),
           dict(id=3,total=100,c_code='P50'),
           dict(id=4,total=110,c_code='F15'),
          ]

discounts={
         'F20':(0.0,20.0),
         'P30':(0.3,0.0),
         'P50':(0.5,0.0),
         'F15':(0.0,15.0),
         }

for customer in customers:
    code=customer['c_code']
    percent,fixed=discounts.get(code,(0.0,0.0))
    customer['discount']=percent*customer['total']+fixed

for customer in customers:
    print(customer['id'],customer['total'],customer['discount'])
