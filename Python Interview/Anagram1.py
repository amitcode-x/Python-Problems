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