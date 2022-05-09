# Select From a Table
# To select from a table in MYSQL,use the "SELECT"

import mysql.connector

mydb = mysql.connector.connect(
    host= "loclahost",
    user ="root",
    password="",
    database ="mydatabase"
)

mycursor =mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()
for x in myresult:
    print(x)
