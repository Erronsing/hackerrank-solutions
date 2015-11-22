#acm_icpc_team_2.py
#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in xrange(n):
   topic_t = str(raw_input().strip())
   topic_t = [int(ch) for ch in topic_t]
   topic.append(topic_t)

maxCount = 0
count = 0

for i in xrange(0, n):
    for j in xrange(i+1, n):
        count = 0
        for k in xrange(0, m):
            count = count +(topic[i][k] | topic[j][k])
        if count > maxCount:
            maxCount = count
            pairCount = 1
        elif count == maxCount:
            pairCount += 1
            
print maxCount
print pairCount