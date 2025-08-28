# WAP to print give year is leap year or not

   

year = int(input('Enter a year :'))
if (year % 400==0)or (year %4 ==0 and year% 100 !=0):
    print(year,' is Leap year',year)
else:
    print(year,'is not Leap year',year)
