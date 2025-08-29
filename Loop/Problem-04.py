# -----For loop of dict

d = {'name':'amit','age':22}
for ele in d:
    print(ele)
for key in d:
    print(d[key])
for ele in d.items():
    print(ele)
for key, value in d.items():
    print(key, value)