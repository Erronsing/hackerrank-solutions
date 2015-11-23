#!/bin/python
def insertionSort(ar):
    for i in xrange(m-1):
        if ar[i]>ar[i+1]:
            temp = ar[i+1]
            ar[i+1] = ar[i]
            ar[i] = temp
            for j in xrange(i-1, -1, -1):
                if temp>ar[j]:
                    ar[j+1] = temp
                    break
                else:
                    ar[j+1] = ar[j]
                    ar[j] = temp
                    
        print ' '.join(str(x) for x in ar)
            
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)