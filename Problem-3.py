# WAP to print give string are anagram or not


s1 = input("Enter a string: ")
s2 = input("Enter a string: ")
if sorted(s1)==sorted(s2):
    print("anagram")
else:
    print("not")


