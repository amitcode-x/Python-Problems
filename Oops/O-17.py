
class Address:

    def __init__(self,c,s,co):
        self.city=c
        self.state=s
        self.country=co
    def display_add(self):
        print(f' city name is : {self.city}')
        print(f' state name is : {self.state}')
        print(f' country name is : {self.country}')

#Banglore=Address('Banglore','Karnatka','India')

##Object method sirf object se call hota hai class se nhi ,ager hum class se call krenge to aese likhenge classname.objectmethodname(object)

#Address.display_add(Banglore)

#ager hum class se call krenge to aese likhenge classname.objectmethodname(object)

#Banglore.display_add()


class Student:
    
    def __init__(self,sN,sAge,sC):
        self.stname=sN
        self.sAge=sAge  
        self.sClass=sC
        c = input('enter city name :')   
        s= input('Enter state name :')   
        co= input('Enter country name: ')  

        #object inside of the class 
             
        ACO= Address(c,s,co)    
        self.Address=ACO  
         
    def student_details(self):
        print(f'student name is : {self.stname} ')
        print(f'student Age is : {self.sAge} ')
        print(f'student Class is : {self.sClass} ')
        self.Address.display_add() 

amit=Student('amit',22,'python')
amit.student_details()
        
        
