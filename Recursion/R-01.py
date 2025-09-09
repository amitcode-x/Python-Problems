def Display(a):
    print(a)
    if a == 0:
        return
    return Display(a-1)
Display(10)