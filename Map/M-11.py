# i/p : 12 45 67 34 66
# o/p : [12,45,67,34,66]

# taking space seprate integer values as input


print(list(map(lambda a: int(a),input("Enter a num: ").split())))


l = list(map(int,input("enter a num:").split()))
print(l)