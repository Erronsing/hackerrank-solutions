n = int(raw_input())
S = raw_input()
k = int(raw_input())
cipher = ''
for char in S:
    if char.isalpha():
        newchar = ord(char)+k%26
        if char.isupper():
            if newchar>ord('Z'):
                newchar-=26
        elif char.islower():
            if newchar>ord('z'):
                newchar-=26
        cipher += chr(newchar)
     
    else:
        cipher += char
print cipher