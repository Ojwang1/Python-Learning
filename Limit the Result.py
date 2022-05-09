# Limit the Result
# You can limit the number of records returned from the query,by using the "LIMIT" statement.

import mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT  * FROM customers LIMIT 5")

myresult =mycursor.fetchall()

for x in myresult:
    print(x)