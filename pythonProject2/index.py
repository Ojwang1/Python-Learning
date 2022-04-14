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

x="Ojwang"
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

def tri_recursion(k):
    if(k >0):
        result =k + tri_recursion(k -1)
        print(result)
    else:
        result =0
        return  result
print("\n\nRcursion Example Results")
tri_recursion(6)


#PYTHON LAMBDA


