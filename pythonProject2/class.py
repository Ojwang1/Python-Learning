f=open("class.txt")
fillecontents=f.read()
print(fillecontents)
f.close()

# Basic syntax to open ,read ,and display file contents.

f=open ('person.txt',"w")
fillecontents=f.read()
print(fillecontents)
f.write("Welcome to Kenya")
f.close()


