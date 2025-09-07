# Wap to count vowel of string using index


s = input('Enter a string :').lower()
v = 'aeiou'
count = 0
for ip in range(len(s)):
    if s[ip] in v:
        count +=1
print(count)
        