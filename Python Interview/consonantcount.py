s = input('Enter a string :').lower()
v = 'aeiou'
cc = 0

for i in s:
    if i not in v and i.isalpha():
        print(i,end=' '); print( )
      
        cc+=1
    
print("this is consonant",cc)
