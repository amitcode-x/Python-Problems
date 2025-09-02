def add(a,b=10,**kwargs):
    print(a+b)
    summ = 0
    for key in kwargs:
        summ +=kwargs[key]
    print(summ)

add(a=10,b=20,c = 90,d=8)