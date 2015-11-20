T = int(raw_input())
for i in range (0,T):
    A,B,C1 = [int(x) for x in raw_input().split(' ')]
    total=A
    price=B
    exchange=C1
    
    wrappers = total/price
    answer = total/price
    while wrappers>=exchange:
        wrappers = wrappers-exchange
        answer += 1
        wrappers+=1
        
    
    # write code to compute answer
    print answer