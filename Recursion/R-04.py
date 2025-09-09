# WAP to find Sum of INDIVIDUAL digit number using recursion.



def sumd(n):
    if n == 0:
        return 0
    return n%10+sumd(n//10)
print(sumd(124))