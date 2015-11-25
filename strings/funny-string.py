# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input().strip())
T_i = 0
Funny = 'Funny'
for T_i in xrange(T):
    S = raw_input().strip()
    R = S[::-1]
    for i in range(1, len(S)):
        if abs(ord(S[i])-ord(S[i-1])) != abs(ord(R[i])-ord(R[i-1])):
            Funny = 'Not Funny'
            break
    print Funny
