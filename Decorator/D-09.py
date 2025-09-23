def deco1(func):
    def wrapper():
        print("inner start Deco1")
        func()
        print("inner end Deco1 after")
    return wrapper

def deco2(func):
    def wrapper():
        print("inner start Deco2 ")
        func()
        print("inner end Deco2 after")
    return wrapper
#say = deco1(say)
#say = deco2(say)
#say = deco1(deco2(say))
@deco1
@deco2
def say():
    print("Say something")

say()