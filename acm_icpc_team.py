#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
maxCount = 0
for topic_i in xrange(n):
   topic_t = str(raw_input().strip())
   topic.append(topic_t)
    
for i in range (0, n):
    for j in range (i+1, n):
        count = 0
        temp = int(topic[i])+int(topic[j])
        for digit in str(temp):
            if int(digit)>0:
                count+=1
            if count > maxCount:
                maxCount = count
                pairCount = 1
            elif count == maxCount:
                pairCount+=1
print maxCount
print pairCount