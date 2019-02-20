#!/usr/bin/python 

s="This is º£∫ñµµ√"

s_encode=s.encode('utf-8')

print(s_encode)

print(type(s_encode))

print(s_encode.decode('utf-8'))


