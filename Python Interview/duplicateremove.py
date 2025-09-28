# Remove duplicate characters from string

s = input('Enter a string:')
d= ''
for i in s:
    if i not in d:
        d +=i
        
print(d)