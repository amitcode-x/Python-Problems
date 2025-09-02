# Variable length Arguments


def add(*args):
    
    print(args)
    print(type(args))
    summ = 0
    for i in args:
        summ += i 
        
    print(summ)

add()
add(10,20,30)
add(10,20)
add(100)