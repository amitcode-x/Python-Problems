# Modifying generic perprties by using child class object


class Father:
    bike= 'chetak'
    car ='nano'
    money=100000
mother = Father()

class Son(Father):
    bike='himalayan'
    house='2bhk'
    
wife=Son()

wife.money = 10000
print(Father.money)
print(mother.money)
print(Son.money)
print(wife.money)