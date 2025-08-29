# -----------Wap to print how many times given substring is present in given string

s = input('Enter a string: ')
ss = input('Enter a substring: ')
count = 0
for i in range(len(s) - len(ss) + 1):   
    if s[i:i+len(ss)] == ss:        
        count += 1
print(count)
    