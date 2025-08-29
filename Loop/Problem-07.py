# Wap to print how many vowel are present in given string


s = input ('Enter a string:').lower()
c = 0
v = 'aeiou'
for ele in s:
    if ele in v:
        c+=1
print(c)