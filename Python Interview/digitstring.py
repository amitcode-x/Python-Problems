s = input('Enter a string :').lower()

d = 0

for i in s:
    if i.isdigit():
        print(i,end=' '); print( )
      
        d+=1
    
print("this is digit",d)