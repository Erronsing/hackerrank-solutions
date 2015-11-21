# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
sticks = map(int, raw_input().split(' '))
cut = min(sticks)
while sticks:
    
    print len(sticks)
    #print sticks
    
    for i in range(0,len(sticks)):
        sticks[i] -= cut
    cut = min(sticks)
        
    sticks = list(filter(lambda stick: stick>cut, sticks))