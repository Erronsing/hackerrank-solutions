# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = [int(x) for x in raw_input().split()]
lst = []
count = 0
maxCount = 0
pairs = []
pairCount = 0

for i in range (0, N):
    lst.append([int(x) for x in raw_input().split()][0])
for i in range (0, N):
    for j in range(i, N):
        count = 0
        temp = lst[i]+lst[j]
        for digit in str(temp):
            if int(digit)>0:
                count+=1
        if count>maxCount:
            maxCount = count
            pairs = []
            pairs.append((i+1, j+1))
            pairCount = 1
        elif count==maxCount:
            pairs.append((i+1,j+1))
            pairCount+=1
        
            
        
#print lst
print maxCount
#print pairs
print pairCount