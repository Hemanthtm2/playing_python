#!/usr/bin/python

class Weird:

      def __init__(self,s):
          self._s=s
      def __len__(self):
          return len(self._s)

      def __bool__(self):
          return '42' in self._s

weird=Weird('Hello! Iam 29 years old')

print(len(weird))
print(bool(weird))


