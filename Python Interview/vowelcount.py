# Count vowels

s = input('Enter a string :').lower()
v = 'aeiou'
cv = 0

for i in s:
    if i in v:
        cv+=1
print(cv)