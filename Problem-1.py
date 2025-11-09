
# 1. Generate the square pattern (based on numbers) with sides equal to the given number input: x

# Use the following examples for  references
# Ex:1 - Input number: 4
# 	1 2 3 4
# 	2     3
# 	3     2
# 	4 3 2 1 

    
num = int(input("Enter a number:  "))
for i in range(1, num+1):
     for j in range(1, num+1):
         if i ==1:
             print(f"{j:2} ", end=' ')
         elif i == num:
             print(f"{num-j+1:2} ", end=' ')
         elif j == 1 :
             print(f"{i:2} ", end=' ')
         elif j == num:
             print(f"{num-i+1:2} ", end=' ')
         else:
             print("   ", end=' ')
     print( )                     
     

 