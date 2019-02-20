#!/usr/bin/python
import os
def connect(**options):
    conn_params={
                'host':options.get('host','127.0.0.1'),
                'port':options.get('port',5432),
                'user':options.get('user',''),
                'pwd':options.get('pwd',''),
                }
    print(conn_params)
                


connect()

connect(host='127.0.0.2',user='hmurali@zynga.com')

#connect(host=os.system('hostname'),port='80',user='root',pwd=os.system('pwd'))
