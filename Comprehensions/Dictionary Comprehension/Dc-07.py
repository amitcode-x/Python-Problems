s = 'hai'
l=[10,20,30]

#OUTPUT CHAHIYE = {'H': 10,'A': 20, 'I':30}

dictval = {s[ip].upper():l[ip] for ip in range(len(s))}
print(dictval)