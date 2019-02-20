#!/usr/bin/python


from collections import ChainMap

d_conn={'host':'localhost','port':8080}

conns={'port':11211}

conn=ChainMap(d_conn,conns)

print(conn.maps)

print(conn['port'])


conn['host']='server1.com'

print(conn.maps)
