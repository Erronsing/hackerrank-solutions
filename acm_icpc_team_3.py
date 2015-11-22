#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in xrange(n):
   topic_t = str(raw_input().strip())
   topic.append(topic_t)
max_topics_lst = [bin(int(topic[i],2)|int(topic[j],2)).count('1') for i in xrange(n-1) for j in xrange(i+1, n)]
max_topics = max(max_topics_lst)
max_pairs = max_topics_lst.count(max_topics)
print max_topics
print max_pairs