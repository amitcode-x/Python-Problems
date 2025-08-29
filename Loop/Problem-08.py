# Wap to print how many consonant are present in given string


s = input('Enter a string :').lower()
c = 0
v= 'aeiou'
for ele in s:
    if ele.isalpha() and ele not in v:
        c+=1
print(c)