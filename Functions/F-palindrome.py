# wap to print palindrome numbers in a given range
def isPalindrome(n):
    dummy = n
    rev = 0
    while dummy > 0:
        rem = dummy % 10
        rev = rev * 10 + rem
        dummy //= 10
    else:
        if rev == n:
            return True
        else:
            return False


def PalindromeNum(LL, UL):
    for n in range(LL, UL + 1):
        if isPalindrome(n):
            print(n)

PalindromeNum(1, 200)
