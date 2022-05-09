# First Example in Class 1

if 5 >2:
 print("Five is greater than two!")

x=5
y="Hellow,World!"
#Comments
print("Hellow World")

#print("Hellow ,World!")
print("Cheers,Mate!")
#Example2
x=4
y="Nicholas"
print(x) # Variable is created the moment you first assign a value to it.
print(y)

x=4
x="Sally"
print(x)

#Casting

x=str(3)
y=int(3)
z=float(3)
print(x)
print(y)

# Variable Names start with a letter not a number.
# Example
 #myvar="Beryl"
 #my_var ="Rose"

x,y,z="Orange","Banana","Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x=y=z="Orange"
print(x)
print(y)
print(z)

#Unpack a Collection

fruits=["apple","banana","cheery"]
x,y,z=fruits
print(x)
print(y)
print(z)

x="Python"
y="is"
z="awesome"
print(x,y,z)

x=5
y=10
print(x+y)

#Output Variables

x="Nicholas"
y="Nicholas"
z="awesome"
print(x,y,z)

x="Python"
y="is"
z="awesome"
print(x+y+z)

x=5
y="John"
print(x,y)
#Wrong Format
#x=5
#y="John"
#print(x+y)

#Global Variables
x="Nicholas"
def myfunc():
    print("Omondi is" + x)
    myfunc()
  #Create a variable inside a function ,with the same name as the global variable.
x="awesome"
def myfunc():
    x="fantastic"
    print("Python is" + x)
    myfunc()
    print("Python is" + x)

def myfunc():
    global x
    x="fantastic"

myfunc()
print("Pythone is" + x)
#Convert from one type to another:

x=1 # int
y=2.8 # float
z=1j  # complex

# Conver from int to float:
a=float(x)
# Conver from float to init:
b=int(y)
#Convert from int to complex
c=complex(x)
print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Assign String to Variable
a="Hellow"
print(a)

# Slicing
b="Hellow","World"
print(b[2:5])


# Python Condition and if statements

a=33
b=200
if b>a:
    print("b is greater than a")

#Elif
a=33
b=33
if b> a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")

#Else
a=200
b=33
if b > a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater than b")

#Example 2
a =200
b =33
if b >a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#Short Hand if
if a>b:print("a is greater than b")

#Short Hand if Else

a =2
b =330
print("A") if a > b else print("B")

#Add
a =200
b =33
c=500
if a>b and c>a:
    print("Both condition are true")

#Nested if statement within a if  statement
x=41

if x>10:
    print("Above ten,")
    if x >20:
        print("and also above 20!")
    else:
        print("but not above 20.")

#The pass Statement
a=33
b=200

if b > a:
    pass

#The while Loop

i =1
while i<6:
    print(i)
    i +=1

#The break Stament

i =1
while i <6:
    print(i)
    if i==3:
        break
    i +=1

#The continue Statement

i =0
while i<6:
    i += 1
    if i == 3:
        continue
        print(i)

#The else Stament

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


#Python For Loops

fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)

#Looping Through a Srring
for x in "banana":
    print(x)

#The break Statement

fruits =["apple","banana","cherry","Berry","Lemon","Orange"]
for x in fruits:
    print(x)
    if x =="Berry":
        break

#Example2

fruits =["apple","banana","cherry","Berry","Lemon","Orange"]
for x in fruits:
    if x =="Orange":
        break
        print(x)

#The Continue Statement

fruits =["apple","banana","cherry"]
for x in fruits:
    if x =="banana":
        continue
        print(x)

#The range() Function

for x in range(6):
    print(x)

#Example 2

for x in range(2,6):
    print(x)
for x in range(2,30,3):
    print(x)

#Else in For Loop

for x in range(6):
    print(x)
else:
    print("Finaly finished!")

#Example Break the loop when x is 3

for x in range(6):
    if x==3: break
    print(x)
else:
    print("Finally finished!")

#The pass Statement

for x in [0,1,2]:
    pass

#Python Function
#Creating a Function

def my_function():
    print("Hellow from a function")
my_function()

#Aegument and Parameters can used as the same thing.

def my_function(fname,lname):
    print(fname + "" + lname)
    my_function("Emil")

#Arbitary Argument ,*args call it before the name.

def my_function(*Girls):
    print("The yougest child is " + Girls[2])
my_function("Emil","Tobias","Linus")

#Passing a List as an Argument

def my_function(food):
    for x in food:
        print(x)
fruits = ["apple","banana","cherry"]
my_function(fruits)

#Return Values

def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))

print(my_function(9))

#The Pass Statement

def myfunction():
    pass

#Recursion is like eating.

#def tri_recursion(k):
 #  if(k >0):
      #  result =k + tri_recursion(k -1)
     #   print(result)
  #  else:
      #  result =0
      #  return  result
# print("\n\nRcursion Example Results")
# tri_recursion(6)


#PYTHON LAMBDA only have one way of expression.

x =lambda a: a+10
print(x(5))

x=lambda a,b,:a * b
print(x(5,6))

x=lambda a,b,c : a + b+c
print(x(5,6,2))

#Why Use Lambda Functions

def myfunc(n):
    return lambda a:a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#Example

def myfunc(n):
    return lambda a:a * n

mydoubler=myfunc(2)
mytripler=myfunc(3)

print(mydoubler(11))
print(mytripler(11))


#Python Arrays

#Python Classes/Objects Lesson 5.

def Person(param, param1):
    pass


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    p1=Person("Nicholas",36)

    print(p1.name)
    print(p1.age)

#Object Methods

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunc(self):
        print("Hellow my name is " + self.name)

    p1 =Person("Nicholas",36)
    p1.myfunc()


