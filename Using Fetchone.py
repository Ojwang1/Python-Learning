# Using the fetchone () Method
# If you are only interested in one row ,you can use the fetchone () method.
# The fetchone() method will return the first row of the result:

import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user ="root",
    password ="",
    database ="mydatabase"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

print(myresult)