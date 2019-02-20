#!/usr/bin/python


from datetime import date,timedelta

today=date.today()
tomorrow=today + timedelta(days=1)

products=[{'sku':'1','exp_date':today,'price':100.0},{'sku':'2','exp_date':tomorrow,'price':50},{'sku':'3','exp_date':today,'price':20}]

for product in products:
    if product['exp_date'] != today:
       continue 
    product['price']*=0.8
    print('Price of sku',product['sku'],'is now',product['price'])
