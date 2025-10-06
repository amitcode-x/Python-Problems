# Modifying generic perprties by using of parent by patrent class



class Father:
    bike= 'chetak'
    car ='nano'
    money=100000
mother = Father()
print(mother.money)
class Son(Father):
    bike='himalayan'
    house='2bhk'
wife=Son()
print(Son.money)
Father.money = 50000
print(Father.money)
print(mother.money)
print(Son.money)
print(wife.money)