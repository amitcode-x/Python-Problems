# Wap if a string is palindrome:
    
     
s = input('Enter a string: ')
rev = ''
for ele in s:
    rev = ele + rev
if s == rev:
    print("string is palindrome")
else:
    print('Not palindrome')