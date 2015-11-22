#!/bin/python

import sys


d1,m1,y1 = raw_input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = raw_input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

'''no fine for on or expected return date
same calendar month = 15 * late days
same year = 500 hackos * late months
more than same year = 10,000 hackos
'''
if y1==y2:
    if m1==m2:
        if d1<=d2:
            print 0
        else:
            print 15 * (d1-d2)
    elif m1<m2:
        print 0
    else:
        print 500 *(m1-m2)
elif y1<y2:
    print 0
else:
    print 10000