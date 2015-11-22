# Enter your code here. Read input from STDIN. Print output to STDOUT
H = int(raw_input())
M = int(raw_input())
num2words = { 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'ninteen', 20 : 'twenty'}
if M<=20:
    if M == 0:
        s = num2words[H] + " o' clock"
    elif M==15:
        s = 'quarter past ' + num2words[H]
    else:
        s = num2words[M]+ ' minutes past ' + num2words[H]
elif M>20 and M<30:
    secondnumber = M - 20
    s = num2words[20] +' ' + num2words[secondnumber] + ' minutes past ' + num2words[H]
elif M==30:
    s = 'half past ' + num2words[H]
else:
    if M==45:
        s = 'quarter to ' + num2words[H+1]
    elif M<40:
        secondnumber = M-30
        s = num2words[20] + ' ' + num2words[secondnumber]+ ' minutes to ' + num2words[H+1]
    else:
        s = num2words[60-M] + ' minutes to ' + num2words[H+1]
print s