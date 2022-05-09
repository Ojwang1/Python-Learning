# Lesson 8 try helps you to check errors within the code.

try:
    print(x)
except:
    print("An exception occurred")

# initialize variable
x=10
y=30
z=(x+y)
try:
    print(z)
except:
    print("Nicholas Nicholas")
else:
    print("is there")
finally:
    raise Exception("True")

#Example 1

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")


#Example 2

try:
  f=open("demofile.txt")
  try:
      f.write("Omondi")
      print("something went wrong")
  finally:
      f.close()
except:
    print("something went wrong when opening the file")

#Example 3
try:
    print(x)
except:
    print("Kenya is greate")
else:
    print("Uganda")
finally:
    print("Is true")
    raise Exception ("If Uganda is greater than Kenya")

# User Input

username=input("Enter username:")
print("Username is:" + username)

username=raw_input("Enter username:")
print("Username is:" + username)

# Oppening and Reading a file

f = open("Nicholas.txt")
print(f.read())

# Read Only Parts of the File.
f = open("D:\\myfile\Mind Lecture.txt","r")
print(f.read())

