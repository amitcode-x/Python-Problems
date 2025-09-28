# Remove duplicate characters from string

s = input('Enter a string:')
d= ''
for i in s:
    if i not in d:
        d +=i
        
print(d)

# Using set()
s = input('Enter a string:')
r = ''.join(set(s))
print(r)  

# Using dict.fromkeys()

s = input('Enter a string:')
r = ''.join(dict.fromkeys(s))
print(r)

