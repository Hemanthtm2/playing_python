#!/usr/bin/python


from collections import ChainMap


def_conn={'host':'localhost','port':8989}

new_conn={'port':8080}

conn=ChainMap(def_conn,new_conn)

print(conn.maps)

conn['host']='playlinux.com'

print(conn.maps)
