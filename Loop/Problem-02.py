# -----For loop of Tuple


t = 12,23,34,45,56,67,'hai',[12,30]
for i in t:
    print(i)
  
    if type(i)== list:
        for j in i:
            print(j)
