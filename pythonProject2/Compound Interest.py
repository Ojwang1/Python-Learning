# Calculator the amount of money after 10years .Interest is 10%.
#Amount=150,000
#Interest rate=10% # Per year
a = 150000  #principal
I = 0.1    #Interest rate
Time = 10   #time in years
Total = a * ((I + 1) ** 10)

def Total():   #define a functionfor the total amount after 10 yrs
    Total = a *((I + 1) ** 10)
    return Total    #return the function

Total()          #call the function
print(Total())   #print the function


 # Example to the correct method

principleyear1 =150000
intrestyear1 =principleyear1 * 1.0
print(intrestyear1)

principleyear2= principleyear1 + intrestyear1
print(principleyear2)

intrestyear2 =principleyear2 * 0.1
print(intrestyear2)

principleyear3= principleyear2 + intrestyear2
print(principleyear3)

intrestyear3 =principleyear3 * 0.1
print(intrestyear3)

intrestyear3 =principleyear3 * 0.1
print(intrestyear3)

principleyear4 =principleyear3 + intrestyear3
print(principleyear4)

intrestyear4= principleyear4 * 0.1
print(intrestyear4)

# Write a Python that display even Number between 100 and 500
Numbers =[ 386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,
           399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,
           815,67,104,58,512,24,892,894,767,553,81,379,843,831,445,742,717,958,743,527]

for x in Numbers:
    if x ==237:
        print(x)
        break;
    elif x % 2==0:
        print(x)

        #Object Methods

class Person:
    def __init__(self, name, age):
     self.name=name
     self.age=age

p1 = Person("john", 36)
p2 = Person("Nicholas", 40)


print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)


#Create a Parent Class

class Person:
    def __init__(self, fname, lname):
         self.firstname= fname
         self.lastnmae= lname

    def printname(self):
     print(self.firstname, self.lastname)

 #Use the Person class to create an object, and then execute the printname method:

     x=Person("John", "Doe")
     x.printname()

#Create a Child Class
class Student(Person):
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
     print(self.firstname,self.lastname)

     #Add Methods
class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year
        def welcome(self):
            print("Welcome",self.firstname,self.lastname,"to the class of",self.graduationyear)
            







