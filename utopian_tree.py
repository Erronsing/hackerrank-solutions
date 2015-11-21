# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())

for i in range(0,t):
    h = 1
    n = int(raw_input())
    j = 0
    while j < n:
        if(j%2!=0):
            h+=1
        else:
            h+=h
        j+=1
    print h