def smart_divide(arg):
    def swap(a,b):
        if a<b:
            a,b=b,a
        arg(a,b)
    return swap
@smart_divide
def divide(a,b):
    print(a,b)

divide(10,2)
divide(5,15)