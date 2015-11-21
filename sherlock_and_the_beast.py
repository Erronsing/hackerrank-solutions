t = int(raw_input())
for i in range(0,t):
    target = int(raw_input())
    fives=target
    while fives>0:
        if(fives%3==0):
            break;
        fives-=5
    threes = target-fives
    if fives < 0 or threes%5!=0:
        print -1
    else:
        print '5'*fives + '3'*threes