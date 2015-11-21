# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
#print T
for i in range(0, T):
    B, W = [int(x) for x in raw_input().split(' ')]
    X, Y, Z = [int(x) for x in raw_input().split(' ')]
    left = 0
    right = 0
    #print B, W
    #print X, Y, Z
    if Y+Z<X:
        left = B * (Y+Z)
    else:
        left = B *X
    if X+Z<Y:
        right = W * (X+Z)
    else:
        right = W * Y
    print left+right 
        