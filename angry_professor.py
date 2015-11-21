# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
for i in range(0,t):
    n_and_k = raw_input().split(' ')
    n = int(n_and_k[0])
    k = int(n_and_k[1])
    arrivals= map(int,raw_input().split(' '))
    print 'YES' if sum(1 for x in arrivals if x<1)<k else 'NO'