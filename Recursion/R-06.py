# WAP to reverse a string using recursion.           

def rev(s):
    if s == '':
        return s
    return rev(s[1:])+ s[0]
print(rev('amit'))


# 