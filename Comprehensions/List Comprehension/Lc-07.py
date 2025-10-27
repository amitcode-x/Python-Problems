#value, multiple forloop and one if condition normal approch

#[i,j,k] = [[1,1,1],[2,2,2],[3,3,3],.......,[10,10,10]]

L= []
for i in range(1,11):
    for j in range(1,11):
        for k in range(1,11):
            if i==j==k:
                L.append([i,j,k])
print(L)

#value, multiple forloop and one if condition LC approch

# syntax:
# variablename =[value forloop1 ,forloop2, forloop3 if condition] 

L = [[i,j,k] for i in range(1,11) for j in range(1,11) for k in range (1,11) if i==j==k]
print(L)