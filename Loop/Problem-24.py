# Wap to check how many time each char is present in string

s = input('Enter a string :')
freq = {}
for char in s:
    if char in freq:
        freq[char]+=1
    else:
        freq[char] =1
for char in freq:
    print(freq[char])
