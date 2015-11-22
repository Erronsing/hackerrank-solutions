#!/bin/python
def insertionSort(ar):
    e = ar[m-1]
    for i in xrange(m-2, -1, -1):
        if ar[i]>e:
            ar[i+1] = ar[i]
            print ' '.join(str(x) for x in ar)
        else:
            ar[i+1] = e
            print ' '.join(str(x) for x in ar)
            break   
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)