#!/usr/bin/python


def get_geo_prog(a,q):
    k=0
    while True:
          result=a*q**k
          if result <=100000:
             yield result
          else:
             return
          k+=1

for n in get_geo_prog(2,5):
    print(n)
