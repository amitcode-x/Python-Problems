# WAP to calculate the nth Fibonacci number using recursion.


def fs(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fs(n - 1) + fs(n - 2)
print(fs(5))
            