#Looping Through an Iterator

mytuple =("apple","banana","cherry")

for x in mytuple:
    print(x)

#Example

class MyNumbers:
    def __iter__(self):
        self.__a =1
        return self
    def __next__(self):
        x =self.a
        self.a +=1
        return x

#Example

class MyNumber:
    def __iter__(self):
        self.__a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

    myclass = MyNumbers()
    myiter = iter(myclass)


    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))

#StopIteration

class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    def __init__(self):
        if self.a <=20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

        myclass = MyNumbers()
        myiter =iter(myclass)

        for x in myiter:
            print(x)

#Local Scope

#Avariable created inside a function belongs to the local scope of the that function, and can only be used inside that function.

#Example

def myfunc():
    x = 300
    print(x)

# Function Inside Function

def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
        myinnerfunc()

    myfunc()

#Global Scope this are variables created outside of a function is global and can be used by anyone:

x = 300

def myfunc():
    print(x)
myfunc()

print(x)


# Naming Variables

x = 300

def myfunc():
    x = 200
    print(x)

myfunc()

print(x)

#Global Keyword

def myfunc():
    global x
    x = 300

myfunc()

print(x)

#Example2
x = 300
def myfunc():
    global x
    x = 200
    myfunc()
    print(x)

# LESSON 6
# what is module just created by using the import statement.

def greeting(name):
    print("Hellow," + name)

    import mymodule

    mymodule.greeting("Jonathan")

    # Variables in Module
    person1 ={
        "name":"John",
        "age" :36,
        "country":"Norway"
    }

    import mymodule

    a = mymodule.person["age"]
    print(a)

# Naming a Module

import mymodule as mx

a = mx.person1["age"]
print(a)

# Built -in Module

import platform

x = platform.system()
print(x)
 # Using the dir() Function

import platform

x = dir(platform)
print(x)

# Import From Module
def greeting(name):
    print("Hellow," + name)
person1 = {
    "name": "John",
    "age":36,
    "contry":"Norwar"
}
from mymodule import person1
print(person1["age"])

# Date Output

import datetime

x = datetime.datetime.now()
print(x)

# Example 2

import  datetime
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Creating Date Objects
import datetime
x = datetime.datetime(2020,5,17)
print(x)

# The strftime() Method

import datetime

x = datetime.datetime(2018,6,1)

print(x.strftime("%B"))

# Example
# The min and max functions can be used to find the lowest or highest value in an iterable:

x = min(5,10,25)
y = max(5,10,25)

print(x)
print(y)

# Example abs() function returns the absolute ( positive) value of the specified number:
x =abs(-7.25)

print(x)

# Example pow(x,y) function retuens the value of x to the power of y (xy)

x =pow(4,3)

print(x)


# Math Module

import  math

x = math.sqrt(64)

print(x)

# Example2

import  math
x = math.ceil(1.4)

y = math.floor(1.4)

print(x) # return 2
print(y) # return 1

# Example 3

import  math

x = math.pi

print(x)

# JSON in Python Lesson 7

# JSON is syntax for storing and exchanging data .JSON is text ,wrriten with JavaScript Object notation.

# Parse JSON -Convert from JSON to Python

import json

# some JSON:
x = '{"name":"John","age":30,"city":"New York"}'

y = json.loads(x)

# the result is a Python dictionary:

print(y["age"])

# Convert from Python to JSON

import json

x ={
    "name":"John",
    "age":30,
    "city":"New York"
}

# Convert into JSON:

y = json.dumps(x)

# the result is a JSON string:
print(y)

print(json.dumps({"name":"John","age":30}))
print(json.dumps(["apple","bananas"]))
print(json.dumps(("apple","bananas")))
print(json.dumps("hellow"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Example

x = {
    "name":"John",
    "age":30,
    "married":True,
    "divorced":False,
    "children":("Ann","Billy"),
    "pets":None,
    "cars":[
        {"model":"BMW 230","mpg": 27.5},
        {"model": "Ford Edge","mpg":24.1}
    ]
}
print(json.dumps(x))


# The findall() Function

import re

txt = "The rain in Spain"

x = re.findall("ai",txt)
print(x)

# Example

import  re

txt = "The rain in Spain"
x = re.findall("Portugal",txt)
print(x)

# The search () Function

import re

txt ="The rain in Spain"

x = re.search("\s",txt)

print("The first white-space character is located in position:",
      x.start())

 # Example

# If no matches are found, th the value None is returned:

import re

txt = "The rain Spain"
x = re.search("Portugal",txt)
print(x)

# The split() Function

import  re

txt = "The rain in Spain"
x = re.split("\s",txt)
print(x)

# Example 2

import re

txt = "The rain Spain"
x =re.split("\s",txt,1) # Split the string only at the first occurrence:
print(x)

# The sub() Function

import  re

txt = "The rain in Spain"
x = re.sub("\s","9", txt)
print(x)

#NB Replace every white-space character with the number9:
#NB You can control the number of replacements by specifying the count parameter:

#Example

import  re

txt = "The rain in Spain"
x = re.sub("\s","9",txt, 2)  # Replace the first 2 occurrences:

# Match Object

import re

txt = "The rain in Spain"
x = re.search("ai",txt)
print(x) # this will print an object

# Example2

import re

txt = "The rain in Spain"
x = re.search(r"\bs\w+",txt)
print(x.span())

#Example

import  re

txt = "The rain in Spain"

x = re.search(r"\bs\w+",txt)
print(x.string())

# Example3
import  re

txt = "The rain in Spain"

x = re.search(r"\bs\w+",txt)
print(x.group())



