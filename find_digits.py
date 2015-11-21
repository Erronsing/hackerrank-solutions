# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
for i in range(0,t):
    n = raw_input()
    positive_ints = []
    for x in n:
    	if int(x)>0:
    	   positive_ints.append(int(x))
    print sum(1 for x in positive_ints if int(n)%x==0)