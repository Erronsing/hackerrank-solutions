# Enter your code here. Read input from STDIN. Print output to STDOUT
A, B, N = [int(x) for x in raw_input().strip().split()]
fib_list = [A, B]
for i in xrange(2, N):
    ith_term = fib_list[i-2]+fib_list[i-1]**2
    fib_list.append(ith_term)
print fib_list[N-1]