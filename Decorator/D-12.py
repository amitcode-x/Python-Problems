
# Write a decorator that prints "Before function call" and "After function call" around the execution of a function.


def outer(fun):
    def inner():
        print("Before function call")
        fun()
        print("Before function call")
    return inner
#hai = outer(hai)
@outer
def hai():
    pass

hai()