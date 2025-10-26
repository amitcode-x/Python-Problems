# Generator Function to generate range of numbers 
def rangeGen(sl,el,up=1):
    while sl<=el:
        yield sl
        sl+=up
rgo = rangeGen(1,10,2)
for i in rgo:
    print(i)




