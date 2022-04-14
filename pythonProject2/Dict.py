#DICTIONARY
people={
    'htanaka':'Haru Tanaka',
    'ppatel':'Priya patel',
    'bagarcia':'Benjamin Alberto Garcia',
    'zmin':'Zhang min',
    'afarooqi':'Ayesha farooqi',
    'hajackson':'Hanna Jackson',
    'papatel':'Pratyush Aarav patel',
    'hrjackson':'Henry jackson',
}
print(people)


del people["htanaka"]
del people["ppatel"]
print(people)

#Tuples
Names=("Ojwang","Mike","Njery","Paule","Omolo")
print(Names)
print(len(Names))
a = list(Names)
print(a)
a.remove("Mike")
print(a)

#converting back to tuple from list
Names = tuple(a)
print(Names)

#Working with Sets
sample_set={1.98,98.9,74.96,2.5,1,16.3}
#Show the whole set
print(sample_set)

#Make a copy and shoe the copy.
ss2=sample_set
print(ss2)

# IF ELSE STATEMENTS
#a==b  #equal
#a! = b # Not equals
#a<b # less than
#a<=b #less than or equal to
#a>b #Greater than
#a>=b #Greater than or equal to

#Example1
a=33
b=200
if b>a:
 print("b is greater than a")

#Example2
 a =60
 b =90
 if a <=b:
     print("a is greater than b")
 else:
     print("b is greater than a")
     #Elif
a=33
b=33
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")

    #Ele
    a=200
    bdb=33
    print("b is grater than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater than b")
    #Short Hand if
    if a>b:print("a is greater than b")
    #Short Hand If...Else
    a=2
    b=330
    print("A") if a>b else print("B")


a=330
b=330
print("A") if a>b else print("a") if a ==b else print("B")

 #Add
a=200
b=33
c=500
if a>b and c>a:
    print("Both condition are True")

    #Nested
    x=41
    if x>10:
        print("Above ten")
        if x>20:
            print("and also above 20!")
    else:
            print("but not above 20!!")
            #The pass Statement
            a=33
            b=20
            if b>a:
                pass

#PYTHON LOOPs
i =1
while i<6:
    print(i)
    i +=1

#The break Statement


#Continue
i =0
while i<6:
    i +=1
    if i ==3:
        continue
        print(i)
#For Loops
fruits=["apple","banana","Cherry"]
for x in fruits:
    print(x)

#Loops through a String
fruits=["apple","banana","cherry"]
for x in fruits:
 if x == "banana":
     break
print(x)
#The range Function

#Nested Loops
adj=["red","big","tasty"]
fruits=["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)

#Function

r=49
p=3.142
def area():
    print(p *r*r)
area ()

# Input Marks
grade =10 #
if grade > 0 and grade <20:
    print("Fail")
elif grade >20 and grade<40:
    print("E")
elif grade >40 and grade<60:
    print("D")
elif grade > 60 and grade <80:
    print("C")
elif grade >80 and grade <100:
    print("B")
elif grade ==100:
    print("A")
else:
    print("Y")


    # Parameter Value

    def my_function(food):
        for x in food:
            print(x)
            fruits = ["apple","banana","Cherry"]
            my_function(fruits)
# Example 2

 #def my_function(x):
# return 5 * x
#print(my_function(3))
#print(my_function(5))

 # Example 3
def myfunction():
 pass

# Recursion  eatig is recursion or steps you make

def tri_recursion(k):
    if(k>0):
        result= k + tri_recursion(k-1)
        print(result)
    else:
        result = 0

    return result
print("\n\nRecursion Example Results")
tri_recursion(6)

# Lambda
x =lambda a : a+10
print(x(5))

 # Example2
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)

print(mydoubler(11))

   # Arrays

cloths=["jaket","dress","short","kaki","vest","jampa",]
x= cloths[4]
print(x)
x =len(cloths)
print(x)
x.pop(1)
print(x)













