
def outer(fun):
    c = 0
    def inner():
        nonlocal c
        c +=1
        fun()
        print(f"Before function {c} call")
    return inner
#hai = outer(hai)
@outer
def hai():
    pass

hai()
hai()