# Variable length keyword Arguments

def add(**kwargs):
    
    print(kwargs)
    print(type(kwargs))
    summ = 0
    for key in kwargs:
        summ += kwargs[key]
        
    print(summ)

add()
add(a=10)
add(a=10,b=20)

