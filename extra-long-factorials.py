#!/bin/python

import sys


n = int(raw_input().strip())
f=1

for i in xrange(n, 1, -1):
     f*= i
print f