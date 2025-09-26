def outer(fun):
   
    def inner(s):
        a = fun(s)
        print(f"square is {a}")
    return inner
#hai=outer(hai)
@outer
def hai(s):
    return s*s

hai(3)
