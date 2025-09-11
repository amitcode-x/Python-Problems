# Add five to each number in the list
def add_five(x):
    return x + 5

numbers = [1, 2, 3, 4]
result = map(add_five, numbers)
print(list(result))