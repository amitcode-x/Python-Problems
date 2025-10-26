# Size of generator object vs size of iterator object( proof of memory efficiency of generator)
def func():
    i = 1
    while i > 0:
        yield i
        i -=1
f = func()
print(func().__sizeof__())
print(iter([1]).__sizeof__())