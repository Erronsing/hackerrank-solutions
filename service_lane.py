# Enter your code here. Read input from STDIN. Print output to STDOUT
first_line = map(int,raw_input().split(' '))
n = first_line[0]
t = first_line[1]
width_array = map(int, raw_input().split(' ', n))
for i in range(0,t):
    entry_exit = map(int,raw_input().split(' '))
    entry = entry_exit[0]
    exit = entry_exit[1]
    print(min(width_array[j] for j in range(entry, exit+1)))