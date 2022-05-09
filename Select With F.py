# Select With a Filter
# When selecting records from a table, you can filter the selection  by using the the"WHERE" statement:

import  mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user ="root",
    password="",
    database ="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = 'Apple st 652'"
mycursor.execute(sql)
myresult=mycursor.fetchall()

for x in myresult:
    print(x)

