# Use the Order by statement to sort the result in ascending or descending order.
# Sort the result alphabetically name:result:

import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user="root",
    passowrd="",
    database ="mydatabase"
)

mycursor=mydb.cursor()

sql ="SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult =mycursor.fetchall()

for x in myresult:
    print(x)