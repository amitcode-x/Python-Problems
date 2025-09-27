from collections import Counter


def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    return Counter(s1) == Counter(s2)
s1=input('Enter s1 string:')
s2=input('Enter s2 string:')
if is_anagram(s1, s2):
    print("anagram")
else:
    print("not")
    
    

from collections import Counter
def isna(s1,s2):
    s1 = s1.replace(' ','')
    s2 = s2.replace(' ','')
    if Counter(s1)== Counter(s2):
        print("ANgram")
    else:
        print('not')
isna('amit','tima')

# without functions 
s1 = input('Enter s1 string:')
s2 = input('Enter s2 string:')
if len(s1) != len(s2):
    print('not anagram')
else:
    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            print('not anagram')
            break
    else:
        print('anagram')
      