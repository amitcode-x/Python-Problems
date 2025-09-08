# wap to print kaprekar numbers in a given range
def isKaprekar(n):
    sq = n * n
    s = str(sq)
    for i in range(1, len(s)):
        left = int(s[:i]) if s[:i] else 0
        right = int(s[i:])
        if left + right == n:
            return True
    else:
        return n == 1  # 1 is Kaprekar


def KaprekarNum(LL, UL):
    for n in range(LL, UL + 1):
        if isKaprekar(n):
            print(n)


# Test
KaprekarNum(1, 200)
