# Check palindrome string


s = input('Enter a string :')
rev =''
for i in s:
    rev = i + rev
if s == rev :
    print('String is palindrome ',rev)
else:
    print('Not palindrome ',rev)
