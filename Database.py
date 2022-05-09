import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword"
)
print(mydb)

# Check if Database Exits
import mysql.connector
mydb=mysql.connector.connect(
     host="localhost",
     user="yourusername",
     password="yourpassword"
 )
mycursor =mydb.cursor()
mycursor.execute("SHOW DATABASE")

for x in mycursor:
     print(x)
     
