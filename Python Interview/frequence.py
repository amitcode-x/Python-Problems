from collections import Counter
s = input('Enter a string :')
c =Counter(s)
print(c)

# Frequency of characters in a string
s = input("Enter a string: ")
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in freq:
    print(f"{ch}: {freq[ch]}")