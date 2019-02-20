#!/usr/bin/python


def calc_triple(mx):
    triples=[]

    for a in range(1,mx+1):
        for b in range(a,mx+1):
            hypotenues=calc_hypotenues(a,b)
            if is_int(hypotenues):
               triples.append((a,b,int(hypotenues)))
    return triples


def calc_hypotenues(a,b):
    return (a**2 + b**2) **.5

def is_int(n):
    return n.is_integer()


triples=calc_triple(1000)
